# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore.md.txt

# FirebaseFirestore

# FirebaseFirestore


```
public class FirebaseFirestore
```

<br />

*** ** * ** ***

Represents a Cloud Firestore database and is the entry point for all Cloud Firestore operations.

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

| ### Public fields |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheIndexManager` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#persistentCacheIndexManager()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#addSnapshotsInSyncListener(java.lang.Runnable)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Runnable.html runnable)` Attaches a listener for a snapshots-in-sync event. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#addSnapshotsInSyncListener(android.app.Activity,java.lang.Runnable)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Runnable.html runnable )` Attaches a listener for a snapshots-in-sync event. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#addSnapshotsInSyncListener(java.util.concurrent.Executor,java.lang.Runnable)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Runnable.html runnable )` Attaches a listener for a snapshots-in-sync event. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#batch()()` Creates a write batch, used for performing multiple writes as a single atomic operation. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#clearPersistence()()` Clears the persistent storage, including pending writes and cached documents. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/CollectionReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#collection(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html collectionPath)` Gets a `CollectionReference` instance that refers to the collection at the specified path within the database. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#collectionGroup(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html collectionId)` Creates and returns a new `Query` that includes all documents in the database that are contained in a collection or subcollection with the given `collectionId`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#disableNetwork()()` Disables network access for this instance. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#document(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html documentPath)` Gets a \`DocumentReference\` instance that refers to the document at the specified path within the database. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#enableNetwork()()` Re-enables network usage for this instance after a prior call to `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#disableNetwork()`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#getApp()()` Returns the FirebaseApp instance to which this `FirebaseFirestore` belongs. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#getFirestoreSettings()()` Returns the settings used by this `FirebaseFirestore` object. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#getInstance()()` Returns the default `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` instance for the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#getInstance(com.google.firebase.FirebaseApp)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app)` Returns the default `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` instance for the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#getInstance(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html database)` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` instance for the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#getInstance(com.google.firebase.FirebaseApp,java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html database)` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` instance for the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#getNamedQuery(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name)` Reads a Firestore `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query` from local cache, identified by the given name. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheIndexManager` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#getPersistentCacheIndexManager()()` Gets the `PersistentCacheIndexManager` instance used by this `FirebaseFirestore` object. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#loadBundle(byte[])(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] bundleData)` Loads a Firestore bundle into the local cache. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#loadBundle(java.nio.ByteBuffer)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/nio/ByteBuffer.html bundleData)` Loads a Firestore bundle into the local cache. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#loadBundle(java.io.InputStream)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/io/InputStream.html bundleData)` Loads a Firestore bundle into the local cache. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource` | `@https://firebase.google.com/docs/reference/android/com/google/common/annotations/Beta https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#pipeline()()` Creates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource` to build and execute a data pipeline. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#runBatch(com.google.firebase.firestore.WriteBatch.Function)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch.Function batchFunction)` Executes a batchFunction on a newly created `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch` and then commits all of the writes made by the batchFunction as a single atomic unit. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TResult>` | `<TResult> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#runTransaction(com.google.firebase.firestore.Transaction.Function<TResult>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Transaction.Function<TResult> updateFunction )` Executes the given `updateFunction` and then attempts to commit the changes applied within the transaction. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TResult>` | `<TResult> https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#runTransaction(com.google.firebase.firestore.TransactionOptions,com.google.firebase.firestore.Transaction.Function<TResult>)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/TransactionOptions options, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Transaction.Function<TResult> updateFunction )` Executes the given `updateFunction` and then attempts to commit the changes applied within the transaction. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#setFirestoreSettings(com.google.firebase.firestore.FirebaseFirestoreSettings)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings settings)` Sets any custom settings used to configure this `FirebaseFirestore` object. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `@https://firebase.google.com/docs/reference/android/com/google/firebase/annotations/PreviewApi [setIndexConfiguration](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#setIndexConfiguration(java.lang.String))(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html json)` **This method is deprecated.** Instead of creating cache indexes manually, consider using `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheIndexManager#enableIndexAutoCreation()` to let the SDK decide whether to create cache indexes for queries running locally. <br /> |
| `static void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#setLoggingEnabled(boolean)(boolean loggingEnabled)` Globally enables / disables Cloud Firestore logging for the SDK. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#terminate()()` Terminates this `FirebaseFirestore` instance. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#useEmulator(java.lang.String,int)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html host, int port)` Modifies this FirebaseDatabase instance to communicate with the Cloud Firestore emulator. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#waitForPendingWrites()()` Waits until all currently pending writes for the active user have been acknowledged by the backend. |

