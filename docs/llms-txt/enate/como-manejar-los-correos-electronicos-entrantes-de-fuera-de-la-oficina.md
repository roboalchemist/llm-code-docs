# Source: https://docs.enate.net/enate-help/espanol/correos-electronicos/correos-electronicos-entrantes-logica-de-procesamiento/como-manejar-los-correos-electronicos-entrantes-de-fuera-de-la-oficina.md

# Cómo manejar los correos electrónicos entrantes de Fuera de la oficina

### ¿Cómo maneja Enate los correos electrónicos de Fuera de la oficina?

Enate maneja los correos electrónicos entrantes de "Fuera de la oficina" de dos maneras:

1. Si el correo electrónico de "Fuera de la oficina" se genera en respuesta a la recepción de un correo electrónico escrito por un usuario en Enate, Enate adjuntará el correo electrónico de "Fuera de la oficina" a la tarea y marcará la tarea con "nueva información recibida". Véase más abajo para más detalles.
2. Si el correo electrónico de "Fuera de la oficina" se envía en respuesta a un correo electrónico generado automáticamente desde Enate (por ejemplo, reconocimiento de la creación de un Ticket), el correo electrónico de "Fuera de la oficina" NO se adjuntará a la tarea y la tarea no se marcará con "nueva información recibida", sino que se ignorará.

Ampliando la lógica de la situación 1 anterior, en la que se genera un correo electrónico de "Fuera de la oficina" en respuesta a la recepción de un correo electrónico escrito por un usuario en Enate...

### Correos electrónicos entrantes de "Fuera de la oficina" que coinciden con una tarea en progreso existente

Si el correo electrónico entrante de "Fuera de la oficina" coincide con un Ticket, Caso o Acción existente que se encuentra en estado de BORRADOR, POR HACER o EN PROGRESO, el sistema:

* adjuntará el correo electrónico a la tarea;
* marcará la tarea con "nueva información recibida".

