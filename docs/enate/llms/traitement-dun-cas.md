# Source: https://docs.enate.net/enate-help/francais/traitement-dun-cas-1/traitement-dun-cas.md

# Traitement d’un cas

## Soumission initiale du cas

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTg1NA==>" %}

Les cas peuvent être créés des manières suivantes :

* Par un e-mail entrant (si le système est configuré au préalable pour cette boîte de réception)&#x20;
* En cliquant sur « Démarrer un cas » dans un autre flux de Cas.
* Manuellement, à partir du lien « Créer une nouvelle activité » dans la barre d’outils de Work Manager&#x20;
* Automatiquement
* Via des intégrations tierces

## Comment les Cas évoluent d’un statut à un autre

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTg2NQ==>" %}

Lorsque vous démarrez manuellement un Cas directement dans Enate, il restera reste sur le statut "brouillon" jusqu’à ce qu’il ait été soumis pour la première fois.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MibsW4tqMUvzJLHiaR5%2F-MifpKBGRI8M5vvqexJN%2Fimage.png?alt=media\&token=7b2fbb1c-2841-4ecf-8f89-c58d83d2ea06)

Lorsque vous créez manuellement un Cas directement dans Enate, son statut sera « Brouillon » jusqu’à ce qu’il ait été soumis pour la première fois.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWsy10QGFwapNDi9Yhz%2F-MWszrIkYzS2Po4X-rzW%2Fimage.png?alt=media\&token=0b8a5884-45ac-469a-8086-2145cd2c25a0)

Une fois qu’un Cas a été soumis à Enate, son statut changera en « À faire » jusqu’à ce qu’une ressource le prenne en charge, qu’il s’agisse d’une personne ou d’un robot. Quand vous commencez à travailler sur un Cas avec ce statut :

* il vous sera automatiquement affecté
* son statut passera à « En cours »

Vous pouvez également choisir de changer son statut vous-même. Cela signifie que ce Cas est pris en charge et qu’il conservera ce statut jusqu’à ce qu’il soit résolu, en supposant, par exemple, que des informations supplémentaires ne soient pas requises.

## Définir une activité dans la catégorie « À faire »

Si vous avez pris un Cas en charge par erreur, ou si vous vous rendez compte que vous ne serez pas en mesure de le faire progresser, vous pouvez annuler l’affectation, le transférer à une autre ressource ou le renvoyer dans sa file d'attente. Que cela se produise au bout de 10 secondes ou d’une demi-heure, le système le redonnera automatiquement le statut « À faire » afin que tout le monde puisse voir qu’aucun progrès ne sera réalisé tant qu’une autre ressource ne l’aura pas pris en charge. Vous pouvez également lui redonner manuellement le statut « À faire » si, par exemple, vous avez commencé à travailler sur cette activité par erreur et que vous devez rapidement annuler le changement de statut.

De même, si un robot refuse un activité, son statut repassera sur « À faire » afin de permettre à une personne de la prendre en charge.

### Nécessite une attention particulière

De plus, en cas de problème avec un Cas (généralement en raison d’un problème avec l’une de ses actions), le cas repassera au statut « À faire ».

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MibsW4tqMUvzJLHiaR5%2F-MifzQ0-4vYb2Xm2Dvlp%2Fimage.png?alt=media\&token=3bad4434-10f3-4b82-a20e-3e2db4fe5fd9)

Une fois que le Cas a ce statut, le Responsable du cas peut le voir ainsi que la raison, c’est-à-dire souvent l’action qui pose problème dans la fiche d'information. En tant que Responsable du Cas, vous avez plusieurs options à votre disposition :

* Retravailler le Cas depuis une étape précédente ou depuis des Actions terminées lors d’une étape\
  Mettre le cas en pause&#x20;
* Mettre le cas en pause&#x20;
* Redonner le statut « En cours » au Cas&#x20;
* Lancer / relancer manuellement les actions

## Utiliser le statut « En attente »

Si vous travaillez sur un Cas et devez temporairement arrêter votre travail, car vous attendez de recevoir des informations supplémentaires ou à cause d'un autre problème temporaire, donnez-lui le statut « En attente ».

Lorsqu’un Cas passe au statut « En attente », aucune nouvelle Action pour ce Cas ne pourra être créée jusqu'à ce qu’il repasse au statut « À faire » ou « En cours ». Les utilisateurs peuvent terminer des Actions qui ont déjà été créées et qui sont déjà en cours de traitement, mais une fois ces Actions terminées, aucune nouvelle Action ne sera créée.

Lorsque vous placez un Cas sur « En attente », vous devez préciser le type d’attente :

