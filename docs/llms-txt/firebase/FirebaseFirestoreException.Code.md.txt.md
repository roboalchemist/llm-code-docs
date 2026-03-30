# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code.md.txt

# FirebaseFirestoreException.Code

# FirebaseFirestoreException.Code


```
public enum FirebaseFirestoreException.Code
```

<br />

*** ** * ** ***

The set of Cloud Firestore status codes. The codes are the same at the ones exposed by gRPC here: https://github.com/grpc/grpc/blob/master/doc/statuscodes.md

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code#ABORTED` | The operation was aborted, typically due to a concurrency issue like transaction aborts, etc. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code#ALREADY_EXISTS` | Some document that we attempted to create already exists. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code#CANCELLED` | The operation was cancelled (typically by the caller). |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code#DATA_LOSS` | Unrecoverable data loss or corruption. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code#DEADLINE_EXCEEDED` | Deadline expired before operation could complete. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code#FAILED_PRECONDITION` | Operation was rejected because the system is not in a state required for the operation's execution. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code#INTERNAL` | Internal errors. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code#INVALID_ARGUMENT` | Client specified an invalid argument. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code#NOT_FOUND` | Some requested document was not found. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code#OK` | The operation completed successfully. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code#OUT_OF_RANGE` | Operation was attempted past the valid range. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code#PERMISSION_DENIED` | The caller does not have permission to execute the specified operation. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code#RESOURCE_EXHAUSTED` | Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code#UNAUTHENTICATED` | The request does not have valid authentication credentials for the operation. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code#UNAVAILABLE` | The service is currently unavailable. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code#UNIMPLEMENTED` | Operation is not implemented or not supported/enabled. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code#UNKNOWN` | Unknown error or an error from a different error domain. |

| ### Public methods |
|---|---|
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code#fromValue(int)(int value)` |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code#value()()` The numerical value of the code. |
| `static https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code#valueOf(java.lang.String)(https://developer.android.com/reference/kotlin/java/lang/String.html name)` Returns the enum constant of this type with the specified name. |
| `static FirebaseFirestoreException.Code[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### ABORTED

```
FirebaseFirestoreException.Code FirebaseFirestoreException.Code.ABORTED
```

The operation was aborted, typically due to a concurrency issue like transaction aborts, etc.

### ALREADY_EXISTS

```
FirebaseFirestoreException.Code FirebaseFirestoreException.Code.ALREADY_EXISTS
```

Some document that we attempted to create already exists.

### CANCELLED

```
FirebaseFirestoreException.Code FirebaseFirestoreException.Code.CANCELLED
```

The operation was cancelled (typically by the caller).

### DATA_LOSS

```
FirebaseFirestoreException.Code FirebaseFirestoreException.Code.DATA_LOSS
```

Unrecoverable data loss or corruption.

### DEADLINE_EXCEEDED

```
FirebaseFirestoreException.Code FirebaseFirestoreException.Code.DEADLINE_EXCEEDED
```

Deadline expired before operation could complete. For operations that change the state of the system, this error may be returned even if the operation has completed successfully. For example, a successful response from a server could have been delayed long enough for the deadline to expire.

### FAILED_PRECONDITION

```
FirebaseFirestoreException.Code FirebaseFirestoreException.Code.FAILED_PRECONDITION
```

Operation was rejected because the system is not in a state required for the operation's execution.

### INTERNAL

```
FirebaseFirestoreException.Code FirebaseFirestoreException.Code.INTERNAL
```

Internal errors. Means some invariants expected by underlying system has been broken. If you see one of these errors, something is very broken.

### INVALID_ARGUMENT

```
FirebaseFirestoreException.Code FirebaseFirestoreException.Code.INVALID_ARGUMENT
```

Client specified an invalid argument. Note that this differs from `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code#FAILED_PRECONDITION`. `INVALID_ARGUMENT` indicates arguments that are problematic regardless of the state of the system (like an invalid field name).

### NOT_FOUND

```
FirebaseFirestoreException.Code FirebaseFirestoreException.Code.NOT_FOUND
```

Some requested document was not found.

### OK

```
FirebaseFirestoreException.Code FirebaseFirestoreException.Code.OK
```

The operation completed successfully. `FirebaseFirestoreException` will never have a status of `OK`.

### OUT_OF_RANGE

```
FirebaseFirestoreException.Code FirebaseFirestoreException.Code.OUT_OF_RANGE
```

Operation was attempted past the valid range.

### PERMISSION_DENIED

```
FirebaseFirestoreException.Code FirebaseFirestoreException.Code.PERMISSION_DENIED
```

The caller does not have permission to execute the specified operation.

### RESOURCE_EXHAUSTED

```
FirebaseFirestoreException.Code FirebaseFirestoreException.Code.RESOURCE_EXHAUSTED
```

Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space.

### UNAUTHENTICATED

```
FirebaseFirestoreException.Code FirebaseFirestoreException.Code.UNAUTHENTICATED
```

The request does not have valid authentication credentials for the operation.

### UNAVAILABLE

```
FirebaseFirestoreException.Code FirebaseFirestoreException.Code.UNAVAILABLE
```

The service is currently unavailable. This is a most likely a transient condition and may be corrected by retrying with a backoff.

### UNIMPLEMENTED

```
FirebaseFirestoreException.Code FirebaseFirestoreException.Code.UNIMPLEMENTED
```

Operation is not implemented or not supported/enabled.

### UNKNOWN

```
FirebaseFirestoreException.Code FirebaseFirestoreException.Code.UNKNOWN
```

Unknown error or an error from a different error domain.

## Public methods

### fromValue

```
public static @NonNull FirebaseFirestoreException.Code fromValue(int value)
```

### value

```
public int value()
```

The numerical value of the code.

### valueOf

```
public static FirebaseFirestoreException.Code valueOf(String name)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException.Code` | the enum constant with the specified name |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html java.lang.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
public static FirebaseFirestoreException.Code[] values()
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `FirebaseFirestoreException.Code[]` | an array containing the constants of this enum type, in the order they're declared |