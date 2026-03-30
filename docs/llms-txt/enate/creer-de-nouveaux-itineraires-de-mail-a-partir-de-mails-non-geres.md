# Source: https://docs.enate.net/enate-help/francais/courriels/gestion-des-e-mails-non-geres/creer-de-nouveaux-itineraires-de-mail-a-partir-de-mails-non-geres.md

# Créer de nouveaux itinéraires d’e-mail à partir d’e-mails non gérés

Dans le cadre de la gestion des e-mails non gérés, les agents peuvent créer des règles d’acheminement des e-mails directement dans Work Manager. La création de ces règles permet d’empêcher les futurs e-mails équivalents de se retrouver dans la catégorie des e-mails non gérés, et permet de s’assurer qu’un ticket ou un cas est créé à partir de ces e-mails. Cela permet de réduire les volumes de futurs e-mails non gérés et de s’assurer que le traitement de ces activités peut commencer plus rapidement. Afin d’assurer un certain contrôle, la capacité des utilisateurs de Work Manager à créer de nouveaux itinéraires d’e-mails est une option qui peut être activée/désactivée via les rôles d’utilisateur dans Builder.

Quand ces règles sont créées dans Work Manager, elles sont immédiatement opérationnelles. Les administrateurs de Builder sont toutefois informés de la création de toute nouvelle règle d’acheminement, et ces règles sont mises en évidence jusqu’à ce que l’administrateur en prenne connaissance. Les administrateurs ont toujours la possibilité d’ajuster ou même de désactiver ces règles après les avoir évaluées.

## Permettre aux utilisateurs de Work Manager de créer de nouveaux itinéraires d’e-mails

L’accès à la fonctionnalité permettant de créer de nouveaux itinéraires d’e-mails dans Work Manager est contrôlé par le système de rôles d’utilisateur d’Enate, une nouvelle option ayant été ajoutée à la section Options d’affichage des e-mails.

{% hint style="info" %}
Remarque : l’accès à la fonction « Créer des itinéraires d’e-mails » sera activé pour le rôle de membre de l’équipe standard.
{% endhint %}

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2Fsq1j4AvUSrO7qnXZmraP%2Fimage.png?alt=media&#x26;token=cb27ec54-4e50-42d3-8d50-9d1097d3bea4" alt=""><figcaption></figcaption></figure>

## Comment créer un nouvel itinéraire d’e-mails dans les e-mails non gérés ?

Lorsque vous traitez un e-mail non géré dans la section *E-mails non gérés* de votre boîte de réception, si vous choisissez de convertir l’e-mail en un ticket ou un cas (en cliquant sur « Nouvelle activité »), vous verrez la fenêtre suivante :

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FadTEMpEEArwi8OPi5WXX%2Fimage.png?alt=media&#x26;token=2bcf2777-a2da-4a66-b7be-5ebadfa14cf7" alt=""><figcaption></figcaption></figure>

Vous pouvez effectuer une recherche par itinéraire d’emails (ce qui remplira automatiquement les champs Client/Contrat/Service/Processus sur la base de suggestions pour l’adresse de messagerie sélectionnée), ou saisir ces informations manuellement. À ce stade, cliquer sur Créer vous permettra de créer le ticket ou le cas spécifique à partir de l’e-mail, comme cela est normalement le cas.

Cependant, si vous souhaitez que la même chose se produise automatiquement en permanence, vous pouvez cliquer sur « Appliquer à d’autres e-mails » au bas de la fenêtre contextuelle avant de cliquer sur « Créer ». Si vous sélectionnez cette option, deux choses se produiront lorsque vous cliquerez sur « Créer » :

* Un petit message de confirmation s’affichera pour indiquer qu’une nouvelle activité a été créée.
* La fenêtre contextuelle « Créer une nouvelle règle d’acheminement des e-mails » s’affichera ensuite pour vous permettre de saisir les autres détails de cette règle d’acheminement avant de confirmer sa création.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2Fup2nlIet9gZbs8W8q91a%2Fimage.png?alt=media&#x26;token=55ef7e8f-113b-4274-9de2-5c75568aca33" alt=""><figcaption></figcaption></figure>

Vous pouvez décider si l’itinéraire sera de type « DE » ou « À », c.-à-d. qu’il traitera :

* tous les e-mails provenant DE cette adresse de la même manière, OU
* tous les e-mails envoyés À cette adresse de la même manière

et décider ensuite de l’adresse e-mail à utiliser en conjonction avec celle-ci. Enate remplacera automatiquement l’adresse e-mail par l’adresse e-mail pertinente associée à l’e-mail non traité sur lequel vous travailliez.

{% hint style="info" %}
Dans la section « Conseils » de cette fenêtre contextuelle, un lien renvoie les utilisateurs à la page des e-mails non gérés de l’aide en ligne d’Enate, au cas où ils auraient besoin de plus d’informations.
{% endhint %}

## Appliquer la règle aux e-mails existants (exécution rétroactive)

En plus de définir une règle qui s’appliquera à tous les futurs e-mails correspondant à ce modèle, vous pouvez également choisir d’appliquer la règle à tous les e-mails non gérés existants ou uniquement à ceux qui correspondent à cette règle. Pour ce faire, cliquez sur le bouton « Appliquer automatiquement » au bas de la fenêtre contextuelle.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FeecWnJp4jA6XLuxgEZ2m%2Fimage.png?alt=media&#x26;token=f5b6f439-26a9-47e6-8243-610f996ad2f8" alt=""><figcaption></figcaption></figure>

