# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.md.txt

# DocumentChange

# DocumentChange


```
class DocumentChange
```

<br />

*** ** * ** ***

A `DocumentChange` represents a change to the documents matching a query. It contains the document affected and a the type of change that occurred (added, modified, or removed).

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

| ### Nested types |
|---|
| `enum https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.Type` An enumeration of snapshot diff types. |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange#equals(java.lang.Object)(object: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange#hashCode()()` |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QueryDocumentSnapshot!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange#document()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange#newIndex()` The index in the new snapshot, after processing all previous changes. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange#oldIndex()` The index in the old snapshot, after processing all previous changes. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange.Type!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentChange#type()` |

## Public functions

### equals

```
fun equals(object: Any?): Boolean
```

### hashCode

```
fun hashCode(): Int
```

## Public properties

### document

```
val document: QueryDocumentSnapshot!
```

### newIndex

```
val newIndex: Int
```

The index in the new snapshot, after processing all previous changes.

### oldIndex

```
val oldIndex: Int
```

The index in the old snapshot, after processing all previous changes.

### type

```
val type: DocumentChange.Type!
```