# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.batchresponse.md.txt

# BatchResponse interface

Interface representing the server response from the [Messaging.sendEach()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messaging.md#messagingsendeach) and [Messaging.sendEachForMulticast()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messaging.md#messagingsendeachformulticast) methods.

**Signature:**  

    export interface BatchResponse 

## Properties

|                                                                 Property                                                                  |                                                                   Type                                                                    |                              Description                              |
|-------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [failureCount](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.batchresponse.md#batchresponsefailurecount) | number                                                                                                                                    | The number of messages that resulted in errors when sending.          |
| [responses](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.batchresponse.md#batchresponseresponses)       | [SendResponse](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.sendresponse.md#sendresponse_interface)\[\] | An array of responses, each corresponding to a message.               |
| [successCount](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.batchresponse.md#batchresponsesuccesscount) | number                                                                                                                                    | The number of messages that were successfully handed off for sending. |

## BatchResponse.failureCount

The number of messages that resulted in errors when sending.

**Signature:**  

    failureCount: number;

## BatchResponse.responses

An array of responses, each corresponding to a message.

**Signature:**  

    responses: SendResponse[];

## BatchResponse.successCount

The number of messages that were successfully handed off for sending.

**Signature:**  

    successCount: number;