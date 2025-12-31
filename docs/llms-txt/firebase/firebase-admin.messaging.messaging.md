# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messaging.md.txt

# Messaging class

Messaging service bound to the provided app.

**Signature:**  

    export declare class Messaging 

## Properties

|                                                    Property                                                     | Modifiers | Type |                                                                            Description                                                                             |
|-----------------------------------------------------------------------------------------------------------------|-----------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [app](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messaging.md#messagingapp) |           | App  | The [App](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.app.md#app_interface) associated with the current `Messaging` service instance. |

## Methods

|                                                                                       Method                                                                                        | Modifiers |                                                                                                                                                                                                                                                                                                                                  Description                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [enableLegacyHttpTransport()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messaging.md#messagingenablelegacyhttptransport)                       |           | Enables the use of legacy HTTP/1.1 transport for `sendEach()` and `sendEachForMulticast()`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [send(message, dryRun)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messaging.md#messagingsend)                                                  |           | Sends the given message via FCM.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [sendEach(messages, dryRun)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messaging.md#messagingsendeach)                                         |           | Sends each message in the given array via Firebase Cloud Messaging.This method makes a single RPC call for each message in the given array.The responses list obtained from the return value corresponds to the order of `messages`. An error from this method or a `BatchResponse` with all failures indicates a total failure, meaning that none of the messages in the list could be sent. Partial failures or no failures are only indicated by a `BatchResponse` return value.                                                                                                                                                                                            |
| [sendEachForMulticast(message, dryRun)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messaging.md#messagingsendeachformulticast)                  |           | Sends the given multicast message to all the FCM registration tokens specified in it.This method uses the [Messaging.sendEach()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messaging.md#messagingsendeach) API under the hood to send the given message to all the target recipients. The responses list obtained from the return value corresponds to the order of tokens in the `MulticastMessage`. An error from this method or a `BatchResponse` with all failures indicates a total failure, meaning that the messages in the list could be sent. Partial failures or failures are only indicated by a `BatchResponse` return value. |
| [subscribeToTopic(registrationTokenOrTokens, topic)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messaging.md#messagingsubscribetotopic)         |           | Subscribes a device to an FCM topic.See [Subscribe to a topic](https://firebase.google.com/docs/cloud-messaging/manage-topics#suscribe_and_unsubscribe_using_the) for code samples and detailed documentation. Optionally, you can provide an array of tokens to subscribe multiple devices.                                                                                                                                                                                                                                                                                                                                                                                   |
| [unsubscribeFromTopic(registrationTokenOrTokens, topic)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messaging.md#messagingunsubscribefromtopic) |           | Unsubscribes a device from an FCM topic.See [Unsubscribe from a topic](https://firebase.google.com/docs/cloud-messaging/admin/manage-topic-subscriptions#unsubscribe_from_a_topic) for code samples and detailed documentation. Optionally, you can provide an array of tokens to unsubscribe multiple devices.                                                                                                                                                                                                                                                                                                                                                                |

## Messaging.app

The [App](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.app.md#app_interface) associated with the current `Messaging` service instance.

**Signature:**  

    get app(): App;

### Example

    var app = messaging.app;

## Messaging.enableLegacyHttpTransport()

> | **Warning:** This API is now obsolete.
>
> This will be removed when the HTTP/2 transport implementation reaches the same stability as the legacy HTTP/1.1 implementation.

Enables the use of legacy HTTP/1.1 transport for `sendEach()` and `sendEachForMulticast()`.

**Signature:**  

    enableLegacyHttpTransport(): void;

**Returns:**

void

### Example

    const messaging = getMessaging(app);
    messaging.enableLegacyTransport();
    messaging.sendEach(messages);

## Messaging.send()

Sends the given message via FCM.

**Signature:**  

    send(message: Message, dryRun?: boolean): Promise<string>;

### Parameters

| Parameter |                                                 Type                                                 |                            Description                             |
|-----------|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| message   | [Message](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.md#message) | The message payload.                                               |
| dryRun    | boolean                                                                                              | Whether to send the message in the dry-run (validation only) mode. |

**Returns:**

Promise\<string\>

A promise fulfilled with a unique message ID string after the message has been successfully handed off to the FCM service for delivery.

## Messaging.sendEach()

Sends each message in the given array via Firebase Cloud Messaging.

This method makes a single RPC call for each message in the given array.

The responses list obtained from the return value corresponds to the order of `messages`. An error from this method or a `BatchResponse` with all failures indicates a total failure, meaning that none of the messages in the list could be sent. Partial failures or no failures are only indicated by a `BatchResponse` return value.

**Signature:**  

    sendEach(messages: Message[], dryRun?: boolean): Promise<BatchResponse>;

### Parameters

| Parameter |                                                   Type                                                   |                             Description                             |
|-----------|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| messages  | [Message](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.md#message)\[\] | A non-empty array containing up to 500 messages.                    |
| dryRun    | boolean                                                                                                  | Whether to send the messages in the dry-run (validation only) mode. |

**Returns:**

Promise\<[BatchResponse](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.batchresponse.md#batchresponse_interface)\>

A Promise fulfilled with an object representing the result of the send operation.

## Messaging.sendEachForMulticast()

Sends the given multicast message to all the FCM registration tokens specified in it.

This method uses the [Messaging.sendEach()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messaging.md#messagingsendeach) API under the hood to send the given message to all the target recipients. The responses list obtained from the return value corresponds to the order of tokens in the `MulticastMessage`. An error from this method or a `BatchResponse` with all failures indicates a total failure, meaning that the messages in the list could be sent. Partial failures or failures are only indicated by a `BatchResponse` return value.

**Signature:**  

    sendEachForMulticast(message: MulticastMessage, dryRun?: boolean): Promise<BatchResponse>;

### Parameters

| Parameter |                                                                       Type                                                                        |                            Description                             |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| message   | [MulticastMessage](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.multicastmessage.md#multicastmessage_interface) | A multicast message containing up to 500 tokens.                   |
| dryRun    | boolean                                                                                                                                           | Whether to send the message in the dry-run (validation only) mode. |

**Returns:**

Promise\<[BatchResponse](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.batchresponse.md#batchresponse_interface)\>

A Promise fulfilled with an object representing the result of the send operation.

## Messaging.subscribeToTopic()

Subscribes a device to an FCM topic.

See [Subscribe to a topic](https://firebase.google.com/docs/cloud-messaging/manage-topics#suscribe_and_unsubscribe_using_the) for code samples and detailed documentation. Optionally, you can provide an array of tokens to subscribe multiple devices.

**Signature:**  

    subscribeToTopic(registrationTokenOrTokens: string | string[], topic: string): Promise<MessagingTopicManagementResponse>;

### Parameters

|         Parameter         |         Type         |           Description            |
|---------------------------|----------------------|----------------------------------|
| registrationTokenOrTokens | string \| string\[\] |                                  |
| topic                     | string               | The topic to which to subscribe. |

**Returns:**

Promise\<[MessagingTopicManagementResponse](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingtopicmanagementresponse.md#messagingtopicmanagementresponse_interface)\>

A promise fulfilled with the server's response after the device has been subscribed to the topic.

## Messaging.unsubscribeFromTopic()

Unsubscribes a device from an FCM topic.

See [Unsubscribe from a topic](https://firebase.google.com/docs/cloud-messaging/admin/manage-topic-subscriptions#unsubscribe_from_a_topic) for code samples and detailed documentation. Optionally, you can provide an array of tokens to unsubscribe multiple devices.

**Signature:**  

    unsubscribeFromTopic(registrationTokenOrTokens: string | string[], topic: string): Promise<MessagingTopicManagementResponse>;

### Parameters

|         Parameter         |         Type         |             Description              |
|---------------------------|----------------------|--------------------------------------|
| registrationTokenOrTokens | string \| string\[\] |                                      |
| topic                     | string               | The topic from which to unsubscribe. |

**Returns:**

Promise\<[MessagingTopicManagementResponse](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messagingtopicmanagementresponse.md#messagingtopicmanagementresponse_interface)\>

A promise fulfilled with the server's response after the device has been unsubscribed from the topic.