# Source: https://docs.enate.net/enate-help/espanol/tipos-de-tareas-tickets-casos-and-acciones/tarjeta-de-archivos.md

# Pestaña de archivos

## **Descripción general**

Hemos realizado importantes mejoras en la forma de ver y gestionar los archivos y enlaces en los Tickets, las Acciones y los Casos.&#x20;

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTc5Nw==>" %}

La Tarjeta de archivos, que antes se mostraba en la barra lateral, se ha ampliado y reubicado en la pestaña “Archivos” en la parte principal de la pantalla de la tarea, junto a la Cronología: aquí es donde ahora puede añadir archivos y enlaces y ver los que se han añadido a la tarea.

La pestaña de archivos muestra todos los archivos y enlaces que se han añadido a esa tarea y a sus tareas relacionadas, además de los archivos adjuntos de los correos electrónicos entrantes y salientes.

Todos los archivos / enlaces de la tarea actual que está abierta se muestran en la parte superior de las pestañas de archivos, y los archivos / enlaces de sus tareas relacionadas se muestran en una sección separada debajo de esto. Las tareas se ordenan por la fecha / hora en la que se subieron, con la más reciente en la parte superior.

Puede ver el nombre del archivo, el tipo de archivo, el tamaño, quién lo subió (y cuándo), además del número de referencia y la tarea a la que se subió. También puede ver las [etiquetas ](#etiquetar-archivos-y-enlaces)y [notas ](#anadir-notas-a-los-archivos)que se han añadido a los archivos.

Varios iconos le ayudan a identificar más información:

* Los archivos adjuntos estándar se indican con el icono de un clip: <img src="https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FFmN1L9j3LDOaruzKg37x%2Fimage.png?alt=media&#x26;token=11206fb7-00ef-473f-b667-c79fa4c9f950" alt="" data-size="line">
* Los enlaces se indican con un icono de enlace: ![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FgTVQJ156lkHJyF7DklIM%2Fimage.png?alt=media\&token=187c73de-bda3-480f-804c-5fdee61f45ce)
* Los archivos adjuntos de los correos electrónicos entrantes se indican con un icono de correo electrónico verde: ![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FYxu6OTV74CAiptT05XbC%2Fimage.png?alt=media\&token=18bbd221-c264-4512-a13b-3882cedb602f)
* Los archivos adjuntos de los correos electrónicos salientes se indican con un icono de correo electrónico azul: <img src="https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FvVgHnbgrXjtSdOROVFir%2Fimage.png?alt=media&#x26;token=f40694cb-6f05-4257-84f8-f8c193fc3a06" alt="" data-size="line">

Todos los archivos de la pestaña de archivos pueden añadirse como [archivos adjuntos a cualquier correo electrónico](https://docs.enate.net/enate-help/espanol/correos-electronicos/adjuntar-archivos-a-un-correo-electronico) saliente y los enlaces pueden añadirse al cuerpo del correo electrónico.

{% hint style="info" %}
Tenga en cuenta que cuando realiza una actualización desde versiones anteriores a la 2022.3, los archivos que están adjuntos directamente a una tarea se mostrarán en la sección “Otras tareas” sin un número de referencia. Sin embargo, los archivos adjuntos de los correos electrónicos de esta tarea se *mostrarán* en la sección “Actual”.
{% endhint %}

## Añadir archivos / enlaces a una tarea

Si la tarea está asignada a usted, puede añadir archivos y enlaces a una tarea en la pestaña Archivos. Se pueden subir varios archivos a la vez. Para ello, haga clic en los enlaces de subir en la parte superior de la pestaña.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FIKtIsCIZWJOJE9JvAhSn%2Fimage.png?alt=media\&token=4d1bcb8c-2249-4fcf-aafb-66490cd0a648)

También puede arrastrar y soltar archivos en la pestaña de archivos para subirlos.

{% hint style="info" %}
Nota: el tamaño máximo por archivo es de 100 MB.
{% endhint %}

### Restricciones al tipo de archivo

Por defecto, todos los tipos de archivos pueden subirse. Sin embargo, se *pueden* restringir los tipos de archivos especificando los tipos aceptables en la sección de [configuración general de Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#allowed-file-types).

## Etiquetar archivos y enlaces

Se pueden añadir etiquetas a los archivos y a los enlaces. Las etiquetas le ayudan a estructurar sus archivos, y a adjuntar automáticamente archivos con determinadas etiquetas a los mensajes de correo electrónico que envía automáticamente el sistema o a las respuestas estándar de los mensajes que se redactan. También permiten que las rutinas de automatización externas sepan qué archivos específicos deben recoger de una tarea.

El etiquetado de archivos también es una función importante para los procesos que implican tecnología de automatización. Ejemplo: si una Acción automatizada posterior necesita saber cuál de los archivos que ha adjuntado a su Caso es el archivo de "Confirmación de factura", puede etiquetar los archivos relevantes como tales y, sin importar el nombre del archivo, la tecnología de automatización sabrá seleccionar ese archivo en función de su etiqueta. Esta tecnología de automatización externa también puede suministrar etiquetas como parte de la carga de documentos en Tareas en Enate para su posterior uso manual o automatizado.

Los títulos de las etiquetas disponibles se [establecen en Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/file-tags). Si con frecuencia comprueba que una etiqueta específica no está disponible para su selección, asegúrese de hablar con su equipo de administración para que la añadan.

Puede añadir una etiqueta a un archivo haciendo clic en el icono "+" y seleccionando después una etiqueta de la lista resultante.

!\[A screenshot of a computer

Description automatically generated]\(<https://lh4.googleusercontent.com/D0RHOWi5ZzK-vQuhTNv_MSP-byAOPTgT3iiylCUww0qSTXvReDZRcfGBVBhTNb7zJL9aoygoQ7cg7Bh_gLMvPcv5YCSYF57WRH5AD30m53mvRKwpph0KqStu7CE6KMUh7wNXUIq0sanePbYIW3nmPA>)

También puede añadir etiquetas a varios archivos y enlaces a la vez, seleccionando una o varias tareas y utilizando el icono que se muestra en el encabezado de la pestaña Archivos.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FjiSsM7PVLSOQasyTWiHa%2Fimage.png?alt=media\&token=5bcad862-0b10-48b6-b481-498d6499bafb)

Enate también puede ayudar a etiquetar automáticamente los archivos adjuntos a los correos electrónicos. Hay varias opciones disponibles en la sección [Mercado en línea](https://docs.enate.net/enate-help/builder/builder-2021.1/integrations-marketplace) de Enate Builder para habilitar componentes (tanto de Enate como de terceros) que analizan el contenido del correo entrante, incluida la capacidad de sugerir etiquetas para los adjuntos de correo electrónico en función de su contenido.

Si su administrador ha activado un componente de etiquetado automático, verá algunos datos adicionales en la sección de etiquetas de archivos, donde se han realizado sugerencias automáticas de valores de etiquetas para un archivo adjunto.

!\[A screenshot of a computer

Description automatically generated]\(<https://lh6.googleusercontent.com/sjnSvQ17kcn_y63B968uYRk_tyqZqtE9DNWZKQwQkivIQtLTSjAHO7knGLZMbSrxKIzc4ptpBrkJHLQqIGdyDUXwUTvDTu6vSQIEeXuNpJ9EFWaPDSYW-561EKVvYyXjj76MQYyOS3yD2eEAcyd0mA)\\>
\
Si la tecnología que utiliza confía lo suficiente en su sugerencia de etiquetado, la etiqueta aparecerá en verde. Si está de acuerdo con la sugerencia, no tiene que hacer nada, pero si no lo está, puede hacer clic para cambiarla.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FagKTNm3RNdVCa9LznVnp%2Fimage.png?alt=media\&token=f1a63e3b-1216-465c-a2e7-051036d97156)

\
Y si la tecnología se mostró menos confiada en su sugerencia de etiqueta, la etiqueta aparecerá resaltada en naranja. Si está de acuerdo con la etiqueta sugerida, asegúrese de confirmarla; de lo contrario, cámbiela según sus preferencias. Cada vez que haga esto, la tecnología aprenderá y mejorará un poco la sugerencia de etiquetas. Si observa que la tecnología se equivoca con frecuencia en sus sugerencias, hable con su equipo de administración para modificar el umbral de confianza.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FoxXAKvJXEUedKcCfmL54%2Fimage.png?alt=media\&token=c343924d-9d3b-4e7f-b0ab-e7339de45b53)

\
Una vez que se hayan añadido las etiquetas, los archivos/enlaces estarán disponibles para ser añadidos automáticamente a los correos electrónicos con etiquetas coincidentes, lo que le permitirá asegurarse de que todos los documentos de un tipo relevante se incluyen con correos electrónicos específicos/contenido del cuerpo del correo electrónico.

Cuando se inserta un [texto de respuesta estándar](https://docs.enate.net/enate-help/espanol/correos-electronicos/textos-enlatados) en un correo electrónico manual o cuando se crea automáticamente un nuevo correo electrónico y se envía durante el proceso, el sistema identificará cualquier etiqueta vinculada al texto estándar/plantilla de correo electrónico y, a continuación, adjuntará automáticamente todos los archivos de esa tarea que compartan la misma etiqueta. Las etiquetas se vinculan al contenido de la respuesta estándar/correo electrónico como parte de la configuración del sistema por parte de los usuarios administradores en Builder al crear [plantillas de correo electrónico](https://docs.enate.net/enate-help/builder/builder-2021.1/email-template-configuration).

{% hint style="info" %}
Nota: Si las etiquetas de archivo no están [configuradas en su sistema](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/file-tags), esta opción de "añadir etiqueta de archivo" no se mostrará.
{% endhint %}

Una vez que se hayan añadido las etiquetas, los archivos/enlaces estarán disponibles para su incorporación automática a los correos electrónicos con etiquetas coincidentes, lo que le permitirá asegurarse de que todos los documentos de un tipo relevante se incluyan con correos electrónicos específicos/contenido del cuerpo del correo electrónico.

Cuando se inserta un texto de respuesta estándar en un correo electrónico manual o cuando se crea automáticamente un nuevo correo electrónico y se envía en proceso, el sistema identificará cualquier etiqueta vinculada al texto estándar/plantilla de correo electrónico y entonces adjuntará automáticamente todos los archivos de esa tarea que compartan la misma etiqueta. Las etiquetas están vinculadas al contenido de la respuesta estándar/correo electrónico como parte de la configuración del sistema realizada por los usuarios administradores en Builder al crear las plantillas de correo electrónico.

El etiquetado de archivos es también una característica importante para los procesos que implican tecnología de automatización. Por ejemplo: si una Acción automatizada posterior necesita saber cuál de los archivos que ha adjuntado a su Caso es el archivo de “Confirmación de factura”, puede etiquetar los archivos relevantes como tal y, sin importar el nombre del archivo, la tecnología de automatización sabrá seleccionar ese archivo basándose en su etiqueta. Dicha tecnología de automatización externa puede igualmente suministrar etiquetas como parte de la subida de documentos en Tareas en Enate para su posterior uso manual / automatizado.

{% hint style="info" %}
Nota: si las etiquetas de archivo no están configuradas en su sistema, esta opción de “añadir etiqueta de archivo” no se mostrará.
{% endhint %}

## Añadir notas a los archivos

También puede añadir notas a los archivos y enlaces para proporcionar una breve descripción del contenido o para aportar cualquier otro tipo de información que pueda ser útil. &#x20;

Asimismo, puede añadir notas a varios archivos y enlaces a la vez seleccionando una o más tareas y usando el icono que luego se mostrará en el encabezado de la pestaña de Archivos.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FLRL1DaVdZ2C88DtwmyeP%2Fimage.png?alt=media\&token=9cfe0715-fe29-4d89-93a6-b7bc67b308c0)

## Ver vista previa de los archivos

El menú a la derecha le permite ver una vista previa de un archivo individual. La vista previa se abrirá en una pestaña nueva.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FNDZLLlyl9i6yaTnN4Kpb%2Fimage.png?alt=media\&token=2d8a9ee9-65dd-4eeb-b523-cfee5d694198)

{% hint style="info" %}
Si el archivo no se puede previsualizar, aparecerá un banner de confirmación para explicarlo y ofrecer una opción para descargar el archivo. Los tipos de archivos compatibles con la vista previa son los siguientes: **txt, pdf, jpg, jpeg, jpe, jif, jfif, jfi, png, gif, web, tiff, tif, heif,heic, svg, svgz.**
{% endhint %}

## Descargar archivos

Puede descargar archivos individuales haciendo clic en la opción que aparece en el menú a la derecha.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FthtubYicmcnobNj1qE4K%2Fimage.png?alt=media\&token=a38329cc-ed26-4e87-973e-b20aeb6ccaa4)

