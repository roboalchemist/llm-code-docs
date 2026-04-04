# Source: https://gitbook.com/docs/documentation/fr/gitbook-agent/suggestions-automatiques-de-documentation.md

# Suggestions automatiques de documentation

{% hint style="info" %}

#### Cette fonctionnalité est actuellement en accès anticipé

Rendez-vous dans **Paramètres de l’organisation → Agent GitBook** pour demander l’accès.
{% endhint %}

GitBook Agent peut [se connecter aux mêmes signaux](https://gitbook.com/docs/documentation/fr/gitbook-agent/suggestions-automatiques-de-documentation/connexion-dune-source) que votre équipe utilise pour comprendre à la fois votre produit et ce dont vos utilisateurs ont besoin : conversations de support, fils Slack, issues GitHub, et plus encore.

Avec ce contexte, l’Agent peut identifier de manière proactive les lacunes, proposer des mises à jour et générer automatiquement des modifications de documentation.&#x20;

GitBook Agent est entraîné sur le contenu de votre organisation, ce qui signifie qu’il connaît le style d’écriture, la structure et le ton de votre équipe. Et vous pouvez [ajouter des instructions personnalisées](#add-custom-instructions) que l’Agent doit suivre — plus d’informations ci‑dessous.

{% stepper %}
{% step %}

### Connecter une source

Pour permettre à GitBook Agent de proposer des améliorations automatiques de la docs, vous devrez d’abord [connecter une source](https://gitbook.com/docs/documentation/fr/gitbook-agent/suggestions-automatiques-de-documentation/connexion-dune-source).&#x20;

Après avoir connecté une ou plusieurs sources, l’Agent commencera à travailler en arrière‑plan pour collecter et analyser vos données.
{% endstep %}

{% step %}

### Découvrez comment GitBook Agent analyse vos données

Après la connexion d’une source, GitBook Agent catégorisera ces informations contextuelles en conversations, issues et sujets.

Il les utilise en combinaison pour suggérer des améliorations automatiques à votre documentation, qui sont ouvertes sous forme de demandes de modification.

Pour consulter les données analysées par GitBook Agent, rendez‑vous dans les paramètres de votre organisation, puis ouvrez [**Explorateur de données** onglet](https://gitbook.com/docs/documentation/fr/gitbook-agent/suggestions-automatiques-de-documentation/explorer-vos-donnees) dans le **Agent GitBook** section.
{% endstep %}

{% step %}

### Examiner les demandes de modification effectuées par GitBook Agent

Au fur et à mesure que les données arrivent, GitBook Agent disposera de suffisamment de contexte pour commencer à faire des suggestions — en ouvrant de nouvelles [demandes de modification](https://gitbook.com/docs/documentation/fr/collaboration/change-requests) dans les espaces pertinents.

Vous pouvez modifier les demandes de modification ouvertes par GitBook Agent comme n’importe quelle autre demande de modification — et toute personne de votre équipe peut les examiner, tant qu’elle dispose des [autorisations](https://gitbook.com/docs/documentation/fr/gestion-du-compte/member-management/permissions-and-inheritance).&#x20;

Vous pouvez également [demander une révision à GitBook Agent](https://gitbook.com/docs/documentation/fr/gitbook-agent/reviser-les-demandes-de-modification-avec-gitbook-agent) pour qu’il analyse les modifications qu’il a suggérées.
{% endstep %}

{% step %}

### Collaborer avec GitBook Agent sur les modifications

GitBook Agent peut aussi agir comme partenaire d’écriture, vous permettant de planifier, rédiger, réécrire ou mettre à jour n’importe quoi au sein d’une demande de modification.

Lors de l’examen d’une demande de modification depuis l’ [écran des demandes de modification](https://gitbook.com/docs/documentation/fr/collaboration/change-requests/ecran-des-demandes-de-modification), ouvrir GitBook Agent vous permettra de discuter directement avec lui pour apporter des modifications dans le contexte de la demande de modification sur laquelle vous travaillez.&#x20;

Vous pouvez également ajouter [commentaires](https://gitbook.com/docs/documentation/fr/collaboration/comments) à des blocs spécifiques, et taguer @gitbook pour demander à GitBook Agent d’apporter une modification.
{% endstep %}
{% endstepper %}

### Ajouter ou supprimer des sites publiés que GitBook Agent peut modifier

Par défaut, GitBook Agent aura accès pour créer des demandes de modification sur n’importe lequel de vos sites de documentation publiés. Dans l’écran des paramètres de GitBook Agent, vous pouvez choisir les sites sur lesquels vous souhaitez que l’Agent propose des modifications.

### Ajouter des instructions personnalisées pour GitBook Agent

Pour [ajouter des instructions personnalisées pour GitBook Agent](https://gitbook.com/docs/documentation/fr/quest-ce-que-gitbook-agent#add-a-style-guide-and-custom-instructions) à suivre, ouvrez les paramètres de votre organisation et choisissez la **Agent GitBook** page dans la barre latérale.

À partir d’ici, vous pouvez rédiger des instructions personnalisées que l’Agent utilisera chaque fois qu’il préparera, analysera et générera des demandes de modification pour vos sites de documentation.
