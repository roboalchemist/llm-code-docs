# Source: https://docs.enate.net/enate-help/espanol/procesando-una-accion/accion-esperando-a-que-se-completen-los-sub-casos.md

# Acciones de “Esperar a que se completen los Sub-casos”

Una Acción de “Esperar a que se completen los Sub-casos” esperará a que un Sub-caso específico se complete antes de permitir que el Caso pase a la siguiente Acción.

Podrá darse cuenta de que una Acción es una Acción de "Esperar a que los Sub-casos se completen" porque se indicará "La Acción está esperando a que el Sub-caso se complete" en la tarjeta de información de la Acción.

Una vez que una Acción de "Esperar a que se completen los Sub-casos" ha sido lanzada Y el Sub-caso que ha sido configurado para esperar ha sido lanzado (ya sea manualmente o a través de una Acción "Iniciar Caso"), la Acción "Esperar a que se completen los Sub-casos" pasará a un estado de "En espera".

Una vez que se complete el Sub-caso, la Acción de “Esperar a que se completen los Sub-casos” se cerrará automáticamente.

También recibirá una notificación en la cronología.

Si el Sub-caso que la acción "Esperar a que se completen los Sub-casos" está configurada para esperar no está disponible, ya sea porque no se ha lanzado o porque se resolvió antes de que se lanzara la Acción "Esperar a que se completen los Sub-casos", la acción "Esperar a que se completen los Sub-casos" entrará en un estado de "Por hacer" y se asignará a una Lista en la que un usuario la recogerá y decidirá cómo proceder.

Si a continuación intenta establecer la Acción "Esperar a que se complete el Sub-caso" en "En espera", la Acción se cerrará ya que el Sub-caso que está configurado para esperar no se ha lanzado.

Si la Acción no está en estado de "Esperar a que se completen los Sub-casos' y el Sub-caso por el que está esperando se ha completado, aparecerá un mensaje de "El Sub-caso se ha completado" en la tarjeta de información.

Si usted resuelve manualmente una Acción de “Esperar a que el Sub-caso se complete”, la Acción se marcará como Resuelta sin que el Sub-caso se haya completado.

{% hint style="info" %}
Tenga en cuenta que si su sistema se ha configurado para cerrar automáticamente una Acción de "Esperar a que se complete el Sub-caso" (véase aquí para más información sobre cómo hacerlo) y el Sub-caso que la Acción "Esperar a que se complete el Sub-caso" está configurada para esperar no está disponible - ya sea porque no ha sido lanzado o porque fue resuelto antes de que la Acción "Esperar a que se complete el Sub-caso" fuera lanzada, la Acción de "Esperar a que se complete el Sub-caso" pasará automáticamente a un estado de Cerrado. Recibirá una notificación en la cronología.
{% endhint %}
