# Source: https://docs.enate.net/enate-help/francais/traitement-dun-cas-1/specificites-de-lecran-des-cas.md

# L’écran des cas

L’écran des cas a la même présentation générale que l’écran des [Ticket](https://docs.enate.net/enate-help/francais/traitement-dun-ticket-1/lecran-des-tickets) et l’écran des [Action](https://docs.enate.net/enate-help/francais/traitement-dune-action-1/specificites-de-lecran-des-actions), et les mêmes fonctionnalités de base, notamment [ajouter une note](https://docs.enate.net/enate-help/francais/les-differents-types-decran-des-activites/ajout-dune-note) à une activité, [envoyer un e-mail](https://docs.enate.net/enate-help/francais/courriels/redaction-de-courriels), visualiser les [fichiers et les liens joints](https://docs.enate.net/enate-help/francais/les-differents-types-decran-des-activites/carte-des-fichiers) et visualiser [les communications/la chronologie](https://docs.enate.net/enate-help/francais/les-differents-types-decran-des-activites/section-chronologie), mais il contient également des fonctionnalités spécifiques aux cas.

## Titre du cas

En haut de l’écran des cas, vous pouvez voir le contexte du cas, composé du :

Nom du client - Nom du contrat - Nom du service - Nom du processus du cas

Par exemple :

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FjV6ETWMGPBqgMLi7tZhR%2Fimage.png?alt=media\&token=4b3e7f46-1e82-419e-84fb-3ad26413130a)

La description courte du cas est affichée sur le côté droit de l’écran. Si l’option « [Autoriser la modification du titre](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/info-section/case-info-section) » a été sélectionnée dans l’onglet "Infos sur le cas" dans Builder, vous pourrez modifier la description courte du cas.&#x20;

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2F6f4TqOrSEGgXzydGYLpN%2Fimage.png?alt=media\&token=547314f4-1d82-4b9c-9412-d924ba1c9c7e)

Il s’agit du titre qui apparaîtra alors en haut de l’onglet du cas.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2F0nbbcf2Od3XJtOBTkEmG%2Fimage.png?alt=media\&token=c6ac90f4-baf6-4860-8542-297c2efa5e5e)

Il apparaîtra également dans la colonne « Titre » de la grille de la page d’accueil.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FTaxOW1i0hCmjcpSZmwWm%2Fimage.png?alt=media\&token=b89826eb-7da0-4e14-a979-55c4d4ded7ca)

Vous pouvez copier le numéro de référence et le titre du cas en cliquant sur l’icône Copier dans l’onglet :

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FsboJXG75xZBOb2sA16mu%2Fimage.png?alt=media\&token=3f841049-22bb-433e-aaa4-8d4ff4cfe567)

## Consulter les actions d’un cas

L'affichage de l’écran des cas met en évidence les actions en cours. Un onglet supplémentaire existe dans la section Chronologie afin de permettre à l'utilisateur de voir rapidement le statut de ses actions et d'y accéder. C'est l'onglet affiché par défaut dans cette section pour les cas.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FiGTSCa9SZkGjWbYt7MOz%2Fimage.png?alt=media\&token=ef939826-a012-4cb0-a2d8-02097c7d8e05)

Les informations suivantes seront affichées pour toutes les actions entreprises pour ce cas :

* Icône du statut actuel
* Cas parent et numéro de référence de l’action
* Titre de l'action et instructions
* Échéance, bénéficiaire, file d'attente
* Statut sous forme de fichier texte

Les actions seront affichées dans l’ordre suivant :

1. **Statut**, avec les actions dont le statut est Brouillon en premier, suivies des actions dont le statut est À faire, puis En cours, puis En attente, puis Résolu, puis Fermé. Si tous les statuts sont identiques, les actions seront classées par :
2. **Date d’échéance**, avec les actions dont l’échéance est la plus proche en premier. Si toutes les dates d'échéance sont les mêmes, les actions seront classées par :
3. **Temps restant après la mise en pause**, avec l’action pour laquelle il reste le moins de temps après la mise en pause en premier. Si le temps restant après la mise en pause est le même pour toutes les actions, elles seront classées par :
4. **Numéro d'étape**, avec l’action ayant le numéro d’étape le plus bas en premier. Si les numéros d’étape sont tous identiques, les actions seront classées par :
5. **Date/heure de début**, avec l’action ayant la date/heure de début la plus récente en premier. Si la date/heure de début est la même pour toutes les actions, elles seront classées par :
6. **Numéro de référence**

