# Source: https://gitbook.com/docs/documentation/fr/collaboration/change-requests/demandes-de-modification-dans-un-espace.md

# Demandes de modification dans un espace

Lorsque vous êtes dans un [espace](https://gitbook.com/docs/documentation/fr/getting-started/concepts#space), vous pouvez apporter des modifications en ouvrant une nouvelle demande de modification, ou parcourir les demandes de modification existantes pour voir sur quoi d'autres personnes travaillent.

### Créer une demande de modification

Dans un espace où les éditions en direct sont désactivées, cliquez sur le **Modifier** bouton dans le [en-tête de l’espace](https://gitbook.com/docs/documentation/fr/ressources/gitbook-ui#space-header) pour démarrer une nouvelle demande de modification.

Cela ouvrira une nouvelle demande de modification, où vous pourrez éditer ou supprimer du contenu selon les besoins. Vos modifications sont enregistrées automatiquement, et d'autres personnes peuvent vous rejoindre dans une demande de modification pour collaborer en temps réel.

Lors de la création d'une demande de modification, vous pouvez ajouter un titre et une description pour fournir plus de contexte sur les modifications que vous apportez.

Une fois que vous êtes satisfait de vos modifications, vous pouvez utiliser le bouton dans la barre d'en-tête pour [**Demander une relecture**](#request-a-review-on-a-change-request) de votre demande de modification, ou [**Fusionner**](#merging-a-change-request) l'intégrer directement dans la branche principale.

#### Créer une demande de modification avec GitBook Agent

[Agent GitBook](https://gitbook.com/docs/documentation/fr/gitbook-agent/quest-ce-que-gitbook-agent) est un coéquipier IA qui peut [planifier et mettre en œuvre des demandes de modification](https://gitbook.com/docs/documentation/fr/gitbook-agent/write-and-edit-with-ai#implement-a-change-request-with-gitbook-agent) en fonction de toutes les instructions que vous lui donnez.

Pour ouvrir une nouvelle demande de modification avec GitBook Agent, cliquez sur l'icône GitBook Agent en haut à droite à côté du bouton « Modifier », et demandez à GitBook d'appliquer les modifications que vous souhaitez.

Voici quelques exemples de choses que vous pouvez lui demander de faire :

* Ajouter des exemples d'utilisation
* Améliorer le référencement de la page
* Améliorer la clarté
* Vérifier la cohérence
* Corriger les fautes de frappe et les erreurs d’orthographe
* Lier le contenu connexe
* \+ plus

Rendez-vous sur [Rédiger avec GitBook Agent](https://gitbook.com/docs/documentation/fr/gitbook-agent/write-and-edit-with-ai) pour en savoir plus.

### Aperçu d'une demande de modification

Vous pouvez prévisualiser les modifications que vous avez apportées dans une demande de modification en cliquant sur l'option **Aperçu** dans le [en-tête de l’espace](https://gitbook.com/docs/documentation/fr/ressources/gitbook-ui#space-header). Cela basculera vers un aperçu de vos documents publiés avec les modifications proposées incluses, afin que vous puissiez voir vos changements dans le contexte complet de votre documentation publiée.

Sous le **Aperçu** bouton se trouve une URL pour l'aperçu de votre site. Cliquez dessus et l'aperçu de votre site s'ouvrira complètement dans un nouvel onglet.&#x20;

Lorsque vous ouvrez une URL d'aperçu dans un nouvel onglet, vous verrez également [la barre d'outils Aperçu](https://gitbook.com/docs/documentation/fr/ressources/gitbook-ui/toolbar-on-published-sites-and-site-previews) en bas de la fenêtre du navigateur. Cette barre d'outils vous permet de revenir rapidement dans GitBook pour afficher, modifier ou commenter la demande de modification, ou ouvrir la version en direct de votre site.

{% hint style="info" %}
Vous ne pouvez prévisualiser les demandes de modification que pour les espaces ajoutés à un [site de documentation publié](https://gitbook.com/docs/documentation/fr/publishing-documentation/publish-a-docs-site).
{% endhint %}

{% hint style="warning" %}
Si votre contenu est publié en utilisant des liens de partage ou un accès authentifié, la fonction d'aperçu n'apparaîtra pas.
{% endhint %}

### Demander une révision d'une demande de modification

Demandez une révision de votre demande de modification lorsque vous souhaitez demander aux membres de votre équipe de vérifier votre contenu avant de fusionner les modifications dans la branche principale.

Sélectionnez l'onglet **Aperçu** dans la barre d'en-tête de l'espace pour ouvrir un aperçu de votre demande de modification — y compris toutes les modifications que vous avez apportées en vue des différences.

Ici, vous pouvez ajouter une description à votre demande de modification pour donner à vos réviseurs un peu de contexte, et taguer des personnes spécifiques que vous souhaitez voir vérifier votre travail.

Lorsque vous cliquez sur **Demander une relecture**, le statut de la demande de modification changera en **En cours de révision**, et toute personne que vous avez taguée dans votre demande de révision recevra une notification.

Si vos modifications ne nécessitent pas de révision, si vous avez le [autorisations](https://gitbook.com/docs/documentation/fr/gestion-du-compte/member-management/roles)approprié, et si vous n'avez aucune [règle de fusion](https://gitbook.com/docs/documentation/fr/collaboration/merge-rules)bloquante, vous pouvez fusionner vos modifications directement dans la version principale à la place.

{% hint style="info" %}
[Ajouter GitBook Agent en tant que réviseur](https://gitbook.com/docs/documentation/fr/gitbook-agent/reviser-les-demandes-de-modification-avec-gitbook-agent) à votre demande de modification et il peut vérifier votre contenu pour les fautes d'orthographe, de grammaire et de style, suggérer des améliorations et bien plus.&#x20;
{% endhint %}

{% hint style="warning" %}
Si vous ne taguez personne dans votre demande de révision, tous ceux qui ont des autorisations de réviseur recevront une notification concernant votre demande. Si aucun réviseur n'est présent dans l'espace, le rôle supérieur au réviseur sera notifié.
{% endhint %}

#### Vue des différences <a href="#diff-mode" id="diff-mode"></a>

Lorsque vous ouvrez l'onglet **Modifications** dans l'en-tête de l'espace, la vue des différences apparaîtra. La vue des différences met en évidence chaque page et bloc qui a été modifié dans une demande de modification. Elle mettra en évidence toutes les pages modifiées dans la table des matières, et sur les pages elle montrera les blocs spécifiques qui ont été ajoutés, modifiés ou supprimés.

Il y a deux options lors de l'utilisation de la vue des différences :

1. **Afficher toutes les pages** – Il s'agit du mode par défaut pour la vue des différences, qui affichera à la fois les pages modifiées et non modifiées dans la table des matières. C'est utile pour voir quelles pages ont été modifiées dans le contexte de l'ensemble de l'espace.
2. **Afficher uniquement les pages modifiées** – Ce mode affichera uniquement les pages modifiées dans la table des matières, ce qui vous aide à vous concentrer sur le contenu modifié. Ceci est particulièrement utile dans les grands espaces comportant de nombreuses pages et sous-pages.

Vous pouvez basculer vers l'onglet **Modifications** pour vérifier la vue des différences dans n'importe quelle demande de modification.

### Fusionner une demande de modification

La fusion d'une demande de modification ajoutera les modifications de la demande de modification dans la branche principale du contenu, créant une version mise à jour et une nouvelle entrée dans [l'historique des versions](https://gitbook.com/docs/documentation/fr/creating-content/version-control#see-the-activity-of-a-specific-draft).

Vous pourriez ne pas être en mesure de fusionner une demande de modification si vous n'avez pas le [autorisations](https://gitbook.com/docs/documentation/fr/gestion-du-compte/member-management/permissions-and-inheritance)approprié, ou si votre demande de modification n'a pas passé les [règle de fusion](https://gitbook.com/docs/documentation/fr/collaboration/merge-rules).

### de votre organisation ou de votre espace.

Résolution des conflits de fusion

Parfois, lorsque vous souhaitez fusionner une demande de modification, vous pouvez découvrir des conflits entre le contenu principal et le contenu que vous essayez de fusionner. Dans sa forme la plus simple, un conflit est un élément de contenu qui n'a pas pu être fusionné automatiquement.

Si cela se produit, vous recevrez une alerte de conflit et une liste des conflits que vous devrez résoudre avant de continuer la fusion. **Vous avez deux options pour résoudre un conflit de fusion —** ou **sélectionner une version à fusionner** **manuellement**.

#### modifier le contenu

Sélectionner une version à fusionner

Vous pouvez résoudre un conflit de fusion en sélectionnant une version que vous souhaitez fusionner — soit votre contenu entrant, soit le contenu qui était précédemment présent. Cela vous permet de choisir entre une modification et une autre — soit votre travail récent, soit le contenu original.

#### Si vous traitez un conflit de fusion qui peut être résolu de cette manière, vous pouvez sélectionner la version que vous souhaitez conserver, et l'autre version sera supprimée.

Modification manuelle

### Si vous ne souhaitez pas choisir entre les versions, vous pouvez résoudre un conflit de fusion en modifiant manuellement le conflit. Vous pourrez supprimer les blocs dont vous n'avez pas besoin, ou même les réécrire entièrement. Une fois que vous serez satisfait des modifications, vous pourrez passer au conflit suivant jusqu'à ce qu'ils soient tous résolus.

Archivage d'une demande de modification

Si vous décidez de ne pas fusionner une demande de modification et que vous souhaitez la retirer de la file d'attente, vous pouvez l'archiver. **menu Actions** <picture><source srcset="broken-reference" media="(prefers-color-scheme: dark)"><img src="https://3903131528-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FPnnI41SqLSaKBNwT98fW%2Factions-horizontal.svg?alt=media&#x26;token=99754200-a354-4ffe-931e-aa6322ea7395" alt="The Actions menu icon in GitBook"></picture> Pour archiver une demande de modification, ouvrez-la d'abord. Ensuite, cliquez sur le **à côté du titre de la demande de modification et choisissez**Archiver **Vous pouvez retrouver et rouvrir les demandes de modification archivées plus tard en ouvrant le menu** Demandes de modification **et en sélectionnant l'onglet** Archivé.
