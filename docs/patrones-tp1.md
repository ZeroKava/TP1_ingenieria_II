# Documentación de Patrones de Diseño - Nexo Coworking

## 1. Patrón: Observer (Comportamiento)

**Intención:** Definir una dependencia de uno a muchos entre objetos, de manera que cuando un objeto cambie de estado, todos sus dependientes sean notificados y se actualicen automáticamente.

**Problema que resuelve en el sistema:**
Durante el proceso de autenticación (como registrar un usuario, fallar un inicio de sesión o bloquear una cuenta), el sistema necesita ejecutar múltiples acciones secundarias (ej: registrar un log en la consola, enviar un correo de bienvenida, o guardar un registro en la base de datos de auditoría). Si el servicio de autenticación (`AuthService`) llamara directamente a estas funciones, terminaría fuertemente acoplado a servicios externos, violando el Principio de Responsabilidad Única (SRP).

**Justificación de la elección:**
Se eligió el patrón Observer mediante la implementación de un `AuthEventBus`. Esto permite que el `AuthService` simplemente "publique" un evento (ej. `LOGIN_SUCCESS`) sin importarle quién lo está escuchando. Esto cumple con el Principio Abierto/Cerrado (OCP), ya que el día de mañana podemos agregar un nuevo observador (como un `EmailNotifier`) sin tener que modificar ni una sola línea de código del `AuthService`.

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

# Uso en la lógica de negocio (AuthService)
self._event_bus.publish(AuthEvent(
    AuthEvent.USER_REGISTERED,
    {"user_id": user.user_id, "username": username, "email": email, "role": role},
))
## Patrón: Factory Method (Creacional)

**Intención:**
[cite_start]Define una interfaz para crear un objeto, pero deja que las subclases decidan qué clase instanciar[cite: 4, 13]. [cite_start]Permite que una clase delegue la responsabilidad de la instanciación a subclases específicas[cite: 13].

**Problema que resuelve en el sistema:**
[cite_start]En el sistema de Nexo Coworking existen diferentes perfiles de usuario: **Miembro**, **Administrador** e **Invitado**[cite: 4, 13]. [cite_start]Cada uno de estos perfiles tiene atributos o comportamientos iniciales distintos[cite: 4, 13]. [cite_start]Sin este patrón, el servicio de autenticación (`AuthService`) tendría que contener bloques lógicos complejos (`if/else` o `switch`) para decidir qué tipo de objeto crear, lo que dificultaría el mantenimiento y la escalabilidad del código al agregar nuevos roles[cite: 4, 13].

**Justificación de la elección:**
[cite_start]Se implementó mediante un registro de fábricas (`UserFactoryRegistry`) y creadores concretos como `MemberFactory` y `AdminFactory`[cite: 4, 13]. [cite_start]Esta elección permite que el proceso de registro (`sign_up`) sea agnóstico al tipo de usuario que se está creando[cite: 4, 13]. [cite_start]Si en el futuro se requiere un nuevo tipo de usuario (ej. "Empresa"), solo se debe añadir una nueva fábrica al registro sin modificar la lógica central del servicio[cite: 13].

**Ejemplo en el código (`src/auth.py`):**

```python
# [cite_start]Creador abstracto que define el método de fábrica [cite: 4, 13]
class UserFactory(ABC):
    @abstractmethod
    def create_user(self, user_id, username, email, password_hash) -> User:
        ...

# [cite_start]Creador concreto para usuarios administradores [cite: 4, 13]
class AdminFactory(UserFactory):
    def create_user(self, user_id, username, email, password_hash) -> AdminUser:
        return AdminUser(user_id, username, email, password_hash)

# [cite_start]Uso dinámico en el registro para instanciar el tipo correcto [cite: 4, 13]
factory = UserFactoryRegistry.get(role)
user = factory.build(username, email, password_hash)
