# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.Type.md.txt

# DocumentChange.Type

# DocumentChange.Type


```
enum DocumentChange.Type
```

<br />

*** ** * ** ***

An enumeration of snapshot diff types.

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.Type#ADDED` | Indicates a new document was added to the set of documents matching the query. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.Type#MODIFIED` | Indicates a document within the query was modified. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.Type#REMOVED` | Indicates a document within the query was removed (either deleted or no longer matches the query. |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.Type!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.Type#valueOf(java.lang.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!)` Returns the enum constant of this type with the specified name. |
| `java-static https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.Type!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.Type#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### ADDED

```
val DocumentChange.Type.ADDED: DocumentChange.Type
```

Indicates a new document was added to the set of documents matching the query.

### MODIFIED

```
val DocumentChange.Type.MODIFIED: DocumentChange.Type
```

Indicates a document within the query was modified.

### REMOVED

```
val DocumentChange.Type.REMOVED: DocumentChange.Type
```

Indicates a document within the query was removed (either deleted or no longer matches the query.

## Public functions

### valueOf

```
java-static fun valueOf(name: String!): DocumentChange.Type!
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.Type!` | the enum constant with the specified name |

| Throws |
|---|---|
| `java.lang.IllegalArgumentException: https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html` | if this enum type has no constant with the specified name |

### values

```
java-static fun values(): Array<DocumentChange.Type!>!
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.Type!>!` | an array containing the constants of this enum type, in the order they're declared |