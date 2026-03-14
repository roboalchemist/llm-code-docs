# Source: https://docs.enate.net/enate-help/espanol/tipos-de-tareas-tickets-casos-and-acciones/tarjeta-de-seguimiento-de-tiempo.md

# Tarjeta de seguimiento de tiempo

## Descripción general

Para ayudarle a gestionar la actividad con respecto a sus SLA, Enate permite a los usuarios hacer un seguimiento del tiempo que tardan las tareas en completarse, ya sea el total general o desglosado por los distintos recursos que pueden haber trabajado en ellas.

La Tarjeta de seguimiento de tiempo en las tareas hace un seguimiento del tiempo de cada sesión individual del navegador en la que se ejecuta la tarea. Se hace un seguimiento de tiempo siempre que una tarea esté abierta en la pantalla, independientemente de si está asignada al usuario o no, e independientemente del estado en el que se encuentre la tarea. El seguimiento de tiempo se ejecuta en una sola tarea a la vez dentro de una sesión de navegador y se ejecutará para una pestaña de tarea cuando obtenga el foco de la pestaña del navegador. Continúa ejecutándose incluso si el navegador está minimizado, si la computadora tiene la pantalla bloqueada, etc.

En el caso de que la tarea A esté abierta (con el temporizador en marcha) y se abra otra pestaña de la tarea B, el temporizador se detendrá en la tarea A y cambiará a la tarea B. Al pasar de una pestaña a otra, el seguimiento de tiempo también cambiará de pestaña.&#x20;

El seguimiento de tiempo se detiene cuando se cierra la pestaña de la tarea y en caso de que el navegador/máquina se desconecte.

&#x20;Véase aquí para obtener más detalles sobre [cuándo se hace el seguimiento o no](#cuando-se-hace-un-seguimiento-de-tiempo-y-cuando-no) de tiempo en la Tarjeta de seguimiento de tiempo.

{% hint style="info" %}
Nota importante: Al hacer clic directamente en un correo electrónico en cualquiera de las pestañas de la vista de correo electrónico, se iniciará el seguimiento de tiempo para esa tarea y se detendrá el seguimiento de tiempo para cualquier otra pestaña de tarea que se haya estado ejecutando inmediatamente antes.
{% endhint %}

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTgwNw==>" %}

La tarjeta muestra la duración de la sesión actual, el tiempo total acumulado de todas las sesiones anteriores, el tiempo inicial estimado como referencia y, en el caso de las Acciones y los Tickets, el valor estimado del esfuerzo que puede ser modificado por el agente de servicio, y que puede resultar útil para la Previsión.

<figure><img src="https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FTMntLETpw74FKy5hWMz4%2Fimage.png?alt=media&#x26;token=c3b45b01-86ad-427c-ad4a-6b2640b2a130" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Nota: Podrá pausar y restablecer el tiempo que se está registrando para la sesión actual, independientemente de si es o no la persona asignada a la tarea.
{% endhint %}

Además, puede editar el tiempo de la sesión actual *y* de las anteriores, independientemente de si es o no la persona asignada a la tarea. Sin embargo, tenga en cuenta que solo los Líderes de equipo pueden editar el tiempo registrado por *otros* miembros de su equipo, mientras que los Miembros del equipo solo pueden editar el tiempo registrado para sus propias sesiones.

## Vista de sesiones registradas previamente

Al desplegar la Tarjeta de seguimiento de tiempo se muestra el tiempo registrado de las sesiones anteriores, así como quién estaba trabajando en la tarea durante esa sesión, cuánto duró la sesión y si el tiempo registrado de la sesión ha sido editado.

<figure><img src="https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FgFA5jZcoChxjQ3F3AHMU%2Fimage.png?alt=media&#x26;token=36eee3c7-920b-4156-9094-7c7b3a30d8bb" alt=""><figcaption></figcaption></figure>

Al hacer clic en el icono de información se puede ver la fecha y la hora en que se registró la sesión y, si la tarea es un Ticket, a qué categoría se asignó durante esa sesión.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FyTlqzKbKkf5kH3WMBFlY%2Fimage.png?alt=media\&token=de6c5595-2679-4ff8-8c29-34dede27ecd3)

## Edición de tiempos registrados

Puede editar el tiempo de las sesiones registradas actuales y anteriores, independientemente de si es o no la persona asignada a la tarea. Sin embargo, tenga en cuenta que solo los Líderes de equipo pueden editar el tiempo registrado por otros miembros de su equipo, mientras que los Miembros del equipo solo pueden editar el tiempo registrado para sus propias sesiones.

Al editar manualmente el tiempo en la tarea actual, se guardará ese tiempo editado **como una nueva fila** en el historial.&#x20;

Podrá ver más información, incluido cuándo se hizo la edición y quién la hizo, cuando abra la tarjeta en modo de pantalla completa.

{% hint style="info" %}
Tenga en cuenta que los valores del seguimiento de tiempo para las tareas realizadas por los robots son de solo lectura.
{% endhint %}

### Vista de tiempos editados

Puede hacer clic en el icono de desplegar para abrir la tarjeta en modo de pantalla completa. Aquí puede ver la duración de la sesión actual, un total combinado de la duración de todas las sesiones anteriores y, para las Acciones y los Tickets, el tiempo previsto necesario para completar la tarea. También podrá ver información más detallada sobre la sesión individual, así como información sobre las ediciones realizadas en el tiempo registrado:

| Usuario                                           | Quién estaba trabajando en la tarea.                                    |
| ------------------------------------------------- | ----------------------------------------------------------------------- |
| <p> </p><p>Tiempo</p>                             | La hora de inicio y fin y la duración total de la sesión registrada.    |
| Fecha                                             | La fecha en la que se registró la sesión.                               |
| Tiempo editado por                                | Quién editó por última vez el tiempo de registro de la sesión.          |
| <p> </p><p>Tiempo editado a</p>                   | A qué se ha editado el tiempo registrado de la sesión.                  |
| <p> </p><p>Fecha editada</p>                      | La fecha en la que se editó la hora registrada de la sesión.            |
| <p> </p><p>Categoría del Ticket (Solo Ticket)</p> | La categoría en la que se encontraba el Ticket cuando se editó la hora. |

## Tiempo previsto

El tiempo previsto para completar la tarea puede configurarse en Builder para las Acciones y los Tickets. Tenga en cuenta que esta información solo se mostrará si:

* Se ha introducido un valor de Esfuerzo estimado para esta Acción / Categoría de Ticket seleccionada en Builder.
* Las opciones "Mostrar seguimiento de tiempo" y "Mostrar el tiempo previsto en el seguimiento de tiempo" están activadas en todo el sistema.

## ¿Cuándo se hace un seguimiento de tiempo y cuándo no?

El tiempo se registra siempre que el usuario tenga la tarea abierta y esté exhibida en pantalla. El tiempo no se registrará cuando la tarjeta de seguimiento de tiempo esté en pausa. Puede encontrar información más detallada sobre si el tiempo se registra o no en una situación hipotética concreta en la siguiente tabla.

| Situación hipotética                                                                                                                                                                     | Qué sucede con el contador en marcha                                                                                                                                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| La tarea está abierta en la pantalla - asignada a mí / no asignada a mí.                                                                                                                 | <p> </p><p>Se hace un seguimiento de tiempo.</p>                                                                                                                                                                                                             |
| <p> </p><p>La pestaña de la tarea está cerrada.</p>                                                                                                                                      | El seguimiento de tiempo se detiene y la sesión de seguimiento de tiempo actual se termina. Cualquier actividad posterior iniciará una nueva sesión de seguimiento de tiempo.                                                                                |
| <p> </p><p>El usuario selecciona una pestaña de tarea diferente.</p>                                                                                                                     | El seguimiento de tiempo para la tarea original se detiene cuando no está abierta en la pantalla, ya que una pestaña de tarea diferente abierta más recientemente se ha abierto.                                                                             |
| El usuario vuelve a seleccionar la pestaña de la tarea original.                                                                                                                         | El seguimiento de tiempo comienza de nuevo como parte de la misma sesión. El seguimiento de tiempo para la otra Tarea (si su pestaña sigue abierta) se detiene.                                                                                              |
| Se redacta un correo electrónico para una tarea en una ventana emergente de correo electrónico mientras la pestaña de la tarea sigue seleccionada en la ventana principal del navegador. | <p> </p><p> </p><p>El seguimiento de tiempo continúa.</p>                                                                                                                                                                                                    |
| El navegador se minimiza, pero la pestaña de la tarea sigue siendo la pestaña de la tarea seleccionada en la ventana del navegador.                                                      | <p> </p><p>El seguimiento de tiempo continúa.</p>                                                                                                                                                                                                            |
| La computadora se bloquea, pero Enate sigue funcionando y la pestaña de la tarea sigue abierta en la pantalla.                                                                           | El seguimiento de tiempo continúa, pero se detendrá cuando finalice la sesión de Enate.                                                                                                                                                                      |
| <p> </p><p>El usuario sale de la sesión de Enate.</p>                                                                                                                                    | El seguimiento de tiempo se detiene y la sesión de seguimiento de tiempo actual se termina. Se iniciará una nueva sesión de seguimiento de tiempo cuando el usuario vuelva a conectarse.                                                                     |
| <p> </p><p> </p><p>El navegador se cierra inesperadamente / la computadora se cierra inesperadamente / se pierde la conexión a Internet.</p>                                             | El sistema Enate tendrá un registro de la hora recientemente recogida (dentro de los últimos 3 minutos) y la sesión de seguimiento de tiempo actual se termina. Una nueva sesión de seguimiento de tiempo se iniciará cuando el usuario vuelva a conectarse. |

## Información adicional sobre el seguimiento de tiempo

El sistema Enate siempre mantendrá un registro del tiempo registrado automáticamente (es decir, no editado manualmente). Se trata de un registro de la cantidad de tiempo que la pestaña de la tarea se mostró directamente en la pantalla. Estos datos no se visualizan, pero se puede acceder a ellos para fines de información gerencial / informes. Tenga en cuenta que el seguimiento de tiempo hace un seguimiento de TODOS los accesos a la tarea, incluso después de que se haya completado. Al editar manualmente el tiempo actual de la tarea, ese tiempo se guardará editado como una nueva fila en el historial. El cuadro de “tiempo en la tarea” mostrará posteriormente el recuento automático del tiempo transcurrido desde que se inició la edición manual del valor mostrado anteriormente.