Nota: Esta lógica se aplica a todos los correos electrónicos entrantes generados automáticamente que coinciden con una tarea existente en un estado de BORRADOR, POR HACER o EN PROGRESO (es decir, los correos electrónicos entrantes de fuera de la oficina se tratan exactamente igual que otros correos electrónicos entrantes generados automáticamente en estos estados). Consulte esta [<mark style="color:blue;">sección</mark> ](https://docs.enate.net/enate-help/espanol/correos-electronicos/correos-electronicos-entrantes-logica-de-procesamiento/..#logica-de-deteccion-de-correos-electronicos-generados-automaticamente)para obtener más información sobre cómo el sistema detecta los correos electrónicos generados automáticamente.

### Correos electrónicos entrantes de "Fuera de la oficina" que coinciden con una tarea en estado de En espera

Si el correo electrónico entrante de "Fuera de la oficina" coincide con una tarea existente que se encuentra en estado de EN ESPERA, el sistema:

* adjuntará el correo electrónico a la tarea;
* marcará la tarea con "nueva información recibida".

Además, si el tipo de Espera es "Esperando más información", el sistema:

* cambiará el estado de la tarea de EN ESPERA a POR HACER.
* Como resultado del cambio de estado a POR HACER, se establecerá una Lista y una Persona asignada a la tarea y esta volverá a la Bandeja de entrada de Enate del agente responsable, marcada con "nueva información recibida".
* Si la tarea es una Acción y tanto la Acción como su Caso principal se encuentran en estado de EN ESPERA con un tipo de espera de Esperando más información, el estado del Caso principal cambiará a EN PROGRESO.

Las mismas reglas se aplican a otros correos electrónicos entrantes generados automáticamente que coinciden con una tarea existente en un estado de En espera o Esperando más información (es decir, los correos electrónicos entrantes de Fuera de la oficina se tratan exactamente igual que otros correos electrónicos entrantes generados automáticamente en este estado). Consulte esta [<mark style="color:blue;">sección</mark> ](https://docs.enate.net/enate-help/espanol/correos-electronicos/correos-electronicos-entrantes-logica-de-procesamiento/..#logica-de-deteccion-de-correos-electronicos-generados-automaticamente)para obtener más información sobre cómo el sistema detecta los correos electrónicos generados automáticamente.

## Correos electrónicos entrantes de Fuera de la oficina que coinciden con una tarea resuelta (Caso y Ticket)

Si el correo electrónico entrante de "Fuera de la oficina" coincide con una tarea existente que se encuentra en un estado de RESUELTO (tenga en cuenta que solo los Casos y Tickets pueden estar en un estado de RESUELTO), el sistema:

* adjuntará el correo electrónico a la tarea;
* reabrirá la tarea y la establecerá de nuevo como POR HACER.
* Como resultado del cambio de estado a POR HACER, se establecerá una Lista y una Persona asignada a la tarea y esta volverá a la Bandeja de entrada de Enate del agente responsable, marcada con "nueva información recibida".

Las mismas reglas se aplican a otros correos electrónicos entrantes generados automáticamente que coinciden con una tarea existente en un estado de RESUELTO (es decir, los correos electrónicos entrantes de Fuera de la oficina se tratan exactamente igual que otros correos electrónicos entrantes generados automáticamente en este estado). Consulte esta [<mark style="color:blue;">sección</mark> ](https://docs.enate.net/enate-help/espanol/correos-electronicos/correos-electronicos-entrantes-logica-de-procesamiento/..#logica-de-deteccion-de-correos-electronicos-generados-automaticamente)para obtener más información sobre cómo el sistema detecta los correos electrónicos generados automáticamente.

## Correos electrónicos entrantes de Fuera de la oficina que coinciden con una tarea cerrada

Si el correo electrónico entrante de "Fuera de la oficina" coincide con una tarea existente que se encuentra en un estado de CERRADO, el sistema puede adoptar varios procedimientos dependiendo del tipo de tarea:

* El sistema primero "subirá" por la cadena de tareas para buscar una tarea principal, por ejemplo:&#x20;

\- si el correo electrónico coincide con una Acción que está CERRADA, el sistema verá si el Caso principal de la Acción sigue abierto;

\- si el correo electrónico coincide con un Caso que está CERRADO, el sistema verá si el Caso tiene un Caso o Ticket principal que aún está abierto;

-si el correo electrónico coincide con un Ticket que está CERRADO, el sistema verá si el Ticket tiene un Ticket principal que aún está abierto.

* Si el sistema encuentra una tarea principal que aún está abierta, el sistema aplicará el resto de la lógica de procesamiento de correo electrónico a la tarea principal (es decir, toda la lógica de las secciones anteriores sobre tareas en progreso).
* Si el sistema no puede encontrar una tarea principal que aún esté abierta, el correo electrónico entrante NO se adjuntará a la tarea ya cerrada. En su lugar, creará una nueva siguiendo las [<mark style="color:blue;">reglas que se indican a continuación</mark>](#si-no-se-puede-hacer-coincidir-un-correo-electronico-entrante-de-fuera-de-la-oficina-con-una-tarea-e) para lo que ocurre cuando el sistema no puede hacer coincidir un correo electrónico con una tarea existente.

Las mismas reglas se aplican a otros correos electrónicos entrantes generados automáticamente que coinciden con una tarea existente en un estado de CERRADO (es decir, los correos electrónicos entrantes de Fuera de la oficina se tratan exactamente igual que otros correos electrónicos entrantes generados automáticamente en este estado). Consulte esta [<mark style="color:blue;">sección</mark> ](https://docs.enate.net/enate-help/espanol/correos-electronicos/correos-electronicos-entrantes-logica-de-procesamiento/..#logica-de-deteccion-de-correos-electronicos-generados-automaticamente)para obtener más información sobre cómo el sistema detecta los correos electrónicos generados automáticamente.

### Si no se puede hacer coincidir un correo electrónico entrante de Fuera de la oficina con una tarea existente

Si no se puede identificar ninguna información que vincule el correo electrónico entrante de "Fuera de la oficina" con una tarea que se esté ejecutando actualmente, el sistema generará una nueva tarea (Ticket o Caso) basada en las reglas de enrutamiento configuradas del correo electrónico.

Si se ha creado un Ticket, incluso si la configuración de la ruta del correo electrónico especificada en Builder tiene la opción "enviar respuesta" activada, NO se enviará automáticamente un correo electrónico de confirmación a la dirección de correo electrónico de la que procede el correo electrónico de "Fuera de la oficina", ya que la opción "Desactivar correos electrónicos automatizados" se activará automáticamente.
