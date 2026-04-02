"""
=============================================================
  COWORKING SPACE — Tests de Autenticación
  Módulo: tests.py
  Ejecutar:  python tests.py
=============================================================
"""

import unittest
from auth import (
    AuthService, AuthEventBus, AuthEvent, AuthObserver,
    InMemoryUserRepository, PasswordPolicy, InputValidator,
    PasswordHasher, UserFactoryRegistry,
)


# ── Observer de prueba ─────────────────────────────────────────

class TestObserver(AuthObserver):
    def __init__(self):
        self.received: list[AuthEvent] = []

    def update(self, event: AuthEvent) -> None:
        self.received.append(event)


# ── Fixture base ───────────────────────────────────────────────

def make_service():
    bus     = AuthEventBus()
    obs     = TestObserver()
    bus.subscribe(obs)
    repo    = InMemoryUserRepository()
    service = AuthService(repository=repo, event_bus=bus)
    return service, obs


VALID_USER = {
    "username":         "juan_dev",
    "email":            "juan@cowork.com",
    "password":         "Segura1!",
    "confirm_password": "Segura1!",
}


# ═══════════════════════════════════════════════════════════════
# TESTS
# ═══════════════════════════════════════════════════════════════

class TestPasswordPolicy(unittest.TestCase):

    def test_valid_password(self):
        ok, errs = PasswordPolicy.validate("Segura1!")
        self.assertTrue(ok)
        self.assertEqual(errs, [])

    def test_too_short(self):
        ok, errs = PasswordPolicy.validate("Ab1!")
        self.assertFalse(ok)
        self.assertTrue(any("caracteres" in e for e in errs))

    def test_no_uppercase(self):
        ok, errs = PasswordPolicy.validate("segura1!")
        self.assertFalse(ok)

    def test_no_number(self):
        ok, errs = PasswordPolicy.validate("Seguraa!")
        self.assertFalse(ok)

    def test_no_special(self):
        ok, errs = PasswordPolicy.validate("Segura12")
        self.assertFalse(ok)


class TestInputValidator(unittest.TestCase):

    def test_valid_username(self):
        ok, _ = InputValidator.is_valid_username("juan_dev")
        self.assertTrue(ok)

    def test_short_username(self):
        ok, _ = InputValidator.is_valid_username("ab")
        self.assertFalse(ok)

    def test_invalid_username_chars(self):
        ok, _ = InputValidator.is_valid_username("ju an!")
        self.assertFalse(ok)

    def test_valid_email(self):
        ok, _ = InputValidator.is_valid_email("juan@cowork.com")
        self.assertTrue(ok)

    def test_invalid_email(self):
        ok, _ = InputValidator.is_valid_email("not-an-email")
        self.assertFalse(ok)

    def test_passwords_match(self):
        ok, _ = InputValidator.passwords_match("Segura1!", "Segura1!")
        self.assertTrue(ok)

    def test_passwords_mismatch(self):
        ok, _ = InputValidator.passwords_match("Segura1!", "Otra1!")
        self.assertFalse(ok)


class TestPasswordHasher(unittest.TestCase):

    def test_hash_and_verify(self):
        hashed = PasswordHasher.hash("Segura1!")
        self.assertTrue(PasswordHasher.verify("Segura1!", hashed))

    def test_wrong_password_fails(self):
        hashed = PasswordHasher.hash("Segura1!")
        self.assertFalse(PasswordHasher.verify("Incorrecta1!", hashed))


class TestUserFactory(unittest.TestCase):

    def test_member_factory(self):
        factory = UserFactoryRegistry.get("member")
        user = factory.build("test", "t@t.com", "hash")
        self.assertEqual(user.role, "member")

    def test_admin_factory(self):
        factory = UserFactoryRegistry.get("admin")
        user = factory.build("admin", "a@t.com", "hash")
        self.assertEqual(user.role, "admin")

    def test_unknown_role_raises(self):
        with self.assertRaises(ValueError):
            UserFactoryRegistry.get("superalien")


