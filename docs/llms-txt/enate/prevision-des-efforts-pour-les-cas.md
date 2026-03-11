# Source: https://docs.enate.net/enate-help/francais/les-differents-types-decran-des-activites/prevision-des-efforts-pour-les-cas.md

# Prévision des efforts pour les cas

## Vue d’ensemble

Les utilisateurs de la version 2024.1 pourront utiliser la fonction de prévision des efforts pour fournir une estimation plus précise des efforts nécessaires pour traiter des activités, ce qui vous permettra de planifier les besoins en ressources de manière plus efficace.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTY5NTg1MQ==>" %}

À long terme, ces données peuvent être rassemblées et transmises aux administrateurs afin d’ajuster les délais d’estimation des efforts et de fournir des prévisions plus précises pour les futurs volumes de travail.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FVsG4PhkIc9AOxAS4yjPn%2Fimage.png?alt=media&#x26;token=a1813c4a-f113-4b2b-ade4-071bb1e5c590" alt=""><figcaption></figcaption></figure>

## Comment utiliser la prévision des efforts

Une fois la fonction « Prévision des efforts » activée, un nouvel onglet « Estimation des efforts » apparaît dans vos cas, dans Work Manager.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FNZIYXis1vtXOA4qDr0lm%2Fimage.png?alt=media&#x26;token=2e208d5b-17fa-46cc-9253-3ba4df72162b" alt=""><figcaption></figcaption></figure>

Vous y trouverez un résumé des efforts estimés pour l’ensemble du cas, une répartition des efforts estimés pour les actions ou les sous-cas qui composent le cas, ainsi qu’une répartition des efforts estimés pour les actions ou les sous-cas qui n’ont pas encore été créés.

#### Résumé des efforts du cas

La section « Résumé des efforts du cas » permet à l’utilisateur de modifier la durée estimée nécessaire pour terminer le cas. Elle fournit également d’autres mesures utiles pour celui-ci.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FvPVeP70ylqraOXXDgtBk%2Fimage.png?alt=media&#x26;token=2bb20e4e-2fb6-418c-9512-c7fd9ce97496" alt=""><figcaption></figcaption></figure>

* L’effort « estimé » indique la durée totale estimée nécessaire pour terminer le cas. Il peut être modifié par un utilisateur avec une estimation plus précise.
  * Il s’agit de la somme de l’effort « estimé » de toutes les activités créées et des actions (et actions de sous-cas) qui composent le cas, ainsi que de la valeur « Effort pour les activités pas encore créées ».
  * Le champ affichera initialement la valeur « Effort estimé initial par enregistrement » de Builder (le cas échéant) multipliée par le nombre d’enregistrements.
    * Si le nombre d’enregistrements est modifié, l’effort estimé pour le cas qui n’a pas été modifié par un utilisateur de Work Manager sera actualisé afin de refléter la modification du nombre d'enregistrements.
  * Une fois que le cas est résolu ou clôturé, l’estimation de l’effort ne peut plus être modifiée.
  * Attention, si vous augmentez cette valeur, vous augmentez l’estimation de « l’effort pour l’activité pas encore créée », et vice versa.
* L’effort « réel » indique le temps qui a été consacré au cas.
  * Il s’agit de la somme de l’effort « réel » pour toutes les actions créées et les sous-cas qui composent le cas, à partir de leur suivi du temps respectif.
* « Restant estimé » indique le temps restant estimé pour terminer le cas.
  * Il s’agit de la somme de l’effort « restant estimé » pour toutes les actions créées et les sous-cas qui composent le cas ET du temps restant estimé pour les activités qui n’ont pas encore été créées (il se peut donc qu’il ne soit pas toujours égal à l’effort « estimé du cas » moins l’effort « réel du cas »).

Modifier la valeur de l’effort « estimé » pour un cas aura pour effet de :

