# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException.md.txt

# FirebaseRemoteConfigServerException

# FirebaseRemoteConfigServerException


```
public class FirebaseRemoteConfigServerException extends FirebaseRemoteConfigException
```

<br />

|---|---|---|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) ||||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html) ||||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException) |||
|   |   |   | ↳ | [com.google.firebase.remoteconfig.FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) ||
|   |   |   |   | ↳ | [com.google.firebase.remoteconfig.FirebaseRemoteConfigServerException](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException) |

*** ** * ** ***

A Firebase Remote Config internal issue caused by an interaction with the Firebase Remote Config server.

## Summary

| ### Public fields |
|---|---|
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException#httpStatusCode()` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException#FirebaseRemoteConfigServerException(java.lang.String,com.google.firebase.remoteconfig.FirebaseRemoteConfigException.Code)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html detailMessage, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code code )` Creates a Firebase Remote Config server exception with the given message and ` FirebaseRemoteConfigException` code. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException#FirebaseRemoteConfigServerException(int,java.lang.String)( int httpStatusCode, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html detailMessage )` Creates a Firebase Remote Config server exception with the given message and HTTP status code. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException#FirebaseRemoteConfigServerException(java.lang.String,java.lang.Throwable,com.google.firebase.remoteconfig.FirebaseRemoteConfigException.Code)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html detailMessage, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html cause, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code code )` Creates a Firebase Remote Config server exception with the given message, exception cause, and `FirebaseRemoteConfigException` code. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException#FirebaseRemoteConfigServerException(int,java.lang.String,java.lang.Throwable)( int httpStatusCode, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html detailMessage, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html cause )` Creates a Firebase Remote Config server exception with the given message, HTTP status code and |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException#FirebaseRemoteConfigServerException(int,java.lang.String,com.google.firebase.remoteconfig.FirebaseRemoteConfigException.Code)( int httpStatusCode, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html detailMessage, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code code )` Creates a Firebase Remote Config server exception with the HTTP status code, given message, and `FirebaseRemoteConfigException` code. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException#FirebaseRemoteConfigServerException(int,java.lang.String,java.lang.Throwable,com.google.firebase.remoteconfig.FirebaseRemoteConfigException.Code)( int httpStatusCode, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html detailMessage, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html cause, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code code )` Creates a Firebase Remote Config server exception with the HTTP status code, given message, exception cause, and `FirebaseRemoteConfigException` code. |

| ### Public methods |
|---|---|
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException#getHttpStatusCode()()` Gets the HTTP status code of the failed Firebase Remote Config server operation. |

| ### Inherited fields |
|---|
| From [com.google.firebase.remoteconfig.FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) |---|---| | `final https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException#code()` Code that specifies the type of exception. | |

| ### Inherited methods |
|---|
| From [com.google.firebase.remoteconfig.FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) |---|---| | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException#getCode()()` Gets the `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code` representing the type of exception. | |
| From [java.lang.Throwable](https://developer.android.com/reference/kotlin/java/lang/Throwable.html) |---|---| | `synchronized final void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#addSuppressed-java.lang.Throwable-(https://developer.android.com/reference/kotlin/java/lang/Throwable.html exception)` | | `synchronized https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#fillInStackTrace--()` | | `synchronized https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getCause--()` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getLocalizedMessage--()` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getMessage--()` | | `StackTraceElement[]` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getStackTrace--()` | | `synchronized final Throwable[]` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getSuppressed--()` | | `synchronized https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#initCause-java.lang.Throwable-(https://developer.android.com/reference/kotlin/java/lang/Throwable.html cause)` | | `void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#printStackTrace--()` | | `void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#setStackTrace-java.lang.StackTraceElement[]-(StackTraceElement[] stackTrace)` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#toString--()` | |

## Public fields

### httpStatusCode

```
public final int httpStatusCode
```

## Public constructors

### FirebaseRemoteConfigServerException

```
public FirebaseRemoteConfigServerException(
    @NonNull String detailMessage,
    @NonNull FirebaseRemoteConfigException.Code code
)
```

Creates a Firebase Remote Config server exception with the given message and `
FirebaseRemoteConfigException` code.

### FirebaseRemoteConfigServerException

```
public FirebaseRemoteConfigServerException(
    int httpStatusCode,
    @NonNull String detailMessage
)
```

Creates a Firebase Remote Config server exception with the given message and HTTP status code.

### FirebaseRemoteConfigServerException

```
public FirebaseRemoteConfigServerException(
    @NonNull String detailMessage,
    @Nullable Throwable cause,
    @NonNull FirebaseRemoteConfigException.Code code
)
```

Creates a Firebase Remote Config server exception with the given message, exception cause, and `FirebaseRemoteConfigException` code.

### FirebaseRemoteConfigServerException

```
public FirebaseRemoteConfigServerException(
    int httpStatusCode,
    @NonNull String detailMessage,
    @Nullable Throwable cause
)
```

Creates a Firebase Remote Config server exception with the given message, HTTP status code and

### FirebaseRemoteConfigServerException

```
public FirebaseRemoteConfigServerException(
    int httpStatusCode,
    @NonNull String detailMessage,
    @NonNull FirebaseRemoteConfigException.Code code
)
```

Creates a Firebase Remote Config server exception with the HTTP status code, given message, and `FirebaseRemoteConfigException` code.

### FirebaseRemoteConfigServerException

```
public FirebaseRemoteConfigServerException(
    int httpStatusCode,
    @NonNull String detailMessage,
    @Nullable Throwable cause,
    @NonNull FirebaseRemoteConfigException.Code code
)
```

Creates a Firebase Remote Config server exception with the HTTP status code, given message, exception cause, and `FirebaseRemoteConfigException` code.

## Public methods

### getHttpStatusCode

```
public int getHttpStatusCode()
```

Gets the HTTP status code of the failed Firebase Remote Config server operation.