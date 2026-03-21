# Plan de Gestión de Riesgos del Proyecto

Este documento detalla la Matriz de Riesgos identificada para el desarrollo del proyecto, incluyendo las estrategias de mitigación (preventivas) y los planes de contingencia (reactivos).

## Resumen de Clasificación

Para la evaluación de los riesgos, se utiliza la siguiente escala:

* **Impacto:** Bajo, Medio, Alto.
* **Probabilidad:** Baja, Media, Alta.

---

## 1. Matriz de Riesgos y Mitigación

Esta matriz identifica los eventos potenciales y establece acciones preventivas para reducir su probabilidad o impacto *antes* de que ocurran.

| Riesgo | Categoria | Impacto | Probabilidad | Plan de Mitigación (Preventivo) |
| :--- | :--- | :---: | :---: | :--- |
| **Conflictos de Concurrencia** (Doble Reserva) | Técnico | **Alto** | Media | Implementar bloqueos (*locks*) a nivel de base de datos y validaciones estrictas en el backend antes de confirmar. |
| **Curva de aprendizaje** del Stack Tecnológico | Técnico | Medio | **Alta** | Realizar una semana de investigación y prototipado rápido (PoC) antes de empezar la implementación del MVP. |
| **Indisponibilidad** por exámenes parciales | Equipo | Medio | **Alta** | Actualizar el tablero Kanban semanalmente y adelantar entregas críticas antes de las semanas de exámenes. |
| **Falla en la persistencia** de datos | Técnico | **Alto** | Baja | Implementar un sistema de logs de errores y realizar backups periódicos de la base de datos de desarrollo. |
| **Desviación del alcance** (*Scope Creep*) | Requisitos | Bajo | Media | Mantener reuniones constantes con el docente para validar que las funcionalidades no excedan los requisitos de la materia. |
| **Inconsistencias** en diseño UI/UX | Técnico | Bajo | Baja | Utilizar un sistema de diseño o biblioteca de componentes estándar (como Material UI o Tailwind) para mantener coherencia. |

---

## 2. Plan de Contingencia

Este plan define las acciones inmediatas a tomar *una vez que el riesgo ha ocurrido* para minimizar los daños y recuperar el control del proyecto.

### 🚨 1. Conflictos de Concurrencia (Doble Reserva)
* **Disparador:** Reportes de usuarios o detección en logs de múltiples transacciones fallidas simultáneas.
* **Acción Inmediata:**
    1.  **Congelar:** Bloquear temporalmente nuevas confirmaciones en el backend (mantener el sistema en modo solo lectura).
    2.  **Identificar y Mediar:** Consultar la base de datos para hallar duplicados. Aplicar regla "primero en llegar": mantener la primera reserva, cancelar la segunda.
    3.  **Notificar:** Informar inmediatamente a ambos usuarios. Ofrecer disculpas y una alternativa inmediata (otra fecha/recurso) al usuario cancelado.
    4.  **Parche:** Implementar un *fix* de emergencia (e.g., cola de mensajes, caché distribuida) antes de reabrir el sistema.

### 🚨 2. Curva de aprendizaje del Stack Tecnológico
* **Disparador:** Tareas críticas bloqueadas tras la semana de PoC o imposibilidad de completar el Sprint 1 por dudas técnicas.
* **Acción Inmediata:**
    1.  **Simplificar MVP:** Reúnase con stakeholders/docente para acordar una reducción drástica del alcance técnico. Sustituir lógicas complejas por soluciones simples o "hardcodeadas".
    2.  **Asignar Dueños:** Dividir el desarrollo por módulos y nombrar al miembro con más conocimiento como "dueño" técnico para centralizar y resolver bloqueos del equipo.
    3.  **Adaptar Código Verificado:** Priorizar el uso de repositorios de ejemplo o *boilerplates* verificados en lugar de programar arquitecturas base desde cero.

### 🚨 3. Indisponibilidad por exámenes parciales
* **Disparador:** Miembros clave del equipo reportan incapacidad total de trabajo durante la semana crítica de entrega.
* **Acción Inmediata:**
    1.  **Congelar No Críticos:** Detener inmediatamente el pulido visual y las *features* secundarias. Cero recursos dedicados a ellas.
    2.  **Foco en *Happy Path*:** Redistribuir el esfuerzo limitado *exclusivamente* en asegurar que los flujos principales de usuario funcionen para la entrega.
    3.  **Consumir Reserva:** Utilizar la reserva de tiempo final (buffer) planificada para pruebas como tiempo de desarrollo ahora.
    4.  **Notificar:** Avisar preventivamente al docente sobre la entrega parcial debido a la baja disponibilidad del equipo.

### 🚨 4. Falla en la persistencia de datos
* **Disparador:** Incapacidad absoluta del sistema para leer/escribir datos o detección de tablas clave corruptas/vacías.
* **Acción Inmediata:**
    1.  **Restaurar:** Ejecutar inmediatamente el *restore* de la base de datos desde el backup más reciente. Aceptar la pérdida de datos generados desde dicho backup.
    2.  **Diagnosticar:** Analizar logs de errores para hallar la causa raíz (error de deploy, falta de disco, fallo del motor de BD).
    3.  **Prevenir Daño Circular:** Confirmar que el código de la aplicación no volverá a dañar la base restaurada antes de reactivar el servicio.

### 🚨 5. Desviación del alcance (*Scope Creep*)
* **Disparador:** Identificación de tareas no planificadas en el backlog que están consumiendo tiempo de desarrollo a mitad del Sprint.
* **Acción Inmediata:**
    1.  **Detener:** Parar inmediatamente el desarrollo de cualquier *feature* no esencial. Moverlas a una lista de "Deseables para V2.0".
    2.  **Validar:** Confirmar con el docente que dichas funcionalidades no son obligatorias para la nota y obtener aprobación para removerlas de la entrega actual.
    3.  **Re-priorizar:** Usar técnica MoSCoW para asegurar que todo "Must Have" esté cubierto antes de dedicar tiempo a cualquier otra tarea.

### 🚨 6. Inconsistencias en el diseño de UI/UX
* **Disparador:** La integración final muestra pantallas que parecen de aplicaciones distintas, dificultando el uso.
* **Acción Inmediata:**
    1.  **Estilo Global Mínimo:** Crear y aplicar un archivo CSS global básico para forzar colores de marca, tipografía y estilos de botón uniformes en todas las vistas.
    2.  **Fix de Flujos Críticos:** Pulir la interfaz *exclusivamente* para el flujo de reserva y confirmación. Aceptar la inconsistencia visual en páginas secundarias.
    3.  **Simplificar:** Eliminar estilos visuales complejos (sombras, bordes, animaciones) en favor de una vista plana y simple para facilitar la uniformidad rápida.
