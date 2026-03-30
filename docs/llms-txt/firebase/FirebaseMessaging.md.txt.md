# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging.md.txt

# FirebaseMessaging

public class **FirebaseMessaging** extends Object  
This class is the entry point for all server-side Firebase Cloud Messaging actions.

You can get an instance of FirebaseMessaging via `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#getInstance(com.google.firebase.FirebaseApp)`, and
then use it to send messages or manage FCM topic subscriptions.

### Public Method Summary

|---|---|
| static [FirebaseMessaging](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging) | [getInstance](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#getInstance())() Gets the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging` instance for the default `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp`. |
| synchronized static [FirebaseMessaging](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging) | [getInstance](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#getInstance(com.google.firebase.FirebaseApp))([FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) app) Gets the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging` instance for the specified `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp`. |
| String | [send](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#send(com.google.firebase.messaging.Message))([Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message) message) Sends the given `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message` via Firebase Cloud Messaging. |
| String | [send](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#send(com.google.firebase.messaging.Message, boolean))([Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message) message, boolean dryRun) Sends the given `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message` via Firebase Cloud Messaging. |
| [BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse) | [sendAll](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendAll(java.util.List<com.google.firebase.messaging.Message>))(List\<[Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message)\> messages) *This method is deprecated. Use `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEach(java.util.List<com.google.firebase.messaging.Message>)` instead.* |
| [BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse) | [sendAll](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendAll(java.util.List<com.google.firebase.messaging.Message>, boolean))(List\<[Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message)\> messages, boolean dryRun) *This method is deprecated. Use `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEach(java.util.List<com.google.firebase.messaging.Message>, boolean)` instead.* |
| ApiFuture\<[BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse)\> | [sendAllAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendAllAsync(java.util.List<com.google.firebase.messaging.Message>))(List\<[Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message)\> messages) *This method is deprecated. Use `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEachAsync(java.util.List<com.google.firebase.messaging.Message>)` instead.* |
| ApiFuture\<[BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse)\> | [sendAllAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendAllAsync(java.util.List<com.google.firebase.messaging.Message>, boolean))(List\<[Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message)\> messages, boolean dryRun) *This method is deprecated. Use `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEachAsync(java.util.List<com.google.firebase.messaging.Message>, boolean)` instead.* |
| ApiFuture\<String\> | [sendAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendAsync(com.google.firebase.messaging.Message, boolean))([Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message) message, boolean dryRun) Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#send(com.google.firebase.messaging.Message, boolean)` but performs the operation asynchronously. |
| ApiFuture\<String\> | [sendAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendAsync(com.google.firebase.messaging.Message))([Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message) message) Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#send(com.google.firebase.messaging.Message)` but performs the operation asynchronously. |
| [BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse) | [sendEach](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEach(java.util.List<com.google.firebase.messaging.Message>))(List\<[Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message)\> messages) Sends each message in the given list via Firebase Cloud Messaging. |
| [BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse) | [sendEach](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEach(java.util.List<com.google.firebase.messaging.Message>, boolean))(List\<[Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message)\> messages, boolean dryRun) Sends each message in the given list via Firebase Cloud Messaging. |
| ApiFuture\<[BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse)\> | [sendEachAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEachAsync(java.util.List<com.google.firebase.messaging.Message>))(List\<[Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message)\> messages) Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEach(java.util.List<com.google.firebase.messaging.Message>)` but performs the operation asynchronously. |
| ApiFuture\<[BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse)\> | [sendEachAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEachAsync(java.util.List<com.google.firebase.messaging.Message>, boolean))(List\<[Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message)\> messages, boolean dryRun) Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEach(java.util.List<com.google.firebase.messaging.Message>, boolean)` but performs the operation asynchronously. |
| [BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse) | [sendEachForMulticast](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEachForMulticast(com.google.firebase.messaging.MulticastMessage))([MulticastMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage) message) Sends the given multicast message to all the FCM registration tokens specified in it. |
| [BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse) | [sendEachForMulticast](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEachForMulticast(com.google.firebase.messaging.MulticastMessage, boolean))([MulticastMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage) message, boolean dryRun) Sends the given multicast message to all the FCM registration tokens specified in it. |
| ApiFuture\<[BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse)\> | [sendEachForMulticastAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEachForMulticastAsync(com.google.firebase.messaging.MulticastMessage))([MulticastMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage) message) Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEachForMulticast(com.google.firebase.messaging.MulticastMessage)` but performs the operation asynchronously. |
| ApiFuture\<[BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse)\> | [sendEachForMulticastAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEachForMulticastAsync(com.google.firebase.messaging.MulticastMessage, boolean))([MulticastMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage) message, boolean dryRun) Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEachForMulticast(com.google.firebase.messaging.MulticastMessage, boolean)` but performs the operation asynchronously. |
| [BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse) | [sendMulticast](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendMulticast(com.google.firebase.messaging.MulticastMessage, boolean))([MulticastMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage) message, boolean dryRun) *This method is deprecated. Use `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEachForMulticast(com.google.firebase.messaging.MulticastMessage, boolean)` instead.* |
| [BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse) | [sendMulticast](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendMulticast(com.google.firebase.messaging.MulticastMessage))([MulticastMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage) message) *This method is deprecated. Use `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEachForMulticast(com.google.firebase.messaging.MulticastMessage)` instead.* |
| ApiFuture\<[BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse)\> | [sendMulticastAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendMulticastAsync(com.google.firebase.messaging.MulticastMessage))([MulticastMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage) message) *This method is deprecated. Use `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEachForMulticastAsync(com.google.firebase.messaging.MulticastMessage)` instead.* |
| ApiFuture\<[BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse)\> | [sendMulticastAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendMulticastAsync(com.google.firebase.messaging.MulticastMessage, boolean))([MulticastMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage) message, boolean dryRun) *This method is deprecated. Use `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEachForMulticastAsync(com.google.firebase.messaging.MulticastMessage, boolean)` instead.* |
| [TopicManagementResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse) | [subscribeToTopic](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#subscribeToTopic(java.util.List<java.lang.String>, java.lang.String))(List\<String\> registrationTokens, String topic) Subscribes a list of registration tokens to a topic. |
| ApiFuture\<[TopicManagementResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse)\> | [subscribeToTopicAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#subscribeToTopicAsync(java.util.List<java.lang.String>, java.lang.String))(List\<String\> registrationTokens, String topic) Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#subscribeToTopic(java.util.List<java.lang.String>, java.lang.String)` but performs the operation asynchronously. |
| [TopicManagementResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse) | [unsubscribeFromTopic](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#unsubscribeFromTopic(java.util.List<java.lang.String>, java.lang.String))(List\<String\> registrationTokens, String topic) Unsubscribes a list of registration tokens from a topic. |
| ApiFuture\<[TopicManagementResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse)\> | [unsubscribeFromTopicAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#unsubscribeFromTopicAsync(java.util.List<java.lang.String>, java.lang.String))(List\<String\> registrationTokens, String topic) Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#unsubscribeFromTopic(java.util.List<java.lang.String>, java.lang.String)` but performs the operation asynchronously. |

### Inherited Method Summary

From class java.lang.Object

|---|---|
| Object | clone() |
| boolean | equals(Object arg0) |
| void | finalize() |
| final Class\<?\> | getClass() |
| int | hashCode() |
| final void | notify() |
| final void | notifyAll() |
| String | toString() |
| final void | wait(long arg0, int arg1) |
| final void | wait(long arg0) |
| final void | wait() |

## Public Methods

#### public static [FirebaseMessaging](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging)
**getInstance**
()

Gets the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging` instance for the default `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp`.

##### Returns

- The `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging` instance for the default `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp`.

#### public static synchronized [FirebaseMessaging](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging)
**getInstance**
([FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) app)

Gets the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging` instance for the specified `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp`.

##### Returns

- The `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging` instance for the specified `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp`.

#### public String
**send**
([Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message) message)

Sends the given `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message` via Firebase Cloud Messaging.

##### Parameters

| message | A non-null `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message` to be sent. |
|---|---|

##### Returns

- A message ID string.

##### Throws

| [FirebaseMessagingException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessagingException) | If an error occurs while handing the message off to FCM for delivery. |
|---|---|

#### public String
**send**
([Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message) message, boolean dryRun)

Sends the given `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message` via Firebase Cloud Messaging.

If the `dryRun` option is set to true, the message will not be actually sent. Instead
FCM performs all the necessary validations and emulates the send operation. The `dryRun`
option is useful for determining whether an FCM registration has been deleted. However, it
cannot be used to validate APNs tokens.

##### Parameters

| message | A non-null `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message` to be sent. |
| dryRun | a boolean indicating whether to perform a dry run (validation only) of the send. |
|---|---|

##### Returns

- A message ID string.

##### Throws

| [FirebaseMessagingException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessagingException) | If an error occurs while handing the message off to FCM for delivery. |
|---|---|

#### public [BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse)
**sendAll**
(List\<[Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message)\> messages)


**This method is deprecated.**   
Use `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEach(java.util.List<com.google.firebase.messaging.Message>)` instead.

Sends all the messages in the given list via Firebase Cloud Messaging. Employs batching to
send the entire list as a single RPC call. Compared to the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#send(com.google.firebase.messaging.Message)` method, this
is a significantly more efficient way to send multiple messages.

The responses list obtained by calling `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse#getResponses()` on the return
value corresponds to the order of input messages.

##### Parameters

| messages | A non-null, non-empty list containing up to 500 messages. |
|---|---|

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse` indicating the result of the operation.

##### Throws

| [FirebaseMessagingException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessagingException) | If an error occurs while handing the messages off to FCM for delivery. An exception here indicates a total failure, meaning that none of the messages in the list could be sent. Partial failures are indicated by a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse` return value. |
|---|---|

#### public [BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse)
**sendAll**
(List\<[Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message)\> messages, boolean dryRun)


**This method is deprecated.**   
Use `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEach(java.util.List<com.google.firebase.messaging.Message>, boolean)` instead.

Sends all the messages in the given list via Firebase Cloud Messaging. Employs batching to
send the entire list as a single RPC call. Compared to the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#send(com.google.firebase.messaging.Message)` method, this
is a significantly more efficient way to send multiple messages.

If the `dryRun` option is set to true, the message will not be actually sent. Instead
FCM performs all the necessary validations, and emulates the send operation. The `dryRun`
option is useful for determining whether an FCM registration has been deleted. But it cannot be
used to validate APNs tokens.

The responses list obtained by calling `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse#getResponses()` on the return
value corresponds to the order of input messages.

##### Parameters

| messages | A non-null, non-empty list containing up to 500 messages. |
| dryRun | A boolean indicating whether to perform a dry run (validation only) of the send. |
|---|---|

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse` indicating the result of the operation.

##### Throws

| [FirebaseMessagingException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessagingException) | If an error occurs while handing the messages off to FCM for delivery. An exception here indicates a total failure, meaning that none of the messages in the list could be sent. Partial failures are indicated by a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse` return value. |
|---|---|

#### public ApiFuture\<[BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse)\>
**sendAllAsync**
(List\<[Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message)\> messages)


**This method is deprecated.**   
Use `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEachAsync(java.util.List<com.google.firebase.messaging.Message>)` instead.

Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendAll(java.util.List<com.google.firebase.messaging.Message>)` but performs the operation asynchronously.

##### Parameters

| messages | A non-null, non-empty list containing up to 500 messages. |
|---|---|

##### Returns

- An `ApiFuture` that will complete with a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse` when the messages have been sent.

#### public ApiFuture\<[BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse)\>
**sendAllAsync**
(List\<[Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message)\> messages, boolean dryRun)


**This method is deprecated.**   
Use `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEachAsync(java.util.List<com.google.firebase.messaging.Message>, boolean)` instead.

Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendAll(java.util.List<com.google.firebase.messaging.Message>, boolean)` but performs the operation asynchronously.

##### Parameters

| messages | A non-null, non-empty list containing up to 500 messages. |
| dryRun | A boolean indicating whether to perform a dry run (validation only) of the send. |
|---|---|

##### Returns

- An `ApiFuture` that will complete with a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse` when the messages have been sent, or when the emulation has finished.

#### public ApiFuture\<String\>
**sendAsync**
([Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message) message, boolean dryRun)

Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#send(com.google.firebase.messaging.Message, boolean)` but performs the operation asynchronously.

##### Parameters

| message | A non-null `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message` to be sent. |
| dryRun | a boolean indicating whether to perform a dry run (validation only) of the send. |
|---|---|

##### Returns

- An `ApiFuture` that will complete with a message ID string when the message has been sent, or when the emulation has finished.

#### public ApiFuture\<String\>
**sendAsync**
([Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message) message)

Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#send(com.google.firebase.messaging.Message)` but performs the operation asynchronously.

##### Parameters

| message | A non-null `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message` to be sent. |
|---|---|

##### Returns

- An `ApiFuture` that will complete with a message ID string when the message has been sent.

#### public [BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse)
**sendEach**
(List\<[Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message)\> messages)

Sends each message in the given list via Firebase Cloud Messaging.
Unlike `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendAll(java.util.List<com.google.firebase.messaging.Message>)`, this method makes an HTTP call for each message in the
given array.

The list of responses obtained by calling `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse#getResponses()` on the return
value is in the same order as the input list.

##### Parameters

| messages | A non-null, non-empty list containing up to 500 messages. |
|---|---|

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse` indicating the result of the operation.

##### Throws

| [FirebaseMessagingException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessagingException) | If an error occurs while handing the messages off to FCM for delivery. An exception here or a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse` with all failures indicates a total failure, meaning that none of the messages in the list could be sent. Partial failures or no failures are only indicated by a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse`. |
|---|---|

#### public [BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse)
**sendEach**
(List\<[Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message)\> messages, boolean dryRun)

Sends each message in the given list via Firebase Cloud Messaging.
Unlike `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendAll(java.util.List<com.google.firebase.messaging.Message>)`, this method makes an HTTP call for each message in the
given array.

If the `dryRun` option is set to true, the message will not be actually sent. Instead
FCM performs all the necessary validations, and emulates the send operation. The `dryRun`
option is useful for determining whether an FCM registration has been deleted. But it cannot be
used to validate APNs tokens.

The list of responses obtained by calling `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse#getResponses()` on the return
value is in the same order as the input list.

##### Parameters

| messages | A non-null, non-empty list containing up to 500 messages. |
| dryRun | A boolean indicating whether to perform a dry run (validation only) of the send. |
|---|---|

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse` indicating the result of the operation.

##### Throws

| [FirebaseMessagingException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessagingException) | If an error occurs while handing the messages off to FCM for delivery. An exception here or a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse` with all failures indicates a total failure, meaning that none of the messages in the list could be sent. Partial failures or no failures are only indicated by a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse`. |
|---|---|

#### public ApiFuture\<[BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse)\>
**sendEachAsync**
(List\<[Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message)\> messages)

Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEach(java.util.List<com.google.firebase.messaging.Message>)` but performs the operation asynchronously.

##### Parameters

| messages | A non-null, non-empty list containing up to 500 messages. |
|---|---|

##### Returns

- An `ApiFuture` that will complete with a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse` when the messages have been sent.

#### public ApiFuture\<[BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse)\>
**sendEachAsync**
(List\<[Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message)\> messages, boolean dryRun)

Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEach(java.util.List<com.google.firebase.messaging.Message>, boolean)` but performs the operation asynchronously.

##### Parameters

| messages | A non-null, non-empty list containing up to 500 messages. |
| dryRun | A boolean indicating whether to perform a dry run (validation only) of the send. |
|---|---|

##### Returns

- An `ApiFuture` that will complete with a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse` when the messages have been sent.

#### public [BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse)
**sendEachForMulticast**
([MulticastMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage) message)

Sends the given multicast message to all the FCM registration tokens specified in it.

This method uses the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEach(java.util.List<com.google.firebase.messaging.Message>)` API under the hood to send the given
message to all the target recipients. The list of responses obtained by calling
`https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse#getResponses()` on the return value is in the same order as the
tokens in the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage`.

##### Parameters

| message | A non-null `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage` |
|---|---|

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse` indicating the result of the operation.

##### Throws

| [FirebaseMessagingException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessagingException) | If an error occurs while handing the messages off to FCM for delivery. An exception here or a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse` with all failures indicates a total failure, meaning that none of the messages in the list could be sent. Partial failures or no failures are only indicated by a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse`. |
|---|---|

#### public [BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse)
**sendEachForMulticast**
([MulticastMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage) message, boolean dryRun)

Sends the given multicast message to all the FCM registration tokens specified in it.

If the `dryRun` option is set to true, the message will not be actually sent. Instead
FCM performs all the necessary validations, and emulates the send operation. The `dryRun`
option is useful for determining whether an FCM registration has been deleted. But it cannot be
used to validate APNs tokens.

This method uses the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEach(java.util.List<com.google.firebase.messaging.Message>)` API under the hood to send the given
message to all the target recipients. The list of responses obtained by calling
`https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse#getResponses()` on the return value is in the same order as the
tokens in the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage`.

##### Parameters

| message | A non-null `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage`. |
| dryRun | A boolean indicating whether to perform a dry run (validation only) of the send. |
|---|---|

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse` indicating the result of the operation.

##### Throws

| [FirebaseMessagingException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessagingException) | If an error occurs while handing the messages off to FCM for delivery. An exception here or a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse` with all failures indicates a total failure, meaning that none of the messages in the list could be sent. Partial failures or no failures are only indicated by a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse`. |
|---|---|

#### public ApiFuture\<[BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse)\>
**sendEachForMulticastAsync**
([MulticastMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage) message)

Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEachForMulticast(com.google.firebase.messaging.MulticastMessage)` but performs the operation
asynchronously.

##### Parameters

| message | A non-null `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage`. |
|---|---|

##### Returns

- An `ApiFuture` that will complete with a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse` when the messages have been sent.

#### public ApiFuture\<[BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse)\>
**sendEachForMulticastAsync**
([MulticastMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage) message, boolean dryRun)

Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEachForMulticast(com.google.firebase.messaging.MulticastMessage, boolean)` but performs the operation
asynchronously.

##### Parameters

| message | A non-null `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage`. |
| dryRun | A boolean indicating whether to perform a dry run (validation only) of the send. |
|---|---|

##### Returns

- An `ApiFuture` that will complete with a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse` when the messages have been sent.

#### public [BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse)
**sendMulticast**
([MulticastMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage) message, boolean dryRun)


**This method is deprecated.**   
Use `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEachForMulticast(com.google.firebase.messaging.MulticastMessage, boolean)` instead.

Sends the given multicast message to all the FCM registration tokens specified in it.

If the `dryRun` option is set to true, the message will not be actually sent. Instead
FCM performs all the necessary validations, and emulates the send operation. The `dryRun`
option is useful for determining whether an FCM registration has been deleted. But it cannot be
used to validate APNs tokens.

This method uses the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendAll(java.util.List<com.google.firebase.messaging.Message>)` API under the hood to send the given
message to all the target recipients. The responses list obtained by calling
`https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse#getResponses()` on the return value corresponds to the order of tokens
in the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage`.

##### Parameters

| message | A non-null `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage`. |
| dryRun | A boolean indicating whether to perform a dry run (validation only) of the send. |
|---|---|

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse` indicating the result of the operation.

##### Throws

| [FirebaseMessagingException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessagingException) | If an error occurs while handing the messages off to FCM for delivery. An exception here indicates a total failure, meaning that the messages could not be delivered to any recipient. Partial failures are indicated by a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse` return value. |
|---|---|

#### public [BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse)
**sendMulticast**
([MulticastMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage) message)


**This method is deprecated.**   
Use `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEachForMulticast(com.google.firebase.messaging.MulticastMessage)` instead.

Sends the given multicast message to all the FCM registration tokens specified in it.

This method uses the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendAll(java.util.List<com.google.firebase.messaging.Message>)` API under the hood to send the given
message to all the target recipients. The responses list obtained by calling
`https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse#getResponses()` on the return value corresponds to the order of tokens
in the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage`.

##### Parameters

| message | A non-null `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage` |
|---|---|

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse` indicating the result of the operation.

##### Throws

| [FirebaseMessagingException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessagingException) | If an error occurs while handing the messages off to FCM for delivery. An exception here indicates a total failure, meaning that the messages could not be delivered to any recipient. Partial failures are indicated by a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse` return value. |
|---|---|

#### public ApiFuture\<[BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse)\>
**sendMulticastAsync**
([MulticastMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage) message)


**This method is deprecated.**   
Use `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEachForMulticastAsync(com.google.firebase.messaging.MulticastMessage)` instead.

Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendMulticast(com.google.firebase.messaging.MulticastMessage)` but performs the operation
asynchronously.

##### Parameters

| message | A non-null `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage`. |
|---|---|

##### Returns

- An `ApiFuture` that will complete with a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse` when the messages have been sent.

#### public ApiFuture\<[BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse)\>
**sendMulticastAsync**
([MulticastMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage) message, boolean dryRun)


**This method is deprecated.**   
Use `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendEachForMulticastAsync(com.google.firebase.messaging.MulticastMessage, boolean)` instead.

Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendMulticast(com.google.firebase.messaging.MulticastMessage, boolean)` but performs the operation
asynchronously.

##### Parameters

| message | A non-null `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage`. |
| dryRun | A boolean indicating whether to perform a dry run (validation only) of the send. |
|---|---|

##### Returns

- An `ApiFuture` that will complete with a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse` when the messages have been sent.

#### public [TopicManagementResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse)
**subscribeToTopic**
(List\<String\> registrationTokens, String topic)

Subscribes a list of registration tokens to a topic.

##### Parameters

| registrationTokens | A non-null, non-empty list of device registration tokens, with at most 1000 entries. |
| topic | Name of the topic to subscribe to. May contain the `/topics/` prefix. |
|---|---|

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse`.

##### Throws

| [FirebaseMessagingException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessagingException) |   |
|---|---|

#### public ApiFuture\<[TopicManagementResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse)\>
**subscribeToTopicAsync**
(List\<String\> registrationTokens, String topic)

Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#subscribeToTopic(java.util.List<java.lang.String>, java.lang.String)` but performs the operation asynchronously.

##### Parameters

| registrationTokens | A non-null, non-empty list of device registration tokens, with at most 1000 entries. |
| topic | Name of the topic to subscribe to. May contain the `/topics/` prefix. |
|---|---|

##### Returns

- An `ApiFuture` that will complete with a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse`.

#### public [TopicManagementResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse)
**unsubscribeFromTopic**
(List\<String\> registrationTokens, String topic)

Unsubscribes a list of registration tokens from a topic.

##### Parameters

| registrationTokens | A non-null, non-empty list of device registration tokens, with at most 1000 entries. |
| topic | Name of the topic to unsubscribe from. May contain the `/topics/` prefix. |
|---|---|

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse`.

##### Throws

| [FirebaseMessagingException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessagingException) |   |
|---|---|

#### public ApiFuture\<[TopicManagementResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse)\>
**unsubscribeFromTopicAsync**
(List\<String\> registrationTokens, String topic)

Similar to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#unsubscribeFromTopic(java.util.List<java.lang.String>, java.lang.String)` but performs the operation
asynchronously.

##### Parameters

| registrationTokens | A non-null, non-empty list of device registration tokens, with at most 1000 entries. |
| topic | Name of the topic to unsubscribe from. May contain the `/topics/` prefix. |
|---|---|

##### Returns

- An `ApiFuture` that will complete with a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/TopicManagementResponse`.