* [Attendre plus d'informations](#en-attente-dinformations-supplementaires)
* [Attendre jusqu’à](#attendre-jusqua)&#x20;
* [Pause](#pause)

### En attente de plus d'informations

Impact sur la durée de l’accord de niveau de service : si l’option « [Ajouter le temps d’attente à la date d’échéance](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/due-date-flavours) » est ACTIVÉE dans les règles de la date d'échéance du Cas (configurées lors de la conception du processus), la durée de l’accord de niveau de service EST MISE EN PAUSE lorsqu’un Cas passe à ce statut. Si l’option est DÉSACTIVÉE, la durée de l’accord de niveau de service CONTINUE à s’écouler pendant que le Cas a ce statut.

Si vous travaillez sur un Cas et que vous devez temporairement interrompre votre travail parce que vous attendez des informations d’un tiers ou d’un client, vous devez choisir « En attente de plus d’informations » comme type d’attente.

Lorsqu’un Cas passe au statut « En attente », aucune nouvelle Action pour ce Cas ne pourra être créée jusqu'à ce qu’il repasse au statut « À faire » ou « En cours ». Les utilisateurs peuvent terminer des Actions qui ont déjà été créées et qui sont déjà en cours de traitement, mais une fois ces Actions terminées, aucune nouvelle Action ne sera créée.

Quand vous cliquez sur « En attente de plus d’informations », vous devez choisir dans la liste déroulante la raison pour laquelle vous avez assigné ce statut au Cas.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MibsW4tqMUvzJLHiaR5%2F-MifzkY21EOU6j2mZuw7%2Fimage.png?alt=media\&token=f4f10105-62b4-47cf-a569-3e602bbd737b)

Si vous confirmez le statut « En attente de plus d'informations », le Cas passera de votre Boîte de réception de travail à votre liste « Mes responsabilités», car vous ne pourrez plus travailler dessus tant que vous n’avez pas reçu de réponse.

Une fois la réponse reçue, le Cas passera de la liste « Mes responsabilités » à votre Boîte de réception de travail, et sera mis en évidence pour que vous puissiez poursuivre votre travail.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FZVRnSRiHNiOcQeYKCLEw%2Fimage.png?alt=media\&token=a71fe65c-78e2-4ce8-b0ef-603db9db0458)

#### Que montre la date d’échéance lorsque la durée de l’accord de niveau de service est mise en pause pour les Cas « En attente de plus d’informations »

Le temps restant de l’accord de niveau de service sera affiché lorsqu'un Cas reçoit le statut « En attente de plus d’informations ».

Si un Cas reçoit le statut « En attente de plus d’informations » et que l’option « [Ajouter le temps d’attente à la date d’échéance](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/due-date-flavours) » est ACTIVÉE dans les règles de la date d'échéance du Cas (configurées lors de la conception du processus), le système mettra la durée de l’accord de niveau de service EN PAUSE. En parallèle, la valeur de la date d’échéance normalement affichée dans la barre d’en-tête du Cas sera cachée (en effet, il est impossible de la connaître avant que la durée de l’accord de niveau de service ne reprenne). À sa place, le système affichera le temps restant jusqu’à l’échéance du Cas au moment où il a reçu ce statut (ou la durée du retard au moment où il a reçu ce statut, si la date d’échéance avait déjà été dépassée).

Exemple : Si le Cas n'a pas encore dépassé la date d'échéance, le message sera : « **Échéance : mis en pause** x **h** y **m avant la date d’échéance** ».

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FvUrNpVbZdSyHM2yySrRE%2Fimage.png?alt=media&#x26;token=9fcafd4e-825b-4731-aab7-6e6d93665f9c" alt=""><figcaption></figcaption></figure>

Exemple : Si le Cas a dépassé la date d'échéance, le message sera : « **Échéance : mis en pause** x **h** y **m après la date d'échéance** ».

### Attendre jusqu’à

Impact sur la durée de l’accord de niveau de service : la durée de l’accord de niveau de service CONTINUE à s’écouler pendant que le Cas a ce statut.

Si vous travaillez sur un Cas et que vous devez temporairement interrompre votre travail jusqu'à une date/heure ultérieure spécifique, vous devez choisir « Attendre jusqu’à » comme type d’attente.

Lorsqu’un Cas se trouve dans ce statut, aucune nouvelle Action ne pourra être créée pour ce Cas jusqu'à ce que la date de Suivi soit atteinte. Les utilisateurs peuvent terminer des Actions qui ont déjà été créées et qui sont déjà en cours de traitement, mais une fois ces Actions terminées, aucune nouvelle Action ne sera créée.

Si vous sélectionnez « Attendre jusqu’à », vous devez préciser la date et l’heure à laquelle l’attente doit se terminer.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MibsW4tqMUvzJLHiaR5%2F-Mil6HHWa0t-lhbI7Py6%2Fimage.png?alt=media\&token=1b3a4472-dde0-4c8b-b044-fcab9b73547d)

