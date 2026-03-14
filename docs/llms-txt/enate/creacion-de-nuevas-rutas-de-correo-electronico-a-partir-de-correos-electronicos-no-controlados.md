# Source: https://docs.enate.net/enate-help/espanol/correos-electronicos/correos-electronicos-no-controlados/creacion-de-nuevas-rutas-de-correo-electronico-a-partir-de-correos-electronicos-no-controlados.md

# Creación de nuevas rutas de correo electrónico a partir de correos electrónicos no controlados

Como parte del tratamiento de los correos electrónicos no controlados, los usuarios agentes pueden crear enrutamientos de correo electrónico directamente en Work Manager. La creación de estas reglas ayuda a evitar que futuros correos electrónicos equivalentes lleguen como correos electrónicos no controlados, y así garantizar que se cree un Ticket o Caso para ellos. Esto reduce los volúmenes futuros de correos electrónicos no controlados y asegura que se pueda empezar a trabajar en estas tareas más rápidamente. Para que disponga de aún más control, la opción de que los usuarios de Work Manager puedan crear nuevas rutas de correo electrónico se puede habilitar/deshabilitar a través de los roles de usuario en Builder.&#x20;

Una vez que estas reglas se crean en Work Manager, se activan y funcionan al instante. Sin embargo, los usuarios administradores de Builder reciben una notificación de las nuevas reglas de enrutamiento creadas de esta forma, y estas permanecen marcadas para su atención hasta que el administrador las confirma. Los administradores siguen teniendo la posibilidad de ajustar o incluso desactivar dichas reglas después de evaluarlas.

## Concesión de acceso a los usuarios de Work Manager para crear nuevas rutas de correo electrónico

La función de acceso para poder crear nuevas rutas de correo electrónico en Work Manager se controla a través del sistema de roles de usuario de Enate, con una nueva opción que ha sido añadida a la sección de Opciones de visualización de correo electrónico.

{% hint style="info" %}
Nota: Este acceso a "Crear rutas de correo electrónico" estará activado para el rol de miembro de equipo estándar.
{% endhint %}

<figure><img src="https://lh7-us.googleusercontent.com/YSH53s0duzieWEU1OY0OwKa8ozwniUh1uSdKmSOlfWWnFLhv1tpFmOqe9AJAOVqZKaUKkwESL6Ou9xMjsqsOzdLt2cSJa8NzsB1SAuDQWPdnGMLZT3aTKyRuiyf0b_CMsUTJcpLVN8_Lf9F51IZMyw" alt=""><figcaption></figcaption></figure>

## Cómo crear una nueva ruta de correo electrónico en correos electrónicos no controlados

Al tratar un correo electrónico no controlado en la sección de correos electrónicos no controlados de la página Bandeja de entrada de correo electrónico, si elige que el correo electrónico se procese en un Ticket / Caso (haciendo clic en la opción 'Tarea nueva'), se encontrará con la siguiente ventana emergente:

<figure><img src="https://lh7-us.googleusercontent.com/GIKC7X-O9oejd7gqFtJDF6q3C7EpqQc4Iq3Bj4JHtwvzKb8z0c5YpeA0pa2hza10p70S6UPD1QmczORlFolby9m4FBuA281DPYVHOi2S7DtUwHdN1-PIYpyGdnd3G_UKAfgzTfMcdRKpLJTOa13N9A" alt=""><figcaption></figcaption></figure>

Puede buscar por ruta de correo electrónico (que rellenará automáticamente los campos Cliente/Contrato/Servicio/Proceso en función de las sugerencias para la dirección de correo electrónico seleccionada), o puede seleccionarlo manualmente. Al hacer clic en Crear en este punto, se creará el Ticket o Caso específico a partir del correo electrónico de forma normal.

Sin embargo, si *también* desea que lo mismo ocurra automáticamente de forma continua, puede hacer clic en el enlace "Aplicar a otros correos electrónicos" al pie de la ventana emergente antes de pulsar "Crear". Si ha seleccionado esta opción, cuando pulse "Crear" ocurrirán dos cosas:

* Aparecerá un pequeño mensaje de confirmación que le indicará que se ha creado una nueva tarea.
* A continuación, se mostrará otra pantalla emergente para "Crear una nueva regla de enrutamiento de correo electrónico" en la que puede rellenar los detalles restantes de la regla de enrutamiento antes de confirmar su creación.

