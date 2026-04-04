"""
=============================================================
  COWORKING SPACE — Authentication Backend
  Módulo: auth.py
  Patrones: Observer, Factory Method
  + JWT + bcrypt
=============================================================
"""

from __future__ import annotations
from abc import abstractmethod

import bcrypt
import jwt
import re
import uuid
from datetime import datetime, timedelta
from typing import Any

# ---------- JWT Secret (cambiar en producción) ----------
JWT_SECRET = "nexo_coworking_super_secret_key_2025"
JWT_EXPIRATION_HOURS = 2


# ═══════════════════════════════════════════════════════════════
# SECCIÓN 1 ─ OBSERVER PATTERN (igual que tu versión)
# ═══════════════════════════════════════════════════════════════

class AuthEvent:
    USER_REGISTERED  = "USER_REGISTERED"
    LOGIN_SUCCESS    = "LOGIN_SUCCESS"
    LOGIN_FAILED     = "LOGIN_FAILED"
    ACCOUNT_LOCKED   = "ACCOUNT_LOCKED"
    PASSWORD_CHANGED = "PASSWORD_CHANGED"

    def __init__(self, event_type: str, payload: dict[str, Any]):
        self.event_type = event_type
        self.payload    = payload
        self.timestamp  = datetime.utcnow().isoformat()

    def __repr__(self) -> str:
        return f"AuthEvent(type={self.event_type}, at={self.timestamp})"


class AuthObserver:
    def update(self, event: AuthEvent) -> None:
        ...


class AuthEventBus:
    def __init__(self):
        self._observers: list[AuthObserver] = []

    def subscribe(self, observer: AuthObserver) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer: AuthObserver) -> None:
        self._observers = [o for o in self._observers if o is not observer]

    def publish(self, event: AuthEvent) -> None:
        for observer in self._observers:
            observer.update(event)


class ConsoleLogger(AuthObserver):
    def update(self, event: AuthEvent) -> None:
        print(f"[LOG] {event.timestamp} | {event.event_type} | {event.payload}")


class DatabaseObserver(AuthObserver):
    def update(self, event: AuthEvent) -> None:
        # ── INTEGRAR BD ──
        pass


class EmailNotifier(AuthObserver):
    def update(self, event: AuthEvent) -> None:
        if event.event_type == AuthEvent.USER_REGISTERED:
            username = event.payload.get("username", "")
            # ── INTEGRAR EMAIL ──
            pass


# ═══════════════════════════════════════════════════════════════
# SECCIÓN 2 ─ MODELOS DE USUARIO
# ═══════════════════════════════════════════════════════════════

class User:
    def __init__(
        self,
        user_id:       str,
        username:      str,
        email:         str,
        password_hash: str,
        role:          str,
    ):
        self.user_id       = user_id
        self.username      = username
        self.email         = email
        self.password_hash = password_hash
        self.role          = role
        self.is_active     = True
        self.created_at    = datetime.utcnow().isoformat()
        self.failed_attempts: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "user_id":    self.user_id,
            "username":   self.username,
            "email":      self.email,
            "role":       self.role,
            "is_active":  self.is_active,
            "created_at": self.created_at,
        }


class MemberUser(User):
    def __init__(self, user_id, username, email, password_hash):
        super().__init__(user_id, username, email, password_hash, role="member")


class AdminUser(User):
    def __init__(self, user_id, username, email, password_hash):
        super().__init__(user_id, username, email, password_hash, role="admin")


class GuestUser(User):
    def __init__(self, user_id, username, email, password_hash):
        super().__init__(user_id, username, email, password_hash, role="guest")


# ═══════════════════════════════════════════════════════════════
# SECCIÓN 3 ─ FACTORY METHOD
# ═══════════════════════════════════════════════════════════════

class UserFactory:
    @abstractmethod
    def create_user(self, user_id, username, email, password_hash) -> User:
        """Create a user with the given parameters."""
        ...

    def build(self, username, email, password_hash) -> User:
        user_id = str(uuid.uuid4())
        return self.create_user(user_id, username, email, password_hash)


class MemberFactory(UserFactory):
    def create_user(self, user_id, username, email, password_hash) -> MemberUser:
        return MemberUser(user_id, username, email, password_hash)


