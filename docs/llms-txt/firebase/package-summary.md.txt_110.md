# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/package-summary.md.txt

# com.google.firebase.messaging

# com.google.firebase.messaging

Contains public API classes for Firebase Cloud Messaging.

## Classes

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging` | Top level [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/) singleton that provides methods for generating tokens and subscribing to topics. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessagingService` | Base class for receiving messages from Firebase Cloud Messaging. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage` | A remote Firebase Message. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Builder` | Builder object for constructing `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage` instances. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification` | Remote Firebase notification details. |

## Exceptions

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/SendException` | Firebase message send exception. |

## Annotations

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.MessagePriority` | Priority of the message |

## Top-level functions summary

|---|---|
| `inline https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/package-summary#remoteMessage(kotlin.String,kotlin.Function1)(to: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, crossinline init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage` instance initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/package-summary#remoteMessage(kotlin.String,kotlin.Function1)` function. |

## Extension properties summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/package-summary#(com.google.firebase.Firebase).messaging()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |

## Top-level functions

### remoteMessage

```
inline fun remoteMessage(to: String, crossinline init: RemoteMessage.Builder.() -> Unit): RemoteMessage
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage` instance initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/package-summary#remoteMessage(kotlin.String,kotlin.Function1)` function.

## Extension properties

### messaging

```
val Firebase.messaging: FirebaseMessaging
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.