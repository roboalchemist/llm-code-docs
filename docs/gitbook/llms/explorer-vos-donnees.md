# Source: https://gitbook.com/docs/documentation/fr/gitbook-agent/suggestions-automatiques-de-documentation/explorer-vos-donnees.md

# Explorer vos données

Une fois que GitBook Agent commence à ingérer des conversations, il commencera à classer vos données en trois catégories :

1. **Conversations**: Données brutes que l'agent a indexées à partir de vos connecteurs.
2. **Problèmes**: Problèmes individuels qui ont été identifiés au sein d'une conversation.
3. **Sujets**: Groupes de problèmes qui sont liés les uns aux autres autour d'un même sujet.

Les trois sont utilisés par GitBook Agent pour déterminer les types de modifications qui pourraient être nécessaires dans votre documentation afin de l'améliorer. Vous trouverez ci-dessous plus d'informations sur le fonctionnement de chacun.

{% hint style="info" %}
GitBook Agent catégorise les données et propose automatiquement des suggestions proactives pour vos docs. Vous n'avez rien à faire avec ces données — elles sont disponibles pour consultation.
{% endhint %}

### Conversations

Les conversations sont les données brutes envoyées à GitBook Agent depuis vos [connecteurs](https://gitbook.com/docs/documentation/fr/gitbook-agent/suggestions-automatiques-de-documentation/connexion-dune-source). L'Agent les analyse et leur attribue un score d'impact, qui est ajouté aux métadonnées depuis l'ingestion initiale de la conversation.

Les conversations sont ensuite découpées en problèmes, qui sont des axes d'amélioration spécifiques identifiés dans une conversation. Une conversation peut contenir plus d'un problème.

Vous pouvez consulter les conversations en ouvrant **Paramètres de l'organisation** > **GitBook Agent** > **Explorateur de données** et en choisissant l' **Conversations** onglet.

### Problèmes

Les problèmes sont des points de données autonomes qui ont été identifiés au sein d'une conversation. GitBook Agent leur attribue un score d'impact, qui est ajouté aux métadonnées lors de l'ingestion des données.&#x20;

Vous pouvez consulter les problèmes en ouvrant **Paramètres de l'organisation** > **GitBook Agent** > **Explorateur de données** et en choisissant l' **Problèmes** onglet.

Cliquez sur **Inspecter** <picture><source srcset="broken-reference" media="(prefers-color-scheme: dark)"><img src="https://3903131528-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FHBSHfffDzLSBh8vIMDpr%2Finspect.svg?alt=media&#x26;token=66d56df6-aa54-4bd5-985e-83ea0cfed841" alt=""></picture> le bouton sur un problème pour lire un résumé, ainsi que l'analyse que GitBook Agent en fait.

### Sujets

Les sujets sont des groupes de problèmes qui sont liés entre eux. En regroupant les problèmes, GitBook Agent peut créer des demandes de modification utiles et contextuelles pour votre équipe.

L'Agent attribuera à chaque sujet un score d'impact et affichera le nombre de problèmes et de conversations utilisés pour former le sujet. Ils se mettront à jour automatiquement au fur et à mesure que de nouvelles conversations et problèmes seront traités.

Cliquez sur **Inspecter** <picture><source srcset="broken-reference" media="(prefers-color-scheme: dark)"><img src="https://3903131528-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FHBSHfffDzLSBh8vIMDpr%2Finspect.svg?alt=media&#x26;token=66d56df6-aa54-4bd5-985e-83ea0cfed841" alt=""></picture> sur n'importe quel sujet pour voir les problèmes utilisés pour former le sujet, ainsi qu'un journal du raisonnement de GitBook Agent pour traiter ces problèmes et créer le sujet.

Cet écran d'inspection montre également toutes les demandes de modification que GitBook Agent a créées à partir du sujet — prêtes pour [vous et votre équipe à examiner](https://gitbook.com/docs/documentation/fr/collaboration/change-requests/ecran-des-demandes-de-modification).

{% hint style="info" %}

## Désactivation d'un sujet

Si un sujet n'est pas utile, vous pouvez désactiver le sujet depuis son écran d'inspection. Une fois désactivé, le sujet ne sera plus utilisé pour créer des demandes de modification pour votre documentation.
{% endhint %}
