# Source: https://docs.enate.net/enate-help/espanol/procesando-una-accion/acciones-de-abbyy-flexicapture.md

# Acciones de ABBYY FlexiCapture

Enate es capaz de proporcionar integración con [ABBYY FlexiCapture ](https://www.abbyy.com/flexicapture/)- esto se consigue mediante el uso de una Acción integrada de ABBYY FlexiCapture (véase [aqui ](https://docs.enate.net/enate-help/integrations/enate-integrations/ocr-integration/abbyy-integration)cómo crear y configurar este nuevo tipo de Acción).

Cuando se ejecuta una Acción de ABBYY para un Caso, los documentos adjuntos al caso pueden enviarse a ABBYY FlexiCapture para el escaneo OCR y los archivos de salida procesados se devolverán y se adjuntarán automáticamente al Caso.

{% hint style="info" %}
Nota: Solo se pueden enviar los tipos de archivo compatibles con ABBYY v12 en adelante. Haga clic [aquí ](https://help.abbyy.com/en-us/flexicapture/12/standalone_operator/input_formats/)para ver el siguiente enlace con la lista de formatos compatibles con ABBYY.
{% endhint %}

El sistema mostrará este mensaje mientras espera que usted envíe el o los documentos al motor de ABBYY FlexiCapture para su procesamiento:

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FLKFhheDIQ8mud7P3s1f1%2Fimage.png?alt=media\&token=31925fdb-b0b6-4dfa-ab15-19f6c30e9166)

Verá la confirmación de que los documentos se han enviado correctamente a ABBYY para su procesamiento:

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FUl6QgQtA0fjs56FbRw7u%2Fimage.png?alt=media\&token=88f2db37-5ff9-4cae-a143-b3a6eacceab7)

Último intento hace referencia a la hora en la que el o los documentos se enviaron al motor de ABBYY FlexiCapture para su procesamiento.

Si los documentos enviados tenían un formato de archivo no válido o si había problemas con el formato del propio documento, el sistema devolverá este mensaje:

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FKUoMTdROAv3uqB9z9NzL%2Fimage.png?alt=media\&token=2411a568-b7a9-47ce-a044-c7818ff43ec2)

### **Reintentos automáticos**

Si se produce un problema con el envío de documentos, el sistema reintentará automáticamente enviarlos un número determinado de veces, dependiendo de cómo se haya configurado el sistema en Builder (véase [aquí ](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#automated-failure-retry-pattern)para obtener más información).

Si sigue habiendo un problema con el envío después de los reintentos automáticos (por ejemplo, si la configuración de reintentos está establecida en 5 y el sistema no consigue establecer una conexión después de 5 reintentos automáticos), la acción de ABBYY pasará a un estado de "Cerrado".

{% hint style="info" %}
En *esta* circunstancia, si la Acción no logra establecer una conexión con el sistema externo, esto se elevará al Propietario del Caso, resaltando en la sección de Acción de la pantalla del Caso que esta Acción fue Cerrada - No Realizada con Éxito.
{% endhint %}

## Validación

Después de haber escaneado un documento, ABBYY crea una puntuación basada en la confianza que tiene en la calidad del escaneo. Si la puntuación de confianza está por encima del umbral definido, no se requiere ninguna verificación y procesará los datos y completará la tarea. Si la puntuación de confianza está por debajo de un determinado umbral, se requiere una verificación humana.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWskNwXafCKXzHPD007%2F-MWslty_G4gksJ22CFBo%2Fimage.png?alt=media\&token=8e051fb0-72bd-4144-802f-29c87bc62933)

### No se requiere verificación <a href="#no-verification-required" id="no-verification-required"></a>

Un mensaje de estado confirmará que la validación humana no es necesaria:

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FfjuaBCkfMJe7EWguj0Hd%2Fimage.png?alt=media\&token=4e150c1a-8d7f-4e99-9ab9-f35473431682)

Una vez completado el procesamiento, la acción de ABBYY se cerrará. Los archivos exportados se adjuntarán al Caso y serán visibles en la Tarjeta de Archivos.

{% hint style="info" %}
Nota: si se han configurado las "Etiquetas de archivo de salida", ABBYY aplicará la etiqueta de salida a todos los archivos que haya procesado, listos para su uso en actividades posteriores.
{% endhint %}

### Se requiere verificación humana

El sistema le avisará si se requiere una verificación humana:

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2F2hlWqzuLVj80LP63kQqL%2Fimage.png?alt=media\&token=675c6d19-3538-4489-8dc0-95ef68be79e2)

Además, se mostrará un texto recordatorio junto al estado de la acción para reafirmar que la verificación manual debe completarse en ABBYY antes de continuar.

Al hacer clic en el botón "Verificar", accederá a la estación de verificación de ABBYY, donde podrá verificar los escaneos de los documentos y ajustar la información según sea necesario.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2F1teLm1GXaZXfaOvAB4k4%2Fimage.png?alt=media\&token=740b5f28-15bc-4280-b30b-c07a3ac9e84b)

Una vez que haya iniciado la sesión, se le presentará la pantalla de la estación de verificación de ABBY FlexiCapture, donde podrá revisar y ajustar la información según sea necesario.

El Puesto de Verificación se compone de tres secciones:&#x20;

1. Las páginas individuales del documento a escanear.
2. Un primer plano del documento original que se va a escanear.
3. La salida extraída - es decir, la versión escaneada del documento original

El texto resaltado en amarillo en la ficha del documento original son los datos que ABBYY no puede leer.&#x20;

Esto está resaltado en rojo en la salida extraída. Ciertos caracteres como la 'i' también pueden ser resaltados en la sección Salida extraída si ABBYY no está seguro de la copia escaneada.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2F6AeOm756tSzIqVpHGkC8%2Fimage.png?alt=media\&token=f1fe76c0-b95f-42db-b3eb-662f500cfd36)

Una vez que haya terminado la verificación manual, la pantalla confirmará que se ha realizado, pero señalará que había una expectativa que requería la intervención manual:

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FPsjYHzbSOiBciVhJg6mq%2Fimage.png?alt=media\&token=5dd381c2-1bac-4f7c-9f3d-154f3f40cfda)

Una vez completado el procesamiento, los archivos exportados se adjuntarán al Caso y serán visibles en la Tarjeta de Archivos.

A continuación, puede marcar la Acción como completa.

{% hint style="info" %}
Nota: si se han configurado las "Etiquetas de archivo de salida", ABBYY aplicará la etiqueta de salida a todos los archivos que haya procesado, listos para su uso en actividades posteriores.
{% endhint %}
