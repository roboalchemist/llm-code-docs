# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.md.txt

# FirebaseAppDistributionException

# FirebaseAppDistributionException


```
public class FirebaseAppDistributionException extends FirebaseException
```

<br />

|---|---|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) ||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html) |||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException) ||
|   |   |   | ↳ | [com.google.firebase.appdistribution.FirebaseAppDistributionException](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException) |

*** ** * ** ***

The class for all Exceptions thrown by `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistribution`.

## Summary

| ### Nested types |
|---|
| `public enum https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status` Enum for potential error statuses that caused the `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException`. |

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException#release()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException#getErrorCode()()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status` that caused the exception. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException#getRelease()()` Returns the release that was ready to be installed when the error was thrown. |

| ### Inherited methods |
|---|
| From [java.lang.Throwable](https://developer.android.com/reference/kotlin/java/lang/Throwable.html) |---|---| | `synchronized final void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#addSuppressed-java.lang.Throwable-(https://developer.android.com/reference/kotlin/java/lang/Throwable.html exception)` | | `synchronized https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#fillInStackTrace--()` | | `synchronized https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getCause--()` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getLocalizedMessage--()` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getMessage--()` | | `StackTraceElement[]` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getStackTrace--()` | | `synchronized final Throwable[]` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getSuppressed--()` | | `synchronized https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#initCause-java.lang.Throwable-(https://developer.android.com/reference/kotlin/java/lang/Throwable.html cause)` | | `void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#printStackTrace--()` | | `void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#setStackTrace-java.lang.StackTraceElement[]-(StackTraceElement[] stackTrace)` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#toString--()` | |

## Public fields

### release

```
public final @Nullable AppDistributionRelease release
```

## Public methods

### getErrorCode

```
public @NonNull FirebaseAppDistributionException.Status getErrorCode()
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/FirebaseAppDistributionException.Status` that caused the exception.

### getRelease

```
public @Nullable AppDistributionRelease getRelease()
```

Returns the release that was ready to be installed when the error was thrown.