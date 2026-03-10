# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath.md.txt

# FieldPath

# FieldPath


```
class FieldPath
```

<br />

*** ** * ** ***

A `FieldPath` refers to a field in a document. The path may consist of a single field name (referring to a top level field in the document), or a list of field names (referring to a nested field in the document).

## Summary

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath#documentId()()` Returns A special sentinel `FieldPath` to refer to the ID of a document. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath#equals(java.lang.Object)(o: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath#hashCode()()` |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath#of(java.lang.String...)(fieldNames: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>!)` Creates a `FieldPath` from the provided field names. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath#toString()()` |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/model/FieldPath!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath#internalPath()` |

## Public functions

### documentId

```
java-static fun documentId(): FieldPath
```

Returns A special sentinel `FieldPath` to refer to the ID of a document. It can be used in queries to sort or filter by the document ID.

### equals

```
fun equals(o: Any!): Boolean
```

### hashCode

```
fun hashCode(): Int
```

### of

```
java-static fun of(fieldNames: Array<String!>!): FieldPath
```

Creates a `FieldPath` from the provided field names. If more than one field name is provided, the path will point to a nested field in a document.

| Parameters |
|---|---|
| `fieldNames: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>!` | A list of field names. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | A `FieldPath` that points to a field location in a document. |

### toString

```
fun toString(): String!
```

## Public properties

### internalPath

```
val internalPath: FieldPath!
```