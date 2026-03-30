# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference.md.txt

# DocumentReference

# DocumentReference


```
class DocumentReference
```

<br />

*** ** * ** ***

A `DocumentReference` refers to a document location in a Cloud Firestore database and can be used to write, read, or listen to the location. There may or may not exist a document at the referenced location. A `DocumentReference` can also be used to create a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/CollectionReference` to a subcollection.

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#addSnapshotListener(com.google.firebase.firestore.EventListener<com.google.firebase.firestore.DocumentSnapshot>)(listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot!>)` Starts listening to the document referenced by this `DocumentReference`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#addSnapshotListener(android.app.Activity,com.google.firebase.firestore.EventListener<com.google.firebase.firestore.DocumentSnapshot>)( activity: https://developer.android.com/reference/kotlin/android/app/Activity.html, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot!> )` Starts listening to the document referenced by this `DocumentReference` using an Activity-scoped listener. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#addSnapshotListener(java.util.concurrent.Executor,com.google.firebase.firestore.EventListener<com.google.firebase.firestore.DocumentSnapshot>)( executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot!> )` Starts listening to the document referenced by this `DocumentReference`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#addSnapshotListener(com.google.firebase.firestore.MetadataChanges,com.google.firebase.firestore.EventListener<com.google.firebase.firestore.DocumentSnapshot>)( metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot!> )` Starts listening to the document referenced by this `DocumentReference` with the given options. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#addSnapshotListener(com.google.firebase.firestore.SnapshotListenOptions,com.google.firebase.firestore.EventListener<com.google.firebase.firestore.DocumentSnapshot>)( options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot!> )` Starts listening to the document referenced by this `DocumentReference` with the given options. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#addSnapshotListener(android.app.Activity,com.google.firebase.firestore.MetadataChanges,com.google.firebase.firestore.EventListener<com.google.firebase.firestore.DocumentSnapshot>)( activity: https://developer.android.com/reference/kotlin/android/app/Activity.html, metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot!> )` Starts listening to the document referenced by this `DocumentReference` with the given options using an Activity-scoped listener. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#addSnapshotListener(java.util.concurrent.Executor,com.google.firebase.firestore.MetadataChanges,com.google.firebase.firestore.EventListener<com.google.firebase.firestore.DocumentSnapshot>)( executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html, metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot!> )` Starts listening to the document referenced by this `DocumentReference` with the given options. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/CollectionReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#collection(java.lang.String)(collectionPath: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Gets a `CollectionReference` instance that refers to the subcollection at the specified path relative to this document. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#delete()()` Deletes the document referred to by this `DocumentReference`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#equals(java.lang.Object)(o: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!)` |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#get()()` Reads the document referenced by this `DocumentReference`. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#get(com.google.firebase.firestore.Source)(source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Source)` Reads the document referenced by this `DocumentReference`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#getId()()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/CollectionReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#getParent()()` Gets a `CollectionReference` to the collection that contains this document. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#getPath()()` Gets the path of this document (relative to the root of the database) as a slash-separated string. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#hashCode()()` |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#set(java.lang.Object)(data: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Overwrites the document referred to by this `DocumentReference`. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#set(java.lang.Object,com.google.firebase.firestore.SetOptions)(data: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html, options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions)` Writes to the document referred to by this `DocumentReference`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#toString()()` |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#update(java.util.Map<java.lang.String,java.lang.Object>)(data: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Updates fields in the document referred to by this `DocumentReference`. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#update(java.lang.String,java.lang.Object,java.lang.Object...)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?, moreFieldsAndValues: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>!)` Updates fields in the document referred to by this `DocumentReference`. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#update(com.google.firebase.firestore.FieldPath,java.lang.Object,java.lang.Object...)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?, moreFieldsAndValues: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>!)` Updates fields in the document referred to by this `DocumentReference`. |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#firestore()` |

| ### Extension functions |
|---|---|
| `inline https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<T?>` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#(com.google.firebase.firestore.DocumentReference).dataObjects(com.google.firebase.firestore.MetadataChanges)(metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges)` Starts listening to the document referenced by this `DocumentReference` with the given options and emits its values converted to a POJO via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. |
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#(com.google.firebase.firestore.DocumentReference).snapshots(com.google.firebase.firestore.MetadataChanges)(metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges)` Starts listening to the document referenced by this `DocumentReference` with the given options and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. |