* Actualiser automatiquement la valeur estimée de « l’Effort pour l’activité pas encore créée ». En effet, « l’Effort estimé » pour le cas est une valeur calculée composée de la somme de l’effort « estimé » de toutes les activités créées et des actions (et actions secondaires) qui composent le cas et de la valeur de « l’Effort pour l’activité pas encore créée ».
  * Augmenter l’effort « estimé » pour un cas augmente la valeur de « l’effort pour l’activité pas encore créée » du même montant.
  * Diminuer l’effort « estimé » pour un cas diminue la valeur de « l’Effort pour l’activité pas encore créée » du même montant.

#### Répartition de l'effort pour une activité créée

La section « Répartition de l’effort pour l’activité créée » permet à l’utilisateur de modifier la durée estimée des différentes actions créées (et des sous-cas) qui composent le cas. Elle présente également d’autres indicateurs de mesure utiles pour chacune des actions créées (et des sous-cas) qui composent le cas.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FT9VouZu04BwuCXonfobZ%2Fimage.png?alt=media&#x26;token=a4f19efb-60ca-4ee7-a001-2ba8fe61c934" alt=""><figcaption></figcaption></figure>

Notez qu’une fois qu’une action est résolue ou clôturée, son effort estimé ne peut plus être modifié.

Au fur et à mesure que des actions (et des sous-cas) sont créées, l’effort estimé pour ces actions sera tiré de la valeur de l’effort estimé de la section Activité pas encore créée ci-dessous.

#### Répartition pour les actions

Pour chaque action, vous verrez :

* Un lien vers chaque action
* Une valeur d’effort « estimé » qui montre le temps total estimé nécessaire au traitement de l’action. Cette estimation peut être modifiée par un utilisateur avec une valeur plus précise.
  * Le champ affichera initialement la valeur manuelle « Effort estimé initial par enregistrement » de Builder multipliée par le nombre d’enregistrements.
    * Si le « nombre d’enregistrements » est modifié, l’« effort estimé » pour toutes les actions en cours qui n’ont pas été modifiées par un utilisateur du Work Manager sera actualisé pour refléter le changement du nombre d’enregistrements.
  * Augmenter cette valeur diminuera l’estimation pour l’« activité pas encore créée » et vice-versa, ce qui pourrait affecter l’effort total estimé pour le cas.
  * Notez qu’une fois qu’une action est résolue ou clôturée, son estimation d’effort ne peut plus être modifiée.
* L’effort « réel » indique le temps qui a été consacré à cette action jusqu’à présent.
  * Cette valeur est tirée du suivi du temps de l’action.
* « Restant estimé » indique le temps restant estimé pour terminer l’action.
  * Il est calculé en soustrayant l’effort « réel » pour l'action de son effort « estimé ».
* La date d’échéance de l’action.
  * Si l’effort « réel » est égal à zéro, vous verrez également une valeur « Commencer avant le ». Elle indique la date la plus tardive à laquelle le traitement de l’action doit débuter afin de respecter son échéance.
* Le statut de l’action.

Modifier la valeur de l’effort « estimé » pour une action aura pour effet de :

* Actualiser automatiquement la valeur estimée de l’« effort pour l’activité pas encore créée » pour le cas.
* Possiblement actualiser automatiquement l’effort « estimé » pour l’ensemble du cas.

Détails :&#x20;

