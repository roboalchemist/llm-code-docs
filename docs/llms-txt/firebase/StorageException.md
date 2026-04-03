# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageException.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException.md.txt

# StorageException

# StorageException


```
class StorageException : FirebaseException
```

<br />

|---|---|---|---|------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                          |||||
| â³ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)                                                           ||||
|   | â³ | [java.lang.Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html)                                                       |||
|   |   | â³ | [com.google.firebase.FirebaseException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseException)                  ||
|   |   |   | â³ | [com.google.firebase.storage.StorageException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException) |

*** ** * ** ***

Represents an Exception resulting from an operation on a [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference).

## Summary

|                                                                                                                                                                                                                                                                                   ### Nested types                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[Retention](https://developer.android.com/reference/kotlin/java/lang/annotation/Retention.html)`(value = RetentionPolicy.SOURCE)` `@`[IntDef](https://developer.android.com/reference/kotlin/androidx/annotation/IntDef.html)`(value = )` `annotation `[StorageException.ErrorCode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException.ErrorCode) An [ErrorCode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException.ErrorCode) indicates the source of a failed StorageTask or operation. |

|                                   ### Constants                                    |
|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [ERROR_BUCKET_NOT_FOUND](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#ERROR_BUCKET_NOT_FOUND())` = -13011`         |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [ERROR_CANCELED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#ERROR_CANCELED())` = -13040`                         |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [ERROR_INVALID_CHECKSUM](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#ERROR_INVALID_CHECKSUM())` = -13031`         |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [ERROR_NOT_AUTHENTICATED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#ERROR_NOT_AUTHENTICATED())` = -13020`       |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [ERROR_NOT_AUTHORIZED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#ERROR_NOT_AUTHORIZED())` = -13021`             |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [ERROR_OBJECT_NOT_FOUND](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#ERROR_OBJECT_NOT_FOUND())` = -13010`         |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [ERROR_PROJECT_NOT_FOUND](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#ERROR_PROJECT_NOT_FOUND())` = -13012`       |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [ERROR_QUOTA_EXCEEDED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#ERROR_QUOTA_EXCEEDED())` = -13013`             |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [ERROR_RETRY_LIMIT_EXCEEDED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#ERROR_RETRY_LIMIT_EXCEEDED())` = -13030` |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [ERROR_UNKNOWN](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#ERROR_UNKNOWN())` = -13000`                           |

|                                                        ### Public functions                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java-static `[StorageException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException)    | [fromErrorStatus](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#fromErrorStatus(com.google.android.gms.common.api.Status))`(status: `[Status](https://developers.google.com/android/reference/com/google/android/gms/common/api/Status.html)`)`                                                                                   |
| `java-static `[StorageException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException)    | [fromException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#fromException(java.lang.Throwable))`(exception: `[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)`)`                                                                                                                          |
| `java-static `[StorageException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException)`?` | [fromExceptionAndHttpCode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#fromExceptionAndHttpCode(java.lang.Throwable,int))`(exception: `[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)`?, httpResultCode: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`)` |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                  | [getIsRecoverableException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#getIsRecoverableException())`()`                                                                                                                                                                                                                        |

|                                   ### Public properties                                   |
|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)`!` | [cause](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#cause())                   |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                | [errorCode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#errorCode())           |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                | [httpResultCode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException#httpResultCode()) |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             ### Inherited functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [java.lang.Throwable](https://developer.android.com/reference/kotlin/java/lang/Throwable.html) |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `synchronized `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                 | [addSuppressed](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/add-suppressed.html)`(exception: `[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)`!)`                                                                                                    | | `synchronized `[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)`!`                                                                                    | [fillInStackTrace](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/fill-in-stack-trace.html)`()`                                                                                                                                                                                                | | `synchronized `[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)`!`                                                                                    | [getCause](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-cause.html)`()`                                                                                                                                                                                                                  | | [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                                                                                         | [getLocalizedMessage](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-localized-message.html)`()`                                                                                                                                                                                           | | [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                                                                                         | [getMessage](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-message.html)`()`                                                                                                                                                                                                              | | [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[StackTraceElement](https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html)`!>!`  | [getStackTrace](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-stack-trace.html)`()`                                                                                                                                                                                                       | | `synchronized `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)`!>!` | [getSuppressed](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-suppressed.html)`()`                                                                                                                                                                                                        | | `synchronized `[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)`!`                                                                                    | [initCause](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/init-cause.html)`(cause: `[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)`!)`                                                                                                                | | [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                | [printStackTrace](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html)`()`                                                                                                                                                                                                   | | [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                | [setStackTrace](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/set-stack-trace.html)`(stackTrace: `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[StackTraceElement](https://developer.android.com/reference/kotlin/java/lang/StackTraceElement.html)`!>!)` | | [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                                                                                         | [toString](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/to-string.html)`()`                                                                                                                                                                                                                  | |

## Constants

### ERROR_BUCKET_NOT_FOUND

```
constÂ valÂ ERROR_BUCKET_NOT_FOUND = -13011:Â Int
```  

### ERROR_CANCELED

```
constÂ valÂ ERROR_CANCELED = -13040:Â Int
```  

### ERROR_INVALID_CHECKSUM

```
constÂ valÂ ERROR_INVALID_CHECKSUM = -13031:Â Int
```  

### ERROR_NOT_AUTHENTICATED

```
constÂ valÂ ERROR_NOT_AUTHENTICATED = -13020:Â Int
```  

### ERROR_NOT_AUTHORIZED

```
constÂ valÂ ERROR_NOT_AUTHORIZED = -13021:Â Int
```  

### ERROR_OBJECT_NOT_FOUND

```
constÂ valÂ ERROR_OBJECT_NOT_FOUND = -13010:Â Int
```  

### ERROR_PROJECT_NOT_FOUND

```
constÂ valÂ ERROR_PROJECT_NOT_FOUND = -13012:Â Int
```  

### ERROR_QUOTA_EXCEEDED

```
constÂ valÂ ERROR_QUOTA_EXCEEDED = -13013:Â Int
```  

### ERROR_RETRY_LIMIT_EXCEEDED

```
constÂ valÂ ERROR_RETRY_LIMIT_EXCEEDED = -13030:Â Int
```  

### ERROR_UNKNOWN

```
constÂ valÂ ERROR_UNKNOWN = -13000:Â Int
```  

## Public functions

### fromErrorStatus

```
java-staticÂ funÂ fromErrorStatus(status:Â Status):Â StorageException
```  

### fromException

```
java-staticÂ funÂ fromException(exception:Â Throwable):Â StorageException
```  

### fromExceptionAndHttpCode

```
java-staticÂ funÂ fromExceptionAndHttpCode(exception:Â Throwable?,Â httpResultCode:Â Int):Â StorageException?
```  

### getIsRecoverableException

```
funÂ getIsRecoverableException():Â Boolean
```  

|                                      Returns                                       |
|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | True if this request failed due to a network condition that may be resolved in a future attempt. |

## Public properties

### cause

```
valÂ cause:Â Throwable!
```  

### errorCode

```
valÂ errorCode:Â Int
```  

### httpResultCode

```
valÂ httpResultCode:Â Int
```