## Sous-cas

Les sous-cas sont créés à partir d’un cas « parent » existant qui conserve un lien avec leur cas « parent ». Ils se comportent selon leur propre configuration spécifique, mais leur cas parent ne pourra pas être terminé tant que tous ses sous-cas ne seront pas terminés.

Vous pouvez créer des sous-cas en cliquant sur « + Activité » près de la section des onglets d’un cas et en choisissant l’option « Sous-cas » dans la liste déroulante.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2Fk3mjgeqmKpBwa1mCW0MK%2Fimage.png?alt=media\&token=340814fa-24b4-4916-85e6-f76c6fda3ad0)

L’onglet « Sous-cas » affichera les sous-cas de ce cas.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mj8nUZIHmGMjv5LM6go%2F-Mj8o18I3JZ3nO3hyj0a%2FSub-Cases-Tab.gif?alt=media\&token=bd36ffad-fe23-4381-b5ff-2f74c03a9518)

Cliquez ici pour plus d’informations sur les sous-cas:

{% content-ref url="sous-cas" %}
[sous-cas](https://docs.enate.net/enate-help/francais/traitement-dun-cas-1/sous-cas)
{% endcontent-ref %}

## Consulter une activité liée à un cas

Une autre caractéristique de l’écran des cas est la possibilité de créer un cas ou un ticket à partir du cas afin de créer une relation « liée » entre les activités.

Les activités créées de cette manière conserveront un lien avec le cas ou le ticket d’origine et s’afficheront dans un [onglet « Liens »](https://docs.enate.net/enate-help/francais/travailler-avec-des-activites-liees#creer-un-cas-lie), facilitant ainsi le suivi d’un groupe d’activités liées les unes aux autres.&#x20;

Pour plus d’informations, cliquez ici:

{% content-ref url="../travailler-avec-des-activites-liees" %}
[travailler-avec-des-activites-liees](https://docs.enate.net/enate-help/francais/travailler-avec-des-activites-liees)
{% endcontent-ref %}

## Date d’échéance

La date d’échéance du cas sera affichée, avec un code couleur pour indiquer si le cas est :

Dans les délais :

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FEGVtLxRgAnxytIUd5ION%2Fimage.png?alt=media\&token=9ac95525-666c-467a-94b1-fbfc354535ce)

Dû aujourd’hui :

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FQ0gPxJYERIZpISI1OXOG%2Fimage.png?alt=media\&token=77dceb21-f364-4f41-baef-7d58a61cf8b4)

En retard :

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FxYoDpuDtucrXxNarogOW%2Fimage.png?alt=media\&token=ff436f50-5628-4979-96e3-a4ed6a0cba6e)

### Remplacer la date d’échéance

Si un Cas a été configuré avec l’option de remplacer la date d’échéance dans Builder, vous pourrez remplacer sa date d’échéance en cliquant sur la date d’échéance dans l’en-tête et en changeant la date dans la fenêtre contextuelle.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FvkU8p3fccfI6Tt2m9cGU%2Fimage.png?alt=media\&token=d45af518-bfd3-44e0-86da-cde637ef0ef5)

## Utilisateur affecté

Vous pouvez également voir si le Cas a été affecté ou non, et l’utilisateur auquel il a été affecté.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FnWeJpNw3dO2GUEczoffW%2Fimage.png?alt=media\&token=66be1e26-717b-42b5-b36f-b907aa4a8eb5)

Vous pouvez réaffecter et retirer l’affectation à un Cas, ou vous affecter le Cas à vous-même s’il ne vous a pas déjà été affecté.&#x20;

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FiyrOLpkukkGnwlOzHO1H%2Fimage.png?alt=media\&token=814ca26c-cd46-4b62-962f-7bd23b2e15fa)

