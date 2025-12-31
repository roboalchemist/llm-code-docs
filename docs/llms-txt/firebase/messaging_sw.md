# Source: https://firebase.google.com/docs/reference/js/messaging_sw.md.txt

# @firebase/messaging/sw

## Functions

|                                                                                                  Function                                                                                                   |                                                                                                       Description                                                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **function(app, ...)**                                                                                                                                                                                      |                                                                                                                                                                                                                          |
| [getMessaging(app)](https://firebase.google.com/docs/reference/js/messaging_sw.md#getmessaging_cf608e1)                                                                                                     | Retrieves a Firebase Cloud Messaging instance.                                                                                                                                                                           |
| **function(messaging, ...)**                                                                                                                                                                                |                                                                                                                                                                                                                          |
| [experimentalSetDeliveryMetricsExportedToBigQueryEnabled(messaging, enable)](https://firebase.google.com/docs/reference/js/messaging_sw.md#experimentalsetdeliverymetricsexportedtobigqueryenabled_f3e53bd) | Enables or disables Firebase Cloud Messaging message delivery metrics export to BigQuery. By default, message delivery metrics are not exported to BigQuery. Use this method to enable or disable the export at runtime. |
| [onBackgroundMessage(messaging, nextOrObserver)](https://firebase.google.com/docs/reference/js/messaging_sw.md#onbackgroundmessage_b9887da)                                                                 | Called when a message is received while the app is in the background. An app is considered to be in the background if no active window is displayed.                                                                     |
| **function()**                                                                                                                                                                                              |                                                                                                                                                                                                                          |
| [isSupported()](https://firebase.google.com/docs/reference/js/messaging_sw.md#issupported)                                                                                                                  | Checks whether all required APIs exist within SW Context                                                                                                                                                                 |

## Interfaces

|                                                               Interface                                                                |                                                                                                                                                                                                           Description                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FcmOptions](https://firebase.google.com/docs/reference/js/messaging_sw.fcmoptions.md#fcmoptions_interface)                            | Options for features provided by the FCM SDK for Web. See [WebpushFcmOptions](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#webpushfcmoptions).                                                                                                                                                                                                                                                       |
| [GetTokenOptions](https://firebase.google.com/docs/reference/js/messaging_sw.gettokenoptions.md#gettokenoptions_interface)             | Options for [getToken()](https://firebase.google.com/docs/reference/js/messaging_.md#gettoken_b538f38).                                                                                                                                                                                                                                                                                                                          |
| [MessagePayload](https://firebase.google.com/docs/reference/js/messaging_sw.messagepayload.md#messagepayload_interface)                | Message payload that contains the notification payload that is represented with [NotificationPayload](https://firebase.google.com/docs/reference/js/messaging_.notificationpayload.md#notificationpayload_interface) and the data payload that contains an arbitrary number of key-value pairs sent by developers through the [Send API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#notification). |
| [Messaging](https://firebase.google.com/docs/reference/js/messaging_sw.messaging.md#messaging_interface)                               | Public interface of the Firebase Cloud Messaging SDK.                                                                                                                                                                                                                                                                                                                                                                            |
| [NotificationPayload](https://firebase.google.com/docs/reference/js/messaging_sw.notificationpayload.md#notificationpayload_interface) | Display notification details. Details are sent through the [Send API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#notification).                                                                                                                                                                                                                                                                    |

## function(app, ...)

### getMessaging(app)

Retrieves a Firebase Cloud Messaging instance.

**Signature:**  

    export declare function getMessagingInSw(app?: FirebaseApp): Messaging;

#### Parameters

| Parameter |                                                 Type                                                  | Description |
|-----------|-------------------------------------------------------------------------------------------------------|-------------|
| app       | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) |             |

**Returns:**

[Messaging](https://firebase.google.com/docs/reference/js/messaging_.messaging.md#messaging_interface)

The Firebase Cloud Messaging instance associated with the provided firebase app.

## function(messaging, ...)

### experimentalSetDeliveryMetricsExportedToBigQueryEnabled(messaging, enable)

Enables or disables Firebase Cloud Messaging message delivery metrics export to BigQuery. By default, message delivery metrics are not exported to BigQuery. Use this method to enable or disable the export at runtime.

**Signature:**  

    export declare function experimentalSetDeliveryMetricsExportedToBigQueryEnabled(messaging: Messaging, enable: boolean): void;

#### Parameters

| Parameter |                                                  Type                                                  |                                     Description                                      |
|-----------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| messaging | [Messaging](https://firebase.google.com/docs/reference/js/messaging_.messaging.md#messaging_interface) | The `FirebaseMessaging` instance.                                                    |
| enable    | boolean                                                                                                | Whether Firebase Cloud Messaging should export message delivery metrics to BigQuery. |

**Returns:**

void

### onBackgroundMessage(messaging, nextOrObserver)

Called when a message is received while the app is in the background. An app is considered to be in the background if no active window is displayed.

**Signature:**  

    export declare function onBackgroundMessage(messaging: Messaging, nextOrObserver: NextFn<MessagePayload> | Observer<MessagePayload>): Unsubscribe;

#### Parameters

|   Parameter    |                                                                                                                                                                                                           Type                                                                                                                                                                                                            |                                                               Description                                                               |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| messaging      | [Messaging](https://firebase.google.com/docs/reference/js/messaging_.messaging.md#messaging_interface)                                                                                                                                                                                                                                                                                                                    | The [Messaging](https://firebase.google.com/docs/reference/js/messaging_.messaging.md#messaging_interface) instance.                    |
| nextOrObserver | [NextFn](https://firebase.google.com/docs/reference/js/util.md#nextfn)\<[MessagePayload](https://firebase.google.com/docs/reference/js/messaging_.messagepayload.md#messagepayload_interface)\> \| [Observer](https://firebase.google.com/docs/reference/js/util.observer.md#observer_interface)\<[MessagePayload](https://firebase.google.com/docs/reference/js/messaging_.messagepayload.md#messagepayload_interface)\> | This function, or observer object with `next` defined, is called when a message is received and the app is currently in the background. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/util.md#unsubscribe)

To stop listening for messages execute this returned function

## function()

### isSupported()

Checks whether all required APIs exist within SW Context

**Signature:**  

    export declare function isSwSupported(): Promise<boolean>;

**Returns:**

Promise\<boolean\>

a Promise that resolves to a boolean.