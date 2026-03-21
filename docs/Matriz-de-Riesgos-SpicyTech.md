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

