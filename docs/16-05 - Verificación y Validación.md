# Informe de Ingeniería de Software II: Estándares, Usabilidad y V&V

##  Cuestionario de Verificación y Validación (V&V) Aplicado a Spicy Tech

### 1. Verificación vs Validación
* **Verificación (*Verificamos si estamos construyendo el producto con el plano y las herramientas correctas*):** Comprobación técnica de que el software responde fielmente a las especificaciones de diseño y requerimientos lógicos sin introducir fallas en el código.
    * *Ejemplo en nuestro proyecto Spicy Tech:* Implementar una prueba unitaria para verificar que la función constructora de tarifas calcule correctamente el valor neto sumando las horas reservadas por el valor base de la sala de coworking, sin bugs de redondeo o desbordamiento de tipos.
* **Validación (*Estamos haciendo el producto correcto para nuestro cliente?*):** Evaluación de si el software en funcionamiento satisface las necesidades reales del negocio y del usuario final dentro de su entorno operativo.
    * *Ejemplo en nuestro proyecto Spicy Tech:* Someter la interfaz del flujo de reservas a un test con un administrador real de un coworking para certificar que la planilla horaria visual le permite organizar el espacio físico de forma fluida y sin confusiones operacionales.

### 2. Planificación de V&V en un Sprint de 1 Semana
Este tipo de planificaciones son una sección estratégica donde se define cómo, cuándo y con qué herramientas el equipo va a asegurar que el sistema se está construyendo bien (Verificación) y que cumple con las necesidades del cliente (Validación) a lo largo del ciclo de vida del proyecto, si tuviéramos que planificar las actividades de V&V para el próximo sprint de desarrollo de **Spicy Tech**, considerando la alta restricción de tiempo (1 semana), nos enfocaríamos concretamente en el **módulo de reservas y asignación de roles**:

1.  **Actividad de Verificación Concreta:** Desarrollar e integrar una suite de pruebas unitarias automatizadas sobre el controlador de la base de datos que maneja la disponibilidad de salas. El objetivo técnico es verificar que cuando un usuario con rol "Cliente" reserve un espacio, el sistema bloquee el registro de manera atómica para impedir colisiones (*race conditions*) si otro usuario intenta clickear el mismo asiento simultáneamente.
2.  **Actividad de Validación Concreta:** Preparar un escenario de prueba interactivo (User Acceptance Testing ágil) del "camino feliz" de una reserva desde la interfaz móvil. Al final de la semana, ejecutaremos una sesión de pruebas con un usuario externo simulando un entorno con conexión inestable para validar si el flujo de selección de escritorio y confirmación de franja horaria resulta intuitivo, veloz y libre de fricciones cognitivas.

### 3. Inspecciones de Software vs Pruebas Automáticas
* **Diferencia Clave:** La **Inspección de código** es un proceso estático y humano (ej. *Code Reviews* a través de *Pull Requests*) enfocado en evaluar la calidad del diseño arquitectónico, legibilidad y mantenibilidad. La **Prueba automática** es un proceso dinámico y computacional donde se ejecuta un fragmento de código aislado con entradas y salidas predefinidas de forma repetitiva.
* **Aplicación en Spicy Tech:**
    * *Cuándo nos conviene una Inspección?:* Al diseñar la estructura de los middlewares de autenticación y los decoradores de **gestión de roles** en la API. Una revisión por pares humana es superior para detectar vulnerabilidades lógicas de seguridad (como saltos de permisos o IDOR) que las pruebas automáticas suelen pasar por alto.
    * *Cuándo nos convienen Pruebas Automáticas?:* Al realizar cambios en los modelos de datos o agregar nuevos tipos de membresías (ej. pase corporativo). Ejecutar tests automáticos nos permite hacer **pruebas de regresión** instantáneas para asegurar que el nuevo código no rompió la lógica de reservas básicas que ya funcionaba bien.

### 4. Análisis Estático Automatizado
* **Herramienta de referencia:** `ESLint` (para el frontend en React) o `Pylint` (si se utiliza Python en el backend).
* **Errores específicos en nuestro proyecto Spicy Tech:** Analiza el código fuente como texto plano sin ejecutar el programa. En nuestro sistema de coworking, esta herramienta detectaría tempranamente si un desarrollador importó un hook de conexión a la pasarela de pagos pero olvidó invocarlo (código muerto), si se dejaron bloques `try/catch` vacíos al intentar conectar con la base de datos (lo que silenciaría errores críticos de servidor), o si se instanció una variable de sesión de usuario que nunca se lee, optimizando la memoria antes del despliegue.

### 5. Métodos Formales de Verificación
* **Imprescindibles en:** Sistemas de misión crítica o vida crítica donde un fallo de software causa catástrofes físicas o financieras humanas (sistemas aeroespaciales, dispositivos médicos autónomos, algoritmos core de compensación bancaria masiva).
* **Por qué no los usamos en Spicy Tech:** Los métodos formales se basan en demostraciones matemáticas lógicas extremadamente complejas para asegurar matemáticamente que un programa está 100% libre de fallas. Para una aplicación comercial de gestión de coworking como Spicy Tech, el costo financiero, la especialización requerida del equipo y el tiempo de desarrollo que demandaría aplicar estos métodos harían inviable el proyecto, superando drásticamente los beneficios comerciales de la plataforma.

### 6. Reuniones de Validación en Frameworks Ágiles (Scrum/XP)
* **Rol del Product Owner (PO) en la Sprint Review:** El PO actúa como el validador supremo del incremento de software. Su función en la demo de Spicy Tech no es evaluar el código, sino juzgar si las funcionalidades de reserva de salas construidas durante la semana cumplen con los criterios de aceptación y si realmente aportan el valor estratégico que el negocio del coworking necesita.
* **Relación con las Pruebas Automatizadas:** Las pruebas automáticas actúan como un filtro higiénico de verificación técnica previa. Al garantizar robóticamente que el servidor de Spicy Tech es estable y que no va a colapsar por bugs básicos en plena presentación, le permiten al PO y a los stakeholders clave enfocar la discusión de la Sprint Review al 100% en la **validación funcional y usabilidad de negocio**, maximizando el valor del feedback recibido.
