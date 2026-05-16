# Informe de Ingeniería de Software II: Estándares, Usabilidad y V&V
## Proyecto: Spicy Tech — Sistema de Gestión de Espacios de Coworking

Este documento recopila la investigación de estándares internacionales, su análisis aplicado al proyecto **Spicy Tech**, el estudio de fallas críticas del sistema y las definiciones fundamentales sobre Verificación y Validación (V&V). Está estructurado para ser integrado directamente en la documentación (`/docs`) del repositorio de GitHub.

---

## 1. Investigación y Resumen de Estándares Internacionales

A continuación, se presenta una síntesis teórica de los estándares analizados y su métrica o enfoque principal:

| Estándar | Nombre / Ámbito | Concepto Clave y Enfoque |
| :--- | :--- | :--- |
| **ISO 9241-11** | Ergonomía de la interacción hombre-sistema — Usabilidad | Define la **usabilidad** a través de tres métricas fundamentales: **Eficacia** (precisión para lograr objetivos), **Eficiencia** (recursos/esfuerzo empleados) y **Satisfacción** (comodidad del usuario). |
| **ISO 13407** | Procesos de diseño centrado en el humano para sistemas interactivos | Metodología iterativa de desarrollo basada en 4 pasos: entender el contexto de uso, especificar requisitos del usuario, producir soluciones de diseño y evaluar los diseños frente a los requisitos. *(Reemplazada modernamente por ISO 9241-210)*. |
| **ISO/IEC 27001** | Sistemas de Gestión de Seguridad de la Información (SGSI) | Norma de oro para la seguridad de datos. Se enfoca en la protección de la tríada **CIA**: **Confidencialidad** (acceso autorizado), **Integridad** (datos inalterados) y **Disponibilidad** (acceso cuando se requiera). |
| **ISA/IEC 62443** | Ciberseguridad en sistemas de automatización y control industrial | Conjunto de estándares para proteger redes de Tecnología de Operaciones (OT), como SCADA y PLCs, que controlan hardware en el mundo físico (fábricas, infraestructura crítica). |
| **ISO 9001** | Sistemas de Gestión de la Calidad (SGC) | Estándar genérico enfocado en la optimización y mejora continua de los procesos organizacionales, asegurando la trazabilidad, auditoría y consistencia en las metodologías de trabajo. |

---

## 2. Análisis de Relevancia Aplicado a Spicy Tech

Para un sistema de administración de reservas y espacios de coworking como **Spicy Tech**, la prioridad radica en la experiencia del cliente y la robustez en el manejo de datos comerciales.

### Estándares Muy Relevantes / Relevantes
* **ISO 9241-11 (Usabilidad) — *Muy Relevante*:** El éxito de Spicy Tech depende de que clientes con diversos niveles tecnológicos puedan reservar un escritorio o sala rápidamente (**eficiencia**) y sin equivocarse de fecha/hora (**eficacia**). Una interfaz frustrante ahuyentará a los usuarios hacia la competencia.
* **ISO/IEC 27001 (Seguridad de la Información) — *Muy Relevante*:** El sistema procesa credenciales de acceso, historiales de uso y, fundamentalmente, **información financiera y de facturación** (tarjetas de crédito/débito). Una vulnerabilidad arquitectónica que exponga estos datos acarrearía severas penalizaciones legales y la quiebra reputacional de la plataforma.
* **ISO 13407 (Diseño Centrado en el Humano) — *Relevante*:** Crucial para el modelado en fases tempranas (Sprint 0). Permite segmentar claramente los flujos de datos y UX según el rol del actor: el *Administrador* requiere paneles densos con métricas de facturación desde una PC, mientras que el *Cliente* necesita una experiencia móvil ágil para reservar en segundos.

### Estándares Poco Relevantes
* **ISA/IEC 62443 (Ciberseguridad Industrial):** No aplica al alcance de Spicy Tech, ya que operamos en un entorno puramente de Tecnologías de la Información (IT) comerciales. No controlamos hardware industrial o PLCs a bajo nivel.
* **ISO 9001 (Calidad de Procesos):** Aunque es útil para certificar la metodología de trabajo de la célula de desarrollo, no impone requisitos técnicos directos sobre el código, la base de datos o el comportamiento de la aplicación de cara al usuario final.

---

## 3. Escenario de Sistema Declarado "Crítico"

Si la naturaleza de **Spicy Tech** cambiara drásticamente y fuera declarado un **sistema crítico** (como la gestión de fondos bancarios, control de tránsito aéreo o monitoreo de pacientes), la tolerancia al fallo pasa a ser cero y las normativas se vuelven de cumplimiento **obligatorio**:

1.  **ISO/IEC 27001 (Seguridad Obligatoria):** Un ciberataque en este entorno puede costar vidas o desastres financieros masivos. Exige el diseño de arquitecturas con **Alta Disponibilidad (High Availability)** y tolerancia a fallos de infraestructura para alcanzar la regla de los cinco nueves (**99.999% de uptime**), permitiendo menos de 5.26 minutos de inactividad anuales.
2.  **ISO 9001 (Trazabilidad y Calidad Obligatoria):** Se prohíbe la improvisación. Todo el Ciclo de Vida del Desarrollo de Software (SDLC) debe estar estrictamente auditado. Cada línea de código, prueba de regresión y despliegue debe contar con un registro firmado que demuestre los procesos de Verificación y Validación (V&V).
3.  **ISA/IEC 62443 (Ciberseguridad de Operaciones — OT):** Absolutamente obligatoria si el sistema interactúa con hardware del mundo real (ej. dosificadores de medicamentos, radares, sensores de tráfico). Exige la segmentación estricta de la red en zonas y conductos para impedir lógicamente que una intrusión en la capa web comprometa el funcionamiento físico de las máquinas críticas.

---

## 4. Conceptos Clásicos Vigentes en la Actualidad

A pesar de la evolución tecnológica, principios fundamentales de las normas **ISO 13407** e **ISO 9241-11** siguen siendo pilares innegociables hoy en día:

* **El Contexto de Uso (ISO 13407):** Entender **quién** usa el sistema, **qué** hace y **bajo qué condiciones**. En entornos de alta presión (controladores aéreos, guardias médicas), los operadores sufren fatiga y estrés cognitivo extremo. Diseñar interfaces limpias que reduzcan la carga cognitiva no es una decisión estética; es una barrera de seguridad que previene el error humano catastrófico.
* **La Eficacia sobre la Estética (ISO 9241-11):** En sistemas críticos, la prioridad absoluta es que el usuario complete la acción con precisión milimétrica e integridad. El diseño debe estructurarse con controles de validación robustos (ej. patrones de confirmación explícita para acciones destructivas) para evitar que un operario ejecute por error una orden errónea. **La usabilidad es, intrínsecamente, una capa más de la seguridad.**
* **El Proceso de Evaluación Iterativa (ISO 13407):** El paradigma de probar prototipos con usuarios reales en simuladores antes del despliegue masivo sigue vigente. Permite mitigar riesgos de diseño en etapas tempranas donde el costo de corrección es bajo.

---

## 5. Matriz de Situaciones Críticas de Falla en Spicy Tech

Modelado de riesgos técnicos específicos basados en la arquitectura basada en roles, autenticación de usuarios y lógica transaccional de **Spicy Tech**:

| # | Situación Crítica / Falla | Tipo de Vulnerabilidad | Impacto en el Negocio |
| :-: | :--- | :--- | :--- |
| **1** | **Colisión de Reservas (Race Condition)**<br>Dos usuarios intentan reservar el mismo escritorio o sala de reuniones en el mismo milisegundo. | Falla de **Integridad** en la concurrencia de la Base de Datos. | **Overbooking físico:** Ambas transacciones se confirman debido a la falta de bloqueos pesimistas u optimistas en el servidor, generando conflictos logísticos presenciales. |
| **2** | **Interrupción del Flujo de Pago (Callback Drop)**<br>El cliente abona el monto, pero la conexión entre la pasarela externa y la API de Spicy Tech se corta antes de recibir la confirmación de pago. | Falla de **Disponibilidad / Sincronización** asíncrona. | **Cobro sin reserva:** El dinero es debitado de la cuenta del cliente, pero el espacio permanece libre o es asignado a otro, destruyendo la confianza del usuario y requiriendo soporte manual. |
| **3** | **Falla de Autorización de Roles (IDOR)**<br>La API no valida a nivel de servidor si la sesión del usuario coincide con el propietario del recurso solicitado. | Falla de **Confidencialidad** y Control de Acceso Lógico. | **Escalada de Privilegios:** Un usuario con rol "Cliente" altera los IDs de las peticiones HTTP y logra cancelar, editar o ver reservas de terceros, o acceder a datos sensibles de administración. |
| **4** | **Inconsistencia de Estados (Falla de Transacción)**<br>Ocurre una micro-caída de la base de datos a mitad de la escritura de un proceso de reserva. | Falla de **Atomicidad** (ACID) en la capa de datos. | **Bloqueo fantasma:** El espacio se marca como "ocupado" en las tablas de disponibilidad, pero la orden de reserva de usuario nunca se crea. El espacio queda inutilizable y genera pérdida de ingresos. |

