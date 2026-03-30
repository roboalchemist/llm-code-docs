# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore.md.txt

# FirebaseFirestore

# FirebaseFirestore


```
class FirebaseFirestore
```

<br />

*** ** * ** ***

Represents a Cloud Firestore database and is the entry point for all Cloud Firestore operations.

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#addSnapshotsInSyncListener(java.lang.Runnable)(runnable: https://developer.android.com/reference/kotlin/java/lang/Runnable.html)` Attaches a listener for a snapshots-in-sync event. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#addSnapshotsInSyncListener(android.app.Activity,java.lang.Runnable)(activity: https://developer.android.com/reference/kotlin/android/app/Activity.html, runnable: https://developer.android.com/reference/kotlin/java/lang/Runnable.html)` Attaches a listener for a snapshots-in-sync event. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#addSnapshotsInSyncListener(java.util.concurrent.Executor,java.lang.Runnable)(executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html, runnable: https://developer.android.com/reference/kotlin/java/lang/Runnable.html)` Attaches a listener for a snapshots-in-sync event. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#batch()()` Creates a write batch, used for performing multiple writes as a single atomic operation. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#clearPersistence()()` Clears the persistent storage, including pending writes and cached documents. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/CollectionReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#collection(java.lang.String)(collectionPath: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Gets a `CollectionReference` instance that refers to the collection at the specified path within the database. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#collectionGroup(java.lang.String)(collectionId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates and returns a new `Query` that includes all documents in the database that are contained in a collection or subcollection with the given `collectionId`. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#disableNetwork()()` Disables network access for this instance. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#document(java.lang.String)(documentPath: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Gets a \`DocumentReference\` instance that refers to the document at the specified path within the database. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#enableNetwork()()` Re-enables network usage for this instance after a prior call to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#disableNetwork()`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#getApp()()` Returns the FirebaseApp instance to which this `FirebaseFirestore` belongs. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#getFirestoreSettings()()` Returns the settings used by this `FirebaseFirestore` object. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#getInstance()()` Returns the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance for the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#getInstance(com.google.firebase.FirebaseApp)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` Returns the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance for the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#getInstance(java.lang.String)(database: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance for the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#getInstance(com.google.firebase.FirebaseApp,java.lang.String)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp, database: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance for the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#getNamedQuery(java.lang.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Reads a Firestore `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` from local cache, identified by the given name. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#loadBundle(byte[])(bundleData: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)` Loads a Firestore bundle into the local cache. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#loadBundle(java.nio.ByteBuffer)(bundleData: https://developer.android.com/reference/kotlin/java/nio/ByteBuffer.html)` Loads a Firestore bundle into the local cache. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#loadBundle(java.io.InputStream)(bundleData: https://developer.android.com/reference/kotlin/java/io/InputStream.html)` Loads a Firestore bundle into the local cache. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource` | `@https://firebase.google.com/docs/reference/kotlin/com/google/common/annotations/Beta https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#pipeline()()` Creates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource` to build and execute a data pipeline. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#runBatch(com.google.firebase.firestore.WriteBatch.Function)(batchFunction: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch.Function)` Executes a batchFunction on a newly created `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch` and then commits all of the writes made by the batchFunction as a single atomic unit. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TResult!>` | `<TResult> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#runTransaction(com.google.firebase.firestore.Transaction.Function<TResult>)(updateFunction: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction.Function<TResult!>)` Executes the given `updateFunction` and then attempts to commit the changes applied within the transaction. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TResult!>` | `<TResult> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#runTransaction(com.google.firebase.firestore.TransactionOptions,com.google.firebase.firestore.Transaction.Function<TResult>)( options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/TransactionOptions, updateFunction: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction.Function<TResult!> )` Executes the given `updateFunction` and then attempts to commit the changes applied within the transaction. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#setFirestoreSettings(com.google.firebase.firestore.FirebaseFirestoreSettings)(settings: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings)` Sets any custom settings used to configure this `FirebaseFirestore` object. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/annotations/PreviewApi [setIndexConfiguration](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#setIndexConfiguration(java.lang.String))(json: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` **This function is deprecated.** Instead of creating cache indexes manually, consider using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheIndexManager#enableIndexAutoCreation()` to let the SDK decide whether to create cache indexes for queries running locally. <br /> |
| `java-static https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#setLoggingEnabled(boolean)(loggingEnabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Globally enables / disables Cloud Firestore logging for the SDK. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#terminate()()` Terminates this `FirebaseFirestore` instance. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#useEmulator(java.lang.String,int)(host: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, port: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Modifies this FirebaseDatabase instance to communicate with the Cloud Firestore emulator. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#waitForPendingWrites()()` Waits until all currently pending writes for the active user have been acknowledged by the backend. |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheIndexManager?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#persistentCacheIndexManager()` |

