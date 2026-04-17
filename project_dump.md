# 📁 Estructura del Proyecto

```
┣ design
┃ ┗ prototipo.md
┣ docs
┃ ┣ AI_LOG-SpicyTech.md
┃ ┣ Contingency  plan.md
┃ ┣ Contrato-de-SpicyTech.md
┃ ┣ Matriz de Riesgos SpicyTech.xlsx.pdf
┃ ┣ Matriz-de-Riesgos-SpicyTech.md
┃ ┗ patrones-tp1.md
┣ dump.js
┣ package.json
┣ README.md
┣ src
┃ ┣ api.py
┃ ┣ app.js
┃ ┣ auth.py
┃ ┣ home.html
┃ ┣ login.html
┃ ┗ tests.py
┗ tests
  ┗ test.md
```

# 📄 Contenido de Archivos

## C:\Users\User\Desktop\TP1_ingenieria_II\design\prototipo.md

```md

```

## C:\Users\User\Desktop\TP1_ingenieria_II\docs\AI_LOG-SpicyTech.md

```md
## Entrada 001 — Semana 1

**Fecha:** 19/03/2026
**Herramienta:** Gemini
**Responsable:** Scrum Master — Octavio García
**Eje temático:** Eje 1

**¿Para qué se usó?**
Definir la estructura inicial de gestión del proyecto (Sprint 0), incluyendo la configuración del tablero Kanban, la redacción del Contrato de Proyecto y la elaboración de la Matriz de Riesgos.

**¿Qué generó la IA?**
1. Una lista de 9 tarjetas para el backlog inicial con descripción y responsables.
2. Un borrador del Contrato de Proyecto con 4 secciones (Escenario, Metodología, Roles y Acuerdos).
3. Una tabla de Matriz de Riesgos con 6 ítems específicos para un sistema de coworking.

**¿Qué aceptamos tal cual?**
La justificación técnica de la metodología Scrum y la estructura de la Matriz de Riesgos (columnas de Impacto, Probabilidad y Mitigación).

**¿Qué modificamos y por qué?**
- **Nombre de la empresa:** Cambiamos el nombre sugerido por "SpicyTech" para alinearlo con la identidad definida por el grupo.
- **Roles y Acuerdos:** Completamos los nombres reales de los integrantes y definimos horarios de reunión específicos (Discord/WhatsApp) según la disponibilidad real del equipo.
- **Mitigación de riesgos:** Ajustamos el plan de mitigación del riesgo de "Concurrencia" para enfocarnos específicamente en bloqueos de base de datos, que es el enfoque técnico que discutió el equipo.

**¿Qué descartamos y por qué?**
Decidimos enfocarnos solo en el núcleo de reservas para no exceder el alcance del cuatrimestre y asegurar la calidad de las funcionalidades básicas.

## Entrada 002 — Semana 3

**Fecha:** 02/04/2026
**Herramienta:** Claude
**Responsable:** Dev Lead — Matías Polcowñuk
**Eje temático:** Eje 1

**¿Para qué se usó?**
Para crear el Back End del sistema en general.

**¿Qué generó la IA?**
1. La carpeta api.py, para combinar back end con front end.
2. La carpeta auth.py para autentificar al usuario en el login.
3. La carpeta tests.py pruebas del código.

**¿Qué aceptamos tal cual?**
El código base del Back End.
**¿Qué modificamos y por qué?**
- **Front End:** Vamos a agregarlo para su correcto funcionamiento.
- **Base de Datos:** Fusionarlo con el código.

**¿Qué descartamos y por qué?**
Por el momento el código funciona correctamente, así que no es necesario el descarte de nada.

## Entrada 003 — Semana 3

**Fecha:** 03/04/2026
**Herramienta:** Gemini
**Responsable:** QA Lead — Jesus Emanuel De Olivera
**Eje temático:** Eje 2 / Integración y Pruebas

**¿Para qué se usó?**
Integrar el Front y Back, aplicar seguridad (Bcrypt/JWT) y asegurar que las pruebas (`tests.py`) pasen sin errores.

**¿Qué generó la IA?**
Un backend seguro (`auth.py`, `api.py`), el JS necesario para consumir la API y un entorno 100% compatible con nuestros tests.

**¿Qué aceptamos tal cual?**
La lógica de encriptación (Bcrypt), el manejo de sesiones (JWT) y el formato de respuesta JSON.

**¿Qué modificamos y por qué?**
Bloqueamos los cambios de diseño. Forzamos a la IA a mantener nuestro código HTML/CSS original, inyectando únicamente el JS necesario para conectar ambas partes y no perder nuestro trabajo.

**¿Qué descartamos y por qué?**
Descartamos la interfaz visual que propuso la IA y su idea de validar contraseñas solo en el backend (decidimos mantener nuestra validación visual en tiempo real en el frontend para mejorar la UX).

```

## C:\Users\User\Desktop\TP1_ingenieria_II\docs\Contingency  plan.md

```md
# Plan de Gestión de Riesgos del Proyecto

Este documento detalla la Matriz de Riesgos identificada para el desarrollo del proyecto, alineada con los hallazgos visuales. Incluye las estrategias de mitigación (preventivas) y los planes de contingencia (reactivos).

## Resumen de Clasificación

Para la evaluación y visualización de los riesgos, se utiliza la siguiente escala de severidad, tal como se muestra en la matriz gráfica del proyecto:

* **Bajo (Verde):** Puntuaciones 1-3.
* **Medio (Amarillo/Naranja claro):** Puntuaciones 4-6.
* **Alto (Naranja oscuro):** Puntuaciones 8-12.
* **Extremo (Rojo):** Puntuaciones 15-25.

---

## 1. Matriz de Riesgos y Mitigación

Esta matriz identifica los eventos potenciales y establece acciones preventivas para reducir su probabilidad o impacto *antes* de que ocurran.

| # | Nombre del Riesgo | Categoría | Probabilidad | Impacto (Severidad Visual) | Plan de Mitigación (Preventivo) |
| :-: | :--- | :---: | :---: | :---: | :--- |
| **1** | **Falta de experiencia en React de Dev Leaders**: Retraso en calendario de reservas dinámico. | Técnicos | **Alta** | **Medio** (4-6) | Realizar una semana de investigación y prototipado rápido (PoC) enfocado en gestión de estados de React. |
| **2** | **Indisponibilidad por exámenes parciales**: Coincidencia de fechas de exámenes, reduciendo capacidad en Sprint 1. | Equipo | **Alta** | **Alto** (8-10) | Actualizar el tablero Kanban semanalmente y adelantar entregas críticas antes de las semanas de exámenes. |
| **3** | **Ambigüedad en reglas de negocio**: Retrabajo en backend por definición difusa de cancelaciones y reembolsos. | Requisitos | Media | **Alto** (12) | Mantener reuniones constantes con el docente para validar que las reglas de negocio sean claras y precisas. |
| **4** | **Dependencia de hosting gratuito**: Suspensión por inactividad (Render/Railway), dificultando pruebas y demo. | Externo | Media | **Medio** (12) | Configurar un sistema de logs de errores y realizar backups periódicos para asegurar disponibilidad. |
| **5** | **Conflictos de Concurrencia (Doble Reserva)**: Falta de conocimiento técnico para implementar bloqueos (locks) de BD. | Técnicos | Baja | **Alto/Extremo** (10-25) | Implementar validaciones estrictas en el backend antes de confirmar una reserva y capacitar al equipo en locks de BD. |

---

## 2. Plan de Contingencia

Este plan define las acciones inmediatas a tomar *una vez que el riesgo ha ocurrido* para minimizar los daños y recuperar el control del proyecto.

### 🚨 R1. Falta de experiencia en React
* **Disparador:** Tareas de gestión de estado bloqueadas o retrasos críticos detectados tras la primera semana de PoC.
* **Acción Inmediata:**
    1.  **Simplificar MVP:** Reúnase con stakeholders/docente para acordar una reducción drástica del alcance técnico de la gestión de estados. Sustituir lógicas complejas por soluciones simples o "hardcodeadas".
    2.  **Asignar Dueños:** Dividir el desarrollo por módulos y nombrar al miembro con más conocimiento como "dueño" técnico para centralizar y resolver bloqueos de React del equipo.
    3.  **Adaptar Código Verificado:** Priorizar el uso de repositorios de ejemplo o *boilerplates* verificados para React en lugar de programar arquitecturas base desde cero.

### 🚨 R2. Indisponibilidad por exámenes parciales
* **Disparador:** Miembros clave del equipo reportan incapacidad total de trabajo o baja drástica de productividad durante la semana crítica de entrega.
* **Acción Inmediata:**
    1.  **Congelar No Críticos:** Detener inmediatamente el pulido visual y las *features* secundarias. Cero recursos dedicados a ellas.
    2.  **Foco en *Happy Path*:** Redistribuir el esfuerzo limitado *exclusivamente* en asegurar que los flujos principales de usuario funcionen para la entrega (MVP).
    3.  **Consumir Reserva:** Utilizar la reserva de tiempo final (buffer) planificada para pruebas como tiempo de desarrollo ahora.
    4.  **Notificar:** Avisar preventivamente al docente sobre la entrega parcial debido a la baja disponibilidad del equipo.

### 🚨 R3. Ambigüedad en reglas de negocio
* **Disparador:** Identificación de retrabajo significativo en el backend o lógica de negocio que no cumple con las expectativas a mitad del desarrollo.
* **Acción Inmediata:**
    1.  **Detener Desarrollo:** Parar inmediatamente el desarrollo en la lógica afectada hasta tener claridad. Mover tareas a una lista de "Por Validar".
    2.  **Validación con Docente:** Programar una reunión de emergencia con el docente para re-definir y aclarar las reglas de negocio ambiguas. Obtener aprobación por escrito si es posible.
    3.  **Actualizar Documentación:** Reflejar inmediatamente los cambios en la documentación de requisitos y comunicarlos a todo el equipo para evitar futuros retrabajos.

### 🚨 R4. Dependencia de hosting gratuito
* **Disparador:** Detección de tiempos de inactividad o fallos en las pruebas integrales y demo debido a suspensión del hosting Render/Railway.
* **Acción Inmediata:**
    1.  **Diagnosticar:** Analizar logs de errores y alertas para hallar la causa raíz de la inactividad.
    2.  **Ejecutar Plan de Backups:** Iniciar inmediatamente el proceso de restore de la base de datos y/o archivos de aplicación desde el backup periódico más reciente.
    3.  **Prevenir Daño Circular:** Asegurar que el código de la aplicación o configuración no causará un nuevo fallo antes de reactivar el servicio. Si es necesario, configurar alertas adicionales.

### 🚨 R5. Conflictos de Concurrencia (Doble Reserva)
* **Disparador:** Reportes de usuarios de reservas duplicadas o detección visual de la severidad del riesgo alcanzando el nivel Alto/Extremo.
* **Acción Inmediata:**
    1.  **Congelar Confirmaciones:** Bloquear temporalmente nuevas confirmaciones en el backend (mantener el sistema en modo solo lectura).
    2.  **Identificar y Mediar:** Consultar la base de datos para hallar duplicados. Aplicar regla "primero en llegar": mantener la primera reserva, cancelar la segunda.
    3.  **Notificar y Compensar:** Informar inmediatamente a ambos usuarios. Ofrecer disculpas y una alternativa inmediata (otra fecha/recurso) al usuario cancelado.
    4.  **Parche Técnico:** Implementar un *fix* de emergencia (e.g., cola de mensajes, caché distribuida) o acelerar la capacitación y aplicación de locks de BD antes de reabrir el sistema.

```

## C:\Users\User\Desktop\TP1_ingenieria_II\docs\Contrato-de-SpicyTech.md

