# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.md.txt

# FirebaseRemoteConfigException

# FirebaseRemoteConfigException


```
public class FirebaseRemoteConfigException extends FirebaseException
```

<br />

|---|---|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) ||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html) |||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException) ||
|   |   |   | ↳ | [com.google.firebase.remoteconfig.FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) |

Known direct subclasses [FirebaseRemoteConfigClientException](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigClientException), [FirebaseRemoteConfigFetchThrottledException](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchThrottledException), [FirebaseRemoteConfigServerException](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException)

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigClientException` | A Firebase Remote Config internal issue that isn't caused by an interaction with the Firebase Remote Config server. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchThrottledException` | An exception thrown when a `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#fetch()` call is throttled. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException` | A Firebase Remote Config internal issue caused by an interaction with the Firebase Remote Config server. |

*** ** * ** ***

Base class for `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig` exceptions.

## Summary

| ### Nested types |
|---|
| `public enum https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code` |

| ### Public fields |
|---|---|
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException#code()` Code that specifies the type of exception. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException#FirebaseRemoteConfigException(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html detailMessage)` Creates a Firebase Remote Config exception with the given message. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException#FirebaseRemoteConfigException(java.lang.String,java.lang.Throwable)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html detailMessage, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html cause )` Creates a Firebase Remote Config exception with the given message and cause. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException#FirebaseRemoteConfigException(java.lang.String,com.google.firebase.remoteconfig.FirebaseRemoteConfigException.Code)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html detailMessage, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code code )` Creates a Firebase Remote Config exception with the given message and Code. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException#FirebaseRemoteConfigException(java.lang.String,java.lang.Throwable,com.google.firebase.remoteconfig.FirebaseRemoteConfigException.Code)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html detailMessage, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html cause, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code code )` Creates a Firebase Remote Config exception with the given message, cause, and Code. |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException#getCode()()` Gets the `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code` representing the type of exception. |

| ### Inherited methods |
|---|
| From [java.lang.Throwable](https://developer.android.com/reference/kotlin/java/lang/Throwable.html) |---|---| | `synchronized final void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#addSuppressed-java.lang.Throwable-(https://developer.android.com/reference/kotlin/java/lang/Throwable.html exception)` | | `synchronized https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#fillInStackTrace--()` | | `synchronized https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getCause--()` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getLocalizedMessage--()` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getMessage--()` | | `StackTraceElement[]` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getStackTrace--()` | | `synchronized final Throwable[]` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getSuppressed--()` | | `synchronized https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#initCause-java.lang.Throwable-(https://developer.android.com/reference/kotlin/java/lang/Throwable.html cause)` | | `void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#printStackTrace--()` | | `void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#setStackTrace-java.lang.StackTraceElement[]-(StackTraceElement[] stackTrace)` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#toString--()` | |

## Public fields

### code

```
public final FirebaseRemoteConfigException.Code code
```

Code that specifies the type of exception.

## Public constructors

### FirebaseRemoteConfigException

```
public FirebaseRemoteConfigException(@NonNull String detailMessage)
```

Creates a Firebase Remote Config exception with the given message.

### FirebaseRemoteConfigException

```
public FirebaseRemoteConfigException(
    @NonNull String detailMessage,
    @Nullable Throwable cause
)
```

Creates a Firebase Remote Config exception with the given message and cause.

### FirebaseRemoteConfigException

```
public FirebaseRemoteConfigException(
    @NonNull String detailMessage,
    @NonNull FirebaseRemoteConfigException.Code code
)
```

Creates a Firebase Remote Config exception with the given message and Code.

### FirebaseRemoteConfigException

```
public FirebaseRemoteConfigException(
    @NonNull String detailMessage,
    @Nullable Throwable cause,
    @NonNull FirebaseRemoteConfigException.Code code
)
```

Creates a Firebase Remote Config exception with the given message, cause, and Code.

## Public methods

### getCode

```
public @NonNull FirebaseRemoteConfigException.Code getCode()
```

Gets the `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code` representing the type of exception.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code` representing the type of exception. |