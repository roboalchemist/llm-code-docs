# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code.md.txt

# FirebaseFunctionsException.Code

# FirebaseFunctionsException.Code


```
enum FirebaseFunctionsException.Code : Enum
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [kotlin.Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html) ||
|   | ↳ | [com.google.firebase.functions.FirebaseFunctionsException.Code](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code) |

*** ** * ** ***

The set of error status codes that can be returned from a Callable HTTPS tigger. These are the canonical error codes for Google APIs, as documented here: https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto#L26

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#ABORTED` | The operation was aborted, typically due to a concurrency issue like transaction aborts, etc. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#ALREADY_EXISTS` | Some document that we attempted to create already exists. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#CANCELLED` | The operation was cancelled (typically by the caller). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#DATA_LOSS` | Unrecoverable data loss or corruption. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#DEADLINE_EXCEEDED` | Deadline expired before operation could complete. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#FAILED_PRECONDITION` | Operation was rejected because the system is not in a state required for the operation's execution. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#INTERNAL` | Internal errors. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#INVALID_ARGUMENT` | Client specified an invalid argument. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#NOT_FOUND` | Some requested document was not found. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#OK` | The operation completed successfully. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#OUT_OF_RANGE` | Operation was attempted past the valid range. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#PERMISSION_DENIED` | The caller does not have permission to execute the specified operation. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#RESOURCE_EXHAUSTED` | Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#UNAUTHENTICATED` | The request does not have valid authentication credentials for the operation. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#UNAVAILABLE` | The service is currently unavailable. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#UNIMPLEMENTED` | Operation is not implemented or not supported/enabled. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#UNKNOWN` | Unknown error or an error from a different error domain. |

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code.Companion#fromHttpStatus(kotlin.Int)(status: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Takes an HTTP status code and returns the corresponding `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code` error code. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code.Companion#fromValue(kotlin.Int)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#valueOf(kotlin.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the enum constant of this type with the specified name. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### ABORTED

```
val FirebaseFunctionsException.Code.ABORTED: FirebaseFunctionsException.Code
```

The operation was aborted, typically due to a concurrency issue like transaction aborts, etc.

### ALREADY_EXISTS

```
val FirebaseFunctionsException.Code.ALREADY_EXISTS: FirebaseFunctionsException.Code
```

Some document that we attempted to create already exists.

### CANCELLED

```
val FirebaseFunctionsException.Code.CANCELLED: FirebaseFunctionsException.Code
```

The operation was cancelled (typically by the caller).

### DATA_LOSS

```
val FirebaseFunctionsException.Code.DATA_LOSS: FirebaseFunctionsException.Code
```

Unrecoverable data loss or corruption.

### DEADLINE_EXCEEDED

```
val FirebaseFunctionsException.Code.DEADLINE_EXCEEDED: FirebaseFunctionsException.Code
```

Deadline expired before operation could complete. For operations that change the state of the system, this error may be returned even if the operation has completed successfully. For example, a successful response from a server could have been delayed long enough for the deadline to expire.

### FAILED_PRECONDITION

```
val FirebaseFunctionsException.Code.FAILED_PRECONDITION: FirebaseFunctionsException.Code
```

Operation was rejected because the system is not in a state required for the operation's execution.

### INTERNAL

```
val FirebaseFunctionsException.Code.INTERNAL: FirebaseFunctionsException.Code
```

Internal errors. Means some invariants expected by underlying system has been broken. If you see one of these errors, something is very broken.

### INVALID_ARGUMENT

```
val FirebaseFunctionsException.Code.INVALID_ARGUMENT: FirebaseFunctionsException.Code
```

Client specified an invalid argument. Note that this differs from `FAILED_PRECONDITION`. `INVALID_ARGUMENT` indicates arguments that are problematic regardless of the state of the system (For example, an invalid field name).

### NOT_FOUND

```
val FirebaseFunctionsException.Code.NOT_FOUND: FirebaseFunctionsException.Code
```

Some requested document was not found.

### OK

```
val FirebaseFunctionsException.Code.OK: FirebaseFunctionsException.Code
```

The operation completed successfully. `FirebaseFunctionsException` will never have a status of `OK`.

### OUT_OF_RANGE

```
val FirebaseFunctionsException.Code.OUT_OF_RANGE: FirebaseFunctionsException.Code
```

Operation was attempted past the valid range.

### PERMISSION_DENIED

```
val FirebaseFunctionsException.Code.PERMISSION_DENIED: FirebaseFunctionsException.Code
```

The caller does not have permission to execute the specified operation.

### RESOURCE_EXHAUSTED

```
val FirebaseFunctionsException.Code.RESOURCE_EXHAUSTED: FirebaseFunctionsException.Code
```

Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space.

### UNAUTHENTICATED

```
val FirebaseFunctionsException.Code.UNAUTHENTICATED: FirebaseFunctionsException.Code
```

The request does not have valid authentication credentials for the operation.

### UNAVAILABLE

```
val FirebaseFunctionsException.Code.UNAVAILABLE: FirebaseFunctionsException.Code
```

The service is currently unavailable. This is a most likely a transient condition and may be corrected by retrying with a backoff.

### UNIMPLEMENTED

```
val FirebaseFunctionsException.Code.UNIMPLEMENTED: FirebaseFunctionsException.Code
```

Operation is not implemented or not supported/enabled.

### UNKNOWN

```
val FirebaseFunctionsException.Code.UNKNOWN: FirebaseFunctionsException.Code
```

Unknown error or an error from a different error domain.

## Public companion functions

### fromHttpStatus

```
fun fromHttpStatus(status: Int): FirebaseFunctionsException.Code
```

Takes an HTTP status code and returns the corresponding `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code` error code. This is the standard HTTP status code -\> error mapping defined in: https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto

| Parameters |
|---|---|
| `status: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | An HTTP status code. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code` | The corresponding `Code`, or `Code.UNKNOWN` if none. |

### fromValue

```
fun fromValue(value: Int): FirebaseFunctionsException.Code
```

## Public functions

### valueOf

```
fun valueOf(value: String): FirebaseFunctionsException.Code
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Throws |
|---|---|
| `kotlin.IllegalArgumentException: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html` | if this enum type has no constant with the specified name |

### values

```
fun values(): Array<FirebaseFunctionsException.Code>
```

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.