## Public fields

### persistentCacheIndexManager

```
public @Nullable PersistentCacheIndexManager persistentCacheIndexManager
```

## Public methods

### addSnapshotsInSyncListener

```
public @NonNull ListenerRegistration addSnapshotsInSyncListener(@NonNull Runnable runnable)
```

Attaches a listener for a snapshots-in-sync event. The snapshots-in-sync event indicates that all listeners affected by a given change have fired, even if a single server-generated change affects multiple listeners.

NOTE: The snapshots-in-sync event only indicates that listeners are in sync with each other, but does not relate to whether those snapshots are in sync with the server. Use SnapshotMetadata in the individual listeners to determine if a snapshot is from the cache or the server.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Runnable.html runnable` | A callback to be called every time all snapshot listeners are in sync with each other. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### addSnapshotsInSyncListener

```
public @NonNull ListenerRegistration addSnapshotsInSyncListener(
    @NonNull Activity activity,
    @NonNull Runnable runnable
)
```

Attaches a listener for a snapshots-in-sync event. The snapshots-in-sync event indicates that all listeners affected by a given change have fired, even if a single server-generated change affects multiple listeners.

NOTE: The snapshots-in-sync event only indicates that listeners are in sync with each other, but does not relate to whether those snapshots are in sync with the server. Use SnapshotMetadata in the individual listeners to determine if a snapshot is from the cache or the server.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/app/Activity.html activity` | The activity to scope the listener to. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Runnable.html runnable` | A callback to be called every time all snapshot listeners are in sync with each other. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### addSnapshotsInSyncListener

```
public @NonNull ListenerRegistration addSnapshotsInSyncListener(
    @NonNull Executor executor,
    @NonNull Runnable runnable
)
```

Attaches a listener for a snapshots-in-sync event. The snapshots-in-sync event indicates that all listeners affected by a given change have fired, even if a single server-generated change affects multiple listeners.

NOTE: The snapshots-in-sync event only indicates that listeners are in sync with each other, but does not relate to whether those snapshots are in sync with the server. Use SnapshotMetadata in the individual listeners to determine if a snapshot is from the cache or the server.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html executor` | The executor to use to call the listener. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Runnable.html runnable` | A callback to be called every time all snapshot listeners are in sync with each other. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### batch

```
public @NonNull WriteBatch batch()
```

Creates a write batch, used for performing multiple writes as a single atomic operation.

The maximum number of writes allowed in a single batch is 500, but note that each usage of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue#serverTimestamp()`, `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue#arrayUnion(java.lang.Object...)`, `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue#arrayRemove(java.lang.Object...)`, or `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue#increment(long)` inside a transaction counts as an additional write.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch` | The created WriteBatch object. |

### clearPersistence

```
public @NonNull Task<Void> clearPersistence()
```

Clears the persistent storage, including pending writes and cached documents.

Must be called while the `FirebaseFirestore` instance is not started (after the app is shutdown or when the app is first initialized). On startup, this method must be called before other methods (other than `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#setFirestoreSettings(com.google.firebase.firestore.FirebaseFirestoreSettings)`). If the `FirebaseFirestore` instance is still running, the `Task` will fail with an error code of `FAILED_PRECONDITION`.

Note: `clearPersistence()` is primarily intended to help write reliable tests that use Cloud Firestore. It uses an efficient mechanism for dropping existing data but does not attempt to securely overwrite or otherwise make cached data unrecoverable. For applications that are sensitive to the disclosure of cached data in between user sessions, we strongly recommend not enabling persistence at all.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | A `Task` that is resolved when the persistent storage is cleared. Otherwise, the `Task` is rejected with an error. |

### collection

```
public @NonNull CollectionReference collection(@NonNull String collectionPath)
```

Gets a `CollectionReference` instance that refers to the collection at the specified path within the database.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html collectionPath` | A slash-separated path to a collection. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/CollectionReference` | The `CollectionReference` instance. |

### collectionGroup

```
public @NonNull Query collectionGroup(@NonNull String collectionId)
```

Creates and returns a new `Query` that includes all documents in the database that are contained in a collection or subcollection with the given `collectionId`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html collectionId` | Identifies the collections to query over. Every collection or subcollection with this ID as the last segment of its path will be included. Cannot contain a slash. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query` | The created Query. |

### disableNetwork