## Public functions

### addSnapshotListener

```
fun addSnapshotListener(listener: EventListener<DocumentSnapshot!>): ListenerRegistration
```

Starts listening to the document referenced by this `DocumentReference`.

| Parameters |
|---|---|
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot!>` | The event listener that will be called with the snapshots. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### addSnapshotListener

```
fun addSnapshotListener(
    activity: Activity,
    listener: EventListener<DocumentSnapshot!>
): ListenerRegistration
```

Starts listening to the document referenced by this `DocumentReference` using an Activity-scoped listener.

The listener will be automatically removed during `https://developer.android.com/reference/kotlin/android/app/Activity.html#onStop--`.

| Parameters |
|---|---|
| `activity: https://developer.android.com/reference/kotlin/android/app/Activity.html` | The activity to scope the listener to. |
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot!>` | The event listener that will be called with the snapshots. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### addSnapshotListener

```
fun addSnapshotListener(
    executor: Executor,
    listener: EventListener<DocumentSnapshot!>
): ListenerRegistration
```

Starts listening to the document referenced by this `DocumentReference`.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | The executor to use to call the listener. |
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot!>` | The event listener that will be called with the snapshots. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### addSnapshotListener

```
fun addSnapshotListener(
    metadataChanges: MetadataChanges,
    listener: EventListener<DocumentSnapshot!>
): ListenerRegistration
```

Starts listening to the document referenced by this `DocumentReference` with the given options.

| Parameters |
|---|---|
| `metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges` | Indicates whether metadata-only changes (specifically, only ` DocumentSnapshot.getMetadata()` changed) should trigger snapshot events. |
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot!>` | The event listener that will be called with the snapshots. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### addSnapshotListener

```
fun addSnapshotListener(
    options: SnapshotListenOptions,
    listener: EventListener<DocumentSnapshot!>
): ListenerRegistration
```

Starts listening to the document referenced by this `DocumentReference` with the given options.

| Parameters |
|---|---|
| `options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions` | Sets snapshot listener options, including whether metadata-only changes should trigger snapshot events, the source to listen to, the executor to use to call the listener, or the activity to scope the listener to. |
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot!>` | The event listener that will be called with the snapshots. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### addSnapshotListener

```
fun addSnapshotListener(
    activity: Activity,
    metadataChanges: MetadataChanges,
    listener: EventListener<DocumentSnapshot!>
): ListenerRegistration
```

Starts listening to the document referenced by this `DocumentReference` with the given options using an Activity-scoped listener.

The listener will be automatically removed during `https://developer.android.com/reference/kotlin/android/app/Activity.html#onStop--`.

| Parameters |
|---|---|
| `activity: https://developer.android.com/reference/kotlin/android/app/Activity.html` | The activity to scope the listener to. |
| `metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges` | Indicates whether metadata-only changes (specifically, only ` DocumentSnapshot.getMetadata()` changed) should trigger snapshot events. |
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot!>` | The event listener that will be called with the snapshots. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### addSnapshotListener

```
fun addSnapshotListener(
    executor: Executor,
    metadataChanges: MetadataChanges,
    listener: EventListener<DocumentSnapshot!>
): ListenerRegistration
```

Starts listening to the document referenced by this `DocumentReference` with the given options.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | The executor to use to call the listener. |
| `metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges` | Indicates whether metadata-only changes (specifically, only ` DocumentSnapshot.getMetadata()` changed) should trigger snapshot events. |
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot!>` | The event listener that will be called with the snapshots. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### collection

```
fun collection(collectionPath: String): CollectionReference
```

Gets a `CollectionReference` instance that refers to the subcollection at the specified path relative to this document.

| Parameters |
|---|---|
| `collectionPath: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A slash-separated relative path to a subcollection. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/CollectionReference` | The `CollectionReference` instance. |

### delete

```
fun delete(): Task<Void!>
```

Deletes the document referred to by this `DocumentReference`.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | A Task that will be resolved when the delete completes. |

### equals

```
fun equals(o: Any!): Boolean
```

### get

```
fun get(): Task<DocumentSnapshot!>
```

