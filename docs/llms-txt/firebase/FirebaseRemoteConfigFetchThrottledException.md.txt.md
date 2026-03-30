# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchThrottledException.md.txt

# FirebaseRemoteConfigFetchThrottledException

# FirebaseRemoteConfigFetchThrottledException


```
public class FirebaseRemoteConfigFetchThrottledException extends FirebaseRemoteConfigException
```

<br />

|---|---|---|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) ||||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) |||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html) ||||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException) |||
|   |   |   | ↳ | [com.google.firebase.remoteconfig.FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) ||
|   |   |   |   | ↳ | [com.google.firebase.remoteconfig.FirebaseRemoteConfigFetchThrottledException](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchThrottledException) |

*** ** * ** ***

An exception thrown when a `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#fetch()` call is throttled.

## Summary

| ### Public fields |
|---|---|
| `final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchThrottledException#throttleEndTimeMillis()` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchThrottledException#FirebaseRemoteConfigFetchThrottledException(long)( long throttleEndTimeMillis )` Creates a throttled exception with the earliest time that a fetch call might be made without being throttled. |

| ### Public methods |
|---|---|
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchThrottledException#getThrottleEndTimeMillis()()` Returns the time, in millis since epoch, until which all fetch calls will be throttled. |

| ### Inherited fields |
|---|
| From [com.google.firebase.remoteconfig.FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) |---|---| | `final https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException#code()` Code that specifies the type of exception. | |

| ### Inherited methods |
|---|
| From [com.google.firebase.remoteconfig.FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) |---|---| | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException#getCode()()` Gets the `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code` representing the type of exception. | |
| From [java.lang.Throwable](https://developer.android.com/reference/kotlin/java/lang/Throwable.html) |---|---| | `synchronized final void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#addSuppressed-java.lang.Throwable-(https://developer.android.com/reference/kotlin/java/lang/Throwable.html exception)` | | `synchronized https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#fillInStackTrace--()` | | `synchronized https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getCause--()` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getLocalizedMessage--()` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getMessage--()` | | `StackTraceElement[]` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getStackTrace--()` | | `synchronized final Throwable[]` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getSuppressed--()` | | `synchronized https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#initCause-java.lang.Throwable-(https://developer.android.com/reference/kotlin/java/lang/Throwable.html cause)` | | `void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#printStackTrace--()` | | `void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#setStackTrace-java.lang.StackTraceElement[]-(StackTraceElement[] stackTrace)` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#toString--()` | |

## Public fields

### throttleEndTimeMillis

```
public final long throttleEndTimeMillis
```

## Public constructors

### FirebaseRemoteConfigFetchThrottledException

```
public FirebaseRemoteConfigFetchThrottledException(
    long throttleEndTimeMillis
)
```

Creates a throttled exception with the earliest time that a fetch call might be made without being throttled.

| Parameters |
|---|---|
| `long throttleEndTimeMillis` | the time, in millis since epoch, until which all fetch calls will be throttled. |

## Public methods

### getThrottleEndTimeMillis

```
public long getThrottleEndTimeMillis()
```

Returns the time, in millis since epoch, until which all fetch calls will be throttled.