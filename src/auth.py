"""
=============================================================
  COWORKING SPACE — Authentication Backend
  Módulo: auth.py
  Patrones: Observer, Factory Method
  Autor: (tu nombre)
=============================================================

ESTRUCTURA:
  - Observer Pattern  → notificaciones de eventos de auth
  - Factory Method    → creación de distintos tipos de usuario
  - AuthService       → lógica central de negocio (login / signup)

PUNTOS DE EXTENSIÓN MARCADOS CON: # ── EXTENSIBLE ──
"""

from __future__ import annotations

import hashlib
import re
import uuid
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any


# ═══════════════════════════════════════════════════════════════
# SECCIÓN 1 ─ OBSERVER PATTERN
# ═══════════════════════════════════════════════════════════════

class AuthEvent:
    """Evento emitido por el sistema de autenticación."""

    # Tipos de evento disponibles
    USER_REGISTERED  = "USER_REGISTERED"
    LOGIN_SUCCESS    = "LOGIN_SUCCESS"
    LOGIN_FAILED     = "LOGIN_FAILED"
    ACCOUNT_LOCKED   = "ACCOUNT_LOCKED"
    PASSWORD_CHANGED = "PASSWORD_CHANGED"
    # ── EXTENSIBLE ── agrega aquí nuevos tipos de evento

    def __init__(self, event_type: str, payload: dict[str, Any]):
        self.event_type = event_type
        self.payload    = payload
        self.timestamp  = datetime.utcnow().isoformat()

    def __repr__(self) -> str:
        return f"AuthEvent(type={self.event_type}, at={self.timestamp})"


class AuthObserver(ABC):
    """Interfaz base para cualquier observer de eventos de auth."""

    @abstractmethod
    def update(self, event: AuthEvent) -> None:
        """Recibe y procesa un evento de autenticación."""
        ...


class AuthEventBus:
    """
    Bus de eventos (Subject del patrón Observer).
    Desacopla al AuthService de sus efectos secundarios.
    """

    def __init__(self):
        self._observers: list[AuthObserver] = []

    def subscribe(self, observer: AuthObserver) -> None:
        """Registra un observer."""
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer: AuthObserver) -> None:
        """Elimina un observer."""
        self._observers = [o for o in self._observers if o is not observer]

    def publish(self, event: AuthEvent) -> None:
        """Notifica a todos los observers registrados."""
        for observer in self._observers:
            observer.update(event)


# ── EXTENSIBLE ── Implementaciones concretas de observers ──────

class ConsoleLogger(AuthObserver):
    """Observer de consola — útil en desarrollo."""

    def update(self, event: AuthEvent) -> None:
        print(f"[LOG] {event.timestamp} | {event.event_type} | {event.payload}")


class DatabaseObserver(AuthObserver):
    """
    Observer para persistir eventos en la base de datos.
    ── PUNTO DE INTEGRACIÓN DE BASE DE DATOS ──
    Implementa aquí la lógica de persistencia.
    """

    def update(self, event: AuthEvent) -> None:
        # ── INTEGRAR BD ── ejemplo:
        # db.insert("auth_events", {
        #     "type":      event.event_type,
        #     "payload":   event.payload,
        #     "timestamp": event.timestamp,
        # })
        pass  # ← reemplaza con tu lógica de BD


class EmailNotifier(AuthObserver):
    """
    Observer para enviar emails transaccionales.
    ── EXTENSIBLE ── conecta tu servicio de email aquí.
    """

    def update(self, event: AuthEvent) -> None:
        if event.event_type == AuthEvent.USER_REGISTERED:
            username = event.payload.get("username", "")
            # ── INTEGRAR EMAIL ──
            # email_service.send_welcome(username)
            pass


# ═══════════════════════════════════════════════════════════════
# SECCIÓN 2 ─ MODELOS DE USUARIO
# ═══════════════════════════════════════════════════════════════

class User:
    """Modelo base de usuario del sistema coworking."""

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
        """Serializa el usuario (sin exponer la contraseña)."""
        return {
            "user_id":    self.user_id,
            "username":   self.username,
            "email":      self.email,
            "role":       self.role,
            "is_active":  self.is_active,
            "created_at": self.created_at,
        }

    def __repr__(self) -> str:
        return f"User(username={self.username}, role={self.role})"


