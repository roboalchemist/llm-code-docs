# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException.md.txt

# StorageException

# StorageException


```
class StorageException : FirebaseException
```

<br />

|---|---|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) ||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html) |||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseException) ||
|   |   |   | ↳ | [com.google.firebase.storage.StorageException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException) |

*** ** * ** ***

Represents an Exception resulting from an operation on a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`.

## Summary

| ### Nested types |
|---|
| `@https://developer.android.com/reference/kotlin/java/lang/annotation/Retention.html(value = RetentionPolicy.SOURCE) @https://developer.android.com/reference/kotlin/androidx/annotation/IntDef.html(value = ) annotation https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException.ErrorCode` An `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException.ErrorCode` indicates the source of a failed StorageTask or operation. |

| ### Constants |
|---|---|
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#ERROR_BUCKET_NOT_FOUND() = -13011` |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#ERROR_CANCELED() = -13040` |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#ERROR_INVALID_CHECKSUM() = -13031` |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#ERROR_NOT_AUTHENTICATED() = -13020` |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#ERROR_NOT_AUTHORIZED() = -13021` |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#ERROR_OBJECT_NOT_FOUND() = -13010` |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#ERROR_PROJECT_NOT_FOUND() = -13012` |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#ERROR_QUOTA_EXCEEDED() = -13013` |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#ERROR_RETRY_LIMIT_EXCEEDED() = -13030` |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#ERROR_UNKNOWN() = -13000` |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#fromErrorStatus(com.google.android.gms.common.api.Status)(status: https://developers.google.com/android/reference/com/google/android/gms/common/api/Status.html)` |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#fromException(java.lang.Throwable)(exception: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)` |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#fromExceptionAndHttpCode(java.lang.Throwable,int)(exception: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html?, httpResultCode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#getIsRecoverableException()()` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#cause()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#errorCode()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#httpResultCode()` |

| ### Inherited functions |
|---|
| From [java.lang.Throwable](https://developer.android.com/reference/kotlin/java/lang/Throwable.html) |---|---| | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/add-suppressed.html(exception: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!)` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/fill-in-stack-trace.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-cause.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-localized-message.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-message.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html!>!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-stack-trace.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!>!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-suppressed.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/init-cause.html(cause: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/set-stack-trace.html(stackTrace: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html!>!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/to-string.html()` | |

## Constants

### ERROR_BUCKET_NOT_FOUND

```
const val ERROR_BUCKET_NOT_FOUND = -13011: Int
```

### ERROR_CANCELED

```
const val ERROR_CANCELED = -13040: Int
```

### ERROR_INVALID_CHECKSUM

```
const val ERROR_INVALID_CHECKSUM = -13031: Int
```

### ERROR_NOT_AUTHENTICATED

```
const val ERROR_NOT_AUTHENTICATED = -13020: Int
```

### ERROR_NOT_AUTHORIZED

```
const val ERROR_NOT_AUTHORIZED = -13021: Int
```

### ERROR_OBJECT_NOT_FOUND

```
const val ERROR_OBJECT_NOT_FOUND = -13010: Int
```

### ERROR_PROJECT_NOT_FOUND

```
const val ERROR_PROJECT_NOT_FOUND = -13012: Int
```

### ERROR_QUOTA_EXCEEDED

```
const val ERROR_QUOTA_EXCEEDED = -13013: Int
```

### ERROR_RETRY_LIMIT_EXCEEDED

```
const val ERROR_RETRY_LIMIT_EXCEEDED = -13030: Int
```

### ERROR_UNKNOWN

```
const val ERROR_UNKNOWN = -13000: Int
```

## Public functions

### fromErrorStatus

```
java-static fun fromErrorStatus(status: Status): StorageException
```

### fromException

```
java-static fun fromException(exception: Throwable): StorageException
```

### fromExceptionAndHttpCode

```
java-static fun fromExceptionAndHttpCode(exception: Throwable?, httpResultCode: Int): StorageException?
```

### getIsRecoverableException

```
fun getIsRecoverableException(): Boolean
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | True if this request failed due to a network condition that may be resolved in a future attempt. |

## Public properties

### cause

```
val cause: Throwable!
```

### errorCode

```
val errorCode: Int
```

### httpResultCode

```
val httpResultCode: Int
```