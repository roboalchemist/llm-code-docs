# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot.md.txt

# QuerySnapshot

# QuerySnapshot


```
public class QuerySnapshot implements Iterable
```

<br />

*** ** * ** ***

A `QuerySnapshot` contains the results of a query. It can contain zero or more `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot` objects.

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

| ### Public fields |
|---|---|
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotMetadata` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot#metadata()` |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot#equals(java.lang.Object)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html obj)` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot#getDocumentChanges()()` Returns the list of documents that changed since the last snapshot. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot#getDocumentChanges(com.google.firebase.firestore.MetadataChanges)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges metadataChanges)` Returns the list of documents that changed since the last snapshot. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot#getDocuments()()` Returns the documents in this `QuerySnapshot` as a List in order of the query. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotMetadata` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot#getMetadata()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot#getQuery()()` |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot#hashCode()()` |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot#isEmpty()()` Returns true if there are no documents in the `QuerySnapshot`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Iterator.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QueryDocumentSnapshot>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot#iterator()()` |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot#size()()` Returns the number of documents in the `QuerySnapshot`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<T>` | `<T> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot#toObjects(java.lang.Class<T>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> clazz)` Returns the contents of the documents in the `QuerySnapshot`, converted to the provided class, as a list. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<T>` | `<T> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot#toObjects(java.lang.Class<T>,com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> clazz, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the contents of the documents in the `QuerySnapshot`, converted to the provided class, as a list. |

| ### Extension functions |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T>` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot#(com.google.firebase.firestore.QuerySnapshot).toObjects()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot receiver)` Returns the contents of the documents in the QuerySnapshot, converted to the provided class, as a list. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T>` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot#(com.google.firebase.firestore.QuerySnapshot).toObjects(com.google.firebase.firestore.DocumentSnapshot.ServerTimestampBehavior)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/QuerySnapshot receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior )` Returns the contents of the documents in the QuerySnapshot, converted to the provided class, as a list. |

| ### Inherited methods |
|---|
| From [java.lang.Iterable](https://developer.android.com/reference/kotlin/java/lang/Iterable.html) |---|---| | `void` | `https://developer.android.com/reference/kotlin/java/lang/Iterable.html#forEach-java.util.function.Consumer&lt;? super T&gt;-(https://developer.android.com/reference/kotlin/java/util/function/Consumer.html<https://developer.android.com/reference/kotlin/java/lang/Object.html> action)` | | `https://developer.android.com/reference/kotlin/java/util/Spliterator.html<T>` | `https://developer.android.com/reference/kotlin/java/lang/Iterable.html#spliterator--()` | |

## Public fields

### metadata

```
public final SnapshotMetadata metadata
```

## Public methods

### equals

```
public boolean equals(@Nullable Object obj)
```

### getDocumentChanges

```
public @NonNull List<DocumentChange> getDocumentChanges()
```

Returns the list of documents that changed since the last snapshot. If it's the first snapshot all documents will be in the list as added changes.

Documents with changes only to their metadata will not be included.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange>` | The list of document changes since the last snapshot. |

### getDocumentChanges

```
public @NonNull List<DocumentChange> getDocumentChanges(@NonNull MetadataChanges metadataChanges)
```

Returns the list of documents that changed since the last snapshot. If it's the first snapshot all documents will be in the list as added changes.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges metadataChanges` | Indicates whether metadata-only changes (specifically, only ` DocumentSnapshot.getMetadata()` changed) should be included. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentChange>` | The list of document changes since the last snapshot. |

### getDocuments

```
public @NonNull List<DocumentSnapshot> getDocuments()
```

Returns the documents in this `QuerySnapshot` as a List in order of the query.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot>` | The list of documents. |

### getMetadata

```
public @NonNull SnapshotMetadata getMetadata()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotMetadata` | The metadata for this query snapshot. |

### getQuery

```
public @NonNull Query getQuery()
```

### hashCode

```
public int hashCode()
```

### isEmpty

```
public boolean isEmpty()
```

Returns true if there are no documents in the `QuerySnapshot`.

### iterator

```
public @NonNull Iterator<QueryDocumentSnapshot> iterator()
```

### size

```
public int size()
```

Returns the number of documents in the `QuerySnapshot`.

### toObjects

```
public @NonNull List<T> <T> toObjects(@NonNull Class<T> clazz)
```

Returns the contents of the documents in the `QuerySnapshot`, converted to the provided class, as a list.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> clazz` | The POJO type used to convert the documents in the list. |

### toObjects

```
public @NonNull List<T> <T> toObjects(
    @NonNull Class<T> clazz,
    @NonNull DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior
)
```

Returns the contents of the documents in the `QuerySnapshot`, converted to the provided class, as a list.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> clazz` | The POJO type used to convert the documents in the list. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet been set to their final value. |

## Extension functions

### FirestoreKt.toObjects

```
public final @NonNull List<@NonNull T> <T extends Object> FirestoreKt.toObjects(@NonNull QuerySnapshot receiver)
```

Returns the contents of the documents in the QuerySnapshot, converted to the provided class, as a list.

| Parameters |
|---|---|
| `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html>` | The POJO type used to convert the documents in the list. |

### FirestoreKt.toObjects

```
public final @NonNull List<@NonNull T> <T extends Object> FirestoreKt.toObjects(
    @NonNull QuerySnapshot receiver,
    @NonNull DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior
)
```

Returns the contents of the documents in the QuerySnapshot, converted to the provided class, as a list.

| Parameters |
|---|---|
| `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html>` | The POJO type used to convert the documents in the list. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot.ServerTimestampBehavior serverTimestampBehavior` | Configures the behavior for server timestamps that have not yet ``` been set to their final value. ``` |