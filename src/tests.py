"""
test.py - Pruebas actualizadas para el auth.py de Nexo Coworking
Patrones evaluados: Factory Method y Observer
Ejecutar: python tests.py
"""

import unittest
from auth import (
    AuthService, AuthEventBus, InMemoryUserRepository,
    PasswordHasher, PasswordPolicy, UserFactoryRegistry, ConsoleLogger,
    AuthEvent
)

class TestPasswordHasherAndPolicy(unittest.TestCase):
    def test_hash_and_verify(self):
        hashed = PasswordHasher.hash("Segura1!")
        self.assertTrue(PasswordHasher.verify("Segura1!", hashed))

    def test_wrong_password_fails(self):
        hashed = PasswordHasher.hash("Segura1!")
        self.assertFalse(PasswordHasher.verify("Incorrecta1!", hashed))

    def test_password_strength_valid(self):
        # Ahora PasswordPolicy devuelve una tupla (bool, lista_de_errores)
        is_valid, _ = PasswordPolicy.validate("Segura1!")
        self.assertTrue(is_valid)
        
        is_valid, _ = PasswordPolicy.validate("weak")
        self.assertFalse(is_valid)
        
        is_valid, _ = PasswordPolicy.validate("SoloMayuscula1")
        self.assertFalse(is_valid)

class TestUserFactory(unittest.TestCase):
    def test_member_creation(self):
        # Ahora usamos el Registry del patrón Factory Method
        factory = UserFactoryRegistry.get("member")
        user = factory.build("miembro_test", "m@x.com", "hash123")
        self.assertEqual(user.role, "member")
        self.assertEqual(user.email, "m@x.com")

    def test_invalid_type_raises(self):
        with self.assertRaises(ValueError):
            UserFactoryRegistry.get("alien")

class TestAuthServiceSignUp(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryUserRepository()
        self.bus = AuthEventBus()
        # AuthService ahora solo necesita repo y bus
        self.service = AuthService(self.repo, self.bus)

    def test_successful_signup(self):
        result = self.service.sign_up(
            username="newuser", 
            email="new@example.com", 
            password="Password1!", 
            confirm_password="Password1!", 
            role="member"
        )
        self.assertTrue(result.success)
        self.assertEqual(result.data["role"], "member")
        
        # Verificar que se guardó en el repositorio
        found = self.repo.find_by_username("newuser")
        self.assertIsNotNone(found)

    def test_duplicate_username_fails(self):
        self.service.sign_up("user1", "uno@example.com", "Segura1!", "Segura1!", "member")
        result = self.service.sign_up("user1", "dos@example.com", "Segura1!", "Segura1!", "member")
        
        self.assertFalse(result.success)
        self.assertIn("Usuario duplicado", result.errors[0])

    def test_passwords_do_not_match(self):
        result = self.service.sign_up("userX", "x@x.com", "Segura1!", "Distinta2@", "member")
        self.assertFalse(result.success)
        self.assertIn("Las contraseñas no coinciden", result.message)

class TestAuthServiceLogin(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryUserRepository()
        self.bus = AuthEventBus()
        self.service = AuthService(self.repo, self.bus)
        self.service.sign_up("loginuser", "login@example.com", "Segura1!", "Segura1!", "member")

    def test_successful_login_returns_token(self):
        result = self.service.log_in("loginuser", "Segura1!")
        self.assertTrue(result.success)
        self.assertIn("token", result.data) # El JWT debe estar en la data

    def test_wrong_password_fails(self):
        result = self.service.log_in("loginuser", "wrong_password")
        self.assertFalse(result.success)
        self.assertIn("Contraseña incorrecta", result.message)

    def test_nonexistent_user_fails(self):
        result = self.service.log_in("fantasma", "Segura1!")
        self.assertFalse(result.success)
        self.assertEqual(result.message, "Credenciales inválidas.")

class TestObserverPattern(unittest.TestCase):
    def test_event_bus_publishes_events(self):
        bus = AuthEventBus()
        
        # Creamos un observador espía para el test
        class TestObserver:
            def __init__(self):
                self.events_received = []
            def update(self, event):
                self.events_received.append(event)
                
        espia = TestObserver()
        bus.subscribe(espia)
        
        # Publicamos un evento estructurado
        evento_prueba = AuthEvent(AuthEvent.USER_REGISTERED, {"email": "test@x.com"})
        bus.publish(evento_prueba)
        
        self.assertEqual(len(espia.events_received), 1)
        self.assertEqual(espia.events_received[0].event_type, AuthEvent.USER_REGISTERED)

if __name__ == "__main__":
    unittest.main(verbosity=2)
