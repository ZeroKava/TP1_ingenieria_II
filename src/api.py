"""
=============================================================
  COWORKING SPACE — API REST de Autenticación
  Módulo: api.py
  Framework: Flask
=============================================================
"""

from flask import Flask, request, jsonify
from flask_cors import CORS

from auth import (
    AuthEventBus,
    ConsoleLogger,
    DatabaseObserver,
    EmailNotifier,
    SQLiteUserRepository,
    AuthService,
)

app = Flask(__name__)
CORS(app)

# Composición del sistema con SQLite
event_bus = AuthEventBus()
event_bus.subscribe(ConsoleLogger())
event_bus.subscribe(DatabaseObserver())
event_bus.subscribe(EmailNotifier())

repository = SQLiteUserRepository()          # ← persiste en coworking_auth.db
auth_service = AuthService(repository=repository, event_bus=event_bus)


def _require_json_fields(data: dict, *fields: str):
    missing = [f for f in fields if not data.get(f)]
    if missing:
        return False, f"Campos requeridos: {', '.join(missing)}"
    return True, None


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


if __name__ == "__main__":
    app.run(debug=True, port=5000)
