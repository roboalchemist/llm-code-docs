# Source: https://docs.enate.net/enate-help/francais/traitement-dun-cas-1/sous-cas.md

# Sous-cas

## Créer un Sous-cas

Un Sous-cas agira selon sa propre configuration spécifique, mais son Cas « parent » ne pourra pas être terminé tant que tous ses Sous-cas ne le seront pas également.

Vous ne pouvez donc créer un Sous-cas qu’à partir d’un cas existant.

Pour créer un nouveau Sous-cas, cliquez sur le lien « + Activité » qui se trouve près des onglets du Cas, puis sélectionnez l’option « Sous-cas » dans le menu déroulant.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FOG8xHYsR8K8XUSIjBDqF%2Fimage.png?alt=media\&token=c9e1cda6-1955-4d47-ac8b-1aef697b79e0)

Dans la fenêtre contextuelle qui s’affiche alors, vous pouvez utiliser des filtres pour rechercher le nouveau type de processus de Sous-Cas que vous souhaitez créer de deux façons :

* en cherchant les itinéraires d’e-mails : vous pouvez spécifier l’adresse à laquelle les utilisateurs envoient normalement des e-mails pour créer des activités. Souvent, une boîte aux lettres de messagerie représente une certaine partie de l’entreprise au sein de laquelle vous souhaitez créer votre nouvelle activité. Nous avons ajouté une nouvelle fonction utile qui vous permet de rechercher par boîte aux lettres de messagerie et de réduire immédiatement les processus de Sous-Cas que vous pouvez choisir. Sélectionner une boîte aux lettres de messagerie filtrera les options de la liste déroulante pour n’afficher que les processus liés à cette boîte aux lettres.
* en sélectionnant un Client, un Contrat, un Service et un processus de Sous-Cas à créer (les valeurs seront choisies par défaut si vous ne disposez que d’une seule option). Attention, le client d'un Sous-Cas sera automatiquement défini comme étant le même que celui de son Cas parent, c’est-à-dire le Cas à partir duquel vous le créez.&#x20;

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2F6rn6enNKdoAPuwJsuHmW%2Fimage.png?alt=media\&token=28ed81cd-e3af-4bbb-937d-95c1ca3d6e26)

{% hint style="info" %}
Attention, les Sous-Cas que vous pouvez créer dépendent des paramètres d’autorisation dans Builder. De plus, vous ne pourrez également que sélectionner un processus de Sous-Cas à partir d’un itinéraire d’e-mails ayant été activé dans Builder ([voir ici pour plus d'informations](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/email-routes-detail)). Vous aurez aussi la possibilité de sélectionner un processus de Sous-Cas en [Mode test](https://docs.enate.net/enate-help/francais/mode-test) si l’itinéraire d’e-mails pour ce processus de Sous-Cas a été configuré pour fonctionner en [Mode test](https://docs.enate.net/enate-help/francais/mode-test).
{% endhint %}

Vous pouvez ensuite modifier les paramètres suivants :

| Remplacer la date d’échéance | Si votre système a été configuré de la sorte ([voir ici pour plus d’informations](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/due-date-flavours)), vous pouvez choisir de remplacer la date d’échéance du nouveau Sous-Cas que vous créez. |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Description                  | Vous pouvez modifier le titre du nouveau Sous-Cas que vous créez                                                                                                                                                                                                                              |
| Calendrier                   | Si votre système a été configuré de la sorte ([voir ici pour plus d’informations](https://docs.enate.net/enate-help/builder/builder-2021.1/schedules-and-frequency-based-triggers/configuring-schedules)), vous devez choisir un calendrier pour le nouveau Sous-Cas que vous créez.          |
| Ajouter des contacts         | Vous pouvez ajouter plusieurs contacts pour le nouveau Sous-Cas et diviser les balises selon vos besoins.                                                                                                                                                                                     |

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2Ft5sQKES2D54CVzWhptVa%2Fimage.png?alt=media\&token=9ac070b0-485f-4082-bde4-c0787ecab121)

{% hint style="info" %}
Les défauts, les fichiers, les liens et les données personnalisées seront automatiquement partagés du Cas parent vers votre nouveau Sous-cas. Les communications du Cas parent, et ses activités liées, c’est-à-dire ses Actions et ses Sous-cas (s’il y en a) seront également partagées avec le nouveau Sous-cas. Les e-mails ne seront toutefois pas partagés, mais vous pourrez facilement les consulter en sélectionnant l'option « [Inclure les activités liées](https://docs.enate.net/enate-help/francais/les-differents-types-decran-des-activites/section-chronologie#filtrer-longlet-chronologie) » dans la chronologie. Les mises à jour des défauts, fichiers, liens, données personnalisées ou communications dans le nouveau Sous-cas seront également effectuées dans le Cas parent.
{% endhint %}

Un lien vers le nouveau Sous-Cas apparaîtra dans [l’onglet Sous-Cas](#onglet-sous-cas) et PAS dans [l’onglet Liens](#consulter-les-activites-liees-longlet-liens).

### **Onglet « Sous-cas »**

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mj8nUZIHmGMjv5LM6go%2F-Mj8o18I3JZ3nO3hyj0a%2FSub-Cases-Tab.gif?alt=media\&token=bd36ffad-fe23-4381-b5ff-2f74c03a9518)

L’onglet « Sous-Cas » affichera les informations suivantes pour tous les Sous-Cas d’un Cas :

* L’icône indiquant le statut actuel
* Le numéro de référence du Sous-Cas et titre du Cas
* Le nombre d’Actions : le nombre d’Actions associées ce Sous-Cas Le responsable : le responsable du Cas *(s’il a été défini)*
* La file d’attente : la file d’attente du Cas *(si elle a été définie)*
* La date d’échéance : la date d’échéance du Cas
* L’icône pour développer le Sous-Cas afin d’afficher ses Actions

#### Logique du numéro de référence du Sous-Cas

Les numéros de référence des Sous-Cas peuvent être ventilés des manières suivantes **:**

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FXyt5xYzu16LtKGXXR9za%2Fimage.png?alt=media\&token=a2608583-4f29-4634-bce6-4c2a8662df6c)
