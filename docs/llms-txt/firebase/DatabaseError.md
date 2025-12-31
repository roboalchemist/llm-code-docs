# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError.md.txt

# DatabaseError

# DatabaseError


```
class DatabaseError
```

<br />

*** ** * ** ***

Instances of DatabaseError are passed to callbacks when an operation failed. They contain a description of the specific error that occurred.

## Summary

|                                   ### Constants                                    |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [DATA_STALE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#DATA_STALE())` = -1` **Internal use**                                                             |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [DISCONNECTED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#DISCONNECTED())` = -4` The operation had to be aborted due to a network disconnect              |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [EXPIRED_TOKEN](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#EXPIRED_TOKEN())` = -6` The supplied auth token has expired                                    |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [INVALID_TOKEN](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#INVALID_TOKEN())` = -7` The specified authentication token is invalid.                         |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [MAX_RETRIES](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#MAX_RETRIES())` = -8` The transaction had too many retries                                       |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [NETWORK_ERROR](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#NETWORK_ERROR())` = -24` The operation could not be performed due to a network error.          |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [OPERATION_FAILED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#OPERATION_FAILED())` = -2` The server indicated that this operation failed                  |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [OVERRIDDEN_BY_SET](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#OVERRIDDEN_BY_SET())` = -9` The transaction was overridden by a subsequent set             |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [PERMISSION_DENIED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#PERMISSION_DENIED())` = -3` This client does not have permission to perform this operation |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [UNAVAILABLE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#UNAVAILABLE())` = -10` The service is unavailable                                                |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [UNKNOWN_ERROR](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#UNKNOWN_ERROR())` = -999` An unknown error occurred.                                           |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [USER_CODE_EXCEPTION](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#USER_CODE_EXCEPTION())` = -11` An exception occurred in user code                        |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [WRITE_CANCELED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#WRITE_CANCELED())` = -25` The write was canceled locally                                      |

|                                                    ### Public functions                                                     |
|-----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java-static `[DatabaseError](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError) | [fromException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#fromException(java.lang.Throwable))`(e: `[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)`)` |
| [DatabaseException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseException)       | [toException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#toException())`()` Can be used if a third party needs an Exception from Firebase Database for integration purposes.                  |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                         | [toString](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#toString())`()`                                                                                                                         |

|                                ### Public properties                                |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)          | [code](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#code())       |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [details](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#details()) |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [message](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#message()) |

## Constants

### DATA_STALE

```
constÂ valÂ DATA_STALE = -1:Â Int
```

**Internal use**  

### DISCONNECTED

```
constÂ valÂ DISCONNECTED = -4:Â Int
```

The operation had to be aborted due to a network disconnect  

### EXPIRED_TOKEN

```
constÂ valÂ EXPIRED_TOKEN = -6:Â Int
```

The supplied auth token has expired  

### INVALID_TOKEN

```
constÂ valÂ INVALID_TOKEN = -7:Â Int
```

The specified authentication token is invalid. This can occur when the token is malformed, expired, or the secret that was used to generate it has been revoked.  

### MAX_RETRIES

```
constÂ valÂ MAX_RETRIES = -8:Â Int
```

The transaction had too many retries  

### NETWORK_ERROR

```
constÂ valÂ NETWORK_ERROR = -24:Â Int
```

The operation could not be performed due to a network error.  

### OPERATION_FAILED

```
constÂ valÂ OPERATION_FAILED = -2:Â Int
```

The server indicated that this operation failed  

### OVERRIDDEN_BY_SET

```
constÂ valÂ OVERRIDDEN_BY_SET = -9:Â Int
```

The transaction was overridden by a subsequent set  

### PERMISSION_DENIED

```
constÂ valÂ PERMISSION_DENIED = -3:Â Int
```

This client does not have permission to perform this operation  

### UNAVAILABLE

```
constÂ valÂ UNAVAILABLE = -10:Â Int
```

The service is unavailable  

### UNKNOWN_ERROR

```
constÂ valÂ UNKNOWN_ERROR = -999:Â Int
```

An unknown error occurred. Please refer to the error message and error details for more information.  

### USER_CODE_EXCEPTION

```
constÂ valÂ USER_CODE_EXCEPTION = -11:Â Int
```

An exception occurred in user code  

### WRITE_CANCELED

```
constÂ valÂ WRITE_CANCELED = -25:Â Int
```

The write was canceled locally  

## Public functions

### fromException

```
java-staticÂ funÂ fromException(e:Â Throwable):Â DatabaseError
```  

### toException

```
funÂ toException():Â DatabaseException
```

Can be used if a third party needs an Exception from Firebase Database for integration purposes.  

|                                                        Returns                                                        |
|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [DatabaseException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseException) | An exception wrapping this error, with an appropriate message and no stack trace. |

### toString

```
funÂ toString():Â String!
```  

## Public properties

### code

```
valÂ code:Â Int
```  

### details

```
valÂ details:Â String!
```  

### message

```
valÂ message:Â String!
```