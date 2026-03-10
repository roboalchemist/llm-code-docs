# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference.md.txt

# DocumentReference

# DocumentReference


```
public final class DocumentReference
```

<br />

*** ** * ** ***

A `DocumentReference` refers to a document location in a Cloud Firestore database and can be used to write, read, or listen to the location. There may or may not exist a document at the referenced location. A `DocumentReference` can also be used to create a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/CollectionReference` to a subcollection.

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

| ### Public fields |
|---|---|
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#firestore()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#addSnapshotListener(com.google.firebase.firestore.EventListener<com.google.firebase.firestore.DocumentSnapshot>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot> listener)` Starts listening to the document referenced by this `DocumentReference`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#addSnapshotListener(android.app.Activity,com.google.firebase.firestore.EventListener<com.google.firebase.firestore.DocumentSnapshot>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot> listener )` Starts listening to the document referenced by this `DocumentReference` using an Activity-scoped listener. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#addSnapshotListener(java.util.concurrent.Executor,com.google.firebase.firestore.EventListener<com.google.firebase.firestore.DocumentSnapshot>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot> listener )` Starts listening to the document referenced by this `DocumentReference`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#addSnapshotListener(com.google.firebase.firestore.MetadataChanges,com.google.firebase.firestore.EventListener<com.google.firebase.firestore.DocumentSnapshot>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges metadataChanges, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot> listener )` Starts listening to the document referenced by this `DocumentReference` with the given options. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#addSnapshotListener(com.google.firebase.firestore.SnapshotListenOptions,com.google.firebase.firestore.EventListener<com.google.firebase.firestore.DocumentSnapshot>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions options, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot> listener )` Starts listening to the document referenced by this `DocumentReference` with the given options. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#addSnapshotListener(android.app.Activity,com.google.firebase.firestore.MetadataChanges,com.google.firebase.firestore.EventListener<com.google.firebase.firestore.DocumentSnapshot>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges metadataChanges, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot> listener )` Starts listening to the document referenced by this `DocumentReference` with the given options using an Activity-scoped listener. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#addSnapshotListener(java.util.concurrent.Executor,com.google.firebase.firestore.MetadataChanges,com.google.firebase.firestore.EventListener<com.google.firebase.firestore.DocumentSnapshot>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges metadataChanges, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot> listener )` Starts listening to the document referenced by this `DocumentReference` with the given options. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/CollectionReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#collection(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html collectionPath)` Gets a `CollectionReference` instance that refers to the subcollection at the specified path relative to this document. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#delete()()` Deletes the document referred to by this `DocumentReference`. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#equals(java.lang.Object)(https://developer.android.com/reference/kotlin/java/lang/Object.html o)` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#get()()` Reads the document referenced by this `DocumentReference`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#get(com.google.firebase.firestore.Source)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Source source)` Reads the document referenced by this `DocumentReference`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#getFirestore()()` Gets the Cloud Firestore instance associated with this document reference. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#getId()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/CollectionReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#getParent()()` Gets a `CollectionReference` to the collection that contains this document. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#getPath()()` Gets the path of this document (relative to the root of the database) as a slash-separated string. |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#hashCode()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#set(java.lang.Object)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html data)` Overwrites the document referred to by this `DocumentReference`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#set(java.lang.Object,com.google.firebase.firestore.SetOptions)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html data, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SetOptions options)` Writes to the document referred to by this `DocumentReference`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#toString()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#update(java.util.Map<java.lang.String,java.lang.Object>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/Object.html> data)` Updates fields in the document referred to by this `DocumentReference`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#update(java.lang.String,java.lang.Object,java.lang.Object...)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value, Object[] moreFieldsAndValues )` Updates fields in the document referred to by this `DocumentReference`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#update(com.google.firebase.firestore.FieldPath,java.lang.Object,java.lang.Object...)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value, Object[] moreFieldsAndValues )` Updates fields in the document referred to by this `DocumentReference`. |

| ### Extension functions |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<T>` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#(com.google.firebase.firestore.DocumentReference).dataObjects(com.google.firebase.firestore.MetadataChanges)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges metadataChanges )` Starts listening to the document referenced by this `DocumentReference` with the given options and emits its values converted to a POJO via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirestoreKt.https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference#(com.google.firebase.firestore.DocumentReference).snapshots(com.google.firebase.firestore.MetadataChanges)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges metadataChanges )` Starts listening to the document referenced by this `DocumentReference` with the given options and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. |

