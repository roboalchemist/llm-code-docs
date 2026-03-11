# Source: https://docs.enate.net/enate-help/espanol/procesamiento-de-un-caso/detalles-de-la-pantalla-de-caso.md

# La pantalla del Caso

La pantalla del Caso tiene el mismo diseño general de la pantalla del [Ticket ](https://docs.enate.net/enate-help/espanol/procesamiento-de-un-ticket/la-pantalla-del-ticket)y la [Acción](https://docs.enate.net/enate-help/espanol/procesando-una-accion/detalles-de-pantalla-de-accion), y las mismas funciones básicas, entre las que se incluyen, [añadir una nota](https://docs.enate.net/enate-help/espanol/tipos-de-tareas-tickets-casos-and-acciones/agregar-una-nota) a una tarea, [enviar un correo electrónico](https://docs.enate.net/enate-help/espanol/correos-electronicos/correos-electronicos-entrantes-logica-de-procesamiento), ver los [archivos y enlaces adjuntos](https://docs.enate.net/enate-help/espanol/tipos-de-tareas-tickets-casos-and-acciones/tarjeta-de-archivos) y ver las [Comunicaciones / Cronología](https://docs.enate.net/enate-help/espanol/tipos-de-tareas-tickets-casos-and-acciones/seccion-principal), pero también incluye algunas funciones específicas del Caso.

## Título del Caso

En la parte superior de la pantalla del Caso, podrá ver el contexto del Caso, compuesto por:&#x20;

Nombre del cliente – Nombre del contrato – Nombre del servicio – Nombre del proceso de Caso

Por ejemplo:&#x20;

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FuEBhEn8RpqXyOMX6DGmV%2Fimage.png?alt=media\&token=e5880e49-125f-4c1e-8641-61a3f6da448b)

La descripción breve del Caso se muestra en la parte derecha de la pantalla. Si la [opción “Permitir cambio de título”](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-a-case/case-screen#case-title) ha sido seleccionada en la pantalla de información del Caso en Builder, usted podrá editar la descripción breve del Caso.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2F2FhjQzo34e3g3xo2Jtpz%2Fimage.png?alt=media\&token=deee3ee5-c6ca-4858-a1c5-d6ac9dc71916)

Luego, aparecerá este título en la parte superior de la pestaña del Caso.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FegggSa5GkODanr8liv72%2Fimage.png?alt=media\&token=6db309ce-8d2a-4106-835a-8ab3771591a5)

Este es el título que también aparecerá en la columna “Título” de la cuadrícula de la página de inicio.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FezfFd0VynkznSHa8niOI%2Fimage.png?alt=media\&token=1d4a8d82-a1eb-4298-924d-9b851213bea8)

Puede copiar el número de referencia y el título del Caso haciendo clic en el icono de copiar que aparece en la pestaña:

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FeK8mfqgm4N3wUfheG30X%2Fimage.png?alt=media\&token=c63f7b50-2b14-45f9-9861-e5050c8241e3)

## Vista de las Acciones de un Caso

La pantalla del Caso está diseñada para destacar la visibilidad de las Acciones que se ejecutan en él. Para ello, existe una pestaña adicional dedicada a las “Acciones” que le permite ver rápidamente el estado de sus Acciones y acceder a ellas. Esta es la pestaña que se muestra en esta sección por defecto para los Casos.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FkJoj3sq08HxXZjoNJSAt%2Fimage.png?alt=media\&token=67c4906f-485f-4079-8c2d-8ef7c18990b7)

Esta pestaña muestra la siguiente información para cualquier Acción en el Caso:

* Icono del estado actual
* Número de referencia de la Acción
* Título e instrucciones de la Acción
* Fecha de vencimiento
* Persona asignada
* Estado de la lista en formato de texto

Las Acciones aparecerán por orden de:

