# Pruebas de Software - SpicyTech Coworking 

## B0. Investigación Previa y Técnicas de Diseño de Pruebas

### 1. Clases de Equivalencia
**¿Qué es y cómo se aplica?**
La partición en clases de equivalencia es una técnica de testing de caja negra que consiste en dividir el dominio de los datos de entrada en diferentes grupos (clases). La premisa es que si un valor de una clase funciona correctamente (o falla), todos los demás valores de esa misma clase se comportarán exactamente igual. Esto permite reducir drásticamente la cantidad de casos de prueba necesarios, eligiendo solo un valor representativo por cada clase válida o inválida.

### 2. Valores Límite
**¿Qué es y cómo se aplica?**
El análisis de valores límite es una técnica complementaria a las clases de equivalencia. Se basa en la observación de que la mayoría de los defectos de software ocurren en los "bordes" de las clases de equivalencia, más que en el centro. Consiste en diseñar casos de prueba que evalúen los extremos exactos (límites permitidos) y los valores inmediatamente fuera de esos límites (justo por encima o justo por debajo).

### 3. Ejemplo Concreto Aplicado a SpicyTech Coworking
**Función bajo prueba:** Validación del rango horario para reservar un espacio.
**Regla de negocio:** El coworking opera estrictamente de 08:00 a 20:00 hs.

*   **Clases de Equivalencia:**
    *   *Clase Válida:* Cualquier hora entre las 08:00 y las 20:00 (ej. valor representativo: 14:00).
    *   *Clase Inválida 1 (Inferior):* Cualquier hora antes de las 08:00 (ej. 03:00).
    *   *Clase Inválida 2 (Superior):* Cualquier hora después de las 20:00 (ej. 22:00).
*   **Valores Límite:**
    *   *Límite Inferior Válido:* 08:00.
    *   *Límite Inferior Inválido:* 07:59.
    *   *Límite Superior Válido:* 20:00.
    *   *Límite Superior Inválido:* 20:01.

## B1. Diseño de Casos de Prueba Unitaria (TDD)

A continuación se detallan los 6 casos de prueba diseñados utilizando partición de equivalencia y análisis de valores límite. Estos casos aseguran la integridad de las reglas de negocio fundamentales de **SpicyTech Coworking** y serán automatizados mediante código por el equipo de desarrollo.

### Función 1: `validar_horario_operativo(hora_solicitada)`
*Regla de negocio:* El coworking solo permite reservas dentro de la franja horaria de 08:00 a 20:00 hs.

*   **Caso de Prueba 1 (CP01)**
    *   **Técnica:** Partición de Equivalencia (Clase Válida).
    *   **Datos de entrada:** `hora_solicitada = "14:00"`
    *   **Resultado esperado:** `True` (El sistema permite continuar con la reserva).

*   **Caso de Prueba 2 (CP02)**
    *   **Técnica:** Valores Límite (Frontera Inferior Inválida).
    *   **Datos de entrada:** `hora_solicitada = "07:59"`
    *   **Resultado esperado:** `False` / Excepción: "Horario fuera del rango operativo".

*   **Caso de Prueba 3 (CP03)**
    *   **Técnica:** Valores Límite (Frontera Superior Válida).
    *   **Datos de entrada:** `hora_solicitada = "20:00"`
    *   **Resultado esperado:** `True` (Es el último minuto válido para estar en el espacio).

---

### Función 2: `validar_logica_tiempo(hora_inicio, hora_fin)`
*Regla de negocio:* Para que un bloque de reserva sea válido, la hora de finalización debe ser estrictamente posterior a la hora de inicio.

*   **Caso de Prueba 4 (CP04)**
    *   **Técnica:** Partición de Equivalencia (Clase Válida).
    *   **Datos de entrada:** `hora_inicio = "10:00"`, `hora_fin = "13:00"`
    *   **Resultado esperado:** `True` (El bloque es lógico y válido).

*   **Caso de Prueba 5 (CP05)**
    *   **Técnica:** Valores Límite (Límite exacto de colisión).
    *   **Datos de entrada:** `hora_inicio = "15:00"`, `hora_fin = "15:00"`
    *   **Resultado esperado:** `False` / Excepción: "La hora de fin no puede ser igual a la hora de inicio".

*   **Caso de Prueba 6 (CP06)**
    *   **Técnica:** Partición de Equivalencia (Clase Inválida - Lógica inversa).
    *   **Datos de entrada:** `hora_inicio = "18:00"`, `hora_fin = "16:00"`
    *   **Resultado esperado:** `False` / Excepción: "La hora de fin debe ser posterior a la hora de inicio".
---

## B3. Diseño Conceptual de Pruebas de Integración

### 1. Dependencias Externas Identificadas
Para el módulo de reservas y autenticación de nuestro backend (Flask), hemos identificado las siguientes dependencias externas críticas:
1.  **Base de Datos Relacional (SQLite/SQLAlchemy):** Encargada de persistir el estado de los usuarios y las reservas.
2.  **Servicio de Notificaciones (AuthEventBus):** El bus de eventos que enviaría correos electrónicos o alertas al Administrador cuando un miembro solicita una reserva y esta queda en estado "PENDIENTE".

### 2. Estrategia de Mocks y Stubs
Para realizar pruebas de integración rápidas, predecibles y que no afecten los datos de producción, aislaremos estas dependencias:
*   **Stub para la Base de Datos:** En lugar de conectarnos a la base de datos real, configuraremos SQLAlchemy para que utilice una base de datos en memoria (`sqlite:///:memory:`). Este Stub nace vacío al inicio de la prueba y se destruye al finalizar, garantizando un entorno limpio.
*   **Mock para Notificaciones:** Reemplazaremos el objeto real del notificador por un objeto *Mock* simulado. Esto evitará que se envíen correos reales durante las pruebas automatizadas, pero nos permitirá "espiar" si el sistema intentó enviar el mensaje correctamente.

### 3. Flujo de Prueba de Integración (Pseudocódigo)
**Escenario:** Un miembro solicita una sala, la cual debe guardarse como "PENDIENTE" y notificar al Administrador.
```python
def test_integracion_flujo_reserva_pendiente():
    # 1. Preparación (Arrange)
    db_stub = inicializar_db_en_memoria()
    usuario_test = crear_usuario_miembro(db_stub)
    espacio_test = crear_espacio_coworking(db_stub)
    
    mock_notificador = crear_mock()
    sistema_eventos.suscribir(mock_notificador)

    # 2. Ejecución (Act)
    # Se simula el POST a la API /api/reservas
    respuesta = api.post('/api/reservas', data={
        "usuario_id": usuario_test.id,
        "espacio_id": espacio_test.id,
        "hora_inicio": "10:00",
        "hora_fin": "12:00"
    })

    # 3. Verificación (Assert)
    # Verificamos la respuesta HTTP
    asegurar_que(respuesta.status_code == 201)
    
    # Verificamos la persistencia en el Stub de la BD
    reserva_guardada = db_stub.obtener_ultima_reserva()
    asegurar_que(reserva_guardada.estado == "PENDIENTE")
    
    # Verificamos la interacción con el Mock
    asegurar_que(mock_notificador.fue_llamado_con("NUEVA_RESERVA_PENDIENTE"))
