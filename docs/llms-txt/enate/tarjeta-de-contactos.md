# Source: https://docs.enate.net/enate-help/espanol/contactos/tarjeta-de-contactos.md

# Etiquetas de Contactos

Las etiquetas de contactos se utilizan para enlazar los contactos con las tareas.

## Etiquetas predeterminadas del sistema

Las etiquetas predeterminadas del sistema que se encuentran disponibles son las siguientes:

* ***Contacto primario*** - la persona principal con la que está tratando para esta consulta. Solo puede haber un Contacto primario para una tarea. Esto es obligatorio para un Ticket. Dependiendo de la configuración del Caso en Builder, esto puede ser obligatorio o no para un Caso (si se establece como obligatorio para el tipo de Caso, también es obligatorio para las Acciones de ese Caso).
* ***Solicitante original*** - la persona que planteó la solicitud inicial. Solo puede haber un Solicitante original para una tarea y es independiente de la etiqueta 'Solicitante'. El solicitante original se establecerá automáticamente en el caso de que un contacto válido haya enviado el correo electrónico que inició la tarea, o la primera persona que se establezca manualmente como "solicitante" será promovida a "solicitante original". La etiqueta Solicitante original no se puede cambiar una vez que se ha establecido y no se puede eliminar el contacto etiquetado como solicitante original de la tarea.
* ***Solicitante*** - la persona que plantea la solicitud. Solo puede haber un Solicitante para una tarea. Esto es obligatorio para un Ticket. Dependiendo de la configuración del Caso en Builder, esto puede ser obligatorio o no para un Caso (si se establece como obligatorio para el tipo de Caso, también es obligatorio para las Acciones de ese Caso).
* ***Sujeto*** - de quién trata el contenido de la tarea (puede que no sea ninguno de los anteriores). Solo puede haber un Sujeto para una tarea.

Muy a menudo los tres serán la misma persona. Si usted etiqueta a otro contacto como cualquiera de estos tipos de relaciones predeterminadas del sistema, la etiqueta será eliminada del contacto anterior - ya que solo puede haber un titular de los contactos predeterminados del sistema en una tarea.

Cuando añada manualmente el primer contacto a una tarea, se establecerá por defecto como Contacto primario, Solicitante y Sujeto. Posteriormente podrá reasignar manualmente estas etiquetas a otros usuarios.

* CC - cualquier otro contacto que se pueda copiar en cualquier correspondencia. Cuando un contacto se etiqueta solo como "CC", se mostrará en la sección separada de CC (oculta hasta que exista cualquier contacto solo CC en la tarea).

## Establecer etiquetas predeterminadas adicionales a un registro de contactos

Además de las etiquetas de contacto predeterminadas del sistema (Contacto primario, Sujeto, CC, Solicitante), puede añadir otra etiqueta de contacto predeterminada a un registro de contactos para que el uso de las etiquetas de contacto en las tareas sea más rápido y sencillo.

Por ejemplo: Si sabe que "Jane Smith" siempre será la agente de bolsa en cualquier tarea a la que se añada como contacto, puede asignarle al registro de contacto de Jane una etiqueta predeterminada de "Agente de bolsa" para que se complete automáticamente para ella en la tarea, en lugar de que usted tenga que configurar este valor de etiqueta manualmente cada vez.&#x20;

La lista disponible de Etiquetas predeterminadas se conserva en Builder, en la sección [<mark style="color:blue;">Configuración general>>Etiquetas de contacto</mark>](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/contact-tags)<mark style="color:blue;">.</mark>&#x20;

Puede configurar esta Etiqueta predeterminada siempre que añada un nuevo contacto al sistema.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FV4WTt9qOVHZrdJfdtYxr%2Fimage.png?alt=media\&token=0920663a-8368-4df8-a47b-720c705daf0e)

También puede añadir la etiqueta a los contactos existentes y editar la Etiqueta predeterminada establecida para un contacto a través de la Página de contactos.

El atributo de Etiqueta predeterminada también está disponible para editar en masa, es decir, puede configurar esto para múltiples contactos a la vez. Simplemente seleccione una cantidad de registros de contacto cuando se encuentre en la cuadrícula de la página de Contactos y haga clic en el botón de Editar para acceder a la ventana emergente de Editar en masa.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2Ft7n6hzDmADMIPfyiy4Mg%2Fimage.png?alt=media\&token=72da690e-d844-4dcf-b0f8-c17737f17c23)

### **Comportamiento de la Etiqueta de contacto predeterminada si no está establecida en "Permitir múltiples"**

Si un valor de etiqueta específico no se ha establecido en "Permitir múltiples", solo se permite que un contacto en una Tarea tenga el valor. Por ejemplo: puede ser que solo pueda existir un solo contacto de "Agente de bolsa" para un Ticket. Esto obviamente tiene un impacto en el etiquetado predeterminado si dos contactos con la misma etiqueta predeterminada que "debe ser única" se añaden a una tarea, ya sea de forma manual o automática. En este supuesto, el sistema asignará la Etiqueta predeterminada a un solo contacto (y, por lo tanto, quitará la Etiqueta predeterminada para los otros contactos). El sistema asignará al Contacto ya etiquetado un valor de *otra* etiqueta existente, en el siguiente orden de prioridad.