```md
Contrato de Proyecto - SpicyTech.

Sistema de Gestión de Reservas para Coworking

1. Escenario elegido y justificación
Seleccionamos el sistema de reservas para un espacio de Coworking debido a la necesidad crítica de resolver conflictos de disponibilidad en tiempo real. Actualmente, la gestión manual genera errores de doble reserva y falta de visibilidad para los usuarios finales. Nuestro objetivo es centralizar la gestión de recursos (escritorios, salas de reuniones y oficinas) permitiendo un control automatizado. Esta solución optimizará el uso del espacio físico y mejorará significativamente la experiencia de los miembros. Al ser un sistema con alta concurrencia, representa un desafío técnico ideal para aplicar los conceptos de Ingeniería de Software II.

2. Metodología de desarrollo y justificación técnica
Implementaremos el marco de trabajo Scrum debido a su enfoque iterativo e incremental, lo cual es fundamental para cumplir con las entregas de la cátedra. Esta metodología nos permite dividir el sistema en Sprints, asegurando que las funcionalidades críticas (como el motor de reservas) se validen tempranamente. La estructura de roles facilitará una división de tareas clara y una responsabilidad compartida sobre la calidad del producto final. Utilizaremos ceremonias de inspección y adaptación para ajustar el alcance del MVP según el progreso del equipo. El uso de Scrum garantiza una trazabilidad total mediante el tablero Kanban y el control de versiones en GitHub.

3. Roles asignados
**Scrum Master: [Octavio García]

**Dev Leader: [Polcowñuk Matias]

**QA Lead: [De Olivera Jesus]

**QA Lead: [Calamari Santino]

**UX Lead: [Manrique Santiago]

4. Acuerdos de trabajo del equipo
El equipo se reunirá de forma sincrónica todos los días habiles de la sena a las [09:00 hs] vía Discord para coordinar avances. Se establece una frecuencia de commits mínima de tres veces por semana para asegurar la integración continua. Para que una tarea pase a "Done", el código debe estar testeado y revisado por al menos un compañero (Tester). La comunicación oficial será por vía WhatsApp, con un tiempo de respuesta esperado menor a 2 horas. Cualquier impedimento técnico debe ser comunicado de inmediato al Scrum Master para su gestión.

```

## C:\Users\User\Desktop\TP1_ingenieria_II\docs\Matriz-de-Riesgos-SpicyTech.md

```md
# Matriz de Riesgos - Proyecto Coworking (UCP Inc.)

Esta matriz identifica los eventos que podrían afectar el desarrollo del proyecto y establece planes de acción preventivos.

| Riesgo | Impacto | Probabilidad | Plan de Mitigación 

| **Conflictos de Concurrencia (Doble Reserva)** | Alto | Media | Implementar bloqueos (locks) a nivel de base de datos y validaciones estrictas en el backend antes de confirmar. |

| **Curva de aprendizaje del Stack Tecnológico** | Medio | Alta | Realizar una semana de investigación y prototipado rápido (PoC) antes de empezar la implementación del MVP. |

| **Indisponibilidad por exámenes parciales** | Medio | Alta | Actualizar el tablero Kanban semanalmente y adelantar entregas críticas antes de las semanas de exámenes. |

| **Falla en la persistencia de datos** | Alto | Baja | Implementar un sistema de logs de errores y realizar backups periódicos de la base de datos de desarrollo. |

| **Desviación del alcance (Scope Creep)** | Bajo | Media | Mantener reuniones constantes con el docente para validar que las funcionalidades no excedan los requisitos de la materia. |

| **Inconsistencias en el diseño de UI/UX** | Bajo | Baja | Utilizar un sistema de diseño o biblioteca de componentes estándar (como Material UI o Tailwind) para mantener coherencia. |

### Clasificación de Impacto y Probabilidad:
* **Impacto:** Bajo, Medio, Alto.
* **Probabilidad:** Baja, Media, Alta.

[borrador-riesgos.md.xlsx](https://github.com/user-attachments/files/26157397/borrador-riesgos.md.xlsx)


```

## C:\Users\User\Desktop\TP1_ingenieria_II\docs\patrones-tp1.md

```md
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

```

## C:\Users\User\Desktop\TP1_ingenieria_II\dump.js

```js
const fs = require('fs');
const path = require('path');

// 1. Adaptado para Nexo Coworking (Python, Web, Markdown)
const allowedExtensions = ['.py', '.js', '.html', '.css', '.md'];

// 2. Carpetas prohibidas (¡Para que no colapse la IA!)
const ignoreDirs = ['node_modules', '.git', '__pycache__', 'venv', 'env'];

function generateTree(dir, prefix = '') {
  if (!fs.existsSync(dir)) return '';
  const entries = fs.readdirSync(dir);
  let tree = '';

  entries.forEach((entry, index) => {
    const fullPath = path.join(dir, entry);
    
    // Ignorar carpetas pesadas
    if (ignoreDirs.includes(entry)) return;

    const isLast = index === entries.length - 1;
    const connector = isLast ? '┗' : '┣';
    const subPrefix = prefix + (isLast ? '  ' : '┃ ');

    tree += `${prefix}${connector} ${entry}\n`;

    if (fs.statSync(fullPath).isDirectory()) {
      tree += generateTree(fullPath, subPrefix);
    }
  });
  return tree;
}

function walk(dir, fileList = []) {
  if (!fs.existsSync(dir)) return fileList;

  fs.readdirSync(dir).forEach(file => {
    const fullPath = path.join(dir, file);
    const stat = fs.statSync(fullPath);

    if (stat.isDirectory()) {
      if (!ignoreDirs.includes(file)) {
        walk(fullPath, fileList);
      }
    } else {
      const ext = path.extname(fullPath);
      if (allowedExtensions.includes(ext)) {
        const content = fs.readFileSync(fullPath, 'utf8');
        // Ajuste estético para Python en Markdown
        const lang = ext === '.py' ? 'python' : ext.slice(1);
        fileList.push(`## ${fullPath}\n\n\`\`\`${lang}\n${content}\n\`\`\`\n`);
      }
    }
  });
  return fileList;
}

// Escanea todo el proyecto desde la raíz
const targetPath = path.join(__dirname, '.');
const tree = generateTree(targetPath);
const files = walk(targetPath);

const markdown = `# 📁 Estructura del Proyecto\n\n\`\`\`\n${tree}\`\`\`\n\n# 📄 Contenido de Archivos\n\n${files.join('\n')}`;

// Guarda el archivo
fs.writeFileSync(path.join(__dirname, 'project_dump.md'), markdown);
console.log('✅ Contexto generado con éxito: project_dump.md');
```

## C:\Users\User\Desktop\TP1_ingenieria_II\README.md

```md
# Sistema de Reservas para Espacios de Coworking
**Grupo:** SpicyTech 
**Proyecto:** Sistema de Reservas UCP 
**Materia:** Ingeniería de Software II · UCP · 2026

---

## Descripción del Proyecto
Este sistema permite a los miembros de un espacio de coworking reservar salas y escritorios de forma eficiente a través de una interfaz web, eliminando conflictos de doble reserva. El software gestiona la disponibilidad en tiempo real, permite bloqueos por mantenimiento y mantiene un historial detallado de las reservas por miembro. 

---

## Integrantes y Roles
| Nombre | Rol | GitHub |
| :--- | :--- | :--- |
| **Octavio García** | **Scrum Master** | @octavioleogarcia-png |
| **Calamari Santino** | Dev Leader + QA Lead | @Barriletecosmicok |
| **Polcowñuk Matias** | Dev Leader | @ZeroKava |
| **De Olivera Jesus** | QA Lead | @Jesucristo23 |
| **Manrique Santiago** | UX Lead | @Santiago-Manrique |



---

## Enlaces de Gestión
**Tablero Kanban:** https://github.com/users/ZeroKava/projects/2/views/1

**Reporte Semanal (S1):** [Enlace al campus/Moodle](PEGAR_ACA_LINK_A_MOODLE)

**Diagrama Casos de Uso:** https://miro.com/welcomeonboard/T29CeXUwaE5YRHU2aUE5MGV5UVAwc1NDbEJlMXR3UlY4dUdGQW9HZmRkWUtJQXRuQU0yN2xET2JvdzVPbVVUdklCVk1kQlZEeHJwamdRTkhXY25DK3g3c3RzWUZSTU5kN3hJUlo2UlRYbGd4MDBjVHhleHVJZlZPSHYzTzVTU01nbHpza3F6REdEcmNpNEFOMmJXWXBBPT0hdjE=?share_link_id=557559127714

---

## Estructura del Repositorio
Organización de archivos según los lineamientos de la cátedra: 

