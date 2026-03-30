# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/SendException.md.txt

# SendException

# SendException


```
public final class SendException extends Exception
```

<br />

|---|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) ||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html) ||
|   |   | ↳ | [com.google.firebase.messaging.SendException](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/SendException) |

*** ** * ** ***

Firebase message send exception.

This will be passed to `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessagingService#onSendError(java.lang.String,java.lang.Exception)` on errors that prevented a message from being sent via `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#send(com.google.firebase.messaging.RemoteMessage)`

## Summary

| ### Constants |
|---|---|
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/SendException#ERROR_INVALID_PARAMETERS() = 1` Message was sent with invalid parameters. |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/SendException#ERROR_SIZE() = 2` Message exceeded the maximum payload size. |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/SendException#ERROR_TOO_MANY_MESSAGES() = 4` App has too many pending messages so this one was dropped. |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/SendException#ERROR_TTL_EXCEEDED() = 3` Message time to live (TTL) was exceeded before the message could be sent. |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/SendException#ERROR_UNKNOWN() = 0` Unknown error. |

| ### Public fields |
|---|---|
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/SendException#errorCode()` |

| ### Public methods |
|---|---|
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/SendException#getErrorCode()()` |

| ### Inherited methods |
|---|
| From [java.lang.Throwable](https://developer.android.com/reference/kotlin/java/lang/Throwable.html) |---|---| | `synchronized final void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#addSuppressed-java.lang.Throwable-(https://developer.android.com/reference/kotlin/java/lang/Throwable.html exception)` | | `synchronized https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#fillInStackTrace--()` | | `synchronized https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getCause--()` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getLocalizedMessage--()` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getMessage--()` | | `StackTraceElement[]` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getStackTrace--()` | | `synchronized final Throwable[]` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getSuppressed--()` | | `synchronized https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#initCause-java.lang.Throwable-(https://developer.android.com/reference/kotlin/java/lang/Throwable.html cause)` | | `void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#printStackTrace--()` | | `void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#setStackTrace-java.lang.StackTraceElement[]-(StackTraceElement[] stackTrace)` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#toString--()` | |

## Constants

### ERROR_INVALID_PARAMETERS

```
public static final int ERROR_INVALID_PARAMETERS = 1
```

Message was sent with invalid parameters.

### ERROR_SIZE

```
public static final int ERROR_SIZE = 2
```

Message exceeded the maximum payload size.

### ERROR_TOO_MANY_MESSAGES

```
public static final int ERROR_TOO_MANY_MESSAGES = 4
```

App has too many pending messages so this one was dropped.

### ERROR_TTL_EXCEEDED

```
public static final int ERROR_TTL_EXCEEDED = 3
```

Message time to live (TTL) was exceeded before the message could be sent.

### ERROR_UNKNOWN

```
public static final int ERROR_UNKNOWN = 0
```

Unknown error.

## Public fields

### errorCode

```
public final int errorCode
```

## Public methods

### getErrorCode

```
public int getErrorCode()
```