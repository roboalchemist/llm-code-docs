# Source: https://firebase.google.com/docs/reference/js/v8/firebase.messaging.md.txt

# messaging | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- messaging

The Messaging SDK does not work in a Node.js environment.

### Callable

- messaging ( app ? : [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App) ) : [Messaging](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.Messaging)
- Gets the [`Messaging`](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.Messaging) service for the
  default app or a given app.

  `firebase.messaging()` can be called with no arguments to access the default
  app's [`Messaging`](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.Messaging) service or as
  `firebase.messaging(app)` to access the
  [`Messaging`](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.Messaging) service associated with a
  specific app.

  Calling `firebase.messaging()` in a service worker results in Firebase
  generating notifications if the push message payload has a `notification`
  parameter.

  The Messaging SDK does not work in a Node.js environment.

  example
  :

          // Get the Messaging service for the default app
          var defaultMessaging = firebase.messaging();


  example
  :

          // Get the Messaging service for a given app
          var otherMessaging = firebase.messaging(otherApp);


  namespace
  :

  #### Parameters

  -

    ##### Optional app: [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App)

    The app to create a Messaging service for.
    If not passed, uses the default app.

  #### Returns [Messaging](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.Messaging)

## Index

### Interfaces

- [FcmOptions](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.FcmOptions)
- [MessagePayload](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.MessagePayload)
- [Messaging](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.Messaging)
- [NotificationPayload](https://firebase.google.com/docs/reference/js/v8/firebase.messaging.NotificationPayload)

### Functions

- [isSupported](https://firebase.google.com/docs/reference/js/v8/firebase.messaging#issupported)

## Functions

### isSupported

- isSupported ( ) : boolean
-

  #### Returns boolean