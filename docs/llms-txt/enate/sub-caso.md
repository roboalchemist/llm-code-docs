# Source: https://docs.enate.net/enate-help/espanol/procesamiento-de-un-caso/sub-caso.md

# Sub-caso

## Crear un Sub-caso

Un Sub-caso se comportará de acuerdo con su propia configuración específica, pero su caso "principal" no se completará hasta que todos sus sub-casos se hayan completado.

Por lo tanto, solo se puede crear un Sub-caso a partir de un Caso existente.

Para crear un Sub-caso, haga clic en el enlace “+ Tarea” que se muestra cerca de la sección de pestañas de un Caso y elija la opción de “Sub-caso”' del menú desplegable.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FfjJ70044JxSh7eHwVebb%2Fimage.png?alt=media\&token=2c35d5f8-8be2-4aa3-af25-534014593969)

En la ventana emergente resultante, puede filtrar para buscar el nuevo tipo de proceso de Sub-caso que desea crear de dos maneras:

* buscando por ruta de correo electrónico: puede especificar la dirección del buzón al que normalmente se envían los correos electrónicos para crear tareas. A menudo, un buzón de correo electrónico representa una parte determinada de la empresa en la que desea crear su nueva tarea. Como un atajo útil, hemos añadido una función en la que puede buscar por buzón de correo y limitar directamente los procesos de Sub-caso que puede elegir. Al seleccionar un buzón de correo se filtrarán las opciones desplegables a solo los procesos vinculados a ese buzón.
* seleccionando un Cliente, un Contrato, un Servicio y un proceso de Sub-caso para lanzar (estos serán los valores por defecto si solo hay una opción para elegir). Tenga en cuenta que el cliente de un Sub-caso se rellenará automáticamente como su Caso principal, es decir, el Caso a partir del cual lo está creando.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2F4OL4SiE5WvueeItHG3MS%2Fimage.png?alt=media\&token=84319f3b-4438-4034-b131-ce56aadc2ca2)

{% hint style="info" %}
Tenga en cuenta que los Sub-casos disponibles para su lanzamiento dependerán de la configuración de permisos en Builder. Además, solo podrá seleccionar un proceso de Sub-caso desde una ruta de correo electrónico que haya sido habilitada en Builder ([véase aquí para más información](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/email-routes-detail)). También podrá seleccionar un proceso de Sub-caso en [Modo de prueba](https://docs.enate.net/enate-help/espanol/modo-de-prueba) si la ruta de correo electrónico para ese proceso de Sub-caso ha sido configurada para ejecutarse en [Modo de prueba](https://docs.enate.net/enate-help/v/espanol/modo-de-prueba).
{% endhint %}

A continuación, puede configurar los siguientes ajustes para el Sub-caso:

| Anular fecha de vencimiento | Si su sistema se ha sido configurado de este modo ([véase aquí para más información](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/due-date-flavours#a-overview-of-due-date-flavours)), puede elegir anular la fecha de vencimiento del nuevo Sub-caso que está creando. |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Descripción                 | Puede modificar la descripción del nuevo Sub-caso que está creando.                                                                                                                                                                                                                                                       |
| Programa                    | Si su sistema se ha sido configurado de este modo ([véase aquí para más información](https://docs.enate.net/enate-help/builder/builder-2021.1/schedules-and-frequency-based-triggers/configuring-schedules)), debe seleccionar un programa para el nuevo Sub-caso que está creando.                                       |
| Añadir contactos            | Puede añadir varios contactos diferentes para el nuevo Sub-caso y dividir las etiquetas entre ellos según sus necesidades.                                                                                                                                                                                                |

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FkMKZnmcgksDwSEsjOSiu%2Fimage.png?alt=media\&token=0e8ff87f-43ac-4027-b327-46339c26b5bc)

{% hint style="info" %}
Por favor, tenga en cuenta que los Defectos, Archivos, Enlaces y Datos personalizados se compartirán automáticamente desde el Caso principal a su nuevo Sub-caso. Las comunicaciones del Caso principal y sus tareas relacionadas, así como sus Acciones y Sub-casos (si los hubiere) también se compartirán con el nuevo Sub-caso. Sin embargo, tenga en cuenta que los correos electrónicos no se compartirán, pero puede verlos fácilmente seleccionando la opción ["Incluir tareas relacionadas" en la cronología](https://docs.enate.net/enate-help/espanol/tipos-de-tareas-tickets-casos-and-acciones/seccion-principal)<mark style="color:blue;">.</mark> También tenga en cuenta que las actualizaciones de los defectos, archivos, enlaces, datos personalizados o comunicaciones en el nuevo Sub-caso también se actualizarán en el Caso principal.
{% endhint %}

Aparecerá un enlace al nuevo Sub-caso en la [pestaña de Sub-casos](https://docs.enate.net/enate-help/espanol/trabajar-con-elementos-de-trabajo-enlazados#pestana-de-sub-casos) y NO en la [pestaña de Enlaces](https://docs.enate.net/enate-help/espanol/trabajar-con-elementos-de-trabajo-enlazados#visualizar-las-tareas-enlazadas-la-pestana-de-enlaces).

### **Pestaña de Sub-casos**

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FjeaGRPjGJu18sttbNg7G%2FSub-Cases-Tab.gif?alt=media\&token=7c2932a2-f570-45c3-927a-f802b796baa8)

La pestaña de Sub-casos mostrará la siguiente información para cualquier Sub-caso bajo un Caso:

* Estado actual del icono
* Número de referencia del Sub-Caso y título del Caso
* Cantidad de Acciones – La cantidad de Acciones asociadas a este Sub-caso Propietario– el Propietario del Caso *(si está definido)*
* Lista – la Lista de Casos *(si está definida)*
* Fecha de vencimiento – La fecha de vencimiento del Caso
* Icono para desplegar el Sub-caso y revelar sus Acciones

#### Lógica del número de referencia del Sub-caso

Los números de referencia de los Sub-casos se pueden desglosar de la siguiente manera:

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FjqApHJbFiOpIjS2Axzmz%2Fimage.png?alt=media\&token=fc03367c-ccf3-49db-adfc-a9a3e5edfbbb)