1. **Estado**, con las Acciones en estado Borrador en la parte superior, seguidas de las Acciones en estado Por hacer, luego En progreso, luego Esperando, luego Resuelto, luego Cerrado. Si todos los estados son iguales, las Acciones se mostrarán por orden de:
2. **Fecha de vencimiento**, con las Acciones que vencen antes en la parte superior. Si todas las fechas de vencimiento son iguales, entonces las Acciones se mostrarán por orden de:
3. **Tiempo restante durante la pausa**, con la Acción con menos tiempo restante durante la pausa en la parte superior. Si el tiempo restante en la pausa es el mismo para todas las Acciones, entonces las Acciones se mostrarán por orden de:
4. **Número de paso**, con la Acción con el número de paso más bajo en la parte superior. Si los números de paso son todos iguales, entonces las Acciones se mostrarán por orden de:
5. **Fecha/hora de inicio**, con la Acción con la fecha/hora de inicio más reciente en la parte superior. Si la fecha/hora de inicio es la misma para todas las Acciones, entonces las Acciones se mostrarán por orden de:
6. **Número de referencia**

## Sub-casos

Los Sub-casos se crean a partir de un caso “principal” existente que mantiene un vínculo con su caso “principal” y se comportará de acuerdo con su propia configuración específica, pero su caso principal no se completará hasta que todos sus Sub-casos se hayan completado previamente.

Puede crear Sub-casos haciendo clic en el enlace “+ Tarea” que se muestra cerca de la sección de pestañas de un Caso y eligiendo la opción “Sub-caso” del menú desplegable.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2F7173rzwQRGwa3YMq7pL5%2Fimage.png?alt=media\&token=0feb7d52-11db-4492-b3d6-0e026a52c94f)

La pestaña de Sub-casos mostrará los Sub-casos para ese Caso.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mj8nUZIHmGMjv5LM6go%2F-Mj8o18I3JZ3nO3hyj0a%2FSub-Cases-Tab.gif?alt=media\&token=bd36ffad-fe23-4381-b5ff-2f74c03a9518)

Véase aquí para obtener más información sobre los Sub-casos:

{% content-ref url="sub-caso" %}
[sub-caso](https://docs.enate.net/enate-help/espanol/procesamiento-de-un-caso/sub-caso)
{% endcontent-ref %}

## Vista de una tarea enlazada a un Caso

Otra función de la pantalla de Caso es la opción de lanzar un Caso o Ticket desde el Caso para crear una relación “Enlazada” entre las tareas.

Las tareas creadas de este modo mantendrán un enlace con el Caso / Ticket original y se mostrarán en una [pestaña de Enlaces](https://docs.enate.net/enate-help/espanol/trabajar-con-elementos-de-trabajo-enlazados) dentro del mismo, facilitando el seguimiento de un grupo de tareas relacionadas entre sí.&#x20;

Véase aquí para obtener más información:

{% content-ref url="../trabajar-con-elementos-de-trabajo-enlazados" %}
[trabajar-con-elementos-de-trabajo-enlazados](https://docs.enate.net/enate-help/espanol/trabajar-con-elementos-de-trabajo-enlazados)
{% endcontent-ref %}

## Fecha de vencimiento

La fecha de vencimiento del Caso se mostrará con un código de colores que indicará si está:

&#x20;A tiempo:

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FtQuMgIfsqwWCb3eATrN1%2Fimage.png?alt=media\&token=918151de-c219-4076-bc65-7c0588c5a7de)

Para hoy:

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FlylfBQXi670qFtelZJmW%2Fimage.png?alt=media\&token=b2d09dc6-d0ae-487e-81cf-8c006837be1e)

Atrasado:

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FsM2hrLLN4Ik7jIWWuFRa%2Fimage.png?alt=media\&token=a824db83-ce90-4f14-9084-a1decb4e0881)

### Anulación de la fecha de vencimiento

Si se ha configurado un Caso con la opción de anular la fecha de vencimiento en Builder, podrá anular la fecha de vencimiento de un Caso haciendo clic en la fecha de vencimiento en el encabezado y cambiando la fecha en la ventana emergente.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FNO2OWBpJSBALLAIRO9xw%2Fimage.png?alt=media\&token=05444174-6de6-4b82-bed7-656e9ba5ac6e)

## Persona asignada

También puede ver si el Caso ha sido asignado o no, y a quién se ha asignado.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FwLZYXfG7C8CAdjOakXD4%2Fimage.png?alt=media\&token=6f0a3a04-7154-44dd-87c5-cf65f337993b)

