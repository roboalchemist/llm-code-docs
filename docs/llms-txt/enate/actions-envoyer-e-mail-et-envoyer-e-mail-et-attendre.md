# Source: https://docs.enate.net/enate-help/francais/traitement-dune-action-1/actions-envoyer-e-mail-et-envoyer-e-mail-et-attendre.md

# Actions Envoyer e-mail et Envoyer e-mail et attendre

## Aperçu

Les actions « Envoyer un e-mail » impliquent l'envoi automatique d’un e-mail par Enate, puis la fermeture immédiate de l’action. Les utilisateurs de Work Manager ne devraient pas avoir à travailler sur ce type d'action.

Les actions « Envoyer un e-mail et attendre » impliquent l’envoie automatique d’un e-mail par Enate. Le statut de l'action passe alors à « En attente » jusqu’à ce qu'une réponse soit reçue. Une fois la réponse reçue, le statut de l’action passe à « À faire » afin que son traitement se poursuive.

L’adresse de destination et toutes les adresses en Cc ou en Cci de l’e-mail sont configurées dans Builder. Pour savoir comment configurer les actions « Envoyer un e-mail » dans Builder, consultez cet article :&#x20;

{% embed url="<https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/email-action-info-tab>" %}

Une fois que l’e-mail a été envoyé, une entrée apparaît dans la chronologie dans laquelle vous pourrez trouver sa date d’envoi, son expéditeur et son destinataire, les adresses en Cc ou en Cci, l’objet de l’e-mail et, si vous cliquez pour le développer, le corps de l’e-mail.

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FJ5aDSb98mbKx7utQqlIg%2Fimage.png?alt=media&#x26;token=9b2c6afb-d648-4181-bd6d-89f6577d6d0f" alt=""><figcaption></figcaption></figure>

## Exceptions

Si une adresse e-mail invalide est saisie pour le destinaire ou en Cc et/ou en Cci, l’e-mail de l’action « Envoyer un e-mail » ou « Envoyer un e-mail et attendre » ne sera pas envoyé automatiquement et l’action sera replacée dans sa file d’attente.

Un avertissement apparaîtra dans la chronologie signaler le problème :&#x20;

<figure><img src="https://675373381-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-2056118458%2Fuploads%2FFchycRWXIUmZcYhbwNkh%2Fimage.png?alt=media&#x26;token=b80c3ac8-88bf-4710-84ee-47f1a00706ec" alt=""><figcaption></figcaption></figure>

Le propriétaire du cas peut alors décider d’envoyer l'e-mail manuellement, auquel cas il devra corriger l’adresse e-mail et ajouter le corps de l’e-mail manuellement. Il devra également contacter son administrateur système pour lui signaler le problème afin qu’il corrige l’adresse e-mail et évite ainsi les erreurs futures.
