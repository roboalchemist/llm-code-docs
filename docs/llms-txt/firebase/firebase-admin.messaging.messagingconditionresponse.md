# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingconditionresponse.md.txt

# MessagingConditionResponse interface

Interface representing the server response from the legacy [Messaging.sendToCondition()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messaging.md#messagingsendtocondition) method.

See [Send to a condition](https://firebase.google.com/docs/cloud-messaging/admin/send-messages#send_to_a_condition) for code samples and detailed documentation.

**Signature:**  

    export interface MessagingConditionResponse 

## Properties

|                                                                           Property                                                                            |  Type  |                                                   Description                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------|
| [messageId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingconditionresponse.md#messagingconditionresponsemessageid) | number | The message ID for a successfully received request which FCM will attempt to deliver to all subscribed devices. |

## MessagingConditionResponse.messageId

The message ID for a successfully received request which FCM will attempt to deliver to all subscribed devices.

**Signature:**  

    messageId: number;