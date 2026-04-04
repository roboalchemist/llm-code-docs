# Source: https://docs.enate.net/enate-help/espanol/modo-de-prueba.md

# Modo de Prueba

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2ODI0MA==>" %}

## Cambio al Modo de Prueba <a href="#a-cambio-al-modo-de-prueba" id="a-cambio-al-modo-de-prueba"></a>

Si su cuenta de usuario está configurada para permitirle acceder a los datos de prueba, puede cambiar su entorno de *Work Manager* a "*Modo de prueba*". Este enlace está disponible en el menú desplegable del usuario a la derecha de la barra de encabezado.

## Explicación del Modo de Prueba <a href="#b-explicacion-del-modo-de-prueba" id="b-explicacion-del-modo-de-prueba"></a>

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWs9IbXLiOIO_4AlezW%2F-MWs9UvXRgxVZmDdfoiC%2Fimage.png?alt=media\&token=551e6ab5-1c96-451d-880b-f7998fdbef21)

En el modo de prueba, solo verá datos de prueba; lo que le permite crear y ejecutar *Tareas* a través de versiones de prueba de procesos para verificarlos antes de configurarlos en vivo, todo sin afectar los datos de producción en vivo.

Como recordatorio visual, la barra de encabezado se establece en rojo cuando está en modo *Prueba.*

## Definir diferentes gerentes y miembros en listas en el modo de prueba <a href="#c-definir-diferentes-gerentes-y-miembros-en-listas-en-el-modo-de-prueba" id="c-definir-diferentes-gerentes-y-miembros-en-listas-en-el-modo-de-prueba"></a>

El modo de prueba le permite configurar diferentes gerentes para una lista al ejecutarse en modo de prueba vs. El modo en vivo.

Ejemplo: El Gerente 1 tiene acceso al modo en vivo y es responsable de administrar dos Listas, Financiación y Caso maestro.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWs9IbXLiOIO_4AlezW%2F-MWs9gm1OMy6tLbgy9Dy%2Fimage.png?alt=media\&token=bf28b64a-3e8e-4c3d-b9a8-66472c51830b)

En el Modo de prueba, las mismas dos listas pueden ser administradas por otro usuario que tenga permisos de Modo de prueba y Líder de equipo– véase a continuación donde al Gerente 2 se le asigna la responsabilidad de las Listas en el Modo de prueba.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWs9IbXLiOIO_4AlezW%2F-MWs9kGgY1W_t3ul-aLF%2Fimage.png?alt=media\&token=7ec9b6f7-c3c3-4bc3-8eb7-3513f2308dea)

## Cambiar bots entre el Modo en vivo y el Modo prueba <a href="#d-cambiar-bots-entre-el-modo-en-vivo-y-el-modo-prueba" id="d-cambiar-bots-entre-el-modo-en-vivo-y-el-modo-prueba"></a>

Se pueden cambiar bots para que se ejecuten en el modo de prueba o en el modo en vivo. Dos nuevas actividades se han añadido específicamente al repertorio de actividades para UiPath, Automation Anywhere y BluePrism (los APIs estándar ajustados para que puedan nombrarse de forma general) de esta manera:

* Establecer Modo en vivo
* Establecer Modo prueba

Estas Acciones le permiten cambiar un bot entre los estados prueba y en vivo. Una vez que el bot ha cambiado a Modo prueba, las actividades sucesivas que pueda ejecutar el bot (como por ejemplo, ‘Tener más trabajo’ y ‘Crear Ticket/Caso’, etc.) ocurren dentro del contexto del Modo prueba, teniendo y creando solo tareas de prueba. El bot debe Volver al Modo en vivo una vez el proceso se configura para estar en vivo, así asegura de que está creando tareas en vivo.

## Contactos de prueba – Separar contactos de prueba en el sistema <a href="#e-contactos-de-prueba-separar-contactos-de-prueba-en-el-sistema" id="e-contactos-de-prueba-separar-contactos-de-prueba-en-el-sistema"></a>

Enate admite la creación de registros de Contactos separados en el Modo prueba, por ejemplo, cualquier contacto que crees en el Modo prueba solo será accesible a usuarios en el Modo prueba (y contactos creados en el modo en vivo solo estarán disponibles en el modo en vivo). Esto ayuda a asegurar que los correos electrónicos en las pruebas no se envían por error a usuarios de producción y viceversa.
