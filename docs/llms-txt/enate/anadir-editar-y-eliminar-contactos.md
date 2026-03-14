# Source: https://docs.enate.net/enate-help/espanol/contactos/anadir-editar-y-eliminar-contactos.md

# Añadir, editar y eliminar contactos

## Añadir contactos

En Enate, los contactos externos se pueden crear de varias maneras.

### 1) Automáticamente desde un correo electrónico entrante

El sistema de Enate puede configurarse para crear automáticamente nuevos registros de contacto externos cuando lleguen correos electrónicos que contengan nuevas direcciones de correo electrónico, si la configuración [“Habilitar creación automática de contactos” está ACTIVADA en Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation).

El sistema completará automáticamente el nombre y el apellido del contacto basándose en el nombre de visualización del correo electrónico. Más detalles sobre esto:

* Si hay un espacio en el nombre de visualización del correo electrónico, todo lo que esté antes del primer espacio se utilizará como nombre del contacto y todo lo que esté después del último espacio se utilizará como su apellido. Por ejemplo, si el nombre de visualización del correo electrónico es “John Smith”, el nombre del contacto se completará automáticamente como “John” y su apellido se completará automáticamente como “Smith”.
* Si hay una coma en el nombre de visualización del correo electrónico, todo lo que esté antes de la primera coma se utilizará como el apellido del contacto y todo lo que esté después de la coma, pero antes del espacio, se utilizará como su nombre. Por ejemplo, si el nombre de visualización del correo electrónico es “Smith, John”, el apellido del contacto se completará automáticamente como “Smith” y su nombre se completará automáticamente como “John”.
* Si el sistema no puede completar automáticamente el nombre y el apellido con seguridad, el contacto se creará automáticamente sin nombre ni apellido y se pedirá al usuario que lo complete él mismo cuando envíe la tarea.

