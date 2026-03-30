# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query.Direction.md.txt

# Query.Direction

# Query.Direction


```
public enum Query.Direction
```

<br />

*** ** * ** ***

An enum for the direction of a sort.

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query.Direction#ASCENDING` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query.Direction#DESCENDING` |   |

| ### Public methods |
|---|---|
| `static https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query.Direction` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query.Direction#valueOf(java.lang.String)(https://developer.android.com/reference/kotlin/java/lang/String.html name)` Returns the enum constant of this type with the specified name. |
| `static Query.Direction[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query.Direction#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### ASCENDING

```
Query.Direction Query.Direction.ASCENDING
```

### DESCENDING

```
Query.Direction Query.Direction.DESCENDING
```

## Public methods

### valueOf

```
public static Query.Direction valueOf(String name)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query.Direction` | the enum constant with the specified name |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html java.lang.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
public static Query.Direction[] values()
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `Query.Direction[]` | an array containing the constants of this enum type, in the order they're declared |