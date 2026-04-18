# Análisis de Estándares - SpicyTech 

Este documento analiza los estándares de ingeniería de software y su aplicabilidad al sistema de gestión de reservas del proyecto Spicy Coworking, evaluando su impacto en la arquitectura y el diseño.

## 1. Tabla Comparativa de Estándares

| Estándar | Año (aprox) | Enfoque principal | ¿Aplica a mi proyecto? | Justificación |
| :--- | :--- | :--- | :---: | :--- |
| **ISO 9241-11** | 1998 (2018) | Usabilidad (Eficacia, eficiencia y satisfacción)  | **Sí** | Es innegociable; si el cliente tiene que hacer muchos clics o lidiar con un calendario confuso, abandonará la plataforma. La usabilidad actúa como capa de seguridad, priorizando que el usuario logre el objetivo con precisión absoluta antes que la estética. |
| **ISO 13407** | 1999 (2010) | Proceso de diseño centrado en el humano  | **Sí** | El software se construye desde el usuario hacia abajo, resolviendo los problemas reales de cada perfil (administrador en PC, cliente en celular). Diseñar pensando en el entorno de uso evita saturar a un operador bajo estrés y previene errores. |
| **ISO/IEC 27001** | 2005 (2022) | Seguridad de la información  | **Sí** | Garantiza la confidencialidad, integridad y disponibilidad. Es vital porque el sistema maneja datos sensibles de clientes y pagos; una inyección SQL o caída del servicio implicaría demandas legales y pérdida de confianza. Exige arquitecturas de alta disponibilidad (99.99% uptime). |
| **ISO/IEC 25010** | 2011 (2023) | Calidad del Producto de Software | **Sí** | Evalúa características técnicas como la mantenibilidad, portabilidad y el rendimiento. Aplica directamente a nuestra necesidad de tener una API REST (Flask) que responda rápido a las reservas concurrentes y un código fácil de mantener para futuros Sprints. |
| **ISO/IEC/IEEE 29119** | 2013 | Pruebas de Software (Testing) | **Sí** | Estandariza los procesos de validación y verificación. Para asegurar la calidad (QA), aplicar esta norma nos obliga a mantener y ejecutar pruebas automatizadas rigurosas antes de desplegar código, previniendo regresiones en la lógica de turnos. |

## 2. Conclusión y Relación con la Arquitectura (TP1)

Si tuviéramos que certificar nuestro sistema hoy, elegiríamos **ISO/IEC 27001 (Seguridad de la Información)** por el nivel crítico de los datos personales y bancarios que gestionamos. Cumplir con esto nos obligaría a robustecer nuestra arquitectura actual añadiendo capas de encriptación en reposo y rotación automatizada de tokens JWT. Afortunadamente, nuestras decisiones de diseño del TP1 facilitan este camino: el patrón **Observer** implementado en la autenticación nos permite agregar un `DatabaseObserver` para registrar logs de auditoría inmutables (vitales para la ISO 27001) cada vez que alguien inicia sesión, sin acoplar ni alterar el flujo principal de seguridad; mientras que el patrón **Factory Method** centraliza y blinda la creación de roles, mitigando riesgos de escalamiento de privilegios de manera estandarizada.