Reads the document referenced by this `DocumentReference`.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot!>` | A Task that will be resolved with the contents of the Document at this ` DocumentReference`. |

### get

```
fun get(source: Source): Task<DocumentSnapshot!>
```

Reads the document referenced by this `DocumentReference`.

By default, `get()` attempts to provide up-to-date data when possible by waiting for data from the server, but it may return cached data or fail if you are offline and the server cannot be reached. This behavior can be altered via the `Source` parameter.

| Parameters |
|---|---|
| `source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Source` | A value to configure the get behavior. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot!>` | A Task that will be resolved with the contents of the Document at this ` DocumentReference`. |

### getId

```
fun getId(): String
```

### getParent

```
fun getParent(): CollectionReference
```

Gets a `CollectionReference` to the collection that contains this document.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/CollectionReference` | The `CollectionReference` that contains this document. |

### getPath

```
fun getPath(): String
```

Gets the path of this document (relative to the root of the database) as a slash-separated string.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The path of this document. |

### hashCode

```
fun hashCode(): Int
```

### set

```
fun set(data: Any): Task<Void!>
```

Overwrites the document referred to by this `DocumentReference`. If the document does not yet exist, it will be created. If a document already exists, it will be overwritten.

| Parameters |
|---|---|
| `data: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The data to write to the document (like a Map or a POJO containing the desired document contents). |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | A Task that will be resolved when the write finishes. |

### set

```
fun set(data: Any, options: SetOptions): Task<Void!>
```

Writes to the document referred to by this `DocumentReference`. If the document does not yet exist, it will be created. If you pass `SetOptions`, the provided data can be merged into an existing document.

| Parameters |
|---|---|
| `data: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The data to write to the document (like a Map or a POJO containing the desired document contents). |
| `options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SetOptions` | An object to configure the set behavior. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | A Task that will be resolved when the write finishes. |

### toString

```
fun toString(): String
```

### update

```
fun update(data: (Mutable)Map<String!, Any!>): Task<Void!>
```

Updates fields in the document referred to by this `DocumentReference`. If no document exists yet, the update will fail.

| Parameters |
|---|---|
| `data: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>` | A map of field / value pairs to update. Fields can contain dots to reference nested fields within the document. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | A Task that will be resolved when the write finishes. |

### update

```
fun update(field: String, value: Any?, moreFieldsAndValues: Array<Any!>!): Task<Void!>
```

Updates fields in the document referred to by this `DocumentReference`. If no document exists yet, the update will fail.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The first field to update. Fields can contain dots to reference a nested field within the document. |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The first value |
| `moreFieldsAndValues: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>!` | Additional field/value pairs. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | A Task that will be resolved when the write finishes. |

### update

```
fun update(fieldPath: FieldPath, value: Any?, moreFieldsAndValues: Array<Any!>!): Task<Void!>
```

Updates fields in the document referred to by this `DocumentReference`. If no document exists yet, the update will fail.

| Parameters |
|---|---|
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The first field to update. |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The first value |
| `moreFieldsAndValues: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>!` | Additional field/value pairs. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | A Task that will be resolved when the write finishes. |

## Public properties

### firestore

```
val firestore: FirebaseFirestore!
```

## Extension functions

### dataObjects

```
inline fun <T : Any> DocumentReference.dataObjects(
    metadataChanges: MetadataChanges = MetadataChanges.EXCLUDE
): Flow<T?>
```

Starts listening to the document referenced by this `DocumentReference` with the given options and emits its values converted to a POJO via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener` will be attached.

- When the flow completes, the listener will be removed.

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The type of the object to convert to. |
| `metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges = MetadataChanges.EXCLUDE` | controls metadata-only changes. Default: `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges#EXCLUDE` |

### snapshots

```
fun DocumentReference.snapshots(
    metadataChanges: MetadataChanges = MetadataChanges.EXCLUDE
): Flow<DocumentSnapshot>
```

Starts listening to the document referenced by this `DocumentReference` with the given options and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener` will be attached.

- When the flow completes, the listener will be removed.

| Parameters |
|---|---|
| `metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges = MetadataChanges.EXCLUDE` | controls metadata-only changes. Default: `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges#EXCLUDE` |