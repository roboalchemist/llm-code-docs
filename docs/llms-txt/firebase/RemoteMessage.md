# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.md.txt

# RemoteMessage

# RemoteMessage


```
@SafeParcelable.Reserved(valueÂ =Â [1])
@SafeParcelable.Class(creatorÂ =Â "RemoteMessageCreator")
class RemoteMessage : AbstractSafeParcelable
```

<br />

|---|---|----------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                  |||
| â³ | [com.google.android.gms.common.internal.safeparcel.AbstractSafeParcelable](https://firebase.google.com/docs/reference/kotlin/com/google/android/gms/common/internal/safeparcel/AbstractSafeParcelable) ||
|   | â³ | [com.google.firebase.messaging.RemoteMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage) |

*** ** * ** ***

A remote Firebase Message.

Messages will be received via [onMessageReceived](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessagingService#onMessageReceived(com.google.firebase.messaging.RemoteMessage)).

Messages may have a [Notification](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification) instance if they are received while the application is in the foreground, otherwise they will be automatically posted to the notification tray.

## Summary

|                                                                                                                                                                                                         ### Nested types                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `class `[RemoteMessage.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Builder) Builder object for constructing [RemoteMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage) instances.                                                                                                                                 |
| `@`[IntDef](https://developer.android.com/reference/kotlin/androidx/annotation/IntDef.html)`(value = )` `@`[Retention](https://developer.android.com/reference/kotlin/java/lang/annotation/Retention.html)`(value = RetentionPolicy.SOURCE)` `annotation `[RemoteMessage.MessagePriority](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.MessagePriority) Priority of the message |
| `class `[RemoteMessage.Notification](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification) Remote Firebase notification details.                                                                                                                                                                                                                                           |

|                                   ### Constants                                    |
|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [PRIORITY_HIGH](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#PRIORITY_HIGH())` = 1`       |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [PRIORITY_NORMAL](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#PRIORITY_NORMAL())` = 2`   |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [PRIORITY_UNKNOWN](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#PRIORITY_UNKNOWN())` = 0` |

|                                ### Public functions                                 |
|-------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | [getCollapseKey](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#getCollapseKey())`()` Gets the collapse key of the message.                                                                                                                                                              |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | [getFrom](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#getFrom())`()` Get the sender of this message.                                                                                                                                                                                  |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | [getMessageId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#getMessageId())`()` Gets the message's ID.                                                                                                                                                                                 |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | [getMessageType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#getMessageType())`()` Gets the type of message.                                                                                                                                                                          |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)          | `@`[RemoteMessage.MessagePriority](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.MessagePriority) [getOriginalPriority](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#getOriginalPriority())`()` Gets the original priority of message. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)          | `@`[RemoteMessage.MessagePriority](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.MessagePriority) [getPriority](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#getPriority())`()` Gets the priority of message as delivered.             |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | [getSenderId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#getSenderId())`()` Gets the Sender ID for the sender of this message.                                                                                                                                                       |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)        | [getSentTime](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#getSentTime())`()` Gets the time in milliseconds from the Epoch that the message was sent.                                                                                                                                  |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | ~~[getTo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#getTo())~~`()` **This function is deprecated.** This function is actually **decommissioned** along with all of FCM upstream messaging. <br />                                                                                   |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)          | [getTtl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#getTtl())`()` Gets the message time to live (TTL) in seconds.                                                                                                                                                                    |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)        | [writeToParcel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#writeToParcel(android.os.Parcel,int))`(out: `[Parcel](https://developer.android.com/reference/kotlin/android/os/Parcel.html)`, flags: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`)`      |

|                                                                                                                                                                            ### Public properties                                                                                                                                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!, `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!>!` | [data](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#data())                 |
| [RemoteMessage.Notification](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Notification)`!`                                                                                                                                                                                                                                 | [notification](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#notification()) |

|                                                                                                                                                                                                                                                                                                                                                                                                        ### Inherited Constants                                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/kotlin/android/os/Parcelable.html) |------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------| | `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [CONTENTS_FILE_DESCRIPTOR](https://developer.android.com/reference/kotlin/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR--)` = 1`           | | `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [PARCELABLE_WRITE_RETURN_VALUE](https://developer.android.com/reference/kotlin/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE--)` = 1` | |
| From [com.google.android.gms.common.internal.safeparcel.SafeParcelable](https://firebase.google.com/docs/reference/kotlin/com/google/android/gms/common/internal/safeparcel/SafeParcelable) |---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [NULL](https://firebase.google.com/docs/reference/kotlin/com/google/android/gms/common/internal/safeparcel/SafeParcelable#NULL())` = "SAFE_PARCELABLE_NULL_STRING"` |                                                                                               |

|                                                                                                                                                                                                                                                                                                                                                  ### Inherited functions                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [com.google.android.gms.common.internal.safeparcel.AbstractSafeParcelable](https://firebase.google.com/docs/reference/kotlin/com/google/android/gms/common/internal/safeparcel/AbstractSafeParcelable) |----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------| | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [describeContents](https://firebase.google.com/docs/reference/kotlin/com/google/android/gms/common/internal/safeparcel/AbstractSafeParcelable#describeContents())`()` | |

## Constants

### PRIORITY_HIGH

```
constÂ valÂ PRIORITY_HIGH = 1:Â Int
```  

### PRIORITY_NORMAL

```
constÂ valÂ PRIORITY_NORMAL = 2:Â Int
```  

### PRIORITY_UNKNOWN

```
constÂ valÂ PRIORITY_UNKNOWN = 0:Â Int
```  

## Public functions

### getCollapseKey

```
funÂ getCollapseKey():Â String?
```

Gets the collapse key of the message.  

|                                       Returns                                       |
|-------------------------------------------------------------------------------------|------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The collapse key |

### getFrom

```
funÂ getFrom():Â String?
```

Get the sender of this message.

This will be the sender ID or the topic for topic messages.  

|                                       Returns                                       |
|-------------------------------------------------------------------------------------|--------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The message sender |

### getMessageId

```
funÂ getMessageId():Â String?
```

Gets the message's ID.

This is automatically generated by the server. Treat it as an opaque string. Do not rely on its format to be consistent.  

|                                       Returns                                       |
|-------------------------------------------------------------------------------------|----------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The message ID |

### getMessageType

```
funÂ getMessageType():Â String?
```

Gets the type of message.  

|                                       Returns                                       |
|-------------------------------------------------------------------------------------|------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The message type |

### getOriginalPriority

```
@RemoteMessage.MessagePriority
funÂ getOriginalPriority():Â Int
```

Gets the original priority of message.  

|                                  Returns                                   |
|----------------------------------------------------------------------------|-------------------------------|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | The original message priority |

### getPriority

```
@RemoteMessage.MessagePriority
funÂ getPriority():Â Int
```

Gets the priority of message as delivered. This may be lower than the priority originally requested.  

|                                  Returns                                   |
|----------------------------------------------------------------------------|-----------------------------------|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | The message priority as delivered |

### getSenderId

```
funÂ getSenderId():Â String?
```

Gets the Sender ID for the sender of this message.  

|                                       Returns                                       |
|-------------------------------------------------------------------------------------|-----------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | the message Sender ID |

### getSentTime

```
funÂ getSentTime():Â Long
```

Gets the time in milliseconds from the Epoch that the message was sent.  

|                                   Returns                                    |
|------------------------------------------------------------------------------|------------------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | The time that the message was sent |

### getTo

```
funÂ [getTo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage#getTo())():Â String?
```
| **This function is deprecated.**   
|
| This function is actually **decommissioned** along with all of FCM upstream messaging. Learn more in the [FAQ about FCM features deprecated in June 2023](https://firebase.google.com/support/faq#fcm-23-deprecation).

Gets the message destination.  

### getTtl

```
funÂ getTtl():Â Int
```

Gets the message time to live (TTL) in seconds.  

|                                  Returns                                   |
|----------------------------------------------------------------------------|-----------------|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | The message TTL |

### writeToParcel

```
funÂ writeToParcel(out:Â Parcel,Â flags:Â Int):Â Unit
```  

## Public properties

### data

```
valÂ data:Â (Mutable)Map<String!,Â String!>!
```  

### notification

```
valÂ notification:Â RemoteMessage.Notification!
```