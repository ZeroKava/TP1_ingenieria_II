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
┃ ┣ index.html
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

## C:\Users\User\Desktop\TP1_ingenieria_II\src\index.html

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
  <title>Nexo Coworking · Acceso seguro</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500&display=swap');

    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --brand: #1D9E75;
      --brand-dark: #0F6E56;
      --brand-light: #E1F5EE;
      --accent: #D85A30;
      --surface: #ffffff;
      --surface2: #f8fafc;
      --border: #e2e8f0;
      --border2: #cbd5e1;
      --txt: #0f172a;
      --txt2: #475569;
      --txt3: #94a3b8;
      --danger: #b91c1c;
      --danger-bg: #fee2e2;
      --success-txt: #166534;
      --success-bg: #dcfce7;
      --r: 20px;
      --rm: 12px;
    }

    body {
      background: linear-gradient(135deg, #f1f5f9 0%, #e6edf4 100%);
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
      font-family: 'DM Sans', sans-serif;
    }

    #cw-root {
      max-width: 1200px;
      width: 100%;
      background: var(--surface);
      border-radius: var(--r);
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
      display: flex;
      flex-wrap: wrap;
      overflow: hidden;
      transition: all 0.2s;
    }

    /* ── PANEL IZQUIERDO ── */
    .side-panel {
      width: 300px;
      background: #085041;
      padding: 2rem 1.8rem;
      display: flex;
      flex-direction: column;
      position: relative;
      overflow: hidden;
      color: white;
    }

    .side-panel::before {
      content: '';
      position: absolute;
      top: -80px; right: -80px;
      width: 260px; height: 260px;
      border-radius: 50%;
      background: rgba(255,255,255,0.04);
    }
    .side-panel::after {
      content: '';
      position: absolute;
      bottom: -60px; left: -60px;
      width: 220px; height: 220px;
      border-radius: 50%;
      background: rgba(255,255,255,0.04);
    }

    .logo {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 2.5rem;
      position: relative; z-index: 1;
    }
    .logo-mark {
      width: 36px; height: 36px;
      background: #1D9E75;
      border-radius: 8px;
      display: flex; align-items: center; justify-content: center;
    }
    .logo-mark svg { width: 20px; height: 20px; fill: #fff; }
    .logo-name {
      font-family: 'DM Serif Display', serif;
      font-size: 18px;
      color: #fff;
      letter-spacing: -0.3px;
    }
    .logo-sub { font-size: 11px; color: rgba(255,255,255,0.5); margin-top: 1px; }

    .side-tagline {
      font-family: 'DM Serif Display', serif;
      font-size: 28px;
      line-height: 1.25;
      color: #fff;
      margin-bottom: 1.25rem;
      position: relative; z-index: 1;
    }
    .side-tagline em { font-style: italic; color: #5DCAA5; }

    .side-desc {
      font-size: 13px;
      color: rgba(255,255,255,0.55);
      line-height: 1.7;
      margin-bottom: 2rem;
      position: relative; z-index: 1;
    }

    .side-features {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 12px;
      position: relative; z-index: 1;
    }
    .side-features li {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 13px;
      color: rgba(255,255,255,0.7);
    }
    .feat-dot {
      width: 6px; height: 6px;
      border-radius: 50%;
      background: #1D9E75;
      flex-shrink: 0;
    }

    .side-footer {
      margin-top: auto;
      font-size: 11px;
      color: rgba(255,255,255,0.3);
      position: relative; z-index: 1;
    }

    /* ── PANEL DERECHO ── */
    .main-panel {
      flex: 1;
      background: var(--surface);
      padding: 2rem 2rem 2rem 2rem;
      display: flex;
      flex-direction: column;
      min-width: 280px;
    }

    /* ── TABS ── */
    .tab-bar {
      display: flex;
      gap: 4px;
      background: var(--surface2);
      border-radius: var(--rm);
      padding: 4px;
      margin-bottom: 2rem;
      border: 0.5px solid var(--border);
    }
    .tab-btn {
      flex: 1;
      padding: 8px;
      border: none;
      background: transparent;
      border-radius: 6px;
      font-family: 'DM Sans', sans-serif;
      font-size: 13px;
      font-weight: 500;
      color: var(--txt2);
      cursor: pointer;
      transition: background 0.15s, color 0.15s;
    }
    .tab-btn.active {
      background: var(--surface);
      color: var(--txt);
      border: 0.5px solid var(--border2);
    }

    /* ── FORM HEADER ── */
    .form-header { margin-bottom: 1.5rem; }
    .form-title {
      font-family: 'DM Serif Display', serif;
      font-size: 24px;
      color: var(--txt);
      margin-bottom: 4px;
    }
    .form-subtitle { font-size: 13px; color: var(--txt2); line-height: 1.5; }

    /* ── FORM FIELDS ── */
    .field { margin-bottom: 1rem; }
    .field-label {
      display: block;
      font-size: 12px;
      font-weight: 500;
      color: var(--txt2);
      margin-bottom: 6px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .field-wrap { position: relative; }
    .field-input {
      width: 100%;
      height: 40px;
      padding: 0 12px 0 36px;
      border: 0.5px solid var(--border2);
      border-radius: var(--rm);
      background: var(--surface);
      font-family: 'DM Sans', sans-serif;
      font-size: 14px;
      color: var(--txt);
      outline: none;
      transition: border-color 0.15s;
    }
    .field-input:focus { border-color: var(--brand); border-width: 1px; }
    .field-input.error { border-color: var(--danger); }
    .field-icon {
      position: absolute;
      left: 10px; top: 50%;
      transform: translateY(-50%);
      width: 16px; height: 16px;
      color: var(--txt3);
      pointer-events: none;
    }
    .field-error {
      font-size: 11.5px;
      color: var(--danger);
      margin-top: 4px;
      display: none;
    }
    .field-error.show { display: block; }

    /* ── PASSWORD STRENGTH ── */
    .pw-strength {
      margin-top: 8px;
      display: none;
    }
    .pw-strength.show { display: block; }
    .pw-bars {
      display: flex;
      gap: 4px;
      margin-bottom: 4px;
    }
    .pw-bar {
      flex: 1; height: 3px;
      border-radius: 2px;
      background: var(--border2);
      transition: background 0.2s;
    }
    .pw-bar.fill-weak   { background: #E24B4A; }
    .pw-bar.fill-fair   { background: #EF9F27; }
    .pw-bar.fill-strong { background: #1D9E75; }
    .pw-label { font-size: 11px; color: var(--txt3); }

    /* ── RULES CHECK ── */
    .pw-rules {
      display: flex;
      flex-direction: column;
      gap: 4px;
      margin-top: 8px;
    }
    .rule {
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 11.5px;
      color: var(--txt3);
      transition: color 0.15s;
    }
    .rule.ok { color: var(--success-txt); }
    .rule-dot {
      width: 5px; height: 5px;
      border-radius: 50%;
      background: currentColor;
      flex-shrink: 0;
    }

    /* ── ALERT ── */
    .alert {
      padding: 10px 14px;
      border-radius: var(--rm);
      font-size: 13px;
      margin-bottom: 1rem;
      display: none;
    }
    .alert.show { display: block; }
    .alert.err { background: var(--danger-bg); color: var(--danger); }
    .alert.ok  { background: var(--success-bg); color: var(--success-txt); }

    /* ── SUBMIT BTN ── */
    .btn-submit {
      width: 100%;
      height: 42px;
      border: none;
      border-radius: var(--rm);
      background: #085041;
      color: #fff;
      font-family: 'DM Sans', sans-serif;
      font-size: 14px;
      font-weight: 500;
      cursor: pointer;
      margin-top: 0.25rem;
      transition: background 0.15s, transform 0.1s;
    }
    .btn-submit:hover { background: #0F6E56; }
    .btn-submit:active { transform: scale(0.99); }
    .btn-submit.loading { pointer-events: none; opacity: 0.7; }

    /* ── ROLE SELECTOR ── */
    .role-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
      margin-bottom: 1rem;
    }
    .role-card {
      padding: 10px 8px;
      border: 0.5px solid var(--border2);
      border-radius: var(--rm);
      cursor: pointer;
      text-align: center;
      transition: all 0.15s;
      background: var(--surface);
    }
    .role-card:hover { background: var(--surface2); }
    .role-card.selected {
      border-color: var(--brand);
      border-width: 1.5px;
      background: var(--brand-light);
    }
    .role-card input { display: none; }
    .role-icon { font-size: 18px; margin-bottom: 4px; display: block; }
    .role-name { font-size: 12px; font-weight: 500; color: var(--txt); }
    .role-desc { font-size: 10px; color: var(--txt2); margin-top: 2px; }

    /* ── DIVIDER ── */
    .divider {
      display: flex; align-items: center; gap: 12px;
      margin: 1.25rem 0;
      font-size: 12px; color: var(--txt3);
    }
    .divider::before, .divider::after {
      content: ''; flex: 1;
      height: 0.5px; background: var(--border);
    }

    /* ── PANEL HIDDEN ── */
    .form-panel { display: none; }
    .form-panel.active { display: block; }

    /* ── SUCCESS STATE ── */
    .success-screen {
      display: none;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 2rem;
      flex: 1;
    }
    .success-screen.show { display: flex; }
    .success-icon {
      width: 64px; height: 64px;
      border-radius: 50%;
      background: var(--success-bg);
      display: flex; align-items: center; justify-content: center;
      margin-bottom: 1.25rem;
    }
    .success-icon svg { width: 32px; height: 32px; stroke: var(--success-txt); }
    .success-title {
      font-family: 'DM Serif Display', serif;
      font-size: 22px; color: var(--txt);
      margin-bottom: 8px;
    }
    .success-msg { font-size: 13px; color: var(--txt2); line-height: 1.6; max-width: 280px; }
    .success-user {
      margin-top: 1.5rem;
      padding: 12px 20px;
      background: var(--surface2);
      border-radius: var(--rm);
      border: 0.5px solid var(--border);
      font-size: 13px; color: var(--txt2);
    }
    .success-user strong { color: var(--txt); font-weight: 500; }
    .btn-back {
      margin-top: 1.5rem;
      padding: 9px 24px;
      background: transparent;
      border: 0.5px solid var(--border2);
      border-radius: var(--rm);
      font-family: 'DM Sans', sans-serif;
      font-size: 13px;
      color: var(--txt);
      cursor: pointer;
      transition: background 0.15s;
    }
    .btn-back:hover { background: var(--surface2); }

    @media (max-width: 700px) {
      #cw-root { flex-direction: column; }
      .side-panel { width: 100%; text-align: center; }
      .side-features { align-items: center; }
      .main-panel { padding: 1.5rem; }
    }
  </style>
</head>
<body>
<div id="cw-root">
  <div class="side-panel">
    <div class="logo">
      <div class="logo-mark">
        <svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22" fill="none" stroke="white" stroke-width="1.5" stroke-linecap="round"/></svg>
      </div>
      <div>
        <div class="logo-name">Nexo</div>
        <div class="logo-sub">Coworking Space</div>
      </div>
    </div>
    <p class="side-tagline">Tu espacio,<br><em>tu ritmo</em></p>
    <p class="side-desc">Reserva salas de reuniones, escritorios y espacios privados en minutos desde cualquier dispositivo.</p>
    <ul class="side-features">
      <li><span class="feat-dot"></span>Reservas en tiempo real</li>
      <li><span class="feat-dot"></span>Gestión de accesos</li>
      <li><span class="feat-dot"></span>Historial de uso</li>
      <li><span class="feat-dot"></span>Notificaciones automáticas</li>
    </ul>
    <div class="side-footer">© 2025 Nexo Coworking</div>
  </div>

  <div class="main-panel" id="main-panel">
    <div class="tab-bar">
      <button class="tab-btn active" id="tab-login" onclick="switchTab('login')">Iniciar sesión</button>
      <button class="tab-btn" id="tab-signup" onclick="switchTab('signup')">Crear cuenta</button>
    </div>

    <!-- LOGIN -->
    <div class="form-panel active" id="panel-login">
      <div class="form-header">
        <h2 class="form-title">Bienvenido de vuelta</h2>
        <p class="form-subtitle">Ingresa tus credenciales para acceder al sistema de reservas.</p>
      </div>
      <div class="alert" id="login-alert"></div>
      <div class="field">
        <label class="field-label">Nombre de usuario</label>
        <div class="field-wrap">
          <svg class="field-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.6-7 8-7s8 3 8 7"/></svg>
          <input class="field-input" type="text" id="login-username" placeholder="tu_usuario" autocomplete="username">
        </div>
        <span class="field-error" id="login-username-err"></span>
      </div>
      <div class="field">
        <label class="field-label">Contraseña</label>
        <div class="field-wrap">
          <svg class="field-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg>
          <input class="field-input" type="password" id="login-password" placeholder="••••••••" autocomplete="current-password">
        </div>
        <span class="field-error" id="login-password-err"></span>
      </div>
      <button class="btn-submit" id="btn-login" onclick="doLogin()">Iniciar sesión</button>
      <div class="divider">o</div>
      <p style="text-align:center; font-size: 13px; color: var(--txt2);">
        ¿No tenés cuenta? <a href="#" onclick="switchTab('signup'); return false;" style="color: var(--brand); text-decoration: none; font-weight: 500;">Registrate</a>
      </p>
    </div>

    <!-- SIGNUP -->
    <div class="form-panel" id="panel-signup">
      <div class="form-header">
        <h2 class="form-title">Creá tu cuenta</h2>
        <p class="form-subtitle">Elegí tu tipo de acceso y completá los datos.</p>
      </div>
      <div class="alert" id="signup-alert"></div>
      <label class="field-label" style="display:block; margin-bottom: 8px;">Tipo de cuenta</label>
      <div class="role-grid">
        <label class="role-card selected" id="role-member">
          <input type="radio" name="role" value="member" checked>
          <span class="role-icon">🪑</span>
          <div class="role-name">Miembro</div>
          <div class="role-desc">Reservas personales</div>
        </label>
        <label class="role-card" id="role-admin">
          <input type="radio" name="role" value="admin">
          <span class="role-icon">⚙️</span>
          <div class="role-name">Admin</div>
          <div class="role-desc">Gestión total</div>
        </label>
        <label class="role-card" id="role-guest">
          <input type="radio" name="role" value="guest">
          <span class="role-icon">👁️</span>
          <div class="role-name">Invitado</div>
          <div class="role-desc">Solo lectura</div>
        </label>
      </div>

      <div class="field">
        <label class="field-label">Nombre de usuario</label>
        <div class="field-wrap">
          <svg class="field-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.6-7 8-7s8 3 8 7"/></svg>
          <input class="field-input" type="text" id="su-username" placeholder="mi_usuario" oninput="validateUsernameField()" autocomplete="username">
        </div>
        <span class="field-error" id="su-username-err"></span>
      </div>

      <div class="field">
        <label class="field-label">Correo electrónico</label>
        <div class="field-wrap">
          <svg class="field-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M2 7l10 7 10-7"/></svg>
          <input class="field-input" type="email" id="su-email" placeholder="vos@ejemplo.com" oninput="validateEmailField()" autocomplete="email">
        </div>
        <span class="field-error" id="su-email-err"></span>
      </div>

      <div class="field">
        <label class="field-label">Contraseña</label>
        <div class="field-wrap">
          <svg class="field-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg>
          <input class="field-input" type="password" id="su-password" placeholder="••••••••" oninput="onPasswordInput()" autocomplete="new-password">
        </div>
        <div class="pw-strength" id="pw-strength">
          <div class="pw-bars">
            <div class="pw-bar" id="b1"></div>
            <div class="pw-bar" id="b2"></div>
            <div class="pw-bar" id="b3"></div>
            <div class="pw-bar" id="b4"></div>
          </div>
          <span class="pw-label" id="pw-label">—</span>
        </div>
        <div class="pw-rules" id="pw-rules">
          <div class="rule" id="r-len"><span class="rule-dot"></span>Mínimo 8 caracteres</div>
          <div class="rule" id="r-upper"><span class="rule-dot"></span>Una letra mayúscula</div>
          <div class="rule" id="r-lower"><span class="rule-dot"></span>Una letra minúscula</div>
          <div class="rule" id="r-num"><span class="rule-dot"></span>Un número</div>
          <div class="rule" id="r-special"><span class="rule-dot"></span>Un carácter especial</div>
        </div>
        <span class="field-error" id="su-password-err"></span>
      </div>

      <div class="field">
        <label class="field-label">Confirmar contraseña</label>
        <div class="field-wrap">
          <svg class="field-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg>
          <input class="field-input" type="password" id="su-confirm" placeholder="••••••••" oninput="validateConfirmField()" autocomplete="new-password">
        </div>
        <span class="field-error" id="su-confirm-err"></span>
      </div>

      <button class="btn-submit" id="btn-signup" onclick="doSignup()">Crear cuenta</button>
      <div class="divider">o</div>
      <p style="text-align:center; font-size: 13px; color: var(--txt2);">
        ¿Ya tenés cuenta? <a href="#" onclick="switchTab('login'); return false;" style="color: var(--brand); text-decoration: none; font-weight: 500;">Iniciá sesión</a>
      </p>
    </div>

    <!-- SUCCESS -->
    <div class="success-screen" id="success-screen">
      <div class="success-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>
      </div>
      <h2 class="success-title" id="success-title">¡Listo!</h2>
      <p class="success-msg" id="success-msg"></p>
      <div class="success-user" id="success-user"></div>
      <button class="btn-back" onclick="backToForm()">Volver al inicio</button>
    </div>
  </div>
</div>

<script>
  const API = 'http://localhost:5000/api/auth';

  // Almacenar token JWT
  function storeToken(token) {
    if (token) {
      localStorage.setItem('nexo_token', token);
      console.log('✅ Token JWT guardado');
    }
  }

  // Cambio de pestañas
  function switchTab(tab) {
    document.getElementById('tab-login').classList.toggle('active', tab === 'login');
    document.getElementById('tab-signup').classList.toggle('active', tab === 'signup');
    document.getElementById('panel-login').classList.toggle('active', tab === 'login');
    document.getElementById('panel-signup').classList.toggle('active', tab === 'signup');
    clearAlerts();
  }

  function clearAlerts() {
    ['login-alert','signup-alert'].forEach(id => {
      const el = document.getElementById(id);
      if (el) { el.className = 'alert'; el.textContent = ''; }
    });
  }

  function showAlert(id, msg, type) {
    const el = document.getElementById(id);
    if (!el) return;
    el.textContent = msg;
    el.className = `alert show ${type}`;
  }

  function setFieldError(fieldId, errId, msg) {
    const inp = document.getElementById(fieldId);
    const err = document.getElementById(errId);
    if (!inp || !err) return;
    if (msg) { inp.classList.add('error'); err.textContent = msg; err.classList.add('show'); }
    else { inp.classList.remove('error'); err.textContent = ''; err.classList.remove('show'); }
  }

  // Validaciones inline
  function validateUsernameField() {
    const v = document.getElementById('su-username')?.value.trim() || '';
    if (v.length > 0 && v.length < 3) setFieldError('su-username','su-username-err','Mínimo 3 caracteres');
    else if (v.length > 0 && !/^[a-zA-Z0-9_]+$/.test(v)) setFieldError('su-username','su-username-err','Solo letras, números y _');
    else setFieldError('su-username','su-username-err','');
  }

  function validateEmailField() {
    const v = document.getElementById('su-email')?.value.trim() || '';
    if (v.length > 0 && !/^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$/.test(v))
      setFieldError('su-email','su-email-err','Email inválido');
    else setFieldError('su-email','su-email-err','');
  }

  function validateConfirmField() {
    const pw = document.getElementById('su-password')?.value || '';
    const cf = document.getElementById('su-confirm')?.value || '';
    if (cf.length > 0 && pw !== cf) setFieldError('su-confirm','su-confirm-err','Las contraseñas no coinciden');
    else setFieldError('su-confirm','su-confirm-err','');
  }

  function onPasswordInput() {
    const pw = document.getElementById('su-password')?.value || '';
    const strengthDiv = document.getElementById('pw-strength');
    if (strengthDiv) strengthDiv.classList.toggle('show', pw.length > 0);

    const rules = {
      'r-len':     pw.length >= 8,
      'r-upper':   /[A-Z]/.test(pw),
      'r-lower':   /[a-z]/.test(pw),
      'r-num':     /\d/.test(pw),
      'r-special': /[!@#$%^&*(),.?":{}|<>]/.test(pw),
    };
    Object.entries(rules).forEach(([id, ok]) => {
      const el = document.getElementById(id);
      if (el) el.classList.toggle('ok', ok);
    });

    const score = Object.values(rules).filter(Boolean).length;
    const bars = [document.getElementById('b1'),document.getElementById('b2'),document.getElementById('b3'),document.getElementById('b4')];
    const label = document.getElementById('pw-label');
    if (!bars[0] || !label) return;
    bars.forEach(b => b.className = 'pw-bar');
    if (score <= 2) {
      bars[0]?.classList.add('fill-weak');
      label.textContent = 'Débil'; label.style.color = '#E24B4A';
    } else if (score <= 3) {
      bars[0]?.classList.add('fill-fair'); bars[1]?.classList.add('fill-fair');
      label.textContent = 'Regular'; label.style.color = '#EF9F27';
    } else if (score === 4) {
      [0,1,2].forEach(i => bars[i]?.classList.add('fill-strong'));
      label.textContent = 'Buena'; label.style.color = '#1D9E75';
    } else {
      bars.forEach(b => b?.classList.add('fill-strong'));
      label.textContent = 'Excelente'; label.style.color = '#1D9E75';
    }
    if (document.getElementById('su-confirm')?.value) validateConfirmField();
  }

  // Role cards interactivas
  document.querySelectorAll('.role-card').forEach(card => {
    card.addEventListener('click', () => {
      document.querySelectorAll('.role-card').forEach(c => c.classList.remove('selected'));
      card.classList.add('selected');
      const radio = card.querySelector('input[type="radio"]');
      if (radio) radio.checked = true;
    });
  });

  // Llamadas a la API real
  async function doLogin() {
    const btn = document.getElementById('btn-login');
    if (!btn) return;
    btn.classList.add('loading'); btn.textContent = 'Verificando…';

    const username = document.getElementById('login-username')?.value.trim() || '';
    const password = document.getElementById('login-password')?.value || '';

    try {
      const response = await fetch(API + '/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
      });
      const result = await response.json();

      if (result.success && result.data) {
        if (result.data.token) storeToken(result.data.token);
        showSuccess('¡Bienvenido!',
          'Has iniciado sesión exitosamente en el sistema de reservas.',
          `Conectado como <strong>${result.data.username}</strong> · ${result.data.role}`
        );
      } else {
        showAlert('login-alert', result.message || 'Credenciales inválidas', 'err');
      }
    } catch (error) {
      console.error(error);
      showAlert('login-alert', 'Error de conexión con el servidor (¿Flask corriendo en puerto 5000?)', 'err');
    } finally {
      btn.classList.remove('loading'); btn.textContent = 'Iniciar sesión';
    }
  }

  async function doSignup() {
    const btn = document.getElementById('btn-signup');
    if (!btn) return;
    btn.classList.add('loading'); btn.textContent = 'Creando cuenta…';

    const username = document.getElementById('su-username')?.value.trim() || '';
    const email    = document.getElementById('su-email')?.value.trim().toLowerCase() || '';
    const password = document.getElementById('su-password')?.value || '';
    const confirm  = document.getElementById('su-confirm')?.value || '';
    const roleRadio = document.querySelector('input[name="role"]:checked');
    const role = roleRadio ? roleRadio.value : 'member';

    try {
      const response = await fetch(API + '/signup', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, email, password, confirm_password: confirm, role })
      });
      const result = await response.json();

      if (result.success) {
        showSuccess('¡Cuenta creada!',
          'Tu cuenta fue registrada exitosamente. Ya podés iniciar sesión.',
          `<strong>${result.data.username}</strong> · ${result.data.email} · ${result.data.role}`
        );
      } else {
        const errorMsg = (result.errors && result.errors.length) ? result.errors.join(' ') : (result.message || 'Error al crear la cuenta');
        showAlert('signup-alert', errorMsg, 'err');
      }
    } catch (error) {
      console.error(error);
      showAlert('signup-alert', 'Error de conexión con el servidor', 'err');
    } finally {
      btn.classList.remove('loading'); btn.textContent = 'Crear cuenta';
    }
  }

  function showSuccess(title, msg, userInfo) {
    document.querySelectorAll('.form-panel').forEach(p => p.classList.remove('active'));
    const tabBar = document.querySelector('.tab-bar');
    if (tabBar) tabBar.style.display = 'none';
    const successTitle = document.getElementById('success-title');
    const successMsg = document.getElementById('success-msg');
    const successUser = document.getElementById('success-user');
    if (successTitle) successTitle.textContent = title;
    if (successMsg) successMsg.textContent = msg;
    if (successUser) successUser.innerHTML = userInfo;
    const successScreen = document.getElementById('success-screen');
    if (successScreen) successScreen.classList.add('show');
  }

  function backToForm() {
    const successScreen = document.getElementById('success-screen');
    if (successScreen) successScreen.classList.remove('show');
    const tabBar = document.querySelector('.tab-bar');
    if (tabBar) tabBar.style.display = '';
    switchTab('login');
  }

  // Inicialización: si ya hay token, se podría redirigir, pero dejamos que el usuario decida.
  window.onload = () => {
    const token = localStorage.getItem('nexo_token');
    if (token) console.log('🟢 Token existente, sesión potencialmente activa');
  };
</script>
</body>
</html>

```

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