* Diminuer l’effort « estimé » pour une action augmente la valeur « Effort pour l’activité pas encore créée » pour le cas du même montant (laissant l’effort « estimé » pour l’ensemble du cas inchangé).
* Augmenter l’effort « estimé » pour une action diminue la valeur « Effort pour l’activité pas encore créée » pour le cas du même montant. Cela peut ou non affecter la valeur de l’effort « estimé » pour l’ensemble du cas.
  * Si l’effort estimé modifié d’une action n’augmente pas suffisamment pour que la valeur de l'effort pour l’activité pas encore créée tombe en dessous de 0, l’effort estimé pour l’activité ne sera pas affecté.
    * Exemple : imaginons que l’effort « estimé » pour l’Action 1 soit de deux heures, que l’effort estimé pour l’activité pas encore créée soit d’une heure et que l’effort estimé pour le cas soit de trois. Un utilisateur décide que l’Action 1 va prendre une heure de plus et modifie donc l’effort « estimé » pour l’Action 1 de deux à trois heures. L’effort pour l’activité pas encore créée passera alors d’une heure à zéro, et l’effort estimé pour le cas, lui, ne changera pas, il restera à trois heures.
  * Si l’« effort estimé » modifié d’une action augmente suffisamment pour que la valeur de l’ « effort pour l’activité pas encore créée » du cas soit inférieure à 0, la différence doit être ajoutée à l’« effort estimé » de l’ensemble du cas.
    * Exemple : imaginons qu’une seule action, l’Action 1, ait été créée pour un cas. L’effort « estimé » pour traiter l’Action 1 est de deux heures, l’effort estimé pour l’activité pas encore créée est de zéro et, par conséquent, l’effort « estimé » pour l’ensemble du cas est de deux heures. Un utilisateur décide que l’Action 1 va prendre une heure de plus et modifie donc l’effort « estimé » pour l’Action 1 de deux à trois heures. L’effort pour l’activité pas encore créée étant de zéro, l’effort « estimé » pour l’ensemble du cas va donc augmenter d’une heure, passant de deux à trois heures.
    * Exemple 2 : imaginons qu’une seule action, l’Action 1, ait été créée pour un cas. L’effort « estimé » pour traiter l’Action 1 est de deux heures, l’effort estimé pour « l’activité pas encore créée » est d’une heure et l’effort « estimé » pour l’ensemble du cas est donc de trois heures. Un utilisateur décide que l’Action 1 va prendre deux heures de plus et modifie donc l’effort « estimé » pour l’Action 1 de deux à quatre heures, ce qui entraîne une diminution de l’effort pour « l’activité pas encore créée » d’une heure, soit d’une heure à zéro (il diminue autant que possible). L’heure « restante » sera effectivement ajoutée à l’effort total « estimé » du cas, qui augmentera donc d’une heure et passera de trois à quatre heures.

#### Répartition pour les sous-cas

Si un sous-cas est créé, vous verrez :

* un lien vers le sous-cas si vous avez la permission d’y accéder (sinon, vous verrez seulement le nom et le numéro de référence du sous-cas, sans lien)
* Une ligne « total » des sous-cas avec les éléments suivants :
  * L’effort « estimé » indique la durée totale estimée nécessaire au traitement du sous-cas. Un utilisateur peut le modifier avec une estimation plus précise.
    * Il s’agit de la somme des efforts « estimés » de toutes les actions créées et à créer qui composent le sous-cas.
    * Le champ affichera initialement la valeur « Effort estimé initial par enregistrement » de Builder (le cas échéant) multipliée par le nombre d'enregistrements.
      * Si le nombre d’enregistrements est modifié, l’effort estimé pour le sous-cas qui n’a pas été modifié par un utilisateur de Work Manager sera actualisé afin de refléter la modification du nombre d’enregistrements.
    * Une fois qu’un sous-cas est résolu ou clôturé, son effort estimé ne peut plus être modifié.
    * Notez qu’en augmentant cette valeur, vous augmentez l’estimation de « l’activité pas encore créée » pour le sous-cas et vice versa.
  * L’effort « réel » indique le temps qui a été consacré jusqu’à présent au traitement du sous-cas.
    * Il s’agit de la somme des efforts « réels » pour toutes les actions créées qui composent le sous-cas, tirés de leur suivi du temps respectif.
  * « Restant estimé » indique le temps restant estimé pour le sous-cas.
    * Il s’agit de la somme de l’effort « restant estimé » pour toutes les actions créées qui composent le sous-cas ET du temps restant estimé pour les activités qui n’ont pas encore être créées pour ce sous-cas (il se peut donc qu’il ne soit pas toujours égal à l’effort « estimé pour le sous-cas » moins l’effort « réel pour le sous-cas »).
    * La date d’échéance du sous-cas
    * Le statut du sous-cas
