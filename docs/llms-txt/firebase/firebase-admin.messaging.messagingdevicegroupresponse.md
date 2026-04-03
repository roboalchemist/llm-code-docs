# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingdevicegroupresponse.md.txt

# MessagingDeviceGroupResponse interface

> | **Warning:** This API is now obsolete.
>
> Returned by [Messaging.sendToDeviceGroup()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messaging.md#messagingsendtodevicegroup), which is also deprecated.

Interface representing the server response from the [Messaging.sendToDeviceGroup()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messaging.md#messagingsendtodevicegroup) method.

See [Send messages to device groups](https://firebase.google.com/docs/cloud-messaging/send-message?authuser=0#send_messages_to_device_groups) for code samples and detailed documentation.

**Signature:**  

    export interface MessagingDeviceGroupResponse 

## Properties

|                                                                                            Property                                                                                             |    Type    |                                 Description                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|------------------------------------------------------------------------------|
| [failedRegistrationTokens](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingdevicegroupresponse.md#messagingdevicegroupresponsefailedregistrationtokens) | string\[\] | An array of registration tokens that failed to receive the message.          |
| [failureCount](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingdevicegroupresponse.md#messagingdevicegroupresponsefailurecount)                         | number     | The number of messages that could not be processed and resulted in an error. |
| [successCount](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingdevicegroupresponse.md#messagingdevicegroupresponsesuccesscount)                         | number     | The number of messages that could not be processed and resulted in an error. |

## MessagingDeviceGroupResponse.failedRegistrationTokens

An array of registration tokens that failed to receive the message.

**Signature:**  

    failedRegistrationTokens: string[];

## MessagingDeviceGroupResponse.failureCount

The number of messages that could not be processed and resulted in an error.

**Signature:**  

    failureCount: number;

## MessagingDeviceGroupResponse.successCount

The number of messages that could not be processed and resulted in an error.

**Signature:**  

    successCount: number;