---

## 6. Cuestionario de Verificación y Validación (V&V)

### 1. Verificación vs Validación
* **Verificación (*¿Estamos construyendo el producto correctamente?*):** Proceso estático y dinámico enfocado en comprobar que el software cumple con las especificaciones técnicas, requisitos de diseño y buenas prácticas de desarrollo.
    * *Ejemplo en Spicy Tech:* Implementar una prueba unitaria para verificar que la función constructora de tarifas calcule correctamente el valor neto sumando las horas reservadas por el valor base, sin bugs de redondeo.
* **Validación (*¿Estamos construyendo el producto correcto?*):** Proceso enfocado en evaluar si el software terminado cumple con las expectativas reales, necesidades de negocio y objetivos de los usuarios finales.
    * *Ejemplo en Spicy Tech:* Someter el flujo completo de reserva a un test con un administrador del coworking real para certificar que la interfaz le permite gestionar la planilla diaria de forma fluida y sin confusiones operacionales.

### 2. Planificación de V&V en un Sprint de 1 Semana
Debido a la alta restricción de tiempo, la planificación de actividades debe ser altamente automatizada y enfocada:
1.  **Actividad de Verificación (Automatizada):** Desarrollar e integrar suites de pruebas unitarias específicas sobre las funciones del controlador de autenticación y asignación de roles de usuario, garantizando estabilidad lógica antes de mergear la funcionalidad.
2.  **Actividad de Validación (Ágil):** Preparar una demostración funcional (Demo) del "camino feliz" de una reserva de espacio y ejecutarla frente al Product Owner (PO) al cierre del sprint para corroborar la alineación con la visión del negocio.

### 3. Inspecciones de Software vs Pruebas Automáticas
* **Diferencia:** La **Inspección de código** es un proceso estático y humano (ej. Code Reviews o Pull Requests) enfocado en evaluar la calidad del diseño, el cumplimiento de principios SOLID, la legibilidad y fallas lógicas complejas. La **Prueba automática** es un proceso dinámico y de máquina donde se ejecuta un fragmento de código con entradas predefinidas para validar si produce las salidas esperadas.
* **Cuándo conviene cada una:**
    * *Inspección:* Ideal en fases tempranas de codificación, al definir patrones arquitectónicos, o al evaluar código crítico de seguridad, ya que promueve la transferencia de conocimiento en el equipo.
    * *Prueba Automática:* Indispensable para realizar **pruebas de regresión** masivas de forma rápida y repetitiva, asegurando que los nuevos cambios del sprint no rompan funcionalidades preexistentes de Spicy Tech.

### 4. Análisis Estático Automatizado
* **Herramienta de referencia:** `ESLint` (si el stack es JavaScript/React) o `Pylint` (para Python).
* **Errores detectados:** Analiza el código fuente como texto sin necesidad de ejecutarlo. Detecta de forma temprana variables inicializadas pero nunca leídas (fugas latentes de memoria), bloques de captura de errores (`try/catch`) vacíos que silencian excepciones críticas, o código muerto (inaccesible), además de asegurar el estándar estilístico del proyecto.

### 5. Métodos Formales de Verificación
* **Imprescindibles en:** Sistemas de alta criticidad o misión crítica (médicos, aeroespaciales, bancarios core).
* **Por qué no se generalizan:** Utilizan modelos matemáticos rigurosos y lógicas formales para probar la ausencia absoluta de fallos. Su aplicación requiere perfiles con alta formación matemática, los tiempos de desarrollo se incrementan exponencialmente y el costo financiero resultante es prohibitivo para aplicaciones de software comercial convencional como plataformas de coworking.

### 6. Reuniones de Validación en Frameworks Ágiles (Scrum/XP)
* **Rol del Product Owner (PO) en la Sprint Review:** El PO actúa como el validador supremo del incremento del producto. Su función consiste en evaluar si las funcionalidades construidas por el equipo de desarrollo cumplen con los criterios de aceptación y, principalmente, si entregan valor estratégico real al cliente del negocio.
* **Relación con las Pruebas Automatizadas:** Las pruebas automatizadas actúan como un filtro de calidad previo (Verificación). Al asegurar de manera robótica que el sistema no posee fallos o bugs técnicos básicos en su infraestructura, le permiten al PO y a los Stakeholders centrar la discusión de la Sprint Review exclusivamente en la **validación** funcional y estratégica, optimizando los tiempos de feedback de negocio.
