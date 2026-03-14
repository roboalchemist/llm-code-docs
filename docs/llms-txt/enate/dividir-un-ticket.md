# Source: https://docs.enate.net/enate-help/espanol/procesamiento-de-un-ticket/dividir-un-ticket.md

# Dividir un Ticket

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTgzNw==>" %}

Si un *Ticket* contiene múltiples consultas/preguntas separadas que se manejan mejor por separado, usted puede dividir el *Ticket*. Haga clic en la pestaña *Dividir* de las pestañas *Actividades* para comenzar la división:

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FLesJUW9apCW7Cf2wvVA4%2Fimage.png?alt=media\&token=841df41e-e3f0-4931-aa36-9a6700f14e2f)

La pantalla se dividirá automáticamente en dos *Tickets.* Puede agregar manualmente más divisiones. El título, la descripción y el contexto (*Cliente >> Categoría del Ticket,* etc.) se copian del *Ticket* actual, pero todo se puede modificar antes de que finalice la división del *Ticket.* Puede elegir quedarse con cada Ticket por separado.

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FXiriYzMEcrsXPu24t4Jy%2Fimage.png?alt=media\&token=26562bb7-2836-4db8-bf6d-48f7275b99a7)

Confirme la división del *Ticket* haciendo clic en el botón en la *Tarjeta de información*:

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FUH8o3whQ4jvZhnZL25bX%2Fimage.png?alt=media\&token=87b96756-2217-429c-b1da-30c6ad52d1f6)

Después de dividir, el *Ticket* original se establecerá en "*Esperando- Ticket dividido*" y ya no formara parte de la entrega del servicio (está esencialmente cerrado).

![](https://429105696-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-987003710%2Fuploads%2FTzYZGZH9v6YtAO7lAVlH%2Fimage.png?alt=media\&token=6d04546c-6fc3-438e-a815-c86fab050170)

Una vez que se resuelven los *Tickets* divididos y la ventana de recomendaciones, si tienen una, ha vencido, este *Ticket* original se configurará para completarse por completo.&#x20;

Para fines de SLA, la fecha de inicio del *Ticket* original se copia en cada uno de los *Tickets* resultantes y la hora en la que el *Ticket* original se marcó como Resuelto se calcula como la hora en que se resuelve el último Ticket en el que se ha dividido.

Por ejemplo, si el *Ticket* A se ha dividido en los *Tickets* B y C, y el *Ticket* B se resuelve el "2022-02-02 01:10:00" y el Ticket C se resuelve el "2022-02-03 02:00:00", la hora marcada para cuando el *Ticket* A se resuelva será "2022-02-03 02:00:00".

Puede cancelar la división de un *Ticket* en cualquier momento cerrando de la pestaña *Dividir* (el botón de Acción principal en el *Ticket* deja de ser "Dividir", por lo que puede estar seguro de que no lo está dividiendo).