Pour plus d’informations sur l’affectation des activités dans Enate, cliquez ici:

{% content-ref url="../activites-affecter-reaffecter-retirer-laffectation" %}
[activites-affecter-reaffecter-retirer-laffectation](https://docs.enate.net/enate-help/francais/activites-affecter-reaffecter-retirer-laffectation)
{% endcontent-ref %}

## Panneau latéral

### Consulter le statut d’un cas

Dans la fiche Infos, vous pouvez consulter le statut du cas et le modifier si nécessaire.

L’étiquette principale sur la gauche de la fiche Infos affichera le statut actuel du cas. Le bouton déroulant sur la droite vous permet de choisir les statuts que vous pouvez lui attribuer dans le cadre de son traitement.&#x20;

Pour plus d’informations sur le traitement d’un cas, cluez ici:

{% content-ref url="traitement-dun-cas" %}
[traitement-dun-cas](https://docs.enate.net/enate-help/francais/traitement-dun-cas-1/traitement-dun-cas)
{% endcontent-ref %}

{% hint style="info" %}
**Après avoir sélectionné le nouveau statut dans la liste déroulante et rempli toutes les autres informations requises, cliquez sur le bouton pour confirmer.**
{% endhint %}

Le cadre de la fiche Infos apparaît dans une couleur correspondant au statut actuel du cas et, quand vous aurez cliqué sur le bouton pour changer son statut, le système traitera les changements, et la couleur du cadre ainsi que le nouveau statut changeront pour confirmer que la modification du statut a eu lieu.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FWBg8Rzm6VaewRagjHPBb%2Fimage.png?alt=media\&token=60909289-2e0d-4be8-b385-1f87a48faaef)

Quand vous modifiez le statut d’une activité, si vous lui donnez le statut « En cours », l’onglet de l’activité restera ouvert après confirmation du nouveau statut. Si vous le faites passer à un autre statut, par exemple « En attente » ou « Refusé », l’onglet se fermera automatiquement. Une étiquette sous le statut vous en informera à l’avance.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2F3hPb52EJZ9ROdJLxxwl8%2Fimage.png?alt=media\&token=e08e55c1-747e-4d33-9f4f-160eec42d31c)

En plus de montrer le statut du Cas, les informations suivantes sont affichées directement en dessous :

* Défini par : l’utilisateur qui a défini le statut
* Motif : le motif de la modification du statut, c’est-à-dire la raison pour laquelle il a été modifié (manuellement ou dans le cadre d’un processus).
* Date : date à laquelle le statut a été modifié
* Dernière mise à jour par : l’utilisateur qui a modifié en dernier lieu certaines données du Cas.
* Dernière mise à jour le : date à laquelle certaines données ont été modifiées pour la dernière fois dans le Cas.

{% hint style="info" %}
Attention, toutes les informations ci-dessus ne seront pas toujours visibles. Les informations affichées dépendent du statut du cas et de la façon dont il a été configuré dans Builder.
{% endhint %}

### Consulter les paramètres d’un cas

La fiche Paramètres vous permet de consulter des informations détaillées sur le cas, notamment :

* Le contexte du Cas (Client>Contrat>Service>Processus du cas).
* Quand, comment et qui a créé le cas
* Si ce cas a été créé à partir d’une autre activité, la date de la demande initiale indique la date à laquelle la demande initiale a été introduite, ce qui vous permet de connaître la durée totale de l’exécution d’une demande.
* Maintenir avec moi : l’option de maintenir le cas avec l’utilisateur actuel.
* Maintenir l’Action avec moi : option permettant de maintenir les actions pour le cas avec l’utilisateur actuel.&#x20;
* Envoyer des e-mails automatisés : option permettant d’envoyer des e-mails automatisés pour le cas. Pour l'instant, le seul e-mail automatisé que vous pouvez envoyer pour des Cas est un accusé de réception de création de cas.&#x20;
* Nombre d'enregistrements : selon la configuration du cas dans Builder, le nombre d’enregistrements peut ou non être affiché ici. S’il l'est, le nombre d'enregistrements peut être modifié.

### Contacts du cas