Puede descargar varios archivos a la vez seleccionando los archivos que desea descargar y seleccionando la opción en la parte superior de la pantalla. Estos pueden descargarse como múltiples archivos individuales o como un único archivo ZIP comprimido a través de la opción de descarga ZIP aquí.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FexOuy3pfSCQ7xFkJc5kQ%2Fimage.png?alt=media\&token=42355e4a-c58c-4b65-8ece-e69c7f121e62)

## Eliminar archivos / enlaces

Puede eliminar archivos o enlaces individualmente haciendo clic en el menú a la derecha.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2F5IcI2hcXw4Jkfxv3jwf2%2Fimage.png?alt=media\&token=b8992fac-2961-4ffa-a44d-42824d830a3c)

También puede eliminar múltiples archivos / enlaces seleccionando los archivos / enlaces que desea quitar y seleccionando la opción de eliminar que aparece en la parte superior de la pantalla.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FYaZHuGRoF8BWewh1FhCs%2Fimage.png?alt=media\&token=61d630f2-af1b-4c92-b135-5d8d51d1536f)

## Filtrar archivos / enlaces

Puede filtrar los archivos y enlaces que se muestran en la pestaña de archivos con la opción de filtrar en la parte superior. Puede filtrar por: archivos adjuntos, archivos adjuntos de correos electrónicos salientes, archivos adjuntos de correos electrónicos entrantes y enlaces.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FDWJI8hJRjPU9j3kLZozO%2Fimage.png?alt=media\&token=cd9c9863-dbed-47de-aeed-44a71d49d5df)

### Búsqueda de archivos de texto libre

También hay una búsqueda de texto libre para ayudarle a localizar archivos o enlaces individuales. Puede buscar en función de los distintos grupos de texto que se muestran: nombre del archivo, información de la etiqueta y textos de las notas.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2F2ouHWcDQNZitPwrdxx30%2Fimage.png?alt=media\&token=c247a4ca-f518-462a-9ed8-438d5e16ff4f)
