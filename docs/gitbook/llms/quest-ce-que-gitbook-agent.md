# Source: https://gitbook.com/docs/documentation/fr/gitbook-agent/quest-ce-que-gitbook-agent.md

# Qu'est-ce que GitBook Agent ?

GitBook Agent est un coéquipier IA qui travaille à vos côtés, vous aidant à garder votre documentation précise, complète et à jour.&#x20;

L’Agent est profondément intégré à GitBook, vous n’avez donc pas besoin d’apprendre de nouveaux flux de travail pour en profiter — il travaille avec vous en utilisant les processus que vous connaissez déjà.

### Que peut faire GitBook Agent ?

GitBook Agent peut :

* **Rédiger des docs à partir d’une invite :** Demandez à l’Agent de mettre à jour une page avec les informations les plus récentes, de remplacer chaque mention d’un nom de produit par un nouveau nom, ou toute autre modification dont vous avez besoin.
* **Imaginer et mettre en œuvre des changements plus importants :** Décrivez ce dont vous avez besoin et l’Agent ouvrira une demande de modification, expliquera ses modifications prévues, répondra à vos retours, puis mettra en œuvre le plan que vous aurez créé ensemble.
* **Comprendre votre guide de style :** Ajoutez votre guide de style dans les paramètres de votre organisation et il l’appliquera toujours lors de la rédaction ou de la relecture du contenu.
* **Suivre des instructions personnalisées au niveau de l’organisation :** Donnez à l’Agent des instructions spécifiques au niveau de l’organisation, comme ajouter des liens de manières spécifiques ou éviter certains types de blocs.
* **Traduire votre documentation :** Choisissez le contenu que vous souhaitez traduire, sélectionnez une langue et l’Agent fera le travail de localisation de vos docs.
* **Invoquer depuis un commentaire :** Ajoutez un commentaire à n’importe quel bloc de votre page, tapez @gitbook et dites à l’Agent ce dont vous avez besoin.
* **Examiner les demandes de modification :** Ajoutez l’Agent en tant que relecteur sur votre demande de modification. Il peut agir comme un linter de documentation, identifiant ou corrigeant les erreurs, suggérant des améliorations et signalant les écarts par rapport au guide de style.

#### Suggestions automatiques de documentation

L’Agent peut également se connecter aux mêmes signaux que votre équipe utilise pour comprendre votre produit et ce dont vos utilisateurs ont besoin : conversations de support, tickets et fils de discussion provenant de vos outils connectés.

Avec ce contexte, l’Agent peut identifier de manière proactive les lacunes, proposer des mises à jour et générer automatiquement des modifications de documentation. Ainsi, vos docs peuvent évoluer avec votre produit et vos utilisateurs obtiennent toujours les bonnes informations au bon moment et au bon endroit.

{% hint style="info" %}

#### Les suggestions automatiques de docs sont en accès anticipé

Rendez-vous dans **Paramètres de l’organisation → GitBook Agent** pour demander l’accès.
{% endhint %}

### Explorez les fonctionnalités de GitBook Agent

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Rédiger avec GitBook Agent</strong></td><td>Créer du contenu à partir d’une invite ou modifier un seul bloc</td><td><a href="write-and-edit-with-ai">write-and-edit-with-ai</a></td></tr><tr><td><strong>Relire avec GitBook Agent</strong></td><td>Demandez à l’Agent de vérifier votre travail pour l’orthographe, la grammaire et le style</td><td><a href="reviser-les-demandes-de-modification-avec-gitbook-agent">reviser-les-demandes-de-modification-avec-gitbook-agent</a></td></tr><tr><td><strong>Traduire votre site de docs</strong></td><td>GitBook Agent peut créer des localisations à mise à jour automatique</td><td><a href="translations">translations</a></td></tr></tbody></table>

### Ajouter un guide de style et des instructions personnalisées

Vous pouvez configurer GitBook Agent en ajoutant le guide de style de votre équipe ou des instructions spécifiques sur la façon dont vous souhaitez qu’il travaille avec votre équipe. L’Agent utilisera ces éléments comme contexte chaque fois qu’il créera ou modifiera du contenu dans votre organisation.

Pour ajouter un guide de style ou des instructions personnalisées, ouvrez vos **Paramètres de l’organisation** puis choisissez le **GitBook Agent** section. Cliquez sur **Paramètres** l’onglet et ajoutez vos instructions dans le champ de saisie de texte.

Vous pouvez accéder rapidement à cet écran en ouvrant la fenêtre de chat GitBook Agent dans une demande de modification, puis en ouvrant le **menu Actions** <picture><source srcset="broken-reference" media="(prefers-color-scheme: dark)"><img src="https://3903131528-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt=""></picture> et en choisissant **Configurer GitBook Agent** <picture><source srcset="broken-reference" media="(prefers-color-scheme: dark)"><img src="https://3903131528-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FwkBqgOPry9HAcW4cxJk0%2Fsettings.svg?alt=media&#x26;token=67bdbb00-ebf3-4a2d-9df8-0c822406f71c" alt=""></picture>.

#### Exemple d’instructions personnalisées

Voici un exemple du type d’instructions personnalisées que vous pourriez ajouter dans les paramètres de GitBook Agent.

<pre data-overflow="wrap"><code><strong>Vous êtes rédacteur technique chez Stripe. Utilisez un langage clair et direct et privilégiez l’exactitude plutôt que l’ornementation. Pour les guides, introduisez toujours le concept par un résumé en une phrase et structurez le contenu en sections bien organisées. Pour les quickstarts, utilisez toujours un pas à pas et gardez chaque étape axée sur l’action et concise.
</strong></code></pre>

### FAQ

<details>

<summary>Comment GitBook Agent utilise-t-il mes données ?</summary>

Nous suivons toujours nos pratiques de protection des données pour garder vos données privées.&#x20;

GitBook Agent n’utilise pas vos données pour entraîner des modèles d’IA. Nous partageons les informations que vous ajoutez à GitBook Agent avec OpenAI dans le seul but de vous fournir les fonctionnalités d’IA de GitBook. Consultez la politique de confidentialité d’OpenAI pour plus d’informations.

</details>

<details>

<summary>Combien coûte GitBook Agent ?</summary>

GitBook Agent est gratuit pour tous les abonnements pendant la bêta.

[Les traductions](https://gitbook.com/docs/documentation/fr/gitbook-agent/translations) sont tarifées séparément en tant qu’option mensuelle. Visitez [la section tarification](https://gitbook.com/docs/documentation/fr/translations#pricing) pour en savoir plus.

</details>
