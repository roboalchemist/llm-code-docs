# Source: https://gitbook.com/docs/documentation/fr/gitbook-agent/suggestions-automatiques-de-documentation/connexion-dune-source.md

# Connexion d'une source

GitBook Agent peut intégrer du contexte provenant de différentes sources, notamment Intercom, Slack, e‑mail et plus encore. Connecter une source permet à l’Agent de créer des demandes de modification basées sur un contexte réel, comme des chaînes d’e‑mails, des fils Slack ou des conversations Intercom résolues.

L’Agent analyse ce contexte, regroupe les données pertinentes en problèmes et sujets, puis génère des modifications suggérées basées sur ces points de données.

Le contexte fourni via différents connecteurs permettra à votre équipe de travailler plus rapidement et de manière plus fiable, en réduisant le travail dupliqué consistant à documenter quelque chose qui a peut‑être déjà été résolu sur une autre plateforme.

### Connecter une source

Allez dans les paramètres de votre organisation, puis dans la **section GitBook Agent** À partir d’ici, vous pourrez configurer les différents connecteurs afin de connecter correctement l’outil souhaité.

Chaque connecteur fonctionne légèrement différemment et peut contenir des fonctionnalités différentes. Consultez la section correspondant à votre outil ci‑dessous pour voir comment configurer et utiliser l’outil souhaité.

<details>

<summary>E‑mail</summary>

Le connecteur e‑mail est un connecteur polyvalent qui vous permet de fournir du contexte à GitBook Agent **via une adresse e‑mail dédiée**.

Aucune configuration n’est nécessaire pour utiliser le connecteur e‑mail — il fonctionne immédiatement.

#### Ajouter des fils e‑mail à GitBook Agent

1. Ajoutez n’importe quel fil e‑mail à l’Agent en transférant le fil e‑mail vers l’adresse e‑mail dédiée fournie dans les paramètres de GitBook Agent.

#### Utiliser le connecteur e‑mail pour connecter des applications tierces

Le connecteur e‑mail est le moyen le plus polyvalent de fournir du contexte à GitBook. En utilisant des outils comme [Zapier](https://zapier.com/) ou [Relay.app](https://relay.app/), vous pouvez connecter des milliers d’applications tierces.

Dans l’un ou l’autre de ces outils, configurez un nouveau flux de travail/une nouvelle connexion, et assurez‑vous que la sortie est envoyée à l’adresse e‑mail dédiée fournie dans les paramètres de GitBook Agent.

</details>

<details>

<summary>Intercom</summary>

Le connecteur Intercom permet à GitBook Agent d’extraire du contexte depuis **des conversations résolues ou clôturées**.&#x20;

Chaque fois qu’une conversation est clôturée par votre équipe de support, le connecteur Intercom enverra le contexte complet de la conversation à GitBook Agent. L’Agent utilisera ce contexte pour générer [des problèmes](https://gitbook.com/docs/documentation/fr/gitbook-agent/explorer-vos-donnees#issues) (et finalement [des sujets](https://gitbook.com/docs/documentation/fr/gitbook-agent/explorer-vos-donnees#topics)), qui sont ensuite utilisés pour générer une demande de modification exploitable pouvant être examinée par votre équipe.

#### Connecter Intercom

1. Dans les paramètres de GitBook Agent, cliquez sur le connecteur Intercom et autorisez Intercom avec votre compte.
2. Une fois connecté, GitBook Agent est prêt à commencer à analyser vos tickets de support clôturés.

#### Ajouter des conversations Intercom à GitBook Agent

Le connecteur Intercom fonctionne en arrière‑plan — une fois installé et configuré, il s’exécutera automatiquement en arrière‑plan et ajoutera les conversations résolues ou clôturées à GitBook Agent.

</details>

<details>

<summary>Slack</summary>

Le connecteur Slack permet à GitBook Agent d’extraire du contexte depuis **les fils dans lesquels il est mentionné**.

Une fois que le connecteur Slack est appelé dans un fil, il analysera le contexte du fil et enverra le contexte complet de la conversation à votre GitBook Agent. L’Agent utilisera ensuite ce contexte pour générer des problèmes (et finalement des sujets), qui sont ensuite utilisés pour générer une demande de modification exploitable pouvant être examinée par votre équipe.

#### Connecter Slack

1. Dans les paramètres de GitBook Agent, cliquez sur le connecteur Slack et autorisez Slack avec votre compte.
2. Installez le bot Slack dans l’espace de travail Slack de votre organisation.

#### Ajouter des fils Slack à GitBook Agent

1. Appelez `@gitbook` à l’intérieur d’un fil que vous souhaitez ingérer.
2. Ajoutez éventuellement un contexte supplémentaire que l’Agent peut utiliser, par exemple :

```
@gitbook utilisez cette conversation pour mieux documenter notre référence API.
```

</details>