## Public functions

### addSnapshotsInSyncListener

```
fun addSnapshotsInSyncListener(runnable: Runnable): ListenerRegistration
```

Attaches a listener for a snapshots-in-sync event. The snapshots-in-sync event indicates that all listeners affected by a given change have fired, even if a single server-generated change affects multiple listeners.

NOTE: The snapshots-in-sync event only indicates that listeners are in sync with each other, but does not relate to whether those snapshots are in sync with the server. Use SnapshotMetadata in the individual listeners to determine if a snapshot is from the cache or the server.

| Parameters |
|---|---|
| `runnable: https://developer.android.com/reference/kotlin/java/lang/Runnable.html` | A callback to be called every time all snapshot listeners are in sync with each other. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### addSnapshotsInSyncListener

```
fun addSnapshotsInSyncListener(activity: Activity, runnable: Runnable): ListenerRegistration
```

Attaches a listener for a snapshots-in-sync event. The snapshots-in-sync event indicates that all listeners affected by a given change have fired, even if a single server-generated change affects multiple listeners.

NOTE: The snapshots-in-sync event only indicates that listeners are in sync with each other, but does not relate to whether those snapshots are in sync with the server. Use SnapshotMetadata in the individual listeners to determine if a snapshot is from the cache or the server.

| Parameters |
|---|---|
| `activity: https://developer.android.com/reference/kotlin/android/app/Activity.html` | The activity to scope the listener to. |
| `runnable: https://developer.android.com/reference/kotlin/java/lang/Runnable.html` | A callback to be called every time all snapshot listeners are in sync with each other. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### addSnapshotsInSyncListener

```
fun addSnapshotsInSyncListener(executor: Executor, runnable: Runnable): ListenerRegistration
```

Attaches a listener for a snapshots-in-sync event. The snapshots-in-sync event indicates that all listeners affected by a given change have fired, even if a single server-generated change affects multiple listeners.

NOTE: The snapshots-in-sync event only indicates that listeners are in sync with each other, but does not relate to whether those snapshots are in sync with the server. Use SnapshotMetadata in the individual listeners to determine if a snapshot is from the cache or the server.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | The executor to use to call the listener. |
| `runnable: https://developer.android.com/reference/kotlin/java/lang/Runnable.html` | A callback to be called every time all snapshot listeners are in sync with each other. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### batch

```
fun batch(): WriteBatch
```

Creates a write batch, used for performing multiple writes as a single atomic operation.

The maximum number of writes allowed in a single batch is 500, but note that each usage of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue#serverTimestamp()`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue#arrayUnion(java.lang.Object...)`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue#arrayRemove(java.lang.Object...)`, or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue#increment(long)` inside a transaction counts as an additional write.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch` | The created WriteBatch object. |

### clearPersistence

```
fun clearPersistence(): Task<Void!>
```

Clears the persistent storage, including pending writes and cached documents.

Must be called while the `FirebaseFirestore` instance is not started (after the app is shutdown or when the app is first initialized). On startup, this method must be called before other methods (other than `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#setFirestoreSettings(com.google.firebase.firestore.FirebaseFirestoreSettings)`). If the `FirebaseFirestore` instance is still running, the `Task` will fail with an error code of `FAILED_PRECONDITION`.

Note: `clearPersistence()` is primarily intended to help write reliable tests that use Cloud Firestore. It uses an efficient mechanism for dropping existing data but does not attempt to securely overwrite or otherwise make cached data unrecoverable. For applications that are sensitive to the disclosure of cached data in between user sessions, we strongly recommend not enabling persistence at all.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | A `Task` that is resolved when the persistent storage is cleared. Otherwise, the `Task` is rejected with an error. |

### collection

```
fun collection(collectionPath: String): CollectionReference
```

Gets a `CollectionReference` instance that refers to the collection at the specified path within the database.

| Parameters |
|---|---|
| `collectionPath: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A slash-separated path to a collection. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/CollectionReference` | The `CollectionReference` instance. |

### collectionGroup

```
fun collectionGroup(collectionId: String): Query
```

Creates and returns a new `Query` that includes all documents in the database that are contained in a collection or subcollection with the given `collectionId`.

| Parameters |
|---|---|
| `collectionId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Identifies the collections to query over. Every collection or subcollection with this ID as the last segment of its path will be included. Cannot contain a slash. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created Query. |

### disableNetwork

```
fun disableNetwork(): Task<Void!>
```

Disables network access for this instance. While the network is disabled, any snapshot listeners or `get()` calls will return results from cache, and any write operations will be queued until network usage is re-enabled via a call to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#enableNetwork()`.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | A Task that will be completed once networking is disabled. |

