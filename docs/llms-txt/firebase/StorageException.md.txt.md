# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException.md.txt

# StorageException

# StorageException


```
public class StorageException extends FirebaseException
```

<br />

|---|---|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) ||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html) |||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException) ||
|   |   |   | ↳ | [com.google.firebase.storage.StorageException](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException) |

*** ** * ** ***

Represents an Exception resulting from an operation on a `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`.

## Summary

| ### Nested types |
|---|
| `@https://developer.android.com/reference/kotlin/java/lang/annotation/Retention.html(value = RetentionPolicy.SOURCE) @https://developer.android.com/reference/kotlin/androidx/annotation/IntDef.html(value = ) public annotation https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException.ErrorCode` An `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException.ErrorCode` indicates the source of a failed StorageTask or operation. |

| ### Constants |
|---|---|
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException#ERROR_BUCKET_NOT_FOUND() = -13011` |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException#ERROR_CANCELED() = -13040` |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException#ERROR_INVALID_CHECKSUM() = -13031` |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException#ERROR_NOT_AUTHENTICATED() = -13020` |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException#ERROR_NOT_AUTHORIZED() = -13021` |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException#ERROR_OBJECT_NOT_FOUND() = -13010` |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException#ERROR_PROJECT_NOT_FOUND() = -13012` |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException#ERROR_QUOTA_EXCEEDED() = -13013` |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException#ERROR_RETRY_LIMIT_EXCEEDED() = -13030` |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException#ERROR_UNKNOWN() = -13000` |

| ### Public fields |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException#cause()` |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException#errorCode()` |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException#httpResultCode()` |

| ### Public methods |
|---|---|
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException#fromErrorStatus(com.google.android.gms.common.api.Status)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/common/api/Status.html status)` |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException#fromException(java.lang.Throwable)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html exception)` |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException#fromExceptionAndHttpCode(java.lang.Throwable,int)( @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html exception, int httpResultCode )` |
| `synchronized @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException#getCause()()` Returns the cause of this `Throwable`, or `null` if there is no cause. |
| `int` | `@https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException.ErrorCode https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException#getErrorCode()()` |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException#getHttpResultCode()()` |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException#getIsRecoverableException()()` |

| ### Inherited methods |
|---|
| From [java.lang.Throwable](https://developer.android.com/reference/kotlin/java/lang/Throwable.html) |---|---| | `synchronized final void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#addSuppressed-java.lang.Throwable-(https://developer.android.com/reference/kotlin/java/lang/Throwable.html exception)` | | `synchronized https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#fillInStackTrace--()` | | `synchronized https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getCause--()` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getLocalizedMessage--()` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getMessage--()` | | `StackTraceElement[]` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getStackTrace--()` | | `synchronized final Throwable[]` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getSuppressed--()` | | `synchronized https://developer.android.com/reference/kotlin/java/lang/Throwable.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#initCause-java.lang.Throwable-(https://developer.android.com/reference/kotlin/java/lang/Throwable.html cause)` | | `void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#printStackTrace--()` | | `void` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#setStackTrace-java.lang.StackTraceElement[]-(StackTraceElement[] stackTrace)` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://developer.android.com/reference/kotlin/java/lang/Throwable.html#toString--()` | |

## Constants

### ERROR_BUCKET_NOT_FOUND

```
public static final int ERROR_BUCKET_NOT_FOUND = -13011
```

### ERROR_CANCELED

```
public static final int ERROR_CANCELED = -13040
```

### ERROR_INVALID_CHECKSUM

```
public static final int ERROR_INVALID_CHECKSUM = -13031
```

### ERROR_NOT_AUTHENTICATED

```
public static final int ERROR_NOT_AUTHENTICATED = -13020
```

### ERROR_NOT_AUTHORIZED

```
public static final int ERROR_NOT_AUTHORIZED = -13021
```

### ERROR_OBJECT_NOT_FOUND

```
public static final int ERROR_OBJECT_NOT_FOUND = -13010
```

### ERROR_PROJECT_NOT_FOUND

```
public static final int ERROR_PROJECT_NOT_FOUND = -13012
```

### ERROR_QUOTA_EXCEEDED

```
public static final int ERROR_QUOTA_EXCEEDED = -13013
```

### ERROR_RETRY_LIMIT_EXCEEDED

```
public static final int ERROR_RETRY_LIMIT_EXCEEDED = -13030
```

### ERROR_UNKNOWN

```
public static final int ERROR_UNKNOWN = -13000
```

## Public fields

### cause

```
public Throwable cause
```

### errorCode

```
public final int errorCode
```

### httpResultCode

```
public final int httpResultCode
```

## Public methods

### fromErrorStatus

```
public static @NonNull StorageException fromErrorStatus(@NonNull Status status)
```

### fromException

```
public static @NonNull StorageException fromException(@NonNull Throwable exception)
```

### fromExceptionAndHttpCode

```
public static @Nullable StorageException fromExceptionAndHttpCode(
    @Nullable Throwable exception,
    int httpResultCode
)
```

### getCause

```
synchronized public @Nullable Throwable getCause()
```

Returns the cause of this `Throwable`, or `null` if there is no cause.

### getErrorCode

```
@StorageException.ErrorCode
public int getErrorCode()
```

### getHttpResultCode

```
public int getHttpResultCode()
```

| Returns |
|---|---|
| `int` | the Http result code (if one exists) from a network operation. |

### getIsRecoverableException

```
public boolean getIsRecoverableException()
```

| Returns |
|---|---|
| `boolean` | True if this request failed due to a network condition that may be resolved in a future attempt. |