class MemberUser(User):
    """Usuario estándar — puede reservar espacios."""

    def __init__(self, user_id, username, email, password_hash):
        super().__init__(user_id, username, email, password_hash, role="member")


class AdminUser(User):
    """
    Administrador — gestiona espacios y usuarios.
    ── EXTENSIBLE ── agrega permisos administrativos aquí.
    """

    def __init__(self, user_id, username, email, password_hash):
        super().__init__(user_id, username, email, password_hash, role="admin")


class GuestUser(User):
    """
    Usuario invitado — acceso de solo lectura.
    ── EXTENSIBLE ── limita capacidades según política.
    """

    def __init__(self, user_id, username, email, password_hash):
        super().__init__(user_id, username, email, password_hash, role="guest")


# ═══════════════════════════════════════════════════════════════
# SECCIÓN 3 ─ FACTORY METHOD PATTERN
# ═══════════════════════════════════════════════════════════════

class UserFactory(ABC):
    """
    Creator abstracto del patrón Factory Method.
    Cada subclase decide qué tipo de User construye.
    """

    @abstractmethod
    def create_user(
        self,
        username:      str,
        email:         str,
        password_hash: str,
    ) -> User:
        """Factory method: construye y devuelve un User."""
        ...

    def build(
        self,
        username:      str,
        email:         str,
        password_hash: str,
    ) -> User:
        """
        Template method: coordina la creación.
        Llama internamente al factory method.
        """
        user_id = str(uuid.uuid4())
        return self.create_user(user_id, username, email, password_hash)


class MemberFactory(UserFactory):
    """Crea usuarios de tipo Member."""

    def create_user(self, user_id, username, email, password_hash) -> MemberUser:
        return MemberUser(user_id, username, email, password_hash)


class AdminFactory(UserFactory):
    """Crea usuarios de tipo Admin."""

    def create_user(self, user_id, username, email, password_hash) -> AdminUser:
        return AdminUser(user_id, username, email, password_hash)


class GuestFactory(UserFactory):
    """Crea usuarios de tipo Guest."""

    def create_user(self, user_id, username, email, password_hash) -> GuestUser:
        return GuestUser(user_id, username, email, password_hash)


class UserFactoryRegistry:
    """
    Registro central de factories.
    ── EXTENSIBLE ── registra nuevos roles sin tocar AuthService.
    """

    _factories: dict[str, UserFactory] = {
        "member": MemberFactory(),
        "admin":  AdminFactory(),
        "guest":  GuestFactory(),
        # ── EXTENSIBLE ── "enterprise": EnterpriseFactory()
    }

    @classmethod
    def get(cls, role: str) -> UserFactory:
        factory = cls._factories.get(role.lower())
        if not factory:
            raise ValueError(f"Rol desconocido: '{role}'. Disponibles: {list(cls._factories)}")
        return factory

    @classmethod
    def register(cls, role: str, factory: UserFactory) -> None:
        """Permite registrar factories externas en tiempo de ejecución."""
        cls._factories[role.lower()] = factory


# ═══════════════════════════════════════════════════════════════
# SECCIÓN 4 ─ REPOSITORIO DE USUARIOS (INTERFAZ BD)
# ═══════════════════════════════════════════════════════════════

class UserRepository(ABC):
    """
    Interfaz del repositorio — abstrae el storage de usuarios.
    ── PUNTO DE INTEGRACIÓN DE BASE DE DATOS ──
    Implementa esta interfaz con tu ORM / driver de BD.
    """

    @abstractmethod
    def save(self, user: User) -> None: ...

    @abstractmethod
    def find_by_username(self, username: str) -> User | None: ...

    @abstractmethod
    def find_by_email(self, email: str) -> User | None: ...

    @abstractmethod
    def update(self, user: User) -> None: ...