La [fiche Contacts](https://docs.enate.net/enate-help/francais/contacts/carte-des-contacts) est l’endroit où vous pouvez spécifier les personnes qui sont en relation avec le cas.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2F5jowSxLfoXJhHSmLAJhN%2Fimage.png?alt=media\&token=e46ee689-7ef1-439e-bfeb-13610d9d884d)

Par défaut, les relations disponibles sont les suivantes :

* Contact principal : la personne principale avec laquelle vous traitez pour ce Cas. Cette relation peut être obligatoire ou non pour les Cas, selon leur configuration dans Builder.
* Demandeur : la personne qui a fait la demande initiale. Cette relation peut être obligatoire ou non pour les Cas, selon leur configuration dans Builder.
* Sujet : la personne sur laquelle porte le Cas

Très souvent, ces trois relations seront la même personne.

* Cc : tout autre contact qui peut être copié sur toute communication. Lorsqu’un contact est uniquement marqué comme « Cc », il est affiché dans la section Cc séparée ( masquée jusqu’à ce que des contacts uniquement Cc soient marqués sur l’activité).

{% hint style="info" %}
Remarque : il est possible d’ajouter d’autres types de relations dans le système. Voir ici pour plus d’informations sur la façon [d’ajouter des balises de contact](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/contact-tags).
{% endhint %}

La fiche Contacts d’un Cas n’est généralement pas remplie automatiquement, vous devez donc ajouter un contact manuellement. Vous pouvez le faire en recherchant un contact dans la [fiche Contacts](https://docs.enate.net/enate-help/francais/contacts/carte-des-contacts).

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZHaVmBb0E56_Q_jYnK%2F-MZHbC4BRt2U6cLKu08V%2FContact-Card-Search-for-Contact.gif?alt=media\&token=599a753b-246e-417c-af72-9df32a26189e)

Si vous recherchez un utilisateur dans la fiche Contacts qui n’existe pas dans le système, vous pouvez créer un nouveau contact en cliquant sur « Créer un contact » et en remplissant ses détails.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZHZHKfCwmT20z_i-95%2F-MZHa09WPZI3WlIY7Ea-%2FContact-Card-Create-Contact.gif?alt=media\&token=bd8d2355-15e2-4760-b594-6db9028823c3)

Si vous avez écrit l’adresse e-mail du contact, le système décodera et remplira automatiquement son nom et son prénom. Une fois que vous aurez rempli toutes les informations et cliqué sur « Créer un contact », le système vous redirigera vers l’activité.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MZHNQAkYnfT4YfYPY7I%2F-MZHZ15Kudy6pBkdjKew%2FContact-Card-Email-Address.gif?alt=media\&token=971fe34f-7a7b-4a1b-a402-d0868d662d26)

Lorsque vous ajoutez manuellement un contact, il est marqué par défaut comme le Contact principal, le Demandeur et le Sujet du Cas. Vous pouvez réaffecter manuellement ces balises à d’autres utilisateurs par la suite.

### Suivi du temps

Pour vous aider à gérer vos opérations par rapport à vos accords de niveau de service, Enate permet aux utilisateurs de suivre le temps nécessaire pour terminer les activités, à la fois sous la forme d’un total global et sous la forme d’une ventilation par les différentes ressources qui ont pu y travailler.

La fiche Suivi du temps dans les activités permet de suivre le temps de chaque session de navigation individuelle lors de laquelle l’activité est traitée.&#x20;

Pour plus d’informations sur le suivi du temps, cliquez ici.

