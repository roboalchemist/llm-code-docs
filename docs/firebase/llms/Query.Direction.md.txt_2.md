# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.Direction.md.txt

# Query.Direction

# Query.Direction


```
enum Query.Direction
```

<br />

*** ** * ** ***

An enum for the direction of a sort.

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.Direction#ASCENDING` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.Direction#DESCENDING` |   |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.Direction!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.Direction#valueOf(java.lang.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!)` Returns the enum constant of this type with the specified name. |
| `java-static https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.Direction!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.Direction#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### ASCENDING

```
val Query.Direction.ASCENDING: Query.Direction
```

### DESCENDING

```
val Query.Direction.DESCENDING: Query.Direction
```

## Public functions

### valueOf

```
java-static fun valueOf(name: String!): Query.Direction!
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.Direction!` | the enum constant with the specified name |

| Throws |
|---|---|
| `java.lang.IllegalArgumentException: https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html` | if this enum type has no constant with the specified name |

### values

```
java-static fun values(): Array<Query.Direction!>!
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.Direction!>!` | an array containing the constants of this enum type, in the order they're declared |