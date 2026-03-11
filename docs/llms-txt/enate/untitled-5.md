# Source: https://docs.enate.net/enate-help/francais/traitement-dune-action-1/untitled-5.md

# Actions « Attendre que des Sous-cas soient terminés »

Une Action « Attendre que des Sous-cas soient terminés » attendra qu’un Sous-cas spécifique soit terminé avant de permettre au Cas de passer à l’Action suivante.

Vous pouvez reconnaître une Action « Attendre que des Sous-cas soient terminés » à sa fiche d’information qui indiquera : « L’Action attend qu’un Sous-Cas soit terminé ».

Une fois qu’une action « Attendre que des Sous-cas soient terminés » a été lancée ET que le Sous-cas qu’elle doit attendre a été créé (manuellement ou par le biais d’une action « Créer un Cas »), le statut de l’Action « Attendre que des Sous-cas soient terminés » sera changé en « En attente ».

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2F1PcLgZh8YnvNxYgh83Tz%2Fimage.png?alt=media\&token=64ea6505-b04c-4ba8-a306-d93359dc0a19)

Une fois que le Sous-cas est terminé, l’action « Attendre que des Sous-cas soient terminés » se terminera automatiquement.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FHmeHoFPrxNKBiShLjve4%2Fimage.png?alt=media\&token=2fa9e84d-593e-4f95-a939-0ef32f6ed432)

Vous recevrez également une notification dans la chronologie.

![](https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2Fl0Gh1oglrDPGZHs7cNeZ%2Fimage.png?alt=media\&token=759e8a23-47d2-44f7-85c2-27e7cb486190)

Si le Sous-cas que l’Action « Attendre que des Sous-cas soient terminés » doit attendre n’est pas disponible (soit parce qu’il n’a pas été créé, soit parce qu’il a été résolu avant que l’Action ne soit lancée), le statut de l’Action sera changé en « À faire » et elle sera assignée à une File d’attente où un utilisateur pourra la prendre en charge et décider comment procéder.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FvybrgOoy5VtZ4nvCa52t%2Fimage.png?alt=media&#x26;token=c14a8e46-0985-4491-9752-7d797e5a912a" alt=""><figcaption></figcaption></figure>

Si vous essayez ensuite de changer le statut de l’Action « Attendre que des Sous-cas soient terminés » en « En attente », l’Action se terminera, car le Sous-cas qu’elle doit attendre n’a pas été créé.

Si le statut de l’Action n’est pas « Attendre que des Sous-cas soient terminés » et que le Sous-cas qu’elle attend est terminé, le message « Le Sous-cas est terminé » apparaîtra dans la fiche d’information.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FhABrYhlOJQsoRo1unIcY%2Fimage.png?alt=media&#x26;token=523b4419-6680-4c5c-a33e-838c3aa462ff" alt=""><figcaption></figcaption></figure>

Si vous résolvez manuellement une Action « Attendre que des Sous-cas soient terminés », elle sera marquée comme résolue sans que le Sous-cas soit terminé.

{% hint style="info" %}
Veuillez noter que si votre système a été configuré pour automatiquement terminer une Action « Attendre que des Sous-cas soient terminés » (voir ici pour plus d’informations sur la façon de le configurer) et que le Sous-cas que l’Action doit attendre n’est pas disponible (soit parce qu’il n’a pas été créé, soit parce qu’il a été résolu avant que l’Action ne soit lancée), le statut de l’Action sera automatiquement changé en « Fermé ». Vous en serez informé dans la chronologie.
{% endhint %}
