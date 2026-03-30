# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code.md.txt

# FirebaseFirestoreException.Code

# FirebaseFirestoreException.Code


```
enum FirebaseFirestoreException.Code
```

<br />

*** ** * ** ***

The set of Cloud Firestore status codes. The codes are the same at the ones exposed by gRPC here: https://github.com/grpc/grpc/blob/master/doc/statuscodes.md

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code#ABORTED` | The operation was aborted, typically due to a concurrency issue like transaction aborts, etc. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code#ALREADY_EXISTS` | Some document that we attempted to create already exists. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code#CANCELLED` | The operation was cancelled (typically by the caller). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code#DATA_LOSS` | Unrecoverable data loss or corruption. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code#DEADLINE_EXCEEDED` | Deadline expired before operation could complete. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code#FAILED_PRECONDITION` | Operation was rejected because the system is not in a state required for the operation's execution. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code#INTERNAL` | Internal errors. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code#INVALID_ARGUMENT` | Client specified an invalid argument. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code#NOT_FOUND` | Some requested document was not found. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code#OK` | The operation completed successfully. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code#OUT_OF_RANGE` | Operation was attempted past the valid range. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code#PERMISSION_DENIED` | The caller does not have permission to execute the specified operation. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code#RESOURCE_EXHAUSTED` | Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code#UNAUTHENTICATED` | The request does not have valid authentication credentials for the operation. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code#UNAVAILABLE` | The service is currently unavailable. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code#UNIMPLEMENTED` | Operation is not implemented or not supported/enabled. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code#UNKNOWN` | Unknown error or an error from a different error domain. |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code#fromValue(int)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code#value()()` The numerical value of the code. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code#valueOf(java.lang.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!)` Returns the enum constant of this type with the specified name. |
| `java-static https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### ABORTED

```
val FirebaseFirestoreException.Code.ABORTED: FirebaseFirestoreException.Code
```

The operation was aborted, typically due to a concurrency issue like transaction aborts, etc.

### ALREADY_EXISTS

```
val FirebaseFirestoreException.Code.ALREADY_EXISTS: FirebaseFirestoreException.Code
```

Some document that we attempted to create already exists.

### CANCELLED

```
val FirebaseFirestoreException.Code.CANCELLED: FirebaseFirestoreException.Code
```

The operation was cancelled (typically by the caller).

### DATA_LOSS

```
val FirebaseFirestoreException.Code.DATA_LOSS: FirebaseFirestoreException.Code
```

Unrecoverable data loss or corruption.

### DEADLINE_EXCEEDED

```
val FirebaseFirestoreException.Code.DEADLINE_EXCEEDED: FirebaseFirestoreException.Code
```

Deadline expired before operation could complete. For operations that change the state of the system, this error may be returned even if the operation has completed successfully. For example, a successful response from a server could have been delayed long enough for the deadline to expire.

### FAILED_PRECONDITION

```
val FirebaseFirestoreException.Code.FAILED_PRECONDITION: FirebaseFirestoreException.Code
```

Operation was rejected because the system is not in a state required for the operation's execution.

### INTERNAL

```
val FirebaseFirestoreException.Code.INTERNAL: FirebaseFirestoreException.Code
```

Internal errors. Means some invariants expected by underlying system has been broken. If you see one of these errors, something is very broken.

### INVALID_ARGUMENT

```
val FirebaseFirestoreException.Code.INVALID_ARGUMENT: FirebaseFirestoreException.Code
```

Client specified an invalid argument. Note that this differs from `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code#FAILED_PRECONDITION`. `INVALID_ARGUMENT` indicates arguments that are problematic regardless of the state of the system (like an invalid field name).

### NOT_FOUND

```
val FirebaseFirestoreException.Code.NOT_FOUND: FirebaseFirestoreException.Code
```

Some requested document was not found.

### OK

```
val FirebaseFirestoreException.Code.OK: FirebaseFirestoreException.Code
```

The operation completed successfully. `FirebaseFirestoreException` will never have a status of `OK`.

### OUT_OF_RANGE

```
val FirebaseFirestoreException.Code.OUT_OF_RANGE: FirebaseFirestoreException.Code
```

Operation was attempted past the valid range.

### PERMISSION_DENIED

```
val FirebaseFirestoreException.Code.PERMISSION_DENIED: FirebaseFirestoreException.Code
```

The caller does not have permission to execute the specified operation.

### RESOURCE_EXHAUSTED

```
val FirebaseFirestoreException.Code.RESOURCE_EXHAUSTED: FirebaseFirestoreException.Code
```

Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space.

### UNAUTHENTICATED

```
val FirebaseFirestoreException.Code.UNAUTHENTICATED: FirebaseFirestoreException.Code
```

The request does not have valid authentication credentials for the operation.

### UNAVAILABLE

```
val FirebaseFirestoreException.Code.UNAVAILABLE: FirebaseFirestoreException.Code
```

The service is currently unavailable. This is a most likely a transient condition and may be corrected by retrying with a backoff.

### UNIMPLEMENTED

```
val FirebaseFirestoreException.Code.UNIMPLEMENTED: FirebaseFirestoreException.Code
```

Operation is not implemented or not supported/enabled.

### UNKNOWN

```
val FirebaseFirestoreException.Code.UNKNOWN: FirebaseFirestoreException.Code
```

Unknown error or an error from a different error domain.

## Public functions

### fromValue

```
java-static fun fromValue(value: Int): FirebaseFirestoreException.Code
```

### value

```
fun value(): Int
```

The numerical value of the code.

### valueOf

```
java-static fun valueOf(name: String!): FirebaseFirestoreException.Code!
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code!` | the enum constant with the specified name |

| Throws |
|---|---|
| `java.lang.IllegalArgumentException: https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html` | if this enum type has no constant with the specified name |

### values

```
java-static fun values(): Array<FirebaseFirestoreException.Code!>!
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException.Code!>!` | an array containing the constants of this enum type, in the order they're declared |