* Contacto primario
* Solicitante
* Sujeto
* CC
* Cualquier otro contacto en la tarea

### **Notas adicionales sobre la falta de coincidencia de las Etiquetas de contacto con la Empresa proveedora**

* No podrá añadir una Etiqueta predeterminada a un contacto si la empresa a la que está asignado tiene una Empresa proveedora diferente a la Etiqueta predeterminada.
* No podrá enviar una tarea con un contacto cuya Etiqueta predeterminada esté establecida en una Empresa proveedora diferente a la de la tarea.

## Etiquetado automático de los contactos en las tareas

### Contactos rellenados a partir de un correo electrónico inicial

**Contactos conocidos**

Cuando llega un correo electrónico de una dirección que está asociada a un contacto que ya se encuentra en el sistema y el contacto:

* tiene una configuración de alcance global; o
* tiene una configuración de alcance local, pero pertenece a la misma empresa a la que pertenecerá la tarea según las reglas de enrutamiento del correo electrónico;

entonces sus detalles se rellenan automáticamente en la Tarjeta de contactos cuando el sistema crea la tarea y se etiquetan automáticamente como Contacto primario, Solicitante original y Solicitante de la tarea. Además, si tienen una etiqueta predeterminada asignada, también serán etiquetados como tal. Sin embargo, tenga en cuenta que siempre puede entrar y editar manualmente las etiquetas una vez que se haya creado la tarea.

Cuando llega un correo electrónico de una dirección asociada a un contacto que ya está en el sistema, pero que tiene una configuración de ámbito local y pertenece a una empresa *diferente* a la que pertenecerá la tarea según las reglas de enrutamiento del correo electrónico, sus detalles NO se rellenarán automáticamente en la Tarjeta de contactos cuando el sistema cree la tarea, (y por lo tanto, no podrán ser etiquetados automáticamente en la tarea). Tenga en cuenta que siempre puede entrar y editar manualmente el contacto y las etiquetas una vez que se haya creado la tarea.

**Contactos desconocidos**

*Alcance "Global" o "Global y local" predeterminado*

Cuando un correo electrónico llega desde una dirección desconocida y:

* la configuración [<mark style="color:blue;">"Habilitar creación automática de contactos" está ACTIVADA en Builder</mark>](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation)<mark style="color:blue;">,</mark> y;
* su sistema ha sido configurado para establecer el alcance de sus contactos externos en **"Global", o "Global y local";**

entonces el contacto se creará automáticamente, tendrá un alcance global (es decir, no estará vinculado a ninguna empresa específica) y sus detalles se rellenarán automáticamente en la Tarjeta de contactos cuando el sistema cree la tarea. Además, serán etiquetados automáticamente como Contacto primario, Solicitante original y Solicitante de la tarea. Como el sistema no los conocía, no tendrán ninguna etiqueta predeterminada. Tenga en cuenta que siempre puede entrar y editar manualmente las etiquetas una vez que se haya creado la tarea.

*Alcance "local" predeterminado*

Cuando un correo electrónico llega desde una dirección desconocida y:

* la configuración [<mark style="color:blue;">"Habilitar creación automática de contactos" está activada en Builder</mark>](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation)<mark style="color:blue;">,</mark> y;
* su sistema ha sido configurado para establecer el alcance de sus contactos externos en **"Local";**

entonces el contacto se creará automáticamente, tendrá un alcance local (es decir, estará vinculado a una empresa específica) y se creará bajo la empresa en la que existe la tarea. Sus detalles se rellenarán automáticamente en la Tarjeta de contactos cuando el sistema cree la tarea y serán etiquetados automáticamente como Contacto primario, Solicitante original y Solicitante de la tarea. Como el sistema no los conocía, no tendrán ninguna etiqueta predeterminada. Tenga en cuenta que siempre puede entrar y editar manualmente las etiquetas una vez que se haya creado la tarea.

*Creación automática de contactos desactivada*

Cuando un correo electrónico llega desde una dirección desconocida y:

* la configuración [<mark style="color:blue;">"Habilitar creación automática de contactos" está DESACTIVADA en Builder</mark>](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation)<mark style="color:blue;">;</mark>

entonces la tarea se creará basándose en las reglas de enrutamiento del correo electrónico, pero los detalles del remitente del correo electrónico NO se rellenarán automáticamente en la Tarjeta de contactos cuando el sistema cree la tarea, (y, por lo tanto, no podrán ser etiquetados automáticamente en la tarea). Tenga en cuenta que siempre puede entrar y editar manualmente los contactos y las etiquetas una vez que se haya creado la tarea.

### Etiquetas de contactos rellenadas desde la Página de actividad de contacto

Cuando se crea una tarea desde el botón "Iniciar tarea" en la [<mark style="color:blue;">Página de actividad de contacto</mark>](https://docs.enate.net/enate-help/espanol/contactos/pagina-de-gestion-de-contactos), ese contacto se etiquetará automáticamente como Solicitante original, Solicitante, Sujeto y Contacto primario de la tarea, y también se añadirá su etiqueta predeterminada (si la tiene).
