# Informe de Ingeniería de Software II: Estándares, Usabilidad y V&V

## . Cuestionario de Verificación y Validación (V&V)

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
