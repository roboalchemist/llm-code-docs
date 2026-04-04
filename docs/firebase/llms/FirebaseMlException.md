# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/FirebaseMlException.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException.md.txt

# FirebaseMlException

# FirebaseMlException


```
class FirebaseMlException : FirebaseException
```

<br />

|---|---|---|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                                                      |||||
| â³ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)                                                                                       ||||
|   | â³ | [java.lang.Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html)                                                                                   |||
|   |   | â³ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseException)                                              ||
|   |   |   | â³ | [com.google.firebase.ml.modeldownloader.FirebaseMlException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException) |

*** ** * ** ***

Represents an Exception resulting from an operation on a [FirebaseModelDownloader](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader). Error mappings should remain consistent with the original firebase_ml_sdk whenever possible.

## Summary

|                                                                                                                                                                                                              ### Nested types                                                                                                                                                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[IntDef](https://developer.android.com/reference/kotlin/androidx/annotation/IntDef.html)`(value = )` `@`[Retention](https://developer.android.com/reference/kotlin/java/lang/annotation/Retention.html)`(value = RetentionPolicy.CLASS)` `annotation `[FirebaseMlException.Code](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException.Code) The set of Firebase ML status codes. |

|                                   ### Constants                                    |
|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [ABORTED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#ABORTED())` = 10` The operation was aborted, typically due to a concurrency issue like transaction aborts, etc.                                       |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [ALREADY_EXISTS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#ALREADY_EXISTS())` = 6` Some resource that we attempted to create already exists.                                                              |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [CANCELLED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#CANCELLED())` = 1` The operation was cancelled (typically by the caller).                                                                           |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [DEADLINE_EXCEEDED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#DEADLINE_EXCEEDED())` = 4` Deadline expired before operation could complete.                                                                |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [DOWNLOAD_URL_EXPIRED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#DOWNLOAD_URL_EXPIRED())` = 121` The download URL expired before download could complete.                                                 |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [FAILED_PRECONDITION](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#FAILED_PRECONDITION())` = 9` Operation was rejected because the system is not in a state required for the operation's execution.          |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [INTERNAL](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#INTERNAL())` = 13` Internal errors.                                                                                                                  |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [INVALID_ARGUMENT](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#INVALID_ARGUMENT())` = 3` Client specified an invalid argument.                                                                              |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [MODEL_HASH_MISMATCH](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#MODEL_HASH_MISMATCH())` = 102` The downloaded model's hash doesn't match the expected value.                                              |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [NOT_ENOUGH_SPACE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#NOT_ENOUGH_SPACE())` = 101` There is not enough space left on the device.                                                                    |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [NOT_FOUND](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#NOT_FOUND())` = 5` Some requested resource was not found.                                                                                           |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [NO_NETWORK_CONNECTION](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#NO_NETWORK_CONNECTION())` = 17` There is no network connection.                                                                         |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [OUT_OF_RANGE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#OUT_OF_RANGE())` = 11` Operation was attempted past the valid range.                                                                             |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [PERMISSION_DENIED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#PERMISSION_DENIED())` = 7` The caller does not have permission to execute the specified operation.                                          |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [RESOURCE_EXHAUSTED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#RESOURCE_EXHAUSTED())` = 8` Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space. |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [UNAUTHENTICATED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#UNAUTHENTICATED())` = 16` The request does not have valid authentication credentials for the operation.                                       |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [UNAVAILABLE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#UNAVAILABLE())` = 14` The service is currently unavailable.                                                                                       |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [UNIMPLEMENTED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#UNIMPLEMENTED())` = 12` Operation is not implemented or not supported/enabled.                                                                  |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [UNKNOWN](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#UNKNOWN())` = 2` Unknown error or an error from a different error domain.                                                                             |

|                           ### Public properties                            |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | `@`[FirebaseMlException.Code](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException.Code) [code](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException#code()) |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             ### Inherited functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [java.lang.Throwable](https://developer.android.com/reference/kotlin/java/lang/Throwable.html) |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `synchronized `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                 | [addSuppressed](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/add-suppressed.html)`(exception: `[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)`!)`                                                                                                    | | `synchronized `[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)`!`                                                                                    | [fillInStackTrace](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/fill-in-stack-trace.html)`()`                                                                                                                                                                                                | | `synchronized `[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)`!`                                                                                    | [getCause](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-cause.html)`()`                                                                                                                                                                                                                  | | [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                                                                                         | [getLocalizedMessage](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-localized-message.html)`()`                                                                                                                                                                                           | | [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                                                                                         | [getMessage](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-message.html)`()`                                                                                                                                                                                                              | | [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[StackTraceElement](https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html)`!>!`  | [getStackTrace](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-stack-trace.html)`()`                                                                                                                                                                                                       | | `synchronized `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)`!>!` | [getSuppressed](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-suppressed.html)`()`                                                                                                                                                                                                        | | `synchronized `[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)`!`                                                                                    | [initCause](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/init-cause.html)`(cause: `[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)`!)`                                                                                                                | | [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                | [printStackTrace](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html)`()`                                                                                                                                                                                                   | | [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                | [setStackTrace](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/set-stack-trace.html)`(stackTrace: `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[StackTraceElement](https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html)`!>!)` | | [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                                                                                         | [toString](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/to-string.html)`()`                                                                                                                                                                                                                  | |

## Constants

### ABORTED

```
constÂ valÂ ABORTED = 10:Â Int
```

The operation was aborted, typically due to a concurrency issue like transaction aborts, etc.  

### ALREADY_EXISTS

```
constÂ valÂ ALREADY_EXISTS = 6:Â Int
```

Some resource that we attempted to create already exists.  

### CANCELLED

```
constÂ valÂ CANCELLED = 1:Â Int
```

The operation was cancelled (typically by the caller).  

### DEADLINE_EXCEEDED

```
constÂ valÂ DEADLINE_EXCEEDED = 4:Â Int
```

Deadline expired before operation could complete. For operations that change the state of the system, this error may be returned even if the operation has completed successfully. For example, a successful response from a server could have been delayed long enough for the deadline to expire.  

### DOWNLOAD_URL_EXPIRED

```
constÂ valÂ DOWNLOAD_URL_EXPIRED = 121:Â Int
```

The download URL expired before download could complete. Usually, multiple download attempts will be performed before this is returned.  

### FAILED_PRECONDITION

```
constÂ valÂ FAILED_PRECONDITION = 9:Â Int
```

Operation was rejected because the system is not in a state required for the operation's execution.  

### INTERNAL

```
constÂ valÂ INTERNAL = 13:Â Int
```

Internal errors. Means some invariant expected by underlying system has been broken. If you see one of these errors, something is very broken.  

### INVALID_ARGUMENT

```
constÂ valÂ INVALID_ARGUMENT = 3:Â Int
```

Client specified an invalid argument. Note that this differs from `FAILED_PRECONDITION
`. `INVALID_ARGUMENT` indicates arguments that are problematic regardless of the state of the system (for example, an invalid field name).  

### MODEL_HASH_MISMATCH

```
constÂ valÂ MODEL_HASH_MISMATCH = 102:Â Int
```

The downloaded model's hash doesn't match the expected value.  

### NOT_ENOUGH_SPACE

```
constÂ valÂ NOT_ENOUGH_SPACE = 101:Â Int
```

There is not enough space left on the device.  

### NOT_FOUND

```
constÂ valÂ NOT_FOUND = 5:Â Int
```

Some requested resource was not found.  

### NO_NETWORK_CONNECTION

```
constÂ valÂ NO_NETWORK_CONNECTION = 17:Â Int
```

There is no network connection.  

### OUT_OF_RANGE

```
constÂ valÂ OUT_OF_RANGE = 11:Â Int
```

Operation was attempted past the valid range.  

### PERMISSION_DENIED

```
constÂ valÂ PERMISSION_DENIED = 7:Â Int
```

The caller does not have permission to execute the specified operation.  

### RESOURCE_EXHAUSTED

```
constÂ valÂ RESOURCE_EXHAUSTED = 8:Â Int
```

Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space.  

### UNAUTHENTICATED

```
constÂ valÂ UNAUTHENTICATED = 16:Â Int
```

The request does not have valid authentication credentials for the operation.  

### UNAVAILABLE

```
constÂ valÂ UNAVAILABLE = 14:Â Int
```

The service is currently unavailable. This is a most likely a transient condition and may be corrected by retrying with a backoff.

In ML Model Downloader, this error is mostly about the models being not available yet.  

### UNIMPLEMENTED

```
constÂ valÂ UNIMPLEMENTED = 12:Â Int
```

Operation is not implemented or not supported/enabled.  

### UNKNOWN

```
constÂ valÂ UNKNOWN = 2:Â Int
```

Unknown error or an error from a different error domain.  

## Public properties

### code

```
@FirebaseMlException.Code
valÂ code:Â Int
```