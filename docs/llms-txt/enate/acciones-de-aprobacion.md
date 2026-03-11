# Source: https://docs.enate.net/enate-help/espanol/procesando-una-accion/acciones-de-aprobacion.md

# Acciones de aprobación

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTQ5NDEwNw==>" %}

### ¿Qué son las acciones de aprobación? ¿Cómo funcionan?

A menudo, dentro de los flujos de Casos de los procesos comerciales que se construyen en Enate, hay puntos en los que personas externas (es decir, personas que trabajan **fuera** de Enate, como pueden ser los directores comerciales de su empresa o la empresa del cliente correspondiente) tienen que dar el visto bueno a las actividades antes de que el proceso pueda continuar. Los procesos de nómina son buenos ejemplos de este tipo de procesos, en los que la gerencia del cliente debe aprobar los informes de nómina antes de que el proceso pueda continuar.

La acción de aprobación de Enate se ha creado para dar soporte específico a estos escenarios de solicitud de aprobación de una forma más integrada, para garantizar que este "ciclo de aprobación" se gestione de forma rigurosa y sea visible dentro del flujo de actividades de Enate.

### Cómo funcionan las acciones de aprobación en el tiempo de ejecución

Las solicitudes de aprobación se envían a agentes que trabajan fuera de Enate para que las aprueben o rechacen.&#x20;

Hay algunos tipos diferentes de aprobación que afectan a la forma en que se toma la decisión:

* En una situación hipotética de varios niveles, el correo electrónico de solicitud se envía a cada nuevo nivel tras la aprobación satisfactoria del anterior, hasta un máximo de 3 niveles. Si alguna persona la rechaza, se rechaza la aprobación.
* En una situación hipotética de cualquiera en paralelo, el correo electrónico de solicitud se envía a todos los aprobadores y se adopta la primera decisión.
* En una situación hipotética de todos en paralelo, el correo electrónico de solicitud se envía a todos los aprobadores y TODOS deben aprobarla para que se apruebe la solicitud. Si alguno la rechaza, se rechaza la aprobación.

Si la solicitud es aprobada por todas las partes necesarias, la Acción de aprobación se resuelve con éxito y se cierra automáticamente, por lo que no será necesario que ningún Agente de Work Manager la recoja, aunque la Acción cerrada siempre se puede ver haciendo clic manualmente sobre ella.

### Excepciones - gestionadas por el Agente en Work Manager

Sin embargo, hay un par de situaciones hipotéticas en las que un agente de Work Manager podría necesitar recoger y llevar a cabo cualquier actividad requerida para seguir procesando una Acción de aprobación:

* La aprobación ha sido rechazada.
* No se han determinado automáticamente aprobadores (o no se determinaron los aprobadores suficientes).

### Solicitud de aprobación rechazada

En el caso de que una solicitud de aprobación haya sido **rechazada**, la Acción pasará al estado "Por hacer", por lo que en última instancia deberá ser gestionada por un Agente de Work Manager. Este deberá revisar el motivo del rechazo proporcionado por el aprobador y decidir cómo proceder. Puede:

1. **Actualizar según sea necesario y reenviar la solicitud estableciendo la acción en "Esperar".** Esto enviará automáticamente el correo electrónico de solicitud de aprobación de nuevo\*\* y colocará la Acción en un estado de "Esperar más información", ya que estamos esperando que la información externa (una respuesta de aprobación) se registre de nuevo en el sistema antes de que la actividad pueda continuar.
2. **Marcar la Acción como Imposible de completar**. Esto alertará al propietario del Caso, que entonces tendrá que decidir cómo proceder -quizás rehaciendo el Caso o cerrándolo por completo.
3. **Marcar la Acción como Resuelta.** Esto marcará manualmente la solicitud como aprobada. El Caso pasará a la siguiente Acción.

\*\*Nota: El envío de correos electrónicos de solicitud de aprobación comenzará de nuevo desde el principio, es decir, todos los solicitantes recibirán un nuevo correo. Si hacen clic en cualquiera de los correos electrónicos enviados anteriormente, se encontrarán con un mensaje que les informará de que ESA solicitud de aprobación específica ya no es válida, ya que los detalles de lo que se solicita pueden haber cambiado.

### Aprobadores insuficientes

En el caso de que un agente necesite agregar aprobadores porque uno o más aprobadores requeridos están en blanco (o hacer cambios que provoquen que las solicitudes de aprobación necesiten ser enviadas de nuevo), el Agente tomará la Acción de Aprobación en un estado de Por Hacer. Una vez que haya terminado de realizar los ajustes y/o rellenar los nombres de los Aprobadores que falten, deberá **poner la Acción en estado de Espera**. Una vez hecho esto, se enviará automáticamente el correo electrónico de solicitud de aprobación y la Acción pasará al estado "Esperar más información", ya que está esperando información externa (aprobación) antes de continuar.

Nota: Mientras una Acción de Aprobación está en estado "Por hacer", o "En progreso", las partes externas a las que se les enviaron solicitudes de aprobación por correo NO podrán aprobarlas o rechazarlas. En su lugar, recibirán un mensaje donde se les informará de que la tarea en cuestión se está procesando actualmente. Los Agentes de Work Manager DEBEN volver a mover la Acción a un estado de "Esperar más información" si desean que se reanude la actividad de aprobación.

### Si se agota el tiempo de las solicitudes de aprobación

Otra situación posible es que la Acción de aprobación se cierre automáticamente porque se ha agotado el tiempo de espera por no haberse recibido respuestas suficientes a tiempo. En este caso, la Acción se establecerá automáticamente como Resuelta, y el Caso continuará. Ningún agente de Work Manager necesitará recoger una Acción en esta situación, aunque la Acción cerrada siempre puede ser vista haciendo clic manualmente sobre ella.
