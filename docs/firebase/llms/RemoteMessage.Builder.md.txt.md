# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Builder.md.txt

# RemoteMessage.Builder

# RemoteMessage.Builder


```
public class RemoteMessage.Builder
```

<br />

*** ** * ** ***

Builder object for constructing `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage` instances.

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Builder#data()` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Builder#Builder(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html to)` Sets the destination of the message. |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Builder#addData(java.lang.String,java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html value)` Adds a data key value pair to the message. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Builder#build()()` Build a RemoteMessage instance. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Builder#clearData()()` Clears the message data. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Builder#setCollapseKey(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html collapseKey)` Sets the collapse key of the message. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Builder#setData(java.util.Map<java.lang.String,java.lang.String>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/String.html> data)` Sets the message data to the contents of `data`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Builder#setMessageId(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html messageId)` Sets the messages ID. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Builder#setMessageType(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html messageType)` Sets the type of message. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Builder#setTtl(int)(@https://developer.android.com/reference/kotlin/androidx/annotation/IntRange.html(from = 0, to = 86400) int ttl)` Sets the message time to live in seconds. |

## Public fields

### data

```
public final Map<String, String> data
```

## Public constructors

### Builder

```
public Builder(@NonNull String to)
```

Sets the destination of the message.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html to` | The destination of the message in the format of ` SENDER_ID@fcm.googleapis.com`. The `SENDER_ID` should be the FirebaseApp gcm sender id. |

## Public methods

### addData

```
public @NonNull RemoteMessage.Builder addData(@NonNull String key, @Nullable String value)
```

Adds a data key value pair to the message.

An existing value with the same key will be replaced by the new value.

### build

```
public @NonNull RemoteMessage build()
```

Build a RemoteMessage instance.

### clearData

```
public @NonNull RemoteMessage.Builder clearData()
```

Clears the message data.

### setCollapseKey

```
public @NonNull RemoteMessage.Builder setCollapseKey(@Nullable String collapseKey)
```

Sets the collapse key of the message.

A pending message will be replaced by a new message with the same collapse key if it is currently unable to be delivered to the recipient.

### setData

```
public @NonNull RemoteMessage.Builder setData(@NonNull Map<String, String> data)
```

Sets the message data to the contents of `data`.

Any existing data will be removed.

### setMessageId

```
public @NonNull RemoteMessage.Builder setMessageId(@NonNull String messageId)
```

Sets the messages ID.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html messageId` | ID of the message. This is generated by the application. It must be unique for each message. This allows error callbacks and debugging. |

### setMessageType

```
public @NonNull RemoteMessage.Builder setMessageType(@Nullable String messageType)
```

Sets the type of message.

### setTtl

```
public @NonNull RemoteMessage.Builder setTtl(@IntRange(from = 0, to = 86400) int ttl)
```

Sets the message time to live in seconds.

If 0, the message send will be attempted immediately and will be dropped if the device is not connected. Otherwise, the message will be queued.