# Source: https://docs.enate.net/enate-help/espanol/procesando-una-accion/accion-para-inducir-api-externo.md

# Acción para Inducir API Externo

Al igual que otros arquetipos de Acción, las acciones para "Inducir API Externo" se pueden utilizar en los procesos de Caso, y se utilizan para cuando se necesita llamar automáticamente a otro sistema, pasando datos a él y potencialmente consiguiendo que el sistema externo pase datos personalizados actualizados de vuelta a Enate.

Para obtener información sobre cómo conﬁgurar las Acciones para "Inducir API Externo", consulte esta sección de [Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/external-api-action-info-tab).

A veces puede haber un retraso al esperar que el sistema externo responda. Cuando esto ocurre, es decir, cuando la Acción para "Inducir API Externo" está esperando que la información regrese de un sistema externo, la tarjeta de información de la Acción se mostrará en el *Work Manager* como en estado de "En Espera".

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MdHgd4hZr5ftczUZLlW%2F-MdHh8P5k-vTgCwaIMkU%2Fimage.png?alt=media\&token=d8c4e3a9-4d24-4086-980c-d4915b9af99d)

Cuando el sistema externo responda finalmente a Enate con la actualización de los datos, será con un marcador que diga si ha sido exitosa O no:

**Respuesta con cumplimiento exitoso**

Si el sistema responde diciendo que se ha completado con éxito, la Acción pasará automáticamente a un estado de 'Cerrado', con un Método de Resolución de 'Hecho con éxito'.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FvbfhwQDpIAKZWpgQ7AOJ%2Fimage.png?alt=media\&token=a0c3d137-b300-4265-aa8c-e2c4bd37041f)

**Respuesta con cumplimiento no exitoso**

Si el sistema responde diciendo que no ha tenido éxito, la Acción pasa a un estado de "Por hacer", con una razón de "Actualizado por la integración". La API externa también puede responder con información adicional sobre la razón del fracaso. Esta información se mostrará en la Tarjeta de información de la Acción en la sección "Razón rechazada".

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FJZUsL30KtlxjKdqORFEK%2Fimage.png?alt=media\&token=2f841ca5-251e-4bb9-b7ce-eddad3ebbee2)

Si la Acción no tiene éxito porque no se ha completado dentro del tiempo establecido ([conﬁgurado en Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/external-api-action-info-tab)), entonces se moverá a un estado de "Por hacer" con una razón de "Se acabó el tiempo" y se asignará a una Lista / usuario humano basado en las reglas de asignación conﬁguradas.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2Fkpt0DjuHpl6wmv9wSQtj%2Fimage.png?alt=media\&token=493ed986-c145-41d0-bbad-6f6ab5bc3f6b)

Estas Acciones sin éxito se comportarán ahora efectivamente como una Acción manual estándar.

{% hint style="info" %}
Tenga en cuenta que el Propietario del Caso NO será notificado en estas situaciones.
{% endhint %}

### **Reintentos automático**

Si la Acción no puede conectar con el sistema externo, intentará de nuevo de forma automática conectarse al sistema un determinado número de veces, dependiendo de cómo se haya configurado su sistema en Builder ([véase aquí para más información](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#automated-failure-retry-pattern)). También le aparecerá un mensaje de error en la Acción diciéndole:

* cuándo ha ocurrido el error
* cuándo el sistema reintentará establecer la conexión de forma automática
* cuántas veces el sistema automáticamente ha intentado restablecer la conexión de forma automática hasta el momento y,&#x20;
* cuántas veces el sistema intentará establecer una conexión.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FgGeyjS74LNxlN2LtcjQZ%2Fimage.png?alt=media\&token=e2615209-c2c2-4544-87ae-c49cb0ee9e9f)

Usted puede reintentarlo manualmente estableciendo la conexión desde aquí, haciendo clic en el enlace de “Reintentar” en el mensaje de error.

{% hint style="info" %}
Tenga en cuenta que cuando realiza un reintento manual, esto se contará como un reintento y, por lotanto, se incluirá en el número que muestra cuántas veces el sistema ha reintentado "automáticamente" el establecimiento de una conexión.
{% endhint %}

Si la Acción no logra establecer una conexión después de los reintentos automáticos (por ejemplo, si la configuración de reintento se establece en 5 y el sistema no logra establecer una conexión después de 5 reintentos automáticos), pasará a un estado de 'Cerrado' con un método de resolución de 'No se puede completar'.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FWWPXmRT2U0bjoXbBdNMa%2Fimage.png?alt=media\&token=89233d07-1e7d-4256-ba38-31bde2f6b49f)

{% hint style="info" %}
En esta circunstancia de que la Acción no establezca conexión con el sistema externo, esto se elevará al Propietario del Caso, resaltando en la sección de Acción de la pantalla del Caso que esta Acción fue Cerrada - No Hecha con Éxito.
{% endhint %}

Cuando la Acción recibe la información solicitada, se cerrará automáticamente.&#x20;

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FzBlLJQolaaKNfqE0JXBO%2Fimage.png?alt=media\&token=1eda982d-3968-4db0-8977-21b64b7cbee9)

**Ajuste de la configuración de reintentos en el Builder durante / después de que hayan comenzado los reintentos**

&#x20;**S**i la configuración de reintento automático en el Builder se cambia *después* de que el sistema haya reintentado automáticamente el establecimiento de una conexión con un sistema externo, ocurrirá lo siguiente:&#x20;

Si, por ejemplo, la configuración de reintento se estableció originalmente en 5 y el sistema intentó automáticamente establecer una conexión 5 veces, pero falló, la Acción se cambiará al estado ‘Cerrado’ con un mensaje de error que muestra un recuento de reintentos de 5/5.

Si la configuración de reintento aumenta a algo por encima de 5, por ejemplo 7, el mensaje de error    mostrará un recuento de reintentos de 5/7, pero el sistema NO reintentará automáticamente establecer una conexión por sexta y séptima vez, ya que la acción ya está ‘Cerrado’.&#x20;

Sin embargo, si la acción no ha cambiado a un estado de ‘Cerrado’ porque no había alcanzado el número máximo de reintentos automáticos (por ejemplo, solo había intentado establecer una conexión 4 veces de las 5), entonces aumentando la configuración de reintento a 7 significa que la acción volverá a intentar establecer la conexión automáticamente hasta que el recuento llegue a 7.

Por el contrario, si reduce la configuración de reintentos después de que hayan comenzado los reintentos, por ejemplo, está en el reintento 4 de 10 pero luego reduce el máximo a 4, el sistema seguirá mostrando 4 de 10 pero de hecho estará cerrado.
