# Documentación de Patrones de Diseño - TP1 (Nexo Coworking)

Este documento detalla los patrones de diseño aplicados en el módulo de autenticación (`src/auth.py`) del sistema de reservas Nexo Coworking, justificando su uso para resolver problemas específicos de arquitectura.

---

## 1. Patrón: Observer (Comportamiento)

**Intención:** Definir una dependencia de uno a muchos entre objetos, de manera que cuando un objeto cambie de estado, todos sus dependientes sean notificados y se actualicen automáticamente.

**Problema que resuelve en el sistema:**
Durante el proceso de autenticación (como registrar un usuario, fallar un inicio de sesión o bloquear una cuenta), el sistema necesita ejecutar múltiples acciones secundarias (ej: registrar un log en la consola, enviar un correo de bienvenida, o guardar un registro en la base de datos de auditoría). Si el servicio de autenticación (`AuthService`) llamara directamente a estas funciones, terminaría fuertemente acoplado a servicios externos, violando el Principio de Responsabilidad Única (SRP).

**Justificación de la elección:**
Se eligió el patrón Observer mediante la implementación de un `AuthEventBus`. Esto permite que el `AuthService` simplemente "publique" un evento (ej. `LOGIN_SUCCESS`) sin importarle quién lo está escuchando. Esto cumple con el Principio Abierto/Cerrado (OCP), ya que el día de mañana podemos agregar un nuevo observador (como un `EmailNotifier` o `DatabaseObserver`) sin tener que modificar ni una sola línea de código del `AuthService`.

**Ejemplo en el código (`src/auth.py`):**

```python
# El Subject (Event Bus) notifica a los observers
class AuthEventBus:
    def publish(self, event: AuthEvent) -> None:
        for observer in self._observers:
            observer.update(event)

# El Observer concreto
class ConsoleLogger(AuthObserver):
    def update(self, event: AuthEvent) -> None:
        print(f"[LOG] {event.timestamp} | {event.event_type} | {event.payload}")

# Uso en la lógica de negocio (AuthService) para notificar sin acoplarse
self._event_bus.publish(AuthEvent(
    AuthEvent.USER_REGISTERED,
    {"user_id": user.user_id, "username": username, "email": email, "role": role},
))
```

---

## 2. Patrón: Factory Method (Creacional)

**Intención:**
Define una interfaz para crear un objeto, pero deja que las subclases decidan qué clase instanciar. Permite que una clase delegue la responsabilidad de la instanciación a subclases específicas.

**Problema que resuelve en el sistema:**
En el sistema de Nexo Coworking existen diferentes perfiles de usuario: **Miembro**, **Administrador** e **Invitado**. Cada uno de estos perfiles requiere ser instanciado a partir de una clase distinta (`MemberUser`, `AdminUser`, `GuestUser`) porque a futuro manejarán permisos, atributos o comportamientos iniciales distintos. Sin este patrón, el servicio de autenticación (`AuthService`) tendría que contener bloques lógicos complejos (`if/else` o `switch`) para decidir qué tipo de objeto crear al registrar un usuario, lo que dificultaría el mantenimiento y la escalabilidad del código al agregar nuevos roles.

**Justificación de la elección:**
Se implementó mediante un registro de fábricas (`UserFactoryRegistry`) y creadores concretos como `MemberFactory` y `AdminFactory`. Esta elección permite que el proceso de registro (`sign_up`) sea totalmente agnóstico al tipo de usuario que se está creando. Si en el futuro se requiere un nuevo tipo de usuario (ej. "Empresa"), solo se debe añadir una nueva fábrica al registro sin modificar la lógica central del servicio.

**Ejemplo en el código (`src/auth.py`):**

```python
# Creador abstracto que define el método de fábrica
class UserFactory(ABC):
    @abstractmethod
    def create_user(self, user_id, username, email, password_hash) -> User:
        ...

# Creador concreto para usuarios administradores
class AdminFactory(UserFactory):
    def create_user(self, user_id, username, email, password_hash) -> AdminUser:
        return AdminUser(user_id, username, email, password_hash)

# Uso dinámico en el registro para instanciar el tipo correcto en AuthService
factory = UserFactoryRegistry.get(role) # Devuelve la fábrica correcta según el string del rol
user = factory.build(username, email, password_hash)
```
