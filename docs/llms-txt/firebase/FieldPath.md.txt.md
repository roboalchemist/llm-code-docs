# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath.md.txt

# FieldPath

# FieldPath


```
public final class FieldPath
```

<br />

*** ** * ** ***

A `FieldPath` refers to a field in a document. The path may consist of a single field name (referring to a top level field in the document), or a list of field names (referring to a nested field in the document).

## Summary

| ### Public fields |
|---|---|
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/model/FieldPath` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath#internalPath()` |

| ### Public methods |
|---|---|
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath#documentId()()` Returns A special sentinel `FieldPath` to refer to the ID of a document. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath#equals(java.lang.Object)(https://developer.android.com/reference/kotlin/java/lang/Object.html o)` |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath#hashCode()()` |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath#of(java.lang.String...)(String[] fieldNames)` Creates a `FieldPath` from the provided field names. |
| `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath#toString()()` |

## Public fields

### internalPath

```
public final FieldPath internalPath
```

## Public methods

### documentId

```
public static @NonNull FieldPath documentId()
```

Returns A special sentinel `FieldPath` to refer to the ID of a document. It can be used in queries to sort or filter by the document ID.

### equals

```
public boolean equals(Object o)
```

### hashCode

```
public int hashCode()
```

### of

```
public static @NonNull FieldPath of(String[] fieldNames)
```

Creates a `FieldPath` from the provided field names. If more than one field name is provided, the path will point to a nested field in a document.

| Parameters |
|---|---|
| `String[] fieldNames` | A list of field names. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath` | A `FieldPath` that points to a field location in a document. |

### toString

```
public String toString()
```