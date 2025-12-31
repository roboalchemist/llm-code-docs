# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.sendresponse.md.txt

# SendResponse interface

Interface representing the status of an individual message that was sent as part of a batch request.

**Signature:**  

    export interface SendResponse 

## Properties

|                                                             Property                                                              |     Type      |                                                                                               Description                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [error](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.sendresponse.md#sendresponseerror)         | FirebaseError | An error, if the message was not handed off to FCM successfully.                                                                                                                                        |
| [messageId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.sendresponse.md#sendresponsemessageid) | string        | A unique message ID string, if the message was handed off to FCM for delivery.                                                                                                                          |
| [success](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.sendresponse.md#sendresponsesuccess)     | boolean       | A boolean indicating if the message was successfully handed off to FCM or not. When true, the `messageId` attribute is guaranteed to be set. When false, the `error` attribute is guaranteed to be set. |

## SendResponse.error

An error, if the message was not handed off to FCM successfully.

**Signature:**  

    error?: FirebaseError;

## SendResponse.messageId

A unique message ID string, if the message was handed off to FCM for delivery.

**Signature:**  

    messageId?: string;

## SendResponse.success

A boolean indicating if the message was successfully handed off to FCM or not. When true, the `messageId` attribute is guaranteed to be set. When false, the `error` attribute is guaranteed to be set.

**Signature:**  

    success: boolean;