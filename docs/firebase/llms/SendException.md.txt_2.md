# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/SendException.md.txt

# SendException

# SendException


```
class SendException : Exception
```

<br />

|---|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) ||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html) ||
|   |   | ↳ | [com.google.firebase.messaging.SendException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/SendException) |

*** ** * ** ***

Firebase message send exception.

This will be passed to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessagingService#onSendError(java.lang.String,java.lang.Exception)` on errors that prevented a message from being sent via `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/FirebaseMessaging#send(com.google.firebase.messaging.RemoteMessage)`

## Summary

| ### Constants |
|---|---|
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/SendException#ERROR_INVALID_PARAMETERS() = 1` Message was sent with invalid parameters. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/SendException#ERROR_SIZE() = 2` Message exceeded the maximum payload size. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/SendException#ERROR_TOO_MANY_MESSAGES() = 4` App has too many pending messages so this one was dropped. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/SendException#ERROR_TTL_EXCEEDED() = 3` Message time to live (TTL) was exceeded before the message could be sent. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/SendException#ERROR_UNKNOWN() = 0` Unknown error. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/messaging/SendException#errorCode()` |

| ### Inherited functions |
|---|
| From [java.lang.Throwable](https://developer.android.com/reference/kotlin/java/lang/Throwable.html) |---|---| | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/add-suppressed.html(exception: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!)` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/fill-in-stack-trace.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-cause.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-localized-message.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-message.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html!>!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-stack-trace.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!>!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-suppressed.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/init-cause.html(cause: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/set-stack-trace.html(stackTrace: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html!>!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/to-string.html()` | |

## Constants

### ERROR_INVALID_PARAMETERS

```
const val ERROR_INVALID_PARAMETERS = 1: Int
```

Message was sent with invalid parameters.

### ERROR_SIZE

```
const val ERROR_SIZE = 2: Int
```

Message exceeded the maximum payload size.

### ERROR_TOO_MANY_MESSAGES

```
const val ERROR_TOO_MANY_MESSAGES = 4: Int
```

App has too many pending messages so this one was dropped.

### ERROR_TTL_EXCEEDED

```
const val ERROR_TTL_EXCEEDED = 3: Int
```

Message time to live (TTL) was exceeded before the message could be sent.

### ERROR_UNKNOWN

```
const val ERROR_UNKNOWN = 0: Int
```

Unknown error.

## Public properties

### errorCode

```
val errorCode: Int
```