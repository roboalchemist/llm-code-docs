# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.md.txt

# FirebaseRemoteConfigException

# FirebaseRemoteConfigException


```
class FirebaseRemoteConfigException : FirebaseException
```

<br />

|---|---|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) ||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html) |||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseException) ||
|   |   |   | ↳ | [com.google.firebase.remoteconfig.FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) |

Known direct subclasses [FirebaseRemoteConfigClientException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigClientException), [FirebaseRemoteConfigFetchThrottledException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchThrottledException), [FirebaseRemoteConfigServerException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigClientException` | A Firebase Remote Config internal issue that isn't caused by an interaction with the Firebase Remote Config server. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchThrottledException` | An exception thrown when a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#fetch()` call is throttled. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException` | A Firebase Remote Config internal issue caused by an interaction with the Firebase Remote Config server. |

*** ** * ** ***

Base class for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` exceptions.

## Summary

| ### Nested types |
|---|
| `enum https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException#FirebaseRemoteConfigException(java.lang.String)(detailMessage: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates a Firebase Remote Config exception with the given message. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException#FirebaseRemoteConfigException(java.lang.String,java.lang.Throwable)(detailMessage: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, cause: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html?)` Creates a Firebase Remote Config exception with the given message and cause. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException#FirebaseRemoteConfigException(java.lang.String,com.google.firebase.remoteconfig.FirebaseRemoteConfigException.Code)( detailMessage: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, code: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code )` Creates a Firebase Remote Config exception with the given message and Code. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException#FirebaseRemoteConfigException(java.lang.String,java.lang.Throwable,com.google.firebase.remoteconfig.FirebaseRemoteConfigException.Code)( detailMessage: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, cause: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html?, code: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code )` Creates a Firebase Remote Config exception with the given message, cause, and Code. |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException#code()` Code that specifies the type of exception. |

| ### Inherited functions |
|---|
| From [java.lang.Throwable](https://developer.android.com/reference/kotlin/java/lang/Throwable.html) |---|---| | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/add-suppressed.html(exception: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!)` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/fill-in-stack-trace.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-cause.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-localized-message.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-message.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html!>!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-stack-trace.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!>!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-suppressed.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/init-cause.html(cause: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/set-stack-trace.html(stackTrace: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html!>!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/to-string.html()` | |

## Public constructors

### FirebaseRemoteConfigException

```
FirebaseRemoteConfigException(detailMessage: String)
```

Creates a Firebase Remote Config exception with the given message.

### FirebaseRemoteConfigException

```
FirebaseRemoteConfigException(detailMessage: String, cause: Throwable?)
```

Creates a Firebase Remote Config exception with the given message and cause.

### FirebaseRemoteConfigException

```
FirebaseRemoteConfigException(
    detailMessage: String,
    code: FirebaseRemoteConfigException.Code
)
```

Creates a Firebase Remote Config exception with the given message and Code.

### FirebaseRemoteConfigException

```
FirebaseRemoteConfigException(
    detailMessage: String,
    cause: Throwable?,
    code: FirebaseRemoteConfigException.Code
)
```

Creates a Firebase Remote Config exception with the given message, cause, and Code.

## Public properties

### code

```
val code: FirebaseRemoteConfigException.Code!
```

Code that specifies the type of exception.