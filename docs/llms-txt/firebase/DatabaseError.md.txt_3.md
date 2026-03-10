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

| ### Constants |
|---|---|
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#DATA_STALE() = -1` **Internal use** |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#DISCONNECTED() = -4` The operation had to be aborted due to a network disconnect |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#EXPIRED_TOKEN() = -6` The supplied auth token has expired |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#INVALID_TOKEN() = -7` The specified authentication token is invalid. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#MAX_RETRIES() = -8` The transaction had too many retries |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#NETWORK_ERROR() = -24` The operation could not be performed due to a network error. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#OPERATION_FAILED() = -2` The server indicated that this operation failed |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#OVERRIDDEN_BY_SET() = -9` The transaction was overridden by a subsequent set |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#PERMISSION_DENIED() = -3` This client does not have permission to perform this operation |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#UNAVAILABLE() = -10` The service is unavailable |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#UNKNOWN_ERROR() = -999` An unknown error occurred. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#USER_CODE_EXCEPTION() = -11` An exception occurred in user code |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#WRITE_CANCELED() = -25` The write was canceled locally |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#fromException(java.lang.Throwable)(e: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseException` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#toException()()` Can be used if a third party needs an Exception from Firebase Database for integration purposes. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#toString()()` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#code()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#details()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseError#message()` |

## Constants

### DATA_STALE

```
const val DATA_STALE = -1: Int
```

**Internal use**

### DISCONNECTED

```
const val DISCONNECTED = -4: Int
```

The operation had to be aborted due to a network disconnect

### EXPIRED_TOKEN

```
const val EXPIRED_TOKEN = -6: Int
```

The supplied auth token has expired

### INVALID_TOKEN

```
const val INVALID_TOKEN = -7: Int
```

The specified authentication token is invalid. This can occur when the token is malformed, expired, or the secret that was used to generate it has been revoked.

### MAX_RETRIES

```
const val MAX_RETRIES = -8: Int
```

The transaction had too many retries

### NETWORK_ERROR

```
const val NETWORK_ERROR = -24: Int
```

The operation could not be performed due to a network error.

### OPERATION_FAILED

```
const val OPERATION_FAILED = -2: Int
```

The server indicated that this operation failed

### OVERRIDDEN_BY_SET

```
const val OVERRIDDEN_BY_SET = -9: Int
```

The transaction was overridden by a subsequent set

### PERMISSION_DENIED

```
const val PERMISSION_DENIED = -3: Int
```

This client does not have permission to perform this operation

### UNAVAILABLE

```
const val UNAVAILABLE = -10: Int
```

The service is unavailable

### UNKNOWN_ERROR

```
const val UNKNOWN_ERROR = -999: Int
```

An unknown error occurred. Please refer to the error message and error details for more information.

### USER_CODE_EXCEPTION

```
const val USER_CODE_EXCEPTION = -11: Int
```

An exception occurred in user code

### WRITE_CANCELED

```
const val WRITE_CANCELED = -25: Int
```

The write was canceled locally

## Public functions

### fromException

```
java-static fun fromException(e: Throwable): DatabaseError
```

### toException

```
fun toException(): DatabaseException
```

Can be used if a third party needs an Exception from Firebase Database for integration purposes.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseException` | An exception wrapping this error, with an appropriate message and no stack trace. |

### toString

```
fun toString(): String!
```

## Public properties

### code

```
val code: Int
```

### details

```
val details: String!
```

### message

```
val message: String!
```