class TestSignUp(unittest.TestCase):

    def test_successful_registration(self):
        svc, obs = make_service()
        r = svc.sign_up(**VALID_USER)
        self.assertTrue(r.success)
        self.assertEqual(r.data["username"], "juan_dev")
        self.assertEqual(r.data["role"], "member")

    def test_observer_notified_on_signup(self):
        svc, obs = make_service()
        svc.sign_up(**VALID_USER)
        types = [e.event_type for e in obs.received]
        self.assertIn(AuthEvent.USER_REGISTERED, types)

    def test_duplicate_username(self):
        svc, _ = make_service()
        svc.sign_up(**VALID_USER)
        r = svc.sign_up(**VALID_USER)
        self.assertFalse(r.success)

    def test_duplicate_email(self):
        svc, _ = make_service()
        svc.sign_up(**VALID_USER)
        r = svc.sign_up(
            username="otro_user", email="juan@cowork.com",
            password="Segura1!", confirm_password="Segura1!"
        )
        self.assertFalse(r.success)

    def test_password_mismatch(self):
        svc, _ = make_service()
        r = svc.sign_up(
            username="juan_dev", email="juan@cowork.com",
            password="Segura1!", confirm_password="Distinta1!"
        )
        self.assertFalse(r.success)

    def test_weak_password(self):
        svc, _ = make_service()
        r = svc.sign_up(
            username="juan_dev", email="juan@cowork.com",
            password="1234", confirm_password="1234"
        )
        self.assertFalse(r.success)

    def test_invalid_email(self):
        svc, _ = make_service()
        r = svc.sign_up(
            username="juan_dev", email="no-es-email",
            password="Segura1!", confirm_password="Segura1!"
        )
        self.assertFalse(r.success)


class TestLogIn(unittest.TestCase):

    def _register(self, svc):
        svc.sign_up(**VALID_USER)

    def test_successful_login(self):
        svc, obs = make_service()
        self._register(svc)
        r = svc.log_in("juan_dev", "Segura1!")
        self.assertTrue(r.success)
        types = [e.event_type for e in obs.received]
        self.assertIn(AuthEvent.LOGIN_SUCCESS, types)

    def test_wrong_password(self):
        svc, obs = make_service()
        self._register(svc)
        r = svc.log_in("juan_dev", "Incorrecta1!")
        self.assertFalse(r.success)
        types = [e.event_type for e in obs.received]
        self.assertIn(AuthEvent.LOGIN_FAILED, types)

    def test_nonexistent_user(self):
        svc, _ = make_service()
        r = svc.log_in("fantasma", "Segura1!")
        self.assertFalse(r.success)

    def test_account_locked_after_max_attempts(self):
        svc, obs = make_service()
        self._register(svc)
        for _ in range(AuthService.MAX_FAILED_ATTEMPTS):
            svc.log_in("juan_dev", "Incorrecta1!")
        r = svc.log_in("juan_dev", "Segura1!")  # contraseña correcta pero bloqueado
        self.assertFalse(r.success)
        types = [e.event_type for e in obs.received]
        self.assertIn(AuthEvent.ACCOUNT_LOCKED, types)

    def test_failed_attempts_reset_after_success(self):
        svc, _ = make_service()
        self._register(svc)
        svc.log_in("juan_dev", "Incorrecta1!")  # 1 intento fallido
        r = svc.log_in("juan_dev", "Segura1!")  # login correcto
        self.assertTrue(r.success)
        # el usuario debe tener 0 intentos fallidos nuevamente
        repo = svc._repo
        user = repo.find_by_username("juan_dev")
        self.assertEqual(user.failed_attempts, 0)


class TestObserverPattern(unittest.TestCase):

    def test_multiple_observers(self):
        bus  = AuthEventBus()
        obs1 = TestObserver()
        obs2 = TestObserver()
        bus.subscribe(obs1)
        bus.subscribe(obs2)

        event = AuthEvent(AuthEvent.LOGIN_SUCCESS, {"username": "test"})
        bus.publish(event)

        self.assertEqual(len(obs1.received), 1)
        self.assertEqual(len(obs2.received), 1)

    def test_unsubscribe(self):
        bus = AuthEventBus()
        obs = TestObserver()
        bus.subscribe(obs)
        bus.unsubscribe(obs)

        bus.publish(AuthEvent(AuthEvent.LOGIN_SUCCESS, {}))
        self.assertEqual(len(obs.received), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