```
public @NonNull Task<Void> disableNetwork()
```

Disables network access for this instance. While the network is disabled, any snapshot listeners or `get()` calls will return results from cache, and any write operations will be queued until network usage is re-enabled via a call to `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#enableNetwork()`.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | A Task that will be completed once networking is disabled. |

### document

```
public @NonNull DocumentReference document(@NonNull String documentPath)
```

Gets a \`DocumentReference\` instance that refers to the document at the specified path within the database.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html documentPath` | A slash-separated path to a document. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference` | The DocumentReference instance. |

### enableNetwork

```
public @NonNull Task<Void> enableNetwork()
```

Re-enables network usage for this instance after a prior call to `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#disableNetwork()`.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | A Task that will be completed once networking is enabled. |

### getApp

```
public @NonNull FirebaseApp getApp()
```

Returns the FirebaseApp instance to which this `FirebaseFirestore` belongs.

### getFirestoreSettings

```
public @NonNull FirebaseFirestoreSettings getFirestoreSettings()
```

Returns the settings used by this `FirebaseFirestore` object.

### getInstance

```
public static @NonNull FirebaseFirestore getInstance()
```

Returns the default `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` instance for the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

Returns the same instance for all invocations. If no instance exists, initializes a new instance.

The `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` instance.

### getInstance

```
public static @NonNull FirebaseFirestore getInstance(@NonNull FirebaseApp app)
```

Returns the default `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` instance for the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

For a given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`, invocation always returns the same instance. If no instance exists, initializes a new instance.

The `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` instance.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` instance that the returned `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` instance is associated with. |

### getInstance

```
public static @NonNull FirebaseFirestore getInstance(@NonNull String database)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` instance for the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

Returns the same instance for all invocations given the same database parameter. If no instance exists, initializes a new instance.

The `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` instance.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html database` | The database ID. |

### getInstance

```
public static @NonNull FirebaseFirestore getInstance(@NonNull FirebaseApp app, @NonNull String database)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` instance for the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

Returns the same instance for all invocations given the same `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and database parameter. If no instance exists, initializes a new instance.

The `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` instance.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` instance that the returned `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` instance is associated with. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html database` | The database ID. |

### getNamedQuery

```
public @NonNull Task<Query> getNamedQuery(@NonNull String name)
```

Reads a Firestore `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query` from local cache, identified by the given name.

The named queries are packaged into bundles on the server side (along with resulting documents) and loaded to local cache using `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#loadBundle(byte[])`. Once in local cache, you can use this method to extract a query by name.

### getPersistentCacheIndexManager

```
public @Nullable PersistentCacheIndexManager getPersistentCacheIndexManager()
```

Gets the `PersistentCacheIndexManager` instance used by this `FirebaseFirestore` object.

This is not the same as Cloud Firestore Indexes. Persistent cache indexes are optional indexes that only exist within the SDK to assist in local query execution.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheIndexManager` | The `PersistentCacheIndexManager` instance or null if local persistent storage is not in use. |

### loadBundle

```
public @NonNull LoadBundleTask loadBundle(@NonNull byte[] bundleData)
```

Loads a Firestore bundle into the local cache.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] bundleData` | A byte array representing the bundle to be loaded. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask`, which notifies callers with progress updates, and completion or error events. |

### loadBundle

```
public @NonNull LoadBundleTask loadBundle(@NonNull ByteBuffer bundleData)
```

Loads a Firestore bundle into the local cache.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/nio/ByteBuffer.html bundleData` | A ByteBuffer representing the bundle to be loaded. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask`, which notifies callers with progress updates, and completion or error events. |

### loadBundle

```
public @NonNull LoadBundleTask loadBundle(@NonNull InputStream bundleData)
```

Loads a Firestore bundle into the local cache.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/io/InputStream.html bundleData` | A stream representing the bundle to be loaded. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LoadBundleTask`, which notifies callers with progress updates, and completion or error events. |

### pipeline

```
@Beta
public @NonNull PipelineSource pipeline()
```

Creates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource` to build and execute a data pipeline.

A pipeline is composed of a sequence of stages. Each stage processes the output from the previous one, and the final stage's output is the result of the pipeline's execution.

**Example usage:**

```
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
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource` | A `PipelineSource` to begin defining the pipeline's stages. |

### runBatch

```
public @NonNull Task<Void> runBatch(@NonNull WriteBatch.Function batchFunction)
```

