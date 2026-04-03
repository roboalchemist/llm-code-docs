# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingdevicesresponse.md.txt

# MessagingDevicesResponse interface

> | **Warning:** This API is now obsolete.
>
> Returned by [Messaging.sendToDevice()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messaging.md#messagingsendtodevice), which is also deprecated.

Interface representing the status of a message sent to an individual device via the FCM legacy APIs.

See [Send to individual devices](https://firebase.google.com/docs/cloud-messaging/admin/send-messages#send_to_individual_devices) for code samples and detailed documentation.

**Signature:**  

    export interface MessagingDevicesResponse 

## Properties

|                                                                                               Property                                                                                                |                                                                                 Type                                                                                 | Description |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [canonicalRegistrationTokenCount](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingdevicesresponse.md#messagingdevicesresponsecanonicalregistrationtokencount) | number                                                                                                                                                               |             |
| [failureCount](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingdevicesresponse.md#messagingdevicesresponsefailurecount)                                       | number                                                                                                                                                               |             |
| [multicastId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingdevicesresponse.md#messagingdevicesresponsemulticastid)                                         | number                                                                                                                                                               |             |
| [results](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingdevicesresponse.md#messagingdevicesresponseresults)                                                 | [MessagingDeviceResult](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingdeviceresult.md#messagingdeviceresult_interface)\[\] |             |
| [successCount](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingdevicesresponse.md#messagingdevicesresponsesuccesscount)                                       | number                                                                                                                                                               |             |

## MessagingDevicesResponse.canonicalRegistrationTokenCount

**Signature:**  

    canonicalRegistrationTokenCount: number;

## MessagingDevicesResponse.failureCount

**Signature:**  

    failureCount: number;

## MessagingDevicesResponse.multicastId

**Signature:**  

    multicastId: number;

## MessagingDevicesResponse.results

**Signature:**  

    results: MessagingDeviceResult[];

## MessagingDevicesResponse.successCount

**Signature:**  

    successCount: number;