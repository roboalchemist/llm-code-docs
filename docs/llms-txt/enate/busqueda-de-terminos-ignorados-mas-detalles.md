# Source: https://docs.enate.net/enate-help/espanol/apendice/busqueda-de-terminos-ignorados-mas-detalles.md

# Búsqueda de términos ignorados – más detalles

Como parte de las funciones estándar subyacentes en Enate para optimizar las búsquedas que realizan los usuarios, se eliminan de las búsquedas ciertos términos de uso común si se han introducido manualmente. De este modo, se garantiza una respuesta oportuna a los resultados de las búsquedas, además de evitar que se arrojen grandes volúmenes de resultados calificados que oculten los resultados deseados por los usuarios. Uno de los métodos utilizados para ello es el uso de “Listas de parada”.

## Lista de parada

Una lista de parada es una lista de palabras comunes estándar, como “y”, “el”, “yo”, etc., que se ignoran en las búsquedas que, de otro modo, arrojarían demasiados resultados.

A continuación, se muestra una lista completa de todas las palabras de la lista de parada que TODAS las búsquedas dentro de Enate ignorarán - esto no solo incluye el Buscador Rápido, sino también las búsquedas que se realizan para los usuarios, las búsquedas de correos electrónicos, las búsquedas de Tareas, por ejemplo, para los Tickets cuando se fusionan los Tickets, etc. Si introduce cualquiera de estos términos, se ignorarán automáticamente como términos para los que se pueden obtener resultados de búsqueda.

{% file src="<https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FsxuFkOUAEXTsl9l8oPsF%2FEnate%20SQL%20Stop%20List.xlsx?alt=media&token=6ce776cb-c8d0-4f12-9585-19690e0b95ec>" %}

Se admiten múltiples Listas de parada para varios idiomas de usuario.

{% hint style="info" %}
Nota: Cuando se buscan usuarios y correos electrónicos, siempre se utiliza la lista de parada en inglés (británico). Para las Tareas (Título, Nombre del Cliente, Nombre del Contrato, Nombre del Servicio, Nombre del Caso/Ticket, etc.) utilizamos el idioma del usuario conectado para encontrar la lista de parada. Además, tenga en cuenta que SQL no es compatible directamente con el húngaro, por lo que la lista de parada aplicada para las búsquedas de los usuarios húngaros es también la lista de parada inglesa.
{% endhint %}

## Caracteres ignorados en el Buscador Rápido

Se han configurado otros caracteres específicos para que sean ignorados al realizar búsquedas en el Buscador Rápido, por ejemplo, "\*", "?", "@", etc. Esto significa, por ejemplo, que cuando se busque customer.com en el Buscador Rápido, se buscarán las palabras "customer" y “com”. Por ello, se recomienda colocar estas combinaciones de palabras entre comillas para buscarlas como una frase específica - por ejemplo, buscar "customer.com" probablemente le arrojará los resultados que está buscando.

A continuación, encontrará una lista completa de todos los caracteres que las búsquedas ignoran en el Buscador Rápido:

{% file src="<https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2F5ViU4yoPZ0i8edtSda7M%2FCharacters%20ignored%20in%20Quickfind.pdf?alt=media&token=706cd331-a5ab-4145-a34e-abb25de0085a>" %}
