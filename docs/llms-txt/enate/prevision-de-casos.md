# Source: https://docs.enate.net/enate-help/espanol/tipos-de-tareas-tickets-casos-and-acciones/prevision-de-casos.md

# Previsión de Casos

## Descripción general

Los usuarios de la versión v2024.1 podrán emplear la función de previsión para ofrecer estimaciones más exactas del esfuerzo requerido para completar las tareas, lo que facilitará una planificación de recursos más eficiente.

A largo plazo, estos datos se pueden recopilar y devolver a los usuarios administradores para ajustar los temporizadores del esfuerzo estimado y proporcionar previsiones más precisas para futuros volúmenes de trabajo.

<figure><img src="https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FnQYA16GNi9Y20jWtULR2%2Fimage.png?alt=media&#x26;token=7f4416db-47dd-403b-958a-01b8840cee57" alt=""><figcaption></figcaption></figure>

### Cómo usar la "Previsión"

Una vez activada la función "Previsión", aparecerá una nueva pestaña llamada "Estimación del esfuerzo" en los Casos en Work Manager.

<figure><img src="https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FZvgW4vp9xwPRpyggnGDh%2Fimage.png?alt=media&#x26;token=9af64b0f-d2e1-4d38-aba4-1117e30f8333" alt=""><figcaption></figcaption></figure>

Aquí verá un resumen del esfuerzo estimado para todo el Caso, un desglose del esfuerzo estimado para las Acciones o los Sub-casos que conforman el Caso, y un desglose del esfuerzo estimado para las Acciones o los Sub-casos que aún no se han creado.

#### Resumen del esfuerzo del Caso

La sección "Resumen del esfuerzo del Caso" le permite al usuario ajustar el tiempo estimado para el Caso y además proporciona otras métricas relevantes para el Caso.

<figure><img src="https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2Fr1QqyNg6vq5LkqjrNnwO%2Fimage.png?alt=media&#x26;token=c5641489-bdfe-476a-8425-1cbfab4ac33f" alt=""><figcaption></figcaption></figure>

* El "Esfuerzo total estimado" para el Caso indica la cantidad total de tiempo que se calcula que llevará completar el Caso. Un usuario puede actualizar esta información con una estimación más exacta si es necesario.
  * Se trata de la suma del esfuerzo "Estimado" de todas las tareas creadas y las Acciones (y Acciones de Sub-caso) que conforman el Caso, y el valor del "Esfuerzo para tarea aún no creada".
  * El campo inicialmente mostrará el valor manual del <mark style="color:blue;">"Esfuerzo inicial estimado por registro"</mark> de Builder (si existe) multiplicado por el <mark style="color:blue;">recuento de registros.</mark>
    * Si se actualiza el "Recuento de registros", el "Esfuerzo estimado" para el Caso que no ha sido actualizado por un usuario de Work Manager se actualizará para reflejar el cambio en el recuento de registros.
  * Una vez que el Caso se encuentre en estado Resuelto o Cerrado, su esfuerzo estimado ya no podrá modificarse.
  * Tenga en cuenta que al aumentar este valor, aumentará la estimación del "Esfuerzo para tarea aún no creada" y viceversa.
* El "Esfuerzo total real" para el Caso muestra la cantidad de tiempo que se ha invertido trabajando en el Esfuerzo para tarea aún no creada del Caso.
  * Se trata de la suma del esfuerzo "Real" para todas las Acciones y los Sub-casos creados que conforman el Caso, tomado de sus respectivos Seguimientos de tiempo.
* El "Esfuerzo total restante" para el Caso muestra el tiempo que se calcula que le queda al Caso.
  * Se trata de la suma del "Esfuerzo total restante" para todas las Acciones y los Sub-casos creados que conforman el Caso Y el tiempo estimado restante para la tarea que aún debe crearse (por lo tanto, puede no ser siempre igual al esfuerzo "Estimado del Caso" menos el esfuerzo "Real del Caso").

La modificación del valor del esfuerzo "Estimado" para un Caso tiene las siguientes consecuencias:

* Actualización automática del <mark style="color:blue;">valor estimado del "Esfuerzo para tarea aún no creada"</mark>. Esto se debe a que el "Esfuerzo estimado" para el Caso es un valor calculado compuesto por la suma del esfuerzo "Estimado" para todas las tareas creadas y las Acciones (y Acciones del Sub-caso) que conforman el Caso, y el valor del "Esfuerzo para tarea aún no creada".
  * Aumentar el esfuerzo "Estimado" para un Caso aumenta el valor del "Esfuerzo para tarea aún no creada" en la misma medida.
  * Disminuir el esfuerzo "Estimado" para un Caso reduce el valor del "Esfuerzo para tarea aún no creada" en la misma medida.