### document

```
fun document(documentPath: String): DocumentReference
```

Gets a \`DocumentReference\` instance that refers to the document at the specified path within the database.

| Parameters |
|---|---|
| `documentPath: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A slash-separated path to a document. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` | The DocumentReference instance. |

### enableNetwork

```
fun enableNetwork(): Task<Void!>
```

Re-enables network usage for this instance after a prior call to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#disableNetwork()`.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | A Task that will be completed once networking is enabled. |

### getApp

```
fun getApp(): FirebaseApp
```

Returns the FirebaseApp instance to which this `FirebaseFirestore` belongs.

### getFirestoreSettings

```
fun getFirestoreSettings(): FirebaseFirestoreSettings
```

Returns the settings used by this `FirebaseFirestore` object.

### getInstance

```
java-static fun getInstance(): FirebaseFirestore
```

Returns the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance for the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

Returns the same instance for all invocations. If no instance exists, initializes a new instance.

The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance.

### getInstance

```
java-static fun getInstance(app: FirebaseApp): FirebaseFirestore
```

Returns the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance for the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

For a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`, invocation always returns the same instance. If no instance exists, initializes a new instance.

The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance.

| Parameters |
|---|---|
| `app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` instance that the returned `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance is associated with. |

### getInstance

```
java-static fun getInstance(database: String): FirebaseFirestore
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance for the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

Returns the same instance for all invocations given the same database parameter. If no instance exists, initializes a new instance.

The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance.

| Parameters |
|---|---|
| `database: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The database ID. |

### getInstance

```
java-static fun getInstance(app: FirebaseApp, database: String): FirebaseFirestore
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance for the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

Returns the same instance for all invocations given the same `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and database parameter. If no instance exists, initializes a new instance.

The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance.

| Parameters |
|---|---|
| `app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` instance that the returned `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance is associated with. |
| `database: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The database ID. |

### getNamedQuery

```
fun getNamedQuery(name: String): Task<Query!>
```

Reads a Firestore `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` from local cache, identified by the given name.

The named queries are packaged into bundles on the server side (along with resulting documents) and loaded to local cache using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#loadBundle(byte[])`. Once in local cache, you can use this method to extract a query by name.

### loadBundle

```
fun loadBundle(bundleData: ByteArray): LoadBundleTask
```

Loads a Firestore bundle into the local cache.

| Parameters |
|---|---|
| `bundleData: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | A byte array representing the bundle to be loaded. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask`, which notifies callers with progress updates, and completion or error events. |

### loadBundle

```
fun loadBundle(bundleData: ByteBuffer): LoadBundleTask
```

Loads a Firestore bundle into the local cache.

| Parameters |
|---|---|
| `bundleData: https://developer.android.com/reference/kotlin/java/nio/ByteBuffer.html` | A ByteBuffer representing the bundle to be loaded. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask`, which notifies callers with progress updates, and completion or error events. |

### loadBundle

```
fun loadBundle(bundleData: InputStream): LoadBundleTask
```

Loads a Firestore bundle into the local cache.

| Parameters |
|---|---|
| `bundleData: https://developer.android.com/reference/kotlin/java/io/InputStream.html` | A stream representing the bundle to be loaded. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LoadBundleTask`, which notifies callers with progress updates, and completion or error events. |

### pipeline

```
@Beta
fun pipeline(): PipelineSource
```

Creates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource` to build and execute a data pipeline.

A pipeline is composed of a sequence of stages. Each stage processes the output from the previous one, and the final stage's output is the result of the pipeline's execution.

**Example usage:**

```kotlin
Pipeline pipeline = firestore.pipeline()
.collection("books")
.where(Field("rating").isGreaterThan(4.5))
.sort(Field("rating").descending())
.limit(2);
```

**Note on Execution:** The stages are conceptual. The Firestore backend may optimize execution (e.g., reordering or merging stages) as long as the final result remains the same.

**Important Limitations:**

- Pipelines operate on a **request/response basis only**.
- They do **not** utilize or update the local SDK cache.
- They do **not** support realtime snapshot listeners.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource` | A `PipelineSource` to begin defining the pipeline's stages. |

### runBatch

```
fun runBatch(batchFunction: WriteBatch.Function): Task<Void!>
```

Executes a batchFunction on a newly created `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch` and then commits all of the writes made by the batchFunction as a single atomic unit.

| Parameters |
|---|---|
| `batchFunction: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch.Function` | The function to execute within the batch context. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | A Task that will be resolved when the batch has been committed. |

