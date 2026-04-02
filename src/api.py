"""
=============================================================
  COWORKING SPACE — API REST de Autenticación
  Módulo: api.py
  Framework: Flask
=============================================================

ENDPOINTS:
  POST /api/auth/signup  → Registro de cuenta
  POST /api/auth/login   → Inicio de sesión

CORS habilitado para que tu frontend HTML pueda consumirlo.
Instala dependencias:  pip install flask flask-cors
"""

from flask import Flask, request, jsonify
from flask_cors import CORS

from auth import (
    AuthService,
    AuthEventBus,
    ConsoleLogger,
    DatabaseObserver,
    EmailNotifier,
    InMemoryUserRepository,
    # ── INTEGRAR BD ── reemplaza InMemoryUserRepository con:
    # DatabaseUserRepository
)


# ═══════════════════════════════════════════════════════════════
# CONFIGURACIÓN DE LA APLICACIÓN
# ═══════════════════════════════════════════════════════════════

app = Flask(__name__)
CORS(app)  # permite peticiones desde tu frontend HTML

# ── COMPOSICIÓN DEL SISTEMA ────────────────────────────────────

event_bus  = AuthEventBus()

# Registra los observers que necesitas
event_bus.subscribe(ConsoleLogger())
event_bus.subscribe(DatabaseObserver())  # ← conecta tu BD aquí
event_bus.subscribe(EmailNotifier())

# ── INTEGRAR BD ── sustituye el repositorio en memoria:
# from db import get_db_connection
# repository = DatabaseUserRepository(get_db_connection())
repository = InMemoryUserRepository()

auth_service = AuthService(repository=repository, event_bus=event_bus)


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════

def _require_json_fields(data: dict, *fields: str):
    """Devuelve (True, None) si todos los campos están presentes."""
    missing = [f for f in fields if not data.get(f)]
    if missing:
        return False, f"Campos requeridos: {', '.join(missing)}"
    return True, None


# ═══════════════════════════════════════════════════════════════
# ENDPOINTS
# ═══════════════════════════════════════════════════════════════

@app.post("/api/auth/signup")
def signup():
    """
    Registro de nueva cuenta.

    Body JSON esperado:
    {
        "username":         "john_doe",
        "email":            "john@example.com",
        "password":         "Secret1!",
        "confirm_password": "Secret1!",
        "role":             "member"   ← opcional, default "member"
    }
    """
    data = request.get_json(silent=True) or {}

    ok, err = _require_json_fields(data, "username", "email", "password", "confirm_password")
    if not ok:
        return jsonify({"success": False, "message": err, "errors": [err]}), 400

    result = auth_service.sign_up(
        username=         data["username"].strip(),
        email=            data["email"].strip().lower(),
        password=         data["password"],
        confirm_password= data["confirm_password"],
        role=             data.get("role", "member"),
    )

    status_code = 201 if result.success else 400
    return jsonify(result.to_dict()), status_code


@app.post("/api/auth/login")
def login():
    """
    Inicio de sesión.

    Body JSON esperado:
    {
        "username": "john_doe",
        "password": "Secret1!"
    }
    """
    data = request.get_json(silent=True) or {}

    ok, err = _require_json_fields(data, "username", "password")
    if not ok:
        return jsonify({"success": False, "message": err, "errors": [err]}), 400

    result = auth_service.log_in(
        username= data["username"].strip(),
        password= data["password"],
    )

    status_code = 200 if result.success else 401
    return jsonify(result.to_dict()), status_code


# ── EXTENSIBLE ── agrega aquí más endpoints (logout, reset-password, etc.)


# ═══════════════════════════════════════════════════════════════
# ENTRY POINT
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    app.run(debug=True, port=5000)