class AdminFactory(UserFactory):
    def create_user(self, user_id, username, email, password_hash) -> AdminUser:
        return AdminUser(user_id, username, email, password_hash)


class GuestFactory(UserFactory):
    def create_user(self, user_id, username, email, password_hash) -> GuestUser:
        return GuestUser(user_id, username, email, password_hash)


class UserFactoryRegistry:
    _factories: dict[str, UserFactory] = {
        "member": MemberFactory(),
        "admin":  AdminFactory(),
        "guest":  GuestFactory(),
    }

    @classmethod
    def get(cls, role: str) -> UserFactory:
        factory = cls._factories.get(role.lower())
        if not factory:
            raise ValueError(f"Rol desconocido: '{role}'. Disponibles: {list(cls._factories)}")
        return factory

    @classmethod
    def register(cls, role: str, factory: UserFactory) -> None:
        cls._factories[role.lower()] = factory


# ═══════════════════════════════════════════════════════════════
# SECCIÓN 4 ─ REPOSITORIO
# ═══════════════════════════════════════════════════════════════

class UserRepository:
    def save(self, user: User) -> None: ...
    def find_by_username(self, username: str) -> User | None: ...
    def find_by_email(self, email: str) -> User | None: ...
    def update(self, user: User) -> None: ...


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._store: dict[str, User] = {}

    def save(self, user: User) -> None:
        self._store[user.username] = user

    def find_by_username(self, username: str) -> User | None:
        return self._store.get(username)

    def find_by_email(self, email: str) -> User | None:
        return next((u for u in self._store.values() if u.email == email), None)

    def update(self, user: User) -> None:
        if user.username in self._store:
            self._store[user.username] = user


# ═══════════════════════════════════════════════════════════════
# SECCIÓN 5 ─ VALIDACIONES
# ═══════════════════════════════════════════════════════════════

