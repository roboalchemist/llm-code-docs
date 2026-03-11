# Source: https://docs.enate.net/enate-help/espanol/correos-electronicos/correos-electronicos-entrantes-logica-de-procesamiento.md

# Correos electrónicos entrantes - Lógica de procesamiento

## **¿Cómo se relaciona Enate con un correo electrónico entrante?**

Cuando llegan nuevos correos electrónicos a Enate, el sistema analiza el correo para determinar si se trata de una nueva solicitud o si está relacionada con una ya existente, y luego determina cómo proceder.

El sistema buscará varios criterios diferentes en orden y si encuentra una coincidencia, dejará de buscar (es decir, el primero es el que gana). El orden de ejecución es el siguiente:

**1)  Valor “en respuesta a” en el encabezado** –  el valor “en respuesta a” que aparece en el encabezado del correo electrónico. Este valor tiene la siguiente estructura:

<‘GUID de correo electrónico único.’GUID de tarea’@‘servidor de Enate que envió el correo electrónico’.enate>

p. ej. \<d23a9d57-6006-4ab7-a412-8ca8ece2f3aa.2b8586bb-ef95-4020-9cf8- <ed56a059b47e@SendingServerName.enate>>

**2)  Identificador único en el cuerpo del mensaje del correo electrónico -**  Si el correo electrónico entrante ha sido enviado como respuesta a un correo electrónico enviado desde Enate, es probable que contenga una etiqueta de identificador único en el cuerpo del mensaje del correo electrónico.

**3)  Referencia de la tarea en el asunto del correo electrónico**

**4)  Referencia de la tarea en el cuerpo del mensaje del correo electrónico**

## Envío de un correo electrónico entrante a una tarea en progreso existente

Si el sistema encuentra una coincidencia con un Ticket, Caso o Acción existente que se encuentra en estado de BORRADOR, POR HACER o EN PROGRESO, el sistema:

* adjuntar á el correo electrónico a la tarea;
* marcará la tarea con “nueva información recibida”.

