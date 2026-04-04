"""
test.py - Pruebas para el auth.py original (con JWT, sin bloqueo de cuenta)
Ejecutar: python test.py
"""

import unittest
from auth import (
    AuthService, AuthEventBus, InMemoryUserRepository,
    PasswordHasher, UserFactory, ConsoleLogger,
    User
)

# ---------- Helper ----------
def create_valid_user(service):
    return service.sign_up(
        email="test@cowork.com",
        password="Segura1!",
        user_type="member"
    )

class TestPasswordHasher(unittest.TestCase):
    def test_hash_and_verify(self):
        hashed = PasswordHasher.hash_password("Segura1!")
        self.assertTrue(PasswordHasher.verify_password("Segura1!", hashed))

    def test_wrong_password_fails(self):
        hashed = PasswordHasher.hash_password("Segura1!")
        self.assertFalse(PasswordHasher.verify_password("Incorrecta1!", hashed))

    def test_password_strength_valid(self):
        self.assertTrue(PasswordHasher.validate_password_strength("Segura1!"))
        self.assertFalse(PasswordHasher.validate_password_strength("weak"))
        self.assertFalse(PasswordHasher.validate_password_strength("SoloMayuscula1"))
        self.assertFalse(PasswordHasher.validate_password_strength("sin mayuscula1!"))


class TestUserFactory(unittest.TestCase):
    def test_member_creation(self):
        user = UserFactory.create_user("member", "m@x.com", "hash")
        self.assertEqual(user.user_type, "member")
        self.assertEqual(user.email, "m@x.com")

    def test_admin_creation(self):
        user = UserFactory.create_user("admin", "a@x.com", "hash")
        self.assertEqual(user.user_type, "admin")

    def test_guest_creation(self):
        user = UserFactory.create_user("guest", "g@x.com", "hash")
        self.assertEqual(user.user_type, "guest")

    def test_invalid_type_raises(self):
        with self.assertRaises(ValueError):
            UserFactory.create_user("alien", "x@x.com", "hash")


class TestAuthServiceSignUp(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryUserRepository()
        self.bus = AuthEventBus()
        self.service = AuthService(self.repo, self.bus, PasswordHasher(), "test_secret")

    def test_successful_signup(self):
        user = self.service.sign_up("new@example.com", "Segura1!", "member")
        self.assertEqual(user.email, "new@example.com")
        self.assertEqual(user.user_type, "member")
        found = self.repo.find_by_email("new@example.com")
        self.assertIsNotNone(found)

    def test_duplicate_email_raises(self):
        self.service.sign_up("dup@example.com", "Segura1!", "member")
        with self.assertRaises(ValueError) as ctx:
            self.service.sign_up("dup@example.com", "Segura1!", "member")
        self.assertIn("ya está registrado", str(ctx.exception))

    def test_weak_password_raises(self):
        with self.assertRaises(ValueError) as ctx:
            self.service.sign_up("weak@example.com", "1234", "member")
        self.assertIn("no cumple los requisitos", str(ctx.exception))


class TestAuthServiceLogin(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryUserRepository()
        self.bus = AuthEventBus()
        self.service = AuthService(self.repo, self.bus, PasswordHasher(), "test_secret")
        self.service.sign_up("login@example.com", "Segura1!", "member")

    def test_successful_login_returns_token(self):
        token = self.service.log_in("login@example.com", "Segura1!")
        self.assertIsInstance(token, str)
        self.assertGreater(len(token), 10)

    def test_wrong_password_raises(self):
        with self.assertRaises(ValueError) as ctx:
            self.service.log_in("login@example.com", "wrong")
        self.assertIn("Credenciales inválidas", str(ctx.exception))

    def test_nonexistent_user_raises(self):
        with self.assertRaises(ValueError):
            self.service.log_in("ghost@example.com", "Segura1!")


class TestObserverPattern(unittest.TestCase):
    def test_event_bus_emits_events(self):
        bus = AuthEventBus()
        class TestObserver:
            def __init__(self):
                self.events = []
            def update(self, event_type, data):
                self.events.append((event_type, data))
        obs = TestObserver()
        bus.subscribe("USER_REGISTERED", obs)
        bus.emit("USER_REGISTERED", {"email": "test@x.com"})
        self.assertEqual(len(obs.events), 1)
        self.assertEqual(obs.events[0][0], "USER_REGISTERED")

    def test_console_logger_exists(self):
        logger = ConsoleLogger()
        bus = AuthEventBus()
        bus.subscribe("LOGIN_SUCCESS", logger)
        bus.emit("LOGIN_SUCCESS", {})
        # No assertion, solo que no lance excepción


if __name__ == "__main__":
    unittest.main(verbosity=2)