## Public fields

### firestore

```
public final FirebaseFirestore firestore
```

## Public methods

### addSnapshotListener

```
public @NonNull ListenerRegistration addSnapshotListener(@NonNull EventListener<DocumentSnapshot> listener)
```

Starts listening to the document referenced by this `DocumentReference`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot> listener` | The event listener that will be called with the snapshots. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### addSnapshotListener

```
public @NonNull ListenerRegistration addSnapshotListener(
    @NonNull Activity activity,
    @NonNull EventListener<DocumentSnapshot> listener
)
```

Starts listening to the document referenced by this `DocumentReference` using an Activity-scoped listener.

The listener will be automatically removed during `https://developer.android.com/reference/kotlin/android/app/Activity.html#onStop--`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity` | The activity to scope the listener to. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot> listener` | The event listener that will be called with the snapshots. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### addSnapshotListener

```
public @NonNull ListenerRegistration addSnapshotListener(
    @NonNull Executor executor,
    @NonNull EventListener<DocumentSnapshot> listener
)
```

Starts listening to the document referenced by this `DocumentReference`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` | The executor to use to call the listener. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot> listener` | The event listener that will be called with the snapshots. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### addSnapshotListener

```
public @NonNull ListenerRegistration addSnapshotListener(
    @NonNull MetadataChanges metadataChanges,
    @NonNull EventListener<DocumentSnapshot> listener
)
```

Starts listening to the document referenced by this `DocumentReference` with the given options.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges metadataChanges` | Indicates whether metadata-only changes (specifically, only ` DocumentSnapshot.getMetadata()` changed) should trigger snapshot events. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot> listener` | The event listener that will be called with the snapshots. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### addSnapshotListener

```
public @NonNull ListenerRegistration addSnapshotListener(
    @NonNull SnapshotListenOptions options,
    @NonNull EventListener<DocumentSnapshot> listener
)
```

Starts listening to the document referenced by this `DocumentReference` with the given options.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SnapshotListenOptions options` | Sets snapshot listener options, including whether metadata-only changes should trigger snapshot events, the source to listen to, the executor to use to call the listener, or the activity to scope the listener to. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot> listener` | The event listener that will be called with the snapshots. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### addSnapshotListener

```
public @NonNull ListenerRegistration addSnapshotListener(
    @NonNull Activity activity,
    @NonNull MetadataChanges metadataChanges,
    @NonNull EventListener<DocumentSnapshot> listener
)
```

Starts listening to the document referenced by this `DocumentReference` with the given options using an Activity-scoped listener.

The listener will be automatically removed during `https://developer.android.com/reference/kotlin/android/app/Activity.html#onStop--`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity` | The activity to scope the listener to. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges metadataChanges` | Indicates whether metadata-only changes (specifically, only ` DocumentSnapshot.getMetadata()` changed) should trigger snapshot events. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot> listener` | The event listener that will be called with the snapshots. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### addSnapshotListener

```
public @NonNull ListenerRegistration addSnapshotListener(
    @NonNull Executor executor,
    @NonNull MetadataChanges metadataChanges,
    @NonNull EventListener<DocumentSnapshot> listener
)
```

Starts listening to the document referenced by this `DocumentReference` with the given options.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` | The executor to use to call the listener. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges metadataChanges` | Indicates whether metadata-only changes (specifically, only ` DocumentSnapshot.getMetadata()` changed) should trigger snapshot events. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot> listener` | The event listener that will be called with the snapshots. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### collection

```
public @NonNull CollectionReference collection(@NonNull String collectionPath)
```

Gets a `CollectionReference` instance that refers to the subcollection at the specified path relative to this document.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html collectionPath` | A slash-separated relative path to a subcollection. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/CollectionReference` | The `CollectionReference` instance. |

### delete

```
public @NonNull Task<Void> delete()
```

Deletes the document referred to by this `DocumentReference`.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | A Task that will be resolved when the delete completes. |

### equals

```
public boolean equals(Object o)
```

### get

```
public @NonNull Task<DocumentSnapshot> get()
```