### runTransaction

```
fun <TResult> runTransaction(updateFunction: Transaction.Function<TResult!>): Task<TResult!>
```

Executes the given `updateFunction` and then attempts to commit the changes applied within the transaction. If any document read within the transaction has changed, the updateFunction will be retried. If it fails to commit after 5 attempts (the default failure limit), the transaction will fail. To have a different number of retries, use the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#runTransaction(com.google.firebase.firestore.TransactionOptions,com.google.firebase.firestore.Transaction.Function<TResult>)` method instead.

| Parameters |
|---|---|
| `updateFunction: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction.Function<TResult!>` | The function to execute within the transaction context. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TResult!>` | The task returned from the updateFunction. |

### runTransaction

```
fun <TResult> runTransaction(
    options: TransactionOptions,
    updateFunction: Transaction.Function<TResult!>
): Task<TResult!>
```

Executes the given `updateFunction` and then attempts to commit the changes applied within the transaction. If any document read within the transaction has changed, the updateFunction will be retried. If it fails to commit after the maxmimum number of attempts specified in transactionOptions, the transaction will fail.

| Parameters |
|---|---|
| `options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/TransactionOptions` | The transaction options for controlling execution. |
| `updateFunction: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction.Function<TResult!>` | The function to execute within the transaction context. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TResult!>` | The task returned from the updateFunction. |

### setFirestoreSettings

```
fun setFirestoreSettings(settings: FirebaseFirestoreSettings): Unit
```

Sets any custom settings used to configure this `FirebaseFirestore` object. This method can only be called before calling any other methods on this object.

### setIndexConfiguration

```
@PreviewApi
fun [setIndexConfiguration](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#setIndexConfiguration(java.lang.String))(json: String): Task<Void!>
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Instead of creating cache indexes manually, consider using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheIndexManager#enableIndexAutoCreation()` to let the SDK decide whether to create cache indexes for queries running locally.

Configures indexing for local query execution. Any previous index configuration is overridden. The Task resolves once the index configuration has been persisted.

The index entries themselves are created asynchronously. You can continue to use queries that require indexing even if the indices are not yet available. Query execution will automatically start using the index once the index entries have been written.

The method accepts the JSON format exported by the Firebase CLI (\`firebase firestore:indexes\`). If the JSON format is invalid, this method throws an exception.

| Parameters |
|---|---|
| `json: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The JSON format exported by the Firebase CLI. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | A task that resolves once all indices are successfully configured. |

| Throws |
|---|---|
| `java.lang.IllegalArgumentException: https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html` | if the JSON format is invalid |

### setLoggingEnabled

```
java-static fun setLoggingEnabled(loggingEnabled: Boolean): Unit
```

Globally enables / disables Cloud Firestore logging for the SDK.

### terminate

```
fun terminate(): Task<Void!>
```

Terminates this `FirebaseFirestore` instance.

After calling `terminate()` only the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#clearPersistence()` method may be used. Any other method will throw an `https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html`.

To restart after termination, simply create a new instance of `FirebaseFirestore` with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#getInstance()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#getInstance(com.google.firebase.FirebaseApp)`.

`terminate()` does not cancel any pending writes and any tasks that are awaiting a response from the server will not be resolved. The next time you start this instance, it will resume attempting to send these writes to the server.

Note: Under normal circumstances, calling `terminate()` is not required. This method is useful only when you want to force this instance to release all of its resources or in combination with clearPersistence to ensure that all local state is destroyed between test runs.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | A `Task` that is resolved when the instance has been successfully terminated. |

### useEmulator

```
fun useEmulator(host: String, port: Int): Unit
```

Modifies this FirebaseDatabase instance to communicate with the Cloud Firestore emulator.

Note: Call this method before using the instance to do any database operations.

| Parameters |
|---|---|
| `host: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the emulator host (for example, 10.0.2.2) |
| `port: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | the emulator port (for example, 8080) |

### waitForPendingWrites

```
fun waitForPendingWrites(): Task<Void!>
```

Waits until all currently pending writes for the active user have been acknowledged by the backend.

The returned Task completes immediately if there are no outstanding writes. Otherwise, the Task waits for all previously issued writes (including those written in a previous app session), but it does not wait for writes that were added after the method is called. If you wish to wait for additional writes, you have to call `waitForPendingWrites()` again.

Any outstanding `waitForPendingWrites()` Tasks are cancelled during user changes.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | A `Task` which resolves when all currently pending writes have been acknowledged by the backend. |

## Public properties

### persistentCacheIndexManager

```
val persistentCacheIndexManager: PersistentCacheIndexManager?
```