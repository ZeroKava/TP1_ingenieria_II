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

## Entrada 004 — Semana 3

**Fecha:** 05/04/2026
**Herramienta:** Claude
**Responsable:** Dev Lead — Matías Polcowñuk
**Eje temático:** Eje 1

**¿Para qué se usó?**
Para agregar una base de datos al proyecto.

**¿Qué generó la IA?**
Una base de datos en SQlite que puede usarse desde manera remota al iniciarse.

**¿Qué aceptamos tal cual?**
El cambio en el modulo de BD.

**¿Qué modificamos y por qué?**
Anteriormente era todo local y no se guardaban los nuevos usuarios, si se quiere completar el caso de uso de Login es un paso necesario. Además de agregar el iniciador de la BD.

**¿Qué descartamos y por qué?**
Descartamos "InMemoryUserRepository", porque no funcionaba de manera correcta.

## Entrada 005 — Semana 3

**Fecha:** 06/04/2026
**Herramienta:** Gemini
**Responsable:** UX Dev — Santiago Manrique
**Eje temático:** Eje 1 / Desarrollo Front End

**¿Para qué se usó?**

Maquetar la interfaz principal y armar el index.html pasándole todo el contexto del proyecto a la IA para que no tire fruta.

**¿Qué generó la IA?**

## Entrada 006 — Semana 4

**Fecha:** 18/04/2026

**Herramienta:** Gemini/ISO - International Organization for Standardization

**Responsable:** QA Lead — Santino Calamari

**Eje temático:** Eje 2 / Diseño Orientado a Objetos
**¿Para qué se usó?**

Analizamos nuestro sistema en base a los estándares históricos centrados en la interacción persona‑ordenador(ISO 9241‑11 e ISO 13407) y los tres estándares actuales para sistemas críticos (ISO/IEC 27001, ISA/IEC 62443, ISO 9001)

**¿Qué generó la IA?**

Luego de investigar personalmente usamos la ia para que analice nuestro sistema en conjunto con el fin de obtener una conclusión acerca de que normas se ven reflejadas en nuestro sistema y cuales pulir más.

## Entrada 004 — Semana 4

**Fecha:** 18/04/2026
**Herramienta:** Gemini
**Responsable:** QA Lead — Jesus Emanuel De Olivera
**Eje temático:** Eje 1

**¿Para qué se usó?**
Estructurar el entregable `ANALISIS_ESTANDARES.md` requerido por la cátedra, integrando el análisis propio del equipo (basado en un PDF) sobre normas ISO y completando los requisitos faltantes de la consigna.

**¿Qué generó la IA?**
1. Una tabla comparativa en formato Markdown.
2. La redacción técnica y justificación de dos estándares adicionales (ISO/IEC 25010 de Calidad e ISO/IEC/IEEE 29119 de Testing) para cumplir con el mínimo de 5 normas exigidas por el profesor.
3. Un párrafo de conclusión técnica que vincula el cumplimiento de la norma de seguridad (ISO 27001) con los patrones de diseño implementados en el TP1 (Observer y Factory Method).

**¿Qué aceptamos tal cual?**
El formato de la tabla, la justificación de las dos normas agregadas (25010 y 29119) y la conclusión que enlaza los patrones de diseño con la arquitectura segura, ya que aporta mucho valor técnico para el coloquio.

**¿Qué modificamos y por qué?**
Restringimos la autonomía de la IA proporcionándole un archivo PDF (`ISO's Spycytech .pdf`) con nuestro propio análisis previo de 3 normas (ISO 9241-11, ISO 13407, ISO 27001). Forzamos a la IA a usar nuestras justificaciones y no inventar contenido nuevo para esos puntos, manteniendo la autoría intelectual del equipo.

**¿Qué descartamos y por qué?**
No fue necesario descartar nada, ya que la salida se configuró para cumplir estrictamente con los puntos solicitados en la rúbrica de la entrega.