Además, la [empresa establecida](#nombre-de-la-empresa-alcance-del-contacto-externo) para un contacto creado automáticamente dependerá de la  [configuración del alcance del contacto en Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#contact-scope). Si está configurado como “Global”, o “Global y Local”, el contacto creado automáticamente tendrá un alcance global, es decir, no estará vinculado a ninguna empresa específica. Si se establece en “Local”, el contacto creado automáticamente se creará en la empresa en la que exista la tarea relacionada.

### 2) Añadir un contacto individual desde la Página de gestión de contactos

Puede añadir contactos desde la [Página de gestión de contactos](https://docs.enate.net/enate-help/espanol/contactos/pagina-de-gestion-de-contactos) haciendo clic en el icono Crear contacto y completando los detalles del contacto en la ventana emergente resultante.

<figure><img src="https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FrkFqRaXK64tDnNRdrYqG%2FAdding-Contact-from-Contact-Mana.gif?alt=media&#x26;token=fe555400-6f0a-4401-9ea1-99a447fe69f3" alt=""><figcaption></figcaption></figure>

### 3) Importar contactos a la Página de gestión de contactos desde una plantilla de Excel

Puede importar una lista de contactos desde una hoja de cálculo de Excel en la [Página de gestión de contactos](https://docs.enate.net/enate-help/espanol/contactos/pagina-de-gestion-de-contactos). Se proporciona una plantilla que es compatible con todos los idiomas que ofrece Enate.

<figure><img src="https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2F5TmQms8czPPPJ123thJk%2FBulk-Adding-Contacts%20to%20Contact%20Management%20Page.gif?alt=media&#x26;token=7724d803-397a-4010-97f0-c5a5c9960dc0" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Es obligatorio completar la dirección de correo electrónico cuando se importan contactos desde una plantilla de Excel. Si no especifica una empresa, el contacto se establecerá automáticamente como global. Véase aquí para obtener más información sobre el [alcance de la empresa](#nombre-de-la-empresa-alcance-del-contacto-externo).
{% endhint %}

### 4)  Añadir un contacto desde el Buscador rápido

Si está buscando un nuevo contacto que no existe actualmente en el sistema, puede crear un nuevo contacto desde el propio [Buscador rápido](https://docs.enate.net/enate-help/espanol/buscador-rapido). Vaya a la función de búsqueda de personas en el Buscador rápido y haga clic en “añadir un contacto”.

Cuando haga clic en “añadir un contacto”, el sistema decodificará y completará automáticamente el nombre, los apellidos y la dirección de correo electrónico. Una vez que haya completado toda la información y haya hecho clic en crear, accederá a la [Página de actividad](https://docs.enate.net/enate-help/espanol/contactos/la-pagina-de-actividad-de-contacto) del nuevo contacto.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MbH-BYuK4VLPdtNwqfT%2F-MbHBB9sVuyT_nCkaTfK%2FCreating-a-Contact-from-Quickfin.gif?alt=media\&token=fe49d4ff-b5be-4aee-bbd6-b5aeee0ff1f3)

{% hint style="info" %}
Nota: la dirección de correo electrónico del contacto debe ser única en el sistema.
{% endhint %}

### 5) Añadir un contacto desde la Tarjeta de contactos de una tarea

También puede crear un nuevo contacto desde la [Tarjeta de contactos](https://docs.enate.net/enate-help/espanol/contactos/tarjeta-de-contactos) de una tarea. Cuando busca un usuario en la tarjeta de contactos que no existe en el sistema, puede crear un nuevo contacto haciendo clic en la opción “Crear contacto” y completando los detalles de este.

Si ha escrito la dirección de correo electrónico del contacto, el sistema decodificará y completará automáticamente el nombre y el apellido del contacto. Una vez que haya completado toda la información y haya hecho clic en crear contacto, el sistema lo redirigirá de nuevo a la tarea.

<figure><img src="https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FDDaTodFBgWoOvzrS2DeI%2F7-Create-Contact-from-Work-Item.gif?alt=media&#x26;token=38e3e77a-7692-468b-8fab-d269d77bed72" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Tenga en cuenta que, si crea un nuevo contacto en modo de prueba, ese contacto solo estará disponible para ejecutar paquetes de prueba en el sistema.
{% endhint %}

## Creación de contactos automático vs. manual

Puede ver si un contacto externo ha sido creado automáticamente por el sistema o manualmente por un usuario mirando la columna “Creado automáticamente” en la [Página de gestión de contactos](https://docs.enate.net/enate-help/espanol/contactos/pagina-de-gestion-de-contactos).

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FRef4L6RmD8p7bi2uAgya%2Fimage.png?alt=media\&token=592f2bd6-20ef-4458-b58d-32e845c5b73a)

{% hint style="info" %}
Tenga en cuenta que una vez que un contacto creado automáticamente ha sido editado, ya no se mostrará como un contacto creado automáticamente en la columna “Creado automáticamente” de la Página de gestión de contactos.
{% endhint %}

## Nombre de la empresa – Alcance del contacto externo

Dependiendo de cómo se haya configurado en Builder, tendrá varias opciones al asignar una empresa a un contacto externo:

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2Fah0C48BSIEjoF6MAyt1n%2F7-Company-Scope.gif?alt=media\&token=946d5764-56e3-4059-aace-cf5fd78f4559)

* Todas las empresas/Global
  * Si se configura la empresa como tal, el contacto externo puede crear y acceder a las tareas de todas las empresas.
  * También significa que los usuarios del gestor de trabajo pueden buscar otros todos los contactos externos en una tarea.

{% hint style="info" %}
Tenga en cuenta que esta configuración solo está disponible si el Alcance del contacto externo se ha configurado como “Global” o “Global y Local” en Builder. Véase [aquí ](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#external-contact-scoping)para más información.
{% endhint %}

* Una empresa particular (local)
  * Establecer el alcance del contacto a una empresa en particular significa que el contacto externo solo podrá crear y acceder a tareas para esa empresa en particular a la que el contacto externo ha sido asociado.
  * Los usuarios también podrán añadir un contacto a un paquete API solo si el Contacto está en la misma empresa (o está en una empresa paraguas).

{% hint style="info" %}
Tenga en cuenta lo siguiente:

1. Solo es posible cambiar la empresa asociada de un contacto externo de Todas las Empresas/Global a una empresa concreta (local) si el contacto externo no está asociado a tareas de varias empresas diferentes. Puede cambiar esto reasignando el Contacto en una tarea.
2. Para asignar los contactos externos a Global/Todas las empresas, la columna de la empresa en el archivo de carga en masa debe dejarse en blanco para que, por defecto, los contactos se asignen a Global.
3. La empresa que se establezca para un contacto creado automáticamente dependerá de la configuración del alcance del contacto que se haya establecido. Si está configurado como “Global”, o “Global y Local”, el contacto creado automáticamente tendrá un alcance global, es decir, no estará enlazado a ninguna empresa específica. Si se establece en “Local”, el contacto creado automáticamente se creará bajo la empresa en la que exista la tarea relacionada.
   {% endhint %}

### **Impacto del alcance global / local en la vinculación de contactos a una tarea**

{% hint style="warning" %}
Tenga en cuenta que si un contacto externo tiene un alcance Iocal (es decir, está vinculado a una empresa específica), no podrá añadirlo como contacto para una tarea que exista en otra empresa. Esto también se aplica para las cuentas de Agente (que *siempre* deben existir bajo una empresa específica). SOLO las cuentas externas de alcance global tienen la posibilidad de ser vinculadas como contactos a tareas de cualquier Cliente
{% endhint %}

## Editar contactos

Para editar un contacto, vaya a la [Página de gestión de contactos](https://docs.enate.net/enate-help/espanol/contactos/pagina-de-gestion-de-contactos) y haga doble clic en el contacto para que aparezca la ventana emergente de Editar contacto.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FAfWZbdILteM3wNJ5NuFj%2F7%20Bulk-Editing-Contacts-in-Conta.gif?alt=media\&token=4295e7cf-6fcc-4b5f-80ef-bd3305776e89)

También puede editar de forma masiva la empresa, la zona horaria, la ubicación de la oficina, el idioma preferido y la etiqueta predeterminada de sus contactos seleccionando la casilla del contacto. Haga clic en el botón de Editar que aparecerá para mostrar la ventana emergente de Editar de forma masiva. Determine los detalles que desee y pulse Confirmar para guardar los cambios masivos.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FqCX1Dgu9STWs1MuvwuiH%2F7-Editing-a-Conact-in-Contact-Ma.gif?alt=media\&token=224d7f15-d31c-4c34-840f-5d2f6b21091f)

## Eliminar contactos

Para eliminar un contacto, vaya a la [Página de gestión de contactos](https://docs.enate.net/enate-help/espanol/contactos/pagina-de-gestion-de-contactos), haga clic en la casilla del contacto y aparecerá el botón de eliminar. Puede eliminar varios contactos a la vez.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FMFEmPhT9eOqgX6CijHak%2F7-Deleting-Conacts-from-Contact.gif?alt=media\&token=0234c1a0-7552-4161-ba5a-238be3399c3b)
