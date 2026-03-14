# Source: https://docs.enate.net/enate-help/francais/contacts/ajouter-modifier-et-supprimer-des-contacts.md

# Ajouter, modifier et supprimer des contacts

## Ajouter un contact

Il existe plusieurs façons de créer de nouveaux contacts externes dans Enate :&#x20;

### 1) Automatiquement à partir d’un e-mail entrant

Le système Enate peut être configuré pour créer automatiquement de nouveaux contacts externes lors de la réception d’e-mails contenant de nouvelles adresses e-mail si [le paramètre « Activer la création automatique de contacts » est activé dans Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#enable-automatic-contact-creation).

Le système remplit automatiquement le prénom et le nom du contact en fonction du nom affiché dans l’e-mail. Plus de détails à ce sujet :&#x20;

* Si le nom affiché dans l’e-mail comporte un espace, tout ce qui précède le premier espace sera utilisé comme prénom du contact et tout ce qui suit le dernier espace sera utilisé comme nom de famille. Par exemple, si le nom affiché dans l’e-mail est « John Smith », le prénom du contact sera automatiquement remplacé par « John » et son nom par « Smith ».
* Si le nom affiché dans l’e-mail comporte une virgule, tout ce qui se trouve avant la première virgule sera utilisé comme nom de famille du contact et tout ce qui se trouve après la virgule, mais avant l’espace, sera utilisé comme prénom. Par exemple, si le nom affiché dans l’e-mail est « Smith, John », le nom de famille du contact sera automatiquement remplacé par « Smith » et son prénom par « John ».
* Si le système ne peut pas remplir automatiquement le prénom et le nom en toute confiance, le contact sera créé automatiquement sans prénom et sans nom et l’utilisateur sera invité à les remplir lui-même lorsqu’il soumettra l’activité.

En outre, [l’entreprise associée](#impact-du-champ-dapplication-monde-local-sur-la-creation-de-liens-entre-des-contacts-et-une-activite) à un contact créé automatiquement dépend du [paramètre de portée du contact dans Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#contact-scope). S’il est réglé sur « Monde », ou « Monde et local », le contact créé automatiquement aura une portée globale, c’est-à-dire qu’il ne sera pas lié à une entreprise spécifique. S’il est réglé sur « Local », le contact créé automatiquement sera créé dans l’entreprise dans laquelle l’activité liée existe.

### 2) Ajouter un contact individuel à partir de la page Gestion des contacts

Vous pouvez ajouter des contacts à partir de la [page Gestion des contacts](https://docs.enate.net/enate-help/francais/contacts/page-de-gestion-des-contacts) en cliquant sur Créer un contact et en remplissant les détails du contact dans la fenêtre contextuelle qui s’affiche.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FBtoLLI5OqeSxB9finWcg%2F7%20Adding-Contact-from-Contact-Mana.gif?alt=media\&token=e1432490-09c5-407f-ac20-77d867d19169)

### 3) Importer des contacts dans la page Gestion des contacts à partir d’un modèle Excel

Vous pouvez importer une liste de contacts depuis une feuille de calcul Excel dans la [page Gestion des contacts](https://docs.enate.net/enate-help/francais/contacts/page-de-gestion-des-contacts). Un modèle est fourni et le modèle est pris en charge dans toutes les langues proposées par Enate.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2F3l3GUpoAM4FR31FbG7Rk%2F11%20Bulk-Adding-Contacts%20\(2\).gif?alt=media\&token=b9d39785-cb0f-4621-b1e8-115afb3a45b6)

{% hint style="info" %}
Il est obligatoire de renseigner l’adresse e-mail lors de l’importation de contacts à partir d’un modèle Excel. Si vous ne spécifiez pas d’entreprise, le contact sera automatiquement défini comme global. Voir ici pour plus d’informations sur la [portée des entreprises](#impact-du-champ-dapplication-monde-local-sur-la-creation-de-liens-entre-des-contacts-et-une-activite).
{% endhint %}

### 4) Ajouter un contact à partir de la Recherche rapide

Si vous recherchez un nouveau contact qui n’existe pas encore dans le système, vous pouvez créer un nouveau contact directement à partir de la [Recherche rapide](https://docs.enate.net/enate-help/francais/quickfind). Accédez à la fonction de recherche de personnes dans la Recherche rapide et cliquez sur « Ajouter un contact ».

Lorsque vous cliquez sur « Ajouter un contact », le système décode et remplit automatiquement le prénom, le nom et l’adresse e-mail du contact. Une fois que vous avez rempli toutes les informations et cliqué sur « créer », vous accédez à [la page d’activité](https://docs.enate.net/enate-help/francais/contacts/la-page-des-activites-de-contact) du nouveau contact.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MXb0zH-DMnI1hDDpqYh%2F-MXbLFVyVHS1XoH7OEUQ%2FAdd-External-Contact-from-Quickf.gif?alt=media\&token=670bf5e6-48a3-4e3f-89d5-69d370bc529c)

{% hint style="info" %}
L’adresse e-mail du contact doit être unique dans le système.
{% endhint %}

### 5) Ajouter un contact à partir de la fiche Contacts d’une activité

Vous pouvez également créer un nouveau contact à partir de la [fiche Contacts](https://docs.enate.net/enate-help/francais/contacts/carte-des-contacts) d’une activité. Lorsque vous recherchez un utilisateur qui n’existe pas dans le système dans la fiche Contacts, vous pouvez créer un nouveau contact en cliquant sur « Créer un contact » et en remplissant ses détails.

Si vous avez écrit l’adresse e-mail du contact, le système décodera et remplira automatiquement son prénom et son nom. Une fois que vous aurez rempli toutes les informations et cliqué sur « Créer un contact », le système vous redirigera vers l’activité.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FM6LbJEsTjaIae1qCQvZA%2F7-Create-Contact-from-Work-Item.gif?alt=media\&token=99c2d8ba-e79b-4ef7-9c84-6180ce184e3b)

{% hint style="info" %}
Attention, si vous créez un nouveau contact en mode test, ce contact ne sera disponible que pour l'exécution de paquets de test dans le système.
{% endhint %}

## Création automatique ou manuelle d’un contact

Vous pouvez voir si un contact externe a été créé automatiquement par le système ou manuellement par un utilisateur en consultant la colonne « Créé automatiquement » de [la page Gestion des contacts](https://docs.enate.net/enate-help/francais/contacts/page-de-gestion-des-contacts).

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2F8vpHMs1Pa6eHP6tGZWVS%2Fimage.png?alt=media&#x26;token=7d101165-6bae-4fcc-92a3-9c6d397e505e" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Attention, une fois qu’un contact créé automatiquement a été modifié, il n’apparaîtra plus dans la colonne « Créé automatiquement » de la page Gestion des contacts.
{% endhint %}

## Nom de la société : champ d’application des contacts externes

Selon la configuration choisie dans Builder, vous aurez diverses options lors de l'affectation d'une entreprise à un contact externe :

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2F1Yq1EDHIQoZmCfaSDHAV%2F7-Company-Scope.gif?alt=media\&token=5ce5b37b-8dbc-4e63-b8b2-0ce233140265)

* Toutes les entreprises/Monde&#x20;
  * Si vous donnez ce paramètre à une entreprise, le contact externe pourra créer et accéder aux activités de toutes les entreprise.
  * Cela signifie également que les utilisateurs de Work Manager seront en mesure de rechercher d’autres contacts externes dans une activité.

{% hint style="info" %}
Veuillez noter que ce paramètre n’est disponible que si le champ d’application du contact externe a été défini sur « Monde » ou « Monde et local » dans Builder. Voir [ici ](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#external-contact-scoping)pour plus d'informations.
{% endhint %}

* Une entreprise spécifique (locale)
  * Définir le champ d’application du contact à une entreprise spécifique signifie que le contact externe ne pourra créer et accéder qu’aux activités de cette entreprise particulière à laquelle le contact   externe a été associé.
  * Les utilisateurs ne pourront également ajouter un contact à un Packet API que si le contact fait partie de la même entreprise (ou d’une organisation parapluie).

{% hint style="info" %}
Remarque :

1. Il n’est possible de changer l’entreprise associée d’un contact externe de Toutes les entreprises/Global à une entreprise particulière (locale) que si le contact externe n’est pas associé à des activités de plusieurs entreprises différentes. Vous pouvez changer cela en réaffectant le contact à une activité.
2. Pour attribuer des contacts externes au champ Global/Toutes les entreprises, la colonne Entreprise du fichier de téléchargement en bloc doit être laissée vide afin que les contacts soient attribués par défaut au champ Global.
3. L’entreprise attribuée à un contact créé automatiquement dépend du paramètre de champ d’application du contact que vous avez défini. S’il est défini sur « Global" ou « Global et Local », le contact créé automatiquement aura un champ d'application global, c'est-à-dire qu’il ne sera pas lié à une entreprise spécifique. S'il est défini sur « Local », le contact créé automatiquement sera créé dans l’entreprise au sein de laquelle l'activité liée existe.
   {% endhint %}

### **Impact du champ d’application Monde/local sur la création de liens entre des contacts et une activité**

{% hint style="warning" %}
Veuillez noter que si un contact externe a un champ d’application local (c'est-à-dire qu'il est lié à une entreprise spécifique), vous ne pouvez pas l'ajouter comme contact pour une activité qui existe dans une autre entreprise. Cela est également vrai pour les comptes d'agents (qui doivent toujours exister au nom d’une entreprise spécifique). SEULS les comptes externes au champ d’application Monde ont la possibilité d'être liés en tant que contacts à des activités de n'importe quel client.
{% endhint %}

## Modifier un contact

Vous pouvez modifier un contact à partir de la [page Gestion des contacts](https://docs.enate.net/enate-help/francais/contacts/page-de-gestion-des-contacts) en double-cliquant  sur le contact pour ouvrir la fenêtre Modifier le contact.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FUEbJPU5pgJgM4jAYR2v5%2F7-Editing-a-Conact-in-Contact-Ma.gif?alt=media\&token=2d2732be-5a04-413a-b7c2-2eaf2a8fc5cb)

Vous pouvez également modifier en bloc l’entreprise, le fuseau horaire, l’emplacement du bureau, la langue par défaut et la balise par défaut de vos contacts en cochant les cases des contacts concernés. Cliquez sur Modifier qui apparaîtra pour ouvrir la fenêtre contextuelle de modification en bloc. Réglez les détails comme vous le souhaitez et cliquez sur Confirmer pour enregistrer les modifications.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FzSzrUh2AoIuMVPKLlIwj%2F7%20Bulk-Editing-Contacts-in-Conta.gif?alt=media\&token=664c938d-1a4d-479b-b03c-27eaeafc18fc)

## Supprimer un contact

Pour supprimer un contact, rendez-vous sur [la page Gestion des contacts](https://docs.enate.net/enate-help/francais/contacts/page-de-gestion-des-contacts), cliquez sur la case à cocher du contact et le bouton Supprimer apparaîtra. Vous pouvez supprimer plusieurs contacts à la fois.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FeFlj3l3TD2YJftVbA4VH%2F7-Deleting-Conacts-from-Contact.gif?alt=media\&token=92483e88-4637-4c6e-b7e6-7a90d4bee3bd)
