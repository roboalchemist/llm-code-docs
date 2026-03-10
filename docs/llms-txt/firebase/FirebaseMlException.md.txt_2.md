# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException.md.txt

# FirebaseMlException

# FirebaseMlException


```
class FirebaseMlException : FirebaseException
```

<br />

|---|---|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||||
| ↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) ||||
|   | ↳ | [java.lang.Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html) |||
|   |   | ↳ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseException) ||
|   |   |   | ↳ | [com.google.firebase.ml.modeldownloader.FirebaseMlException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException) |

*** ** * ** ***

Represents an Exception resulting from an operation on a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader`. Error mappings should remain consistent with the original firebase_ml_sdk whenever possible.

## Summary

| ### Nested types |
|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/IntDef.html(value = ) @https://developer.android.com/reference/kotlin/java/lang/annotation/Retention.html(value = RetentionPolicy.CLASS) annotation https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException.Code` The set of Firebase ML status codes. |

| ### Constants |
|---|---|
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#ABORTED() = 10` The operation was aborted, typically due to a concurrency issue like transaction aborts, etc. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#ALREADY_EXISTS() = 6` Some resource that we attempted to create already exists. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#CANCELLED() = 1` The operation was cancelled (typically by the caller). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#DEADLINE_EXCEEDED() = 4` Deadline expired before operation could complete. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#DOWNLOAD_URL_EXPIRED() = 121` The download URL expired before download could complete. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#FAILED_PRECONDITION() = 9` Operation was rejected because the system is not in a state required for the operation's execution. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#INTERNAL() = 13` Internal errors. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#INVALID_ARGUMENT() = 3` Client specified an invalid argument. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#MODEL_HASH_MISMATCH() = 102` The downloaded model's hash doesn't match the expected value. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#NOT_ENOUGH_SPACE() = 101` There is not enough space left on the device. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#NOT_FOUND() = 5` Some requested resource was not found. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#NO_NETWORK_CONNECTION() = 17` There is no network connection. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#OUT_OF_RANGE() = 11` Operation was attempted past the valid range. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#PERMISSION_DENIED() = 7` The caller does not have permission to execute the specified operation. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#RESOURCE_EXHAUSTED() = 8` Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#UNAUTHENTICATED() = 16` The request does not have valid authentication credentials for the operation. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#UNAVAILABLE() = 14` The service is currently unavailable. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#UNIMPLEMENTED() = 12` Operation is not implemented or not supported/enabled. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#UNKNOWN() = 2` Unknown error or an error from a different error domain. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException.Code https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#code()` |

| ### Inherited functions |
|---|
| From [java.lang.Throwable](https://developer.android.com/reference/kotlin/java/lang/Throwable.html) |---|---| | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/add-suppressed.html(exception: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!)` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/fill-in-stack-trace.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-cause.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-localized-message.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-message.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html!>!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-stack-trace.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!>!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-suppressed.html()` | | `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/init-cause.html(cause: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/set-stack-trace.html(stackTrace: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html!>!)` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/to-string.html()` | |

## Constants

### ABORTED

```
const val ABORTED = 10: Int
```

The operation was aborted, typically due to a concurrency issue like transaction aborts, etc.

### ALREADY_EXISTS

```
const val ALREADY_EXISTS = 6: Int
```

Some resource that we attempted to create already exists.

### CANCELLED

```
const val CANCELLED = 1: Int
```

The operation was cancelled (typically by the caller).

### DEADLINE_EXCEEDED

```
const val DEADLINE_EXCEEDED = 4: Int
```

Deadline expired before operation could complete. For operations that change the state of the system, this error may be returned even if the operation has completed successfully. For example, a successful response from a server could have been delayed long enough for the deadline to expire.

### DOWNLOAD_URL_EXPIRED

```
const val DOWNLOAD_URL_EXPIRED = 121: Int
```

The download URL expired before download could complete. Usually, multiple download attempts will be performed before this is returned.

### FAILED_PRECONDITION

```
const val FAILED_PRECONDITION = 9: Int
```

Operation was rejected because the system is not in a state required for the operation's execution.

### INTERNAL

```
const val INTERNAL = 13: Int
```

Internal errors. Means some invariant expected by underlying system has been broken. If you see one of these errors, something is very broken.

### INVALID_ARGUMENT

```
const val INVALID_ARGUMENT = 3: Int
```

Client specified an invalid argument. Note that this differs from `FAILED_PRECONDITION
`. `INVALID_ARGUMENT` indicates arguments that are problematic regardless of the state of the system (for example, an invalid field name).

### MODEL_HASH_MISMATCH

```
const val MODEL_HASH_MISMATCH = 102: Int
```

The downloaded model's hash doesn't match the expected value.

### NOT_ENOUGH_SPACE

```
const val NOT_ENOUGH_SPACE = 101: Int
```

There is not enough space left on the device.

### NOT_FOUND

```
const val NOT_FOUND = 5: Int
```

Some requested resource was not found.

### NO_NETWORK_CONNECTION

```
const val NO_NETWORK_CONNECTION = 17: Int
```

There is no network connection.

### OUT_OF_RANGE

```
const val OUT_OF_RANGE = 11: Int
```

Operation was attempted past the valid range.

### PERMISSION_DENIED

```
const val PERMISSION_DENIED = 7: Int
```

The caller does not have permission to execute the specified operation.

### RESOURCE_EXHAUSTED

```
const val RESOURCE_EXHAUSTED = 8: Int
```

Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space.

### UNAUTHENTICATED

```
const val UNAUTHENTICATED = 16: Int
```

The request does not have valid authentication credentials for the operation.

### UNAVAILABLE

```
const val UNAVAILABLE = 14: Int
```

The service is currently unavailable. This is a most likely a transient condition and may be corrected by retrying with a backoff.

In ML Model Downloader, this error is mostly about the models being not available yet.

### UNIMPLEMENTED

```
const val UNIMPLEMENTED = 12: Int
```

Operation is not implemented or not supported/enabled.

### UNKNOWN

```
const val UNKNOWN = 2: Int
```

Unknown error or an error from a different error domain.

## Public properties

### code

```
@FirebaseMlException.Code
val code: Int
```