class InMemoryUserRepository(UserRepository):
    """
    Repositorio en memoria — SOLO para desarrollo / testing.
    Reemplaza con DatabaseUserRepository cuando integres tu BD.
    """

    def __init__(self):
        self._store: dict[str, User] = {}  # username → User

    def save(self, user: User) -> None:
        self._store[user.username] = user

    def find_by_username(self, username: str) -> User | None:
        return self._store.get(username)

    def find_by_email(self, email: str) -> User | None:
        return next(
            (u for u in self._store.values() if u.email == email),
            None,
        )

    def update(self, user: User) -> None:
        if user.username in self._store:
            self._store[user.username] = user

    # ── EXTENSIBLE ── DatabaseUserRepository ──────────────────
    #
    # class DatabaseUserRepository(UserRepository):
    #     def __init__(self, db_connection):
    #         self.db = db_connection
    #
    #     def save(self, user: User) -> None:
    #         self.db.execute(
    #             "INSERT INTO users (id, username, email, password_hash, role) "
    #             "VALUES (?, ?, ?, ?, ?)",
    #             (user.user_id, user.username, user.email,
    #              user.password_hash, user.role)
    #         )
    #
    #     def find_by_username(self, username: str) -> User | None:
    #         row = self.db.execute(
    #             "SELECT * FROM users WHERE username = ?", (username,)
    #         ).fetchone()
    #         return self._row_to_user(row) if row else None
    #
    #     ... (implementa find_by_email y update similarmente)


# ═══════════════════════════════════════════════════════════════
# SECCIÓN 5 ─ VALIDACIONES
# ═══════════════════════════════════════════════════════════════

class PasswordPolicy:
    """
    Centraliza las reglas de contraseña.
    ── EXTENSIBLE ── ajusta MIN_LENGTH y regex según política.
    """

    MIN_LENGTH = 8

    @classmethod
    def validate(cls, password: str) -> tuple[bool, list[str]]:
        """
        Valida la contraseña contra la política.
        Devuelve (es_válida, lista_de_errores).
        """
        errors: list[str] = []

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

        # ── EXTENSIBLE ── agrega más reglas aquí

        return (len(errors) == 0, errors)


class InputValidator:
    """Validaciones de formato para inputs del formulario."""

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
# SECCIÓN 6 ─ HASHING DE CONTRASEÑA
# ═══════════════════════════════════════════════════════════════

class PasswordHasher:
    """
    Utilidad para hashear y verificar contraseñas.
    ── EXTENSIBLE ── reemplaza SHA-256 con bcrypt/argon2 en producción.
    """

    @staticmethod
    def hash(plain_password: str) -> str:
        """Devuelve el hash SHA-256 de la contraseña."""
        return hashlib.sha256(plain_password.encode()).hexdigest()

    @staticmethod
    def verify(plain_password: str, hashed: str) -> bool:
        """Compara la contraseña plana contra el hash almacenado."""
        return hashlib.sha256(plain_password.encode()).hexdigest() == hashed

    # ── EXTENSIBLE ── ejemplo con bcrypt:
    # import bcrypt
    # @staticmethod
    # def hash(plain_password: str) -> str:
    #     return bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt()).decode()
    # @staticmethod
    # def verify(plain_password: str, hashed: str) -> bool:
    #     return bcrypt.checkpw(plain_password.encode(), hashed.encode())


# ═══════════════════════════════════════════════════════════════
# SECCIÓN 7 ─ RESULTADO GENÉRICO
# ═══════════════════════════════════════════════════════════════

class AuthResult:
    """Encapsula el resultado de cualquier operación de auth."""

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
# SECCIÓN 8 ─ AUTH SERVICE (núcleo del sistema)
# ═══════════════════════════════════════════════════════════════