#### Desglose del esfuerzo para tarea creada

La sección "Desglose del esfuerzo para tarea creada" le permite al usuario ajustar el tiempo estimado para las Acciones individuales creadas (y los Sub-casos) que conforman el Caso. También proporciona otras métricas relevantes para cada una de las Acciones creadas (y los Sub-casos) que conforman el Caso.

<figure><img src="https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FxhWzOooyZjOoXdPH9ja0%2Fimage.png?alt=media&#x26;token=0ddd0ec1-0ac9-4121-8c1e-a7d27622a65e" alt=""><figcaption></figcaption></figure>

Tenga en cuenta que una vez que una Acción se encuentre en estado Resuelto o Cerrado, su esfuerzo estimado ya no podrá modificarse.

A medida que se crean Acciones (y Sub-casos), el esfuerzo estimado asociado se deducirá del valor del Esfuerzo estimado de la sección Tarea aún no creada que aparece más abajo.

#### Desglose de las Acciones

Para cada Acción, usted verá lo siguiente:

* Un enlace a cada Acción.
* El esfuerzo "Estimado" muestra el tiempo total estimado que se calcula que llevará completar la Acción. Un usuario puede actualizar esta información con una estimación más exacta si es necesario.
  * El campo inicialmente mostrará el valor manual del <mark style="color:blue;">"Esfuerzo inicial estimado por registro"</mark> de Builder (si existe) multiplicado por el <mark style="color:blue;">recuento de registros.</mark>
    * Si se actualiza el "Recuento de registros", el "Esfuerzo estimado" para cualquier Acción en progreso que no ha sido actualizada por un usuario de Work Manager se actualizará para reflejar el cambio en el recuento de registros.
  * Aumentar este valor reducirá la estimación de "Tarea aún no creada" y viceversa, y por lo tanto, podría afectar el "Esfuerzo total estimado" para el Caso.
  * Tenga en cuenta que una vez que una Acción se encuentre en estado Resuelto o Cerrado, su esfuerzo estimado ya no podrá modificarse.
* El esfuerzo "Real" muestra la cantidad de tiempo que se ha invertido trabajando en esa Acción.
  * El valor se deduce del Seguimiento de tiempo de la Acción.
* El "Restante estimado" muestra el tiempo que se calcula que le queda a la Acción.
  * Se calcula restando el esfuerzo "Real" para la Acción del esfuerzo "Estimado".
* La fecha de vencimiento de la Acción.
  * También verá el valor "Comenzar antes de" si el esfuerzo "Real" es actualmente cero. Este valor muestra cuándo es la fecha límite absoluta en la que puede iniciarse la Acción para que se complete antes de su fecha de vencimiento.
* El estado de la Acción.

La modificación del valor del esfuerzo "Estimado" para una Acción tiene las siguientes consecuencias:

* Actualización automática del valor estimado del "Esfuerzo para tarea aún no creada" para el Caso.
* Posible actualización automática del esfuerzo "Estimado" para todo el Caso.

Detalles:

