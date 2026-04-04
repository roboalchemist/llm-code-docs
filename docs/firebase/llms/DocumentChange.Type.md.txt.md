# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange.Type.md.txt

# DocumentChange.Type

# DocumentChange.Type


```
public enum DocumentChange.Type
```

<br />

*** ** * ** ***

An enumeration of snapshot diff types.

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange.Type#ADDED` | Indicates a new document was added to the set of documents matching the query. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange.Type#MODIFIED` | Indicates a document within the query was modified. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange.Type#REMOVED` | Indicates a document within the query was removed (either deleted or no longer matches the query. |

| ### Public methods |
|---|---|
| `static https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange.Type` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange.Type#valueOf(java.lang.String)(https://developer.android.com/reference/kotlin/java/lang/String.html name)` Returns the enum constant of this type with the specified name. |
| `static DocumentChange.Type[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange.Type#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### ADDED

```
DocumentChange.Type DocumentChange.Type.ADDED
```

Indicates a new document was added to the set of documents matching the query.

### MODIFIED

```
DocumentChange.Type DocumentChange.Type.MODIFIED
```

Indicates a document within the query was modified.

### REMOVED

```
DocumentChange.Type DocumentChange.Type.REMOVED
```

Indicates a document within the query was removed (either deleted or no longer matches the query.

## Public methods

### valueOf

```
public static DocumentChange.Type valueOf(String name)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange.Type` | the enum constant with the specified name |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html java.lang.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
public static DocumentChange.Type[] values()
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `DocumentChange.Type[]` | an array containing the constants of this enum type, in the order they're declared |