class PasswordPolicy:
    MIN_LENGTH = 8

    @classmethod
    def validate(cls, password: str) -> tuple[bool, list[str]]:
        errors = []
        if len(password) < cls.MIN_LENGTH:
            errors.append(f"Debe tener al menos {cls.MIN_LENGTH} caracteres.")
        if not re.search(r"[A-Z]", password):
            errors.append("Debe contener al menos una letra mayúscula.")
        if not re.search(r"[a-z]", password):
            errors.append("Debe contener al menos una letra minúscula.")
        if not re.search(r"\d", password):
            errors.append("Debe contener al menos un número.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            errors.append("Debe contener al menos un carácter especial.")
        return (len(errors) == 0, errors)


class InputValidator:
    @staticmethod
    def is_valid_username(username: str) -> tuple[bool, str]:
        if not username or len(username) < 3:
            return False, "El nombre de usuario debe tener al menos 3 caracteres."
        if len(username) > 30:
            return False, "El nombre de usuario no puede superar los 30 caracteres."
        if not re.match(r"^[a-zA-Z0-9_]+$", username):
            return False, "Solo se permiten letras, números y guiones bajos."
        return True, ""

    @staticmethod
    def is_valid_email(email: str) -> tuple[bool, str]:
        pattern = r"^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, email):
            return False, "Formato de email inválido."
        return True, ""

    @staticmethod
    def passwords_match(password: str, confirm: str) -> tuple[bool, str]:
        if password != confirm:
            return False, "Las contraseñas no coinciden."
        return True, ""


# ═══════════════════════════════════════════════════════════════
# SECCIÓN 6 ─ HASHING CON BCRYPT
# ═══════════════════════════════════════════════════════════════

class PasswordHasher:
    @staticmethod
    def hash(plain_password: str) -> str:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(plain_password.encode('utf-8'), salt).decode('utf-8')

    @staticmethod
    def verify(plain_password: str, hashed: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed.encode('utf-8'))


# ═══════════════════════════════════════════════════════════════
# SECCIÓN 7 ─ RESULTADO
# ═══════════════════════════════════════════════════════════════

class AuthResult:
    def __init__(
        self,
        success: bool,
        message: str,
        data: dict[str, Any] | None = None,
        errors: list[str] | None = None,
    ):
        self.success = success
        self.message = message
        self.data    = data or {}
        self.errors  = errors or []

    def to_dict(self) -> dict[str, Any]:
        return {
            "success": self.success,
            "message": self.message,
            "data":    self.data,
            "errors":  self.errors,
        }


# ═══════════════════════════════════════════════════════════════
# SECCIÓN 8 ─ AUTH SERVICE (con JWT)
# ═══════════════════════════════════════════════════════════════

class AuthService:
    MAX_FAILED_ATTEMPTS = 5

    def __init__(self, repository: UserRepository, event_bus: AuthEventBus):
        self._repo      = repository
        self._event_bus = event_bus

    def sign_up(self, username: str, email: str, password: str,
                confirm_password: str, role: str = "member") -> AuthResult:
        # Validaciones
        valid, err = InputValidator.is_valid_username(username)
        if not valid:
            return AuthResult(False, "Datos inválidos.", errors=[err])

        valid, err = InputValidator.is_valid_email(email)
        if not valid:
            return AuthResult(False, "Datos inválidos.", errors=[err])

        valid, err = InputValidator.passwords_match(password, confirm_password)
        if not valid:
            return AuthResult(False, "Las contraseñas no coinciden.", errors=[err])

        valid, policy_errors = PasswordPolicy.validate(password)
        if not valid:
            return AuthResult(False, "Contraseña no cumple la política.", errors=policy_errors)

        if self._repo.find_by_username(username):
            return AuthResult(False, "El nombre de usuario ya está en uso.", errors=["Usuario duplicado."])

        if self._repo.find_by_email(email):
            return AuthResult(False, "El email ya está registrado.", errors=["Email duplicado."])

        # Hash con bcrypt
        password_hash = PasswordHasher.hash(password)

        try:
            factory = UserFactoryRegistry.get(role)
        except ValueError as exc:
            return AuthResult(False, str(exc))

        user = factory.build(username, email, password_hash)
        self._repo.save(user)

        self._event_bus.publish(AuthEvent(
            AuthEvent.USER_REGISTERED,
            {"user_id": user.user_id, "username": username, "email": email, "role": role},
        ))

        return AuthResult(True, "Cuenta creada exitosamente.", data=user.to_dict())

    def log_in(self, username: str, password: str) -> AuthResult:
        user = self._repo.find_by_username(username)
        if not user:
            self._event_bus.publish(AuthEvent(AuthEvent.LOGIN_FAILED, {"username": username}))
            return AuthResult(False, "Credenciales inválidas.")

        if not user.is_active:
            return AuthResult(False, "La cuenta está desactivada.")

        if user.failed_attempts >= self.MAX_FAILED_ATTEMPTS:
            self._event_bus.publish(AuthEvent(AuthEvent.ACCOUNT_LOCKED, {"username": username}))
            return AuthResult(False, "Cuenta bloqueada por demasiados intentos fallidos.")

        if not PasswordHasher.verify(password, user.password_hash):
            user.failed_attempts += 1
            self._repo.update(user)
            self._event_bus.publish(AuthEvent(
                AuthEvent.LOGIN_FAILED,
                {"username": username, "attempts": user.failed_attempts},
            ))
            remaining = self.MAX_FAILED_ATTEMPTS - user.failed_attempts
            return AuthResult(False, f"Contraseña incorrecta. Intentos restantes: {remaining}.")

        # Login exitoso: resetear intentos y generar JWT
        user.failed_attempts = 0
        self._repo.update(user)

        # Crear token JWT
        payload = {
            "user_id": user.user_id,
            "username": user.username,
            "email": user.email,
            "role": user.role,
            "exp": datetime.utcnow() + timedelta(hours=JWT_EXPIRATION_HOURS)
        }
        token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")

        self._event_bus.publish(AuthEvent(
            AuthEvent.LOGIN_SUCCESS,
            {"user_id": user.user_id, "username": username, "role": user.role},
        ))

        # Incluir token y datos del usuario en la respuesta
        user_data = user.to_dict()
        user_data["token"] = token
        return AuthResult(True, "Inicio de sesión exitoso.", data=user_data)
