# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.md.txt

# RemoteMessage

# RemoteMessage


```
@SafeParcelable.Reserved(value = [1])
@SafeParcelable.Class(creator = "RemoteMessageCreator")
public final class RemoteMessage extends AbstractSafeParcelable
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.android.gms.common.internal.safeparcel.AbstractSafeParcelable](https://firebase.google.com/docs/reference/android/com/google/android/gms/common/internal/safeparcel/AbstractSafeParcelable) ||
|   | ↳ | [com.google.firebase.messaging.RemoteMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage) |

*** ** * ** ***

A remote Firebase Message.

Messages will be received via `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessagingService#onMessageReceived(com.google.firebase.messaging.RemoteMessage)`.

Messages may have a `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification` instance if they are received while the application is in the foreground, otherwise they will be automatically posted to the notification tray.

## Summary

| ### Nested types |
|---|
| `public class https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Builder` Builder object for constructing `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage` instances. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/IntDef.html(value = ) @https://developer.android.com/reference/kotlin/java/lang/annotation/Retention.html(value = RetentionPolicy.SOURCE) public annotation https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.MessagePriority` Priority of the message |
| `public class https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification` Remote Firebase notification details. |

| ### Constants |
|---|---|
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage#PRIORITY_HIGH() = 1` |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage#PRIORITY_NORMAL() = 2` |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage#PRIORITY_UNKNOWN() = 0` |

| ### Public fields |
|---|---|
| `https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage#data()` |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage#notification()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage#getCollapseKey()()` Gets the collapse key of the message. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage#getData()()` Gets the message payload data. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage#getFrom()()` Get the sender of this message. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage#getMessageId()()` Gets the message's ID. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage#getMessageType()()` Gets the type of message. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage#getNotification()()` Gets the notification data from the message if set. |
| `int` | `@https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.MessagePriority https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage#getOriginalPriority()()` Gets the original priority of message. |
| `int` | `@https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.MessagePriority https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage#getPriority()()` Gets the priority of message as delivered. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage#getSenderId()()` Gets the Sender ID for the sender of this message. |
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage#getSentTime()()` Gets the time in milliseconds from the Epoch that the message was sent. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `[getTo](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage#getTo())()` **This method is deprecated.** This function is actually **decommissioned** along with all of FCM upstream messaging. <br /> |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage#getTtl()()` Gets the message time to live (TTL) in seconds. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage#writeToParcel(android.os.Parcel,int)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/os/Parcel.html out, int flags)` |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/kotlin/android/os/Parcelable.html) |---|---| | `static final int` | `https://developer.android.com/reference/kotlin/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR-- = 1` | | `static final int` | `https://developer.android.com/reference/kotlin/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE-- = 1` | |
| From [com.google.android.gms.common.internal.safeparcel.SafeParcelable](https://firebase.google.com/docs/reference/android/com/google/android/gms/common/internal/safeparcel/SafeParcelable) |---|---| | `static final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/android/gms/common/internal/safeparcel/SafeParcelable#NULL() = "SAFE_PARCELABLE_NULL_STRING"` | |

| ### Inherited methods |
|---|
| From [com.google.android.gms.common.internal.safeparcel.AbstractSafeParcelable](https://firebase.google.com/docs/reference/android/com/google/android/gms/common/internal/safeparcel/AbstractSafeParcelable) |---|---| | `final int` | `https://firebase.google.com/docs/reference/android/com/google/android/gms/common/internal/safeparcel/AbstractSafeParcelable#describeContents()()` | |

## Constants

### PRIORITY_HIGH

```
public static final int PRIORITY_HIGH = 1
```

### PRIORITY_NORMAL

```
public static final int PRIORITY_NORMAL = 2
```

### PRIORITY_UNKNOWN

```
public static final int PRIORITY_UNKNOWN = 0
```

## Public fields

### data

```
public Map<String, String> data
```

### notification

```
public RemoteMessage.Notification notification
```

## Public methods

### getCollapseKey

```
public @Nullable String getCollapseKey()
```

Gets the collapse key of the message.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | The collapse key |

### getData

```
public @NonNull Map<String, String> getData()
```

Gets the message payload data.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/String.html>` | A map of the message payload. |

### getFrom

```
public @Nullable String getFrom()
```

Get the sender of this message.

This will be the sender ID or the topic for topic messages.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | The message sender |

### getMessageId

```
public @Nullable String getMessageId()
```

Gets the message's ID.

This is automatically generated by the server. Treat it as an opaque string. Do not rely on its format to be consistent.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | The message ID |

### getMessageType

```
public @Nullable String getMessageType()
```

Gets the type of message.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | The message type |

### getNotification

```
public @Nullable RemoteMessage.Notification getNotification()
```

Gets the notification data from the message if set.

This field will be non-null if a notification message is received while the application is in the foreground.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Notification` | The message notification or null. |

### getOriginalPriority

```
@RemoteMessage.MessagePriority
public int getOriginalPriority()
```

Gets the original priority of message.

| Returns |
|---|---|
| `int` | The original message priority |

### getPriority

```
@RemoteMessage.MessagePriority
public int getPriority()
```

Gets the priority of message as delivered. This may be lower than the priority originally requested.

| Returns |
|---|---|
| `int` | The message priority as delivered |

### getSenderId

```
public @Nullable String getSenderId()
```

Gets the Sender ID for the sender of this message.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | the message Sender ID |

### getSentTime

```
public long getSentTime()
```

Gets the time in milliseconds from the Epoch that the message was sent.

| Returns |
|---|---|
| `long` | The time that the message was sent |

### getTo

```
public @Nullable String [getTo](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage#getTo())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> This function is actually **decommissioned** along with all of FCM upstream messaging. Learn more in the [FAQ about FCM features deprecated in June 2023](https://firebase.google.com/support/faq#fcm-23-deprecation).

Gets the message destination.

### getTtl

```
public int getTtl()
```

Gets the message time to live (TTL) in seconds.

| Returns |
|---|---|
| `int` | The message TTL |

### writeToParcel

```
public void writeToParcel(@NonNull Parcel out, int flags)
```