# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError.md.txt

# DatabaseError

# DatabaseError


```
public class DatabaseError
```

<br />

*** ** * ** ***

Instances of DatabaseError are passed to callbacks when an operation failed. They contain a description of the specific error that occurred.

## Summary

| ### Constants |
|---|---|
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError#DATA_STALE() = -1` **Internal use** |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError#DISCONNECTED() = -4` The operation had to be aborted due to a network disconnect |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError#EXPIRED_TOKEN() = -6` The supplied auth token has expired |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError#INVALID_TOKEN() = -7` The specified authentication token is invalid. |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError#MAX_RETRIES() = -8` The transaction had too many retries |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError#NETWORK_ERROR() = -24` The operation could not be performed due to a network error. |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError#OPERATION_FAILED() = -2` The server indicated that this operation failed |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError#OVERRIDDEN_BY_SET() = -9` The transaction was overridden by a subsequent set |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError#PERMISSION_DENIED() = -3` This client does not have permission to perform this operation |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError#UNAVAILABLE() = -10` The service is unavailable |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError#UNKNOWN_ERROR() = -999` An unknown error occurred. |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError#USER_CODE_EXCEPTION() = -11` An exception occurred in user code |
| `static final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError#WRITE_CANCELED() = -25` The write was canceled locally |

| ### Public fields |
|---|---|
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError#code()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError#details()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError#message()` |

| ### Public methods |
|---|---|
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError#fromException(java.lang.Throwable)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Throwable.html e)` |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError#getCode()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError#getDetails()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError#getMessage()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseException` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError#toException()()` Can be used if a third party needs an Exception from Firebase Database for integration purposes. |
| `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseError#toString()()` |

## Constants

### DATA_STALE

```
public static final int DATA_STALE = -1
```

**Internal use**

### DISCONNECTED

```
public static final int DISCONNECTED = -4
```

The operation had to be aborted due to a network disconnect

### EXPIRED_TOKEN

```
public static final int EXPIRED_TOKEN = -6
```

The supplied auth token has expired

### INVALID_TOKEN

```
public static final int INVALID_TOKEN = -7
```

The specified authentication token is invalid. This can occur when the token is malformed, expired, or the secret that was used to generate it has been revoked.

### MAX_RETRIES

```
public static final int MAX_RETRIES = -8
```

The transaction had too many retries

### NETWORK_ERROR

```
public static final int NETWORK_ERROR = -24
```

The operation could not be performed due to a network error.

### OPERATION_FAILED

```
public static final int OPERATION_FAILED = -2
```

The server indicated that this operation failed

### OVERRIDDEN_BY_SET

```
public static final int OVERRIDDEN_BY_SET = -9
```

The transaction was overridden by a subsequent set

### PERMISSION_DENIED

```
public static final int PERMISSION_DENIED = -3
```

This client does not have permission to perform this operation

### UNAVAILABLE

```
public static final int UNAVAILABLE = -10
```

The service is unavailable

### UNKNOWN_ERROR

```
public static final int UNKNOWN_ERROR = -999
```

An unknown error occurred. Please refer to the error message and error details for more information.

### USER_CODE_EXCEPTION

```
public static final int USER_CODE_EXCEPTION = -11
```

An exception occurred in user code

### WRITE_CANCELED

```
public static final int WRITE_CANCELED = -25
```

The write was canceled locally

## Public fields

### code

```
public final int code
```

### details

```
public final String details
```

### message

```
public final String message
```

## Public methods

### fromException

```
public static @NonNull DatabaseError fromException(@NonNull Throwable e)
```

### getCode

```
public int getCode()
```

| Returns |
|---|---|
| `int` | One of the defined status codes, depending on the error |

### getDetails

```
public @NonNull String getDetails()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | Human-readable details on the error and additional information, e.g. links to docs; |

### getMessage

```
public @NonNull String getMessage()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | A human-readable description of the error |

### toException

```
public @NonNull DatabaseException toException()
```

Can be used if a third party needs an Exception from Firebase Database for integration purposes.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseException` | An exception wrapping this error, with an appropriate message and no stack trace. |

### toString

```
public String toString()
```