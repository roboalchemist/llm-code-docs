# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Builder.md.txt

# RemoteMessage.Builder

# RemoteMessage.Builder


```
class RemoteMessage.Builder
```

<br />

*** ** * ** ***

Builder object for constructing [RemoteMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage) instances.

## Summary

|                                                                                                                          ### Public constructors                                                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Builder#Builder(java.lang.String))`(to: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Sets the destination of the message. |

|                                                      ### Public functions                                                      |
|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [RemoteMessage.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Builder) | [addData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Builder#addData(java.lang.String,java.lang.String))`(key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Adds a data key value pair to the message. |
| [RemoteMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage)                 | [build](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Builder#build())`()` Build a RemoteMessage instance.                                                                                                                                                                                                                                    |
| [RemoteMessage.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Builder) | [clearData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Builder#clearData())`()` Clears the message data.                                                                                                                                                                                                                                   |
| [RemoteMessage.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Builder) | [setCollapseKey](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Builder#setCollapseKey(java.lang.String))`(collapseKey: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Sets the collapse key of the message.                                                                                            |
| [RemoteMessage.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Builder) | [setMessageId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Builder#setMessageId(java.lang.String))`(messageId: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Sets the messages ID.                                                                                                                   |
| [RemoteMessage.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Builder) | [setMessageType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Builder#setMessageType(java.lang.String))`(messageType: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Sets the type of message.                                                                                                        |
| [RemoteMessage.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Builder) | [setTtl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Builder#setTtl(int))`(ttl: @`[IntRange](https://developer.android.com/reference/kotlin/androidx/annotation/IntRange.html)`(from = 0, to = 86400) `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`)` Sets the message time to live in seconds.              |

|                                                                                                                                                                            ### Public properties                                                                                                                                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!, `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!>!` | [data](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/RemoteMessage.Builder#data()) |

## Public constructors

### Builder

```
Builder(to:Â String)
```

Sets the destination of the message.  

|                                       Parameters                                       |
|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| `to: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The destination of the message in the format of ` SENDER_ID@fcm.googleapis.com`. The `SENDER_ID` should be the FirebaseApp gcm sender id. |

## Public functions

### addData

```
funÂ addData(key:Â String,Â value:Â String?):Â RemoteMessage.Builder
```

Adds a data key value pair to the message.

An existing value with the same key will be replaced by the new value.  

### build

```
funÂ build():Â RemoteMessage
```

Build a RemoteMessage instance.  

### clearData

```
funÂ clearData():Â RemoteMessage.Builder
```

Clears the message data.  

### setCollapseKey

```
funÂ setCollapseKey(collapseKey:Â String?):Â RemoteMessage.Builder
```

Sets the collapse key of the message.

A pending message will be replaced by a new message with the same collapse key if it is currently unable to be delivered to the recipient.  

### setMessageId

```
funÂ setMessageId(messageId:Â String):Â RemoteMessage.Builder
```

Sets the messages ID.  

|                                          Parameters                                           |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| `messageId: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | ID of the message. This is generated by the application. It must be unique for each message. This allows error callbacks and debugging. |

### setMessageType

```
funÂ setMessageType(messageType:Â String?):Â RemoteMessage.Builder
```

Sets the type of message.  

### setTtl

```
funÂ setTtl(ttl:Â @IntRange(fromÂ =Â 0,Â toÂ =Â 86400) Int):Â RemoteMessage.Builder
```

Sets the message time to live in seconds.

If 0, the message send will be attempted immediately and will be dropped if the device is not connected. Otherwise, the message will be queued.  

## Public properties

### data

```
varÂ data:Â (Mutable)Map<String!,Â String!>!
```