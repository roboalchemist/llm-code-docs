# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationFailureResponse.md.txt

# DataConnectOperationFailureResponse

# DataConnectOperationFailureResponse


```
interface DataConnectOperationFailureResponse<Data : Any?>
```

<br />

*** ** * ** ***

The data and errors provided by the backend in the response message.

## Summary

| ### Nested types |
|---|
| `interface https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationFailureResponse.ErrorInfo` Information about the error, as provided in the response payload from the backend. |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationFailureResponse#toString()()` Returns a string representation of this object, useful for debugging. |

| ### Public properties |
|---|---|
| `Data?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationFailureResponse#data()` The successfully-decoded `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationFailureResponse#rawData()`, if any. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationFailureResponse.ErrorInfo>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationFailureResponse#errors()` The list of errors provided by the backend in the response message; may be empty. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationFailureResponse#rawData()` The raw, un-decoded data provided by the backend in the response message. |

## Public functions

### toString

```
fun toString(): String
```

Returns a string representation of this object, useful for debugging.

The string representation is *not* guaranteed to be stable and may change without notice at any time. Therefore, the only recommended usage of the returned string is debugging and/or logging. Namely, parsing the returned string or storing the returned string in non-volatile storage should generally be avoided in order to be robust in case that the string representation changes.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | a string representation of this object, which includes the class name and the values of all public properties. |

## Public properties

### data

```
val data: Data?
```

The successfully-decoded `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationFailureResponse#rawData()`, if any.

Will be `null` if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationFailureResponse#rawData()` is `null`, or if decoding the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationFailureResponse#rawData()` failed.

### errors

```
val errors: List<DataConnectOperationFailureResponse.ErrorInfo>
```

The list of errors provided by the backend in the response message; may be empty.

See <https://spec.graphql.org/draft/#sec-Errors> for details.

### rawData

```
val rawData: Map<String, Any?>?
```

The raw, un-decoded data provided by the backend in the response message. Will be `null` if, and only if, the backend explicitly sent null for the data or if the data was not present in the response.

Otherwise, the values in the map will be one of the following:

- `null`

- `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html`

- `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html`

- `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html`

- `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html` containing any of the types in this list of types

- `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html` with `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` keys and values of the types in this list of types