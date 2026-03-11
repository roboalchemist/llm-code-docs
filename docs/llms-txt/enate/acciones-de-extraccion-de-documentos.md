# Source: https://docs.enate.net/enate-help/espanol/procesando-una-accion/acciones-de-extraccion-de-documentos.md

# Acciones de extracción de documentos

### Descripción general

El componente de Extracción de Documentos extrae automáticamente los datos relevantes de los archivos adjuntos a los correos electrónicos entrantes para que estos datos puedan ser utilizados en el procesamiento posterior de la tarea, lo que ahorra tiempo y esfuerzo a sus agentes. Esto también significa que documentos como los PDF pueden ser escaneados y utilizados tanto para iniciar Casos en Enate como para formar parte de las actividades del proceso en curso.

Cuando se ejecuta una Acción de Extracción de Documentos para un Caso, los documentos adjuntos al Caso pueden ser enviados a la herramienta tecnológica deseada para su escaneo y los archivos de salida procesados serán devueltos y adjuntados automáticamente al Caso.

Si en algún momento la herramienta tecnológica que está utilizando no confía lo suficiente en los resultados, basándose en un umbral de confianza que usted puede establecer, Enate transferirá instantáneamente la tarea a un agente en Work Manager para que la revise y verifique, lo que le ofrece ese apoyo de "humano involucrado".

Este componente puede ser activado por su administrador en la sección <mark style="color:blue;">Mercado en línea</mark> de Enate Builder.&#x20;

Consulte este vídeo para obtener más información:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTgwNzUwMw==>" %}

### Cómo funciona en el tiempo de ejecución

Cuando el Caso se ejecuta en Work Manager, los datos relevantes de los archivos adjuntos a los correos electrónicos entrantes serán analizados y extraídos automáticamente.&#x20;

Si la herramienta tecnológica que utiliza tiene suficiente confianza en los resultados de la extracción de datos, esta Acción ni siquiera tendrá que ser vista por un usuario humano. Simplemente se completará automáticamente y el Caso pasará a la siguiente Acción. La Acción de extracción de datos completada aún puede ser vista si hace clic en ella, pero no necesitará ser entregada a un usuario humano para su participación.

<figure><img src="https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FE0DdCvZgR54K0aAuDri6%2Fimage.png?alt=media&#x26;token=9916b599-e6b9-4687-b159-243af6466ffd" alt=""><figcaption></figcaption></figure>

Sin embargo, si la tecnología de extracción no confía lo suficiente en sus resultados de extracción de datos, la Acción se entregará a un usuario humano cuando vuelva a pulsar "extraer de la Lista" en su página de inicio, para que la recoja y la revise. Cuando un agente abra la Acción, verá que se le ha entregado porque es necesario realizar algunas comprobaciones adicionales.

<figure><img src="https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FAHCC4wRPTqOY0UMstt2L%2Fimage.png?alt=media&#x26;token=f8eef39d-b307-43ea-b48d-a88879e03652" alt=""><figcaption></figcaption></figure>

Para ello, solo tiene que hacer clic en "Verificar ahora" y desplazarse hasta la pantalla "Estación de validación" de la Acción, que muestra la imagen del documento escaneado y la tabla de valores de datos extraída resultante. Esto le permite ver dónde están resaltados esos niveles de confianza más bajos, revisarlos y hacer manualmente las correcciones necesarias. Esta pantalla puede visualizarse *in situ* o desplegarse a pantalla completa en una ventana emergente.&#x20;

<figure><img src="https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FmulDpTXwuZhiAChVYOkV%2Fimage.png?alt=media&#x26;token=43adad67-5537-4dcc-a057-b122932371b2" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Nota: Solo se puede ver un documento a la vez.
{% endhint %}

<figure><img src="https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FAeEg2eeBXKPDiWpTRa1R%2Fimage.png?alt=media&#x26;token=eb1837d1-7ec9-4091-b93d-e52f9504540e" alt=""><figcaption></figcaption></figure>

En esta pantalla de validación, el agente podrá ver una copia escaneada del archivo, que puede tener varias páginas, junto con dos pestañas que muestran los datos extraídos.

* La pestaña Datos extraídos muestra los pares clave-valor del agente de los datos extraídos junto con el nivel de confianza que EnateAI les ha asignado. Los valores se pueden ajustar cuando sea necesario y se guardan una vez que el agente hace clic en el botón de actualización de ese valor. Al hacerlo, se establecerá el valor de confianza en 100 % para esa clave.
* La pestaña Tablas muestra cualquier dato repetido que se haya seleccionado como tabla. Puede utilizar el botón Eliminar para eliminar cualquier fila que no necesite.

Si el agente necesita salir de la pantalla de la estación de validación en cualquier momento, solo tiene que hacer clic en «Guardar como borrador» para guardar los cambios realizados en un documento concreto.

{% hint style="info" %}
Nota: Si un agente accede a la pantalla de validación de una Acción que no le ha sido asignada, los datos aparecerán en modo de solo lectura y no podrán editarse. Para poder editar los datos, el agente deberá asignarse primero la Acción.
{% endhint %}

Una vez que el agente esté satisfecho con los datos, todo lo que tiene que hacer para enviar los datos actualizados es hacer clic en el botón «Enviar». EnateAI terminará el procesamiento en segundo plano y actualizará la pantalla Acción para confirmar cuando haya terminado. El procesamiento en segundo plano permite al agente pasar a cualquier otro documento que requiera verificación.

Una vez que se ha hecho clic en «Enviar» para el último documento que necesita validación, la pantalla Acción se cierra automáticamente. Una vez más, EnateAI está terminando el procesamiento en segundo plano y marcará la Acción como Resuelta después de un breve periodo de tiempo, pasando luego a Cerrada.

*Nota: Cada vez que revises y actualices los elementos de datos, EnateAI aprenderá y mejorará ligeramente sus sugerencias de extracción de datos. Si observas que la tecnología se equivoca con frecuencia en sus sugerencias, habla con tu equipo de administración para modificar el umbral de confianza.*