Si vous confirmez le statut « Attendre jusqu’à », le Cas passera de votre Boîte de réception de travail à votre liste « Mes responsabilités», car vous ne pourrez plus travailler dessus tant que la date de suivi n’aura pas été atteinte.

Une fois la date atteinte, le Cas passera de la liste « Mes responsabilités » à votre Boîte de réception de travail, et sera mis en évidence pour que vous puissiez poursuivre votre travail.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FRCi10zBBzQHkN5QaMoL6%2Fimage.png?alt=media&#x26;token=cfe212e1-e400-4913-b433-47ccc860700c" alt=""><figcaption></figcaption></figure>

### En pause

Impact sur la durée de l’accord de niveau de service : la durée de l’accord de niveau de service CONTINUE à s’écouler pendant que le Cas a ce statut.

Si vous travaillez sur un Cas et que vous devez temporairement interrompre votre travail, mais que vous n’attendez pas d'informations de la part d’un tiers ou d’un client, ou que vous n’attendez pas une date/heure spécifique, vous devez choisir « En pause » comme type d’attente.

Lorsqu’un Cas passe au statut « En attente », aucune nouvelle Action pour ce Cas ne pourra être créée jusqu'à ce qu’il repasse au statut « À faire » ou « En cours ». Les Cas ne peuvent pas sortir automatiquement du statut « En pause », cela ne peut être fait que manuellement. Les utilisateurs peuvent terminer des Actions qui ont déjà été créées et qui sont déjà en cours de traitement, mais une fois ces Actions terminées, aucune nouvelle Action ne sera créée.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MibsW4tqMUvzJLHiaR5%2F-Mil6UmVVombwvKxe248%2Fimage.png?alt=media\&token=c67153bb-8451-4867-bc77-00d406c25de2)

Si vous confirmez le statut « Attendre jusqu’à », le Cas passera de votre Boîte de réception de travail à votre liste « Mes responsabilités», car vous ne pourrez plus travailler dessus tant qu'un utilisateur n’aura pas manuellement changé son statut en « À faire » ou « En cours ».

Une fois cette modification effectuée, le Cas passera de la liste « Mes responsabilités » à votre Boîte de réception de travail, et sera mis en évidence pour que vous puissiez poursuivre votre travail.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FDUQ1mkGeSfXurDuGywrs%2Fimage.png?alt=media&#x26;token=8b372fb6-9311-4b3b-b26c-2c1e5540dc83" alt=""><figcaption></figcaption></figure>

## Résoudre un Cas

Terminer la résolution marquera le Cas comme résolu avec succès. Une fois qu’un Cas a été résolu, il peut rester sur ce statut pendant une courte période si une [fenêtre de commentaires](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/case-info-section#case-info-tab) a été définie. Durant cette période, le destinataire du service peut répondre et le Ticket peut être rouvert, soit manuellement, soit automatiquement à la réception d’un nouvel e-mail ou d'un commentaire.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2F4TEn3swVaUJquR8HLqew%2Fimage.png?alt=media\&token=1ac81c53-3d87-41e9-b883-ddd6aac418de)

{% hint style="info" %}
Remarque : lorsque des activités sont rouvertes, les données stockées relatives aux personnes qui les ont résolues et au moment où elles l’ont été sont conservées et ne sont pas écrasées lorsque l’activité est résolue une deuxième fois.
{% endhint %}

Si la fenêtre de commentaires a été terminée sans qu’aucune réponse n’ait été reçue,  le statut du Cas sera changé en « Fermé ». Tous les e-mails reçus par la suite créeront une nouvelle activité.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MibsW4tqMUvzJLHiaR5%2F-MinnNRtuE0Y0qvt2GCG%2Fimage.png?alt=media\&token=c34e6055-cee6-4333-a942-dbe78d2526ce)

### Annuler la résolution

En sélectionnant cette option et en appuyant sur le bouton pour confirmer, le Cas sera abandonné. Il sera complètement fermé et ne pourra plus être traité. Si vous rouvrez l’onglet de cette activité, le système confirmera que le Cas a été abandonné.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FJ1D9wFMn9yAQExJoPfOw%2Fimage.png?alt=media\&token=999ae6f3-d56e-43dd-8067-2ed126f4dadf)

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MibsW4tqMUvzJLHiaR5%2F-MinoH2bhri4INs_C_n4%2Fimage.png?alt=media\&token=488201e4-83e6-4ac7-b3eb-93549c86ad64)