class AuthService:
    """
    Servicio central de autenticación.
    Orquesta validaciones, factory, repositorio y eventos.
    """

    MAX_FAILED_ATTEMPTS = 5  # ── EXTENSIBLE ── ajusta según política

    def __init__(
        self,
        repository: UserRepository,
        event_bus:  AuthEventBus,
    ):
        self._repo      = repository
        self._event_bus = event_bus

    # ─────────────────────────────────────────────────────────
    # CASO DE USO 1: SIGN UP — Registro / validación de cuenta
    # ─────────────────────────────────────────────────────────

    def sign_up(
        self,
        username:         str,
        email:            str,
        password:         str,
        confirm_password: str,
        role:             str = "member",
    ) -> AuthResult:
        """
        Registra un nuevo usuario.
        Valida inputs → hashea → crea con factory → persiste → notifica.
        """

        # 1. Validar username
        valid, err = InputValidator.is_valid_username(username)
        if not valid:
            return AuthResult(False, "Datos inválidos.", errors=[err])

        # 2. Validar email
        valid, err = InputValidator.is_valid_email(email)
        if not valid:
            return AuthResult(False, "Datos inválidos.", errors=[err])

        # 3. Comprobar que las contraseñas coincidan
        valid, err = InputValidator.passwords_match(password, confirm_password)
        if not valid:
            return AuthResult(False, "Las contraseñas no coinciden.", errors=[err])

        # 4. Validar política de contraseña
        valid, policy_errors = PasswordPolicy.validate(password)
        if not valid:
            return AuthResult(False, "Contraseña no cumple la política.", errors=policy_errors)

        # 5. Verificar unicidad de username
        if self._repo.find_by_username(username):
            return AuthResult(False, "El nombre de usuario ya está en uso.", errors=["Usuario duplicado."])

        # 6. Verificar unicidad de email
        if self._repo.find_by_email(email):
            return AuthResult(False, "El email ya está registrado.", errors=["Email duplicado."])

        # 7. Hashear contraseña
        password_hash = PasswordHasher.hash(password)

        # 8. Crear usuario con Factory Method
        try:
            factory = UserFactoryRegistry.get(role)
        except ValueError as exc:
            return AuthResult(False, str(exc))

        user = factory.build(username, email, password_hash)

        # 9. Persistir
        self._repo.save(user)

        # 10. Publicar evento (Observer notifica a BD, email, etc.)
        self._event_bus.publish(AuthEvent(
            AuthEvent.USER_REGISTERED,
            {"user_id": user.user_id, "username": username, "email": email, "role": role},
        ))

        return AuthResult(
            True,
            "Cuenta creada exitosamente.",
            data=user.to_dict(),
        )

    # ─────────────────────────────────────────────────────────
    # CASO DE USO 2: LOG IN — Inicio de sesión
    # ─────────────────────────────────────────────────────────

    def log_in(self, username: str, password: str) -> AuthResult:
        """
        Autentica a un usuario existente.
        Busca → verifica cuenta → verifica contraseña → notifica.
        """

        # 1. Buscar usuario
        user = self._repo.find_by_username(username)
        if not user:
            self._event_bus.publish(AuthEvent(
                AuthEvent.LOGIN_FAILED,
                {"username": username, "reason": "Usuario no encontrado"},
            ))
            return AuthResult(False, "Credenciales inválidas.")

        # 2. Verificar si la cuenta está activa
        if not user.is_active:
            return AuthResult(False, "La cuenta está desactivada.")

        # 3. Verificar bloqueo por intentos fallidos
        if user.failed_attempts >= self.MAX_FAILED_ATTEMPTS:
            self._event_bus.publish(AuthEvent(
                AuthEvent.ACCOUNT_LOCKED,
                {"username": username},
            ))
            return AuthResult(False, "Cuenta bloqueada por demasiados intentos fallidos.")

        # 4. Verificar contraseña
        if not PasswordHasher.verify(password, user.password_hash):
            user.failed_attempts += 1
            self._repo.update(user)
            self._event_bus.publish(AuthEvent(
                AuthEvent.LOGIN_FAILED,
                {"username": username, "reason": "Contraseña incorrecta",
                 "attempts": user.failed_attempts},
            ))
            remaining = self.MAX_FAILED_ATTEMPTS - user.failed_attempts
            return AuthResult(
                False,
                f"Contraseña incorrecta. Intentos restantes: {remaining}.",
            )

        # 5. Login exitoso — resetear intentos fallidos
        user.failed_attempts = 0
        self._repo.update(user)

        # 6. Publicar evento
        self._event_bus.publish(AuthEvent(
            AuthEvent.LOGIN_SUCCESS,
            {"user_id": user.user_id, "username": username, "role": user.role},
        ))

        # ── EXTENSIBLE ── aquí podrías generar un JWT / session token:
        # token = TokenService.generate(user)
        # return AuthResult(True, "Inicio de sesión exitoso.", data={"token": token, **user.to_dict()})

        return AuthResult(
            True,
            "Inicio de sesión exitoso.",
            data=user.to_dict(),
        )
