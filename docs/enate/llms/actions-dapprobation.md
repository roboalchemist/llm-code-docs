# Source: https://docs.enate.net/enate-help/francais/traitement-dune-action-1/actions-dapprobation.md

# Actions d’approbation

## En quoi consistent les actions d’approbation ? Comment fonctionnent-elles ?

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTQ5NDEwNw==>" %}

Souvent, dans les flux de cas des processus d’entreprise élaborés dans Enate, on constate des points où des personnes externes (c’est-à-dire des personnes qui ne travaillent pas sur Enate, telles que des responsables commerciaux de votre entreprise ou de l’entreprise cliente concernée) doivent approuver des activités avant que le processus ne puisse se poursuivre. Les processus de paie des salaires constituent un bon exemple de ce type de processus, car la direction du client doit approuver les rapports de paie avant que le processus ne puisse être autorisé à se poursuivre.

L’action d’approbation d’Enate est conçue pour prendre en charge ces scénarios de demande d’approbation de manière plus intégrée, afin de garantir que ce « cycle d’approbation » est soigneusement organisé et visible dans le flux d’activités d’Enate.

## Fonctionnement des actions d’approbation

Les demandes d’approbation sont envoyées à des agents travaillant en dehors d’Enate pour qu’ils les approuvent, ou les refusent.

Différents types d’approbation influencent la manière dont la décision est prise :

* Dans un scénario impliquant plusieurs niveaux d’approbation, l’e-mail de demande est envoyé à chaque nouveau niveau lorsque l’approbation du niveau précédent a été obtenue, jusqu’à un maximum de trois niveaux. Si une personne refuse, l’approbation est refusée.
* Dans un scénario parallèle de type ***n’importe***, la demande est envoyée par e-mail à tous les approbateurs et la première décision reçue est prise en compte.
* Dans un scénario parallèle de type ***tous***, l’e-mail de demande est envoyé à tous les approbateurs et ils doivent TOUS approuver la demande pour qu’elle soit approuvée. Si l’un d’entre eux refuse, l’approbation est refusée.

Si la demande est approuvée par toutes les parties nécessaires, l’action d’approbation est résolue avec succès et clôturée automatiquement, de sorte qu’aucun agent travaillant dans Work Manager n’aura besoin de s’en occuper. Il est cependant toujours possible de consulter l’action clôturée en cliquant dessus.

## Exceptions : approbations traitées par un agent dans Work Manager

Il existe cependant quelques scénarios dans lesquels un agent travaillant sur Work Manager peut être amené à prendre en charge et à effectuer toutes les activités nécessaires pour poursuivre le traitement d’une action d’approbation :

* L’approbation a été refusée
* Aucun approbateur (ou un nombre insuffisant d'approbateurs) n'a été déterminé automatiquement

### Approbation refusée

Si une demande d’approbation est refusée, le statut de l’action passe à « À faire » et son traitement doit être confié à un agent sur Work Manager. Celui-ci doit examiner le motif de refus fourni par l’approbateur et décider de la marche à suivre. Il peut soit :

1. **Effectuer les modifications nécessaires et renvoyer la demande en réglant le statut de l’action sur « En attente »**. Ceci aura pour effet de renvoyer automatiquement l’e-mail de demande d’approbation\*\* et de faire passer le statut de l’action à « En attente de plus d’informations », car nous attendons que des informations externes (une approbation) soient à nouveau enregistrées dans le système avant que l’activité puisse se poursuivre.
2. **Donner à l’action le statut « Impossible de terminer »**. Cela alertera le propriétaire du cas qui devra alors décider de la marche à suivre (par exemple, retravailler le cas, ou le clôturer).
3. **Marquer l’action comme étant résolue**, ce qui marquera manuellement la demande comme étant approuvée. Le cas peut alors passer à l’action suivante.

{% hint style="info" %}
\*\*Remarque : l’envoi des e-mails de demande d’approbation reprendra depuis le début, c’est-à-dire que tous les demandeurs recevront à nouveau un e-mail. S’ils cliquent sur l’un des e-mails envoyés précédemment, ils recevront un message leur indiquant que CETTE demande d’approbation spécifique n’est plus valable, car les détails de la demande ont peut-être été modifiés.
{% endhint %}

### Nombre insuffisant d’approbateurs

Dans le cas où un agent doit ajouter des approbateurs parce qu’un ou plusieurs approbateurs requis sont manquants (ou apporter des modifications qui font que les demandes d’approbation doivent être renvoyées), l’agent reprendra l’action d’approbation avec pour statut « À faire ».\
Une fois les modifications effectuées et/ou les noms des approbateurs manquants ajoutés, l’agent doit donner à l’action le statut « En attente ». \
L’e-mail de demande d’approbation sera alors envoyé automatiquement et le statut de l’action passera en « En attente de plus d’informations », car l’action attend des informations externes (une approbation) avant de pouvoir continuer.

{% hint style="info" %}
Remarque : Lorsqu’une action d’approbation a le statut « À faire » ou « En cours », les parties externes qui ont reçu des demandes d’approbation par e-mail ne seront PAS en mesure d’approuver ou de refuser la demande. Ils recevront à la place un message les informant que l’élément en question est en cours de traitement. Les agents travaillant sur Work Manager DOIVENT redonner le statut « En attente de plus d’informations » à l’action s’ils souhaitent reprendre l’activité d’approbation.
{% endhint %}

## Si les demandes d’approbation arrivent à expiration...

Un autre scénario possible est que l’action d’approbation soit clôturée automatiquement, car elle a expiré en raison de l’absence ou de l’insuffisance de réponses reçues dans les délais impartis. Dans ce cas, l’action sera automatiquement marquée comme étant résolue et le cas continuera son traitement. Dans ce scénario, aucun agent n’aura besoin de reprendre une action dans Work Manager, mais il sera toujours possible de consulter l’action clôturée en cliquant dessus.
