# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingdeviceresult.md.txt

# MessagingDeviceResult interface

> | **Warning:** This API is now obsolete.
>
> Returned by , which is also deprecated.

Individual status response payload from single devices

**Signature:**  

    export interface MessagingDeviceResult 

## Properties

|                                                                                       Property                                                                                        |     Type      |                                                                                                      Description                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [canonicalRegistrationToken](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingdeviceresult.md#messagingdeviceresultcanonicalregistrationtoken) | string        | The canonical registration token for the client app that the message was processed and sent to. You should use this value as the registration token for future requests. Otherwise, future messages might be rejected. |
| [error](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingdeviceresult.md#messagingdeviceresulterror)                                           | FirebaseError | The error that occurred when processing the message for the recipient.                                                                                                                                                 |
| [messageId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingdeviceresult.md#messagingdeviceresultmessageid)                                   | string        | A unique ID for the successfully processed message.                                                                                                                                                                    |

## MessagingDeviceResult.canonicalRegistrationToken

The canonical registration token for the client app that the message was processed and sent to. You should use this value as the registration token for future requests. Otherwise, future messages might be rejected.

**Signature:**  

    canonicalRegistrationToken?: string;

## MessagingDeviceResult.error

The error that occurred when processing the message for the recipient.

**Signature:**  

    error?: FirebaseError;

## MessagingDeviceResult.messageId

A unique ID for the successfully processed message.

**Signature:**  

    messageId?: string;