Reads the document referenced by this `DocumentReference`.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot>` | A Task that will be resolved with the contents of the Document at this ` DocumentReference`. |

### get

```
public @NonNull Task<DocumentSnapshot> get(@NonNull Source source)
```

Reads the document referenced by this `DocumentReference`.

By default, `get()` attempts to provide up-to-date data when possible by waiting for data from the server, but it may return cached data or fail if you are offline and the server cannot be reached. This behavior can be altered via the `Source` parameter.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Source source` | A value to configure the get behavior. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentSnapshot>` | A Task that will be resolved with the contents of the Document at this ` DocumentReference`. |

### getFirestore

```
public @NonNull FirebaseFirestore getFirestore()
```

Gets the Cloud Firestore instance associated with this document reference.

### getId

```
public @NonNull String getId()
```

### getParent

```
public @NonNull CollectionReference getParent()
```

Gets a `CollectionReference` to the collection that contains this document.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/CollectionReference` | The `CollectionReference` that contains this document. |

### getPath

```
public @NonNull String getPath()
```

Gets the path of this document (relative to the root of the database) as a slash-separated string.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | The path of this document. |

### hashCode

```
public int hashCode()
```

### set

```
public @NonNull Task<Void> set(@NonNull Object data)
```

Overwrites the document referred to by this `DocumentReference`. If the document does not yet exist, it will be created. If a document already exists, it will be overwritten.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html data` | The data to write to the document (like a Map or a POJO containing the desired document contents). |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | A Task that will be resolved when the write finishes. |

### set

```
public @NonNull Task<Void> set(@NonNull Object data, @NonNull SetOptions options)
```

Writes to the document referred to by this `DocumentReference`. If the document does not yet exist, it will be created. If you pass `SetOptions`, the provided data can be merged into an existing document.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html data` | The data to write to the document (like a Map or a POJO containing the desired document contents). |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/SetOptions options` | An object to configure the set behavior. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | A Task that will be resolved when the write finishes. |

### toString

```
public @NonNull String toString()
```

### update

```
public @NonNull Task<Void> update(@NonNull Map<String, Object> data)
```

Updates fields in the document referred to by this `DocumentReference`. If no document exists yet, the update will fail.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/Object.html> data` | A map of field / value pairs to update. Fields can contain dots to reference nested fields within the document. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | A Task that will be resolved when the write finishes. |

### update

```
public @NonNull Task<Void> update(
    @NonNull String field,
    @Nullable Object value,
    Object[] moreFieldsAndValues
)
```

Updates fields in the document referred to by this `DocumentReference`. If no document exists yet, the update will fail.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field` | The first field to update. Fields can contain dots to reference a nested field within the document. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value` | The first value |
| `Object[] moreFieldsAndValues` | Additional field/value pairs. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | A Task that will be resolved when the write finishes. |

### update

```
public @NonNull Task<Void> update(
    @NonNull FieldPath fieldPath,
    @Nullable Object value,
    Object[] moreFieldsAndValues
)
```

Updates fields in the document referred to by this `DocumentReference`. If no document exists yet, the update will fail.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath` | The first field to update. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value` | The first value |
| `Object[] moreFieldsAndValues` | Additional field/value pairs. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | A Task that will be resolved when the write finishes. |

## Extension functions

### FirestoreKt.dataObjects

```
public final @NonNull Flow<T> <T extends Object> FirestoreKt.dataObjects(
    @NonNull DocumentReference receiver,
    @NonNull MetadataChanges metadataChanges
)
```

Starts listening to the document referenced by this `DocumentReference` with the given options and emits its values converted to a POJO via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener` will be attached.

- When the flow completes, the listener will be removed.

| Parameters |
|---|---|
| `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html>` | The type of the object to convert to. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges metadataChanges` | controls metadata-only changes. Default: `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges#EXCLUDE` |

### FirestoreKt.snapshots

```
public final @NonNull Flow<@NonNull DocumentSnapshot> FirestoreKt.snapshots(
    @NonNull DocumentReference receiver,
    @NonNull MetadataChanges metadataChanges
)
```

Starts listening to the document referenced by this `DocumentReference` with the given options and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/EventListener` will be attached.

- When the flow completes, the listener will be removed.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges metadataChanges` | controls metadata-only changes. Default: `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MetadataChanges#EXCLUDE` |