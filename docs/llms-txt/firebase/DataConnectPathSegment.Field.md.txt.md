# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectPathSegment.Field.md.txt

# DataConnectPathSegment.Field

# DataConnectPathSegment.Field


```
value class DataConnectPathSegment.Field : DataConnectPathSegment
```

<br />

*** ** * ** ***

A named field in a path to a field in the response data.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectPathSegment.Field#Field(kotlin.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |

| ### Public functions |
|---|---|
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectPathSegment.Field#toString()()` Returns a string representation of this object, useful for debugging. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectPathSegment.Field#field()` |

## Public constructors

### Field

```
Field(field: String)
```

## Public functions

### toString

```
open fun toString(): String
```

Returns a string representation of this object, useful for debugging.

The string representation is *not* guaranteed to be stable and may change without notice at any time. Therefore, the only recommended usage of the returned string is debugging and/or logging. Namely, parsing the returned string or storing the returned string in non-volatile storage should generally be avoided in order to be robust in case that the string representation changes.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | returns simply `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectPathSegment.Field#field()`. |

## Public properties

### field

```
val field: String
```