{% content-ref url="../les-differents-types-decran-des-activites/carte-de-suivi-du-temps" %}
[carte-de-suivi-du-temps](https://docs.enate.net/enate-help/francais/les-differents-types-decran-des-activites/carte-de-suivi-du-temps)
{% endcontent-ref %}

### Fiche intelligente

Une Fiche intelligente peut également être configurée pour afficher des données personnalisées.

{% content-ref url="../les-differents-types-decran-des-activites/cartes-intelligentes" %}
[cartes-intelligentes](https://docs.enate.net/enate-help/francais/les-differents-types-decran-des-activites/cartes-intelligentes)
{% endcontent-ref %}

### Fiche Défauts

Si des [catégories de défauts ont été configurées dans la ligne de service pour un Cas dans Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/service-lines-screen#b-creating-defect-categories), une fiche Défauts apparaîtra sur l’écran de ce Cas dans Work Manager qui offre la fonctionnalité d’enregistrer les défauts pour le Cas correspondant, si un problème est survenu durant le processus. Ces fiches peuvent être incluses dans l’interface de gestion/le tableau de bord pour identifier les domaines de l’entreprise qui doivent être examinés.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2F6pghaQwJFXFkWtbAoqAK%2Fimage.png?alt=media\&token=5c3cd939-7e55-4905-a215-4560a75cab6d)

La liste déroulante « Partie en faute » indique qui est responsable de l’apparition de ce défaut. Vous pouvez sélectionner si un agent était en faute, si le centre de service était en faute ou si le client était en faute.

Si un défaut est résolu, l’utilisateur peut ouvrir le Cas spécifique et son défaut, et le marquer comme résolu. Les défauts peuvent être supprimés durant le traitement du Cas.

Si le paramètre « [Restreindre la modification des défauts](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#restrict-defect-modification) » est activé dans la section « Paramètres système » de Builder, la modification des détails de tous les défauts existants sur la fiche sera limitée. Plus précisément : si tout agent de service peut toujours AJOUTER un défaut et le marquer comme résolu, seul l’agent qui a créé un défaut spécifique aura le droit d’apporter des modifications ultérieures à ses détails ou de les supprimer.

## Activités créées à partir de l’écran des Cas

### Retravailler un Cas

Si des problèmes sont survenus durant le traitement d’un Cas, vous pouvez souhaiter le retravailler. Vous pouvez le faire à partir du Cas en sélectionnant l’onglet « Retravailler » dans l’écran du Cas.&#x20;

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FLrEiUJD2Nx0Do3yCPc12%2Fimage.png?alt=media\&token=71f3a874-321c-4ebd-917c-8b49bd411341)

Pour en savoir plus sur le retravail d’un Cas, cliquez ici:

{% content-ref url="retravailler" %}
[retravailler](https://docs.enate.net/enate-help/francais/traitement-dun-cas-1/retravailler)
{% endcontent-ref %}

### Démarrer une Action manuellement

La plupart du temps, les Actions d’un Cas sont démarrées automatiquement (soit par le flux de processus, soit sur la base de planifications). Cependant, si une Action a été configurée pour être démarrée manuellement, vous pouvez le faire à partir du Cas en utilisant la fonction « Démarrer l’Action ».&#x20;

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FPEP3Q7oKDCOyC8iVYRnG%2Fimage.png?alt=media\&token=f1533091-acdf-429d-8c1e-836796323a50)

Pour en savoir plus sur comment démarrer une Action manuellement à partir d’un cas, cliquez ici:

{% content-ref url="lancer-une-action" %}
[lancer-une-action](https://docs.enate.net/enate-help/francais/traitement-dun-cas-1/lancer-une-action)
{% endcontent-ref %}

## Plus d’informations sur l’écran des Cas

### Nouvelles informations reçues

Lorsqu’un nouvel e-mail qui n’a pas encore été lu a été reçu pour un Cas, l’icône Nouvelles informations sera mise en évidence. Cliquer dessus vous permettra de savoir quand le nouvel e-mail a été reçu.

Vous pouvez choisir de marquer les nouvelles informations comme lues, ce qui remettra l’icône Nouvelles informations à son état normal. Vous pouvez également marquer les informations comme non lues en cliquant sur l’option « Marquer comme nouvelles ».

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FZN72axuJAApH6yhIF0ae%2FNew-Information-Icon.gif?alt=media&#x26;token=d1011b2e-44f0-4fda-94cd-4d0ff70321b8" alt=""><figcaption></figcaption></figure>

### Procédure opérationnelle standard

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FuRWw1yyefJycRiKtdUIC%2Fimage.png?alt=media\&token=e9ac7098-1eb1-496e-88af-de0544eed695)

Cette option fournit un lien vers la Procédure opérationnelle standard pour l’activité qui a été définie dans Builder.