* Une ligne pour chaque action de sous-cas avec :
  * L'effort « estimé » indique la durée totale estimée de l'action de sous-cas. Il peut être modifié par un utilisateur avec une estimation plus précise.
    * Le champ affichera initialement la valeur « Effort estimé initial par enregistrement » de Builder (le cas échéant) multipliée par le nombre d’enregistrements.
      * Si le nombre d’enregistrements est modifié, l’effort estimé pour toutes les action de sous-cas en cours qui n’ont pas été modifiées par un utilisateur de Work Manager sera actualisé afin de refléter la modification du nombre d'enregistrements.
    * Augmenter cette valeur diminuera l’estimation du sous-cas des « activités pas encore créées » et vice-versa, ce qui pourrait affecter l’effort total estimé du sous-cas.
    * Une fois qu’une action est résolue ou clôturée, son estimation d’effort ne peut plus être modifiée.
  * L’effort « réel » indique le temps qui a été consacré jusqu’à présent au traitement de cette action du sous-cas.
    * Cette valeur est tirée du suivi du temps de l’action de sous-cas.
  * « Restant estimé » indique le temps restant estimé pour l’action du sous-cas.
    * Il est calculé en soustrayant l’effort « réel » pour l’action du sous-cas de son effort « estimé ».
  * La date d’échéance de l’action du sous-cas
    * Si l’effort « réel » est égal à zéro, vous verrez également une valeur « Commencer avant le ». Elle indique la date la plus tardive à laquelle le traitement de l’action du sous-cas doit débuter afin de respecter son échéance.
  * Le statut de l’action du sous-cas.
* Une ligne pour les « activités de sous-cas pas encore créées » avec :
  * L’effort « estimé » indique l’effort estimé nécessaire pour terminer le traitement des actions du sous-cas qui n’ont pas encore été créées pour ce sous-cas. Il peut être modifié par un utilisateur avec une estimation plus précise.
    * Modifier cette estimation affectera l’effort total « estimé pour le sous-cas » et pourrait affecter l’estimation de l’effort pour l’ensemble du cas.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FMr5o99uL8yZmPZIvNNBt%2Fimage.png?alt=media&#x26;token=26b2a088-47be-4d53-a32f-bf5be09df8f4" alt=""><figcaption></figcaption></figure>

Modifier la valeur de l’effort « estimé » pour une action de sous-cas aura pour effet de :

* Actualiser automatiquement la valeur estimée de l’« effort pour l’activité pas encore créée » pour le sous-cas.
* Possiblement actualiser automatiquement l’effort « estimé » pour l’ensemble du sous-cas.
* Possiblement actualiser automatiquement l’effort « estimé » pour l’ensemble du cas parent.

Détails :

