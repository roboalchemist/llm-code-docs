# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingtopicresponse.md.txt

# MessagingTopicResponse interface

Interface representing the server response from the legacy [Messaging.sendToTopic()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messaging.md#messagingsendtotopic) method.

See [Send to a topic](https://firebase.google.com/docs/cloud-messaging/admin/send-messages#send_to_a_topic) for code samples and detailed documentation.

**Signature:**  

    export interface MessagingTopicResponse 

## Properties

|                                                                       Property                                                                        |  Type  |                                                   Description                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------|
| [messageId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingtopicresponse.md#messagingtopicresponsemessageid) | number | The message ID for a successfully received request which FCM will attempt to deliver to all subscribed devices. |

## MessagingTopicResponse.messageId

The message ID for a successfully received request which FCM will attempt to deliver to all subscribed devices.

**Signature:**  

    messageId: number;