**docs/**: Documentación oficial (Contrato, Matriz de Riesgos y AI_LOG).

**design/**: Prototipos y mockups del sistema. 

**src/**: Código fuente del proyecto. 

**tests/**: Casos de prueba y validaciones.


**Patrones de Diseño Seleccionados:**
Factory Method y Observer  

**Diagrama Entidad-Relación:** 
<img width="1600" height="1227" alt="image" src="https://github.com/user-attachments/assets/6f81b8a5-1bc9-4bb6-904e-3347d843c557" />

```

## C:\Users\User\Desktop\TP1_ingenieria_II\src\api.py

```python
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
    AuthService,
    AuthEventBus,
    ConsoleLogger,
    DatabaseObserver,
    EmailNotifier,
    InMemoryUserRepository,
)

app = Flask(__name__)
CORS(app)

# Composición del sistema
event_bus = AuthEventBus()
event_bus.subscribe(ConsoleLogger())
event_bus.subscribe(DatabaseObserver())
event_bus.subscribe(EmailNotifier())

repository = InMemoryUserRepository()
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

```

## C:\Users\User\Desktop\TP1_ingenieria_II\src\app.js

```js
const API_URL = "http://127.0.0.1:5000/api/auth";

// Guardar token
function storeToken(token) {
  if (token) {
    localStorage.setItem('nexo_token', token);
    console.log('Token guardado:', token);
  }
}

// Intercambio entre Login y Sign Up
function toggleAuth() {
    const loginForm = document.getElementById('login-form');
    const signupForm = document.getElementById('signup-form');
    const title = document.getElementById('form-title');
    const toggleText = document.getElementById('toggle-text');

    if (loginForm.classList.contains('hidden')) {
        loginForm.classList.remove('hidden');
        signupForm.classList.add('hidden');
        title.innerText = "SpicyTech Hub";
        toggleText.innerHTML = '¿No tienes cuenta? <span onclick="toggleAuth()">Regístrate</span>';
    } else {
        loginForm.classList.add('hidden');
        signupForm.classList.remove('hidden');
        title.innerText = "Únete a SpicyTech";
        toggleText.innerHTML = '¿Ya tienes cuenta? <span onclick="toggleAuth()">Inicia Sesión</span>';
    }
}

function showMessage(text, isError = true) {
    const msgDiv = document.getElementById('api-message');
    msgDiv.innerText = text;
    msgDiv.className = `message ${isError ? 'error' : 'success'}`;
    msgDiv.style.display = 'block';
}

// Login
document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;

    try {
        const response = await fetch(`${API_URL}/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });
        const result = await response.json();
        
        if (result.success) {
            if (result.data && result.data.token) storeToken(result.data.token);
            showMessage(`¡Bienvenido de nuevo, ${result.data.username}!`, false);
            // Aquí podrías redirigir al dashboard
        } else {
            showMessage(result.message);
        }
    } catch (err) {
        showMessage("Error de conexión con el servidor.");
    }
});

// Sign Up
document.getElementById('signup-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = {
        username: document.getElementById('signup-username').value,
        email: document.getElementById('signup-email').value,
        password: document.getElementById('signup-password').value,
        confirm_password: document.getElementById('signup-confirm').value,
        role: "member"
    };

    try {
        const response = await fetch(`${API_URL}/signup`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        const result = await response.json();

        if (result.success) {
            showMessage("Cuenta creada. ¡Ya puedes iniciar sesión!", false);
            setTimeout(toggleAuth, 2000);
        } else {
            const errorText = result.errors.length > 0 ? result.errors.join(" ") : result.message;
            showMessage(errorText);
        }
    } catch (err) {
        showMessage("Error al intentar registrar el usuario.");
    }
});

```

## C:\Users\User\Desktop\TP1_ingenieria_II\src\auth.py

```python
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

```

## C:\Users\User\Desktop\TP1_ingenieria_II\src\home.html

<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SpicyTech · Coworking Space</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --red:        #C0392B;
      --red-deep:   #96281B;
      --red-soft:   #E8604C;
      --red-muted:  #D4614F;
      --cream:      #FAF6F0;
      --cream-dark: #F0E8DC;
      --cream-mid:  #E8DDD0;
      --sand:       #C9B99A;
      --brown:      #7A5C44;
      --dark:       #1C1209;
      --txt:        #2C1A10;
      --txt2:       #7A5C44;
      --txt3:       #A08870;
      --white:      #FFFFFF;
      --r:          16px;
      --rm:         10px;
    }

    html { scroll-behavior: smooth; }

    body {
      background: var(--cream);
      color: var(--txt);
      font-family: 'Outfit', sans-serif;
      overflow-x: hidden;
    }

    /* ─── SCROLLBAR ─── */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: var(--cream-dark); }
    ::-webkit-scrollbar-thumb { background: var(--red-muted); border-radius: 3px; }

    /* ─── NAVBAR ─── */
    nav {
      position: fixed;
      top: 0; left: 0; right: 0;
      z-index: 100;
      padding: 0 5%;
      height: 72px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      transition: background 0.3s, box-shadow 0.3s;
    }
    nav.scrolled {
      background: rgba(250,246,240,0.95);
      backdrop-filter: blur(12px);
      box-shadow: 0 1px 0 var(--cream-mid);
    }

    .nav-logo {
      display: flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
    }
    .nav-logo-mark {
      width: 38px; height: 38px;
      background: var(--red);
      border-radius: 10px;
      display: flex; align-items: center; justify-content: center;
      font-size: 18px;
    }
    .nav-logo-text {
      font-family: 'Playfair Display', serif;
      font-size: 20px;
      font-weight: 700;
      color: var(--dark);
    }
    .nav-logo-sub {
      font-size: 10px;
      color: var(--txt3);
      margin-top: 1px;
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }

    .nav-links {
      display: flex;
      align-items: center;
      gap: 32px;
      list-style: none;
    }
    .nav-links a {
      font-size: 14px;
      font-weight: 500;
      color: var(--txt2);
      text-decoration: none;
      transition: color 0.2s;
      letter-spacing: 0.02em;
    }
    .nav-links a:hover { color: var(--red); }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .btn-ghost {
      padding: 9px 20px;
      border: 1.5px solid var(--cream-mid);
      border-radius: var(--rm);
      background: transparent;
      font-family: 'Outfit', sans-serif;
      font-size: 13px;
      font-weight: 500;
      color: var(--txt);
      cursor: pointer;
      text-decoration: none;
      transition: border-color 0.2s, color 0.2s;
      display: inline-flex; align-items: center;
    }
    .btn-ghost:hover { border-color: var(--red); color: var(--red); }

    .btn-primary {
      padding: 9px 22px;
      background: var(--red);
      border: none;
      border-radius: var(--rm);
      font-family: 'Outfit', sans-serif;
      font-size: 13px;
      font-weight: 600;
      color: #fff;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex; align-items: center;
      transition: background 0.2s, transform 0.1s;
    }
    .btn-primary:hover { background: var(--red-deep); transform: translateY(-1px); }
    .btn-primary:active { transform: scale(0.98); }

    /* ─── HERO ─── */
    .hero {
      min-height: 100vh;
      display: grid;
      grid-template-columns: 1fr 1fr;
      position: relative;
      overflow: hidden;
    }

    .hero-bg-shape {
      position: absolute;
      inset: 0;
      pointer-events: none;
      z-index: 0;
    }
    .hero-bg-shape::before {
      content: '';
      position: absolute;
      top: -120px; right: -100px;
      width: 700px; height: 700px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(192,57,43,0.08) 0%, transparent 70%);
    }
    .hero-bg-shape::after {
      content: '';
      position: absolute;
      bottom: -80px; left: 10%;
      width: 500px; height: 500px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(201,185,154,0.25) 0%, transparent 70%);
    }

    /* Grain texture overlay */
    .hero::before {
      content: '';
      position: absolute;
      inset: 0;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.03'/%3E%3C/svg%3E");
      pointer-events: none;
      z-index: 0;
    }

    .hero-left {
      padding: 140px 6% 80px 7%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      position: relative;
      z-index: 1;
    }

    .hero-eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--red);
      margin-bottom: 24px;
      opacity: 0;
      animation: fadeUp 0.6s ease forwards 0.2s;
    }
    .eyebrow-dot {
      width: 6px; height: 6px;
      border-radius: 50%;
      background: var(--red);
    }

    .hero-title {
      font-family: 'Playfair Display', serif;
      font-size: clamp(48px, 6vw, 80px);
      font-weight: 900;
      line-height: 1.0;
      color: var(--dark);
      margin-bottom: 28px;
      opacity: 0;
      animation: fadeUp 0.7s ease forwards 0.35s;
    }
    .hero-title em {
      font-style: italic;
      color: var(--red);
    }
    .hero-title .underline-word {
      position: relative;
      display: inline-block;
    }
    .hero-title .underline-word::after {
      content: '';
      position: absolute;
      bottom: 2px; left: 0; right: 0;
      height: 4px;
      background: var(--red-soft);
      border-radius: 2px;
      opacity: 0.4;
    }

    .hero-desc {
      font-size: 17px;
      line-height: 1.7;
      color: var(--txt2);
      max-width: 440px;
      margin-bottom: 44px;
      font-weight: 300;
      opacity: 0;
      animation: fadeUp 0.7s ease forwards 0.5s;
    }

    .hero-cta-group {
      display: flex;
      align-items: center;
      gap: 16px;
      opacity: 0;
      animation: fadeUp 0.7s ease forwards 0.65s;
    }
    .btn-hero {
      padding: 15px 36px;
      background: var(--red);
      border: none;
      border-radius: var(--r);
      font-family: 'Outfit', sans-serif;
      font-size: 15px;
      font-weight: 600;
      color: #fff;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex; align-items: center; gap: 8px;
      transition: background 0.2s, transform 0.15s, box-shadow 0.2s;
      box-shadow: 0 8px 24px rgba(192,57,43,0.3);
    }
    .btn-hero:hover {
      background: var(--red-deep);
      transform: translateY(-2px);
      box-shadow: 0 12px 32px rgba(192,57,43,0.4);
    }
    .btn-hero-outline {
      padding: 15px 28px;
      background: transparent;
      border: 1.5px solid var(--cream-mid);
      border-radius: var(--r);
      font-family: 'Outfit', sans-serif;
      font-size: 15px;
      font-weight: 500;
      color: var(--txt);
      cursor: pointer;
      text-decoration: none;
      display: inline-flex; align-items: center; gap: 8px;
      transition: border-color 0.2s, color 0.2s;
    }
    .btn-hero-outline:hover { border-color: var(--red); color: var(--red); }

    .hero-stats {
      display: flex;
      gap: 36px;
      margin-top: 56px;
      padding-top: 36px;
      border-top: 1px solid var(--cream-mid);
      opacity: 0;
      animation: fadeUp 0.7s ease forwards 0.8s;
    }
    .stat-item {}
    .stat-num {
      font-family: 'Playfair Display', serif;
      font-size: 32px;
      font-weight: 700;
      color: var(--dark);
      line-height: 1;
    }
    .stat-label {
      font-size: 12px;
      color: var(--txt3);
      margin-top: 4px;
      font-weight: 400;
    }

    /* ─── HERO RIGHT ─── */
    .hero-right {
      position: relative;
      z-index: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 120px 5% 60px 4%;
      opacity: 0;
      animation: fadeLeft 0.8s ease forwards 0.4s;
    }

    .hero-visual {
      width: 100%;
      max-width: 520px;
      position: relative;
    }

    .hero-card-main {
      background: var(--white);
      border-radius: 24px;
      overflow: hidden;
      box-shadow: 0 32px 80px rgba(44,26,16,0.15);
      position: relative;
    }

    .hero-card-img {
      width: 100%;
      height: 280px;
      background: linear-gradient(135deg, #C0392B 0%, #E8604C 40%, #D4614F 70%, #96281B 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      overflow: hidden;
    }
    .hero-card-img::before {
      content: '';
      position: absolute;
      inset: 0;
      background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.06'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
    }
    .space-illustration {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      padding: 24px;
      width: 100%;
    }
    .space-desk {
      background: rgba(255,255,255,0.15);
      border-radius: 10px;
      height: 70px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 5px;
      font-size: 22px;
      color: rgba(255,255,255,0.9);
      backdrop-filter: blur(4px);
      border: 1px solid rgba(255,255,255,0.2);
      transition: transform 0.3s;
    }
    .space-desk:hover { transform: scale(1.05); }
    .space-desk span {
      font-size: 10px;
      font-weight: 500;
      letter-spacing: 0.05em;
      opacity: 0.8;
    }

    .hero-card-body {
      padding: 24px;
    }
    .availability-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 16px;
    }
    .availability-title {
      font-weight: 600;
      font-size: 14px;
      color: var(--dark);
    }
    .avail-badge {
      font-size: 11px;
      font-weight: 600;
      padding: 4px 10px;
      border-radius: 20px;
      background: #FEE9E7;
      color: var(--red);
    }

    .time-slots {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }
    .slot {
      padding: 6px 12px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s;
    }
    .slot.free { background: #FEF9F5; border: 1px solid var(--cream-mid); color: var(--txt2); }
    .slot.free:hover { border-color: var(--red); color: var(--red); }
    .slot.taken { background: var(--cream-dark); color: var(--txt3); pointer-events: none; text-decoration: line-through; }
    .slot.selected { background: var(--red); color: white; border: 1px solid var(--red); }

    /* Floating cards */
    .float-card {
      position: absolute;
      background: var(--white);
      border-radius: var(--r);
      box-shadow: 0 12px 40px rgba(44,26,16,0.14);
      padding: 14px 18px;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .float-card-1 {
      bottom: -20px;
      left: -40px;
      animation: float1 4s ease-in-out infinite;
    }
    .float-card-2 {
      top: 20px;
      right: -30px;
      animation: float2 5s ease-in-out infinite;
    }
    .float-icon {
      width: 36px; height: 36px;
      border-radius: 10px;
      display: flex; align-items: center; justify-content: center;
      font-size: 18px;
      flex-shrink: 0;
    }
    .float-text-label { font-size: 11px; color: var(--txt3); }
    .float-text-val { font-size: 14px; font-weight: 600; color: var(--dark); }

    @keyframes float1 {
      0%,100% { transform: translateY(0px) rotate(-1deg); }
      50% { transform: translateY(-10px) rotate(1deg); }
    }
    @keyframes float2 {
      0%,100% { transform: translateY(0px) rotate(1deg); }
      50% { transform: translateY(-14px) rotate(-1deg); }
    }

    /* ─── SECTION SHARED ─── */
    section { position: relative; }
    .section-inner { max-width: 1200px; margin: 0 auto; padding: 100px 5%; }

    .section-label {
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--red);
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .section-label::before {
      content: '';
      display: inline-block;
      width: 24px; height: 2px;
      background: var(--red);
    }

    .section-title {
      font-family: 'Playfair Display', serif;
      font-size: clamp(32px, 4vw, 52px);
      font-weight: 800;
      color: var(--dark);
      line-height: 1.15;
      margin-bottom: 18px;
    }
    .section-title em { font-style: italic; color: var(--red-muted); }

    .section-desc {
      font-size: 16px;
      color: var(--txt2);
      line-height: 1.7;
      max-width: 520px;
      font-weight: 300;
    }

    /* ─── FEATURES ─── */
    .features-section {
      background: var(--dark);
      color: var(--white);
    }
    .features-section .section-title { color: var(--cream); }
    .features-section .section-desc { color: var(--sand); }
    .features-section .section-label { color: var(--red-soft); }
    .features-section .section-label::before { background: var(--red-soft); }

    .features-header {
      display: flex;
      align-items: flex-end;
      justify-content: space-between;
      margin-bottom: 64px;
      gap: 40px;
    }

    .features-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 2px;
      background: rgba(255,255,255,0.05);
      border-radius: 20px;
      overflow: hidden;
    }

    .feature-card {
      background: #241508;
      padding: 40px 32px;
      transition: background 0.2s;
      position: relative;
    }
    .feature-card:hover { background: #2e1b0a; }
    .feature-card::after {
      content: '';
      position: absolute;
      bottom: 0; left: 32px; right: 32px;
      height: 1px;
      background: rgba(255,255,255,0.05);
    }

    .feature-icon {
      width: 48px; height: 48px;
      background: rgba(192,57,43,0.15);
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 22px;
      margin-bottom: 20px;
      border: 1px solid rgba(192,57,43,0.2);
    }
    .feature-name {
      font-family: 'Playfair Display', serif;
      font-size: 18px;
      font-weight: 700;
      color: var(--cream);
      margin-bottom: 10px;
    }
    .feature-desc {
      font-size: 14px;
      color: var(--sand);
      line-height: 1.65;
      font-weight: 300;
    }

    /* ─── ESPACIOS ─── */
    .spaces-section {
      background: var(--cream);
    }
    .spaces-layout {
      display: grid;
      grid-template-columns: 1fr 2fr;
      gap: 80px;
      align-items: start;
    }
    .spaces-sticky { position: sticky; top: 100px; }

    .spaces-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }

    .space-card {
      background: var(--white);
      border-radius: 20px;
      overflow: hidden;
      border: 1px solid var(--cream-mid);
      transition: transform 0.25s, box-shadow 0.25s;
      cursor: pointer;
    }
    .space-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 20px 48px rgba(44,26,16,0.12);
    }
    .space-card.featured {
      grid-column: 1 / -1;
    }

    .space-card-img {
      height: 160px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 48px;
      position: relative;
      overflow: hidden;
    }
    .space-card.featured .space-card-img { height: 200px; }

    .space-card-body { padding: 20px; }
    .space-card-name {
      font-family: 'Playfair Display', serif;
      font-size: 18px;
      font-weight: 700;
      color: var(--dark);
      margin-bottom: 6px;
    }
    .space-card-desc {
      font-size: 13px;
      color: var(--txt2);
      line-height: 1.6;
      margin-bottom: 14px;
      font-weight: 300;
    }
    .space-card-footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .space-price {
      font-size: 13px;
      font-weight: 600;
      color: var(--red);
    }
    .space-badge {
      font-size: 11px;
      padding: 3px 9px;
      border-radius: 20px;
      font-weight: 500;
    }
    .badge-avail { background: #FEE9E7; color: var(--red); }
    .badge-full  { background: var(--cream-dark); color: var(--txt3); }

    /* ─── PRECIOS ─── */
    .pricing-section {
      background: var(--cream-dark);
    }
    .pricing-header {
      text-align: center;
      margin-bottom: 64px;
    }
    .pricing-header .section-label { justify-content: center; }
    .pricing-header .section-desc { margin: 0 auto; text-align: center; }

    .pricing-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      max-width: 960px;
      margin: 0 auto;
    }

    .price-card {
      background: var(--white);
      border-radius: 20px;
      padding: 36px 28px;
      border: 1.5px solid var(--cream-mid);
      transition: transform 0.25s, box-shadow 0.25s;
      position: relative;
    }
    .price-card:hover { transform: translateY(-4px); }
    .price-card.popular {
      background: var(--red);
      border-color: var(--red);
      color: #fff;
      transform: scale(1.04);
    }
    .price-card.popular:hover { transform: scale(1.04) translateY(-4px); }

    .popular-tag {
      position: absolute;
      top: -12px; left: 50%;
      transform: translateX(-50%);
      background: var(--dark);
      color: var(--cream);
      font-size: 11px;
      font-weight: 600;
      padding: 4px 14px;
      border-radius: 20px;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      white-space: nowrap;
    }

    .plan-name {
      font-size: 13px;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-bottom: 12px;
    }
    .plan-name.pop { color: rgba(255,255,255,0.8); }
    .plan-name.reg { color: var(--txt3); }

    .plan-price {
      font-family: 'Playfair Display', serif;
      font-size: 48px;
      font-weight: 900;
      line-height: 1;
      margin-bottom: 4px;
    }
    .plan-price.pop { color: #fff; }
    .plan-price.reg { color: var(--dark); }

    .plan-period {
      font-size: 13px;
      font-weight: 300;
      margin-bottom: 28px;
    }
    .plan-period.pop { color: rgba(255,255,255,0.7); }
    .plan-period.reg { color: var(--txt3); }

    .plan-features {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-bottom: 28px;
    }
    .plan-features li {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 13.5px;
      font-weight: 400;
    }
    .plan-features li.pop { color: rgba(255,255,255,0.9); }
    .plan-features li.reg { color: var(--txt2); }
    .check-icon { color: var(--red); font-size: 14px; flex-shrink: 0; }
    .check-icon.pop { color: rgba(255,255,255,0.9); }

    .btn-plan {
      width: 100%;
      padding: 13px;
      border-radius: var(--rm);
      font-family: 'Outfit', sans-serif;
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
      text-align: center;
      text-decoration: none;
      display: block;
    }
    .btn-plan.pop {
      background: var(--dark);
      color: var(--cream);
      border: none;
    }
    .btn-plan.pop:hover { background: #2e1b0a; }
    .btn-plan.reg {
      background: transparent;
      color: var(--red);
      border: 1.5px solid var(--cream-mid);
    }
    .btn-plan.reg:hover { border-color: var(--red); background: #FEF9F5; }

    /* ─── CONTACTO / FOOTER ─── */
    .contact-section {
      background: var(--dark);
      color: var(--cream);
    }

    .contact-layout {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 80px;
      align-items: center;
    }

    .contact-title {
      font-family: 'Playfair Display', serif;
      font-size: clamp(36px, 4vw, 56px);
      font-weight: 900;
      line-height: 1.1;
      color: var(--cream);
      margin-bottom: 20px;
    }
    .contact-title em { font-style: italic; color: var(--red-soft); }
    .contact-desc { font-size: 15px; color: var(--sand); line-height: 1.7; margin-bottom: 36px; font-weight: 300; }

    .contact-info-item {
      display: flex;
      align-items: center;
      gap: 14px;
      margin-bottom: 16px;
    }
    .contact-icon {
      width: 40px; height: 40px;
      background: rgba(192,57,43,0.15);
      border-radius: 10px;
      display: flex; align-items: center; justify-content: center;
      font-size: 18px;
      border: 1px solid rgba(192,57,43,0.2);
      flex-shrink: 0;
    }
    .contact-info-label { font-size: 11px; color: var(--sand); margin-bottom: 2px; font-weight: 400; letter-spacing: 0.05em; }
    .contact-info-val { font-size: 14px; color: var(--cream); font-weight: 500; }

    .contact-form-card {
      background: #241508;
      border-radius: 24px;
      padding: 40px;
      border: 1px solid rgba(255,255,255,0.05);
    }
    .form-title-small {
      font-family: 'Playfair Display', serif;
      font-size: 22px;
      font-weight: 700;
      color: var(--cream);
      margin-bottom: 24px;
    }

    .form-field { margin-bottom: 16px; }
    .form-label {
      display: block;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--sand);
      margin-bottom: 7px;
    }
    .form-input, .form-textarea {
      width: 100%;
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: var(--rm);
      padding: 11px 14px;
      font-family: 'Outfit', sans-serif;
      font-size: 14px;
      color: var(--cream);
      outline: none;
      transition: border-color 0.2s;
    }
    .form-input::placeholder, .form-textarea::placeholder { color: rgba(255,255,255,0.25); }
    .form-input:focus, .form-textarea:focus { border-color: var(--red-soft); }
    .form-textarea { height: 100px; resize: vertical; }

    .btn-send {
      width: 100%;
      padding: 14px;
      background: var(--red);
      border: none;
      border-radius: var(--rm);
      font-family: 'Outfit', sans-serif;
      font-size: 14px;
      font-weight: 600;
      color: #fff;
      cursor: pointer;
      margin-top: 4px;
      transition: background 0.2s;
    }
    .btn-send:hover { background: var(--red-deep); }

    /* ─── FOOTER BAR ─── */
    .footer-bar {
      background: #140D04;
      padding: 24px 5%;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
    }
    .footer-bar-logo {
      font-family: 'Playfair Display', serif;
      font-size: 18px;
      font-weight: 700;
      color: var(--cream);
      opacity: 0.7;
    }
    .footer-bar-copy {
      font-size: 12px;
      color: var(--sand);
      opacity: 0.6;
    }
    .footer-links {
      display: flex;
      gap: 24px;
    }
    .footer-links a {
      font-size: 12px;
      color: var(--sand);
      text-decoration: none;
      opacity: 0.6;
      transition: opacity 0.2s;
    }
    .footer-links a:hover { opacity: 1; }

    /* ─── ANIMATIONS ─── */
    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(28px); }
      to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeLeft {
      from { opacity: 0; transform: translateX(40px); }
      to   { opacity: 1; transform: translateX(0); }
    }

    .reveal {
      opacity: 0;
      transform: translateY(30px);
      transition: opacity 0.65s ease, transform 0.65s ease;
    }
    .reveal.visible {
      opacity: 1;
      transform: translateY(0);
    }

    /* ─── MOBILE ─── */
    @media (max-width: 900px) {
      .hero { grid-template-columns: 1fr; min-height: auto; }
      .hero-left { padding: 120px 6% 40px; }
      .hero-right { padding: 20px 6% 80px; }
      .hero-visual { max-width: 100%; }
      .float-card-1, .float-card-2 { display: none; }
      .features-grid { grid-template-columns: 1fr; }
      .features-header { flex-direction: column; align-items: flex-start; }
      .spaces-layout { grid-template-columns: 1fr; gap: 40px; }
      .spaces-sticky { position: relative; top: auto; }
      .pricing-grid { grid-template-columns: 1fr; }
      .price-card.popular { transform: none; }
      .contact-layout { grid-template-columns: 1fr; gap: 48px; }
      nav .nav-links { display: none; }
    }
    @media (max-width: 600px) {
      .spaces-grid { grid-template-columns: 1fr; }
      .space-card.featured { grid-column: auto; }
      .hero-stats { gap: 20px; }
    }
  </style>
</head>
<body>

<!-- ══ NAVBAR ══ -->
<nav id="navbar">
  <a href="#" class="nav-logo">
    <div class="nav-logo-mark">🌶️</div>
    <div>
      <div class="nav-logo-text">SpicyTech</div>
      <div class="nav-logo-sub">Coworking Space</div>
    </div>
  </a>
  <ul class="nav-links">
    <li><a href="#features">Servicios</a></li>
    <li><a href="#spaces">Espacios</a></li>
    <li><a href="#pricing">Precios</a></li>
    <li><a href="#contact">Contacto</a></li>
  </ul>
  <div class="nav-actions">
    <a href="login.html" class="btn-ghost">Iniciar sesión</a>
    <a href="login.html#signup" class="btn-primary">Registrarse →</a>
  </div>
</nav>


<!-- ══ HERO ══ -->
<section class="hero" id="home">
  <div class="hero-bg-shape"></div>

  <div class="hero-left">
    <div class="hero-eyebrow">
      <span class="eyebrow-dot"></span>
      Coworking en el corazón de la ciudad
    </div>
    <h1 class="hero-title">
      Tu próximo<br>
      <em>gran proyecto</em><br>
      empieza <span class="underline-word">aquí</span>
    </h1>
    <p class="hero-desc">
      Espacios modernos, comunidad vibrante y todo lo que necesitás para trabajar, crear y crecer. Sin ataduras, sin excusas.
    </p>
    <div class="hero-cta-group">
      <a href="login.html#signup" class="btn-hero">
        Reservá tu lugar
        <span>→</span>
      </a>
      <a href="#spaces" class="btn-hero-outline">
        Ver espacios
      </a>
    </div>
    <div class="hero-stats">
      <div class="stat-item">
        <div class="stat-num">120+</div>
        <div class="stat-label">Coworkers activos</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">4</div>
        <div class="stat-label">Tipos de espacios</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">98%</div>
        <div class="stat-label">Satisfacción</div>
      </div>
    </div>
  </div>

  <div class="hero-right">
    <div class="hero-visual">
      <!-- Floating badge top right -->
      <div class="float-card float-card-2">
        <div class="float-icon" style="background:#FEE9E7;">☕</div>
        <div>
          <div class="float-text-label">Cafetería incluida</div>
          <div class="float-text-val">Ilimitada</div>
        </div>
      </div>

      <div class="hero-card-main">
        <div class="hero-card-img">
          <div class="space-illustration">
            <div class="space-desk">🖥️<span>Desk</span></div>
            <div class="space-desk">🏢<span>Sala</span></div>
            <div class="space-desk">🔒<span>Privada</span></div>
            <div class="space-desk">📡<span>WiFi</span></div>
            <div class="space-desk">🎧<span>Foco</span></div>
            <div class="space-desk">🤝<span>Equipo</span></div>
          </div>
        </div>
        <div class="hero-card-body">
          <div class="availability-row">
            <span class="availability-title">Disponibilidad de hoy</span>
            <span class="avail-badge">8 lugares libres</span>
          </div>
          <div class="time-slots">
            <div class="slot taken">08:00</div>
            <div class="slot taken">09:00</div>
            <div class="slot selected">10:00</div>
            <div class="slot free">11:00</div>
            <div class="slot free">14:00</div>
            <div class="slot free">15:00</div>
            <div class="slot free">16:00</div>
            <div class="slot taken">18:00</div>
          </div>
        </div>
      </div>

      <!-- Floating badge bottom left -->
      <div class="float-card float-card-1">
        <div class="float-icon" style="background:#FEE9E7; font-size:16px;">📶</div>
        <div>
          <div class="float-text-label">Velocidad WiFi</div>
          <div class="float-text-val">500 Mbps</div>
        </div>
      </div>
    </div>
  </div>
</section>


<!-- ══ FEATURES ══ -->
<section class="features-section" id="features">
  <div class="section-inner">
    <div class="features-header reveal">
      <div>
        <div class="section-label">Servicios incluidos</div>
        <h2 class="section-title">Todo lo que<br>necesitás, <em>incluido</em></h2>
      </div>
      <p class="section-desc" style="max-width:320px;">Sin sorpresas. Un solo precio que cubre todo lo que un profesional moderno necesita.</p>
    </div>
    <div class="features-grid reveal">
      <div class="feature-card">
        <div class="feature-icon">📡</div>
        <div class="feature-name">WiFi de alta velocidad</div>
        <div class="feature-desc">Fibra óptica simétrica de 500 Mbps dedicada. Conectividad de respaldo automática.</div>
      </div>
      <div class="feature-card">
        <div class="feature-icon">❄️</div>
        <div class="feature-name">Ambiente climatizado</div>
        <div class="feature-desc">Temperatura ideal todo el año. Sistema de climatización zonal por área de trabajo.</div>
      </div>
      <div class="feature-card">
        <div class="feature-icon">😊</div>
        <div class="feature-name">Recepción personalizada</div>
        <div class="feature-desc">Equipo de recepción disponible para gestionar visitas, paquetes y consultas.</div>
      </div>
      <div class="feature-card">
        <div class="feature-icon">☕</div>
        <div class="feature-name">Cafetería ilimitada</div>
        <div class="feature-desc">Café, té, snacks saludables y bebidas disponibles sin costo adicional.</div>
      </div>
      <div class="feature-card">
        <div class="feature-icon">🔒</div>
        <div class="feature-name">Lockers privados</div>
        <div class="feature-desc">Guardado seguro de pertenencias con lockers asignados y acceso con código.</div>
      </div>
      <div class="feature-card">
        <div class="feature-icon">💺</div>
        <div class="feature-name">Mobiliario ergonómico</div>
        <div class="feature-desc">Sillas, escritorios y monitores de grado profesional para cuidar tu postura.</div>
      </div>
    </div>
  </div>
</section>


<!-- ══ ESPACIOS ══ -->
<section class="spaces-section" id="spaces">
  <div class="section-inner">
    <div class="spaces-layout">
      <div class="spaces-sticky reveal">
        <div class="section-label">Nuestros espacios</div>
        <h2 class="section-title">Elegí el espacio <em>ideal</em> para vos</h2>
        <p class="section-desc">Desde escritorios compartidos hasta oficinas privadas. Flexibilidad total según tus necesidades.</p>
        <br><br>
        <a href="login.html#signup" class="btn-hero" style="display:inline-flex;">Reservar ahora →</a>
      </div>

      <div class="spaces-grid reveal">
        <div class="space-card featured">
          <div class="space-card-img" style="background: linear-gradient(135deg, #FAE8E5 0%, #F5C8C3 100%);">
            🏢
          </div>
          <div class="space-card-body">
            <div class="space-card-name">Sala de Reuniones</div>
            <div class="space-card-desc">Sala equipada para hasta 8 personas con proyector, pizarra y videoconferencia integrada. Ideal para presentaciones y reuniones de equipo.</div>
            <div class="space-card-footer">
              <span class="space-price">Desde $800/hora</span>
              <span class="space-badge badge-avail">✓ Disponible</span>
            </div>
          </div>
        </div>

        <div class="space-card">
          <div class="space-card-img" style="background: linear-gradient(135deg, #F5EBE0 0%, #EDD9C7 100%);">
            🪑
          </div>
          <div class="space-card-body">
            <div class="space-card-name">Espacio Compartido</div>
            <div class="space-card-desc">Escritorios en ambiente abierto. Comunidad, networking y energía colectiva.</div>
            <div class="space-card-footer">
              <span class="space-price">Desde $300/día</span>
              <span class="space-badge badge-avail">✓ Disponible</span>
            </div>
          </div>
        </div>

        <div class="space-card">
          <div class="space-card-img" style="background: linear-gradient(135deg, #FAE8E5 0%, #EFC5BF 100%);">
            🔐
          </div>
          <div class="space-card-body">
            <div class="space-card-name">Oficina Privada</div>
            <div class="space-card-desc">Espacio exclusivo para tu empresa. Totalmente cerrado y personalizable.</div>
            <div class="space-card-footer">
              <span class="space-price">Desde $5.500/mes</span>
              <span class="space-badge badge-avail">✓ Disponible</span>
            </div>
          </div>
        </div>

        <div class="space-card" style="grid-column: 1 / -1;">
          <div class="space-card-img" style="background: linear-gradient(135deg, #EDE0D4 0%, #D6C4AE 100%); height:120px;">
            📚
          </div>
          <div class="space-card-body">
            <div class="space-card-name">Sala de Capacitación</div>
            <div class="space-card-desc">Aula completa para workshops, trainings y eventos. Capacidad para 20 personas con todo el equipamiento audiovisual necesario.</div>
            <div class="space-card-footer">
              <span class="space-price">Desde $1.200/hora</span>
              <span class="space-badge badge-full">Reservar</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>


<!-- ══ PRICING ══ -->
<section class="pricing-section" id="pricing">
  <div class="section-inner">
    <div class="pricing-header reveal">
      <div class="section-label">Planes y precios</div>
      <h2 class="section-title">Elegí cómo <em>trabajar</em></h2>
      <p class="section-desc">Sin contratos a largo plazo. Cambiá de plan cuando quieras.</p>
    </div>

    <div class="pricing-grid reveal">
      <!-- Free -->
      <div class="price-card">
        <div class="plan-name reg">Visita de Día</div>
        <div class="plan-price reg">$300</div>
        <div class="plan-period reg">por día</div>
        <ul class="plan-features">
          <li class="reg"><span class="check-icon">✓</span> Escritorio compartido</li>
          <li class="reg"><span class="check-icon">✓</span> WiFi de alta velocidad</li>
          <li class="reg"><span class="check-icon">✓</span> Cafetería incluida</li>
          <li class="reg"><span class="check-icon">✓</span> Locker por el día</li>
          <li class="reg" style="opacity:0.4;"><span>✗</span> Sala de reuniones</li>
          <li class="reg" style="opacity:0.4;"><span>✗</span> Dirección postal</li>
        </ul>
        <a href="login.html#signup" class="btn-plan reg">Empezar hoy</a>
      </div>

      <!-- Popular -->
      <div class="price-card popular">
        <div class="popular-tag">⭐ Más elegido</div>
        <div class="plan-name pop">Mensual Pro</div>
        <div class="plan-price pop">$4.800</div>
        <div class="plan-period pop">por mes</div>
        <ul class="plan-features">
          <li class="pop"><span class="check-icon pop">✓</span> Acceso ilimitado</li>
          <li class="pop"><span class="check-icon pop">✓</span> Escritorio dedicado</li>
          <li class="pop"><span class="check-icon pop">✓</span> 8 hs sala de reuniones</li>
          <li class="pop"><span class="check-icon pop">✓</span> Locker permanente</li>
          <li class="pop"><span class="check-icon pop">✓</span> Dirección postal</li>
          <li class="pop"><span class="check-icon pop">✓</span> Acceso 24/7</li>
        </ul>
        <a href="login.html#signup" class="btn-plan pop">Suscribirme</a>
      </div>

      <!-- Enterprise -->
      <div class="price-card">
        <div class="plan-name reg">Empresa</div>
        <div class="plan-price reg">$9.500</div>
        <div class="plan-period reg">por mes</div>
        <ul class="plan-features">
          <li class="reg"><span class="check-icon">✓</span> Oficina privada</li>
          <li class="reg"><span class="check-icon">✓</span> 5 puestos incluidos</li>
          <li class="reg"><span class="check-icon">✓</span> Sala ilimitada</li>
          <li class="reg"><span class="check-icon">✓</span> Recepción dedicada</li>
          <li class="reg"><span class="check-icon">✓</span> Facturación empresarial</li>
          <li class="reg"><span class="check-icon">✓</span> Soporte prioritario</li>
        </ul>
        <a href="#contact" class="btn-plan reg">Consultar →</a>
      </div>
    </div>
  </div>
</section>


<!-- ══ CONTACTO ══ -->
<section class="contact-section" id="contact">
  <div class="section-inner">
    <div class="contact-layout">
      <div class="reveal">
        <div class="section-label" style="color:var(--red-soft);">
          <span style="background:var(--red-soft);display:inline-block;width:24px;height:2px;"></span>
          Contacto
        </div>
        <h2 class="contact-title">¿Listo para <em>empezar</em>?</h2>
        <p class="contact-desc">Visitanos, escribinos o llamanos. Estamos para ayudarte a encontrar el espacio perfecto para tu proyecto.</p>

        <div class="contact-info-item">
          <div class="contact-icon">📍</div>
          <div>
            <div class="contact-info-label">Dirección</div>
            <div class="contact-info-val">Av. Ejemplo 1234, Ciudad</div>
          </div>
        </div>
        <div class="contact-info-item">
          <div class="contact-icon">📞</div>
          <div>
            <div class="contact-info-label">Teléfono</div>
            <div class="contact-info-val">+54 11 1234-5678</div>
          </div>
        </div>
        <div class="contact-info-item">
          <div class="contact-icon">✉️</div>
          <div>
            <div class="contact-info-label">Email</div>
            <div class="contact-info-val">hola@spicytech.com</div>
          </div>
        </div>
        <div class="contact-info-item">
          <div class="contact-icon">🕐</div>
          <div>
            <div class="contact-info-label">Horarios</div>
            <div class="contact-info-val">Lun–Vie 8:00 – 22:00 · Sáb 9:00 – 18:00</div>
          </div>
        </div>
      </div>

      <div class="reveal">
        <div class="contact-form-card">
          <div class="form-title-small">Envianos un mensaje</div>
          <div class="form-field">
            <label class="form-label">Nombre</label>
            <input class="form-input" type="text" placeholder="Tu nombre completo">
          </div>
          <div class="form-field">
            <label class="form-label">Email</label>
            <input class="form-input" type="email" placeholder="tu@email.com">
          </div>
          <div class="form-field">
            <label class="form-label">Mensaje</label>
            <textarea class="form-textarea" placeholder="¿En qué podemos ayudarte?"></textarea>
          </div>
          <button class="btn-send">Enviar mensaje →</button>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ══ FOOTER BAR ══ -->
<div class="footer-bar">
  <div class="footer-bar-logo">SpicyTech 🌶️</div>
  <div class="footer-links">
    <a href="#home">Inicio</a>
    <a href="#features">Servicios</a>
    <a href="#spaces">Espacios</a>
    <a href="#pricing">Precios</a>
  </div>
  <div class="footer-bar-copy">© 2026 SpicyTech Coworking · Ingeniería de Software II · UCP</div>
</div>


<script>
  // Navbar scroll effect
  const nav = document.getElementById('navbar');
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 40);
  });

  // Reveal on scroll
  const reveals = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => entry.target.classList.add('visible'), i * 80);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  reveals.forEach(el => observer.observe(el));

  // Interactive time slots
  document.querySelectorAll('.slot.free').forEach(slot => {
    slot.addEventListener('click', () => {
      document.querySelectorAll('.slot').forEach(s => {
        if (s.classList.contains('selected')) {
          s.classList.remove('selected');
          s.classList.add('free');
        }
      });
      slot.classList.remove('free');
      slot.classList.add('selected');
    });
  });

  // Contact form submit
  document.querySelector('.btn-send').addEventListener('click', () => {
    const btn = document.querySelector('.btn-send');
    btn.textContent = '✓ Mensaje enviado';
    btn.style.background = '#2C7A5C';
    setTimeout(() => {
      btn.textContent = 'Enviar mensaje →';
      btn.style.background = '';
    }, 3000);
  });
