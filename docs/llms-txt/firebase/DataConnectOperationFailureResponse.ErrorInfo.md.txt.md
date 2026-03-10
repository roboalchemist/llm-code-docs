# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationFailureResponse.ErrorInfo.md.txt

# DataConnectOperationFailureResponse.ErrorInfo

# DataConnectOperationFailureResponse.ErrorInfo


```
interface DataConnectOperationFailureResponse.ErrorInfo
```

<br />

*** ** * ** ***

Information about the error, as provided in the response payload from the backend.

See <https://spec.graphql.org/draft/#sec-Errors> for details.

## Summary

| ### Public functions |
|---|---|
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationFailureResponse.ErrorInfo#equals(kotlin.Any)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Compares this object with another object for equality. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationFailureResponse.ErrorInfo#hashCode()()` Calculates and returns the hash code for this object. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationFailureResponse.ErrorInfo#toString()()` Returns a string representation of this object, useful for debugging. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationFailureResponse.ErrorInfo#message()` The error's message. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectPathSegment>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationFailureResponse.ErrorInfo#path()` The path of the field in the response data to which this error relates. |

## Public functions

### equals

```
operator fun equals(other: Any?): Boolean
```

Compares this object with another object for equality.

| Parameters |
|---|---|
| `other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The object to compare to this for equality. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | true if, and only if, the other object is an instance of the same implementation of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationFailureResponse.ErrorInfo` whose public properties compare equal using the `==` operator to the corresponding properties of this object. |

### hashCode

```
fun hashCode(): Int
```

Calculates and returns the hash code for this object.

The hash code is *not* guaranteed to be stable across application restarts.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | the hash code for this object, that incorporates the values of this object's public properties. |

### toString

```
fun toString(): String
```

Returns a string representation of this object, useful for debugging.

The string representation is *not* guaranteed to be stable and may change without notice at any time. Therefore, the only recommended usage of the returned string is debugging and/or logging. Namely, parsing the returned string or storing the returned string in non-volatile storage should generally be avoided in order to be robust in case that the string representation changes.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | a string representation of this object, suitable for logging the error indicated by this object; it will include the path formatted into a human-readable string (if the path is not empty), and the message. |

## Public properties

### message

```
val message: String
```

The error's message.

### path

```
val path: List<DataConnectPathSegment>
```

The path of the field in the response data to which this error relates.