Lo mismo se aplica a los correos electrónicos generados automáticamente que coinciden con una tarea existente en un estado de BORRADOR, POR HACER o EN PROGRESO. Consulte la [siguiente sección](#especificaciones-adicionales) para obtener más información sobre cómo el sistema detecta los correos electrónicos generados automáticamente.

## Envío de un correo electrónico entrante a una tarea en estado de En espera

Si un correo electrónico entrante coincide con una tarea existente que se encuentra en estado de EN ESPERA, el sistema:

* adjuntar á el correo electrónico a la tarea;
* marcará la tarea con “nueva información recibida”.

Además, si el tipo de Espera es “Esperando más información”, el sistema:

* cambiará el estado de la tarea de EN ESPERA a POR HACER;
* como resultado del cambio de estado a POR HACER, se asignará una Lista y una Persona asignada a la tarea y esta volverá a la Bandeja de entrada de tareas del agente responsable de Enate, marcada con “nueva información recibida”;
* si la tarea es una Acción y tanto la Acción como su Caso principal se encuentran en estado de EN ESPERA con un tipo de espera clasificado como Esperando más información, el estado del Caso principal cambiará a EN PROGRESO.

Las mismas reglas se aplican a los correos electrónicos generados automáticamente que coinciden con una tarea existente en estado de En espera o Esperando más información. Por favor, consulte la [siguiente sección](#especificaciones-adicionales) para obtener más información sobre cómo el sistema detecta los correos electrónicos generados automáticamente.

## Envío de un correo electrónico entrante a una tarea resuelta (Caso y Ticket)

Si un correo electrónico entrante coincide con una tarea existente que se encuentra en estado de RESUELTO (tenga en cuenta que solo los Casos yTickets pueden estar en estado de RESUELTO), el sistema:

* adjuntará el correo electrónico a la tarea;
* reabrirá la tarea y la volverá a establecer en POR HACER;
* como resultado del cambio de estado a POR HACER, se asignará una Lista y una Persona asignada a la tarea y esta volverá a la bandeja de entrada del agente responsable de Enate, marcada con “nueva información recibida”.

Las mismas reglas se aplican a los correos electrónicos generados automáticamente que coinciden con una tarea existente en un estado de RESUELTO. Consulte la [siguiente sección](#especificaciones-adicionales) para obtener más información sobre cómo el sistema detecta los correos electrónicos generados automáticamente.

## Envío de un correo electrónico entrante a una tarea cerrada

Si un correo electrónico entrante coincide con una tarea existente que se encuentra en estado de CERRADO, el sistema puede tomar varias medidas según el tipo de tarea:

* El sistema primero “subirá” en la cadena de tareas para buscar una tarea principal, p. ej.
  * si el correo electrónico coincide con una Acción que está CERRADA, el sistema verá si el Caso principal de la Acción continúa abierto;
  * si el correo electrónico coincide con un Caso que está CERRADO, el sistema verá si el Caso tiene un Caso principal o Ticket que continúa abierto; &#x20;
  * si el correo electrónico coincide con un Ticket que está CERRADO, el sistema verá si el Ticket tiene un Ticket principal que continúa abierto.
* Si el sistema *encuentra* una tarea principal que continúa abierta, el sistema aplicará el resto de la lógica de procesamiento de correo electrónico a la tarea principal (es decir, toda la lógica de las secciones anteriores sobre tareas en ejecución).
* Si el sistema *no puede* encontrar una tarea principal que continúe abierta, el correo electrónico entrante NO se adjuntará a la tarea ya cerrada. En su lugar, creará una nueva tarea siguiendo las [siguientes reglas](#si-no-se-puede-relacionar-un-correo-electronico-entrante-con-una-tarea-existente) sobre lo que ocurre cuando el sistema no puede relacionar un correo electrónico con una tarea existente y copiará toda la información (comunicaciones, archivos, contactos, etc.) de la tarea cerrada existente a la nueva tarea.   &#x20;

## Si no se puede relacionar un correo electrónico entrante con una tarea existente

Si no se puede identificar ninguna información que vincule el correo electrónico con una tarea que se esté ejecutando actualmente, el sistema generará una nueva tarea (Ticket o Caso) basada en las reglas de enrutamiento configuradas del correo electrónico. Se enviará automáticamente un correo electrónico de confirmación a la dirección de correo electrónico solicitante con el número de referencia si la configuración de la ruta del correo electrónico especificada en Builder tiene “activada” la opción "enviar respuesta".

## Especificaciones adicionales

* **Ticket dividido -** si un correo electrónico entrante coincide con un Ticket dividido – ya sea el Ticket original que se dividió o uno de los Tickets subordinados en los que se dividió – se adjuntará el correo electrónico a cada uno de los Tickets SUBORDINADOS. Luego, el sistema aplicará el resto de la lógica de procesamiento de correo electrónico a cada uno de los Tickets subordinados de forma independiente.
* **Ticket fusionado -**  si un correo electrónico entrante coincide con un Ticket fusionado – ya sea uno de los Tickets originales que se fusionaron o el Ticket “objetivo” en el que se fusionó –  el correo electrónico se adjuntará al Ticket “objetivo”. Luego, el sistema aplicará el resto de la lógica de procesamiento al Ticket “objetivo”.
* **Ticket convertido en un Caso -** si un correo electrónico entrante coincide con un Ticket que fue Resuelto al convertirse en un Caso, el correo electrónico se adjuntará al Caso. Luego, el sistema aplicará el resto de la lógica de procesamiento de correo electrónico al Caso.

## Lógica de detección de correos electrónicos generados automáticamente

El sistema detecta los correos electrónicos generados automáticamente por uno o más de los siguientes motivos:

* Existe un encabezado de «x-contestación automática».
* Existe un encabezado de «x-respuesta automática».
* Existe un encabezado de «enviado automáticamente» y el valor es «generado automáticamente» o «respondido automáticamente».
* Existe un encabezado de «tipo de contenido» y el valor es «varias partes / informe» o «estado de ejecución».
* Existe el encabezado de ReturnPath y tiene un valor de «<>» o «<<>>».