* Disminuir el esfuerzo "Estimado" para una Acción aumenta el valor del "Esfuerzo para tarea aún no creada" para el Caso en la misma medida (y deja igual el esfuerzo "Estimado" para todo el Caso).
* Aumentar el esfuerzo "Estimado" para una Acción disminuye el valor del "Esfuerzo para tarea aún no creada" para el Caso en la misma medida. Esto puede afectar o no el esfuerzo "Estimado" para el Caso en general.
  * Si el "Esfuerzo estimado" actualizado para una Acción no aumenta lo suficiente como para que el valor del "Esfuerzo para tarea aún no creada" del Caso sea inferior a 0, el esfuerzo "Estimado" del Caso no se verá afectado.
    * Ejemplo: Digamos que el esfuerzo "Estimado" para la Acción 1 es de 2 horas, que el "Esfuerzo para tarea aún no creada" es de 1 hora, y que el "Esfuerzo estimado" para el Caso es de 3 horas. Un usuario decide que la Acción 1 va a tomar 1 hora más, así que actualiza el esfuerzo "Estimado" para la Acción 1 de 2 a 3 horas. El "Esfuerzo para tarea aún no creada" disminuirá de 1 hora a 0, y el esfuerzo "Estimado" para el Caso no cambiará, es decir que permanecerá en 3 horas.
  * Si el "Esfuerzo estimado" actualizado para una Acción aumenta lo suficiente como para que el valor del "Esfuerzo para tarea aún no creada" para el Caso sea inferior a 0, se debería añadir la diferencia al "Esfuerzo estimado" para el Caso en general.
    * Ejemplo: Digamos que un Caso tiene solo una Acción creada para él que se llama Acción 1. El esfuerzo "Estimado" para la Acción 1 es de 2 horas,  el "Esfuerzo estimado para tarea aún no creada" es de 0, y por lo tanto, el esfuerzo "Estimado" para todo el Caso es de 2 horas. Un usuario decide que la Acción 1 va a tomar 1 hora más, así que actualiza el esfuerzo "Estimado" para la Acción 1 de 2 a 3 horas. Dado que el "Esfuerzo para tarea aún no creada" es de 0, el esfuerzo "Estimado" para el Caso en general aumentará 1 hora, y pasará a ser de 2 a 3 horas.
    * Ejemplo 2: Digamos que un Caso tiene solo una Acción creada para él que se llama Acción 1. El esfuerzo "Estimado" para la Acción 1 es de 2 horas,  el "Esfuerzo estimado para tarea aún no creada" es de 1 hora, y por lo tanto, el "Esfuerzo estimado" para todo el Caso es de 3 horas. Un usuario decide que la Acción 1 va a tomar 2 horas más, así que actualiza el esfuerzo "Estimado" para la Acción 1 de 2 a 4 horas, lo que provoca que el "Esfuerzo para tarea aún no creada" disminuya 1 hora, y pase de 1 a 0, (disminuyendo todo lo que pueda). La hora "restante" se añadirá efectivamente al esfuerzo total "Estimado" del Caso, que aumentará 1 hora, y pasará a ser de 3 a 4 horas.

#### Desglose de los Sub-casos

Si se crea un Sub-caso, usted verá lo siguiente:

* Un enlace al Sub-caso si tiene permiso para acceder a él (de lo contrario, solo verá el nombre y el número de referencia del Sub-caso sin ningún enlace).
* Una fila del Sub-caso "total" con la siguiente información:
  * El esfuerzo "Estimado" muestra el tiempo total estimado que se calcula que llevará completar el Sub-caso. Un usuario puede actualizar esta información con una estimación más exacta si es necesario.
    * Se trata de la suma del esfuerzo "Estimado" de todas las Acciones creadas y por crear (y Acciones de Sub-caso) que conforman el Sub-caso.
    * El campo inicialmente mostrará el valor manual del <mark style="color:blue;">"Esfuerzo inicial estimado por registro"</mark> de Builder multiplicado por el <mark style="color:blue;">recuento de registros.</mark>
      * Si se actualiza el "Recuento de registros", el "Esfuerzo estimado" para el Sub-caso que no ha sido actualizado por un usuario de Work Manager se actualizará para reflejar el cambio en el recuento de registros.
    * Una vez que el Sub-caso se encuentre en estado Resuelto o Cerrado, su esfuerzo estimado ya no podrá modificarse.
    * Tenga en cuenta que al aumentar este valor aumentará el "Esfuerzo estimado de tarea aún no creada" para el Sub-caso y viceversa.
  * El esfuerzo "Real" muestra la cantidad de tiempo que se ha invertido trabajando en el Sub-caso.
    * Se trata de la suma del esfuerzo "Real" para todas las Acciones creadas que conforman el Sub-caso, tomada de sus respectivos Seguimientos de tiempo.
* El "Restante estimado" muestra el tiempo que se calcula que le queda al Sub-caso.
  * Se trata de la suma del esfuerzo "Restante estimado" para todas las Acciones creadas que conforman el Sub-caso Y el tiempo estimado restante para la tarea que aún debe crearse para ese Sub-caso (por lo tanto, puede no ser siempre igual al esfuerzo "Estimado del Sub-caso" menos el esfuerzo "Real del Sub-caso").
  * La fecha de vencimiento del Sub-Caso.
  * El estado del Sub-caso.