Le système vous indiquera combien d’e-mails non gérés de votre backlog actuel correspondent à cette règle, c.-à-d. combien d’entre eux seront retraités.

#### Choisir un intervalle de temps pour sélectionner les e-mails non gérés existants à retraiter.

Si vous sélectionnez cette option, un filtre de temps apparaîtra pour vous permettre de sélectionner un sous-ensemble de ces e-mails existants pour lesquels la règle doit être appliquée (si, par exemple, vous ne souhaitez appliquer cette règle qu’aux e-mails de moins d’une semaine ou d’un mois, etc.).

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FWXUYQq4WP4gOs3gR1lSd%2Fimage.png?alt=media&#x26;token=2f7e77a0-d2ac-4a1f-bae7-284ce47048c0" alt=""><figcaption></figcaption></figure>

Vous pouvez utiliser le curseur pour définir différentes plages de dates, et même définir des dates spécifiques. Le système se met à jour au fur et à mesure que vous modifiez ce paramètre afin de vous montrer le nombre d’e-mails pour lesquels la règle doit être appliquée.

Quand vous êtes satisfait de votre sélection, cliquez sur Créer. La règle sera alors exécutée une nouvelle fois et les e-mails commenceront à être traités dans le type de cas ou de ticket que vous avez spécifié.

{% hint style="info" %}
Remarque importante : si vous créez une nouvelle règle d’acheminement des e-mails de cette manière dans Work Manager, elle sera instantanément mise en œuvre et s’appliquera à tous les e-mails entrants ultérieurs.
{% endhint %}

## Visibilité des nouvelles règles d'acheminement des e-mails par les administrateurs dans Builder

Si de nouveaux itinéraires d’e-mails ont été créés dans les e-mails non gérés de Work Manager, les administrateurs en seront informés dans Builder par le biais d’un point rouge sur l’icône d’e-mail.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FTxceneQAKVsv2rbwhj88%2Fimage.png?alt=media&#x26;token=3a9aca22-13ea-49df-ae33-18e47f23b5b5" alt=""><figcaption></figcaption></figure>

Toutes les sections et tous les écrans de navigation à naviguer avant d’arriver sur la page Itinéraires d’e-mails comporteront un signal indiquant que de nouvelles règles d’acheminement ont été créées et doivent être examinées.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FJF7tzW5BMoGFEabwumRZ%2Fimage.png?alt=media&#x26;token=08ba2894-89d1-420d-ac13-878dbf1da98c" alt=""><figcaption></figcaption></figure>

Une fois sur la page Itinéraires, les administrateurs pourront voir une bannière les informant des nouveaux itinéraires d’e-mails à examiner, ainsi que de leur nombre. Un lien leur permettra de filtrer les itinéraires pour ne garder que les nouveaux itinéraires qu’ils doivent examiner.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FCTRjORJ8A9vqW7yeDeOo%2Fimage.png?alt=media&#x26;token=8e67e939-59e6-4c27-b3fe-1b28f2b37e50" alt=""><figcaption></figcaption></figure>

Le tableau des itinéraires contiendra également des messages d’avertissement indiquant la création de nouveaux itinéraires aux administrateurs.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FeY9p721HJXHPHynQdGly%2Fimage.png?alt=media&#x26;token=e3a3fac2-9935-4f3f-92ef-a824be712b90" alt=""><figcaption></figcaption></figure>

Les administrateurs sont encouragés à examiner ces nouvelles règles d’acheminement (et à parler à l’agent qui les a créées\*) pour s’assurer qu’ils sont satisfaits de la façon dont elles fonctionnent en conjonction avec les diverses autres règles. Ils peuvent choisir de les désactiver, d’y apporter des modifications et même de les supprimer s’ils le jugent nécessaire.&#x20;

S’ils sont satisfaits de la règle, ils doivent décocher la case « à ajuster ». Ils peuvent utiliser le lien « Effacer le filtre de révision » dans l’en-tête pour revenir à l’affichage normal.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FQXO93ZNCUkTaNWyMvTZK%2Fimage.png?alt=media&#x26;token=922fc3fd-c099-4cd0-89f4-0e81a00eb0d6" alt=""><figcaption></figcaption></figure>

\*Vous pouvez voir qui a créé une règle d’acheminement des e-mails à partir de l’icône « Afficher l’activité » située en haut de la fenêtre contextuelle contenant les détails de la règle.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FsAF1o5TyrQt8uu48z8eC%2Fimage.png?alt=media&#x26;token=21c402b9-8f26-4735-b5e6-ba9b855e1a33" alt=""><figcaption></figcaption></figure>

Cliquer sur cette icône permet d’afficher la piste d’audit dans laquelle vous pourrez trouver le nom de la personne qui a créé la règle et de ceux qui l’ont mise à jour.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2F62Ya6mNqyNnHtwzUy4SC%2Fimage.png?alt=media&#x26;token=7ee9e1a6-60da-45cf-86fb-d1c900de268f" alt=""><figcaption></figcaption></figure>