<figure><img src="https://lh7-us.googleusercontent.com/2fca4wyIepTxFT2goeHii5ec5nC94W2GsmVkhz44YGFm0SDkuYI13w72Z1C0ob1gFKlGkejMN35ImguWbzooMCtrb0fhq7vsJL3TBUjQdgv0t6B7sieHT0brCxXnoqnqD3WEPmeFzAAz1BdpTCD3OA" alt=""><figcaption></figcaption></figure>

Puede decidir si la ruta va a ser del tipo "Para" o "De", es decir,

* "tratar todos los correos electrónicos DE esta dirección de la misma manera"; O
* "tratar todos los correos electrónicos PARA *esta* dirección de la misma manera";&#x20;

y, a continuación, qué dirección de correo electrónico debe utilizarse junto con esta. Enate rellenará automáticamente la dirección de correo electrónico con la dirección de correo electrónico pertinente asociada con el correo electrónico no procesado en el que estaba trabajando.

{% hint style="info" %}
En la sección "Consejos" de esta ventana emergente, hay un enlace que lleva a los usuarios a la página de correos electrónicos no controlados de la ayuda en línea de Enate, por si necesitan más información.
{% endhint %}

## Aplicación de la regla al correo electrónico existente (ejecución retrospectiva)

Además de establecer una regla que se encargará de todos los correos electrónicos futuros que coincidan con este patrón, también puede elegir que la regla se ejecute contra todos o algunos de los correos existentes no controlados que coincidan con esta regla. Si desea que esto suceda, seleccione la opción "Aplicar automáticamente" al pie de esta ventana emergente.

<figure><img src="https://lh7-us.googleusercontent.com/BiRAo9BFgPFSfTgpKthtMwJ56Xar4zCSYWFMpEFDFTEIAT-Onr32APNw3hpGEEMcyJEpxeIy5kbjH5hahcPdT8wUm3CilfbTx15LTFSYWdbfzZAPQkJX0sUjVTG0I8_6TS5ClMJGIw_fae-_hlwvrA" alt=""><figcaption></figcaption></figure>

El sistema le mostrará cuántos de los correos electrónicos no controlados pendientes coinciden con esta regla, es decir, cuántos deberían ser reprocesados.

#### Elección de un rango de tiempo para seleccionar los correos electrónicos no controlados existentes que se reprocesarán

Al seleccionar esta opción, aparecerá un filtro de tiempo que le permitirá seleccionar un subconjunto de estos correos electrónicos existentes para ejecutar la regla (si, por ejemplo, solo desea ejecutar esta regla para correos electrónicos de hasta una semana/mes de antigüedad, etc.).

<figure><img src="https://lh7-us.googleusercontent.com/tZqF4uEnRlOC9S2iz4J6YhvZNRqIMdME6ZnL9nx3sk_6JdvurLvUZ1W0Dw5ykJ1XVcdTcF2bh4A-Sm8bfNIWFnVwamwxJr8XjTxjuEjbg6IMQt0GO8D_6qgiaxuEm0XFXAE-RAhUc8sjzBEa_HmwdQ" alt=""><figcaption></figcaption></figure>

Puede utilizar el control deslizante para establecer diferentes rangos de fechas, incluida la fijación de fechas específicas. A medida que cambie esta configuración, el sistema se actualizará para reflejar el número de correos electrónicos para los que se ejecutaría la regla.

Cuando esté satisfecho con su selección, puede pulsar Crear: la regla se volverá a ejecutar y los correos electrónicos comenzarán a procesarse en el tipo de Caso o Ticket especificado.

{% hint style="info" %}
Nota importante: Una vez que cree una nueva regla de enrutamiento de correo electrónico de esta manera a través de Work Manager, esta se activará instantáneamente y comenzará a ejecutarse contra cualquier correo electrónico entrante posterior.
{% endhint %}

## Visibilidad para el administrador de las nuevas reglas de enrutamiento de correo electrónico en Builder

Si se han creado nuevas rutas de correo electrónico en Correos electrónicos no controlados en Work Manager, los usuarios administradores lo sabrán cuando en Builder observen un punto rojo en la sección de iconos de correo electrónico.

