"""
=============================================================
  COWORKING SPACE — API REST de Autenticación
  Módulo: api.py
  Framework: Flask
=============================================================
"""

import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS


from auth import (
    AuthEventBus,
    ConsoleLogger,
    DatabaseObserver,
    EmailNotifier,
    SupabaseUserRepository,
    AuthService,
    BookingRepository,
    SpaceRepository,
)

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder=SRC_DIR, static_url_path="")
CORS(app, resources={r"/api/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]}})

@app.get("/")
def index():
    return send_from_directory(SRC_DIR, "login.html")

# Composición del sistema con Supabase
event_bus = AuthEventBus()
event_bus.subscribe(ConsoleLogger())
event_bus.subscribe(DatabaseObserver())
event_bus.subscribe(EmailNotifier())

repository = SupabaseUserRepository()  # ← 2. Conectamos el repositorio de la nube
auth_service = AuthService(repository=repository, event_bus=event_bus)
booking_repo = BookingRepository()
space_repo = SpaceRepository()

def _require_json_fields(data: dict, *fields: str):
    missing = [f for f in fields if not data.get(f)]
    if missing:
        return False, f"Campos requeridos: {', '.join(missing)}"
    return True, None


def _json_payload():
    return request.get_json(silent=True) or {}


@app.post("/api/auth/signup")
def signup():
    data = request.get_json(silent=True) or {}
    ok, err = _require_json_fields(data, "username", "email", "password", "confirm_password")
    if not ok:
        return jsonify({"success": False, "message": err, "errors": [err]}), 400

    result = auth_service.sign_up(
        username=data["username"].strip(),
        email=data["email"].strip().lower(),
        password=data["password"],
        confirm_password=data["confirm_password"],
        role=data.get("role", "member"),
    )
    status_code = 201 if result.success else 400
    return jsonify(result.to_dict()), status_code


@app.post("/api/auth/login")
def login():
    data = request.get_json(silent=True) or {}
    ok, err = _require_json_fields(data, "username", "password")
    if not ok:
        return jsonify({"success": False, "message": err, "errors": [err]}), 400

    result = auth_service.log_in(
        username=data["username"].strip(),
        password=data["password"],
    )
    status_code = 200 if result.success else 401
    return jsonify(result.to_dict()), status_code
@app.get("/api/users")

def get_all_users():
    """Endpoint para que el Dashboard obtenga la lista real de usuarios."""
    users = repository.get_all()
    # Convertimos los objetos a diccionarios, pero ocultamos el password_hash por seguridad
    users_data = []
    for u in users:
        u_dict = u.to_dict()
        users_data.append(u_dict)

    return jsonify({
        "success": True,
        "data": users_data
    }), 200


@app.patch("/api/users/<username>")
def update_user(username):
    """Actualiza campos administrativos de un usuario."""
    data = _json_payload()
    user = repository.find_by_username(username)
    if not user:
        return jsonify({"success": False, "message": "No se encontro el usuario"}), 404

    if "is_active" in data:
        user.is_active = bool(data["is_active"])

    try:
        repository.update(user)
        return jsonify({"success": True, "data": user.to_dict()}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# --- ENDPOINTS DE RESERVAS ---

@app.get("/api/bookings")
def get_bookings():
    """Devuelve todas las reservas o las de un usuario puntual."""
    try:
        username = (request.args.get("username") or "").strip()
        bookings = booking_repo.get_by_username(username) if username else booking_repo.get_all()
        return jsonify({"success": True, "data": bookings}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e), "data": []}), 500


@app.post("/api/bookings")
def create_booking():
    """Crea una solicitud de reserva pendiente de aprobacion."""
    data = _json_payload()
    ok, err = _require_json_fields(data, "username", "space_name", "booking_date", "booking_time")
    if not ok:
        return jsonify({"success": False, "message": err, "errors": [err]}), 400

    booking_data = {
        "username": data["username"].strip(),
        "space_name": data["space_name"].strip(),
        "booking_date": data["booking_date"],
        "booking_time": data["booking_time"],
        "status": data.get("status", "pendiente"),
    }

    try:
        result = booking_repo.create(booking_data)
        return jsonify({"success": True, "message": "Reserva creada correctamente.", "data": result}), 201
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# Usamos @app.route para evitar el bloqueo 405 de CORS
@app.route("/api/bookings/<booking_id>", methods=["PATCH"])
def update_booking_status(booking_id):
    """Permite al administrador aprobar o rechazar una reserva."""
    try:
        new_status = _json_payload().get("status")
        if not new_status:
            return jsonify({"success": False, "message": "Falta el estado"}), 400

        # ¡Usamos el método limpio del repositorio!
        result = booking_repo.update_status(booking_id, new_status)

        if result:
            return jsonify({"success": True, "message": f"Reserva {new_status} con éxito"}), 200
        return jsonify({"success": False, "message": "No se encontró la reserva"}), 404

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# --- ENDPOINTS PARA ESPACIOS (ABM) ---
@app.get("/api/spaces")
def get_spaces():
    """Devuelve el catalogo de espacios."""
    try:
        return jsonify({"success": True, "data": space_repo.get_all()}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e), "data": []}), 500


@app.post("/api/spaces")
def create_space():
    """Crea un nuevo espacio"""
    data = _json_payload()
    ok, err = _require_json_fields(data, "name", "type", "capacity", "price")
    if not ok:
        return jsonify({"success": False, "message": err, "errors": [err]}), 400

    try:
        # ¡Usamos el método limpio del repositorio!
        result = space_repo.create(data)
        return jsonify({"success": True, "data": result}), 201
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.put("/api/spaces/<space_id>")
def edit_space(space_id):
    """Edita un espacio existente"""
    data = _json_payload()
    if not data:
        return jsonify({"success": False, "message": "No se recibieron datos para actualizar"}), 400

    try:
        # ¡Usamos el método limpio del repositorio!
        result = space_repo.update(space_id, data)
        return jsonify({"success": True, "data": result}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