</script>
</body>
</html>
## C:\Users\User\Desktop\TP1_ingenieria_II\src\login.html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SpicyTech · Acceso</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --red:        #C0392B;
      --red-deep:   #96281B;
      --red-soft:   #E8604C;
      --red-muted:  #D4614F;
      --cream:      #FAF6F0;
      --cream-dark: #F0E8DC;
      --cream-mid:  #E8DDD0;
      --sand:       #C9B99A;
      --dark:       #1C1209;
      --txt:        #2C1A10;
      --txt2:       #7A5C44;
      --txt3:       #A08870;
      --white:      #FFFFFF;
      --r:          16px;
      --rm:         12px;
    }

    html, body {
      height: 100%;
      font-family: 'Outfit', sans-serif;
      background: var(--cream);
      color: var(--txt);
    }

    ::-webkit-scrollbar { width: 5px; }
    ::-webkit-scrollbar-track { background: var(--cream-dark); }
    ::-webkit-scrollbar-thumb { background: var(--red-muted); border-radius: 3px; }

    .auth-root {
      display: grid;
      grid-template-columns: 1fr 1fr;
      min-height: 100vh;
    }

    /* ══ LEFT PANEL ══ */
    .left-panel {
      background: var(--dark);
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      padding: 48px 52px;
      animation: panelIn 0.7s cubic-bezier(.22,1,.36,1) both;
    }
    @keyframes panelIn {
      from { opacity: 0; transform: translateX(-32px); }
      to   { opacity: 1; transform: translateX(0); }
    }
    .left-panel::before {
      content: '';
      position: absolute;
      top: -160px; right: -160px;
      width: 560px; height: 560px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(192,57,43,0.16) 0%, transparent 65%);
      pointer-events: none;
    }
    .left-panel::after {
      content: '';
      position: absolute;
      bottom: -120px; left: -80px;
      width: 420px; height: 420px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(201,185,154,0.07) 0%, transparent 65%);
      pointer-events: none;
    }
    .lp-grid {
      position: absolute; inset: 0;
      background-image:
        linear-gradient(rgba(255,255,255,0.025) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.025) 1px, transparent 1px);
      background-size: 52px 52px;
      pointer-events: none;
    }
    .lp-dots {
      position: absolute;
      top: 50%; right: 36px;
      transform: translateY(-50%);
      display: flex; flex-direction: column; gap: 9px;
      z-index: 1;
    }
    .lp-dot { width: 5px; height: 5px; border-radius: 50%; background: rgba(255,255,255,0.13); }
    .lp-dot.on { background: var(--red-soft); }

    .lp-top, .lp-mid, .lp-bot { position: relative; z-index: 1; }
    .lp-mid { flex: 1; display: flex; flex-direction: column; justify-content: center; }

    .logo-link { display: inline-flex; align-items: center; gap: 12px; text-decoration: none; }
    .logo-mark {
      width: 42px; height: 42px; background: var(--red);
      border-radius: 12px; display: flex; align-items: center; justify-content: center;
      font-size: 20px; box-shadow: 0 6px 18px rgba(192,57,43,0.38); flex-shrink: 0;
    }
    .logo-name { font-family: 'Playfair Display', serif; font-size: 21px; font-weight: 700; color: var(--cream); }
    .logo-sub  { font-size: 10px; color: var(--sand); opacity: 0.55; letter-spacing: 0.08em; margin-top: 1px; }

    /* Carousel */
    .carousel { margin-bottom: 36px; }
    .c-slides  { position: relative; min-height: 230px; }
    .c-slide   {
      position: absolute; inset: 0;
      opacity: 0; transform: translateY(14px);
      transition: opacity 0.5s ease, transform 0.5s ease;
      pointer-events: none;
    }
    .c-slide.active {
      opacity: 1; transform: translateY(0);
      pointer-events: auto; position: relative;
    }
    .slide-title {
      font-family: 'Playfair Display', serif;
      font-size: clamp(30px, 3vw, 46px);
      font-weight: 900; color: var(--cream);
      line-height: 1.08; margin-bottom: 14px;
    }
    .slide-title em { font-style: italic; color: var(--red-soft); }
    .slide-desc {
      font-size: 14px; color: var(--sand);
      line-height: 1.7; font-weight: 300;
      max-width: 300px; margin-bottom: 26px;
    }
    .slide-pills { display: flex; flex-direction: column; gap: 9px; }
    .slide-pill  {
      display: inline-flex; align-items: center; gap: 10px;
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.09);
      border-radius: 50px; padding: 8px 15px; width: fit-content;
    }
    .pill-icon {
      width: 26px; height: 26px; background: rgba(192,57,43,0.2);
      border-radius: 50%; display: flex; align-items: center; justify-content: center;
      font-size: 13px; flex-shrink: 0;
    }
    .pill-text { font-size: 12.5px; color: var(--cream); opacity: 0.85; }

    .c-nav { display: flex; align-items: center; gap: 8px; margin-top: 22px; }
    .c-dot-btn {
      width: 7px; height: 7px; border-radius: 50%;
      background: rgba(255,255,255,0.2);
      cursor: pointer; border: none; padding: 0;
      transition: all 0.22s;
    }
    .c-dot-btn.active { background: var(--red-soft); width: 22px; border-radius: 4px; }
    .c-arrow {
      width: 28px; height: 28px; border-radius: 50%;
      background: rgba(255,255,255,0.07);
      border: 1px solid rgba(255,255,255,0.1);
      color: rgba(255,255,255,0.6); font-size: 14px;
      cursor: pointer; display: flex; align-items: center; justify-content: center;
      transition: background 0.2s, color 0.2s;
    }
    .c-arrow:hover { background: rgba(255,255,255,0.14); color: #fff; }
    .c-arrow-right { margin-left: auto; }

    .lp-card {
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 14px; padding: 16px 20px;
      display: flex; align-items: center; gap: 12px;
    }
    .lp-card-avatar {
      width: 38px; height: 38px;
      background: linear-gradient(135deg, var(--red), var(--red-soft));
      border-radius: 50%; display: flex; align-items: center; justify-content: center;
      font-size: 17px; flex-shrink: 0;
    }
    .lp-card-quote { font-size: 12.5px; color: var(--sand); line-height: 1.5; font-style: italic; font-weight: 300; }
    .lp-card-author { font-size: 10.5px; color: var(--txt3); margin-top: 3px; font-style: normal; }

    /* ══ RIGHT PANEL ══ */
    .right-panel {
      background: var(--cream);
      display: flex; flex-direction: column;
      overflow-y: auto;
      animation: formIn 0.65s cubic-bezier(.22,1,.36,1) both;
      animation-delay: 0.1s;
    }
    @keyframes formIn {
      from { opacity: 0; transform: translateX(24px); }
      to   { opacity: 1; transform: translateX(0); }
    }
    .right-inner {
      flex: 1; display: flex; flex-direction: column;
      justify-content: center;
      padding: 44px 9% 44px 8%;
      max-width: 500px; width: 100%; margin: 0 auto;
    }

    .back-link {
      display: inline-flex; align-items: center; gap: 6px;
      font-size: 13px; color: var(--txt3);
      text-decoration: none; margin-bottom: 36px;
      transition: color 0.18s;
    }
    .back-link:hover { color: var(--red); }
    .back-link:hover .b-arr { transform: translateX(-3px); }
    .b-arr { transition: transform 0.18s; display: inline-block; }

    /* ── TABS ── */
    .tab-bar {
      display: flex;
      background: var(--cream-dark);
      border-radius: var(--rm); padding: 4px;
      margin-bottom: 30px;
      border: 1px solid var(--cream-mid);
    }
    .tab-btn {
      flex: 1; padding: 10px 8px;
      border: none; background: transparent;
      border-radius: 9px;
      font-family: 'Outfit', sans-serif;
      font-size: 13.5px; font-weight: 500;
      color: var(--txt3); cursor: pointer;
      transition: all 0.2s;
    }
    .tab-btn.active {
      background: var(--white); color: var(--txt);
      box-shadow: 0 2px 8px rgba(44,26,16,0.08);
    }

    /* ── FORM PANELS — THE FIX ── */
    .form-panel        { display: none; }
    .form-panel.active { display: block; }
    .success-screen        { display: none; flex-direction: column; align-items: center; text-align: center; padding: 16px 0; }
    .success-screen.show   { display: flex; }

    .form-eyebrow {
      font-size: 11px; font-weight: 600;
      letter-spacing: 0.12em; text-transform: uppercase;
      color: var(--red); margin-bottom: 8px;
      display: flex; align-items: center; gap: 6px;
    }
    .form-eyebrow::before { content: ''; display: inline-block; width: 16px; height: 2px; background: var(--red); }
    .form-title {
      font-family: 'Playfair Display', serif;
      font-size: clamp(24px, 2.8vw, 32px); font-weight: 800;
      color: var(--dark); line-height: 1.15; margin-bottom: 7px;
    }
    .form-title em { font-style: italic; color: var(--red-muted); }
    .form-sub { font-size: 13.5px; color: var(--txt2); font-weight: 300; line-height: 1.6; margin-bottom: 22px; }

    .alert { padding: 11px 15px; border-radius: var(--rm); font-size: 13px; line-height: 1.5; margin-bottom: 14px; display: none; }
    .alert.show { display: block; }
    .alert.err  { background: #FEE9E7; color: var(--red-deep); border: 1px solid rgba(192,57,43,0.15); }
    .alert.ok   { background: #F0FBF4; color: #166534; border: 1px solid rgba(22,101,52,0.15); }

    .field { margin-bottom: 14px; }
    .field-label { display: block; font-size: 11px; font-weight: 600; letter-spacing: 0.07em; text-transform: uppercase; color: var(--txt2); margin-bottom: 6px; }
    .field-wrap  { position: relative; }
    .field-input {
      width: 100%; height: 44px; padding: 0 13px 0 40px;
      border: 1.5px solid var(--cream-mid); border-radius: var(--rm);
      background: var(--white);
      font-family: 'Outfit', sans-serif; font-size: 14px; color: var(--txt);
      outline: none; transition: border-color 0.18s, box-shadow 0.18s;
    }
    .field-input:focus { border-color: var(--red); box-shadow: 0 0 0 3px rgba(192,57,43,0.07); }
    .field-input.error { border-color: var(--red); }
    .field-input::placeholder { color: var(--sand); }
    .field-icon {
      position: absolute; left: 12px; top: 50%; transform: translateY(-50%);
      width: 15px; height: 15px; color: var(--txt3); pointer-events: none;
    }
    .field-error { font-size: 11.5px; color: var(--red); margin-top: 4px; display: none; }
    .field-error.show { display: block; }

    .role-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 8px; margin-bottom: 14px; }
    .role-card {
      padding: 11px 6px; border: 1.5px solid var(--cream-mid);
      border-radius: var(--rm); cursor: pointer; text-align: center;
      background: var(--white); transition: all 0.16s;
    }
    .role-card:hover { border-color: var(--red-muted); background: #FEF9F5; }
    .role-card.selected { border-color: var(--red); background: #FEF0EE; }
    .role-card input { display: none; }
    .role-icon { font-size: 18px; display: block; margin-bottom: 4px; }
    .role-name { font-size: 11.5px; font-weight: 600; color: var(--dark); }
    .role-desc { font-size: 9.5px; color: var(--txt3); margin-top: 1px; }

    .pw-strength { margin-top: 7px; display: none; }
    .pw-strength.show { display: block; }
    .pw-bars { display: flex; gap: 4px; margin-bottom: 4px; }
    .pw-bar  { flex: 1; height: 3px; border-radius: 2px; background: var(--cream-mid); transition: background 0.2s; }
    .pw-bar.weak   { background: var(--red); }
    .pw-bar.fair   { background: #D4854A; }
    .pw-bar.strong { background: #5C9E6E; }
    .pw-label { font-size: 11px; color: var(--txt3); }
    .pw-rules { display: flex; flex-direction: column; gap: 3px; margin-top: 7px; }
    .rule { display: flex; align-items: center; gap: 5px; font-size: 11px; color: var(--txt3); transition: color 0.15s; }
    .rule.ok { color: #3A7D55; }
    .rule-dot { width: 4px; height: 4px; border-radius: 50%; background: currentColor; flex-shrink: 0; }

    .btn-submit {
      width: 100%; height: 46px; border: none; border-radius: var(--rm);
      background: var(--red); color: #fff;
      font-family: 'Outfit', sans-serif; font-size: 14.5px; font-weight: 600;
      cursor: pointer; margin-top: 4px;
      transition: background 0.18s, transform 0.1s, box-shadow 0.18s;
      box-shadow: 0 5px 18px rgba(192,57,43,0.24);
      display: flex; align-items: center; justify-content: center; gap: 7px;
    }
    .btn-submit:hover { background: var(--red-deep); transform: translateY(-1px); box-shadow: 0 9px 26px rgba(192,57,43,0.3); }
    .btn-submit:active { transform: scale(0.99); }
    .btn-submit:disabled { opacity: 0.7; pointer-events: none; }

    .divider { display: flex; align-items: center; gap: 10px; margin: 16px 0; font-size: 12px; color: var(--txt3); }
    .divider::before, .divider::after { content: ''; flex: 1; height: 1px; background: var(--cream-mid); }

    .success-icon { width: 68px; height: 68px; background: #F0FBF4; border-radius: 50%; border: 2px solid rgba(22,101,52,0.15); display: flex; align-items: center; justify-content: center; font-size: 30px; margin-bottom: 18px; }
    .success-title { font-family: 'Playfair Display', serif; font-size: 24px; font-weight: 800; color: var(--dark); margin-bottom: 8px; }
    .success-msg { font-size: 13.5px; color: var(--txt2); line-height: 1.6; max-width: 280px; margin-bottom: 16px; font-weight: 300; }
    .success-badge { background: var(--white); border: 1px solid var(--cream-mid); border-radius: var(--rm); padding: 10px 18px; font-size: 13px; color: var(--txt2); margin-bottom: 22px; }
    .success-badge strong { color: var(--dark); }
    .btn-back { padding: 9px 26px; border: 1.5px solid var(--cream-mid); border-radius: var(--rm); background: transparent; font-family: 'Outfit', sans-serif; font-size: 13px; color: var(--txt2); cursor: pointer; transition: all 0.18s; }
    .btn-back:hover { border-color: var(--red); color: var(--red); }

    @media (max-width: 860px) {
      .auth-root { grid-template-columns: 1fr; }
      .left-panel { padding: 32px 28px; min-height: auto; }
      .lp-dots, .lp-card { display: none; }
      .right-inner { padding: 36px 7%; max-width: 100%; }
    }
    @media (max-width: 460px) { .role-grid { grid-template-columns: 1fr 1fr; } }
  </style>
</head>
<body>
<div class="auth-root">

  <!-- ══ LEFT ══ -->
  <div class="left-panel">
    <div class="lp-grid"></div>
    <div class="lp-dots">
      <div class="lp-dot"></div><div class="lp-dot on"></div>
      <div class="lp-dot"></div><div class="lp-dot"></div><div class="lp-dot"></div>
    </div>

    <div class="lp-top">
      <a href="home.html" class="logo-link">
        <div class="logo-mark">🌶️</div>
        <div><div class="logo-name">SpicyTech</div><div class="logo-sub">Coworking Space</div></div>
      </a>
    </div>

    <div class="lp-mid">
      <div class="carousel">
        <div class="c-slides" id="c-slides">
          <div class="c-slide active">
            <h2 class="slide-title">Tu espacio,<br><em>tu ritmo,</em><br>tu comunidad.</h2>
            <p class="slide-desc">Accedé a escritorios, salas y oficinas privadas. Todo para trabajar en serio.</p>
            <div class="slide-pills">
              <div class="slide-pill"><div class="pill-icon">📡</div><span class="pill-text">WiFi 500 Mbps incluido</span></div>
              <div class="slide-pill"><div class="pill-icon">🔒</div><span class="pill-text">Acceso seguro 24/7</span></div>
              <div class="slide-pill"><div class="pill-icon">☕</div><span class="pill-text">Cafetería ilimitada</span></div>
            </div>
          </div>
          <div class="c-slide">
            <h2 class="slide-title">Reservá en<br><em>segundos,</em><br>trabajá ya.</h2>
            <p class="slide-desc">Sistema en tiempo real. Sin conflictos de doble reserva, sin llamadas, sin papeles.</p>
            <div class="slide-pills">
              <div class="slide-pill"><div class="pill-icon">📅</div><span class="pill-text">Reservas en tiempo real</span></div>
              <div class="slide-pill"><div class="pill-icon">📊</div><span class="pill-text">Historial de uso</span></div>
              <div class="slide-pill"><div class="pill-icon">🔔</div><span class="pill-text">Notificaciones automáticas</span></div>
            </div>
          </div>
          <div class="c-slide">
            <h2 class="slide-title">Crecé con<br>tu empresa,<br><em>crecé aquí.</em></h2>
            <p class="slide-desc">Desde freelancers hasta equipos. Oficinas privadas y todo el soporte necesario.</p>
            <div class="slide-pills">
              <div class="slide-pill"><div class="pill-icon">💺</div><span class="pill-text">Mobiliario ergonómico</span></div>
              <div class="slide-pill"><div class="pill-icon">🖨️</div><span class="pill-text">Impresión y escaneo</span></div>
              <div class="slide-pill"><div class="pill-icon">🤝</div><span class="pill-text">Comunidad activa</span></div>
            </div>
          </div>
        </div>
        <div class="c-nav">
          <button class="c-dot-btn active" onclick="goSlide(0)"></button>
          <button class="c-dot-btn"        onclick="goSlide(1)"></button>
          <button class="c-dot-btn"        onclick="goSlide(2)"></button>
          <button class="c-arrow"          onclick="prevSlide()">‹</button>
          <button class="c-arrow c-arrow-right" onclick="nextSlide()">›</button>
        </div>
      </div>
    </div>

    <div class="lp-bot">
      <div class="lp-card">
        <div class="lp-card-avatar">🙌</div>
        <div>
          <div class="lp-card-quote">"El mejor espacio para trabajar que encontré en la ciudad."</div>
          <div class="lp-card-author">— Miembro SpicyTech desde 2025</div>
        </div>
      </div>
    </div>
  </div>

  <!-- ══ RIGHT ══ -->
  <div class="right-panel">
    <div class="right-inner">

      <a href="home.html" class="back-link"><span class="b-arr">←</span> Volver al inicio</a>

      <div class="tab-bar">
        <button class="tab-btn active" id="tab-login"  onclick="switchTab('login')">Iniciar sesión</button>
        <button class="tab-btn"        id="tab-signup" onclick="switchTab('signup')">Crear cuenta</button>
      </div>

      <!-- LOGIN -->
      <div class="form-panel active" id="panel-login">
        <div class="form-eyebrow">Acceso</div>
        <h1 class="form-title">Bienvenido <em>de vuelta</em></h1>
        <p class="form-sub">Ingresá tus credenciales para acceder al sistema de reservas.</p>
        <div class="alert" id="login-alert"></div>
        <div class="field">
          <label class="field-label">Nombre de usuario</label>
          <div class="field-wrap">
            <svg class="field-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.6-7 8-7s8 3 8 7"/></svg>
            <input class="field-input" type="text" id="login-username" placeholder="tu_usuario" autocomplete="username">
          </div>
          <span class="field-error" id="err-lu"></span>
        </div>
        <div class="field">
          <label class="field-label">Contraseña</label>
          <div class="field-wrap">
            <svg class="field-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg>
            <input class="field-input" type="password" id="login-password" placeholder="••••••••" autocomplete="current-password">
          </div>
          <span class="field-error" id="err-lp"></span>
        </div>
        <button class="btn-submit" id="btn-login" onclick="doLogin()">Iniciar sesión →</button>
        <div class="divider">o</div>
        <p style="text-align:center;font-size:13px;color:var(--txt2);">¿No tenés cuenta? <a href="#" onclick="switchTab('signup');return false;" style="color:var(--red);text-decoration:none;font-weight:600;">Registrate gratis</a></p>
      </div>

      <!-- SIGNUP -->
      <div class="form-panel" id="panel-signup">
        <div class="form-eyebrow">Registro</div>
        <h1 class="form-title">Creá tu <em>cuenta</em></h1>
        <p class="form-sub">Elegí tu tipo de acceso y completá tus datos.</p>
        <div class="alert" id="signup-alert"></div>
        <label class="field-label" style="display:block;margin-bottom:7px;">Tipo de cuenta</label>
        <div class="role-grid">
          <label class="role-card selected" id="role-member"><input type="radio" name="role" value="member" checked><span class="role-icon">🪑</span><div class="role-name">Miembro</div><div class="role-desc">Reservas personales</div></label>
          <label class="role-card" id="role-admin"><input type="radio" name="role" value="admin"><span class="role-icon">⚙️</span><div class="role-name">Admin</div><div class="role-desc">Gestión total</div></label>
          <label class="role-card" id="role-guest"><input type="radio" name="role" value="guest"><span class="role-icon">👁️</span><div class="role-name">Invitado</div><div class="role-desc">Solo lectura</div></label>
        </div>
        <div class="field">
          <label class="field-label">Nombre de usuario</label>
          <div class="field-wrap">
            <svg class="field-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.6-7 8-7s8 3 8 7"/></svg>
            <input class="field-input" type="text" id="su-username" placeholder="mi_usuario" oninput="valU()" autocomplete="username">
          </div>
          <span class="field-error" id="err-su"></span>
        </div>
        <div class="field">
          <label class="field-label">Correo electrónico</label>
          <div class="field-wrap">
            <svg class="field-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M2 7l10 7 10-7"/></svg>
            <input class="field-input" type="email" id="su-email" placeholder="vos@ejemplo.com" oninput="valE()" autocomplete="email">
          </div>
          <span class="field-error" id="err-se"></span>
        </div>
        <div class="field">
          <label class="field-label">Contraseña</label>
          <div class="field-wrap">
            <svg class="field-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg>
            <input class="field-input" type="password" id="su-password" placeholder="••••••••" oninput="valP()" autocomplete="new-password">
          </div>
          <div class="pw-strength" id="pw-str">
            <div class="pw-bars"><div class="pw-bar" id="b1"></div><div class="pw-bar" id="b2"></div><div class="pw-bar" id="b3"></div><div class="pw-bar" id="b4"></div></div>
            <span class="pw-label" id="pw-lbl">—</span>
          </div>
          <div class="pw-rules">
            <div class="rule" id="r-len"><span class="rule-dot"></span>Mínimo 8 caracteres</div>
            <div class="rule" id="r-up"><span class="rule-dot"></span>Una mayúscula</div>
            <div class="rule" id="r-lo"><span class="rule-dot"></span>Una minúscula</div>
            <div class="rule" id="r-nu"><span class="rule-dot"></span>Un número</div>
            <div class="rule" id="r-sp"><span class="rule-dot"></span>Un carácter especial</div>
          </div>
          <span class="field-error" id="err-sp"></span>
        </div>
        <div class="field">
          <label class="field-label">Confirmar contraseña</label>
          <div class="field-wrap">
            <svg class="field-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg>
            <input class="field-input" type="password" id="su-confirm" placeholder="••••••••" oninput="valC()" autocomplete="new-password">
          </div>
          <span class="field-error" id="err-sc"></span>
        </div>
        <button class="btn-submit" id="btn-signup" onclick="doSignup()">Crear cuenta →</button>
        <div class="divider">o</div>
        <p style="text-align:center;font-size:13px;color:var(--txt2);">¿Ya tenés cuenta? <a href="#" onclick="switchTab('login');return false;" style="color:var(--red);text-decoration:none;font-weight:600;">Iniciá sesión</a></p>
      </div>

      <!-- SUCCESS -->
      <div class="success-screen" id="success-screen">
        <div class="success-icon">✓</div>
        <h2 class="success-title" id="s-title">¡Listo!</h2>
        <p class="success-msg" id="s-msg"></p>
        <div class="success-badge" id="s-badge"></div>
        <button class="btn-back" onclick="backToForm()">Volver al acceso</button>
      </div>

    </div>
  </div>
</div>

<script>
/* ── CAROUSEL ── */
let cur = 0, total = 3, timer;
function goSlide(n) {
  document.querySelectorAll('.c-slide').forEach((s,i) => s.classList.toggle('active', i===n));
  document.querySelectorAll('.c-dot-btn').forEach((d,i) => d.classList.toggle('active', i===n));
  cur = n;
}
function nextSlide() { goSlide((cur+1)%total); resetTimer(); }
function prevSlide() { goSlide((cur-1+total)%total); resetTimer(); }
function resetTimer() { clearInterval(timer); timer = setInterval(nextSlide, 5000); }
timer = setInterval(nextSlide, 5000);

/* ── TABS ── */
function switchTab(tab) {
  document.getElementById('tab-login').classList.toggle('active',   tab==='login');
  document.getElementById('tab-signup').classList.toggle('active',  tab==='signup');
  document.getElementById('panel-login').classList.toggle('active', tab==='login');
  document.getElementById('panel-signup').classList.toggle('active',tab==='signup');
  document.getElementById('success-screen').classList.remove('show');
  clearAlerts();
}
window.addEventListener('DOMContentLoaded', () => {
  if (location.hash === '#signup') switchTab('signup');
});

/* ── HELPERS ── */
const API = 'http://127.0.0.1:5000/api/auth';
function clearAlerts() {
  ['login-alert','signup-alert'].forEach(id => { const e=document.getElementById(id); if(e){e.className='alert';e.textContent='';} });
}
function showAlert(id, msg, type) {
  const e=document.getElementById(id); if(!e) return;
  e.textContent=msg; e.className=`alert show ${type}`;
}
function setErr(iId, eId, msg) {
  const i=document.getElementById(iId), e=document.getElementById(eId); if(!i||!e) return;
  if(msg){ i.classList.add('error'); e.textContent=msg; e.classList.add('show'); }
  else   { i.classList.remove('error'); e.textContent=''; e.classList.remove('show'); }
}
function storeToken(t) { if(t) localStorage.setItem('nexo_token',t); }

/* ── VALIDATIONS ── */
function valU() {
  const v=document.getElementById('su-username').value.trim();
  if(v&&v.length<3)              setErr('su-username','err-su','Mínimo 3 caracteres');
  else if(v&&!/^[a-zA-Z0-9_]+$/.test(v)) setErr('su-username','err-su','Solo letras, números y _');
  else setErr('su-username','err-su','');
}
function valE() {
  const v=document.getElementById('su-email').value.trim();
  if(v&&!/^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$/.test(v)) setErr('su-email','err-se','Email inválido');
  else setErr('su-email','err-se','');
}
function valC() {
  const p=document.getElementById('su-password').value, c=document.getElementById('su-confirm').value;
  if(c&&p!==c) setErr('su-confirm','err-sc','Las contraseñas no coinciden');
  else setErr('su-confirm','err-sc','');
}
function valP() {
  const pw=document.getElementById('su-password').value;
  document.getElementById('pw-str').classList.toggle('show', pw.length>0);
  const ch={'r-len':pw.length>=8,'r-up':/[A-Z]/.test(pw),'r-lo':/[a-z]/.test(pw),'r-nu':/\d/.test(pw),'r-sp':/[!@#$%^&*(),.?":{}|<>]/.test(pw)};
  Object.entries(ch).forEach(([id,ok])=>document.getElementById(id)?.classList.toggle('ok',ok));
  const score=Object.values(ch).filter(Boolean).length;
  const bars=['b1','b2','b3','b4'].map(id=>document.getElementById(id));
  const lbl=document.getElementById('pw-lbl');
  bars.forEach(b=>b&&(b.className='pw-bar'));
  const cfg=[null,{f:'weak',l:'Débil',c:'var(--red)',n:1},{f:'fair',l:'Regular',c:'#D4854A',n:2},{f:'fair',l:'Regular',c:'#D4854A',n:2},{f:'strong',l:'Buena',c:'#5C9E6E',n:3},{f:'strong',l:'Excelente',c:'#3A7D55',n:4}][score]||{f:'weak',l:'Débil',c:'var(--red)',n:1};
  for(let i=0;i<cfg.n;i++) bars[i]?.classList.add(cfg.f);
  lbl.textContent=cfg.l; lbl.style.color=cfg.c;
  if(document.getElementById('su-confirm').value) valC();
}

/* Role cards */
document.querySelectorAll('.role-card').forEach(c=>{
  c.addEventListener('click',()=>{
    document.querySelectorAll('.role-card').forEach(x=>x.classList.remove('selected'));
    c.classList.add('selected');
    c.querySelector('input[type="radio"]').checked=true;
  });
});

/* ── API ── */
async function doLogin() {
  const btn=document.getElementById('btn-login');
  const u=document.getElementById('login-username').value.trim();
  const p=document.getElementById('login-password').value;
  if(!u){setErr('login-username','err-lu','Ingresá tu usuario');return;}
  if(!p){setErr('login-password','err-lp','Ingresá tu contraseña');return;}
  btn.disabled=true; btn.textContent='Verificando…';
  try {
    const r=await fetch(API+'/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u,password:p})});
    const d=await r.json();
    if(d.success&&d.data){
      storeToken(d.data.token);
      showSuccess('¡Bienvenido de vuelta!','Iniciaste sesión en el sistema de reservas de SpicyTech.',`Conectado como <strong>${d.data.username}</strong> · ${d.data.role}`);
    } else showAlert('login-alert',d.message||'Credenciales inválidas.','err');
  } catch { showAlert('login-alert','No se pudo conectar. ¿Flask corriendo en :5000?','err'); }
  finally { btn.disabled=false; btn.innerHTML='Iniciar sesión →'; }
}

async function doSignup() {
  const btn=document.getElementById('btn-signup');
  const u=document.getElementById('su-username').value.trim();
  const m=document.getElementById('su-email').value.trim().toLowerCase();
  const p=document.getElementById('su-password').value;
  const c=document.getElementById('su-confirm').value;
  const role=document.querySelector('input[name="role"]:checked')?.value||'member';
  btn.disabled=true; btn.textContent='Creando cuenta…';
  try {
    const r=await fetch(API+'/signup',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:u,email:m,password:p,confirm_password:c,role})});
    const d=await r.json();
    if(d.success){
      showSuccess('¡Cuenta creada!','Tu cuenta fue registrada y guardada en la base de datos.',`<strong>${d.data.username}</strong> · ${d.data.email} · ${d.data.role}`);
    } else {
      const msg=d.errors?.length?d.errors.join(' '):(d.message||'Error al crear la cuenta.');
      showAlert('signup-alert',msg,'err');
    }
  } catch { showAlert('signup-alert','No se pudo conectar. ¿Flask corriendo en :5000?','err'); }
  finally { btn.disabled=false; btn.innerHTML='Crear cuenta →'; }
}

function showSuccess(title,msg,info) {
  document.getElementById('panel-login').classList.remove('active');
  document.getElementById('panel-signup').classList.remove('active');
  document.querySelector('.tab-bar').style.visibility='hidden';
  document.getElementById('s-title').textContent=title;
  document.getElementById('s-msg').textContent=msg;
  document.getElementById('s-badge').innerHTML=info;
  document.getElementById('success-screen').classList.add('show');
}
function backToForm() {
  document.getElementById('success-screen').classList.remove('show');
  document.querySelector('.tab-bar').style.visibility='';
  switchTab('login');
}

document.addEventListener('keydown',e=>{
  if(e.key!=='Enter') return;
  if(document.getElementById('panel-login').classList.contains('active'))  doLogin();
  if(document.getElementById('panel-signup').classList.contains('active')) doSignup();
});
</script>
</body>
</html>

## C:\Users\User\Desktop\TP1_ingenieria_II\src\tests.py

```python
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

```

## C:\Users\User\Desktop\TP1_ingenieria_II\tests\test.md

```md

```
