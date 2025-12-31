# Source: https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-messaging.md.txt

# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging.md.txt

# FirebaseAdmin.Messaging.FirebaseMessaging Class Reference

# FirebaseAdmin.Messaging.FirebaseMessaging

This is the entry point to all server-side Firebase Cloud [Messaging](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging#namespace_firebase_admin_1_1_messaging) (FCM) operations.

## Summary

You can get an instance of this class via [FirebaseMessaging.DefaultInstance](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a15a60af9a46d9aba14564656ccfb4847).

### Inheritance

Inherits from: FirebaseAdmin.IFirebaseService

|                                                                                                                                                                                                                                           ### Properties                                                                                                                                                                                                                                           ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [DefaultInstance](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a15a60af9a46d9aba14564656ccfb4847) | `static `[FirebaseMessaging](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging) Gets the messaging instance associated with the default Firebase app. |

|                                                                                                                                                                                                                                                                                                  ### Public static functions                                                                                                                                                                                                                                                                                                   ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GetMessaging](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a995d2965bf37707e6ef71e6999f37ac0)`(`[FirebaseApp](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app#class_firebase_admin_1_1_firebase_app)` app)` | [FirebaseMessaging](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging) Returns the messaging instance for the specified app. |

|                                                                                                                                                                                                                                                                                                                                                                                                                                         ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                                         ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [SendAllAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a37541b3d54b9c3ae6b74aea938c6fd89)`(IEnumerable< `[Message](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/message#class_firebase_admin_1_1_messaging_1_1_message)` > messages)`                                                                             | `async Task< `[BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response)` >` Sends all the messages in the given list via Firebase Cloud [Messaging](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging#namespace_firebase_admin_1_1_messaging). |
| [SendAllAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a7277d69c9a87ba3f9611b0ee9a313e91)`(IEnumerable< `[Message](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/message#class_firebase_admin_1_1_messaging_1_1_message)` > messages, CancellationToken cancellationToken)`                                        | `async Task< `[BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response)` >` Sends all the messages in the given list via Firebase Cloud [Messaging](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging#namespace_firebase_admin_1_1_messaging). |
| [SendAllAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a32ac5f2d662d78ed5849f1ef5ab41d48)`(IEnumerable< `[Message](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/message#class_firebase_admin_1_1_messaging_1_1_message)` > messages, bool dryRun)`                                                                | `async Task< `[BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response)` >` Sends all the messages in the given list via Firebase Cloud [Messaging](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging#namespace_firebase_admin_1_1_messaging). |
| [SendAllAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a881f1eab7df51264203cc766895a8cf7)`(IEnumerable< `[Message](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/message#class_firebase_admin_1_1_messaging_1_1_message)` > messages, bool dryRun, CancellationToken cancellationToken)`                           | `async Task< `[BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response)` >` Sends all the messages in the given list via Firebase Cloud [Messaging](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging#namespace_firebase_admin_1_1_messaging). |
| [SendAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a4639a894bc5a2440275b48eb758262df)`(`[Message](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/message#class_firebase_admin_1_1_messaging_1_1_message)` message)`                                                                                                | `async Task< string >` Sends a message to the FCM service for delivery.                                                                                                                                                                                                                                                                                                                                    |
| [SendAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a52fe53ccb6f4e96c3779a965c2e339f7)`(`[Message](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/message#class_firebase_admin_1_1_messaging_1_1_message)` message, CancellationToken cancellationToken)`                                                           | `async Task< string >` Sends a message to the FCM service for delivery.                                                                                                                                                                                                                                                                                                                                    |
| [SendAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a3d6f68610fe94ce369d3c315dbdcff62)`(`[Message](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/message#class_firebase_admin_1_1_messaging_1_1_message)` message, bool dryRun)`                                                                                   | `async Task< string >` Sends a message to the FCM service for delivery.                                                                                                                                                                                                                                                                                                                                    |
| [SendAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a92327f26f31cc21e6327c6b0433cdd58)`(`[Message](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/message#class_firebase_admin_1_1_messaging_1_1_message)` message, bool dryRun, CancellationToken cancellationToken)`                                              | `async Task< string >` Sends a message to the FCM service for delivery.                                                                                                                                                                                                                                                                                                                                    |
| [SendEachAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a5b1151b4eddb64d31aecff103702f099)`(IEnumerable< `[Message](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/message#class_firebase_admin_1_1_messaging_1_1_message)` > messages)`                                                                            | `async Task< `[BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response)` >` Sends each message in the given list via Firebase Cloud [Messaging](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging#namespace_firebase_admin_1_1_messaging).     |
| [SendEachAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a18fbc7d126644abc61d507d8ed5e1e13)`(IEnumerable< `[Message](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/message#class_firebase_admin_1_1_messaging_1_1_message)` > messages, CancellationToken cancellationToken)`                                       | `async Task< `[BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response)` >` Sends each message in the given list via Firebase Cloud [Messaging](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging#namespace_firebase_admin_1_1_messaging).     |
| [SendEachAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1ac8a93b42827f1cbfe4fe072184a63e56)`(IEnumerable< `[Message](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/message#class_firebase_admin_1_1_messaging_1_1_message)` > messages, bool dryRun)`                                                               | `async Task< `[BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response)` >` Sends each message in the given list via Firebase Cloud [Messaging](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging#namespace_firebase_admin_1_1_messaging).     |
| [SendEachAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a5bcb61b73028a7665df59051e6b61f83)`(IEnumerable< `[Message](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/message#class_firebase_admin_1_1_messaging_1_1_message)` > messages, bool dryRun, CancellationToken cancellationToken)`                          | `async Task< `[BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response)` >` Sends each message in the given list via Firebase Cloud [Messaging](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging#namespace_firebase_admin_1_1_messaging).     |
| [SendEachForMulticastAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a3dcaf488517876809eb9519dc0783978)`(`[MulticastMessage](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/multicast-message#class_firebase_admin_1_1_messaging_1_1_multicast_message)` message)`                                                   | `async Task< `[BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response)` >` Sends the given multicast message to all the FCM registration tokens specified in it.                                                                                                                       |
| [SendEachForMulticastAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1ae19ddf00131d307bff214f3093932187)`(`[MulticastMessage](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/multicast-message#class_firebase_admin_1_1_messaging_1_1_multicast_message)` message, CancellationToken cancellationToken)`              | `async Task< `[BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response)` >` Sends the given multicast message to all the FCM registration tokens specified in it.                                                                                                                       |
| [SendEachForMulticastAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a62e4859da0705bff75906e9041b6e948)`(`[MulticastMessage](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/multicast-message#class_firebase_admin_1_1_messaging_1_1_multicast_message)` message, bool dryRun)`                                      | `async Task< `[BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response)` >` Sends the given multicast message to all the FCM registration tokens specified in it.                                                                                                                       |
| [SendEachForMulticastAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a159e7e14b4bd09e05ddb4c9e9a5851ff)`(`[MulticastMessage](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/multicast-message#class_firebase_admin_1_1_messaging_1_1_multicast_message)` message, bool dryRun, CancellationToken cancellationToken)` | `async Task< `[BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response)` >` Sends the given multicast message to all the FCM registration tokens specified in it.                                                                                                                       |
| [SendMulticastAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1ac19b28383fa9217cf44189aaac852613)`(`[MulticastMessage](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/multicast-message#class_firebase_admin_1_1_messaging_1_1_multicast_message)` message)`                                                          | `async Task< `[BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response)` >` Sends the given multicast message to all the FCM registration tokens specified in it.                                                                                                                       |
| [SendMulticastAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a9c45e8353fad2f9ad458291831aac272)`(`[MulticastMessage](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/multicast-message#class_firebase_admin_1_1_messaging_1_1_multicast_message)` message, CancellationToken cancellationToken)`                     | `async Task< `[BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response)` >` Sends the given multicast message to all the FCM registration tokens specified in it.                                                                                                                       |
| [SendMulticastAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1ac4b7d71e8a5ece162524cba1d2bef82e)`(`[MulticastMessage](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/multicast-message#class_firebase_admin_1_1_messaging_1_1_multicast_message)` message, bool dryRun)`                                             | `async Task< `[BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response)` >` Sends the given multicast message to all the FCM registration tokens specified in it.                                                                                                                       |
| [SendMulticastAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a9f7441b52652a5d5fbabb4c155b1632c)`(`[MulticastMessage](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/multicast-message#class_firebase_admin_1_1_messaging_1_1_multicast_message)` message, bool dryRun, CancellationToken cancellationToken)`        | `async Task< `[BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response)` >` Sends the given multicast message to all the FCM registration tokens specified in it.                                                                                                                       |
| [SubscribeToTopicAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a275a9c12c4dcc4c4a7e50e43723e235e)`(IReadOnlyList< string > registrationTokens, string topic)`                                                                                                                                                                                              | `async Task< `[TopicManagementResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/topic-management-response#class_firebase_admin_1_1_messaging_1_1_topic_management_response)` >` Subscribes a list of registration tokens to a topic.                                                                                                                        |
| [UnsubscribeFromTopicAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1ae2dda6909c8dc7e4e8990ae0b0ed179c)`(IReadOnlyList< string > registrationTokens, string topic)`                                                                                                                                                                                          | `async Task< `[TopicManagementResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/topic-management-response#class_firebase_admin_1_1_messaging_1_1_topic_management_response)` >` Unsubscribes a list of registration tokens from a topic.                                                                                                                    |

## Properties

### DefaultInstance

```text
static FirebaseMessaging DefaultInstance
```  
Gets the messaging instance associated with the default Firebase app.

This property is `null` if the default app doesn't yet exist.

## Public static functions

### GetMessaging

```text
FirebaseMessaging GetMessaging(
  FirebaseApp app
)
```  
Returns the messaging instance for the specified app.

<br />

|                                                                                                                        Details                                                                                                                        ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |--------------------------------|------------------------------| | `System.ArgumentNullException` | If the app argument is null. |                                                                                                      |
| Parameters  | |-------|------------------| | `app` | An app instance. |                                                                                                                                                                                |
| **Returns** | The [FirebaseMessaging](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging) instance associated with the specified app. |

## Public functions

### SendAllAsync

```text
async Task< BatchResponse > SendAllAsync(
  IEnumerable< Message > messages
)
```  
Sends all the messages in the given list via Firebase Cloud [Messaging](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging#namespace_firebase_admin_1_1_messaging).

Employs batching to send the entire list as a single RPC call. Compared to the [SendAsync(Message)](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a4639a894bc5a2440275b48eb758262df) method, this is a significantly more efficient way to send multiple messages.

<br />

|                                                                                                                     Details                                                                                                                      ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |------------------------------|------------------------------------------------| | `FirebaseMessagingException` | If an error occurs while sending the messages. |                                                                 |
| Parameters  | |------------|----------------------------------------------------------| | `messages` | Up to 500 messages to send in the batch. Cannot be null. |                                                                                 |
| **Returns** | A [BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response) containing details of the batch operation's outcome. |

### SendAllAsync

```text
async Task< BatchResponse > SendAllAsync(
  IEnumerable< Message > messages,
  CancellationToken cancellationToken
)
```  
Sends all the messages in the given list via Firebase Cloud [Messaging](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging#namespace_firebase_admin_1_1_messaging).

Employs batching to send the entire list as a single RPC call. Compared to the [SendAsync(Message)](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a4639a894bc5a2440275b48eb758262df) method, this is a significantly more efficient way to send multiple messages.

<br />

|                                                                                                                                    Details                                                                                                                                     ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |------------------------------|------------------------------------------------| | `FirebaseMessagingException` | If an error occurs while sending the messages. |                                                                                               |
| Parameters  | |---------------------|-------------------------------------------------------------| | `messages`          | Up to 500 messages to send in the batch. Cannot be null.    | | `cancellationToken` | A cancellation token to monitor the asynchronous operation. | |
| **Returns** | A [BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response) containing details of the batch operation's outcome.                               |

### SendAllAsync

```text
async Task< BatchResponse > SendAllAsync(
  IEnumerable< Message > messages,
  bool dryRun
)
```  
Sends all the messages in the given list via Firebase Cloud [Messaging](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging#namespace_firebase_admin_1_1_messaging).

Employs batching to send the entire list as a single RPC call. Compared to the [SendAsync(Message)](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a4639a894bc5a2440275b48eb758262df) method, this is a significantly more efficient way to send multiple messages.

<br />

|                                                                                                                                                                                                                                                                                                                                                Details                                                                                                                                                                                                                                                                                                                                                 ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |------------------------------|------------------------------------------------| | `FirebaseMessagingException` | If an error occurs while sending the messages. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Parameters  | |------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `messages` | Up to 500 messages to send in the batch. Cannot be null.                                                                                                                                                     | | `dryRun`   | A boolean indicating whether to perform a dry run (validation only) of the send. If set to true, the message will be sent to the FCM backend service, but it will not be delivered to any actual recipients. | |
| **Returns** | A [BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response) containing details of the batch operation's outcome.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

### SendAllAsync

```text
async Task< BatchResponse > SendAllAsync(
  IEnumerable< Message > messages,
  bool dryRun,
  CancellationToken cancellationToken
)
```  
Sends all the messages in the given list via Firebase Cloud [Messaging](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging#namespace_firebase_admin_1_1_messaging).

Employs batching to send the entire list as a single RPC call. Compared to the [SendAsync(Message)](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a4639a894bc5a2440275b48eb758262df) method, this is a significantly more efficient way to send multiple messages.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |------------------------------|------------------------------------------------| | `FirebaseMessagingException` | If an error occurs while sending the messages. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Parameters  | |---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `messages`          | Up to 500 messages to send in the batch. Cannot be null.                                                                                                                                                     | | `dryRun`            | A boolean indicating whether to perform a dry run (validation only) of the send. If set to true, the message will be sent to the FCM backend service, but it will not be delivered to any actual recipients. | | `cancellationToken` | A cancellation token to monitor the asynchronous operation.                                                                                                                                                  | |
| **Returns** | A [BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response) containing details of the batch operation's outcome.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

### SendAsync

```text
async Task< string > SendAsync(
  Message message
)
```  
Sends a message to the FCM service for delivery.

The message gets validated both by the Admin SDK, and the remote FCM service. A successful return value indicates that the message has been successfully sent to FCM, where it has been accepted by the FCM service.

<br />

|                                                                                                                                                                     Details                                                                                                                                                                      ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |------------------------------|-----------------------------------------------| | `ArgumentNullException`      | If the message argument is null.              | | `ArgumentException`          | If the message contains any invalid fields.   | | `FirebaseMessagingException` | If an error occurs while sending the message. | |
| Parameters  | |-----------|-------------------------------------------| | `message` | The message to be sent. Must not be null. |                                                                                                                                                                                                                 |
| **Returns** | A task that completes with a message ID string, which represents successful handoff to FCM.                                                                                                                                                                                                                                         |

### SendAsync

```text
async Task< string > SendAsync(
  Message message,
  CancellationToken cancellationToken
)
```  
Sends a message to the FCM service for delivery.

The message gets validated both by the Admin SDK, and the remote FCM service. A successful return value indicates that the message has been successfully sent to FCM, where it has been accepted by the FCM service.

<br />

|                                                                                                                                                                     Details                                                                                                                                                                      ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |------------------------------|-----------------------------------------------| | `ArgumentNullException`      | If the message argument is null.              | | `ArgumentException`          | If the message contains any invalid fields.   | | `FirebaseMessagingException` | If an error occurs while sending the message. | |
| Parameters  | |---------------------|-------------------------------------------------------------| | `message`           | The message to be sent. Must not be null.                   | | `cancellationToken` | A cancellation token to monitor the asynchronous operation. |                                                                   |
| **Returns** | A task that completes with a message ID string, which represents successful handoff to FCM.                                                                                                                                                                                                                                         |

### SendAsync

```text
async Task< string > SendAsync(
  Message message,
  bool dryRun
)
```  
Sends a message to the FCM service for delivery.

The message gets validated both by the Admin SDK, and the remote FCM service. A successful return value indicates that the message has been successfully sent to FCM, where it has been accepted by the FCM service.

If the *dryRun* option is set to true, the message will not be actually sent to the recipients. Instead, the FCM service performs all the necessary validations, and emulates the send operation. This is a good way to check if a certain message will be accepted by FCM for delivery.

<br />

|                                                                                                                                                                                                                                                                                                                                               Details                                                                                                                                                                                                                                                                                                                                               ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |------------------------------|-----------------------------------------------| | `ArgumentNullException`      | If the message argument is null.              | | `ArgumentException`          | If the message contains any invalid fields.   | | `FirebaseMessagingException` | If an error occurs while sending the message. |                                                                                                                                                                                                                                                                                                                                                    |
| Parameters  | |-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `message` | The message to be sent. Must not be null.                                                                                                                                                                    | | `dryRun`  | A boolean indicating whether to perform a dry run (validation only) of the send. If set to true, the message will be sent to the FCM backend service, but it will not be delivered to any actual recipients. | |
| **Returns** | A task that completes with a message ID string, which represents successful handoff to FCM.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

### SendAsync

```text
async Task< string > SendAsync(
  Message message,
  bool dryRun,
  CancellationToken cancellationToken
)
```  
Sends a message to the FCM service for delivery.

The message gets validated both by the Admin SDK, and the remote FCM service. A successful return value indicates that the message has been successfully sent to FCM, where it has been accepted by the FCM service.

If the *dryRun* option is set to true, the message will not be actually sent to the recipients. Instead, the FCM service performs all the necessary validations, and emulates the send operation. This is a good way to check if a certain message will be accepted by FCM for delivery.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |------------------------------|-----------------------------------------------| | `ArgumentNullException`      | If the message argument is null.              | | `ArgumentException`          | If the message contains any invalid fields.   | | `FirebaseMessagingException` | If an error occurs while sending the message. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Parameters  | |---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `message`           | The message to be sent. Must not be null.                                                                                                                                                                    | | `dryRun`            | A boolean indicating whether to perform a dry run (validation only) of the send. If set to true, the message will be sent to the FCM backend service, but it will not be delivered to any actual recipients. | | `cancellationToken` | A cancellation token to monitor the asynchronous operation.                                                                                                                                                  | |
| **Returns** | A task that completes with a message ID string, which represents successful handoff to FCM.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### SendEachAsync

```text
async Task< BatchResponse > SendEachAsync(
  IEnumerable< Message > messages
)
```  
Sends each message in the given list via Firebase Cloud [Messaging](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging#namespace_firebase_admin_1_1_messaging).

Unlike SendAllAsync(IEnumerable{Message}), this method makes an HTTP call for each message in the given list.

<br />

|                                                                                                                     Details                                                                                                                      ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |------------------------------|------------------------------------------------| | `FirebaseMessagingException` | If an error occurs while sending the messages. |                                                                 |
| Parameters  | |------------|-------------------------------------------------------------------| | `messages` | Up to 500 messages to send in the batch. Cannot be null or empty. |                                                               |
| **Returns** | A [BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response) containing details of the batch operation's outcome. |

### SendEachAsync

```text
async Task< BatchResponse > SendEachAsync(
  IEnumerable< Message > messages,
  CancellationToken cancellationToken
)
```  
Sends each message in the given list via Firebase Cloud [Messaging](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging#namespace_firebase_admin_1_1_messaging).

Unlike SendAllAsync(IEnumerable{Message}, CancellationToken), this method makes an HTTP call for each message in the given list.

<br />

|                                                                                                                                             Details                                                                                                                                              ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |------------------------------|------------------------------------------------| | `FirebaseMessagingException` | If an error occurs while sending the messages. |                                                                                                                 |
| Parameters  | |---------------------|-------------------------------------------------------------------| | `messages`          | Up to 500 messages to send in the batch. Cannot be null or empty. | | `cancellationToken` | A cancellation token to monitor the asynchronous operation.       | |
| **Returns** | A [BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response) containing details of the batch operation's outcome.                                                 |

### SendEachAsync

```text
async Task< BatchResponse > SendEachAsync(
  IEnumerable< Message > messages,
  bool dryRun
)
```  
Sends each message in the given list via Firebase Cloud [Messaging](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging#namespace_firebase_admin_1_1_messaging).

Unlike SendAllAsync(IEnumerable{Message}, bool), this method makes an HTTP call for each message in the given list.

<br />

|                                                                                                                                                                                                                                                                                                                                                Details                                                                                                                                                                                                                                                                                                                                                 ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |------------------------------|------------------------------------------------| | `FirebaseMessagingException` | If an error occurs while sending the messages. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Parameters  | |------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `messages` | Up to 500 messages to send in the batch. Cannot be null or empty.                                                                                                                                            | | `dryRun`   | A boolean indicating whether to perform a dry run (validation only) of the send. If set to true, the message will be sent to the FCM backend service, but it will not be delivered to any actual recipients. | |
| **Returns** | A [BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response) containing details of the batch operation's outcome.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

### SendEachAsync

```text
async Task< BatchResponse > SendEachAsync(
  IEnumerable< Message > messages,
  bool dryRun,
  CancellationToken cancellationToken
)
```  
Sends each message in the given list via Firebase Cloud [Messaging](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/messaging#namespace_firebase_admin_1_1_messaging).

Unlike SendAllAsync(IEnumerable{Message}, bool, CancellationToken), this method makes an HTTP call for each message in the given list.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |------------------------------|------------------------------------------------| | `FirebaseMessagingException` | If an error occurs while sending the messages. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Parameters  | |---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `messages`          | Up to 500 messages to send in the batch. Cannot be null or empty.                                                                                                                                            | | `dryRun`            | A boolean indicating whether to perform a dry run (validation only) of the send. If set to true, the message will be sent to the FCM backend service, but it will not be delivered to any actual recipients. | | `cancellationToken` | A cancellation token to monitor the asynchronous operation.                                                                                                                                                  | |
| **Returns** | A [BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response) containing details of the batch operation's outcome.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

### SendEachForMulticastAsync

```text
async Task< BatchResponse > SendEachForMulticastAsync(
  MulticastMessage message
)
```  
Sends the given multicast message to all the FCM registration tokens specified in it.

Unlike [SendMulticastAsync(MulticastMessage)](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1ac19b28383fa9217cf44189aaac852613), this method makes an HTTP call for each token in the given multicast message.

<br />

|                                                                                                                     Details                                                                                                                      ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |------------------------------|------------------------------------------------| | `FirebaseMessagingException` | If an error occurs while sending the messages. |                                                                 |
| Parameters  | |-----------|----------------------------------------------------| | `message` | The message to be sent. Must not be null or empty. |                                                                                               |
| **Returns** | A [BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response) containing details of the batch operation's outcome. |

### SendEachForMulticastAsync

```text
async Task< BatchResponse > SendEachForMulticastAsync(
  MulticastMessage message,
  CancellationToken cancellationToken
)
```  
Sends the given multicast message to all the FCM registration tokens specified in it.

Unlike [SendMulticastAsync(MulticastMessage, CancellationToken)](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a9c45e8353fad2f9ad458291831aac272), this method makes an HTTP call for each token in the given multicast message.

<br />

|                                                                                                                                    Details                                                                                                                                     ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |------------------------------|------------------------------------------------| | `FirebaseMessagingException` | If an error occurs while sending the messages. |                                                                                               |
| Parameters  | |---------------------|-------------------------------------------------------------| | `message`           | The message to be sent. Must not be null or empty.          | | `cancellationToken` | A cancellation token to monitor the asynchronous operation. | |
| **Returns** | A [BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response) containing details of the batch operation's outcome.                               |

### SendEachForMulticastAsync

```text
async Task< BatchResponse > SendEachForMulticastAsync(
  MulticastMessage message,
  bool dryRun
)
```  
Sends the given multicast message to all the FCM registration tokens specified in it.

Unlike [SendMulticastAsync(MulticastMessage, bool)](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1ac4b7d71e8a5ece162524cba1d2bef82e), this method makes an HTTP call for each token in the given multicast message.

If the *dryRun* option is set to true, the message will not be actually sent to the recipients. Instead, the FCM service performs all the necessary validations, and emulates the send operation. This is a good way to check if a certain message will be accepted by FCM for delivery.

<br />

|                                                                                                                                                                                                                                                                                                                                               Details                                                                                                                                                                                                                                                                                                                                               ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |------------------------------|------------------------------------------------| | `FirebaseMessagingException` | If an error occurs while sending the messages. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Parameters  | |-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `message` | The message to be sent. Must not be null or empty.                                                                                                                                                           | | `dryRun`  | A boolean indicating whether to perform a dry run (validation only) of the send. If set to true, the message will be sent to the FCM backend service, but it will not be delivered to any actual recipients. | |
| **Returns** | A [BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response) containing details of the batch operation's outcome.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

### SendEachForMulticastAsync

```text
async Task< BatchResponse > SendEachForMulticastAsync(
  MulticastMessage message,
  bool dryRun,
  CancellationToken cancellationToken
)
```  
Sends the given multicast message to all the FCM registration tokens specified in it.

Unlike [SendMulticastAsync(MulticastMessage, bool, CancellationToken)](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging#class_firebase_admin_1_1_messaging_1_1_firebase_messaging_1a9f7441b52652a5d5fbabb4c155b1632c), this method makes an HTTP call for each token in the given multicast message.

If the *dryRun* option is set to true, the message will not be actually sent to the recipients. Instead, the FCM service performs all the necessary validations, and emulates the send operation. This is a good way to check if a certain message will be accepted by FCM for delivery.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |------------------------------|------------------------------------------------| | `FirebaseMessagingException` | If an error occurs while sending the messages. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Parameters  | |---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `message`           | The message to be sent. Must not be null or empty.                                                                                                                                                           | | `dryRun`            | A boolean indicating whether to perform a dry run (validation only) of the send. If set to true, the message will be sent to the FCM backend service, but it will not be delivered to any actual recipients. | | `cancellationToken` | A cancellation token to monitor the asynchronous operation.                                                                                                                                                  | |
| **Returns** | A [BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response) containing details of the batch operation's outcome.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

### SendMulticastAsync

```text
async Task< BatchResponse > SendMulticastAsync(
  MulticastMessage message
)
```  
Sends the given multicast message to all the FCM registration tokens specified in it.

<br />

|                                                                                                                     Details                                                                                                                      ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |------------------------------|------------------------------------------------| | `FirebaseMessagingException` | If an error occurs while sending the messages. |                                                                 |
| Parameters  | |-----------|-------------------------------------------| | `message` | The message to be sent. Must not be null. |                                                                                                                 |
| **Returns** | A [BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response) containing details of the batch operation's outcome. |

### SendMulticastAsync

```text
async Task< BatchResponse > SendMulticastAsync(
  MulticastMessage message,
  CancellationToken cancellationToken
)
```  
Sends the given multicast message to all the FCM registration tokens specified in it.

<br />

|                                                                                                                                    Details                                                                                                                                     ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |------------------------------|------------------------------------------------| | `FirebaseMessagingException` | If an error occurs while sending the messages. |                                                                                               |
| Parameters  | |---------------------|-------------------------------------------------------------| | `message`           | The message to be sent. Must not be null.                   | | `cancellationToken` | A cancellation token to monitor the asynchronous operation. | |
| **Returns** | A [BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response) containing details of the batch operation's outcome.                               |

### SendMulticastAsync

```text
async Task< BatchResponse > SendMulticastAsync(
  MulticastMessage message,
  bool dryRun
)
```  
Sends the given multicast message to all the FCM registration tokens specified in it.

If the *dryRun* option is set to true, the message will not be actually sent to the recipients. Instead, the FCM service performs all the necessary validations, and emulates the send operation. This is a good way to check if a certain message will be accepted by FCM for delivery.

<br />

|                                                                                                                                                                                                                                                                                                                                               Details                                                                                                                                                                                                                                                                                                                                               ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |------------------------------|------------------------------------------------| | `FirebaseMessagingException` | If an error occurs while sending the messages. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Parameters  | |-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `message` | The message to be sent. Must not be null.                                                                                                                                                                    | | `dryRun`  | A boolean indicating whether to perform a dry run (validation only) of the send. If set to true, the message will be sent to the FCM backend service, but it will not be delivered to any actual recipients. | |
| **Returns** | A [BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response) containing details of the batch operation's outcome.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

### SendMulticastAsync

```text
async Task< BatchResponse > SendMulticastAsync(
  MulticastMessage message,
  bool dryRun,
  CancellationToken cancellationToken
)
```  
Sends the given multicast message to all the FCM registration tokens specified in it.

If the *dryRun* option is set to true, the message will not be actually sent to the recipients. Instead, the FCM service performs all the necessary validations, and emulates the send operation. This is a good way to check if a certain message will be accepted by FCM for delivery.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exceptions  | |------------------------------|------------------------------------------------| | `FirebaseMessagingException` | If an error occurs while sending the messages. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Parameters  | |---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `message`           | The message to be sent. Must not be null.                                                                                                                                                                    | | `dryRun`            | A boolean indicating whether to perform a dry run (validation only) of the send. If set to true, the message will be sent to the FCM backend service, but it will not be delivered to any actual recipients. | | `cancellationToken` | A cancellation token to monitor the asynchronous operation.                                                                                                                                                  | |
| **Returns** | A [BatchResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/batch-response#class_firebase_admin_1_1_messaging_1_1_batch_response) containing details of the batch operation's outcome.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

### SubscribeToTopicAsync

```verilog
async Task< TopicManagementResponse > SubscribeToTopicAsync(
  IReadOnlyList< string > registrationTokens,
  string topic
)
```  
Subscribes a list of registration tokens to a topic.

<br />

|                                                                                                                                                                                             Details                                                                                                                                                                                              ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |----------------------|--------------------------------------------------------------------------------------------------| | `registrationTokens` | A list of registration tokens to subscribe.                                                      | | `topic`              | The topic name to subscribe to. /topics/ will be prepended to the topic name provided if absent. | |
| **Returns** | A task that completes with a [TopicManagementResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/topic-management-response#class_firebase_admin_1_1_messaging_1_1_topic_management_response), giving details about the topic subscription operations.                                                                                  |

### UnsubscribeFromTopicAsync

```verilog
async Task< TopicManagementResponse > UnsubscribeFromTopicAsync(
  IReadOnlyList< string > registrationTokens,
  string topic
)
```  
Unsubscribes a list of registration tokens from a topic.

<br />

|                                                                                                                                                                                                   Details                                                                                                                                                                                                    ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |----------------------|------------------------------------------------------------------------------------------------------| | `registrationTokens` | A list of registration tokens to unsubscribe.                                                        | | `topic`              | The topic name to unsubscribe from. /topics/ will be prepended to the topic name provided if absent. | |
| **Returns** | A task that completes with a [TopicManagementResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/topic-management-response#class_firebase_admin_1_1_messaging_1_1_topic_management_response), giving details about the topic unsubscription operations.                                                                                            |