Puede reasignar o desasignar un Caso, o asignarse a sí mismo el Caso si no se le ha asignado ya.&#x20;

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FnZH1MBiNZui81P2u5M2B%2Fimage.png?alt=media\&token=96096cf3-24fc-466d-8fc4-12ba37984adc)

Véase aquí para obtener más información sobre la asignación de tareas en Enate:

{% content-ref url="../contactos/anadir-editar-y-eliminar-contactos" %}
[anadir-editar-y-eliminar-contactos](https://docs.enate.net/enate-help/espanol/contactos/anadir-editar-y-eliminar-contactos)
{% endcontent-ref %}

## Panel lateral

### Vista del estado de un Caso

En la tarjeta de información puede ver el estado del Caso y cambiarlo según sea necesario.

La etiqueta principal a la izquierda de la Tarjeta de información mostrará el estado actual del Caso. El botón del menú desplegable a la derecha ofrece opciones para los estados a los que puede moverlo como parte del procesamiento.&#x20;

Véase aquí para obtener más información sobre el procesamiento de un Caso:

{% content-ref url="procesamiento-de-un-caso" %}
[procesamiento-de-un-caso](https://docs.enate.net/enate-help/espanol/procesamiento-de-un-caso/procesamiento-de-un-caso)
{% endcontent-ref %}

{% hint style="info" %}
**Una vez que haya seleccionado el nuevo estado en el menú desplegable y haya rellenado cualquier otra información necesaria, haga clic en el botón para confirmar.**
{% endhint %}

El borde de la Tarjeta de información se resalta en un color relacionado con el estado actual. Una vez que haya pulsado el botón para cambiar el estado, el sistema procesará los cambios.  El color del borde y el nuevo estado cambiarán para confirmar que se ha producido la actualización del estado.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FZvNslwvKmcMMYpIzVfsV%2Fimage.png?alt=media\&token=ea817dd9-819e-4f00-a4b8-543adc8beb57)

Al cambiar el estado de una tarea, si la está pasando a un estado “En progreso”, la pestaña de la tarea permanecerá abierta al confirmar el nuevo estado. Al cambiar a cualquier otro estado, por ejemplo, “En espera” o “Rechazado”, la pestaña se cerrará automáticamente. Una etiqueta debajo del estado le informará de ello con antelación.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FGDMiq8RKmUXMunSHUoOA%2Fimage.png?alt=media\&token=14eaee96-78c0-473c-9bca-02b86a3c9f32)

Además de mostrar el estado del Caso, se muestra la siguiente información directamente debajo:

* Configurado por – quién configuró el estado.
* Razón – la razón por la que cambió el estado, es decir, por qué se cambió. Esto puede hacerse de forma manual o como parte de un proceso.
* Fecha – cuándo cambió el estado.
* Última actualización por – quién cambió por última vez algunos datos del Ticket.
* Última actualización el – cuándo se cambiaron algunos datos del Ticket por última vez.

{% hint style="info" %}
Tenga en cuenta que no toda la información anterior se mostrará siempre. La información que se muestra depende del estado del Ticket y de cómo se haya configurado el Ticket en Builder.
{% endhint %}

### Vista de la configuración de un Caso

La Tarjeta de configuración muestra la información detallada del Caso e incluye lo siguiente:

* El contexto del Caso (Cliente>Contrato>Servicio>Proceso de Caso).
* Cuándo, cómo y quién creó el Caso.
* Si este Caso se creó a partir de otra tarea, la fecha de solicitud inicial muestra la fecha de inicio de la solicitud original, lo que permite captar todo el tiempo que se ha tardado en completar una solicitud.
* Mantener conmigo – la opción de mantener el Caso con el usuario actual.
* Mantener la Acción conmigo – la opción de mantener las Acciones para el Caso con el usuario actual.
* Enviar correos electrónicos automatizados – la opción de enviar correos electrónicos automatizados para el Caso. Por el momento, el único correo electrónico automatizado disponible para enviar para los Casos es un correo electrónico de reconocimiento de creación de un Caso.
* Recuento de registros – dependiendo de la configuración del Caso en Builder, el recuento de registros puede o no mostrarse aquí. Si es así, el recuento de registros se puede editar.

### Contactos del Caso