Executes a batchFunction on a newly created `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch` and then commits all of the writes made by the batchFunction as a single atomic unit.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch.Function batchFunction` | The function to execute within the batch context. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | A Task that will be resolved when the batch has been committed. |

### runTransaction

```
public @NonNull Task<TResult> <TResult> runTransaction(
    @NonNull Transaction.Function<TResult> updateFunction
)
```

Executes the given `updateFunction` and then attempts to commit the changes applied within the transaction. If any document read within the transaction has changed, the updateFunction will be retried. If it fails to commit after 5 attempts (the default failure limit), the transaction will fail. To have a different number of retries, use the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#runTransaction(com.google.firebase.firestore.TransactionOptions,com.google.firebase.firestore.Transaction.Function<TResult>)` method instead.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Transaction.Function<TResult> updateFunction` | The function to execute within the transaction context. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TResult>` | The task returned from the updateFunction. |

### runTransaction

```
public @NonNull Task<TResult> <TResult> runTransaction(
    @NonNull TransactionOptions options,
    @NonNull Transaction.Function<TResult> updateFunction
)
```

Executes the given `updateFunction` and then attempts to commit the changes applied within the transaction. If any document read within the transaction has changed, the updateFunction will be retried. If it fails to commit after the maxmimum number of attempts specified in transactionOptions, the transaction will fail.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/TransactionOptions options` | The transaction options for controlling execution. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Transaction.Function<TResult> updateFunction` | The function to execute within the transaction context. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<TResult>` | The task returned from the updateFunction. |

### setFirestoreSettings

```
public void setFirestoreSettings(@NonNull FirebaseFirestoreSettings settings)
```

Sets any custom settings used to configure this `FirebaseFirestore` object. This method can only be called before calling any other methods on this object.

### setIndexConfiguration

```
@PreviewApi
public @NonNull Task<Void> [setIndexConfiguration](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#setIndexConfiguration(java.lang.String))(@NonNull String json)
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Instead of creating cache indexes manually, consider using `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheIndexManager#enableIndexAutoCreation()` to let the SDK decide whether to create cache indexes for queries running locally.

Configures indexing for local query execution. Any previous index configuration is overridden. The Task resolves once the index configuration has been persisted.

The index entries themselves are created asynchronously. You can continue to use queries that require indexing even if the indices are not yet available. Query execution will automatically start using the index once the index entries have been written.

The method accepts the JSON format exported by the Firebase CLI (\`firebase firestore:indexes\`). If the JSON format is invalid, this method throws an exception.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html json` | The JSON format exported by the Firebase CLI. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | A task that resolves once all indices are successfully configured. |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html java.lang.IllegalArgumentException` | if the JSON format is invalid |

### setLoggingEnabled

```
public static void setLoggingEnabled(boolean loggingEnabled)
```

Globally enables / disables Cloud Firestore logging for the SDK.

### terminate

```
public @NonNull Task<Void> terminate()
```

Terminates this `FirebaseFirestore` instance.

After calling `terminate()` only the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#clearPersistence()` method may be used. Any other method will throw an `https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html`.

To restart after termination, simply create a new instance of `FirebaseFirestore` with `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#getInstance()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#getInstance(com.google.firebase.FirebaseApp)`.

`terminate()` does not cancel any pending writes and any tasks that are awaiting a response from the server will not be resolved. The next time you start this instance, it will resume attempting to send these writes to the server.

Note: Under normal circumstances, calling `terminate()` is not required. This method is useful only when you want to force this instance to release all of its resources or in combination with clearPersistence to ensure that all local state is destroyed between test runs.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | A `Task` that is resolved when the instance has been successfully terminated. |

### useEmulator

```
public void useEmulator(@NonNull String host, int port)
```

Modifies this FirebaseDatabase instance to communicate with the Cloud Firestore emulator.

Note: Call this method before using the instance to do any database operations.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html host` | the emulator host (for example, 10.0.2.2) |
| `int port` | the emulator port (for example, 8080) |

### waitForPendingWrites

```
public @NonNull Task<Void> waitForPendingWrites()
```

Waits until all currently pending writes for the active user have been acknowledged by the backend.

The returned Task completes immediately if there are no outstanding writes. Otherwise, the Task waits for all previously issued writes (including those written in a previous app session), but it does not wait for writes that were added after the method is called. If you wish to wait for additional writes, you have to call `waitForPendingWrites()` again.

Any outstanding `waitForPendingWrites()` Tasks are cancelled during user changes.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | A `Task` which resolves when all currently pending writes have been acknowledged by the backend. |