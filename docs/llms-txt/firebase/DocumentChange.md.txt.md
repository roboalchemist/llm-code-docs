# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange.md.txt

# DocumentChange

# DocumentChange


```
public class DocumentChange
```

<br />

*** ** * ** ***

A `DocumentChange` represents a change to the documents matching a query. It contains the document affected and a the type of change that occurred (added, modified, or removed).

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

| ### Nested types |
|---|
| `public enum https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange.Type` An enumeration of snapshot diff types. |

| ### Public fields |
|---|---|
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QueryDocumentSnapshot` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange#document()` |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange#newIndex()` The index in the new snapshot, after processing all previous changes. |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange#oldIndex()` The index in the old snapshot, after processing all previous changes. |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange.Type` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange#type()` |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange#equals(java.lang.Object)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html object)` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QueryDocumentSnapshot` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange#getDocument()()` Returns the newly added or modified document if this `DocumentChange` is for an updated document. |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange#getNewIndex()()` The index of the changed document in the result set immediately after this ` DocumentChange` (assuming that all prior `DocumentChange` objects and the current ` DocumentChange` object have been applied). |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange#getOldIndex()()` The index of the changed document in the result set immediately prior to this ` DocumentChange` (assuming that all prior `DocumentChange` objects have been applied). |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange.Type` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange#getType()()` |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange#hashCode()()` |

## Public fields

### document

```
public final QueryDocumentSnapshot document
```

### newIndex

```
public final int newIndex
```

The index in the new snapshot, after processing all previous changes.

### oldIndex

```
public final int oldIndex
```

The index in the old snapshot, after processing all previous changes.

### type

```
public final DocumentChange.Type type
```

## Public methods

### equals

```
public boolean equals(@Nullable Object object)
```

### getDocument

```
public @NonNull QueryDocumentSnapshot getDocument()
```

Returns the newly added or modified document if this `DocumentChange` is for an updated document. Returns the deleted document if this document change represents a removal.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QueryDocumentSnapshot` | A snapshot of the new data (for `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange.Type#ADDED` or `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange.Type#MODIFIED`) or the removed data (for `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange.Type#REMOVED`). |

### getNewIndex

```
public int getNewIndex()
```

The index of the changed document in the result set immediately after this `
DocumentChange` (assuming that all prior `DocumentChange` objects and the current `
DocumentChange` object have been applied). Returns -1 for 'removed' events.

### getOldIndex

```
public int getOldIndex()
```

The index of the changed document in the result set immediately prior to this `
DocumentChange` (assuming that all prior `DocumentChange` objects have been applied). Returns -1 for 'added' events.

### getType

```
public @NonNull DocumentChange.Type getType()
```

### hashCode

```
public int hashCode()
```