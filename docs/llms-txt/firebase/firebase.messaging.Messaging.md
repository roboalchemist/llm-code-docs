# Source: https://firebase.google.com/docs/reference/js/v8/firebase.messaging.Messaging.md.txt

# Messaging | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [messaging](https://firebase.google.com/docs/reference/js/v8/firebase.messaging).
- Messaging

The Firebase Messaging service interface.

Do not call this constructor directly. Instead, use
[`firebase.messaging()`](https://firebase.google.com/docs/reference/js/v8/firebase.messaging).

See [Set Up a JavaScript Firebase Cloud Messaging Client App](https://firebase.google.com/docs/cloud-messaging/js/client) for a full guide on how to use the
Firebase Messaging service.

## Index

### Methods

- [deleteToken](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.Messaging#deletetoken)
- [getToken](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.Messaging#gettoken)
- [onBackgroundMessage](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.Messaging#onbackgroundmessage)
- [onMessage](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.Messaging#onmessage)

## Methods

### deleteToken

- deleteToken ( ) : Promise \< boolean \>
- Deletes the registration token associated with this messaging instance and unsubscribes the
  messaging instance from the push subscription.

  #### Returns Promise\<boolean\>

  The promise resolves when the token has been successfully deleted.

### getToken

- getToken ( options ? : { serviceWorkerRegistration ?: ServiceWorkerRegistration ; vapidKey ?: string } ) : Promise \< string \>
- Subscribes the messaging instance to push notifications. Returns an FCM registration token
  that can be used to send push messages to that messaging instance.

  If a notification permission isn't already granted, this method asks the user for permission.
  The returned promise rejects if the user does not allow the app to show notifications.

  #### Parameters

  -

    ##### Optional options: { serviceWorkerRegistration?: ServiceWorkerRegistration; vapidKey?: string }

    -

      ##### Optional serviceWorkerRegistration?: ServiceWorkerRegistration

      The service worker registration for receiving push
      messaging. If the registration is not provided explicitly, you need to have a
      `firebase-messaging-sw.js` at your root location. See
      [Access the registration token](https://firebase.google.com/docs/cloud-messaging/js/client#access_the_registration_token)
      for more details.
    -

      ##### Optional vapidKey?: string

      The public server key provided to push services. It is used to
      authenticate the push subscribers to receive push messages only from sending servers that
      hold the corresponding private key. If it is not provided, a default VAPID key is used. Note
      that some push services (Chrome Push Service) require a non-default VAPID key. Therefore, it
      is recommended to generate and import a VAPID key for your project with
      [Configure Web Credentials with FCM](https://firebase.google.com/docs/cloud-messaging/js/client#configure_web_credentials_with_fcm).
      See
      [The Web Push Protocol](https://developers.google.com/web/fundamentals/push-notifications/web-push-protocol)
      for details on web push services.}

  #### Returns Promise\<string\>

  The promise resolves with an FCM registration token.

### onBackgroundMessage

- onBackgroundMessage ( nextOrObserver : firebase.NextFn \< [MessagePayload](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.MessagePayload) \> \| Observer \< [MessagePayload](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.MessagePayload) \> ) : firebase.Unsubscribe
- Called when a message is received while the app is in the background. An app is considered to
  be in the background if no active window is displayed.

  #### Parameters

  -

    ##### nextOrObserver: firebase.NextFn\<[MessagePayload](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.MessagePayload)\> \| Observer\<[MessagePayload](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.MessagePayload)\>

  #### Returns firebase.Unsubscribe

  To stop listening for messages execute this returned function

### onMessage

- onMessage ( nextOrObserver : firebase.NextFn \< any \> \| Observer \< any \> ) : firebase.Unsubscribe
- When a push message is received and the user is currently on a page for your origin, the
  message is passed to the page and an `onMessage()` event is dispatched with the payload of
  the push message.

  #### Parameters

  -

    ##### nextOrObserver: firebase.NextFn\<any\> \| Observer\<any\>

  #### Returns firebase.Unsubscribe

To stop listening for messages execute this returned function.