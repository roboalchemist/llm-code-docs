# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistributionException.md.txt

# FirebaseAppDistributionException

# FirebaseAppDistributionException


```
class FirebaseAppDistributionException : FirebaseException
```

<br />

|---|---|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) ||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html) |||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseException) ||
|   |   |   | ↳ | [com.google.firebase.appdistribution.FirebaseAppDistributionException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistributionException) |

*** ** * ** ***

The class for all Exceptions thrown by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution`.

## Summary

| ### Nested types |
|---|
| `enum https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status` Enum for potential error statuses that caused the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistributionException`. |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistributionException#getErrorCode()()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status` that caused the exception. |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistributionException#release()` |

| ### Inherited functions |
|---|
| From [java.lang.Throwable](https://developer.android.com/reference/kotlin/java/lang/Throwable.html) |---|---| | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/add-suppressed.html(exception: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!)` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/fill-in-stack-trace.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-cause.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-localized-message.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-message.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html!>!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-stack-trace.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!>!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-suppressed.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/init-cause.html(cause: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/set-stack-trace.html(stackTrace: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html!>!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/to-string.html()` | |

## Public functions

### getErrorCode

```
fun getErrorCode(): FirebaseAppDistributionException.Status
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status` that caused the exception.

## Public properties

### release

```
val release: AppDistributionRelease?
```