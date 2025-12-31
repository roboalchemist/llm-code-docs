# Source: https://firebase.google.com/docs/reference/js/messaging_.md.txt

# @firebase/messaging

## Functions

|                                                       Function                                                        |                                                                                                                                                                                                                                                                          Description                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **function(app, ...)**                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [getMessaging(app)](https://firebase.google.com/docs/reference/js/messaging_.md#getmessaging_cf608e1)                 | Retrieves a Firebase Cloud Messaging instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **function(messaging, ...)**                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [deleteToken(messaging)](https://firebase.google.com/docs/reference/js/messaging_.md#deletetoken_3fae4b1)             | Deletes the registration token associated with this [Messaging](https://firebase.google.com/docs/reference/js/messaging_.messaging.md#messaging_interface) instance and unsubscribes the [Messaging](https://firebase.google.com/docs/reference/js/messaging_.messaging.md#messaging_interface) instance from the push subscription.                                                                                                                                                                                                                          |
| [getToken(messaging, options)](https://firebase.google.com/docs/reference/js/messaging_.md#gettoken_b538f38)          | Subscribes the [Messaging](https://firebase.google.com/docs/reference/js/messaging_.messaging.md#messaging_interface) instance to push notifications. Returns a Firebase Cloud Messaging registration token that can be used to send push messages to that [Messaging](https://firebase.google.com/docs/reference/js/messaging_.messaging.md#messaging_interface) instance.If notification permission isn't already granted, this method asks the user for permission. The returned promise rejects if the user does not allow the app to show notifications. |
| [onMessage(messaging, nextOrObserver)](https://firebase.google.com/docs/reference/js/messaging_.md#onmessage_b9887da) | When a push message is received and the user is currently on a page for your origin, the message is passed to the page and an `onMessage()` event is dispatched with the payload of the push message.                                                                                                                                                                                                                                                                                                                                                         |
| **function()**                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [isSupported()](https://firebase.google.com/docs/reference/js/messaging_.md#issupported)                              | Checks if all required APIs exist in the browser.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## Interfaces

|                                                              Interface                                                               |                                                                                                                                                                                                           Description                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FcmOptions](https://firebase.google.com/docs/reference/js/messaging_.fcmoptions.md#fcmoptions_interface)                            | Options for features provided by the FCM SDK for Web. See [WebpushFcmOptions](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#webpushfcmoptions).                                                                                                                                                                                                                                                       |
| [GetTokenOptions](https://firebase.google.com/docs/reference/js/messaging_.gettokenoptions.md#gettokenoptions_interface)             | Options for [getToken()](https://firebase.google.com/docs/reference/js/messaging_.md#gettoken_b538f38).                                                                                                                                                                                                                                                                                                                          |
| [MessagePayload](https://firebase.google.com/docs/reference/js/messaging_.messagepayload.md#messagepayload_interface)                | Message payload that contains the notification payload that is represented with [NotificationPayload](https://firebase.google.com/docs/reference/js/messaging_.notificationpayload.md#notificationpayload_interface) and the data payload that contains an arbitrary number of key-value pairs sent by developers through the [Send API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#notification). |
| [Messaging](https://firebase.google.com/docs/reference/js/messaging_.messaging.md#messaging_interface)                               | Public interface of the Firebase Cloud Messaging SDK.                                                                                                                                                                                                                                                                                                                                                                            |
| [NotificationPayload](https://firebase.google.com/docs/reference/js/messaging_.notificationpayload.md#notificationpayload_interface) | Display notification details. Details are sent through the [Send API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#notification).                                                                                                                                                                                                                                                                    |

## function(app, ...)

### getMessaging(app)

Retrieves a Firebase Cloud Messaging instance.

**Signature:**  

    export declare function getMessagingInWindow(app?: FirebaseApp): Messaging;

#### Parameters

| Parameter |                                                 Type                                                  | Description |
|-----------|-------------------------------------------------------------------------------------------------------|-------------|
| app       | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) |             |

**Returns:**

[Messaging](https://firebase.google.com/docs/reference/js/messaging_.messaging.md#messaging_interface)

The Firebase Cloud Messaging instance associated with the provided firebase app.

## function(messaging, ...)

### deleteToken(messaging)

Deletes the registration token associated with this [Messaging](https://firebase.google.com/docs/reference/js/messaging_.messaging.md#messaging_interface) instance and unsubscribes the [Messaging](https://firebase.google.com/docs/reference/js/messaging_.messaging.md#messaging_interface) instance from the push subscription.

**Signature:**  

    export declare function deleteToken(messaging: Messaging): Promise<boolean>;

#### Parameters

| Parameter |                                                  Type                                                  |                                                     Description                                                      |
|-----------|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| messaging | [Messaging](https://firebase.google.com/docs/reference/js/messaging_.messaging.md#messaging_interface) | The [Messaging](https://firebase.google.com/docs/reference/js/messaging_.messaging.md#messaging_interface) instance. |

**Returns:**

Promise\<boolean\>

The promise resolves when the token has been successfully deleted.

### getToken(messaging, options)

Subscribes the [Messaging](https://firebase.google.com/docs/reference/js/messaging_.messaging.md#messaging_interface) instance to push notifications. Returns a Firebase Cloud Messaging registration token that can be used to send push messages to that [Messaging](https://firebase.google.com/docs/reference/js/messaging_.messaging.md#messaging_interface) instance.

If notification permission isn't already granted, this method asks the user for permission. The returned promise rejects if the user does not allow the app to show notifications.

**Signature:**  

    export declare function getToken(messaging: Messaging, options?: GetTokenOptions): Promise<string>;

#### Parameters

| Parameter |                                                           Type                                                           |                                                     Description                                                      |
|-----------|--------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| messaging | [Messaging](https://firebase.google.com/docs/reference/js/messaging_.messaging.md#messaging_interface)                   | The [Messaging](https://firebase.google.com/docs/reference/js/messaging_.messaging.md#messaging_interface) instance. |
| options   | [GetTokenOptions](https://firebase.google.com/docs/reference/js/messaging_.gettokenoptions.md#gettokenoptions_interface) | Provides an optional vapid key and an optional service worker registration.                                          |

**Returns:**

Promise\<string\>

The promise resolves with an FCM registration token.

### onMessage(messaging, nextOrObserver)

When a push message is received and the user is currently on a page for your origin, the message is passed to the page and an `onMessage()` event is dispatched with the payload of the push message.

**Signature:**  

    export declare function onMessage(messaging: Messaging, nextOrObserver: NextFn<MessagePayload> | Observer<MessagePayload>): Unsubscribe;

#### Parameters

|   Parameter    |                                                                                                                                                                                                           Type                                                                                                                                                                                                            |                                                               Description                                                                |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| messaging      | [Messaging](https://firebase.google.com/docs/reference/js/messaging_.messaging.md#messaging_interface)                                                                                                                                                                                                                                                                                                                    | The [Messaging](https://firebase.google.com/docs/reference/js/messaging_.messaging.md#messaging_interface) instance.                     |
| nextOrObserver | [NextFn](https://firebase.google.com/docs/reference/js/util.md#nextfn)\<[MessagePayload](https://firebase.google.com/docs/reference/js/messaging_.messagepayload.md#messagepayload_interface)\> \| [Observer](https://firebase.google.com/docs/reference/js/util.observer.md#observer_interface)\<[MessagePayload](https://firebase.google.com/docs/reference/js/messaging_.messagepayload.md#messagepayload_interface)\> | This function, or observer object with `next` defined, is called when a message is received and the user is currently viewing your page. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/util.md#unsubscribe)

To stop listening for messages execute this returned function.

## function()

### isSupported()

Checks if all required APIs exist in the browser.

**Signature:**  

    export declare function isWindowSupported(): Promise<boolean>;

**Returns:**

Promise\<boolean\>

a Promise that resolves to a boolean.