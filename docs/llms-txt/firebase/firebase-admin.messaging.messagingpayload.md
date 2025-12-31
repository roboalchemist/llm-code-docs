# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingpayload.md.txt

# MessagingPayload interface

Interface representing a Firebase Cloud Messaging message payload. One or both of the `data` and `notification` keys are required.

See [Build send requests](https://firebase.google.com/docs/cloud-messaging/send-message) for code samples and detailed documentation.

**Signature:**  

    export interface MessagingPayload 

## Properties

|                                                                    Property                                                                     |                                                                                      Type                                                                                       |            Description            |
|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| [data](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingpayload.md#messagingpayloaddata)                 | [DataMessagePayload](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.datamessagepayload.md#datamessagepayload_interface)                         | The data message payload.         |
| [notification](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingpayload.md#messagingpayloadnotification) | [NotificationMessagePayload](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.notificationmessagepayload.md#notificationmessagepayload_interface) | The notification message payload. |

## MessagingPayload.data

The data message payload.

**Signature:**  

    data?: DataMessagePayload;

## MessagingPayload.notification

The notification message payload.

**Signature:**  

    notification?: NotificationMessagePayload;