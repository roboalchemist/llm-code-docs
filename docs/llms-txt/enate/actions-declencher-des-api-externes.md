# Source: https://docs.enate.net/enate-help/francais/traitement-dune-action-1/actions-declencher-des-api-externes.md

# Actions « Déclencher des API externes »

Comme pour les autres archétypes d’action, les actions « Déclencher des API externes » peuvent être utilisées dans des processus de « Cas ». Elles sont utilisées lorsque vous avez besoin d’appeler automatiquement un autre système, de lui transmettre des données et éventuellement de faire en sorte que le système externe renvoie des données personnalisées mises à jour dans Enate.

Pour savoir comment configurer les actions « Déclencher des API externes », consultez [la section Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/external-api-action-info-tab).

Il peut parfois y avoir un délai dans l’attente de la réponse du système externe. Lorsque cela se produit, c’est-à-dire lorsque l’action « Déclencher des API externes » attend le retour d’informations d’un système externe, la fiche d’information de l’Action s’affiche dans Work Manager comme ayant le statut « En attente ».

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MdMCT6eBWnGur2fxLcM%2F-MdMCs4SYm7Ny87ggv1D%2Fimage.png?alt=media\&token=719e7144-e0ea-43f1-adb8-cf720ba8a4de)

Quand le système externe finit par envoyer les données mises à jour à Enate, cela sera accompagné d’un marqueur qui indiquera si l’envoi à réussi OU non.

#### **Réponse pour une Actions terminée avec succès**

Si le système répond en indiquant que l’opération a été terminée avec succès, l’Action passera automatiquement au statut « Fermé », avec pour méthode de résolution « Réussi ».

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FYnmoCR4cthC2QVYRPvSu%2Fimage.png?alt=media\&token=94f45c58-87bd-4b3d-a6ee-17608dd37b15)

#### **Réponse pour une Actions ayant échoué**

Si le système répond en indiquant que l’opération a échoué, l’Action passera au statut « À faire », avec pour motif « Mise à jour par l’intégration ». L’API externe peut également répondre en fournissant des informations supplémentaires sur la raison de l’échec de l’Action. Ces informations peuvent être consultées dans la fiche d’information de l’Action, dans la section « Motif du rejet »

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FmUd3GX89rx1FZdMusXGX%2Fimage.png?alt=media\&token=b45dc545-f180-4102-a88b-a1b821cc1119)

Si l’action échoue parce qu’elle ne s’est pas terminée dans le temps imparti ([configuré dans Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/external-api-action-info-tab)), son statut sera changé en « À faire » avec pour motif « Délai d’attente dépassé » et elle sera attribuée à une file d’attente/un utilisateur humain en fonction des règles d’attribution configurées.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FCzx7HgwjTLBhrADPHcLV%2Fimage.png?alt=media\&token=33c797a9-3c1f-4227-ab54-de66e5b2bb69)

Ces actions non réussies se comporteront désormais comme une action manuelle standard.

{% hint style="info" %}
Attention, le responsable du Cas ne sera PAS notifié dans ces situations.
{% endhint %}

### &#x20;**Nouvelles tentatives automatiques**

Si l’Action ne peut pas se connecter au système externe, elle essaiera automatiquement de se reconnecter un certain nombre de fois en fonction de la façon dont votre système est configuré dans Builder ([voir ici pour plus d’informations](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings#automated-failure-retry-pattern)). Un message d’erreur apparaîtra également pour vous indiquer :

* quand l’erreur s’est produite
* quand le système réessayera automatiquement d’établir une connexion
* combien de fois le système a réessayé d’établir une connexion automatiquement
* combien de fois le système réessayera automatiquement d’établir une connexion.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2F1GjzJiEifKjbqf7zjeyj%2Fimage.png?alt=media\&token=2ec6cf08-a646-487e-9b02-3578419cbd62)

Vous pouvez également réessayer manuellement d’établir une connexion à partir d’ici en cliquant sur « Réessayer » dans le message d’erreur.

{% hint style="info" %}
Veuillez noter que lorsque vous réessayez manuellement d’établir une connexion, vos nouvelles tentatives seront comptabilisées comme des nouvelles tentatives de connexion et seront donc incluses dans le nombre de nouvelles tentatives automatiques du système pour établir une connexion.
{% endhint %}

Si l’Action ne parvient pas à établir une connexion après les nouvelles tentatives automatiques (par exemple, si le paramètre de nouvelles tentatives est réglé sur 5 et que le système ne parvient pas à établir une connexion après 5 nouvelles tentatives automatiques), son statut sera changé en « Fermé » et sa méthode de résolution indiquera « Impossible de terminer ».

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MdMCT6eBWnGur2fxLcM%2F-MdMCwu5nm_3FzLcHZOY%2Fimage.png?alt=media\&token=2d9a9e53-8243-43c6-a3bd-5871c9ab6f15)

{% hint style="info" %}
*Si* l’Action ne parvient pas à établir une connexion avec le système externe, le propriétaire du cas en sera informé et l’Action sera marquée comme étant Fermée – Inachevée dans la section Action de l’écran des Cas.
{% endhint %}

L’Action se ferma automatiquement lorsqu’elle aura reçu les informations requises.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2F0frdsw2FjqmQ3rQT8ZPt%2Fimage.png?alt=media\&token=83f5b5f7-4e7f-4601-b871-efbbda098f5f)

#### **Ajuster le paramètre des nouvelles tentatives dans Builder pendant/après qu’elles aient commencé**

Si le paramètre de nouvelles tentatives automatiques dans Builder est modifié après que le système a automatiquement réessayé d’établir une connexion avec un système externe, voici ce qui se produira :

Si, par exemple, le paramètre de nouvelles tentatives était initialement réglé sur 5 et que le système a réessayé 5 fois d’établir une connexion sans succès, le statut de l’Action sera changé en « Fermé » et un message d’erreur indiquera un nombre de nouvelles tentatives de 5/5.

Si le paramètre de nouvelles tentatives est ensuite réglé à une valeur supérieure à 5, par exemple 7, le message d’erreur indiquera un nombre de nouvelles tentatives de 5/7, mais le système ne réessayera PAS automatiquement d’établir une connexion une 6e et 7e fois, car l’Action a déjà été fermée.

Cependant, si le statut de l’Action n’a pas été changé en « Fermé » parce que le nombre maximum de nouvelles tentatives automatiques n’a pas été atteint (par exemple, elle n’a réessayé que 4 fois d’établir une connexion sur les 5 nouvelles tentatives définies), l’augmentation du paramètre de nouvelles tentatives à 7 signifie que l’Action réessayera automatiquement d’établir une connexion jusqu’à ce que le compte atteigne les 7 nouvelles tentatives.

À l’inverse, si vous réduisez le nombre de tentatives après qu’elles ont commencé, par exemple si vous êtes à 4 tentatives sur 10, mais que vous réduisez ensuite le maximum à 4, le système affichera toujours 4 sur 10, mais sera en fait fermé.
