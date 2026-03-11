# Source: https://docs.enate.net/enate-help/espanol/buscador-rapido/como-funciona-el-buscador-rapido-detalles.md

# Cómo funciona el Buscador Rápido: detalles

Explicación adicional de cómo funciona el *Buscador Rápido*: hay tres tipos diferentes de búsquedas en paralelo cuando introduce datos de búsqueda en el *Buscador Rápido*:

**1) Búsqueda específica con** **número de referencia.** Esto se basa en reconocer el formato del número de referencia de las *Tareas* y luego sugerir resultados relacionados con *Tickets, Casos, Acciones* que tienen esa referencia. Simplemente escriba la referencia, p.ej. "40308-T " y el sistema lo reconocerá como referencia. No necesita introducir un código corto principal.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2Fk06smuSY5pgN3ztfgp6f%2Fimage.png?alt=media\&token=90380b5f-e34e-4d2e-a4ae-07b363c0600c)

**2) Búsquedas de campos de datos personalizados**. Como se describió anteriormente. El sistema sabrá hacer este tipo de búsqueda cuando introduzca un código corto conocido, p.ej. 'FN:'. La búsqueda será para un campo que contenga el valor específico que introduzca. Vea la nota más abajo en *Comodines*.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FYeREdrMrnFuPvmiDhzAb%2Fimage.png?alt=media\&token=e8781adc-be6c-4393-813f-8b24ad380192)

**3) Búsqueda de texto libre para las tareas, comunicaciones y personas** frente a cualquier otra cosa que se introduzca que no se ajuste a los dos primeros tipos de datos reconocidos. El sistema busca en texto libre las palabras individuales frente a varios atributos del sistema de las tareas, las comunicaciones y las personas, por ejemplo, el título de la tarea, el asunto y el cuerpo del correo electrónico.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FBNKojWS7DhgyoPTrBdOt%2Fimage.png?alt=media\&token=7b39be59-21b4-4563-b102-1ed23210164d)

**4) Búsqueda de archivos por "Inicio con"**: el sistema utiliza una lógica de "Inicio con" para la búsqueda de archivos en la que añade un carácter comodín al FINAL de los textos de búsqueda. Esto significa que si se busca un archivo llamado "Procesamiento de factura.docx", las búsquedas de "procesamiento" no encontrarán el archivo, pero las búsquedas de "factura" sí lo harán.

## Comodines para búsquedas abiertas

Al buscar, el sistema agregará un *Comodín* al FINAL de los textos de búsqueda, no al inicio.

Para búsquedas específicas de *Datos Personalizad*os, un ejemplo de comportamiento sería: Al buscar por p.ej. "P: John Smi" encontraría elementos con el valor "John Smith" en un campo ‘*Persona*’ pero buscando únicamente "p: Smith" **NO** lo encontraría.

En resumen: con las *Búsquedas de Campos de Datos Personalizados*, buscamos el valor preciso del campo, o el inicio del valor. Las búsquedas de texto libre no son exactamente lo mismo, ya que una búsqueda de texto libre intentará hacer coincidir cada palabra individual dentro de un valor de texto para obtener una coincidencia, en lugar del valor en su conjunto.

También se añaden *Comodines* al final de las búsquedas de números de referencia.

### **Ejecutar Comodines mientras escribe**

Mientras usa el *Buscador Rápido*, el sistema hará una *Búsqueda Comodín* de la última palabra, p.ej. si usted escribe en el formato de texto libre de búsqueda: "John return prio". El sistema usará como *Comodín* la última palabra y también filtrará resultados con, p.ej. 'prioridad'.

Una vez que haya presionado la tecla de espacio, el sistema concluirá que ha terminado de escribir esa palabra y buscará sin usar un *Comodín*.

## Otros términos de búsqueda ignorados

Para mantener el rendimiento del sistema, las búsquedas ignoran lo siguiente:

* Palabras de 1 a 2 caracteres.
* Palabras en la "Lista de parada" del sistema. Estas son palabras comunes estándar como "y", "el/la/los/las", "yo", etc., que de lo contrario arrojarían demasiados resultados. Consulte [aquí la lista completa de palabras que se ignoran en las búsquedas](https://docs.enate.net/enate-help/espanol/apendice/busqueda-de-terminos-ignorados-mas-detalles#lista-de-parada) (en el Buscador Rápido y en cualquier otra búsqueda del sistema).&#x20;
* Caracteres específicos que se ignoran, por ejemplo, "\*", "?", "@", etc. específicamente en el Buscador Rápido. Consulte [aquí una lista completa de los caracteres que se ignoran](https://docs.enate.net/enate-help/espanol/apendice/busqueda-de-terminos-ignorados-mas-detalles#caracteres-ignorados-en-el-buscador-rapido)<mark style="color:blue;">.</mark> Esto significa, por ejemplo, que cuando se busque customer.com en el Buscador Rápido, se buscarán las palabras "customer" y "com". Se recomienda colocar estas combinaciones de palabras entre comillas para buscarlas como una frase en concreto, es decir, la búsqueda de "customer.com" probablemente le devolverá los resultados que está buscando.

## **Otros aspectos a tener en cuenta para el Buscador Rápido**

El *Buscador Rápido* es una búsqueda basada en texto. La introducción de fechas en las cadenas de texto puede arrojar resultados incoherentes. Utilice las "comillas" siempre que sea posible para ayudar a la búsqueda a buscar cadenas de caracteres completas.&#x20;

Utilice los deslizadores de fecha para buscar resultados en rangos de fechas especíﬁcos

Cuando busque varias palabras, la búsqueda utilizará una lógica "Y" en lugar de "O", es decir, devolverá los elementos con Manzana Y Banana Y Pera.

## **Detalles de las búsquedas en las tareas y en los correos electrónicos**

Es importante tener en cuenta que el *Buscador Rápido* realiza tres búsquedas independientes:

* una para las tareas (Casos, Acciones, Tickets)
* otra para los correos electrónicos que pueden estar relacionados con ellas
* y otra para las personas.

Un efecto de esto puede ser que, si se busca, por ejemplo, una combinación de tres palabras, como manzana, banana y pera, el *Buscador Rápido* devolverá los resultados de cualquier tarea en la que aparezcan las tres palabras y, por separado, cualquier correo electrónico en el que aparezcan las tres palabras. Las situaciones en las que dos de las palabras aparecen en la tarea, y la tercera solo en un correo electrónico asociado, no serían devueltas por ninguna de las dos búsquedas.

Las características específicas con las que se realizan las búsquedas de tareas son las siguientes:

* Referencia de la Tarea Título
* Nombre del cliente&#x20;
* Nombre del proveedor&#x20;
* Nombre del contrato
* Nombre del servicio&#x20;
* Nombre de la línea de servicio
* Nombre del tipo de procesamiento

&#x20;Las características específicas con las que se realizan las búsquedas de Comunicaciones son las siguientes:

* Título del correo electrónico&#x20;
* Cuerpo del correo electrónico
* Dirección de correo electrónico (De, A, CC, BCC)
* Cuerpo de la nota interna (para las notas agregadas en Enate / Autoservicio).