En la [Tarjeta de contactos](https://docs.enate.net/enate-help/espanol/contactos/tarjeta-de-contactos) puede especificar las personas que se relacionan con el Caso.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FTVzutNhu89tOOZNOrMQ1%2Fimage.png?alt=media\&token=936c7810-a956-4013-b2cb-3813fd6ae021)

Por defecto, las relaciones disponibles son las siguientes:

* Contacto primario – la persona principal con la que está tratando para este Caso. Esto puede ser obligatorio o no para los Casos, dependerá de la configuración del Caso en Builder.
* Solicitante – la persona que planteó la solicitud inicial. Esto puede ser obligatorio o no para los Casos, dependerá de la configuración del Caso en Builder.
* Asunto – de quién trata el contenido del Caso.

Muy a menudo los tres serán la misma persona.

* CC – cualquier otro contacto que pueda ser copiado en cualquier correspondencia. Cuando un contacto está etiquetado solo como “CC”, se mostrará en la sección separada de CC (oculta hasta que exista cualquier contacto solo CC en la tarea).

{% hint style="info" %}
Nota: es posible añadir más tipos de relaciones al sistema.  Véase aquí para obtener más información sobre cómo [añadir etiquetas de contacto.](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#adding-new-contact-tags)
{% endhint %}

La Tarjeta de contactos de un Caso no suele completarse automáticamente, por lo que es necesario añadir un contacto manualmente. Puede hacer esto buscando un contacto en la [Tarjeta de contactos](https://docs.enate.net/enate-help/espanol/contactos/tarjeta-de-contactos-1).

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZHaVmBb0E56_Q_jYnK%2F-MZHbC4BRt2U6cLKu08V%2FContact-Card-Search-for-Contact.gif?alt=media\&token=599a753b-246e-417c-af72-9df32a26189e)

Si busca un usuario en la Tarjeta de contactos que no existe en el sistema, puede crear un nuevo contacto haciendo clic en la opción “Crear contacto” y completando los detalles de este.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZHZHKfCwmT20z_i-95%2F-MZHa09WPZI3WlIY7Ea-%2FContact-Card-Create-Contact.gif?alt=media\&token=bd8d2355-15e2-4760-b594-6db9028823c3)

Si ha escrito la dirección de correo electrónico del contacto, el sistema decodificará y completará automáticamente el nombre y el apellido del contacto. Una vez que haya completado toda la información y haya hecho clic en crear contacto, el sistema lo redirigirá de nuevo a la tarea.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZHNQAkYnfT4YfYPY7I%2F-MZHZ15Kudy6pBkdjKew%2FContact-Card-Email-Address.gif?alt=media\&token=971fe34f-7a7b-4a1b-a402-d0868d662d26)

Cuando añada manualmente un contacto, se le asignarán por defecto las etiquetas Contacto primario, Solicitante y Asunto. Posteriormente podrá reasignar manualmente estas etiquetas a otros usuarios.

### Seguimiento de tiempo

Para ayudarle a gestionar la actividad con respecto a sus SLA, Enate permite a los usuarios hacer un seguimiento del tiempo que tardan las tareas en completarse, ya sea el total general o desglosado por los distintos recursos que pueden haber trabajado en ellas.

La Tarjeta de seguimiento de tiempo en las tareas hace un seguimiento del tiempo de cada sesión individual del navegador en la que se ejecuta la tarea.&#x20;

Véase aquí para obtener más información sobre el seguimiento de tiempo:

{% content-ref url="../tipos-de-tareas-tickets-casos-and-acciones/tarjeta-de-seguimiento-de-tiempo" %}
[tarjeta-de-seguimiento-de-tiempo](https://docs.enate.net/enate-help/espanol/tipos-de-tareas-tickets-casos-and-acciones/tarjeta-de-seguimiento-de-tiempo)
{% endcontent-ref %}

### Tarjeta inteligente

Además, se puede configurar una Tarjeta inteligente para mostrar los datos personalizados.

Véase aquí para obtener más información sobre las tarjetas inteligentes:

{% content-ref url="../tipos-de-tareas-tickets-casos-and-acciones/tarjetas-inteligentes" %}
[tarjetas-inteligentes](https://docs.enate.net/enate-help/espanol/tipos-de-tareas-tickets-casos-and-acciones/tarjetas-inteligentes)
{% endcontent-ref %}

### Tarjeta de defectos

Si se han [configurado categorías de defectos en la línea de servicio para un Caso en Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/service-lines-screen#b-creating-defect-categories), se mostrará una Tarjeta de defectos en la pantalla de ese Caso en Work Manager que ofrece la característica de registrar los defectos para el Caso correspondiente, si algo ha ido mal en el proceso. Estas pueden incluirse en el tablero de información gerencial para identificar las áreas del negocio que necesitan ser investigadas.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FWh6faps3U3LI6XmpAwwa%2Fimage.png?alt=media\&token=58bb6459-d672-45aa-9be8-1ae58672f276)

El menú desplegable de la “Parte culpable” registra quién fue el culpable de la aparición de ese defecto. Puede seleccionar si un Agente, el Centro de Servicio o el Cliente fue el culpable.

Si un defecto se resuelve, el usuario puede abrir el Caso específico y su defecto y marcarlo como resuelto. Los defectos se pueden eliminar mientras el Caso está en progreso.

Si la [<mark style="color:blue;">función "Restringir la modificación de los defectos"</mark>](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#restrict-defect-modification) está activada en la sección de Ajustes del sistema de Builder, se restringirá el acceso para editar los detalles de cualquier defecto existente en la tarjeta. Específicamente: mientras que cualquier agente de servicio siempre puede AÑADIR un registro de defectos y marcar uno como resuelto, solo el agente que creó un defecto específico tendrá los derechos de acceso para hacer cambios posteriores a / eliminar sus detalles.

## Actividades lanzadas desde la pantalla del Caso

### Rehacer un Caso

Si se han producido problemas durante la ejecución de un Caso, es posible que desee rehacer el Caso. Puede hacer esto desde el Caso seleccionando la pestaña “Rehacer” de la pantalla del Caso.&#x20;

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FmdepoR18i5Hx6GksJ55g%2Fimage.png?alt=media\&token=2d07f7f2-bf7c-4705-93da-8306698268ca)

Véase aquí para saber más sobre la opción de rehacer un Caso:

{% content-ref url="rehacer" %}
[rehacer](https://docs.enate.net/enate-help/espanol/procesamiento-de-un-caso/rehacer)
{% endcontent-ref %}

### Iniciar una Acción manualmente

La mayoría de las veces, las Acciones de un Caso se inician automáticamente (ya sea por el flujo del proceso o en base a la programación). Sin embargo, si una Acción ha sido configurada para ser iniciada manualmente, puede hacerlo desde el Caso utilizando la función “Iniciar Acción”.&#x20;

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FWgVh7XQZBV5pjgZW9uVC%2Fimage.png?alt=media\&token=94ffe51d-4f9c-4901-8a03-2d1f7ff59bfc)

Véase aquí para saber más sobre el lanzamiento manual de una Acción desde un Caso:

{% content-ref url="iniciar-una-accion" %}
[iniciar-una-accion](https://docs.enate.net/enate-help/espanol/procesamiento-de-un-caso/iniciar-una-accion)
{% endcontent-ref %}

## Más información sobre la pantalla del Caso

### Nueva información recibida

Cuando reciba un nuevo correo electrónico para un Caso que aún no se ha leído, el icono de Nueva información aparecerá resaltado. Al hacer clic en él, se mostrará cuándo se ha recibido la nueva información.

Puede elegir marcar la nueva información como leída, lo que hará que el icono de Nueva información vuelva a su estado normal. También puede marcar la información como no leída haciendo clic en la opción “Marcar como nuevo”.

<figure><img src="https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2F72D6CB9dVkNywp1VPc1W%2FNew-Information-Icon.gif?alt=media&#x26;token=e3a471df-f71c-404d-9f15-2fd13b0f8ed8" alt=""><figcaption></figcaption></figure>

### Procedimiento operativo estándar

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FjSJ9Qu3Uh0Op7YwDgYrd%2Fimage.png?alt=media\&token=f9489d3a-96f1-40d2-9f9b-756af9f03a10)

Esto proporciona un enlace al Procedimiento operativo estándar para la tarea que se ha establecido en Builder.