* Una fila para cada Acción del Sub-caso con la siguiente información:
  * El esfuerzo "Estimado" muestra el tiempo total estimado que se calcula que llevará completar la Acción del Sub-caso. Un usuario puede actualizar esta información con una estimación más exacta si es necesario.
    * El campo inicialmente mostrará el valor manual <mark style="color:blue;">"Esfuerzo inicial estimado por registro"</mark> de Builder multiplicado por el <mark style="color:blue;">recuento de registros.</mark>
      * Si se actualiza el "Recuento de registros", el "Esfuerzo estimado" para cualquier Acción del Sub-caso en progreso que no ha sido actualizada por un usuario de Work Manager se actualizará para reflejar el cambio en el recuento de registros.
    * Aumentar este valor reducirá la estimación de "Tarea aún no creada" del Sub-caso y viceversa, y, por lo tanto, podría afectar el "Esfuerzo total estimado" para el Sub-caso.
    * Una vez que una Acción se encuentre en estado Resuelto o Cerrado, su esfuerzo estimado ya no podrá modificarse.
  * El esfuerzo "Real" muestra la cantidad de tiempo que se ha invertido trabajando en esa Acción del Sub-caso.
    * El valor se deduce del Seguimiento de tiempo de la Acción del Sub-caso.
  * El "Restante estimado" muestra el tiempo que se calcula que le queda a la Acción del Sub-caso.
    * Se calcula restando el esfuerzo "Real" para la Acción del Sub-caso del esfuerzo "Estimado".
  * La fecha de vencimiento de la Acción del Sub-caso.
  * También verá el valor "Comenzar antes de" si el esfuerzo "Real" es actualmente cero. Este valor muestra cuándo es la fecha límite absoluta en la que puede iniciarse la Acción del Sub-caso para que se complete antes de su fecha de vencimiento.
  * El estado de la Acción del Sub-caso.
* Una fila para "Tarea aún no creada" para el Sub-caso con la siguiente información:
  * El esfuerzo "Estimado" muestra el esfuerzo total estimado que se calcula que llevará completar las Acciones del Sub-caso que aún no han sido creadas para ese Sub-caso. Un usuario puede actualizar esta información con una estimación más exacta si es necesario.
    * La modificación de este valor estimado afectará el "Esfuerzo total estimado" del Sub-caso y podría afectar el esfuerzo estimado del Caso en general.

<figure><img src="https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2Fqn06JAW8gzI8iGkXbklP%2Fimage.png?alt=media&#x26;token=d7172dae-9e2c-416f-997c-dc18ec6dd6cc" alt=""><figcaption></figcaption></figure>

La modificación del valor del esfuerzo "Estimado" para una Acción de Sub-caso tiene las siguientes consecuencias:

* Actualización automática del valor estimado del "Esfuerzo para tarea aún no creada" para el Sub-caso.
* Posible actualización automática del esfuerzo "Estimado" para todo el Sub-caso.
* Posible actualización automática del esfuerzo "Estimado" para todo el Caso principal.

Detalles:

* Disminuir el esfuerzo "Estimado" para una Acción de Sub-caso aumenta el valor del "Esfuerzo para tarea aún no creada" para el Sub-caso en la misma medida (y deja igual el esfuerzo "Estimado" para todo el Sub-caso y, por lo tanto, no afecta el esfuerzo "Estimado" para todo el Caso principal).
* Aumentar el esfuerzo "Estimado" para una Acción de Sub-caso reduce el valor del "Esfuerzo para tarea aún no creada" para el Sub-caso en la misma medida. Esto puede afectar o no el esfuerzo "Estimado" para el Caso en general.
  * Si el "Esfuerzo estimado" actualizado para una Acción de Sub-caso no aumenta lo suficiente como para que el valor del "Esfuerzo para tarea aún no creada" del Sub-caso sea inferior a 0, el esfuerzo "Estimado" para el Sub-caso no se verá afectado (y, por lo tanto, el esfuerzo "Estimado" para todo el Caso principal no se verá afectado).
    * Ejemplo: Digamos que un Sub-caso tiene solo una Acción creada para él que se llama Acción del Sub-caso 1. El esfuerzo "Estimado" para la Acción del Sub-caso 1 es de 2 horas,  y el "Esfuerzo estimado para tarea aún no creada" para el Sub-caso es de 1 hora, por lo tanto, el esfuerzo "Estimado" para el Sub-caso es de 3 horas. Un usuario decide que la Acción del Sub-caso 1 va a tomar 1 hora más, así que actualiza el esfuerzo "Estimado" para la Acción del Sub-caso 1 de 2 a 3 horas, lo que provoca que el "Esfuerzo para tarea aún no creada" del Sub-caso disminuya de 1 a 0. El esfuerzo "Estimado" para el Sub-caso no se modificará y quedará en 3 horas (por lo tanto, el esfuerzo "Estimado" para todo el Caso principal no se verá afectado).
  * Si el "Esfuerzo estimado" actualizado para una Acción de Sub-caso aumenta lo suficiente como para que el valor del "Esfuerzo para tarea aún no creada" del Sub-caso sea inferior a 0, la diferencia debería añadirse al "Esfuerzo estimado" del Sub-caso en general (y, por lo tanto, podría afectar el esfuerzo "Estimado" de todo el Caso principal).
    * Ejemplo: Digamos que un Sub-caso tiene solo una Acción creada para él que se llama Acción del Sub-caso 1. El esfuerzo "Estimado" para la Acción del Sub-caso 1 es de 2 horas,  y el "Esfuerzo estimado para tarea aún no creada" para el Sub-caso es de 0; por lo tanto, el esfuerzo "Estimado" para el Sub-caso en general es de 2 horas. Un usuario decide que la Acción del Sub-caso 1 va a tomar 1 hora más, así que actualiza el esfuerzo "Estimado" para la Acción del Sub-caso 1 de 2 a 3 horas. Dado que el "Esfuerzo para tarea aún no creada" para el Sub-caso es de 0, el esfuerzo "Estimado" para el Sub-caso aumentará 1 hora, y pasará a ser de 2 a 3 horas.&#x20;
      * Si hay tiempo suficiente en el "Esfuerzo para tarea aún no creada" del Caso principal, este aumento de 1 hora podría deducirse de ahí, por lo que no habría impacto en el esfuerzo "Estimado" para todo el Caso principal.
      * Si no hay tiempo suficiente en el "Esfuerzo para tarea aún no creada" del Caso principal, este aumento de 1 hora dará lugar a un aumento en el esfuerzo "Estimado" para todo el Caso principal.
    * Ejemplo 2: Digamos que un Sub-caso tiene solo una Acción creada para él que se llama Acción del Sub-caso 1. El esfuerzo "Estimado" para la Acción del Sub-caso 1 es de 2 horas,  y el "Esfuerzo estimado para tarea aún no creada" para el Sub-caso es de 1 hora; por lo tanto, el esfuerzo "Estimado" para el Sub-caso en general es de 3 horas. Un usuario decide que la Acción del Sub-caso 1 va a tomar 2 horas más, así que actualiza el esfuerzo "Estimado" para la Acción del Sub-caso 1 de 2 a 4 horas y hace que el "Esfuerzo para tarea aún no creada" para el Sub-caso disminuya tanto como pueda (aquí disminuirá en 1 hora, y pasará de 1 a 0). La hora "restante" será efectivamente añadida al esfuerzo total "Estimado" para el Sub-caso, que aumentará en 1 hora, y pasará de 3 a 4 horas.
      * Si hay tiempo suficiente en el "Esfuerzo para tarea aún no creada" del Caso principal, este aumento de 1 hora podría deducirse de ahí, por lo que no habría impacto en el esfuerzo "Estimado" para todo el Caso principal.
      * Si no hay tiempo suficiente en el "Esfuerzo para tarea aún no creada" del Caso principal, este aumento de 1 hora dará lugar a un aumento en el esfuerzo "Estimado" para todo el Caso principal.

#### Esfuerzo para tarea aún no creada

La sección "Esfuerzo para tarea aún no creada" muestra el esfuerzo que se calcula que llevará completar las Acciones (y las Acciones de Sub-casos) que aún no han sido creadas para este Caso.

Se calcula restando la suma del esfuerzo "Estimado" para las tareas creadas al esfuerzo "Estimado" para el Caso. Por lo tanto, aumentar el "Esfuerzo para tarea aún no creada" aumentará el esfuerzo estimado para el Caso en general y viceversa.

A medida que se crean Acciones (y Sub-casos), el esfuerzo estimado asociado se deducirá del valor del "Esfuerzo estimado para tarea aún no creada".

Una vez que el Caso se encuentre en estado Resuelto o Cerrado, el "Esfuerzo para tarea aún no creada" ya no podrá modificarse.

<figure><img src="https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FQh0xAbwhft1qD3yEDCHG%2Fimage.png?alt=media&#x26;token=b939bffc-8360-4b51-a02e-6a3ec7707e3c" alt=""><figcaption></figcaption></figure>
