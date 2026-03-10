# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.md.txt

# RemoteMessage

# RemoteMessage


```
@SafeParcelable.Reserved(value = [1])
@SafeParcelable.Class(creator = "RemoteMessageCreator")
class RemoteMessage : AbstractSafeParcelable
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.android.gms.common.internal.safeparcel.AbstractSafeParcelable](https://firebase.google.com/docs/reference/kotlin/com/google/android/gms/common/internal/safeparcel/AbstractSafeParcelable) ||
|   | ↳ | [com.google.firebase.messaging.RemoteMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage) |

*** ** * ** ***

A remote Firebase Message.

Messages will be received via `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessagingService#onMessageReceived(com.google.firebase.messaging.RemoteMessage)`.

Messages may have a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification` instance if they are received while the application is in the foreground, otherwise they will be automatically posted to the notification tray.

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Builder` Builder object for constructing `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage` instances. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/IntDef.html(value = ) @https://developer.android.com/reference/kotlin/java/lang/annotation/Retention.html(value = RetentionPolicy.SOURCE) annotation https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.MessagePriority` Priority of the message |
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification` Remote Firebase notification details. |

| ### Constants |
|---|---|
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#PRIORITY_HIGH() = 1` |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#PRIORITY_NORMAL() = 2` |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#PRIORITY_UNKNOWN() = 0` |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#getCollapseKey()()` Gets the collapse key of the message. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#getFrom()()` Get the sender of this message. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#getMessageId()()` Gets the message's ID. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#getMessageType()()` Gets the type of message. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.MessagePriority https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#getOriginalPriority()()` Gets the original priority of message. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.MessagePriority https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#getPriority()()` Gets the priority of message as delivered. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#getSenderId()()` Gets the Sender ID for the sender of this message. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#getSentTime()()` Gets the time in milliseconds from the Epoch that the message was sent. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `[getTo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#getTo())()` **This function is deprecated.** This function is actually **decommissioned** along with all of FCM upstream messaging. <br /> |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#getTtl()()` Gets the message time to live (TTL) in seconds. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#writeToParcel(android.os.Parcel,int)(out: https://developer.android.com/reference/kotlin/android/os/Parcel.html, flags: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |

| ### Public properties |
|---|---|
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#data()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#notification()` |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/kotlin/android/os/Parcelable.html) |---|---| | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/kotlin/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR-- = 1` | | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/kotlin/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE-- = 1` | |
| From [com.google.android.gms.common.internal.safeparcel.SafeParcelable](https://firebase.google.com/docs/reference/kotlin/com/google/android/gms/common/internal/safeparcel/SafeParcelable) |---|---| | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/android/gms/common/internal/safeparcel/SafeParcelable#NULL() = "SAFE_PARCELABLE_NULL_STRING"` | |

| ### Inherited functions |
|---|
| From [com.google.android.gms.common.internal.safeparcel.AbstractSafeParcelable](https://firebase.google.com/docs/reference/kotlin/com/google/android/gms/common/internal/safeparcel/AbstractSafeParcelable) |---|---| | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/android/gms/common/internal/safeparcel/AbstractSafeParcelable#describeContents()()` | |

## Constants

### PRIORITY_HIGH

```
const val PRIORITY_HIGH = 1: Int
```

### PRIORITY_NORMAL

```
const val PRIORITY_NORMAL = 2: Int
```

### PRIORITY_UNKNOWN

```
const val PRIORITY_UNKNOWN = 0: Int
```

## Public functions

### getCollapseKey

```
fun getCollapseKey(): String?
```

Gets the collapse key of the message.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | The collapse key |

### getFrom

```
fun getFrom(): String?
```

Get the sender of this message.

This will be the sender ID or the topic for topic messages.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | The message sender |

### getMessageId

```
fun getMessageId(): String?
```

Gets the message's ID.

This is automatically generated by the server. Treat it as an opaque string. Do not rely on its format to be consistent.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | The message ID |

### getMessageType

```
fun getMessageType(): String?
```

Gets the type of message.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | The message type |

### getOriginalPriority

```
@RemoteMessage.MessagePriority
fun getOriginalPriority(): Int
```

Gets the original priority of message.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The original message priority |

### getPriority

```
@RemoteMessage.MessagePriority
fun getPriority(): Int
```

Gets the priority of message as delivered. This may be lower than the priority originally requested.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The message priority as delivered |

### getSenderId

```
fun getSenderId(): String?
```

Gets the Sender ID for the sender of this message.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | the message Sender ID |

### getSentTime

```
fun getSentTime(): Long
```

Gets the time in milliseconds from the Epoch that the message was sent.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The time that the message was sent |

### getTo

```
fun [getTo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#getTo())(): String?
```

> [!CAUTION]
> **This function is deprecated.**   
>
> This function is actually **decommissioned** along with all of FCM upstream messaging. Learn more in the [FAQ about FCM features deprecated in June 2023](https://firebase.google.com/support/faq#fcm-23-deprecation).

Gets the message destination.

### getTtl

```
fun getTtl(): Int
```

Gets the message time to live (TTL) in seconds.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The message TTL |

### writeToParcel

```
fun writeToParcel(out: Parcel, flags: Int): Unit
```

## Public properties

### data

```
val data: (Mutable)Map<String!, String!>!
```

### notification

```
val notification: RemoteMessage.Notification!
```