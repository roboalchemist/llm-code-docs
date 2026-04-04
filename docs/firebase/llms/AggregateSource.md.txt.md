# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateSource.md.txt

# AggregateSource

# AggregateSource


```
public enum AggregateSource
```

<br />

*** ** * ** ***

The sources from which an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery` can retrieve its results.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery#get(com.google.firebase.firestore.AggregateSource)` |   |

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateSource#SERVER` | Perform the aggregation on the server and download the result. |

| ### Public methods |
|---|---|
| `static https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateSource` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateSource#valueOf(java.lang.String)(https://developer.android.com/reference/kotlin/java/lang/String.html name)` Returns the enum constant of this type with the specified name. |
| `static AggregateSource[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateSource#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### SERVER

```
AggregateSource AggregateSource.SERVER
```

Perform the aggregation on the server and download the result.

The result received from the server is presented, unaltered, without considering any local state. That is, documents in the local cache are not taken into consideration, neither are local modifications not yet synchronized with the server. Previously-downloaded results, if any, are not used. Every request using this source necessarily involves a round trip to the server.

The `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery` will fail if the server cannot be reached, such as if the client is offline.

## Public methods

### valueOf

```
public static AggregateSource valueOf(String name)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateSource` | the enum constant with the specified name |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html java.lang.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
public static AggregateSource[] values()
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `AggregateSource[]` | an array containing the constants of this enum type, in the order they're declared |