* Diminuer l’effort « estimé » pour une action de sous-cas augmente la valeur « Effort pour l’activité pas encore créée » pour le sous-cas du même montant (laissant l’effort « estimé » pour l’ensemble du cas inchangé et n’ayant donc pas d’impact sur l’effort « estimé » pour l’ensemble du cas parent).
* Augmenter l’effort « estimé » pour une action de sous-cas diminue la valeur « Effort pour l’activité pas encore créée » pour le sous-cas du même montant. Cela peut ou non affecter la valeur de l’effort « estimé » pour l’ensemble du cas.
  * Si l’effort estimé modifié d’une action de sous-cas n’augmente pas suffisamment pour que la valeur de « l'effort pour l’activité pas encore créée » du sous-cas tombe en dessous de 0, l’effort estimé pour le sous-cas ne sera pas affecté (et l’effort « estimé » pour l’ensemble du cas parent ne sera donc pas affecté).
    * Exemple : imaginons qu’une seule action de sous-cas, l’Action de sous-cas 1, ait été créée pour un sous-cas. L’effort « estimé » pour traiter l’Action de sous-cas 1 est de deux heures et l’effort estimé pour l’activité pas encore créée est d’une heure. L’effort « estimé » pour le sous-cas est donc de trois heures. Un utilisateur décide que l’Action de sous-cas 1 va prendre une heure de plus et modifie donc l’effort « estimé » pour l’Action de sous-cas 1 de deux à trois heures. « L’effort pour les activités pas encore créées » pour le sous-cas passe donc d’une heure à zéro. L’effort « estimé » pour le sous-cas, lui, ne changera pas et restera de trois heures (l’effort « estimé » pour l’ensemble du cas parent n’en sera donc pas affecté).
  * Si l’« effort estimé » modifié d’une action de sous-cas augmente suffisamment pour que la valeur de l’ « effort pour l’activité pas encore créée » du sous-cas soit inférieure à 0, la différence doit être ajoutée à l’« effort estimé » de l’ensemble du sous-cas (et il pourrait donc avoir un impact sur l’effort « estimé » pour l’ensemble du cas parent).
    * Exemple : imaginons qu’une seule action de sous-cas, l’Action de sous-cas 1, ait été créée pour un sous-cas. L’effort « estimé » pour traiter l’Action de sous-cas 1 est de deux heures, l’effort estimé pour l’activité pas encore créée est de zéro et, par conséquent, l’effort « estimé » pour l’ensemble du sous-cas est de deux heures. Un utilisateur décide que l’Action de sous-cas 1 va prendre une heure de plus et modifie donc l’effort « estimé » pour l’Action de sous-cas 1 de deux à trois heures. L’effort pour l’activité pas encore créée pour le sous-cas étant de zéro, l’effort « estimé » pour l’ensemble du sous-cas va donc augmenter d’une heure, passant de deux à trois heures.
      * S’il y a suffisamment de temps disponible dans « l’effort pour les activités pas encore créées » du cas parent, cette augmentation d’une heure peut être tirée de là, et il n’y aura donc pas d’impact sur l’effort « estimé » pour l’ensemble du cas parent.
      * S’il n’y a pas assez de temps disponible dans « l’effort pour les activités pas encore créées » du cas parent, cette augmentation d’une heure se traduira par une augmentation de l’effort « estimé » pour l’ensemble du cas parent.
    * Exemple 2 : imaginons qu’une seule action de sous-cas, l’Action de sous-cas 1, ait été créée pour un sous-cas. L’effort « estimé » pour traiter l’Action de sous-cas 1 est de deux heures, l’effort estimé pour « l’activité pas encore créée » pour le sous-cas est d’une heure et l’effort « estimé » pour l’ensemble du cas est donc de trois heures. Un utilisateur décide que l’Action de sous-cas 1 va prendre deux heures de plus et modifie donc l’effort « estimé » pour l’Action de sous-cas 1 de deux à quatre heures, ce qui entraîne une diminution de l’effort pour « l’activité pas encore créée » pour le sous-cas d’une heure, soit d’une heure à zéro (il diminue autant que possible). L’heure « restante » sera effectivement ajoutée à l’effort total « estimé » du sous-cas, qui augmentera donc d’une heure et passera de trois à quatre heures.
      * S’il y a suffisamment de temps disponible dans « l’effort pour les activités pas encore créées » du cas parent, cette augmentation d’une heure peut être tirée de là, et il n’y aura donc pas d’impact sur l’effort « estimé » pour l’ensemble du cas parent.
      * S’il n’y a pas assez de temps disponible dans « l’effort pour les activités pas encore créées » du cas parent, cette augmentation d’une heure se traduira par une augmentation de l’effort « estimé » pour l’ensemble du cas parent.

#### Effort pour les activités pas encore créées

La section « Effort pour les activités pas encore créées » indique la quantité d’effort estimée nécessaire pour terminer le traitement des actions (et des actions de sous-cas) qui n’ont pas encore été créées pour ce cas.

Il est calculé en soustrayant la somme de l’effort « estimé » pour les activités créées de l’effort « estimé » pour traiter le cas. Par conséquent, augmenter « l’effort pour les activités pas encore créées » augmentera l’estimation de l’effort pour l’ensemble du cas et vice versa.

Au fur et à mesure que des actions (et des sous-cas) sont créées, l’estimation de l’effort pour ces actions sera tirée de la valeur « Effort estimé pour les activités pas encore créées ».

Une fois que le cas est résolu ou clôturé, « l’effort pour les activités pas encore créées » ne peut plus être modifié.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2F0QFpPDIikAhNp7nDolmZ%2Fimage.png?alt=media&#x26;token=f85f3c65-747a-49a8-a760-713df2b9bed4" alt=""><figcaption></figcaption></figure>
