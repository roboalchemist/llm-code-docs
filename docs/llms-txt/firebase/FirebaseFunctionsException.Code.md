# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctionsException.Code.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code.md.txt

# FirebaseFunctionsException.Code

# FirebaseFunctionsException.Code


```
enum FirebaseFunctionsException.Code : Enum
```

<br />

|---|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                                                      |||
| â³ | [kotlin.Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)                                                                                                 ||
|   | â³ | [com.google.firebase.functions.FirebaseFunctionsException.Code](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code) |

*** ** * ** ***

The set of error status codes that can be returned from a Callable HTTPS tigger. These are the canonical error codes for Google APIs, as documented here: https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto#L26

## Summary

|                                                                      ### Enum Values                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [ABORTED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#ABORTED)                         | The operation was aborted, typically due to a concurrency issue like transaction aborts, etc.                  |
| [ALREADY_EXISTS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#ALREADY_EXISTS)           | Some document that we attempted to create already exists.                                                      |
| [CANCELLED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#CANCELLED)                     | The operation was cancelled (typically by the caller).                                                         |
| [DATA_LOSS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#DATA_LOSS)                     | Unrecoverable data loss or corruption.                                                                         |
| [DEADLINE_EXCEEDED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#DEADLINE_EXCEEDED)     | Deadline expired before operation could complete.                                                              |
| [FAILED_PRECONDITION](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#FAILED_PRECONDITION) | Operation was rejected because the system is not in a state required for the operation's execution.            |
| [INTERNAL](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#INTERNAL)                       | Internal errors.                                                                                               |
| [INVALID_ARGUMENT](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#INVALID_ARGUMENT)       | Client specified an invalid argument.                                                                          |
| [NOT_FOUND](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#NOT_FOUND)                     | Some requested document was not found.                                                                         |
| [OK](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#OK)                                   | The operation completed successfully.                                                                          |
| [OUT_OF_RANGE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#OUT_OF_RANGE)               | Operation was attempted past the valid range.                                                                  |
| [PERMISSION_DENIED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#PERMISSION_DENIED)     | The caller does not have permission to execute the specified operation.                                        |
| [RESOURCE_EXHAUSTED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#RESOURCE_EXHAUSTED)   | Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space. |
| [UNAUTHENTICATED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#UNAUTHENTICATED)         | The request does not have valid authentication credentials for the operation.                                  |
| [UNAVAILABLE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#UNAVAILABLE)                 | The service is currently unavailable.                                                                          |
| [UNIMPLEMENTED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#UNIMPLEMENTED)             | Operation is not implemented or not supported/enabled.                                                         |
| [UNKNOWN](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#UNKNOWN)                         | Unknown error or an error from a different error domain.                                                       |

|                                                           ### Public companion functions                                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseFunctionsException.Code](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code) | [fromHttpStatus](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code.Companion#fromHttpStatus(kotlin.Int))`(status: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`)` Takes an HTTP status code and returns the corresponding [Code](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code) error code. |
| [FirebaseFunctionsException.Code](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code) | [fromValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code.Companion#fromValue(kotlin.Int))`(value: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`)`                                                                                                                                                                                                        |

|                                                                                                          ### Public functions                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseFunctionsException.Code](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code)                                                                                     | [valueOf](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#valueOf(kotlin.String))`(value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns the enum constant of this type with the specified name. |
| [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[FirebaseFunctionsException.Code](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code)`>` | [values](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code#values())`()` Returns an array containing the constants of this enum type, in the order they're declared.                                                                             |

## Enum Values

### ABORTED

```
valÂ FirebaseFunctionsException.Code.ABORTED:Â FirebaseFunctionsException.Code
```

The operation was aborted, typically due to a concurrency issue like transaction aborts, etc.  

### ALREADY_EXISTS

```
valÂ FirebaseFunctionsException.Code.ALREADY_EXISTS:Â FirebaseFunctionsException.Code
```

Some document that we attempted to create already exists.  

### CANCELLED

```
valÂ FirebaseFunctionsException.Code.CANCELLED:Â FirebaseFunctionsException.Code
```

The operation was cancelled (typically by the caller).  

### DATA_LOSS

```
valÂ FirebaseFunctionsException.Code.DATA_LOSS:Â FirebaseFunctionsException.Code
```

Unrecoverable data loss or corruption.  

### DEADLINE_EXCEEDED

```
valÂ FirebaseFunctionsException.Code.DEADLINE_EXCEEDED:Â FirebaseFunctionsException.Code
```

Deadline expired before operation could complete. For operations that change the state of the system, this error may be returned even if the operation has completed successfully. For example, a successful response from a server could have been delayed long enough for the deadline to expire.  

### FAILED_PRECONDITION

```
valÂ FirebaseFunctionsException.Code.FAILED_PRECONDITION:Â FirebaseFunctionsException.Code
```

Operation was rejected because the system is not in a state required for the operation's execution.  

### INTERNAL

```
valÂ FirebaseFunctionsException.Code.INTERNAL:Â FirebaseFunctionsException.Code
```

Internal errors. Means some invariants expected by underlying system has been broken. If you see one of these errors, something is very broken.  

### INVALID_ARGUMENT

```
valÂ FirebaseFunctionsException.Code.INVALID_ARGUMENT:Â FirebaseFunctionsException.Code
```

Client specified an invalid argument. Note that this differs from `FAILED_PRECONDITION`. `INVALID_ARGUMENT` indicates arguments that are problematic regardless of the state of the system (For example, an invalid field name).  

### NOT_FOUND

```
valÂ FirebaseFunctionsException.Code.NOT_FOUND:Â FirebaseFunctionsException.Code
```

Some requested document was not found.  

### OK

```
valÂ FirebaseFunctionsException.Code.OK:Â FirebaseFunctionsException.Code
```

The operation completed successfully. `FirebaseFunctionsException` will never have a status of `OK`.  

### OUT_OF_RANGE

```
valÂ FirebaseFunctionsException.Code.OUT_OF_RANGE:Â FirebaseFunctionsException.Code
```

Operation was attempted past the valid range.  

### PERMISSION_DENIED

```
valÂ FirebaseFunctionsException.Code.PERMISSION_DENIED:Â FirebaseFunctionsException.Code
```

The caller does not have permission to execute the specified operation.  

### RESOURCE_EXHAUSTED

```
valÂ FirebaseFunctionsException.Code.RESOURCE_EXHAUSTED:Â FirebaseFunctionsException.Code
```

Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space.  

### UNAUTHENTICATED

```
valÂ FirebaseFunctionsException.Code.UNAUTHENTICATED:Â FirebaseFunctionsException.Code
```

The request does not have valid authentication credentials for the operation.  

### UNAVAILABLE

```
valÂ FirebaseFunctionsException.Code.UNAVAILABLE:Â FirebaseFunctionsException.Code
```

The service is currently unavailable. This is a most likely a transient condition and may be corrected by retrying with a backoff.  

### UNIMPLEMENTED

```
valÂ FirebaseFunctionsException.Code.UNIMPLEMENTED:Â FirebaseFunctionsException.Code
```

Operation is not implemented or not supported/enabled.  

### UNKNOWN

```
valÂ FirebaseFunctionsException.Code.UNKNOWN:Â FirebaseFunctionsException.Code
```

Unknown error or an error from a different error domain.  

## Public companion functions

### fromHttpStatus

```
funÂ fromHttpStatus(status:Â Int):Â FirebaseFunctionsException.Code
```

Takes an HTTP status code and returns the corresponding [Code](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code) error code. This is the standard HTTP status code -\> error mapping defined in: https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto  

|                                      Parameters                                      |
|--------------------------------------------------------------------------------------|----------------------|
| `status: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | An HTTP status code. |

|                                                                      Returns                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| [FirebaseFunctionsException.Code](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code) | The corresponding `Code`, or `Code.UNKNOWN` if none. |

### fromValue

```
funÂ fromValue(value:Â Int):Â FirebaseFunctionsException.Code
```  

## Public functions

### valueOf

```
funÂ valueOf(value:Â String):Â FirebaseFunctionsException.Code
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)  

|                                                                              Throws                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| `kotlin.IllegalArgumentException: `[kotlin.IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) | if this enum type has no constant with the specified name |

### values

```
funÂ values():Â Array<FirebaseFunctionsException.Code>
```

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.