<figure><img src="https://lh7-us.googleusercontent.com/JzQ-wxhd-rutgeaBe2r87kvSebHrAogBd18fON1e1vxxgp4z4NBx_kbBWf41-M6KC16XiT3dg7YgcMWmtjlZlN-IByjz760TwobhUf3llHag2IDjfBQUO1bvKOzG8d6HIBGmh5y3YkOdn1vknCgJhw" alt=""><figcaption></figcaption></figure>

En todas las secciones y pantallas de navegación posteriores, a medida que desciendan a la página Rutas de correo electrónico, verán una señalización continua de las nuevas reglas de enrutamiento que deben conocer.

<figure><img src="https://lh7-us.googleusercontent.com/claxoRJ152NHt3sX1ZNK-NqMRltZ12iO0oCxlghSbt_9JaDcIx08xcI-t2bFv3fLOJVuvFvCAt_hGi-gDoiJx8RN-Wj2uOYHYRZbTfM4oXCP75Etund5pRgZ3dUadYK48Gl9ClomTHoNXSpemy_pBg" alt=""><figcaption></figcaption></figure>

Una vez en la página de Rutas, los usuarios verán un anuncio que les notificará las nuevas rutas de correo electrónico que deben conocer, y la cantidad que hay. Un enlace les permitirá filtrar las rutas para seleccionar solo las nuevas que deben conocer.

<figure><img src="https://lh7-us.googleusercontent.com/CWuEWvh8rkJAQ4qCUzhiojv1IFiUeNP1epRgL5DS6k8s_5gTdSjdQq3ADNrYV0NSPl_DRenONRcCOSwwf2z-7cPrBjj9P9H0koMTXCYE6jlOh5CEVT55eDVXXiyXS8b_Za1v2rNxCToBrjiRbGR15w" alt=""><figcaption></figcaption></figure>

Dentro de la propia tabla de rutas, se les informará a los usuarios de estas nuevas rutas a tener en cuenta.

<figure><img src="https://lh7-us.googleusercontent.com/6muDVueVWUr65zQNDV6qZLlUql3ctVGwVhMEksZRVKN4mLhv0aaS6uSsyjwsJbXTURueN6AXGYbFUmRg6YrPHW8dzXXfCSvBU4sL2_Y8HAFVijtHerFbc1d4moaEH2BW4gYMIDziJmCUTa6ldc4Zfg" alt=""><figcaption></figcaption></figure>

Se recomienda a los usuarios administradores que revisen estas nuevas reglas de enrutamiento (y hablen con el agente que las creó\*) para asegurarse de que están satisfechos con su funcionamiento junto con las demás reglas. Pueden optar por desactivarlas, realizar ajustes e incluso eliminarlas si lo consideran necesario.

Si están satisfechos con la regla, deben desmarcar la opción "Ajustar". Pueden utilizar el enlace "Borrar filtro de revisión" del encabezado para volver a la vista normal.

<figure><img src="https://lh7-us.googleusercontent.com/6_CaXCg8TEcUUZj4iU7QDxjM_C9QTSjSXpXdHfSCQNLdEMj33Mog_Q_s_9zu6bYVQfD9nWz18u2eeQie6w_hMPQvrmPTErVmBhnCmE6MtH6NW27_KXnT5uwoXEhW0k2sxMd2rNtXAcq88r33-lZrIQ" alt=""><figcaption></figcaption></figure>

\*Puede ver quién creó una regla de enrutamiento de correo electrónico desde el icono "Mostrar actividad" en la parte superior de la ventana emergente de detalles de la regla.

<figure><img src="https://lh7-us.googleusercontent.com/ZqEriiyp0WzGNXg-cYVHn9STNlRhjERADA4vu-K0RbaI9DDKDPED1w-oEovI-x_3Fu0oipSAHPZoeP49s3uK9gaalJ9zVlpsWgFaZeAGkve9lo8pL0vuw8dFeK8bSZGzbR2jBaj2kCJHLLBNQhOKWw" alt=""><figcaption></figcaption></figure>

Al hacer clic, se mostrará la pista de auditoría de quién creó y actualizó esta regla.

<figure><img src="https://lh7-us.googleusercontent.com/aBUSNwgSL3iacw40vGsXgrQPOs1VtpWrl2gW8CqAKHdK_5R6H8-_qRyZmUb-7hFt-zaHqhXaj7SmVca3oxlmLjEeAJDhn4nIi19no_sr7GEJ6q2uv_OHIKdkwF5D0eAvXo7prTWfy-Flx9_Y4XaUcg" alt=""><figcaption></figcaption></figure>
