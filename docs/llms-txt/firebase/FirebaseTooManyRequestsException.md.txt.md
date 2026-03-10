# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseTooManyRequestsException.md.txt

# FirebaseTooManyRequestsException

# FirebaseTooManyRequestsException


```
public class FirebaseTooManyRequestsException extends FirebaseException
```

<br />

|---|---|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) ||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html) |||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException) ||
|   |   |   | ↳ | [com.google.firebase.FirebaseTooManyRequestsException](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseTooManyRequestsException) |

*** ** * ** ***

Exception thrown when a request to a Firebase service has been blocked due to having received too many consecutive requests from the same device. Retry the request later to resolve.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseTooManyRequestsException#FirebaseTooManyRequestsException(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html message)` |

| ### Inherited methods |
|---|
| From [java.lang.Throwable](https://developer.android.com/reference/kotlin/java/lang/Throwable.html) |---|---| | `synchronized final void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#addSuppressed-java.lang.Throwable-(https://developer.android.com/reference/kotlin/java/lang/Throwable.html exception)` | | `synchronized https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#fillInStackTrace--()` | | `synchronized https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getCause--()` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getLocalizedMessage--()` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getMessage--()` | | `StackTraceElement[]` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getStackTrace--()` | | `synchronized final Throwable[]` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getSuppressed--()` | | `synchronized https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#initCause-java.lang.Throwable-(https://developer.android.com/reference/kotlin/java/lang/Throwable.html cause)` | | `void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#printStackTrace--()` | | `void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#setStackTrace-java.lang.StackTraceElement[]-(StackTraceElement[] stackTrace)` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#toString--()` | |

## Public constructors

### FirebaseTooManyRequestsException

```
public FirebaseTooManyRequestsException(@NonNull String message)
```