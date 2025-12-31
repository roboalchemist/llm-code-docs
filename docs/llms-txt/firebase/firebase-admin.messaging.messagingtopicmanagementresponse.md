# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingtopicmanagementresponse.md.txt

# MessagingTopicManagementResponse interface

Interface representing the server response from the [Messaging.subscribeToTopic()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messaging.md#messagingsubscribetotopic) and [Messaging.unsubscribeFromTopic()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messaging.md#messagingunsubscribefromtopic) methods.

See [Manage topics from the server](https://firebase.google.com/docs/cloud-messaging/manage-topics) for code samples and detailed documentation.

**Signature:**  

    export interface MessagingTopicManagementResponse 

## Properties

|                                                                                    Property                                                                                     |            Type             |                                                                                                                                                             Description                                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [errors](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingtopicmanagementresponse.md#messagingtopicmanagementresponseerrors)             | FirebaseArrayIndexError\[\] | An array of errors corresponding to the provided registration token(s). The length of this array will be equal to [MessagingTopicManagementResponse.failureCount](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingtopicmanagementresponse.md#messagingtopicmanagementresponsefailurecount). |
| [failureCount](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingtopicmanagementresponse.md#messagingtopicmanagementresponsefailurecount) | number                      | The number of registration tokens that could not be subscribed to the topic and resulted in an error.                                                                                                                                                                                                                               |
| [successCount](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingtopicmanagementresponse.md#messagingtopicmanagementresponsesuccesscount) | number                      | The number of registration tokens that were successfully subscribed to the topic.                                                                                                                                                                                                                                                   |

## MessagingTopicManagementResponse.errors

An array of errors corresponding to the provided registration token(s). The length of this array will be equal to [MessagingTopicManagementResponse.failureCount](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingtopicmanagementresponse.md#messagingtopicmanagementresponsefailurecount).

**Signature:**  

    errors: FirebaseArrayIndexError[];

## MessagingTopicManagementResponse.failureCount

The number of registration tokens that could not be subscribed to the topic and resulted in an error.

**Signature:**  

    failureCount: number;

## MessagingTopicManagementResponse.successCount

The number of registration tokens that were successfully subscribed to the topic.

**Signature:**  

    successCount: number;