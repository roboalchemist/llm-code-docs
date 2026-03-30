# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException.md.txt

# FirebaseRemoteConfigServerException

# FirebaseRemoteConfigServerException


```
class FirebaseRemoteConfigServerException : FirebaseRemoteConfigException
```

<br />

|---|---|---|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) ||||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html) ||||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseException) |||
|   |   |   | ↳ | [com.google.firebase.remoteconfig.FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) ||
|   |   |   |   | ↳ | [com.google.firebase.remoteconfig.FirebaseRemoteConfigServerException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException) |

*** ** * ** ***

A Firebase Remote Config internal issue caused by an interaction with the Firebase Remote Config server.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException#FirebaseRemoteConfigServerException(java.lang.String,com.google.firebase.remoteconfig.FirebaseRemoteConfigException.Code)( detailMessage: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, code: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code )` Creates a Firebase Remote Config server exception with the given message and ` FirebaseRemoteConfigException` code. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException#FirebaseRemoteConfigServerException(int,java.lang.String)( httpStatusCode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, detailMessage: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html )` Creates a Firebase Remote Config server exception with the given message and HTTP status code. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException#FirebaseRemoteConfigServerException(java.lang.String,java.lang.Throwable,com.google.firebase.remoteconfig.FirebaseRemoteConfigException.Code)( detailMessage: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, cause: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html?, code: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code )` Creates a Firebase Remote Config server exception with the given message, exception cause, and `FirebaseRemoteConfigException` code. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException#FirebaseRemoteConfigServerException(int,java.lang.String,java.lang.Throwable)( httpStatusCode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, detailMessage: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, cause: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html? )` Creates a Firebase Remote Config server exception with the given message, HTTP status code and |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException#FirebaseRemoteConfigServerException(int,java.lang.String,com.google.firebase.remoteconfig.FirebaseRemoteConfigException.Code)( httpStatusCode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, detailMessage: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, code: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code )` Creates a Firebase Remote Config server exception with the HTTP status code, given message, and `FirebaseRemoteConfigException` code. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException#FirebaseRemoteConfigServerException(int,java.lang.String,java.lang.Throwable,com.google.firebase.remoteconfig.FirebaseRemoteConfigException.Code)( httpStatusCode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, detailMessage: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, cause: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html?, code: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code )` Creates a Firebase Remote Config server exception with the HTTP status code, given message, exception cause, and `FirebaseRemoteConfigException` code. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException#httpStatusCode()` |

| ### Inherited functions |
|---|
| From [com.google.firebase.remoteconfig.FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) |---|---| | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException#getCode()()` Gets the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code` representing the type of exception. | |
| From [java.lang.Throwable](https://developer.android.com/reference/kotlin/java/lang/Throwable.html) |---|---| | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/add-suppressed.html(exception: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!)` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/fill-in-stack-trace.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-cause.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-localized-message.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-message.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html!>!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-stack-trace.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!>!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-suppressed.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/init-cause.html(cause: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/set-stack-trace.html(stackTrace: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html!>!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/to-string.html()` | |

| ### Inherited properties |
|---|
| From [com.google.firebase.remoteconfig.FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) |---|---| | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException#code()` Code that specifies the type of exception. | |

## Public constructors

### FirebaseRemoteConfigServerException

```
FirebaseRemoteConfigServerException(
    detailMessage: String,
    code: FirebaseRemoteConfigException.Code
)
```

Creates a Firebase Remote Config server exception with the given message and `
FirebaseRemoteConfigException` code.

### FirebaseRemoteConfigServerException

```
FirebaseRemoteConfigServerException(
    httpStatusCode: Int,
    detailMessage: String
)
```

Creates a Firebase Remote Config server exception with the given message and HTTP status code.

### FirebaseRemoteConfigServerException

```
FirebaseRemoteConfigServerException(
    detailMessage: String,
    cause: Throwable?,
    code: FirebaseRemoteConfigException.Code
)
```

Creates a Firebase Remote Config server exception with the given message, exception cause, and `FirebaseRemoteConfigException` code.

### FirebaseRemoteConfigServerException

```
FirebaseRemoteConfigServerException(
    httpStatusCode: Int,
    detailMessage: String,
    cause: Throwable?
)
```

Creates a Firebase Remote Config server exception with the given message, HTTP status code and

### FirebaseRemoteConfigServerException

```
FirebaseRemoteConfigServerException(
    httpStatusCode: Int,
    detailMessage: String,
    code: FirebaseRemoteConfigException.Code
)
```

Creates a Firebase Remote Config server exception with the HTTP status code, given message, and `FirebaseRemoteConfigException` code.

### FirebaseRemoteConfigServerException

```
FirebaseRemoteConfigServerException(
    httpStatusCode: Int,
    detailMessage: String,
    cause: Throwable?,
    code: FirebaseRemoteConfigException.Code
)
```

Creates a Firebase Remote Config server exception with the HTTP status code, given message, exception cause, and `FirebaseRemoteConfigException` code.

## Public properties

### httpStatusCode

```
val httpStatusCode: Int
```