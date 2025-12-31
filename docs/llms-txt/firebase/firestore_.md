# Source: https://firebase.google.com/docs/reference/js/firestore_.md.txt

# @firebase/firestore

## Functions

|                                                                                       Function                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **function(app, ...)**                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [getFirestore(app)](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore_cf608e1)                                                                                | Returns the existing default [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance that is associated with the provided [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface). If no instance exists, initializes a new instance with default settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [getFirestore(app, databaseId)](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore_48de6cb)                                                                    | ***(Public Preview)*** Returns the existing named [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance that is associated with the provided [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface). If no instance exists, initializes a new instance with default settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [initializeFirestore(app, settings, databaseId)](https://firebase.google.com/docs/reference/js/firestore_.md#initializefirestore_fc7d200)                                            | Initializes a new instance of [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) with the provided settings. Can only be called before any other function, including [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore). If the custom settings are empty, this function is equivalent to calling [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **function(db, ...)**                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [documentSnapshotFromJSON(db, json)](https://firebase.google.com/docs/reference/js/firestore_.md#documentsnapshotfromjson_a318ff2)                                                   | Builds a `DocumentSnapshot` instance from a JSON object created by [DocumentSnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshottojson).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [documentSnapshotFromJSON(db, json, converter)](https://firebase.google.com/docs/reference/js/firestore_.md#documentsnapshotfromjson_ddb369d)                                        | Builds a `DocumentSnapshot` instance from a JSON object created by [DocumentSnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshottojson).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [querySnapshotFromJSON(db, json)](https://firebase.google.com/docs/reference/js/firestore_.md#querysnapshotfromjson_a318ff2)                                                         | Builds a `QuerySnapshot` instance from a JSON object created by [QuerySnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshottojson).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [querySnapshotFromJSON(db, json, converter)](https://firebase.google.com/docs/reference/js/firestore_.md#querysnapshotfromjson_ddb369d)                                              | Builds a `QuerySnapshot` instance from a JSON object created by [QuerySnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshottojson).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **function(firestore, ...)**                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [clearIndexedDbPersistence(firestore)](https://firebase.google.com/docs/reference/js/firestore_.md#clearindexeddbpersistence_231a8e0)                                                | Clears the persistent storage. This includes pending writes and cached documents.Must be called while the [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance is not started (after the app is terminated or when the app is first initialized). On startup, this function must be called before other functions (other than [initializeFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#initializefirestore_fc7d200) or [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore))). If the [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance is still running, the promise will be rejected with the error code of `failed-precondition`.Note: `clearIndexedDbPersistence()` is primarily intended to help write reliable tests that use Cloud Firestore. It uses an efficient mechanism for dropping existing data but does not attempt to securely overwrite or otherwise make cached data unrecoverable. For applications that are sensitive to the disclosure of cached data in between user sessions, we strongly recommend not enabling persistence at all. |
| [collection(firestore, path, pathSegments)](https://firebase.google.com/docs/reference/js/firestore_.md#collection_1eb4c23)                                                          | Gets a `CollectionReference` instance that refers to the collection at the specified absolute path.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [collectionGroup(firestore, collectionId)](https://firebase.google.com/docs/reference/js/firestore_.md#collectiongroup_1838fc3)                                                      | Creates and returns a new `Query` instance that includes all documents in the database that are contained in a collection or subcollection with the given `collectionId`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [connectFirestoreEmulator(firestore, host, port, options)](https://firebase.google.com/docs/reference/js/firestore_.md#connectfirestoreemulator_7c247cd)                             | Modify this instance to communicate with the Cloud Firestore emulator.Note: This must be called before this instance has been used to do any operations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [disableNetwork(firestore)](https://firebase.google.com/docs/reference/js/firestore_.md#disablenetwork_231a8e0)                                                                      | Disables network usage for this instance. It can be re-enabled via [enableNetwork()](https://firebase.google.com/docs/reference/js/firestore_.md#enablenetwork_231a8e0). While the network is disabled, any snapshot listeners, `getDoc()` or `getDocs()` calls will return results from cache, and any write operations will be queued until the network is restored.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [doc(firestore, path, pathSegments)](https://firebase.google.com/docs/reference/js/firestore_.md#doc_1eb4c23)                                                                        | Gets a `DocumentReference` instance that refers to the document at the specified absolute path.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [enableIndexedDbPersistence(firestore, persistenceSettings)](https://firebase.google.com/docs/reference/js/firestore_.md#enableindexeddbpersistence_224174f)                         | Attempts to enable persistent storage, if possible.On failure, `enableIndexedDbPersistence()` will reject the promise or throw an exception. There are several reasons why this can fail, which can be identified by the `code` on the error.\* failed-precondition: The app is already open in another browser tab. \* unimplemented: The browser is incompatible with the offline persistence implementation.Note that even after a failure, the [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance will remain usable, however offline persistence will be disabled.Note: `enableIndexedDbPersistence()` must be called before any other functions (other than [initializeFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#initializefirestore_fc7d200), [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore) or [clearIndexedDbPersistence()](https://firebase.google.com/docs/reference/js/firestore_.md#clearindexeddbpersistence_231a8e0).Persistence cannot be used in a Node.js environment.                                                                                                                   |
| [enableMultiTabIndexedDbPersistence(firestore)](https://firebase.google.com/docs/reference/js/firestore_.md#enablemultitabindexeddbpersistence_231a8e0)                              | Attempts to enable multi-tab persistent storage, if possible. If enabled across all tabs, all operations share access to local persistence, including shared execution of queries and latency-compensated local document updates across all connected instances.On failure, `enableMultiTabIndexedDbPersistence()` will reject the promise or throw an exception. There are several reasons why this can fail, which can be identified by the `code` on the error.\* failed-precondition: The app is already open in another browser tab and multi-tab is not enabled. \* unimplemented: The browser is incompatible with the offline persistence implementation.Note that even after a failure, the [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance will remain usable, however offline persistence will be disabled.                                                                                                                                                                                                                                                                                                                                                             |
| [enableNetwork(firestore)](https://firebase.google.com/docs/reference/js/firestore_.md#enablenetwork_231a8e0)                                                                        | Re-enables use of the network for this [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance after a prior call to [disableNetwork()](https://firebase.google.com/docs/reference/js/firestore_.md#disablenetwork_231a8e0).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [getPersistentCacheIndexManager(firestore)](https://firebase.google.com/docs/reference/js/firestore_.md#getpersistentcacheindexmanager_231a8e0)                                      | Returns the PersistentCache Index Manager used by the given `Firestore` object. The `PersistentCacheIndexManager` instance, or `null` if local persistent storage is not in use.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [loadBundle(firestore, bundleData)](https://firebase.google.com/docs/reference/js/firestore_.md#loadbundle_bec5b75)                                                                  | Loads a Firestore bundle into the local cache.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [namedQuery(firestore, name)](https://firebase.google.com/docs/reference/js/firestore_.md#namedquery_6438876)                                                                        | Reads a Firestore [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class) from local cache, identified by the given name.The named queries are packaged into bundles on the server side (along with resulting documents), and loaded to local cache using `loadBundle`. Once in local cache, use this method to extract a [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class) by name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [onSnapshotResume(firestore, snapshotJson, onNext, onError, onCompletion, converter)](https://firebase.google.com/docs/reference/js/firestore_.md#onsnapshotresume_7c84f5e)          | Attaches a listener for `QuerySnapshot` events based on data generated by invoking [QuerySnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshottojson) You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks. The listener can be cancelled by calling the function that is returned when `onSnapshot` is called.NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [onSnapshotResume(firestore, snapshotJson, onNext, onError, onCompletion, converter)](https://firebase.google.com/docs/reference/js/firestore_.md#onsnapshotresume_712362a)          | Attaches a listener for `DocumentSnapshot` events based on data generated by invoking [DocumentSnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshottojson). You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks. The listener can be cancelled by calling the function that is returned when `onSnapshot` is called.NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [onSnapshotResume(firestore, snapshotJson, options, onNext, onError, onCompletion, converter)](https://firebase.google.com/docs/reference/js/firestore_.md#onsnapshotresume_8807e6e) | Attaches a listener for `QuerySnapshot` events based on data generated by invoking [QuerySnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshottojson). You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks. The listener can be cancelled by calling the function that is returned when `onSnapshot` is called.NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [onSnapshotResume(firestore, snapshotJson, options, onNext, onError, onCompletion, converter)](https://firebase.google.com/docs/reference/js/firestore_.md#onsnapshotresume_301fcec) | Attaches a listener for `DocumentSnapshot` events based on data generated by invoking [DocumentSnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshottojson). You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks. The listener can be cancelled by calling the function that is returned when `onSnapshot` is called.NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [onSnapshotResume(firestore, snapshotJson, observer, converter)](https://firebase.google.com/docs/reference/js/firestore_.md#onsnapshotresume_b8b5c9d)                               | Attaches a listener for `QuerySnapshot` events based on QuerySnapshot data generated by invoking [QuerySnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshottojson). You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks. The listener can be cancelled by calling the function that is returned when `onSnapshot` is called.NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [onSnapshotResume(firestore, snapshotJson, observer, converter)](https://firebase.google.com/docs/reference/js/firestore_.md#onsnapshotresume_9b75d28)                               | Attaches a listener for `DocumentSnapshot` events based on data generated by invoking [DocumentSnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshottojson) You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks. The listener can be cancelled by calling the function that is returned when `onSnapshot` is called.NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [onSnapshotResume(firestore, snapshotJson, options, observer, converter)](https://firebase.google.com/docs/reference/js/firestore_.md#onsnapshotresume_fb80adf)                      | Attaches a listener for `QuerySnapshot` events based on QuerySnapshot data generated by invoking [QuerySnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshottojson) You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks. The listener can be cancelled by calling the function that is returned when `onSnapshot` is called.NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [onSnapshotResume(firestore, snapshotJson, options, observer, converter)](https://firebase.google.com/docs/reference/js/firestore_.md#onsnapshotresume_f76d912)                      | Attaches a listener for `DocumentSnapshot` events based on QuerySnapshot data generated by invoking [DocumentSnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshottojson) You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks. The listener can be cancelled by calling the function that is returned when `onSnapshot` is called.NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [onSnapshotsInSync(firestore, observer)](https://firebase.google.com/docs/reference/js/firestore_.md#onsnapshotsinsync_2f0dfa4)                                                      | Attaches a listener for a snapshots-in-sync event. The snapshots-in-sync event indicates that all listeners affected by a given change have fired, even if a single server-generated change affects multiple listeners.NOTE: The snapshots-in-sync event only indicates that listeners are in sync with each other, but does not relate to whether those snapshots are in sync with the server. Use SnapshotMetadata in the individual listeners to determine if a snapshot is from the cache or the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [onSnapshotsInSync(firestore, onSync)](https://firebase.google.com/docs/reference/js/firestore_.md#onsnapshotsinsync_1901c06)                                                        | Attaches a listener for a snapshots-in-sync event. The snapshots-in-sync event indicates that all listeners affected by a given change have fired, even if a single server-generated change affects multiple listeners.NOTE: The snapshots-in-sync event only indicates that listeners are in sync with each other, but does not relate to whether those snapshots are in sync with the server. Use `SnapshotMetadata` in the individual listeners to determine if a snapshot is from the cache or the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [runTransaction(firestore, updateFunction, options)](https://firebase.google.com/docs/reference/js/firestore_.md#runtransaction_6f03ec4)                                             | Executes the given `updateFunction` and then attempts to commit the changes applied within the transaction. If any document read within the transaction has changed, Cloud Firestore retries the `updateFunction`. If it fails to commit after 5 attempts, the transaction fails.The maximum number of writes allowed in a single transaction is 500.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [setIndexConfiguration(firestore, configuration)](https://firebase.google.com/docs/reference/js/firestore_.md#setindexconfiguration_c362f04)                                         | ***(Public Preview)*** Configures indexing for local query execution. Any previous index configuration is overridden. The `Promise` resolves once the index configuration has been persisted.The index entries themselves are created asynchronously. You can continue to use queries that require indexing even if the indices are not yet available. Query execution will automatically start using the index once the index entries have been written.Indexes are only supported with IndexedDb persistence. If IndexedDb is not enabled, any index configuration is ignored.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [setIndexConfiguration(firestore, json)](https://firebase.google.com/docs/reference/js/firestore_.md#setindexconfiguration_90d0285)                                                  | ***(Public Preview)*** Configures indexing for local query execution. Any previous index configuration is overridden. The `Promise` resolves once the index configuration has been persisted.The index entries themselves are created asynchronously. You can continue to use queries that require indexing even if the indices are not yet available. Query execution will automatically start using the index once the index entries have been written.Indexes are only supported with IndexedDb persistence. Invoke either `enableIndexedDbPersistence()` or `enableMultiTabIndexedDbPersistence()` before setting an index configuration. If IndexedDb is not enabled, any index configuration is ignored.The method accepts the JSON format exported by the Firebase CLI (`firebase firestore:indexes`). If the JSON format is invalid, this method throws an error.                                                                                                                                                                                                                                                                                                                                                                      |
| [terminate(firestore)](https://firebase.google.com/docs/reference/js/firestore_.md#terminate_231a8e0)                                                                                | Terminates the provided [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance.After calling `terminate()` only the `clearIndexedDbPersistence()` function may be used. Any other function will throw a `FirestoreError`.To restart after termination, create a new instance of FirebaseFirestore with [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore).Termination does not cancel any pending writes, and any promises that are awaiting a response from the server will not be resolved. If you have persistence enabled, the next time you start this instance, it will resume sending these writes to the server.Note: Under normal circumstances, calling `terminate()` is not required. This function is useful only when you want to force this instance to release all of its resources or in combination with `clearIndexedDbPersistence()` to ensure that all local state is destroyed between test runs.                                                                                                                                                                                                                            |
| [waitForPendingWrites(firestore)](https://firebase.google.com/docs/reference/js/firestore_.md#waitforpendingwrites_231a8e0)                                                          | Waits until all currently pending writes for the active user have been acknowledged by the backend.The returned promise resolves immediately if there are no outstanding writes. Otherwise, the promise waits for all previously issued writes (including those written in a previous app session), but it does not wait for writes that were added after the function is called. If you want to wait for additional writes, call `waitForPendingWrites()` again.Any outstanding `waitForPendingWrites()` promises are rejected during user changes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [writeBatch(firestore)](https://firebase.google.com/docs/reference/js/firestore_.md#writebatch_231a8e0)                                                                              | Creates a write batch, used for performing multiple writes as a single atomic operation. The maximum number of writes allowed in a single [WriteBatch](https://firebase.google.com/docs/reference/js/firestore_.writebatch.md#writebatch_class) is 500.Unlike transactions, write batches are persisted offline and therefore are preferable when you don't need to condition your writes on read data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **function()**                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [count()](https://firebase.google.com/docs/reference/js/firestore_.md#count)                                                                                                         | Create an AggregateField object that can be used to compute the count of documents in the result set of a query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [deleteField()](https://firebase.google.com/docs/reference/js/firestore_.md#deletefield)                                                                                             | Returns a sentinel for use with [updateDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#updatedoc_51a65e3) or [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad) with `{merge: true}` to mark a field for deletion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [documentId()](https://firebase.google.com/docs/reference/js/firestore_.md#documentid)                                                                                               | Returns a special sentinel `FieldPath` to refer to the ID of a document. It can be used in queries to sort or filter by the document ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore)                                                                                           | Returns the existing default [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance that is associated with the default [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface). If no instance exists, initializes a new instance with default settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [memoryEagerGarbageCollector()](https://firebase.google.com/docs/reference/js/firestore_.md#memoryeagergarbagecollector)                                                             | Creates an instance of `MemoryEagerGarbageCollector`. This is also the default garbage collector unless it is explicitly specified otherwise.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [persistentMultipleTabManager()](https://firebase.google.com/docs/reference/js/firestore_.md#persistentmultipletabmanager)                                                           | Creates an instance of `PersistentMultipleTabManager`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [serverTimestamp()](https://firebase.google.com/docs/reference/js/firestore_.md#servertimestamp)                                                                                     | Returns a sentinel used with [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad) or [updateDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#updatedoc_51a65e3) to include a server-generated timestamp in the written data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **function(databaseId, ...)**                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [getFirestore(databaseId)](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore_53dc891)                                                                         | ***(Public Preview)*** Returns the existing named [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance that is associated with the default [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface). If no instance exists, initializes a new instance with default settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **function(elements, ...)**                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [arrayRemove(elements)](https://firebase.google.com/docs/reference/js/firestore_.md#arrayremove_7d853aa)                                                                             | Returns a special value that can be used with [setDoc()](https://firebase.google.com/docs/reference/js/firestore_.md#setdoc_ee215ad) or that tells the server to remove the given elements from any array value that already exists on the server. All instances of each element specified will be removed from the array. If the field being modified is not already an array it will be overwritten with an empty array.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [arrayUnion(elements)](https://firebase.google.com/docs/reference/js/firestore_.md#arrayunion_7d853aa)                                                                               | Returns a special value that can be used with [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad) or [updateDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#updatedoc_51a65e3) that tells the server to union the given elements with any array value that already exists on the server. Each specified element that doesn't already exist in the array will be added to the end. If the field being modified is not already an array it will be overwritten with an array containing exactly the specified elements.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **function(field, ...)**                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [average(field)](https://firebase.google.com/docs/reference/js/firestore_.md#average_aacc3a9)                                                                                        | Create an AggregateField object that can be used to compute the average of a specified field over a range of documents in the result set of a query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [sum(field)](https://firebase.google.com/docs/reference/js/firestore_.md#sum_aacc3a9)                                                                                                | Create an AggregateField object that can be used to compute the sum of a specified field over a range of documents in the result set of a query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **function(fieldPath, ...)**                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [orderBy(fieldPath, directionStr)](https://firebase.google.com/docs/reference/js/firestore_.md#orderby_006d61f)                                                                      | Creates a [QueryOrderByConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryorderbyconstraint.md#queryorderbyconstraint_class) that sorts the query result by the specified field, optionally in descending order instead of ascending.Note: Documents that do not contain the specified field will not be present in the query result.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [where(fieldPath, opStr, value)](https://firebase.google.com/docs/reference/js/firestore_.md#where_0fae4bf)                                                                          | Creates a [QueryFieldFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryfieldfilterconstraint.md#queryfieldfilterconstraint_class) that enforces that documents must contain the specified field and that the value should satisfy the relation constraint provided.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **function(fieldValues, ...)**                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [endAt(fieldValues)](https://firebase.google.com/docs/reference/js/firestore_.md#endat_8b2f2c8)                                                                                      | Creates a [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class) that modifies the result set to end at the provided fields relative to the order of the query. The order of the field values must match the order of the order by clauses of the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [endBefore(fieldValues)](https://firebase.google.com/docs/reference/js/firestore_.md#endbefore_8b2f2c8)                                                                              | Creates a [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class) that modifies the result set to end before the provided fields relative to the order of the query. The order of the field values must match the order of the order by clauses of the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [startAfter(fieldValues)](https://firebase.google.com/docs/reference/js/firestore_.md#startafter_8b2f2c8)                                                                            | Creates a [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class) that modifies the result set to start after the provided fields relative to the order of the query. The order of the field values must match the order of the order by clauses of the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [startAt(fieldValues)](https://firebase.google.com/docs/reference/js/firestore_.md#startat_8b2f2c8)                                                                                  | Creates a [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class) that modifies the result set to start at the provided fields relative to the order of the query. The order of the field values must match the order of the order by clauses of the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **function(indexManager, ...)**                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [deleteAllPersistentCacheIndexes(indexManager)](https://firebase.google.com/docs/reference/js/firestore_.md#deleteallpersistentcacheindexes_98b2645)                                 | Removes all persistent cache indexes.Please note this function will also deletes indexes generated by `setIndexConfiguration()`, which is deprecated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [disablePersistentCacheIndexAutoCreation(indexManager)](https://firebase.google.com/docs/reference/js/firestore_.md#disablepersistentcacheindexautocreation_98b2645)                 | Stops creating persistent cache indexes automatically for local query execution. The indexes which have been created by calling `enablePersistentCacheIndexAutoCreation()` still take effect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [enablePersistentCacheIndexAutoCreation(indexManager)](https://firebase.google.com/docs/reference/js/firestore_.md#enablepersistentcacheindexautocreation_98b2645)                   | Enables the SDK to create persistent cache indexes automatically for local query execution when the SDK believes cache indexes can help improve performance.This feature is disabled by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **function(left, ...)**                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [aggregateFieldEqual(left, right)](https://firebase.google.com/docs/reference/js/firestore_.md#aggregatefieldequal_e80a2b2)                                                          | Compares two 'AggregateField\` instances for equality.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [aggregateQuerySnapshotEqual(left, right)](https://firebase.google.com/docs/reference/js/firestore_.md#aggregatequerysnapshotequal_1529a20)                                          | Compares two `AggregateQuerySnapshot` instances for equality.Two `AggregateQuerySnapshot` instances are considered "equal" if they have underlying queries that compare equal, and the same data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [queryEqual(left, right)](https://firebase.google.com/docs/reference/js/firestore_.md#queryequal_7a1f045)                                                                            | Returns true if the provided queries point to the same collection and apply the same constraints.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [refEqual(left, right)](https://firebase.google.com/docs/reference/js/firestore_.md#refequal_598b780)                                                                                | Returns true if the provided references are equal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [snapshotEqual(left, right)](https://firebase.google.com/docs/reference/js/firestore_.md#snapshotequal_5109204)                                                                      | Returns true if the provided snapshots are equal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **function(limit, ...)**                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [limit(limit)](https://firebase.google.com/docs/reference/js/firestore_.md#limit_ec46c78)                                                                                            | Creates a [QueryLimitConstraint](https://firebase.google.com/docs/reference/js/firestore_.querylimitconstraint.md#querylimitconstraint_class) that only returns the first matching documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [limitToLast(limit)](https://firebase.google.com/docs/reference/js/firestore_.md#limittolast_ec46c78)                                                                                | Creates a [QueryLimitConstraint](https://firebase.google.com/docs/reference/js/firestore_.querylimitconstraint.md#querylimitconstraint_class) that only returns the last matching documents.You must specify at least one `orderBy` clause for `limitToLast` queries, otherwise an exception will be thrown during execution.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **function(logLevel, ...)**                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [setLogLevel(logLevel)](https://firebase.google.com/docs/reference/js/firestore_.md#setloglevel_d02fda2)                                                                             | Sets the verbosity of Cloud Firestore logs (debug, error, or silent).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **function(n, ...)**                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [increment(n)](https://firebase.google.com/docs/reference/js/firestore_.md#increment_5685735)                                                                                        | Returns a special value that can be used with [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad) or [updateDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#updatedoc_51a65e3) that tells the server to increment the field's current value by the given value.If either the operand or the current field value uses floating point precision, all arithmetic follows IEEE 754 semantics. If both values are integers, values outside of JavaScript's safe number range (`Number.MIN_SAFE_INTEGER` to `Number.MAX_SAFE_INTEGER`) are also subject to precision loss. Furthermore, once processed by the Firestore backend, all integer operations are capped between -2\^63 and 2\^63-1.If the current field value is not of type `number`, or if the field does not yet exist, the transformation sets the field to the given value.                                                                                                                                                                                                                                                                                                                                            |
| **function(query, ...)**                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [getAggregateFromServer(query, aggregateSpec)](https://firebase.google.com/docs/reference/js/firestore_.md#getaggregatefromserver_2073a74)                                           | Calculates the specified aggregations over the documents in the result set of the given query without actually downloading the documents.Using this function to perform aggregations is efficient because only the final aggregation values, not the documents' data, are downloaded. This function can perform aggregations of the documents in cases where the result set is prohibitively large to download entirely (thousands of documents).The result received from the server is presented, unaltered, without considering any local state. That is, documents in the local cache are not taken into consideration, neither are local modifications not yet synchronized with the server. Previously-downloaded results, if any, are not used. Every invocation of this function necessarily involves a round trip to the server.                                                                                                                                                                                                                                                                                                                                                                                                       |
| [getCountFromServer(query)](https://firebase.google.com/docs/reference/js/firestore_.md#getcountfromserver_4e56953)                                                                  | Calculates the number of documents in the result set of the given query without actually downloading the documents.Using this function to count the documents is efficient because only the final count, not the documents' data, is downloaded. This function can count the documents in cases where the result set is prohibitively large to download entirely (thousands of documents).The result received from the server is presented, unaltered, without considering any local state. That is, documents in the local cache are not taken into consideration, neither are local modifications not yet synchronized with the server. Previously-downloaded results, if any, are not used. Every invocation of this function necessarily involves a round trip to the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [getDocs(query)](https://firebase.google.com/docs/reference/js/firestore_.md#getdocs_4e56953)                                                                                        | Executes the query and returns the results as a `QuerySnapshot`.Note: `getDocs()` attempts to provide up-to-date data when possible by waiting for data from the server, but it may return cached data or fail if you are offline and the server cannot be reached. To specify this behavior, invoke [getDocsFromCache()](https://firebase.google.com/docs/reference/js/firestore_.md#getdocsfromcache_4e56953) or [getDocsFromServer()](https://firebase.google.com/docs/reference/js/firestore_.md#getdocsfromserver_4e56953).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [getDocsFromCache(query)](https://firebase.google.com/docs/reference/js/firestore_.md#getdocsfromcache_4e56953)                                                                      | Executes the query and returns the results as a `QuerySnapshot` from cache. Returns an empty result set if no documents matching the query are currently cached.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [getDocsFromServer(query)](https://firebase.google.com/docs/reference/js/firestore_.md#getdocsfromserver_4e56953)                                                                    | Executes the query and returns the results as a `QuerySnapshot` from the server. Returns an error if the network is not available.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [onSnapshot(query, observer)](https://firebase.google.com/docs/reference/js/firestore_.md#onsnapshot_8d14049)                                                                        | Attaches a listener for `QuerySnapshot` events. You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks. The listener can be cancelled by calling the function that is returned when `onSnapshot` is called.NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [onSnapshot(query, options, observer)](https://firebase.google.com/docs/reference/js/firestore_.md#onsnapshot_03dfff5)                                                               | Attaches a listener for `QuerySnapshot` events. You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks. The listener can be cancelled by calling the function that is returned when `onSnapshot` is called.NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [onSnapshot(query, onNext, onError, onCompletion)](https://firebase.google.com/docs/reference/js/firestore_.md#onsnapshot_3ebfbe2)                                                   | Attaches a listener for `QuerySnapshot` events. You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks. The listener can be cancelled by calling the function that is returned when `onSnapshot` is called.NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [onSnapshot(query, options, onNext, onError, onCompletion)](https://firebase.google.com/docs/reference/js/firestore_.md#onsnapshot_b8f9c47)                                          | Attaches a listener for `QuerySnapshot` events. You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks. The listener can be cancelled by calling the function that is returned when `onSnapshot` is called.NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [query(query, compositeFilter, queryConstraints)](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4)                                                         | Creates a new immutable instance of [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class) that is extended to also include additional query constraints.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [query(query, queryConstraints)](https://firebase.google.com/docs/reference/js/firestore_.md#query_0f46da1)                                                                          | Creates a new immutable instance of [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class) that is extended to also include additional query constraints.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **function(queryConstraints, ...)**                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [and(queryConstraints)](https://firebase.google.com/docs/reference/js/firestore_.md#and_e72c712)                                                                                     | Creates a new [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class) that is a conjunction of the given filter constraints. A conjunction filter includes a document if it satisfies all of the given filters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [or(queryConstraints)](https://firebase.google.com/docs/reference/js/firestore_.md#or_e72c712)                                                                                       | Creates a new [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class) that is a disjunction of the given filter constraints. A disjunction filter includes a document if it satisfies any of the given filters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **function(reference, ...)**                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [addDoc(reference, data)](https://firebase.google.com/docs/reference/js/firestore_.md#adddoc_6e783ff)                                                                                | Add a new document to specified `CollectionReference` with the given data, assigning it a document ID automatically.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [collection(reference, path, pathSegments)](https://firebase.google.com/docs/reference/js/firestore_.md#collection_568f98d)                                                          | Gets a `CollectionReference` instance that refers to a subcollection of `reference` at the specified relative path.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [collection(reference, path, pathSegments)](https://firebase.google.com/docs/reference/js/firestore_.md#collection_70b4396)                                                          | Gets a `CollectionReference` instance that refers to a subcollection of `reference` at the specified relative path.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [deleteDoc(reference)](https://firebase.google.com/docs/reference/js/firestore_.md#deletedoc_4569087)                                                                                | Deletes the document referred to by the specified `DocumentReference`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [doc(reference, path, pathSegments)](https://firebase.google.com/docs/reference/js/firestore_.md#doc_568f98d)                                                                        | Gets a `DocumentReference` instance that refers to a document within `reference` at the specified relative path. If no path is specified, an automatically-generated unique ID will be used for the returned `DocumentReference`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [doc(reference, path, pathSegments)](https://firebase.google.com/docs/reference/js/firestore_.md#doc_70b4396)                                                                        | Gets a `DocumentReference` instance that refers to a document within `reference` at the specified relative path.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [getDoc(reference)](https://firebase.google.com/docs/reference/js/firestore_.md#getdoc_4569087)                                                                                      | Reads the document referred to by this `DocumentReference`.Note: `getDoc()` attempts to provide up-to-date data when possible by waiting for data from the server, but it may return cached data or fail if you are offline and the server cannot be reached. To specify this behavior, invoke [getDocFromCache()](https://firebase.google.com/docs/reference/js/firestore_.md#getdocfromcache_4569087) or [getDocFromServer()](https://firebase.google.com/docs/reference/js/firestore_.md#getdocfromserver_4569087).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [getDocFromCache(reference)](https://firebase.google.com/docs/reference/js/firestore_.md#getdocfromcache_4569087)                                                                    | Reads the document referred to by this `DocumentReference` from cache. Returns an error if the document is not currently cached.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [getDocFromServer(reference)](https://firebase.google.com/docs/reference/js/firestore_.md#getdocfromserver_4569087)                                                                  | Reads the document referred to by this `DocumentReference` from the server. Returns an error if the network is not available.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [onSnapshot(reference, observer)](https://firebase.google.com/docs/reference/js/firestore_.md#onsnapshot_0312fd7)                                                                    | Attaches a listener for `DocumentSnapshot` events. You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks.NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [onSnapshot(reference, options, observer)](https://firebase.google.com/docs/reference/js/firestore_.md#onsnapshot_86b6b9e)                                                           | Attaches a listener for `DocumentSnapshot` events. You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks.NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [onSnapshot(reference, onNext, onError, onCompletion)](https://firebase.google.com/docs/reference/js/firestore_.md#onsnapshot_905f42c)                                               | Attaches a listener for `DocumentSnapshot` events. You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks.NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [onSnapshot(reference, options, onNext, onError, onCompletion)](https://firebase.google.com/docs/reference/js/firestore_.md#onsnapshot_0c39991)                                      | Attaches a listener for `DocumentSnapshot` events. You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks.NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [setDoc(reference, data)](https://firebase.google.com/docs/reference/js/firestore_.md#setdoc_ee215ad)                                                                                | Writes to the document referred to by this `DocumentReference`. If the document does not yet exist, it will be created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [setDoc(reference, data, options)](https://firebase.google.com/docs/reference/js/firestore_.md#setdoc_ff80739)                                                                       | Writes to the document referred to by the specified `DocumentReference`. If the document does not yet exist, it will be created. If you provide `merge` or `mergeFields`, the provided data can be merged into an existing document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [updateDoc(reference, data)](https://firebase.google.com/docs/reference/js/firestore_.md#updatedoc_51a65e3)                                                                          | Updates fields in the document referred to by the specified `DocumentReference`. The update will fail if applied to a document that does not exist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [updateDoc(reference, field, value, moreFieldsAndValues)](https://firebase.google.com/docs/reference/js/firestore_.md#updatedoc_7c28659)                                             | Updates fields in the document referred to by the specified `DocumentReference` The update will fail if applied to a document that does not exist.Nested fields can be updated by providing dot-separated field path strings or by providing `FieldPath` objects.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **function(settings, ...)**                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [memoryLocalCache(settings)](https://firebase.google.com/docs/reference/js/firestore_.md#memorylocalcache_05f4bf2)                                                                   | Creates an instance of `MemoryLocalCache`. The instance can be set to `FirestoreSettings.cache` to tell the SDK which cache layer to use.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [memoryLruGarbageCollector(settings)](https://firebase.google.com/docs/reference/js/firestore_.md#memorylrugarbagecollector_5ee014c)                                                 | Creates an instance of `MemoryLruGarbageCollector`.A target size can be specified as part of the setting parameter. The collector will start deleting documents once the cache size exceeds the given size. The default cache size is 40MB (40 \* 1024 \* 1024 bytes).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [persistentLocalCache(settings)](https://firebase.google.com/docs/reference/js/firestore_.md#persistentlocalcache_d312f71)                                                           | Creates an instance of `PersistentLocalCache`. The instance can be set to `FirestoreSettings.cache` to tell the SDK which cache layer to use.Persistent cache cannot be used in a Node.js environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [persistentSingleTabManager(settings)](https://firebase.google.com/docs/reference/js/firestore_.md#persistentsingletabmanager_c99c68d)                                               | Creates an instance of `PersistentSingleTabManager`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **function(snapshot, ...)**                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [endAt(snapshot)](https://firebase.google.com/docs/reference/js/firestore_.md#endat_9a4477f)                                                                                         | Creates a [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class) that modifies the result set to end at the provided document (inclusive). The end position is relative to the order of the query. The document must contain all of the fields provided in the orderBy of the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [endBefore(snapshot)](https://firebase.google.com/docs/reference/js/firestore_.md#endbefore_9a4477f)                                                                                 | Creates a [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class) that modifies the result set to end before the provided document (exclusive). The end position is relative to the order of the query. The document must contain all of the fields provided in the orderBy of the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [startAfter(snapshot)](https://firebase.google.com/docs/reference/js/firestore_.md#startafter_9a4477f)                                                                               | Creates a [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class) that modifies the result set to start after the provided document (exclusive). The starting position is relative to the order of the query. The document must contain all of the fields provided in the orderBy of the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [startAt(snapshot)](https://firebase.google.com/docs/reference/js/firestore_.md#startat_9a4477f)                                                                                     | Creates a [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class) that modifies the result set to start at the provided document (inclusive). The starting position is relative to the order of the query. The document must contain all of the fields provided in the `orderBy` of this query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **function(values, ...)**                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [vector(values)](https://firebase.google.com/docs/reference/js/firestore_.md#vector_0dbdaf2)                                                                                         | Creates a new `VectorValue` constructed with a copy of the given array of numbers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## Classes

|                                                                               Class                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AggregateField](https://firebase.google.com/docs/reference/js/firestore_.aggregatefield.md#aggregatefield_class)                                                 | Represents an aggregation that can be performed by Firestore.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [AggregateQuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.aggregatequerysnapshot.md#aggregatequerysnapshot_class)                         | The results of executing an aggregation query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class)                                                                            | An immutable object representing an array of bytes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [CollectionReference](https://firebase.google.com/docs/reference/js/firestore_.collectionreference.md#collectionreference_class)                                  | A `CollectionReference` object can be used for adding documents, getting document references, and querying for documents (using [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4)).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class)                                        | A `DocumentReference` refers to a document location in a Firestore database and can be used to write, read, or listen to the location. The document at the referenced location may or may not exist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshot_class)                                           | A `DocumentSnapshot` contains data read from a document in your Firestore database. The data can be extracted with `.data()` or `.get(<field>)` to get a specific field.For a `DocumentSnapshot` that points to a non-existing document, any data access will return 'undefined'. You can use the `exists()` method to explicitly verify a document's existence.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [FieldPath](https://firebase.google.com/docs/reference/js/firestore_.fieldpath.md#fieldpath_class)                                                                | A `FieldPath` refers to a field in a document. The path may consist of a single field name (referring to a top-level field in the document), or a list of field names (referring to a nested field in the document).Create a `FieldPath` by providing field names. If more than one field name is provided, the path will point to a nested field in a document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [FieldValue](https://firebase.google.com/docs/reference/js/firestore_.fieldvalue.md#fieldvalue_class)                                                             | Sentinel values that can be used when writing document fields with `set()` or `update()`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class)                                                                | The Cloud Firestore service interface.Do not call this constructor directly. Instead, use [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class)                                                 | An error returned by a Firestore operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [GeoPoint](https://firebase.google.com/docs/reference/js/firestore_.geopoint.md#geopoint_class)                                                                   | An immutable object representing a geographic location in Firestore. The location is represented as latitude/longitude pair.Latitude values are in the range of \[-90, 90\]. Longitude values are in the range of \[-180, 180\].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [LoadBundleTask](https://firebase.google.com/docs/reference/js/firestore_.loadbundletask.md#loadbundletask_class)                                                 | Represents the task of loading a Firestore bundle. It provides progress of bundle loading, as well as task completion and error events.The API is compatible with `Promise<LoadBundleTaskProgress>`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [PersistentCacheIndexManager](https://firebase.google.com/docs/reference/js/firestore_.persistentcacheindexmanager.md#persistentcacheindexmanager_class)          | A `PersistentCacheIndexManager` for configuring persistent cache indexes used for local query execution.To use, call `getPersistentCacheIndexManager()` to get an instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class)                                                                            | A `Query` refers to a query which you can read or listen to. You can also construct refined `Query` objects by adding filters and ordering.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class) | A `QueryCompositeFilterConstraint` is used to narrow the set of documents returned by a Firestore query by performing the logical OR or AND of multiple [QueryFieldFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryfieldfilterconstraint.md#queryfieldfilterconstraint_class)s or [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class)s. `QueryCompositeFilterConstraint`s are created by invoking [or()](https://firebase.google.com/docs/reference/js/firestore_.md#or_e72c712) or [and()](https://firebase.google.com/docs/reference/js/firestore_.md#and_e72c712) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains the `QueryCompositeFilterConstraint`.                                                                                                                                                          |
| [QueryConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryconstraint.md#queryconstraint_class)                                              | A `QueryConstraint` is used to narrow the set of documents returned by a Firestore query. `QueryConstraint`s are created by invoking [where()](https://firebase.google.com/docs/reference/js/firestore_.md#where_0fae4bf), [orderBy()](https://firebase.google.com/docs/reference/js/firestore_.md#orderby_006d61f), [startAt()](https://firebase.google.com/docs/reference/js/firestore_.md#startat_9a4477f), [startAfter()](https://firebase.google.com/docs/reference/js/firestore_.md#startafter_9a4477f), [endBefore()](https://firebase.google.com/docs/reference/js/firestore_.md#endbefore_9a4477f), [endAt()](https://firebase.google.com/docs/reference/js/firestore_.md#endat_9a4477f), [limit()](https://firebase.google.com/docs/reference/js/firestore_.md#limit_ec46c78), [limitToLast()](https://firebase.google.com/docs/reference/js/firestore_.md#limittolast_ec46c78) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains this `QueryConstraint`. |
| [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.querydocumentsnapshot.md#querydocumentsnapshot_class)                            | A `QueryDocumentSnapshot` contains data read from a document in your Firestore database as part of a query. The document is guaranteed to exist and its data can be extracted with `.data()` or `.get(<field>)` to get a specific field.A `QueryDocumentSnapshot` offers the same API surface as a `DocumentSnapshot`. Since query results contain only existing documents, the `exists` property will always be true and `data()` will never return 'undefined'.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class)                               | A `QueryEndAtConstraint` is used to exclude documents from the end of a result set returned by a Firestore query. `QueryEndAtConstraint`s are created by invoking [endAt()](https://firebase.google.com/docs/reference/js/firestore_.md#endat_9a4477f) or [endBefore()](https://firebase.google.com/docs/reference/js/firestore_.md#endbefore_9a4477f) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains this `QueryEndAtConstraint`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [QueryFieldFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryfieldfilterconstraint.md#queryfieldfilterconstraint_class)             | A `QueryFieldFilterConstraint` is used to narrow the set of documents returned by a Firestore query by filtering on one or more document fields. `QueryFieldFilterConstraint`s are created by invoking [where()](https://firebase.google.com/docs/reference/js/firestore_.md#where_0fae4bf) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains this `QueryFieldFilterConstraint`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [QueryLimitConstraint](https://firebase.google.com/docs/reference/js/firestore_.querylimitconstraint.md#querylimitconstraint_class)                               | A `QueryLimitConstraint` is used to limit the number of documents returned by a Firestore query. `QueryLimitConstraint`s are created by invoking [limit()](https://firebase.google.com/docs/reference/js/firestore_.md#limit_ec46c78) or [limitToLast()](https://firebase.google.com/docs/reference/js/firestore_.md#limittolast_ec46c78) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains this `QueryLimitConstraint`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [QueryOrderByConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryorderbyconstraint.md#queryorderbyconstraint_class)                         | A `QueryOrderByConstraint` is used to sort the set of documents returned by a Firestore query. `QueryOrderByConstraint`s are created by invoking [orderBy()](https://firebase.google.com/docs/reference/js/firestore_.md#orderby_006d61f) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains this `QueryOrderByConstraint`.Note: Documents that do not contain the orderBy field will not be present in the query result.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [QuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshot_class)                                                    | A `QuerySnapshot` contains zero or more `DocumentSnapshot` objects representing the results of a query. The documents can be accessed as an array via the `docs` property or enumerated using the `forEach` method. The number of documents can be determined via the `empty` and `size` properties.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class)                         | A `QueryStartAtConstraint` is used to exclude documents from the start of a result set returned by a Firestore query. `QueryStartAtConstraint`s are created by invoking [startAt()](https://firebase.google.com/docs/reference/js/firestore_.md#startat_9a4477f) or [startAfter()](https://firebase.google.com/docs/reference/js/firestore_.md#startafter_9a4477f) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains this `QueryStartAtConstraint`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [SnapshotMetadata](https://firebase.google.com/docs/reference/js/firestore_.snapshotmetadata.md#snapshotmetadata_class)                                           | Metadata about a snapshot, describing the state of the snapshot.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Timestamp](https://firebase.google.com/docs/reference/js/firestore_.timestamp.md#timestamp_class)                                                                | A `Timestamp` represents a point in time independent of any time zone or calendar, represented as seconds and fractions of seconds at nanosecond resolution in UTC Epoch time.It is encoded using the Proleptic Gregorian Calendar which extends the Gregorian calendar backwards to year one. It is encoded assuming all minutes are 60 seconds long, i.e. leap seconds are "smeared" so that no leap second table is needed for interpretation. Range is from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59.999999999Z.For examples and further specifications, refer to the [Timestamp definition](https://github.com/google/protobuf/blob/master/src/google/protobuf/timestamp.proto).                                                                                                                                                                                                                                                                                                                                                                                           |
| [Transaction](https://firebase.google.com/docs/reference/js/firestore_.transaction.md#transaction_class)                                                          | A reference to a transaction.The `Transaction` object passed to a transaction's `updateFunction` provides the methods to read and write data within the transaction context. See [runTransaction()](https://firebase.google.com/docs/reference/js/firestore_.md#runtransaction_6f03ec4).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [VectorValue](https://firebase.google.com/docs/reference/js/firestore_.vectorvalue.md#vectorvalue_class)                                                          | Represents a vector type in Firestore documents. Create an instance with [vector()](https://firebase.google.com/docs/reference/js/firestore_.md#vector_0dbdaf2). VectorValue                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [WriteBatch](https://firebase.google.com/docs/reference/js/firestore_.writebatch.md#writebatch_class)                                                             | A write batch, used to perform multiple writes as a single atomic unit.A `WriteBatch` object can be acquired by calling [writeBatch()](https://firebase.google.com/docs/reference/js/firestore_.md#writebatch_231a8e0). It provides methods for adding writes to the write batch. None of the writes will be committed (or visible locally) until [WriteBatch.commit()](https://firebase.google.com/docs/reference/js/firestore_.writebatch.md#writebatchcommit) is called.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Interfaces

|                                                                                     Interface                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AggregateSpec](https://firebase.google.com/docs/reference/js/firestore_.aggregatespec.md#aggregatespec_interface)                                                                | Specifies a set of aggregations and their aliases.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [DocumentChange](https://firebase.google.com/docs/reference/js/firestore_.documentchange.md#documentchange_interface)                                                             | A `DocumentChange` represents a change to the documents matching a query. It contains the document affected and the type of change that occurred.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [DocumentData](https://firebase.google.com/docs/reference/js/firestore_.documentdata.md#documentdata_interface)                                                                   | Document data (for use with [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad)) consists of fields mapped to values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [ExperimentalLongPollingOptions](https://firebase.google.com/docs/reference/js/firestore_.experimentallongpollingoptions.md#experimentallongpollingoptions_interface)             | Options that configure the SDK's underlying network transport (WebChannel) when long-polling is used.Note: This interface is "experimental" and is subject to change.See `FirestoreSettings.experimentalAutoDetectLongPolling`, `FirestoreSettings.experimentalForceLongPolling`, and `FirestoreSettings.experimentalLongPollingOptions`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [FirestoreDataConverter](https://firebase.google.com/docs/reference/js/firestore_.firestoredataconverter.md#firestoredataconverter_interface)                                     | Converter used by `withConverter()` to transform user objects of type `AppModelType` into Firestore data of type `DbModelType`.Using the converter allows you to specify generic type arguments when storing and retrieving objects from Firestore.In this context, an "AppModel" is a class that is used in an application to package together related information and functionality. Such a class could, for example, have properties with complex, nested data types, properties used for memoization, properties of types not supported by Firestore (such as `symbol` and `bigint`), and helper functions that perform compound operations. Such classes are not suitable and/or possible to store into a Firestore database. Instead, instances of such classes need to be converted to "plain old JavaScript objects" (POJOs) with exclusively primitive properties, potentially nested inside other POJOs or arrays of POJOs. In this context, this type is referred to as the "DbModel" and would be an object suitable for persisting into Firestore. For convenience, applications can implement `FirestoreDataConverter` and register the converter with Firestore objects, such as `DocumentReference` or `Query`, to automatically convert `AppModel` to `DbModel` when storing into Firestore, and convert `DbModel` to `AppModel` when retrieving from Firestore. |
| [FirestoreSettings](https://firebase.google.com/docs/reference/js/firestore_.firestoresettings.md#firestoresettings_interface)                                                    | Specifies custom configurations for your Cloud Firestore instance. You must set these before invoking any other methods.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Index](https://firebase.google.com/docs/reference/js/firestore_.index.md#index_interface)                                                                                        | ***(Public Preview)*** The SDK definition of a Firestore index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [IndexConfiguration](https://firebase.google.com/docs/reference/js/firestore_.indexconfiguration.md#indexconfiguration_interface)                                                 | ***(Public Preview)*** A list of Firestore indexes to speed up local query execution.See [JSON Format](https://firebase.google.com/docs/reference/firestore/indexes/#json_format) for a description of the format of the index definition.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [IndexField](https://firebase.google.com/docs/reference/js/firestore_.indexfield.md#indexfield_interface)                                                                         | ***(Public Preview)*** A single field element in an index configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [LoadBundleTaskProgress](https://firebase.google.com/docs/reference/js/firestore_.loadbundletaskprogress.md#loadbundletaskprogress_interface)                                     | Represents a progress update or a final state from loading bundles.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [MemoryCacheSettings](https://firebase.google.com/docs/reference/js/firestore_.memorycachesettings.md#memorycachesettings_interface)                                              | An settings object to configure an `MemoryLocalCache` instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [MemoryEagerGarbageCollector](https://firebase.google.com/docs/reference/js/firestore_.memoryeagergarbagecollector.md#memoryeagergarbagecollector_interface)                      | A garbage collector deletes documents whenever they are not part of any active queries, and have no local mutations attached to them.This collector tries to ensure lowest memory footprints from the SDK, at the risk of documents not being cached for offline queries or for direct queries to the cache.Use factory function to create an instance of this collector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [MemoryLocalCache](https://firebase.google.com/docs/reference/js/firestore_.memorylocalcache.md#memorylocalcache_interface)                                                       | Provides an in-memory cache to the SDK. This is the default cache unless explicitly configured otherwise.To use, create an instance using the factory function , then set the instance to `FirestoreSettings.cache` and call `initializeFirestore` using the settings object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [MemoryLruGarbageCollector](https://firebase.google.com/docs/reference/js/firestore_.memorylrugarbagecollector.md#memorylrugarbagecollector_interface)                            | A garbage collector deletes Least-Recently-Used documents in multiple batches.This collector is configured with a target size, and will only perform collection when the cached documents exceed the target size. It avoids querying backend repeated for the same query or document, at the risk of having a larger memory footprint.Use factory function to create a instance of this collector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [PersistenceSettings](https://firebase.google.com/docs/reference/js/firestore_.persistencesettings.md#persistencesettings_interface)                                              | Settings that can be passed to `enableIndexedDbPersistence()` to configure Firestore persistence.Persistence cannot be used in a Node.js environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [PersistentCacheSettings](https://firebase.google.com/docs/reference/js/firestore_.persistentcachesettings.md#persistentcachesettings_interface)                                  | An settings object to configure an `PersistentLocalCache` instance.Persistent cache cannot be used in a Node.js environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [PersistentLocalCache](https://firebase.google.com/docs/reference/js/firestore_.persistentlocalcache.md#persistentlocalcache_interface)                                           | Provides a persistent cache backed by IndexedDb to the SDK.To use, create an instance using the factory function , then set the instance to `FirestoreSettings.cache` and call `initializeFirestore` using the settings object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [PersistentMultipleTabManager](https://firebase.google.com/docs/reference/js/firestore_.persistentmultipletabmanager.md#persistentmultipletabmanager_interface)                   | A tab manager supporting multiple tabs. SDK will synchronize queries and mutations done across all tabs using the SDK.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [PersistentSingleTabManager](https://firebase.google.com/docs/reference/js/firestore_.persistentsingletabmanager.md#persistentsingletabmanager_interface)                         | A tab manager supporting only one tab, no synchronization will be performed across tabs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [PersistentSingleTabManagerSettings](https://firebase.google.com/docs/reference/js/firestore_.persistentsingletabmanagersettings.md#persistentsingletabmanagersettings_interface) | Type to configure an `PersistentSingleTabManager` instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [SnapshotListenOptions](https://firebase.google.com/docs/reference/js/firestore_.snapshotlistenoptions.md#snapshotlistenoptions_interface)                                        | An options object that can be passed to [onSnapshot()](https://firebase.google.com/docs/reference/js/firestore_.md#onsnapshot_0312fd7) and [QuerySnapshot.docChanges()](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshotdocchanges) to control which types of changes to include in the result set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [SnapshotOptions](https://firebase.google.com/docs/reference/js/firestore_.snapshotoptions.md#snapshotoptions_interface)                                                          | Options that configure how data is retrieved from a `DocumentSnapshot` (for example the desired behavior for server timestamps that have not yet been set to their final value).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [TransactionOptions](https://firebase.google.com/docs/reference/js/firestore_.transactionoptions.md#transactionoptions_interface)                                                 | Options to customize transaction behavior.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Unsubscribe](https://firebase.google.com/docs/reference/js/firestore_.unsubscribe.md#unsubscribe_interface)                                                                      | A function returned by `onSnapshot()` that removes the listener when invoked.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

## Variables

|                                                 Variable                                                 |                                                                                                                        Description                                                                                                                         |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CACHE_SIZE_UNLIMITED](https://firebase.google.com/docs/reference/js/firestore_.md#cache_size_unlimited) | Constant used to indicate the LRU garbage collection should be disabled. Set this value as the `cacheSizeBytes` on the settings passed to the [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance. |

## Type Aliases

|                                                    Type Alias                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AddPrefixToKeys](https://firebase.google.com/docs/reference/js/firestore_.md#addprefixtokeys)                   | Returns a new map where every key is prefixed with the outer key appended to a dot.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [AggregateFieldType](https://firebase.google.com/docs/reference/js/firestore_.md#aggregatefieldtype)             | The union of all `AggregateField` types that are supported by Firestore.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [AggregateSpecData](https://firebase.google.com/docs/reference/js/firestore_.md#aggregatespecdata)               | A type whose keys are taken from an `AggregateSpec`, and whose values are the result of the aggregation performed by the corresponding `AggregateField` from the input `AggregateSpec`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [AggregateType](https://firebase.google.com/docs/reference/js/firestore_.md#aggregatetype)                       | Union type representing the aggregate type to be performed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [ChildUpdateFields](https://firebase.google.com/docs/reference/js/firestore_.md#childupdatefields)               | Helper for calculating the nested fields for a given type T1. This is needed to distribute union types such as `undefined | {...}` (happens for optional props) or `{a: A} | {b: B}`.In this use case, `V` is used to distribute the union types of `T[K]` on `Record`, since `T[K]` is evaluated as an expression and not distributed.See https://www.typescriptlang.org/docs/handbook/advanced-types.html#distributive-conditional-types                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [DocumentChangeType](https://firebase.google.com/docs/reference/js/firestore_.md#documentchangetype)             | The type of a `DocumentChange` may be 'added', 'removed', or 'modified'.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [FirestoreErrorCode](https://firebase.google.com/docs/reference/js/firestore_.md#firestoreerrorcode)             | The set of Firestore status codes. The codes are the same at the ones exposed by gRPC here: https://github.com/grpc/grpc/blob/master/doc/statuscodes.mdPossible values: - 'cancelled': The operation was cancelled (typically by the caller). - 'unknown': Unknown error or an error from a different error domain. - 'invalid-argument': Client specified an invalid argument. Note that this differs from 'failed-precondition'. 'invalid-argument' indicates arguments that are problematic regardless of the state of the system (e.g. an invalid field name). - 'deadline-exceeded': Deadline expired before operation could complete. For operations that change the state of the system, this error may be returned even if the operation has completed successfully. For example, a successful response from a server could have been delayed long enough for the deadline to expire. - 'not-found': Some requested document was not found. - 'already-exists': Some document that we attempted to create already exists. - 'permission-denied': The caller does not have permission to execute the specified operation. - 'resource-exhausted': Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space. - 'failed-precondition': Operation was rejected because the system is not in a state required for the operation's execution. - 'aborted': The operation was aborted, typically due to a concurrency issue like transaction aborts, etc. - 'out-of-range': Operation was attempted past the valid range. - 'unimplemented': Operation is not implemented or not supported/enabled. - 'internal': Internal errors. Means some invariants expected by underlying system has been broken. If you see one of these errors, something is very broken. - 'unavailable': The service is currently unavailable. This is most likely a transient condition and may be corrected by retrying with a backoff. - 'data-loss': Unrecoverable data loss or corruption. - 'unauthenticated': The request does not have valid authentication credentials for the operation. |
| [FirestoreLocalCache](https://firebase.google.com/docs/reference/js/firestore_.md#firestorelocalcache)           | Union type from all supported SDK cache layer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [ListenSource](https://firebase.google.com/docs/reference/js/firestore_.md#listensource)                         | Describe the source a query listens to.Set to `default` to listen to both cache and server changes. Set to `cache` to listen to changes in cache only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [MemoryGarbageCollector](https://firebase.google.com/docs/reference/js/firestore_.md#memorygarbagecollector)     | Union type from all support garbage collectors for memory local cache.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [NestedUpdateFields](https://firebase.google.com/docs/reference/js/firestore_.md#nestedupdatefields)             | For each field (e.g. 'bar'), find all nested keys (e.g. {'bar.baz': T1, 'bar.qux': T2}). Intersect them together to make a single map containing all possible keys that are all marked as optional                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [OrderByDirection](https://firebase.google.com/docs/reference/js/firestore_.md#orderbydirection)                 | The direction of a [orderBy()](https://firebase.google.com/docs/reference/js/firestore_.md#orderby_006d61f) clause is specified as 'desc' or 'asc' (descending or ascending).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [PartialWithFieldValue](https://firebase.google.com/docs/reference/js/firestore_.md#partialwithfieldvalue)       | Similar to TypeScript's `Partial<T>`, but allows nested fields to be omitted and FieldValues to be passed in as property values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [PersistentTabManager](https://firebase.google.com/docs/reference/js/firestore_.md#persistenttabmanager)         | A union of all available tab managers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Primitive](https://firebase.google.com/docs/reference/js/firestore_.md#primitive)                               | Primitive types.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [QueryConstraintType](https://firebase.google.com/docs/reference/js/firestore_.md#queryconstrainttype)           | Describes the different query constraints available in this SDK.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [QueryFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.md#queryfilterconstraint)       | `QueryFilterConstraint` is a helper union type that represents [QueryFieldFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryfieldfilterconstraint.md#queryfieldfilterconstraint_class) and [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [QueryNonFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.md#querynonfilterconstraint) | `QueryNonFilterConstraint` is a helper union type that represents QueryConstraints which are used to narrow or order the set of documents, but that do not explicitly filter on a document field. `QueryNonFilterConstraint`s are created by invoking [orderBy()](https://firebase.google.com/docs/reference/js/firestore_.md#orderby_006d61f), [startAt()](https://firebase.google.com/docs/reference/js/firestore_.md#startat_9a4477f), [startAfter()](https://firebase.google.com/docs/reference/js/firestore_.md#startafter_9a4477f), [endBefore()](https://firebase.google.com/docs/reference/js/firestore_.md#endbefore_9a4477f), [endAt()](https://firebase.google.com/docs/reference/js/firestore_.md#endat_9a4477f), [limit()](https://firebase.google.com/docs/reference/js/firestore_.md#limit_ec46c78) or [limitToLast()](https://firebase.google.com/docs/reference/js/firestore_.md#limittolast_ec46c78) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains the `QueryConstraint`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [SetOptions](https://firebase.google.com/docs/reference/js/firestore_.md#setoptions)                             | An options object that configures the behavior of [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad), and calls. These calls can be configured to perform granular merges instead of overwriting the target documents in their entirety by providing a `SetOptions` with `merge: true`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [TaskState](https://firebase.google.com/docs/reference/js/firestore_.md#taskstate)                               | Represents the state of bundle loading tasks.Both 'Error' and 'Success' are sinking state: task will abort or complete and there will be no more updates after they are reported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [UnionToIntersection](https://firebase.google.com/docs/reference/js/firestore_.md#uniontointersection)           | Given a union type `U = T1 | T2 | ...`, returns an intersected type `(T1 & T2 & ...)`.Uses distributive conditional types and inference from conditional types. This works because multiple candidates for the same type variable in contra-variant positions causes an intersection type to be inferred. https://www.typescriptlang.org/docs/handbook/advanced-types.html#type-inference-in-conditional-types https://stackoverflow.com/questions/50374908/transform-union-type-to-intersection-type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [UpdateData](https://firebase.google.com/docs/reference/js/firestore_.md#updatedata)                             | Update data (for use with [updateDoc()](https://firebase.google.com/docs/reference/js/firestore_.md#updatedoc_51a65e3)) that consists of field paths (e.g. 'foo' or 'foo.baz') mapped to values. Fields that contain dots reference nested fields within the document. FieldValues can be passed in as property values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [WhereFilterOp](https://firebase.google.com/docs/reference/js/firestore_.md#wherefilterop)                       | Filter conditions in a [where()](https://firebase.google.com/docs/reference/js/firestore_.md#where_0fae4bf) clause are specified using the strings '\&lt;', '\&lt;=', '==', '!=', '\&gt;=', '\&gt;', 'array-contains', 'in', 'array-contains-any', and 'not-in'.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [WithFieldValue](https://firebase.google.com/docs/reference/js/firestore_.md#withfieldvalue)                     | Allows FieldValues to be passed in as a property value while maintaining type safety.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## function(app, ...)

### getFirestore(app)

Returns the existing default [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance that is associated with the provided [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface). If no instance exists, initializes a new instance with default settings.

**Signature:**  

    export declare function getFirestore(app: FirebaseApp): Firestore;

#### Parameters

| Parameter |                                                 Type                                                  |                                                                                                                             Description                                                                                                                              |
|-----------|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| app       | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) | The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) instance that the returned [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance is associated with. |

**Returns:**

[Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class)

The default [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance of the provided app.

### getFirestore(app, databaseId)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Returns the existing named [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance that is associated with the provided [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface). If no instance exists, initializes a new instance with default settings.

**Signature:**  

    export declare function getFirestore(app: FirebaseApp, databaseId: string): Firestore;

#### Parameters

| Parameter  |                                                 Type                                                  |                                                                                                                             Description                                                                                                                              |
|------------|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| app        | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) | The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) instance that the returned [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance is associated with. |
| databaseId | string                                                                                                | The name of the database.                                                                                                                                                                                                                                            |

**Returns:**

[Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class)

The named [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance of the provided app.

### initializeFirestore(app, settings, databaseId)

Initializes a new instance of [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) with the provided settings. Can only be called before any other function, including [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore). If the custom settings are empty, this function is equivalent to calling [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore).

**Signature:**  

    export declare function initializeFirestore(app: FirebaseApp, settings: FirestoreSettings, databaseId?: string): Firestore;

#### Parameters

| Parameter  |                                                              Type                                                              |                                                                                                                       Description                                                                                                                        |
|------------|--------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| app        | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface)                          | The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) with which the [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance will be associated. |
| settings   | [FirestoreSettings](https://firebase.google.com/docs/reference/js/firestore_.firestoresettings.md#firestoresettings_interface) | A settings object to configure the [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance.                                                                                                          |
| databaseId | string                                                                                                                         | The name of the database.                                                                                                                                                                                                                                |

**Returns:**

[Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class)

A newly initialized [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance.

## function(db, ...)

### documentSnapshotFromJSON(db, json)

Builds a `DocumentSnapshot` instance from a JSON object created by [DocumentSnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshottojson).

**Signature:**  

    export declare function documentSnapshotFromJSON(db: Firestore, json: object): DocumentSnapshot;

#### Parameters

| Parameter |                                                Type                                                |                         Description                          |
|-----------|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| db        | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) |                                                              |
| json      | object                                                                                             | a JSON object represention of a `DocumentSnapshot` instance. |

**Returns:**

[DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshot_class)

an instance of [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshot_class) if the JSON object could be parsed. Throws a [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class) if an error occurs.

### documentSnapshotFromJSON(db, json, converter)

Builds a `DocumentSnapshot` instance from a JSON object created by [DocumentSnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshottojson).

**Signature:**  

    export declare function documentSnapshotFromJSON<AppModelType, DbModelType extends DocumentData = DocumentData>(db: Firestore, json: object, converter: FirestoreDataConverter<AppModelType, DbModelType>): DocumentSnapshot<AppModelType, DbModelType>;

#### Parameters

| Parameter |                                                                                    Type                                                                                    |                         Description                          |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| db        | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class)                                                                         |                                                              |
| json      | object                                                                                                                                                                     | a JSON object represention of a `DocumentSnapshot` instance. |
| converter | [FirestoreDataConverter](https://firebase.google.com/docs/reference/js/firestore_.firestoredataconverter.md#firestoredataconverter_interface)\<AppModelType, DbModelType\> | Converts objects to and from Firestore.                      |

**Returns:**

[DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\>

an instance of [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshot_class) if the JSON object could be parsed. Throws a [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class) if an error occurs.

### querySnapshotFromJSON(db, json)

Builds a `QuerySnapshot` instance from a JSON object created by [QuerySnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshottojson).

**Signature:**  

    export declare function querySnapshotFromJSON(db: Firestore, json: object): QuerySnapshot;

#### Parameters

| Parameter |                                                Type                                                |                        Description                        |
|-----------|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| db        | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) |                                                           |
| json      | object                                                                                             | a JSON object represention of a `QuerySnapshot` instance. |

**Returns:**

[QuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshot_class)

an instance of [QuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshot_class) if the JSON object could be parsed. Throws a [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class) if an error occurs.

### querySnapshotFromJSON(db, json, converter)

Builds a `QuerySnapshot` instance from a JSON object created by [QuerySnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshottojson).

**Signature:**  

    export declare function querySnapshotFromJSON<AppModelType, DbModelType extends DocumentData = DocumentData>(db: Firestore, json: object, converter: FirestoreDataConverter<AppModelType, DbModelType>): QuerySnapshot<AppModelType, DbModelType>;

#### Parameters

| Parameter |                                                                                    Type                                                                                    |                        Description                        |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| db        | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class)                                                                         |                                                           |
| json      | object                                                                                                                                                                     | a JSON object represention of a `QuerySnapshot` instance. |
| converter | [FirestoreDataConverter](https://firebase.google.com/docs/reference/js/firestore_.firestoredataconverter.md#firestoredataconverter_interface)\<AppModelType, DbModelType\> | Converts objects to and from Firestore.                   |

**Returns:**

[QuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshot_class)\<AppModelType, DbModelType\>

an instance of [QuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshot_class) if the JSON object could be parsed. Throws a [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class) if an error occurs.

## function(firestore, ...)

### clearIndexedDbPersistence(firestore)

Clears the persistent storage. This includes pending writes and cached documents.

Must be called while the [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance is not started (after the app is terminated or when the app is first initialized). On startup, this function must be called before other functions (other than [initializeFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#initializefirestore_fc7d200) or [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore))). If the [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance is still running, the promise will be rejected with the error code of `failed-precondition`.
| **Note:** `clearIndexedDbPersistence()` is primarily intended to help write reliable tests that use Cloud Firestore. It uses an efficient mechanism for dropping existing data but does not attempt to securely overwrite or otherwise make cached data unrecoverable. For applications that are sensitive to the disclosure of cached data in between user sessions, we strongly recommend not enabling persistence at all.

**Signature:**  

    export declare function clearIndexedDbPersistence(firestore: Firestore): Promise<void>;

#### Parameters

| Parameter |                                                Type                                                |                                                                Description                                                                |
|-----------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| firestore | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) | The [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance to clear persistence for. |

**Returns:**

Promise\<void\>

A `Promise` that is resolved when the persistent storage is cleared. Otherwise, the promise is rejected with an error.

### collection(firestore, path, pathSegments)

Gets a `CollectionReference` instance that refers to the collection at the specified absolute path.

**Signature:**  

    export declare function collection(firestore: Firestore, path: string, ...pathSegments: string[]): CollectionReference<DocumentData, DocumentData>;

#### Parameters

|  Parameter   |                                                Type                                                |                            Description                            |
|--------------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| firestore    | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) | A reference to the root `Firestore` instance.                     |
| path         | string                                                                                             | A slash-separated path to a collection.                           |
| pathSegments | string\[\]                                                                                         | Additional path segments to apply relative to the first argument. |

**Returns:**

[CollectionReference](https://firebase.google.com/docs/reference/js/firestore_.collectionreference.md#collectionreference_class)\<[DocumentData](https://firebase.google.com/docs/reference/js/firestore_.documentdata.md#documentdata_interface), [DocumentData](https://firebase.google.com/docs/reference/js/firestore_.documentdata.md#documentdata_interface)\>

The `CollectionReference` instance.

#### Exceptions

If the final path has an even number of segments and does not point to a collection.

### collectionGroup(firestore, collectionId)

Creates and returns a new `Query` instance that includes all documents in the database that are contained in a collection or subcollection with the given `collectionId`.

**Signature:**  

    export declare function collectionGroup(firestore: Firestore, collectionId: string): Query<DocumentData, DocumentData>;

#### Parameters

|  Parameter   |                                                Type                                                |                                                                            Description                                                                             |
|--------------|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| firestore    | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) | A reference to the root `Firestore` instance.                                                                                                                      |
| collectionId | string                                                                                             | Identifies the collections to query over. Every collection or subcollection with this ID as the last segment of its path will be included. Cannot contain a slash. |

**Returns:**

[Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class)\<[DocumentData](https://firebase.google.com/docs/reference/js/firestore_.documentdata.md#documentdata_interface), [DocumentData](https://firebase.google.com/docs/reference/js/firestore_.documentdata.md#documentdata_interface)\>

The created `Query`.

### connectFirestoreEmulator(firestore, host, port, options)

Modify this instance to communicate with the Cloud Firestore emulator.
| **Note:** This must be called before this instance has been used to do any operations.

**Signature:**  

    export declare function connectFirestoreEmulator(firestore: Firestore, host: string, port: number, options?: {
        mockUserToken?: EmulatorMockTokenOptions | string;
    }): void;

#### Parameters

| Parameter |                                                                   Type                                                                    |                            Description                            |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| firestore | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class)                                        | The `Firestore` instance to configure to connect to the emulator. |
| host      | string                                                                                                                                    | the emulator host (ex: localhost).                                |
| port      | number                                                                                                                                    | the emulator port (ex: 9000).                                     |
| options   | { mockUserToken?: [EmulatorMockTokenOptions](https://firebase.google.com/docs/reference/js/util.md#emulatormocktokenoptions) \| string; } |                                                                   |

**Returns:**

void

### disableNetwork(firestore)

Disables network usage for this instance. It can be re-enabled via [enableNetwork()](https://firebase.google.com/docs/reference/js/firestore_.md#enablenetwork_231a8e0). While the network is disabled, any snapshot listeners, `getDoc()` or `getDocs()` calls will return results from cache, and any write operations will be queued until the network is restored.

**Signature:**  

    export declare function disableNetwork(firestore: Firestore): Promise<void>;

#### Parameters

| Parameter |                                                Type                                                | Description |
|-----------|----------------------------------------------------------------------------------------------------|-------------|
| firestore | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) |             |

**Returns:**

Promise\<void\>

A `Promise` that is resolved once the network has been disabled.

### doc(firestore, path, pathSegments)

Gets a `DocumentReference` instance that refers to the document at the specified absolute path.

**Signature:**  

    export declare function doc(firestore: Firestore, path: string, ...pathSegments: string[]): DocumentReference<DocumentData, DocumentData>;

#### Parameters

|  Parameter   |                                                Type                                                |                                  Description                                  |
|--------------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| firestore    | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) | A reference to the root `Firestore` instance.                                 |
| path         | string                                                                                             | A slash-separated path to a document.                                         |
| pathSegments | string\[\]                                                                                         | Additional path segments that will be applied relative to the first argument. |

**Returns:**

[DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class)\<[DocumentData](https://firebase.google.com/docs/reference/js/firestore_.documentdata.md#documentdata_interface), [DocumentData](https://firebase.google.com/docs/reference/js/firestore_.documentdata.md#documentdata_interface)\>

The `DocumentReference` instance.

#### Exceptions

If the final path has an odd number of segments and does not point to a document.

### enableIndexedDbPersistence(firestore, persistenceSettings)

> | **Warning:** This API is now obsolete.
>
> This function will be removed in a future major release. Instead, set `FirestoreSettings.localCache` to an instance of `PersistentLocalCache` to turn on IndexedDb cache. Calling this function when `FirestoreSettings.localCache` is already specified will throw an exception.

Attempts to enable persistent storage, if possible.

On failure, `enableIndexedDbPersistence()` will reject the promise or throw an exception. There are several reasons why this can fail, which can be identified by the `code` on the error.

\* failed-precondition: The app is already open in another browser tab. \* unimplemented: The browser is incompatible with the offline persistence implementation.

Note that even after a failure, the [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance will remain usable, however offline persistence will be disabled.
| **Note:** `enableIndexedDbPersistence()` must be called before any other functions (other than [initializeFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#initializefirestore_fc7d200), [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore) or [clearIndexedDbPersistence()](https://firebase.google.com/docs/reference/js/firestore_.md#clearindexeddbpersistence_231a8e0).

Persistence cannot be used in a Node.js environment.

**Signature:**  

    export declare function enableIndexedDbPersistence(firestore: Firestore, persistenceSettings?: PersistenceSettings): Promise<void>;

#### Parameters

|      Parameter      |                                                                 Type                                                                 |                                                                Description                                                                 |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| firestore           | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class)                                   | The [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance to enable persistence for. |
| persistenceSettings | [PersistenceSettings](https://firebase.google.com/docs/reference/js/firestore_.persistencesettings.md#persistencesettings_interface) | Optional settings object to configure persistence.                                                                                         |

**Returns:**

Promise\<void\>

A `Promise` that represents successfully enabling persistent storage.

### enableMultiTabIndexedDbPersistence(firestore)

> | **Warning:** This API is now obsolete.
>
> This function will be removed in a future major release. Instead, set `FirestoreSettings.localCache` to an instance of `PersistentLocalCache` to turn on indexeddb cache. Calling this function when `FirestoreSettings.localCache` is already specified will throw an exception.

Attempts to enable multi-tab persistent storage, if possible. If enabled across all tabs, all operations share access to local persistence, including shared execution of queries and latency-compensated local document updates across all connected instances.

On failure, `enableMultiTabIndexedDbPersistence()` will reject the promise or throw an exception. There are several reasons why this can fail, which can be identified by the `code` on the error.

\* failed-precondition: The app is already open in another browser tab and multi-tab is not enabled. \* unimplemented: The browser is incompatible with the offline persistence implementation.

Note that even after a failure, the [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance will remain usable, however offline persistence will be disabled.

**Signature:**  

    export declare function enableMultiTabIndexedDbPersistence(firestore: Firestore): Promise<void>;

#### Parameters

| Parameter |                                                Type                                                |                                                                Description                                                                 |
|-----------|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| firestore | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) | The [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance to enable persistence for. |

**Returns:**

Promise\<void\>

A `Promise` that represents successfully enabling persistent storage.

### enableNetwork(firestore)

Re-enables use of the network for this [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance after a prior call to [disableNetwork()](https://firebase.google.com/docs/reference/js/firestore_.md#disablenetwork_231a8e0).

**Signature:**  

    export declare function enableNetwork(firestore: Firestore): Promise<void>;

#### Parameters

| Parameter |                                                Type                                                | Description |
|-----------|----------------------------------------------------------------------------------------------------|-------------|
| firestore | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) |             |

**Returns:**

Promise\<void\>

A `Promise` that is resolved once the network has been enabled.

### getPersistentCacheIndexManager(firestore)

Returns the PersistentCache Index Manager used by the given `Firestore` object.

The `PersistentCacheIndexManager` instance, or `null` if local persistent storage is not in use.

**Signature:**  

    export declare function getPersistentCacheIndexManager(firestore: Firestore): PersistentCacheIndexManager | null;

#### Parameters

| Parameter |                                                Type                                                | Description |
|-----------|----------------------------------------------------------------------------------------------------|-------------|
| firestore | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) |             |

**Returns:**

[PersistentCacheIndexManager](https://firebase.google.com/docs/reference/js/firestore_.persistentcacheindexmanager.md#persistentcacheindexmanager_class) \| null

### loadBundle(firestore, bundleData)

Loads a Firestore bundle into the local cache.

**Signature:**  

    export declare function loadBundle(firestore: Firestore, bundleData: ReadableStream<Uint8Array> | ArrayBuffer | string): LoadBundleTask;

#### Parameters

| Parameter  |                                                Type                                                |                                                             Description                                                              |
|------------|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| firestore  | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) | The [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance to load bundles for. |
| bundleData | ReadableStream\<Uint8Array\> \| ArrayBuffer \| string                                              | An object representing the bundle to be loaded. Valid objects are `ArrayBuffer`, `ReadableStream<Uint8Array>` or `string`.           |

**Returns:**

[LoadBundleTask](https://firebase.google.com/docs/reference/js/firestore_.loadbundletask.md#loadbundletask_class)

A `LoadBundleTask` object, which notifies callers with progress updates, and completion or error events. It can be used as a `Promise<LoadBundleTaskProgress>`.

### namedQuery(firestore, name)

Reads a Firestore [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class) from local cache, identified by the given name.

The named queries are packaged into bundles on the server side (along with resulting documents), and loaded to local cache using `loadBundle`. Once in local cache, use this method to extract a [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class) by name.

**Signature:**  

    export declare function namedQuery(firestore: Firestore, name: string): Promise<Query | null>;

#### Parameters

| Parameter |                                                Type                                                |                                                               Description                                                               |
|-----------|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| firestore | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) | The [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance to read the query from. |
| name      | string                                                                                             | The name of the query.                                                                                                                  |

**Returns:**

Promise\<[Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class) \| null\>

A `Promise` that is resolved with the Query or `null`.

### onSnapshotResume(firestore, snapshotJson, onNext, onError, onCompletion, converter)

Attaches a listener for `QuerySnapshot` events based on data generated by invoking [QuerySnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshottojson) You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks. The listener can be cancelled by calling the function that is returned when `onSnapshot` is called.

NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.

**Signature:**  

    export declare function onSnapshotResume<AppModelType, DbModelType extends DocumentData>(firestore: Firestore, snapshotJson: object, onNext: (snapshot: QuerySnapshot<AppModelType, DbModelType>) => void, onError?: (error: FirestoreError) => void, onCompletion?: () => void, converter?: FirestoreDataConverter<DbModelType>): Unsubscribe;

#### Parameters

|  Parameter   |                                                                               Type                                                                               |                                                                         Description                                                                          |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| firestore    | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class)                                                               | The [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance to enable the listener for.                  |
| snapshotJson | object                                                                                                                                                           | A JSON object generated by invoking [QuerySnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshottojson). |
| onNext       | (snapshot: [QuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshot_class)\<AppModelType, DbModelType\>) =\> void | A callback to be called every time a new `QuerySnapshot` is available.                                                                                       |
| onError      | (error: [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class)) =\> void                              | A callback to be called if the listen fails or is cancelled. No further callbacks will occur.                                                                |
| onCompletion | () =\> void                                                                                                                                                      | Can be provided, but will not be called since streams are never ending.                                                                                      |
| converter    | [FirestoreDataConverter](https://firebase.google.com/docs/reference/js/firestore_.firestoredataconverter.md#firestoredataconverter_interface)\<DbModelType\>     | An optional object that converts objects from Firestore before the onNext listener is invoked.                                                               |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/firestore_.unsubscribe.md#unsubscribe_interface)

An unsubscribe function that can be called to cancel the snapshot listener.

### onSnapshotResume(firestore, snapshotJson, onNext, onError, onCompletion, converter)

Attaches a listener for `DocumentSnapshot` events based on data generated by invoking [DocumentSnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshottojson). You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks. The listener can be cancelled by calling the function that is returned when `onSnapshot` is called.

NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.

**Signature:**  

    export declare function onSnapshotResume<AppModelType, DbModelType extends DocumentData>(firestore: Firestore, snapshotJson: object, onNext: (snapshot: DocumentSnapshot<AppModelType, DbModelType>) => void, onError?: (error: FirestoreError) => void, onCompletion?: () => void, converter?: FirestoreDataConverter<DbModelType>): Unsubscribe;

#### Parameters

|  Parameter   |                                                                                   Type                                                                                    |                                                                              Description                                                                              |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| firestore    | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class)                                                                        | The [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance to enable the listener for.                           |
| snapshotJson | object                                                                                                                                                                    | A JSON object generated by invoking [DocumentSnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshottojson). |
| onNext       | (snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\>) =\> void | A callback to be called every time a new `DocumentSnapshot` is available.                                                                                             |
| onError      | (error: [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class)) =\> void                                       | A callback to be called if the listen fails or is cancelled. No further callbacks will occur.                                                                         |
| onCompletion | () =\> void                                                                                                                                                               | Can be provided, but will not be called since streams are never ending.                                                                                               |
| converter    | [FirestoreDataConverter](https://firebase.google.com/docs/reference/js/firestore_.firestoredataconverter.md#firestoredataconverter_interface)\<DbModelType\>              | An optional object that converts objects from Firestore before the onNext listener is invoked.                                                                        |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/firestore_.unsubscribe.md#unsubscribe_interface)

An unsubscribe function that can be called to cancel the snapshot listener.

### onSnapshotResume(firestore, snapshotJson, options, onNext, onError, onCompletion, converter)

Attaches a listener for `QuerySnapshot` events based on data generated by invoking [QuerySnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshottojson). You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks. The listener can be cancelled by calling the function that is returned when `onSnapshot` is called.

NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.

**Signature:**  

    export declare function onSnapshotResume<AppModelType, DbModelType extends DocumentData>(firestore: Firestore, snapshotJson: object, options: SnapshotListenOptions, onNext: (snapshot: QuerySnapshot<AppModelType, DbModelType>) => void, onError?: (error: FirestoreError) => void, onCompletion?: () => void, converter?: FirestoreDataConverter<DbModelType>): Unsubscribe;

#### Parameters

|  Parameter   |                                                                               Type                                                                               |                                                                         Description                                                                          |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| firestore    | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class)                                                               | The [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance to enable the listener for.                  |
| snapshotJson | object                                                                                                                                                           | A JSON object generated by invoking [QuerySnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshottojson). |
| options      | [SnapshotListenOptions](https://firebase.google.com/docs/reference/js/firestore_.snapshotlistenoptions.md#snapshotlistenoptions_interface)                       | Options controlling the listen behavior.                                                                                                                     |
| onNext       | (snapshot: [QuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshot_class)\<AppModelType, DbModelType\>) =\> void | A callback to be called every time a new `QuerySnapshot` is available.                                                                                       |
| onError      | (error: [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class)) =\> void                              | A callback to be called if the listen fails or is cancelled. No further callbacks will occur.                                                                |
| onCompletion | () =\> void                                                                                                                                                      | Can be provided, but will not be called since streams are never ending.                                                                                      |
| converter    | [FirestoreDataConverter](https://firebase.google.com/docs/reference/js/firestore_.firestoredataconverter.md#firestoredataconverter_interface)\<DbModelType\>     | An optional object that converts objects from Firestore before the onNext listener is invoked.                                                               |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/firestore_.unsubscribe.md#unsubscribe_interface)

An unsubscribe function that can be called to cancel the snapshot listener.

### onSnapshotResume(firestore, snapshotJson, options, onNext, onError, onCompletion, converter)

Attaches a listener for `DocumentSnapshot` events based on data generated by invoking [DocumentSnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshottojson). You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks. The listener can be cancelled by calling the function that is returned when `onSnapshot` is called.

NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.

**Signature:**  

    export declare function onSnapshotResume<AppModelType, DbModelType extends DocumentData>(firestore: Firestore, snapshotJson: object, options: SnapshotListenOptions, onNext: (snapshot: DocumentSnapshot<AppModelType, DbModelType>) => void, onError?: (error: FirestoreError) => void, onCompletion?: () => void, converter?: FirestoreDataConverter<DbModelType>): Unsubscribe;

#### Parameters

|  Parameter   |                                                                                   Type                                                                                    |                                                                              Description                                                                              |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| firestore    | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class)                                                                        | The [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance to enable the listener for.                           |
| snapshotJson | object                                                                                                                                                                    | A JSON object generated by invoking [DocumentSnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshottojson). |
| options      | [SnapshotListenOptions](https://firebase.google.com/docs/reference/js/firestore_.snapshotlistenoptions.md#snapshotlistenoptions_interface)                                | Options controlling the listen behavior.                                                                                                                              |
| onNext       | (snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\>) =\> void | A callback to be called every time a new `DocumentSnapshot` is available.                                                                                             |
| onError      | (error: [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class)) =\> void                                       | A callback to be called if the listen fails or is cancelled. No further callbacks will occur.                                                                         |
| onCompletion | () =\> void                                                                                                                                                               | Can be provided, but will not be called since streams are never ending.                                                                                               |
| converter    | [FirestoreDataConverter](https://firebase.google.com/docs/reference/js/firestore_.firestoredataconverter.md#firestoredataconverter_interface)\<DbModelType\>              | An optional object that converts objects from Firestore before the onNext listener is invoked.                                                                        |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/firestore_.unsubscribe.md#unsubscribe_interface)

An unsubscribe function that can be called to cancel the snapshot listener.

### onSnapshotResume(firestore, snapshotJson, observer, converter)

Attaches a listener for `QuerySnapshot` events based on QuerySnapshot data generated by invoking [QuerySnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshottojson). You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks. The listener can be cancelled by calling the function that is returned when `onSnapshot` is called.

NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.

**Signature:**  

    export declare function onSnapshotResume<AppModelType, DbModelType extends DocumentData>(firestore: Firestore, snapshotJson: object, observer: {
        next: (snapshot: QuerySnapshot<AppModelType, DbModelType>) => void;
        error?: (error: FirestoreError) => void;
        complete?: () => void;
    }, converter?: FirestoreDataConverter<DbModelType>): Unsubscribe;

#### Parameters

|  Parameter   |                                                                                                                                                                       Type                                                                                                                                                                       |                                                                         Description                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| firestore    | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class)                                                                                                                                                                                                                                               | The [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance to enable the listener for.                  |
| snapshotJson | object                                                                                                                                                                                                                                                                                                                                           | A JSON object generated by invoking [QuerySnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshottojson). |
| observer     | { next: (snapshot: [QuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshot_class)\<AppModelType, DbModelType\>) =\> void; error?: (error: [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class)) =\> void; complete?: () =\> void; } | A single object containing `next` and `error` callbacks.                                                                                                     |
| converter    | [FirestoreDataConverter](https://firebase.google.com/docs/reference/js/firestore_.firestoredataconverter.md#firestoredataconverter_interface)\<DbModelType\>                                                                                                                                                                                     | An optional object that converts objects from Firestore before the onNext listener is invoked.                                                               |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/firestore_.unsubscribe.md#unsubscribe_interface)

An unsubscribe function that can be called to cancel the snapshot listener.

### onSnapshotResume(firestore, snapshotJson, observer, converter)

Attaches a listener for `DocumentSnapshot` events based on data generated by invoking [DocumentSnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshottojson) You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks. The listener can be cancelled by calling the function that is returned when `onSnapshot` is called.

NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.

**Signature:**  

    export declare function onSnapshotResume<AppModelType, DbModelType extends DocumentData>(firestore: Firestore, snapshotJson: object, observer: {
        next: (snapshot: DocumentSnapshot<AppModelType, DbModelType>) => void;
        error?: (error: FirestoreError) => void;
        complete?: () => void;
    }, converter?: FirestoreDataConverter<DbModelType>): Unsubscribe;

#### Parameters

|  Parameter   |                                                                                                                                                                           Type                                                                                                                                                                            |                                                                              Description                                                                              |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| firestore    | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class)                                                                                                                                                                                                                                                        | The [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance to enable the listener for.                           |
| snapshotJson | object                                                                                                                                                                                                                                                                                                                                                    | A JSON object generated by invoking [DocumentSnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshottojson). |
| observer     | { next: (snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\>) =\> void; error?: (error: [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class)) =\> void; complete?: () =\> void; } | A single object containing `next` and `error` callbacks.                                                                                                              |
| converter    | [FirestoreDataConverter](https://firebase.google.com/docs/reference/js/firestore_.firestoredataconverter.md#firestoredataconverter_interface)\<DbModelType\>                                                                                                                                                                                              | An optional object that converts objects from Firestore before the onNext listener is invoked.                                                                        |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/firestore_.unsubscribe.md#unsubscribe_interface)

An unsubscribe function that can be called to cancel the snapshot listener.

### onSnapshotResume(firestore, snapshotJson, options, observer, converter)

Attaches a listener for `QuerySnapshot` events based on QuerySnapshot data generated by invoking [QuerySnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshottojson) You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks. The listener can be cancelled by calling the function that is returned when `onSnapshot` is called.

NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.

**Signature:**  

    export declare function onSnapshotResume<AppModelType, DbModelType extends DocumentData>(firestore: Firestore, snapshotJson: object, options: SnapshotListenOptions, observer: {
        next: (snapshot: QuerySnapshot<AppModelType, DbModelType>) => void;
        error?: (error: FirestoreError) => void;
        complete?: () => void;
    }, converter?: FirestoreDataConverter<DbModelType>): Unsubscribe;

#### Parameters

|  Parameter   |                                                                                                                                                                       Type                                                                                                                                                                       |                                                                         Description                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| firestore    | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class)                                                                                                                                                                                                                                               | The [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance to enable the listener for.                  |
| snapshotJson | object                                                                                                                                                                                                                                                                                                                                           | A JSON object generated by invoking [QuerySnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshottojson). |
| options      | [SnapshotListenOptions](https://firebase.google.com/docs/reference/js/firestore_.snapshotlistenoptions.md#snapshotlistenoptions_interface)                                                                                                                                                                                                       | Options controlling the listen behavior.                                                                                                                     |
| observer     | { next: (snapshot: [QuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshot_class)\<AppModelType, DbModelType\>) =\> void; error?: (error: [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class)) =\> void; complete?: () =\> void; } | A single object containing `next` and `error` callbacks.                                                                                                     |
| converter    | [FirestoreDataConverter](https://firebase.google.com/docs/reference/js/firestore_.firestoredataconverter.md#firestoredataconverter_interface)\<DbModelType\>                                                                                                                                                                                     | An optional object that converts objects from Firestore before the onNext listener is invoked.                                                               |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/firestore_.unsubscribe.md#unsubscribe_interface)

An unsubscribe function that can be called to cancel the snapshot listener.

### onSnapshotResume(firestore, snapshotJson, options, observer, converter)

Attaches a listener for `DocumentSnapshot` events based on QuerySnapshot data generated by invoking [DocumentSnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshottojson) You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks. The listener can be cancelled by calling the function that is returned when `onSnapshot` is called.

NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.

**Signature:**  

    export declare function onSnapshotResume<AppModelType, DbModelType extends DocumentData>(firestore: Firestore, snapshotJson: object, options: SnapshotListenOptions, observer: {
        next: (snapshot: DocumentSnapshot<AppModelType, DbModelType>) => void;
        error?: (error: FirestoreError) => void;
        complete?: () => void;
    }, converter?: FirestoreDataConverter<DbModelType>): Unsubscribe;

#### Parameters

|  Parameter   |                                                                                                                                                                           Type                                                                                                                                                                            |                                                                              Description                                                                              |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| firestore    | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class)                                                                                                                                                                                                                                                        | The [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance to enable the listener for.                           |
| snapshotJson | object                                                                                                                                                                                                                                                                                                                                                    | A JSON object generated by invoking [DocumentSnapshot.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshottojson). |
| options      | [SnapshotListenOptions](https://firebase.google.com/docs/reference/js/firestore_.snapshotlistenoptions.md#snapshotlistenoptions_interface)                                                                                                                                                                                                                | Options controlling the listen behavior.                                                                                                                              |
| observer     | { next: (snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\>) =\> void; error?: (error: [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class)) =\> void; complete?: () =\> void; } | A single object containing `next` and `error` callbacks.                                                                                                              |
| converter    | [FirestoreDataConverter](https://firebase.google.com/docs/reference/js/firestore_.firestoredataconverter.md#firestoredataconverter_interface)\<DbModelType\>                                                                                                                                                                                              | An optional object that converts objects from Firestore before the onNext listener is invoked.                                                                        |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/firestore_.unsubscribe.md#unsubscribe_interface)

An unsubscribe function that can be called to cancel the snapshot listener.

### onSnapshotsInSync(firestore, observer)

Attaches a listener for a snapshots-in-sync event. The snapshots-in-sync event indicates that all listeners affected by a given change have fired, even if a single server-generated change affects multiple listeners.

NOTE: The snapshots-in-sync event only indicates that listeners are in sync with each other, but does not relate to whether those snapshots are in sync with the server. Use SnapshotMetadata in the individual listeners to determine if a snapshot is from the cache or the server.

**Signature:**  

    export declare function onSnapshotsInSync(firestore: Firestore, observer: {
        next?: (value: void) => void;
        error?: (error: FirestoreError) => void;
        complete?: () => void;
    }): Unsubscribe;

#### Parameters

| Parameter |                                                                                                  Type                                                                                                   |                       Description                        |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| firestore | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class)                                                                                                      | The instance of Firestore for synchronizing snapshots.   |
| observer  | { next?: (value: void) =\> void; error?: (error: [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class)) =\> void; complete?: () =\> void; } | A single object containing `next` and `error` callbacks. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/firestore_.unsubscribe.md#unsubscribe_interface)

An unsubscribe function that can be called to cancel the snapshot listener.

### onSnapshotsInSync(firestore, onSync)

Attaches a listener for a snapshots-in-sync event. The snapshots-in-sync event indicates that all listeners affected by a given change have fired, even if a single server-generated change affects multiple listeners.

NOTE: The snapshots-in-sync event only indicates that listeners are in sync with each other, but does not relate to whether those snapshots are in sync with the server. Use `SnapshotMetadata` in the individual listeners to determine if a snapshot is from the cache or the server.

**Signature:**  

    export declare function onSnapshotsInSync(firestore: Firestore, onSync: () => void): Unsubscribe;

#### Parameters

| Parameter |                                                Type                                                |                                      Description                                       |
|-----------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| firestore | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) | The `Firestore` instance for synchronizing snapshots.                                  |
| onSync    | () =\> void                                                                                        | A callback to be called every time all snapshot listeners are in sync with each other. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/firestore_.unsubscribe.md#unsubscribe_interface)

An unsubscribe function that can be called to cancel the snapshot listener.

### runTransaction(firestore, updateFunction, options)

Executes the given `updateFunction` and then attempts to commit the changes applied within the transaction. If any document read within the transaction has changed, Cloud Firestore retries the `updateFunction`. If it fails to commit after 5 attempts, the transaction fails.

The maximum number of writes allowed in a single transaction is 500.

**Signature:**  

    export declare function runTransaction<T>(firestore: Firestore, updateFunction: (transaction: Transaction) => Promise<T>, options?: TransactionOptions): Promise<T>;

#### Parameters

|   Parameter    |                                                                   Type                                                                   |                              Description                               |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| firestore      | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class)                                       | A reference to the Firestore database to run this transaction against. |
| updateFunction | (transaction: [Transaction](https://firebase.google.com/docs/reference/js/firestore_.transaction.md#transaction_class)) =\> Promise\<T\> | The function to execute within the transaction context.                |
| options        | [TransactionOptions](https://firebase.google.com/docs/reference/js/firestore_.transactionoptions.md#transactionoptions_interface)        | An options object to configure maximum number of attempts to commit.   |

**Returns:**

Promise\<T\>

If the transaction completed successfully or was explicitly aborted (the `updateFunction` returned a failed promise), the promise returned by the `updateFunction`is returned here. Otherwise, if the transaction failed, a rejected promise with the corresponding failure error is returned.

### setIndexConfiguration(firestore, configuration)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.
> | **Warning:** This API is now obsolete.
>
> Instead of creating cache indexes manually, consider using `enablePersistentCacheIndexAutoCreation()` to let the SDK decide whether to create cache indexes for queries running locally.

Configures indexing for local query execution. Any previous index configuration is overridden. The `Promise` resolves once the index configuration has been persisted.

The index entries themselves are created asynchronously. You can continue to use queries that require indexing even if the indices are not yet available. Query execution will automatically start using the index once the index entries have been written.

Indexes are only supported with IndexedDb persistence. If IndexedDb is not enabled, any index configuration is ignored.

**Signature:**  

    export declare function setIndexConfiguration(firestore: Firestore, configuration: IndexConfiguration): Promise<void>;

#### Parameters

|   Parameter   |                                                               Type                                                                |                                                                Description                                                                |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| firestore     | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class)                                | The [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance to configure indexes for. |
| configuration | [IndexConfiguration](https://firebase.google.com/docs/reference/js/firestore_.indexconfiguration.md#indexconfiguration_interface) | The index definition.                                                                                                                     |

**Returns:**

Promise\<void\>

A `Promise` that resolves once all indices are successfully configured.

#### Exceptions

FirestoreError if the JSON format is invalid.

### setIndexConfiguration(firestore, json)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.
> | **Warning:** This API is now obsolete.
>
> Instead of creating cache indexes manually, consider using `enablePersistentCacheIndexAutoCreation()` to let the SDK decide whether to create cache indexes for queries running locally.

Configures indexing for local query execution. Any previous index configuration is overridden. The `Promise` resolves once the index configuration has been persisted.

The index entries themselves are created asynchronously. You can continue to use queries that require indexing even if the indices are not yet available. Query execution will automatically start using the index once the index entries have been written.

Indexes are only supported with IndexedDb persistence. Invoke either `enableIndexedDbPersistence()` or `enableMultiTabIndexedDbPersistence()` before setting an index configuration. If IndexedDb is not enabled, any index configuration is ignored.

The method accepts the JSON format exported by the Firebase CLI (`firebase firestore:indexes`). If the JSON format is invalid, this method throws an error.

**Signature:**  

    export declare function setIndexConfiguration(firestore: Firestore, json: string): Promise<void>;

#### Parameters

| Parameter |                                                Type                                                |                                                                Description                                                                |
|-----------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| firestore | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) | The [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance to configure indexes for. |
| json      | string                                                                                             | The JSON format exported by the Firebase CLI.                                                                                             |

**Returns:**

Promise\<void\>

A `Promise` that resolves once all indices are successfully configured.

#### Exceptions

FirestoreError if the JSON format is invalid.

### terminate(firestore)

Terminates the provided [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance.

After calling `terminate()` only the `clearIndexedDbPersistence()` function may be used. Any other function will throw a `FirestoreError`.

To restart after termination, create a new instance of FirebaseFirestore with [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore).

Termination does not cancel any pending writes, and any promises that are awaiting a response from the server will not be resolved. If you have persistence enabled, the next time you start this instance, it will resume sending these writes to the server.
| **Note:** Under normal circumstances, calling `terminate()` is not required. This function is useful only when you want to force this instance to release all of its resources or in combination with `clearIndexedDbPersistence()` to ensure that all local state is destroyed between test runs.

**Signature:**  

    export declare function terminate(firestore: Firestore): Promise<void>;

#### Parameters

| Parameter |                                                Type                                                | Description |
|-----------|----------------------------------------------------------------------------------------------------|-------------|
| firestore | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) |             |

**Returns:**

Promise\<void\>

A `Promise` that is resolved when the instance has been successfully terminated.

### waitForPendingWrites(firestore)

Waits until all currently pending writes for the active user have been acknowledged by the backend.

The returned promise resolves immediately if there are no outstanding writes. Otherwise, the promise waits for all previously issued writes (including those written in a previous app session), but it does not wait for writes that were added after the function is called. If you want to wait for additional writes, call `waitForPendingWrites()` again.

Any outstanding `waitForPendingWrites()` promises are rejected during user changes.

**Signature:**  

    export declare function waitForPendingWrites(firestore: Firestore): Promise<void>;

#### Parameters

| Parameter |                                                Type                                                | Description |
|-----------|----------------------------------------------------------------------------------------------------|-------------|
| firestore | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) |             |

**Returns:**

Promise\<void\>

A `Promise` which resolves when all currently pending writes have been acknowledged by the backend.

### writeBatch(firestore)

Creates a write batch, used for performing multiple writes as a single atomic operation. The maximum number of writes allowed in a single [WriteBatch](https://firebase.google.com/docs/reference/js/firestore_.writebatch.md#writebatch_class) is 500.

Unlike transactions, write batches are persisted offline and therefore are preferable when you don't need to condition your writes on read data.

**Signature:**  

    export declare function writeBatch(firestore: Firestore): WriteBatch;

#### Parameters

| Parameter |                                                Type                                                | Description |
|-----------|----------------------------------------------------------------------------------------------------|-------------|
| firestore | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) |             |

**Returns:**

[WriteBatch](https://firebase.google.com/docs/reference/js/firestore_.writebatch.md#writebatch_class)

A [WriteBatch](https://firebase.google.com/docs/reference/js/firestore_.writebatch.md#writebatch_class) that can be used to atomically execute multiple writes.

## function()

### count()

Create an AggregateField object that can be used to compute the count of documents in the result set of a query.

**Signature:**  

    export declare function count(): AggregateField<number>;

**Returns:**

[AggregateField](https://firebase.google.com/docs/reference/js/firestore_.aggregatefield.md#aggregatefield_class)\<number\>

### deleteField()

Returns a sentinel for use with [updateDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#updatedoc_51a65e3) or [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad) with `{merge: true}` to mark a field for deletion.

**Signature:**  

    export declare function deleteField(): FieldValue;

**Returns:**

[FieldValue](https://firebase.google.com/docs/reference/js/firestore_.fieldvalue.md#fieldvalue_class)

### documentId()

Returns a special sentinel `FieldPath` to refer to the ID of a document. It can be used in queries to sort or filter by the document ID.

**Signature:**  

    export declare function documentId(): FieldPath;

**Returns:**

[FieldPath](https://firebase.google.com/docs/reference/js/firestore_.fieldpath.md#fieldpath_class)

### getFirestore()

Returns the existing default [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance that is associated with the default [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface). If no instance exists, initializes a new instance with default settings.

**Signature:**  

    export declare function getFirestore(): Firestore;

**Returns:**

[Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class)

The default [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance of the default app.

### memoryEagerGarbageCollector()

Creates an instance of `MemoryEagerGarbageCollector`. This is also the default garbage collector unless it is explicitly specified otherwise.

**Signature:**  

    export declare function memoryEagerGarbageCollector(): MemoryEagerGarbageCollector;

**Returns:**

[MemoryEagerGarbageCollector](https://firebase.google.com/docs/reference/js/firestore_.memoryeagergarbagecollector.md#memoryeagergarbagecollector_interface)

### persistentMultipleTabManager()

Creates an instance of `PersistentMultipleTabManager`.

**Signature:**  

    export declare function persistentMultipleTabManager(): PersistentMultipleTabManager;

**Returns:**

[PersistentMultipleTabManager](https://firebase.google.com/docs/reference/js/firestore_.persistentmultipletabmanager.md#persistentmultipletabmanager_interface)

### serverTimestamp()

Returns a sentinel used with [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad) or [updateDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#updatedoc_51a65e3) to include a server-generated timestamp in the written data.

**Signature:**  

    export declare function serverTimestamp(): FieldValue;

**Returns:**

[FieldValue](https://firebase.google.com/docs/reference/js/firestore_.fieldvalue.md#fieldvalue_class)

## function(databaseId, ...)

### getFirestore(databaseId)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Returns the existing named [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance that is associated with the default [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface). If no instance exists, initializes a new instance with default settings.

**Signature:**  

    export declare function getFirestore(databaseId: string): Firestore;

#### Parameters

| Parameter  |  Type  |        Description        |
|------------|--------|---------------------------|
| databaseId | string | The name of the database. |

**Returns:**

[Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class)

The named [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance of the default app.

## function(elements, ...)

### arrayRemove(elements)

Returns a special value that can be used with [setDoc()](https://firebase.google.com/docs/reference/js/firestore_.md#setdoc_ee215ad) or that tells the server to remove the given elements from any array value that already exists on the server. All instances of each element specified will be removed from the array. If the field being modified is not already an array it will be overwritten with an empty array.

**Signature:**  

    export declare function arrayRemove(...elements: unknown[]): FieldValue;

#### Parameters

| Parameter |    Type     |              Description               |
|-----------|-------------|----------------------------------------|
| elements  | unknown\[\] | The elements to remove from the array. |

**Returns:**

[FieldValue](https://firebase.google.com/docs/reference/js/firestore_.fieldvalue.md#fieldvalue_class)

The `FieldValue` sentinel for use in a call to `setDoc()` or `updateDoc()`

### arrayUnion(elements)

Returns a special value that can be used with [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad) or [updateDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#updatedoc_51a65e3) that tells the server to union the given elements with any array value that already exists on the server. Each specified element that doesn't already exist in the array will be added to the end. If the field being modified is not already an array it will be overwritten with an array containing exactly the specified elements.

**Signature:**  

    export declare function arrayUnion(...elements: unknown[]): FieldValue;

#### Parameters

| Parameter |    Type     |              Description              |
|-----------|-------------|---------------------------------------|
| elements  | unknown\[\] | The elements to union into the array. |

**Returns:**

[FieldValue](https://firebase.google.com/docs/reference/js/firestore_.fieldvalue.md#fieldvalue_class)

The `FieldValue` sentinel for use in a call to `setDoc()` or `updateDoc()`.

## function(field, ...)

### average(field)

Create an AggregateField object that can be used to compute the average of a specified field over a range of documents in the result set of a query.

**Signature:**  

    export declare function average(field: string | FieldPath): AggregateField<number | null>;

#### Parameters

| Parameter |                                                     Type                                                     |                      Description                      |
|-----------|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| field     | string \| [FieldPath](https://firebase.google.com/docs/reference/js/firestore_.fieldpath.md#fieldpath_class) | Specifies the field to average across the result set. |

**Returns:**

[AggregateField](https://firebase.google.com/docs/reference/js/firestore_.aggregatefield.md#aggregatefield_class)\<number \| null\>

### sum(field)

Create an AggregateField object that can be used to compute the sum of a specified field over a range of documents in the result set of a query.

**Signature:**  

    export declare function sum(field: string | FieldPath): AggregateField<number>;

#### Parameters

| Parameter |                                                     Type                                                     |                    Description                    |
|-----------|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| field     | string \| [FieldPath](https://firebase.google.com/docs/reference/js/firestore_.fieldpath.md#fieldpath_class) | Specifies the field to sum across the result set. |

**Returns:**

[AggregateField](https://firebase.google.com/docs/reference/js/firestore_.aggregatefield.md#aggregatefield_class)\<number\>

## function(fieldPath, ...)

### orderBy(fieldPath, directionStr)

Creates a [QueryOrderByConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryorderbyconstraint.md#queryorderbyconstraint_class) that sorts the query result by the specified field, optionally in descending order instead of ascending.
| **Note:** Documents that do not contain the specified field will not be present in the query result.

**Signature:**  

    export declare function orderBy(fieldPath: string | FieldPath, directionStr?: OrderByDirection): QueryOrderByConstraint;

#### Parameters

|  Parameter   |                                                     Type                                                     |                                         Description                                         |
|--------------|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| fieldPath    | string \| [FieldPath](https://firebase.google.com/docs/reference/js/firestore_.fieldpath.md#fieldpath_class) | The field to sort by.                                                                       |
| directionStr | [OrderByDirection](https://firebase.google.com/docs/reference/js/firestore_.md#orderbydirection)             | Optional direction to sort by ('asc' or 'desc'). If not specified, order will be ascending. |

**Returns:**

[QueryOrderByConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryorderbyconstraint.md#queryorderbyconstraint_class)

The created [QueryOrderByConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryorderbyconstraint.md#queryorderbyconstraint_class).

### where(fieldPath, opStr, value)

Creates a [QueryFieldFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryfieldfilterconstraint.md#queryfieldfilterconstraint_class) that enforces that documents must contain the specified field and that the value should satisfy the relation constraint provided.

**Signature:**  

    export declare function where(fieldPath: string | FieldPath, opStr: WhereFilterOp, value: unknown): QueryFieldFilterConstraint;

#### Parameters

| Parameter |                                                     Type                                                     |                                 Description                                  |
|-----------|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| fieldPath | string \| [FieldPath](https://firebase.google.com/docs/reference/js/firestore_.fieldpath.md#fieldpath_class) | The path to compare                                                          |
| opStr     | [WhereFilterOp](https://firebase.google.com/docs/reference/js/firestore_.md#wherefilterop)                   | The operation string (e.g "\&lt;", "\&lt;=", "==", "\&lt;", "\&lt;=", "!="). |
| value     | unknown                                                                                                      | The value for comparison                                                     |

**Returns:**

[QueryFieldFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryfieldfilterconstraint.md#queryfieldfilterconstraint_class)

The created [QueryFieldFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryfieldfilterconstraint.md#queryfieldfilterconstraint_class).

## function(fieldValues, ...)

### endAt(fieldValues)

Creates a [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class) that modifies the result set to end at the provided fields relative to the order of the query. The order of the field values must match the order of the order by clauses of the query.

**Signature:**  

    export declare function endAt(...fieldValues: unknown[]): QueryEndAtConstraint;

#### Parameters

|  Parameter  |    Type     |                               Description                                |
|-------------|-------------|--------------------------------------------------------------------------|
| fieldValues | unknown\[\] | The field values to end this query at, in order of the query's order by. |

**Returns:**

[QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class)

A [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class) to pass to `query()`

### endBefore(fieldValues)

Creates a [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class) that modifies the result set to end before the provided fields relative to the order of the query. The order of the field values must match the order of the order by clauses of the query.

**Signature:**  

    export declare function endBefore(...fieldValues: unknown[]): QueryEndAtConstraint;

#### Parameters

|  Parameter  |    Type     |                                 Description                                  |
|-------------|-------------|------------------------------------------------------------------------------|
| fieldValues | unknown\[\] | The field values to end this query before, in order of the query's order by. |

**Returns:**

[QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class)

A [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class) to pass to `query()`

### startAfter(fieldValues)

Creates a [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class) that modifies the result set to start after the provided fields relative to the order of the query. The order of the field values must match the order of the order by clauses of the query.

**Signature:**  

    export declare function startAfter(...fieldValues: unknown[]): QueryStartAtConstraint;

#### Parameters

|  Parameter  |    Type     |                                  Description                                  |
|-------------|-------------|-------------------------------------------------------------------------------|
| fieldValues | unknown\[\] | The field values to start this query after, in order of the query's order by. |

**Returns:**

[QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class)

A [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class) to pass to `query()`

### startAt(fieldValues)

Creates a [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class) that modifies the result set to start at the provided fields relative to the order of the query. The order of the field values must match the order of the order by clauses of the query.

**Signature:**  

    export declare function startAt(...fieldValues: unknown[]): QueryStartAtConstraint;

#### Parameters

|  Parameter  |    Type     |                                Description                                 |
|-------------|-------------|----------------------------------------------------------------------------|
| fieldValues | unknown\[\] | The field values to start this query at, in order of the query's order by. |

**Returns:**

[QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class)

A [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class) to pass to `query()`.

## function(indexManager, ...)

### deleteAllPersistentCacheIndexes(indexManager)

Removes all persistent cache indexes.

Please note this function will also deletes indexes generated by `setIndexConfiguration()`, which is deprecated.

**Signature:**  

    export declare function deleteAllPersistentCacheIndexes(indexManager: PersistentCacheIndexManager): void;

#### Parameters

|  Parameter   |                                                                           Type                                                                           | Description |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| indexManager | [PersistentCacheIndexManager](https://firebase.google.com/docs/reference/js/firestore_.persistentcacheindexmanager.md#persistentcacheindexmanager_class) |             |

**Returns:**

void

### disablePersistentCacheIndexAutoCreation(indexManager)

Stops creating persistent cache indexes automatically for local query execution. The indexes which have been created by calling `enablePersistentCacheIndexAutoCreation()` still take effect.

**Signature:**  

    export declare function disablePersistentCacheIndexAutoCreation(indexManager: PersistentCacheIndexManager): void;

#### Parameters

|  Parameter   |                                                                           Type                                                                           | Description |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| indexManager | [PersistentCacheIndexManager](https://firebase.google.com/docs/reference/js/firestore_.persistentcacheindexmanager.md#persistentcacheindexmanager_class) |             |

**Returns:**

void

### enablePersistentCacheIndexAutoCreation(indexManager)

Enables the SDK to create persistent cache indexes automatically for local query execution when the SDK believes cache indexes can help improve performance.

This feature is disabled by default.

**Signature:**  

    export declare function enablePersistentCacheIndexAutoCreation(indexManager: PersistentCacheIndexManager): void;

#### Parameters

|  Parameter   |                                                                           Type                                                                           | Description |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| indexManager | [PersistentCacheIndexManager](https://firebase.google.com/docs/reference/js/firestore_.persistentcacheindexmanager.md#persistentcacheindexmanager_class) |             |

**Returns:**

void

## function(left, ...)

### aggregateFieldEqual(left, right)

Compares two 'AggregateField\` instances for equality.

**Signature:**  

    export declare function aggregateFieldEqual(left: AggregateField<unknown>, right: AggregateField<unknown>): boolean;

#### Parameters

| Parameter |                                                             Type                                                             |                 Description                 |
|-----------|------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| left      | [AggregateField](https://firebase.google.com/docs/reference/js/firestore_.aggregatefield.md#aggregatefield_class)\<unknown\> | Compare this AggregateField to the `right`. |
| right     | [AggregateField](https://firebase.google.com/docs/reference/js/firestore_.aggregatefield.md#aggregatefield_class)\<unknown\> | Compare this AggregateField to the `left`.  |

**Returns:**

boolean

### aggregateQuerySnapshotEqual(left, right)

Compares two `AggregateQuerySnapshot` instances for equality.

Two `AggregateQuerySnapshot` instances are considered "equal" if they have underlying queries that compare equal, and the same data.

**Signature:**  

    export declare function aggregateQuerySnapshotEqual<AggregateSpecType extends AggregateSpec, AppModelType, DbModelType extends DocumentData>(left: AggregateQuerySnapshot<AggregateSpecType, AppModelType, DbModelType>, right: AggregateQuerySnapshot<AggregateSpecType, AppModelType, DbModelType>): boolean;

#### Parameters

| Parameter |                                                                                           Type                                                                                            |                   Description                   |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| left      | [AggregateQuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.aggregatequerysnapshot.md#aggregatequerysnapshot_class)\<AggregateSpecType, AppModelType, DbModelType\> | The first `AggregateQuerySnapshot` to compare.  |
| right     | [AggregateQuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.aggregatequerysnapshot.md#aggregatequerysnapshot_class)\<AggregateSpecType, AppModelType, DbModelType\> | The second `AggregateQuerySnapshot` to compare. |

**Returns:**

boolean

`true` if the objects are "equal", as defined above, or `false` otherwise.

### queryEqual(left, right)

Returns true if the provided queries point to the same collection and apply the same constraints.

**Signature:**  

    export declare function queryEqual<AppModelType, DbModelType extends DocumentData>(left: Query<AppModelType, DbModelType>, right: Query<AppModelType, DbModelType>): boolean;

#### Parameters

| Parameter |                                                        Type                                                         |      Description      |
|-----------|---------------------------------------------------------------------------------------------------------------------|-----------------------|
| left      | [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class)\<AppModelType, DbModelType\> | A `Query` to compare. |
| right     | [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class)\<AppModelType, DbModelType\> | A `Query` to compare. |

**Returns:**

boolean

true if the references point to the same location in the same Firestore database.

### refEqual(left, right)

Returns true if the provided references are equal.

**Signature:**  

    export declare function refEqual<AppModelType, DbModelType extends DocumentData>(left: DocumentReference<AppModelType, DbModelType> | CollectionReference<AppModelType, DbModelType>, right: DocumentReference<AppModelType, DbModelType> | CollectionReference<AppModelType, DbModelType>): boolean;

#### Parameters

| Parameter |                                                                                                                                                           Type                                                                                                                                                           |       Description       |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| left      | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> \| [CollectionReference](https://firebase.google.com/docs/reference/js/firestore_.collectionreference.md#collectionreference_class)\<AppModelType, DbModelType\> | A reference to compare. |
| right     | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> \| [CollectionReference](https://firebase.google.com/docs/reference/js/firestore_.collectionreference.md#collectionreference_class)\<AppModelType, DbModelType\> | A reference to compare. |

**Returns:**

boolean

true if the references point to the same location in the same Firestore database.

### snapshotEqual(left, right)

Returns true if the provided snapshots are equal.

**Signature:**  

    export declare function snapshotEqual<AppModelType, DbModelType extends DocumentData>(left: DocumentSnapshot<AppModelType, DbModelType> | QuerySnapshot<AppModelType, DbModelType>, right: DocumentSnapshot<AppModelType, DbModelType> | QuerySnapshot<AppModelType, DbModelType>): boolean;

#### Parameters

| Parameter |                                                                                                                                                Type                                                                                                                                                 |      Description       |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| left      | [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\> \| [QuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshot_class)\<AppModelType, DbModelType\> | A snapshot to compare. |
| right     | [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\> \| [QuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshot_class)\<AppModelType, DbModelType\> | A snapshot to compare. |

**Returns:**

boolean

true if the snapshots are equal.

## function(limit, ...)

### limit(limit)

Creates a [QueryLimitConstraint](https://firebase.google.com/docs/reference/js/firestore_.querylimitconstraint.md#querylimitconstraint_class) that only returns the first matching documents.

**Signature:**  

    export declare function limit(limit: number): QueryLimitConstraint;

#### Parameters

| Parameter |  Type  |              Description               |
|-----------|--------|----------------------------------------|
| limit     | number | The maximum number of items to return. |

**Returns:**

[QueryLimitConstraint](https://firebase.google.com/docs/reference/js/firestore_.querylimitconstraint.md#querylimitconstraint_class)

The created [QueryLimitConstraint](https://firebase.google.com/docs/reference/js/firestore_.querylimitconstraint.md#querylimitconstraint_class).

### limitToLast(limit)

Creates a [QueryLimitConstraint](https://firebase.google.com/docs/reference/js/firestore_.querylimitconstraint.md#querylimitconstraint_class) that only returns the last matching documents.

You must specify at least one `orderBy` clause for `limitToLast` queries, otherwise an exception will be thrown during execution.

**Signature:**  

    export declare function limitToLast(limit: number): QueryLimitConstraint;

#### Parameters

| Parameter |  Type  |              Description               |
|-----------|--------|----------------------------------------|
| limit     | number | The maximum number of items to return. |

**Returns:**

[QueryLimitConstraint](https://firebase.google.com/docs/reference/js/firestore_.querylimitconstraint.md#querylimitconstraint_class)

The created [QueryLimitConstraint](https://firebase.google.com/docs/reference/js/firestore_.querylimitconstraint.md#querylimitconstraint_class).

## function(logLevel, ...)

### setLogLevel(logLevel)

Sets the verbosity of Cloud Firestore logs (debug, error, or silent).

**Signature:**  

    export declare function setLogLevel(logLevel: LogLevel): void;

#### Parameters

| Parameter |   Type   |                                                                                                             Description                                                                                                              |
|-----------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| logLevel  | LogLevel | The verbosity you set for activity and error logging. Can be any of the following values: - `debug` for the most verbose logging level, primarily for debugging. - `error` to log errors only. - `silent`` to turn off logging.` ` ` |

**Returns:**

void

## function(n, ...)

### increment(n)

Returns a special value that can be used with [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad) or [updateDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#updatedoc_51a65e3) that tells the server to increment the field's current value by the given value.

If either the operand or the current field value uses floating point precision, all arithmetic follows IEEE 754 semantics. If both values are integers, values outside of JavaScript's safe number range (`Number.MIN_SAFE_INTEGER` to `Number.MAX_SAFE_INTEGER`) are also subject to precision loss. Furthermore, once processed by the Firestore backend, all integer operations are capped between -2\^63 and 2\^63-1.

If the current field value is not of type `number`, or if the field does not yet exist, the transformation sets the field to the given value.

**Signature:**  

    export declare function increment(n: number): FieldValue;

#### Parameters

| Parameter |  Type  |        Description         |
|-----------|--------|----------------------------|
| n         | number | The value to increment by. |

**Returns:**

[FieldValue](https://firebase.google.com/docs/reference/js/firestore_.fieldvalue.md#fieldvalue_class)

The `FieldValue` sentinel for use in a call to `setDoc()` or `updateDoc()`

## function(query, ...)

### getAggregateFromServer(query, aggregateSpec)

Calculates the specified aggregations over the documents in the result set of the given query without actually downloading the documents.

Using this function to perform aggregations is efficient because only the final aggregation values, not the documents' data, are downloaded. This function can perform aggregations of the documents in cases where the result set is prohibitively large to download entirely (thousands of documents).

The result received from the server is presented, unaltered, without considering any local state. That is, documents in the local cache are not taken into consideration, neither are local modifications not yet synchronized with the server. Previously-downloaded results, if any, are not used. Every invocation of this function necessarily involves a round trip to the server.

**Signature:**  

    export declare function getAggregateFromServer<AggregateSpecType extends AggregateSpec, AppModelType, DbModelType extends DocumentData>(query: Query<AppModelType, DbModelType>, aggregateSpec: AggregateSpecType): Promise<AggregateQuerySnapshot<AggregateSpecType, AppModelType, DbModelType>>;

#### Parameters

|   Parameter   |                                                        Type                                                         |                                                                                             Description                                                                                             |
|---------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| query         | [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class)\<AppModelType, DbModelType\> | The query whose result set is aggregated over.                                                                                                                                                      |
| aggregateSpec | AggregateSpecType                                                                                                   | An `AggregateSpec` object that specifies the aggregates to perform over the result set. The AggregateSpec specifies aliases for each aggregate, which can be used to retrieve the aggregate result. |

**Returns:**

Promise\<[AggregateQuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.aggregatequerysnapshot.md#aggregatequerysnapshot_class)\<AggregateSpecType, AppModelType, DbModelType\>\>

### Example

    const aggregateSnapshot = await getAggregateFromServer(query, {
      countOfDocs: count(),
      totalHours: sum('hours'),
      averageScore: average('score')
    });

    const countOfDocs: number = aggregateSnapshot.data().countOfDocs;
    const totalHours: number = aggregateSnapshot.data().totalHours;
    const averageScore: number | null = aggregateSnapshot.data().averageScore;

### getCountFromServer(query)

Calculates the number of documents in the result set of the given query without actually downloading the documents.

Using this function to count the documents is efficient because only the final count, not the documents' data, is downloaded. This function can count the documents in cases where the result set is prohibitively large to download entirely (thousands of documents).

The result received from the server is presented, unaltered, without considering any local state. That is, documents in the local cache are not taken into consideration, neither are local modifications not yet synchronized with the server. Previously-downloaded results, if any, are not used. Every invocation of this function necessarily involves a round trip to the server.

**Signature:**  

    export declare function getCountFromServer<AppModelType, DbModelType extends DocumentData>(query: Query<AppModelType, DbModelType>): Promise<AggregateQuerySnapshot<{
        count: AggregateField<number>;
    }, AppModelType, DbModelType>>;

#### Parameters

| Parameter |                                                        Type                                                         |                  Description                   |
|-----------|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| query     | [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class)\<AppModelType, DbModelType\> | The query whose result set size is calculated. |

**Returns:**

Promise\<[AggregateQuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.aggregatequerysnapshot.md#aggregatequerysnapshot_class)\<{ count: [AggregateField](https://firebase.google.com/docs/reference/js/firestore_.aggregatefield.md#aggregatefield_class)\<number\>; }, AppModelType, DbModelType\>\>

A Promise that will be resolved with the count; the count can be retrieved from `snapshot.data().count`, where `snapshot` is the `AggregateQuerySnapshot` to which the returned Promise resolves.

### getDocs(query)

Executes the query and returns the results as a `QuerySnapshot`.
| **Note:** `getDocs()` attempts to provide up-to-date data when possible by waiting for data from the server, but it may return cached data or fail if you are offline and the server cannot be reached. To specify this behavior, invoke [getDocsFromCache()](https://firebase.google.com/docs/reference/js/firestore_.md#getdocsfromcache_4e56953) or [getDocsFromServer()](https://firebase.google.com/docs/reference/js/firestore_.md#getdocsfromserver_4e56953).

**Signature:**  

    export declare function getDocs<AppModelType, DbModelType extends DocumentData>(query: Query<AppModelType, DbModelType>): Promise<QuerySnapshot<AppModelType, DbModelType>>;

#### Parameters

| Parameter |                                                        Type                                                         | Description |
|-----------|---------------------------------------------------------------------------------------------------------------------|-------------|
| query     | [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class)\<AppModelType, DbModelType\> |             |

**Returns:**

Promise\<[QuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshot_class)\<AppModelType, DbModelType\>\>

A `Promise` that will be resolved with the results of the query.

### getDocsFromCache(query)

Executes the query and returns the results as a `QuerySnapshot` from cache. Returns an empty result set if no documents matching the query are currently cached.

**Signature:**  

    export declare function getDocsFromCache<AppModelType, DbModelType extends DocumentData>(query: Query<AppModelType, DbModelType>): Promise<QuerySnapshot<AppModelType, DbModelType>>;

#### Parameters

| Parameter |                                                        Type                                                         | Description |
|-----------|---------------------------------------------------------------------------------------------------------------------|-------------|
| query     | [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class)\<AppModelType, DbModelType\> |             |

**Returns:**

Promise\<[QuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshot_class)\<AppModelType, DbModelType\>\>

A `Promise` that will be resolved with the results of the query.

### getDocsFromServer(query)

Executes the query and returns the results as a `QuerySnapshot` from the server. Returns an error if the network is not available.

**Signature:**  

    export declare function getDocsFromServer<AppModelType, DbModelType extends DocumentData>(query: Query<AppModelType, DbModelType>): Promise<QuerySnapshot<AppModelType, DbModelType>>;

#### Parameters

| Parameter |                                                        Type                                                         | Description |
|-----------|---------------------------------------------------------------------------------------------------------------------|-------------|
| query     | [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class)\<AppModelType, DbModelType\> |             |

**Returns:**

Promise\<[QuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshot_class)\<AppModelType, DbModelType\>\>

A `Promise` that will be resolved with the results of the query.

### onSnapshot(query, observer)

Attaches a listener for `QuerySnapshot` events. You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks. The listener can be cancelled by calling the function that is returned when `onSnapshot` is called.

NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.

**Signature:**  

    export declare function onSnapshot<AppModelType, DbModelType extends DocumentData>(query: Query<AppModelType, DbModelType>, observer: {
        next?: (snapshot: QuerySnapshot<AppModelType, DbModelType>) => void;
        error?: (error: FirestoreError) => void;
        complete?: () => void;
    }): Unsubscribe;

#### Parameters

| Parameter |                                                                                                                                                                       Type                                                                                                                                                                        |                       Description                        |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| query     | [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class)\<AppModelType, DbModelType\>                                                                                                                                                                                                                               | The query to listen to.                                  |
| observer  | { next?: (snapshot: [QuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshot_class)\<AppModelType, DbModelType\>) =\> void; error?: (error: [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class)) =\> void; complete?: () =\> void; } | A single object containing `next` and `error` callbacks. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/firestore_.unsubscribe.md#unsubscribe_interface)

An unsubscribe function that can be called to cancel the snapshot listener.

### onSnapshot(query, options, observer)

Attaches a listener for `QuerySnapshot` events. You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks. The listener can be cancelled by calling the function that is returned when `onSnapshot` is called.

NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.

**Signature:**  

    export declare function onSnapshot<AppModelType, DbModelType extends DocumentData>(query: Query<AppModelType, DbModelType>, options: SnapshotListenOptions, observer: {
        next?: (snapshot: QuerySnapshot<AppModelType, DbModelType>) => void;
        error?: (error: FirestoreError) => void;
        complete?: () => void;
    }): Unsubscribe;

#### Parameters

| Parameter |                                                                                                                                                                       Type                                                                                                                                                                        |                       Description                        |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| query     | [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class)\<AppModelType, DbModelType\>                                                                                                                                                                                                                               | The query to listen to.                                  |
| options   | [SnapshotListenOptions](https://firebase.google.com/docs/reference/js/firestore_.snapshotlistenoptions.md#snapshotlistenoptions_interface)                                                                                                                                                                                                        | Options controlling the listen behavior.                 |
| observer  | { next?: (snapshot: [QuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshot_class)\<AppModelType, DbModelType\>) =\> void; error?: (error: [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class)) =\> void; complete?: () =\> void; } | A single object containing `next` and `error` callbacks. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/firestore_.unsubscribe.md#unsubscribe_interface)

An unsubscribe function that can be called to cancel the snapshot listener.

### onSnapshot(query, onNext, onError, onCompletion)

Attaches a listener for `QuerySnapshot` events. You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks. The listener can be cancelled by calling the function that is returned when `onSnapshot` is called.

NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.

**Signature:**  

    export declare function onSnapshot<AppModelType, DbModelType extends DocumentData>(query: Query<AppModelType, DbModelType>, onNext: (snapshot: QuerySnapshot<AppModelType, DbModelType>) => void, onError?: (error: FirestoreError) => void, onCompletion?: () => void): Unsubscribe;

#### Parameters

|  Parameter   |                                                                               Type                                                                               |                                          Description                                          |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| query        | [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class)\<AppModelType, DbModelType\>                                              | The query to listen to.                                                                       |
| onNext       | (snapshot: [QuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshot_class)\<AppModelType, DbModelType\>) =\> void | A callback to be called every time a new `QuerySnapshot` is available.                        |
| onError      | (error: [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class)) =\> void                              | A callback to be called if the listen fails or is cancelled. No further callbacks will occur. |
| onCompletion | () =\> void                                                                                                                                                      | Can be provided, but will not be called since streams are never ending.                       |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/firestore_.unsubscribe.md#unsubscribe_interface)

An unsubscribe function that can be called to cancel the snapshot listener.

### onSnapshot(query, options, onNext, onError, onCompletion)

Attaches a listener for `QuerySnapshot` events. You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks. The listener can be cancelled by calling the function that is returned when `onSnapshot` is called.

NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.

**Signature:**  

    export declare function onSnapshot<AppModelType, DbModelType extends DocumentData>(query: Query<AppModelType, DbModelType>, options: SnapshotListenOptions, onNext: (snapshot: QuerySnapshot<AppModelType, DbModelType>) => void, onError?: (error: FirestoreError) => void, onCompletion?: () => void): Unsubscribe;

#### Parameters

|  Parameter   |                                                                               Type                                                                               |                                          Description                                          |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| query        | [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class)\<AppModelType, DbModelType\>                                              | The query to listen to.                                                                       |
| options      | [SnapshotListenOptions](https://firebase.google.com/docs/reference/js/firestore_.snapshotlistenoptions.md#snapshotlistenoptions_interface)                       | Options controlling the listen behavior.                                                      |
| onNext       | (snapshot: [QuerySnapshot](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshot_class)\<AppModelType, DbModelType\>) =\> void | A callback to be called every time a new `QuerySnapshot` is available.                        |
| onError      | (error: [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class)) =\> void                              | A callback to be called if the listen fails or is cancelled. No further callbacks will occur. |
| onCompletion | () =\> void                                                                                                                                                      | Can be provided, but will not be called since streams are never ending.                       |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/firestore_.unsubscribe.md#unsubscribe_interface)

An unsubscribe function that can be called to cancel the snapshot listener.

### query(query, compositeFilter, queryConstraints)

Creates a new immutable instance of [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class) that is extended to also include additional query constraints.

**Signature:**  

    export declare function query<AppModelType, DbModelType extends DocumentData>(query: Query<AppModelType, DbModelType>, compositeFilter: QueryCompositeFilterConstraint, ...queryConstraints: QueryNonFilterConstraint[]): Query<AppModelType, DbModelType>;

#### Parameters

|    Parameter     |                                                                               Type                                                                                |                                                                                                                                                                                                                                                            Description                                                                                                                                                                                                                                                             |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| query            | [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class)\<AppModelType, DbModelType\>                                               | The [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class) instance to use as a base for the new constraints.                                                                                                                                                                                                                                                                                                                                                                                      |
| compositeFilter  | [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class) | The [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class) to apply. Create [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class) using [and()](https://firebase.google.com/docs/reference/js/firestore_.md#and_e72c712) or [or()](https://firebase.google.com/docs/reference/js/firestore_.md#or_e72c712). |
| queryConstraints | [QueryNonFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.md#querynonfilterconstraint)\[\]                                              | Additional [QueryNonFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.md#querynonfilterconstraint)s to apply (e.g. [orderBy()](https://firebase.google.com/docs/reference/js/firestore_.md#orderby_006d61f), [limit()](https://firebase.google.com/docs/reference/js/firestore_.md#limit_ec46c78)).                                                                                                                                                                                                       |

**Returns:**

[Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class)\<AppModelType, DbModelType\>

#### Exceptions

if any of the provided query constraints cannot be combined with the existing or new constraints.

### query(query, queryConstraints)

Creates a new immutable instance of [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class) that is extended to also include additional query constraints.

**Signature:**  

    export declare function query<AppModelType, DbModelType extends DocumentData>(query: Query<AppModelType, DbModelType>, ...queryConstraints: QueryConstraint[]): Query<AppModelType, DbModelType>;

#### Parameters

|    Parameter     |                                                           Type                                                           |                                                                  Description                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| query            | [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class)\<AppModelType, DbModelType\>      | The [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class) instance to use as a base for the new constraints. |
| queryConstraints | [QueryConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryconstraint.md#queryconstraint_class)\[\] | The list of [QueryConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryconstraint.md#queryconstraint_class)s to apply.   |

**Returns:**

[Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class)\<AppModelType, DbModelType\>

#### Exceptions

if any of the provided query constraints cannot be combined with the existing or new constraints.

## function(queryConstraints, ...)

### and(queryConstraints)

Creates a new [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class) that is a conjunction of the given filter constraints. A conjunction filter includes a document if it satisfies all of the given filters.

**Signature:**  

    export declare function and(...queryConstraints: QueryFilterConstraint[]): QueryCompositeFilterConstraint;

#### Parameters

|    Parameter     |                                                      Type                                                      |                                                                                                                                                                                                                          Description                                                                                                                                                                                                                           |
|------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| queryConstraints | [QueryFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.md#queryfilterconstraint)\[\] | Optional. The list of [QueryFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.md#queryfilterconstraint)s to perform a conjunction for. These must be created with calls to [where()](https://firebase.google.com/docs/reference/js/firestore_.md#where_0fae4bf), [or()](https://firebase.google.com/docs/reference/js/firestore_.md#or_e72c712), or [and()](https://firebase.google.com/docs/reference/js/firestore_.md#and_e72c712). |

**Returns:**

[QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class)

The newly created [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class).

### or(queryConstraints)

Creates a new [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class) that is a disjunction of the given filter constraints. A disjunction filter includes a document if it satisfies any of the given filters.

**Signature:**  

    export declare function or(...queryConstraints: QueryFilterConstraint[]): QueryCompositeFilterConstraint;

#### Parameters

|    Parameter     |                                                      Type                                                      |                                                                                                                                                                                                                          Description                                                                                                                                                                                                                           |
|------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| queryConstraints | [QueryFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.md#queryfilterconstraint)\[\] | Optional. The list of [QueryFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.md#queryfilterconstraint)s to perform a disjunction for. These must be created with calls to [where()](https://firebase.google.com/docs/reference/js/firestore_.md#where_0fae4bf), [or()](https://firebase.google.com/docs/reference/js/firestore_.md#or_e72c712), or [and()](https://firebase.google.com/docs/reference/js/firestore_.md#and_e72c712). |

**Returns:**

[QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class)

The newly created [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class).

## function(reference, ...)

### addDoc(reference, data)

Add a new document to specified `CollectionReference` with the given data, assigning it a document ID automatically.

**Signature:**  

    export declare function addDoc<AppModelType, DbModelType extends DocumentData>(reference: CollectionReference<AppModelType, DbModelType>, data: WithFieldValue<AppModelType>): Promise<DocumentReference<AppModelType, DbModelType>>;

#### Parameters

| Parameter |                                                                             Type                                                                              |                      Description                       |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| reference | [CollectionReference](https://firebase.google.com/docs/reference/js/firestore_.collectionreference.md#collectionreference_class)\<AppModelType, DbModelType\> | A reference to the collection to add this document to. |
| data      | [WithFieldValue](https://firebase.google.com/docs/reference/js/firestore_.md#withfieldvalue)\<AppModelType\>                                                  | An Object containing the data for the new document.    |

**Returns:**

Promise\<[DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class)\<AppModelType, DbModelType\>\>

A `Promise` resolved with a `DocumentReference` pointing to the newly created document after it has been written to the backend (Note that it won't resolve while you're offline).

### collection(reference, path, pathSegments)

Gets a `CollectionReference` instance that refers to a subcollection of `reference` at the specified relative path.

**Signature:**  

    export declare function collection<AppModelType, DbModelType extends DocumentData>(reference: CollectionReference<AppModelType, DbModelType>, path: string, ...pathSegments: string[]): CollectionReference<DocumentData, DocumentData>;

#### Parameters

|  Parameter   |                                                                             Type                                                                              |                            Description                            |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| reference    | [CollectionReference](https://firebase.google.com/docs/reference/js/firestore_.collectionreference.md#collectionreference_class)\<AppModelType, DbModelType\> | A reference to a collection.                                      |
| path         | string                                                                                                                                                        | A slash-separated path to a collection.                           |
| pathSegments | string\[\]                                                                                                                                                    | Additional path segments to apply relative to the first argument. |

**Returns:**

[CollectionReference](https://firebase.google.com/docs/reference/js/firestore_.collectionreference.md#collectionreference_class)\<[DocumentData](https://firebase.google.com/docs/reference/js/firestore_.documentdata.md#documentdata_interface), [DocumentData](https://firebase.google.com/docs/reference/js/firestore_.documentdata.md#documentdata_interface)\>

The `CollectionReference` instance.

#### Exceptions

If the final path has an even number of segments and does not point to a collection.

### collection(reference, path, pathSegments)

Gets a `CollectionReference` instance that refers to a subcollection of `reference` at the specified relative path.

**Signature:**  

    export declare function collection<AppModelType, DbModelType extends DocumentData>(reference: DocumentReference<AppModelType, DbModelType>, path: string, ...pathSegments: string[]): CollectionReference<DocumentData, DocumentData>;

#### Parameters

|  Parameter   |                                                                          Type                                                                           |                                  Description                                  |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| reference    | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to a Firestore document.                                          |
| path         | string                                                                                                                                                  | A slash-separated path to a collection.                                       |
| pathSegments | string\[\]                                                                                                                                              | Additional path segments that will be applied relative to the first argument. |

**Returns:**

[CollectionReference](https://firebase.google.com/docs/reference/js/firestore_.collectionreference.md#collectionreference_class)\<[DocumentData](https://firebase.google.com/docs/reference/js/firestore_.documentdata.md#documentdata_interface), [DocumentData](https://firebase.google.com/docs/reference/js/firestore_.documentdata.md#documentdata_interface)\>

The `CollectionReference` instance.

#### Exceptions

If the final path has an even number of segments and does not point to a collection.

### deleteDoc(reference)

Deletes the document referred to by the specified `DocumentReference`.

**Signature:**  

    export declare function deleteDoc<AppModelType, DbModelType extends DocumentData>(reference: DocumentReference<AppModelType, DbModelType>): Promise<void>;

#### Parameters

| Parameter |                                                                          Type                                                                           |              Description               |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| reference | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to the document to delete. |

**Returns:**

Promise\<void\>

A Promise resolved once the document has been successfully deleted from the backend (note that it won't resolve while you're offline).

### doc(reference, path, pathSegments)

Gets a `DocumentReference` instance that refers to a document within `reference` at the specified relative path. If no path is specified, an automatically-generated unique ID will be used for the returned `DocumentReference`.

**Signature:**  

    export declare function doc<AppModelType, DbModelType extends DocumentData>(reference: CollectionReference<AppModelType, DbModelType>, path?: string, ...pathSegments: string[]): DocumentReference<AppModelType, DbModelType>;

#### Parameters

|  Parameter   |                                                                             Type                                                                              |                                    Description                                     |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| reference    | [CollectionReference](https://firebase.google.com/docs/reference/js/firestore_.collectionreference.md#collectionreference_class)\<AppModelType, DbModelType\> | A reference to a collection.                                                       |
| path         | string                                                                                                                                                        | A slash-separated path to a document. Has to be omitted to use auto-generated IDs. |
| pathSegments | string\[\]                                                                                                                                                    | Additional path segments that will be applied relative to the first argument.      |

**Returns:**

[DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class)\<AppModelType, DbModelType\>

The `DocumentReference` instance.

#### Exceptions

If the final path has an odd number of segments and does not point to a document.

### doc(reference, path, pathSegments)

Gets a `DocumentReference` instance that refers to a document within `reference` at the specified relative path.

**Signature:**  

    export declare function doc<AppModelType, DbModelType extends DocumentData>(reference: DocumentReference<AppModelType, DbModelType>, path: string, ...pathSegments: string[]): DocumentReference<DocumentData, DocumentData>;

#### Parameters

|  Parameter   |                                                                          Type                                                                           |                                  Description                                  |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| reference    | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to a Firestore document.                                          |
| path         | string                                                                                                                                                  | A slash-separated path to a document.                                         |
| pathSegments | string\[\]                                                                                                                                              | Additional path segments that will be applied relative to the first argument. |

**Returns:**

[DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class)\<[DocumentData](https://firebase.google.com/docs/reference/js/firestore_.documentdata.md#documentdata_interface), [DocumentData](https://firebase.google.com/docs/reference/js/firestore_.documentdata.md#documentdata_interface)\>

The `DocumentReference` instance.

#### Exceptions

If the final path has an odd number of segments and does not point to a document.

### getDoc(reference)

Reads the document referred to by this `DocumentReference`.
| **Note:** `getDoc()` attempts to provide up-to-date data when possible by waiting for data from the server, but it may return cached data or fail if you are offline and the server cannot be reached. To specify this behavior, invoke [getDocFromCache()](https://firebase.google.com/docs/reference/js/firestore_.md#getdocfromcache_4569087) or [getDocFromServer()](https://firebase.google.com/docs/reference/js/firestore_.md#getdocfromserver_4569087).

**Signature:**  

    export declare function getDoc<AppModelType, DbModelType extends DocumentData>(reference: DocumentReference<AppModelType, DbModelType>): Promise<DocumentSnapshot<AppModelType, DbModelType>>;

#### Parameters

| Parameter |                                                                          Type                                                                           |               Description               |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| reference | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | The reference of the document to fetch. |

**Returns:**

Promise\<[DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\>\>

A Promise resolved with a `DocumentSnapshot` containing the current document contents.

### getDocFromCache(reference)

Reads the document referred to by this `DocumentReference` from cache. Returns an error if the document is not currently cached.

**Signature:**  

    export declare function getDocFromCache<AppModelType, DbModelType extends DocumentData>(reference: DocumentReference<AppModelType, DbModelType>): Promise<DocumentSnapshot<AppModelType, DbModelType>>;

#### Parameters

| Parameter |                                                                          Type                                                                           | Description |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| reference | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> |             |

**Returns:**

Promise\<[DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\>\>

A `Promise` resolved with a `DocumentSnapshot` containing the current document contents.

### getDocFromServer(reference)

Reads the document referred to by this `DocumentReference` from the server. Returns an error if the network is not available.

**Signature:**  

    export declare function getDocFromServer<AppModelType, DbModelType extends DocumentData>(reference: DocumentReference<AppModelType, DbModelType>): Promise<DocumentSnapshot<AppModelType, DbModelType>>;

#### Parameters

| Parameter |                                                                          Type                                                                           | Description |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| reference | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> |             |

**Returns:**

Promise\<[DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\>\>

A `Promise` resolved with a `DocumentSnapshot` containing the current document contents.

### onSnapshot(reference, observer)

Attaches a listener for `DocumentSnapshot` events. You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks.

NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.

**Signature:**  

    export declare function onSnapshot<AppModelType, DbModelType extends DocumentData>(reference: DocumentReference<AppModelType, DbModelType>, observer: {
        next?: (snapshot: DocumentSnapshot<AppModelType, DbModelType>) => void;
        error?: (error: FirestoreError) => void;
        complete?: () => void;
    }): Unsubscribe;

#### Parameters

| Parameter |                                                                                                                                                                            Type                                                                                                                                                                            |                       Description                        |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| reference | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class)\<AppModelType, DbModelType\>                                                                                                                                                                                                    | A reference to the document to listen to.                |
| observer  | { next?: (snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\>) =\> void; error?: (error: [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class)) =\> void; complete?: () =\> void; } | A single object containing `next` and `error` callbacks. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/firestore_.unsubscribe.md#unsubscribe_interface)

An unsubscribe function that can be called to cancel the snapshot listener.

### onSnapshot(reference, options, observer)

Attaches a listener for `DocumentSnapshot` events. You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks.

NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.

**Signature:**  

    export declare function onSnapshot<AppModelType, DbModelType extends DocumentData>(reference: DocumentReference<AppModelType, DbModelType>, options: SnapshotListenOptions, observer: {
        next?: (snapshot: DocumentSnapshot<AppModelType, DbModelType>) => void;
        error?: (error: FirestoreError) => void;
        complete?: () => void;
    }): Unsubscribe;

#### Parameters

| Parameter |                                                                                                                                                                            Type                                                                                                                                                                            |                       Description                        |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| reference | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class)\<AppModelType, DbModelType\>                                                                                                                                                                                                    | A reference to the document to listen to.                |
| options   | [SnapshotListenOptions](https://firebase.google.com/docs/reference/js/firestore_.snapshotlistenoptions.md#snapshotlistenoptions_interface)                                                                                                                                                                                                                 | Options controlling the listen behavior.                 |
| observer  | { next?: (snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\>) =\> void; error?: (error: [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class)) =\> void; complete?: () =\> void; } | A single object containing `next` and `error` callbacks. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/firestore_.unsubscribe.md#unsubscribe_interface)

An unsubscribe function that can be called to cancel the snapshot listener.

### onSnapshot(reference, onNext, onError, onCompletion)

Attaches a listener for `DocumentSnapshot` events. You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks.

NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.

**Signature:**  

    export declare function onSnapshot<AppModelType, DbModelType extends DocumentData>(reference: DocumentReference<AppModelType, DbModelType>, onNext: (snapshot: DocumentSnapshot<AppModelType, DbModelType>) => void, onError?: (error: FirestoreError) => void, onCompletion?: () => void): Unsubscribe;

#### Parameters

|  Parameter   |                                                                                   Type                                                                                    |                                          Description                                          |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| reference    | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class)\<AppModelType, DbModelType\>                   | A reference to the document to listen to.                                                     |
| onNext       | (snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\>) =\> void | A callback to be called every time a new `DocumentSnapshot` is available.                     |
| onError      | (error: [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class)) =\> void                                       | A callback to be called if the listen fails or is cancelled. No further callbacks will occur. |
| onCompletion | () =\> void                                                                                                                                                               | Can be provided, but will not be called since streams are never ending.                       |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/firestore_.unsubscribe.md#unsubscribe_interface)

An unsubscribe function that can be called to cancel the snapshot listener.

### onSnapshot(reference, options, onNext, onError, onCompletion)

Attaches a listener for `DocumentSnapshot` events. You may either pass individual `onNext` and `onError` callbacks or pass a single observer object with `next` and `error` callbacks.

NOTE: Although an `onCompletion` callback can be provided, it will never be called because the snapshot stream is never-ending.

**Signature:**  

    export declare function onSnapshot<AppModelType, DbModelType extends DocumentData>(reference: DocumentReference<AppModelType, DbModelType>, options: SnapshotListenOptions, onNext: (snapshot: DocumentSnapshot<AppModelType, DbModelType>) => void, onError?: (error: FirestoreError) => void, onCompletion?: () => void): Unsubscribe;

#### Parameters

|  Parameter   |                                                                                   Type                                                                                    |                                          Description                                          |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| reference    | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class)\<AppModelType, DbModelType\>                   | A reference to the document to listen to.                                                     |
| options      | [SnapshotListenOptions](https://firebase.google.com/docs/reference/js/firestore_.snapshotlistenoptions.md#snapshotlistenoptions_interface)                                | Options controlling the listen behavior.                                                      |
| onNext       | (snapshot: [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\>) =\> void | A callback to be called every time a new `DocumentSnapshot` is available.                     |
| onError      | (error: [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class)) =\> void                                       | A callback to be called if the listen fails or is cancelled. No further callbacks will occur. |
| onCompletion | () =\> void                                                                                                                                                               | Can be provided, but will not be called since streams are never ending.                       |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/firestore_.unsubscribe.md#unsubscribe_interface)

An unsubscribe function that can be called to cancel the snapshot listener.

### setDoc(reference, data)

Writes to the document referred to by this `DocumentReference`. If the document does not yet exist, it will be created.

**Signature:**  

    export declare function setDoc<AppModelType, DbModelType extends DocumentData>(reference: DocumentReference<AppModelType, DbModelType>, data: WithFieldValue<AppModelType>): Promise<void>;

#### Parameters

| Parameter |                                                                          Type                                                                           |                   Description                    |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| reference | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to the document to write.            |
| data      | [WithFieldValue](https://firebase.google.com/docs/reference/js/firestore_.md#withfieldvalue)\<AppModelType\>                                            | A map of the fields and values for the document. |

**Returns:**

Promise\<void\>

A `Promise` resolved once the data has been successfully written to the backend (note that it won't resolve while you're offline).

### setDoc(reference, data, options)

Writes to the document referred to by the specified `DocumentReference`. If the document does not yet exist, it will be created. If you provide `merge` or `mergeFields`, the provided data can be merged into an existing document.

**Signature:**  

    export declare function setDoc<AppModelType, DbModelType extends DocumentData>(reference: DocumentReference<AppModelType, DbModelType>, data: PartialWithFieldValue<AppModelType>, options: SetOptions): Promise<void>;

#### Parameters

| Parameter |                                                                          Type                                                                           |                   Description                    |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| reference | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to the document to write.            |
| data      | [PartialWithFieldValue](https://firebase.google.com/docs/reference/js/firestore_.md#partialwithfieldvalue)\<AppModelType\>                              | A map of the fields and values for the document. |
| options   | [SetOptions](https://firebase.google.com/docs/reference/js/firestore_.md#setoptions)                                                                    | An object to configure the set behavior.         |

**Returns:**

Promise\<void\>

A Promise resolved once the data has been successfully written to the backend (note that it won't resolve while you're offline).

### updateDoc(reference, data)

Updates fields in the document referred to by the specified `DocumentReference`. The update will fail if applied to a document that does not exist.

**Signature:**  

    export declare function updateDoc<AppModelType, DbModelType extends DocumentData>(reference: DocumentReference<AppModelType, DbModelType>, data: UpdateData<DbModelType>): Promise<void>;

#### Parameters

| Parameter |                                                                          Type                                                                           |                                                                      Description                                                                      |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| reference | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to the document to update.                                                                                                                |
| data      | [UpdateData](https://firebase.google.com/docs/reference/js/firestore_.md#updatedata)\<DbModelType\>                                                     | An object containing the fields and values with which to update the document. Fields can contain dots to reference nested fields within the document. |

**Returns:**

Promise\<void\>

A `Promise` resolved once the data has been successfully written to the backend (note that it won't resolve while you're offline).

### updateDoc(reference, field, value, moreFieldsAndValues)

Updates fields in the document referred to by the specified `DocumentReference` The update will fail if applied to a document that does not exist.

Nested fields can be updated by providing dot-separated field path strings or by providing `FieldPath` objects.

**Signature:**  

    export declare function updateDoc<AppModelType, DbModelType extends DocumentData>(reference: DocumentReference<AppModelType, DbModelType>, field: string | FieldPath, value: unknown, ...moreFieldsAndValues: unknown[]): Promise<void>;

#### Parameters

|      Parameter      |                                                                          Type                                                                           |              Description               |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| reference           | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to the document to update. |
| field               | string \| [FieldPath](https://firebase.google.com/docs/reference/js/firestore_.fieldpath.md#fieldpath_class)                                            | The first field to update.             |
| value               | unknown                                                                                                                                                 | The first value.                       |
| moreFieldsAndValues | unknown\[\]                                                                                                                                             | Additional key value pairs.            |

**Returns:**

Promise\<void\>

A `Promise` resolved once the data has been successfully written to the backend (note that it won't resolve while you're offline).

## function(settings, ...)

### memoryLocalCache(settings)

Creates an instance of `MemoryLocalCache`. The instance can be set to `FirestoreSettings.cache` to tell the SDK which cache layer to use.

**Signature:**  

    export declare function memoryLocalCache(settings?: MemoryCacheSettings): MemoryLocalCache;

#### Parameters

| Parameter |                                                                 Type                                                                 | Description |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------|-------------|
| settings  | [MemoryCacheSettings](https://firebase.google.com/docs/reference/js/firestore_.memorycachesettings.md#memorycachesettings_interface) |             |

**Returns:**

[MemoryLocalCache](https://firebase.google.com/docs/reference/js/firestore_.memorylocalcache.md#memorylocalcache_interface)

### memoryLruGarbageCollector(settings)

Creates an instance of `MemoryLruGarbageCollector`.

A target size can be specified as part of the setting parameter. The collector will start deleting documents once the cache size exceeds the given size. The default cache size is 40MB (40 \* 1024 \* 1024 bytes).

**Signature:**  

    export declare function memoryLruGarbageCollector(settings?: {
        cacheSizeBytes?: number;
    }): MemoryLruGarbageCollector;

#### Parameters

| Parameter |             Type             | Description |
|-----------|------------------------------|-------------|
| settings  | { cacheSizeBytes?: number; } |             |

**Returns:**

[MemoryLruGarbageCollector](https://firebase.google.com/docs/reference/js/firestore_.memorylrugarbagecollector.md#memorylrugarbagecollector_interface)

### persistentLocalCache(settings)

Creates an instance of `PersistentLocalCache`. The instance can be set to `FirestoreSettings.cache` to tell the SDK which cache layer to use.

Persistent cache cannot be used in a Node.js environment.

**Signature:**  

    export declare function persistentLocalCache(settings?: PersistentCacheSettings): PersistentLocalCache;

#### Parameters

| Parameter |                                                                       Type                                                                       | Description |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| settings  | [PersistentCacheSettings](https://firebase.google.com/docs/reference/js/firestore_.persistentcachesettings.md#persistentcachesettings_interface) |             |

**Returns:**

[PersistentLocalCache](https://firebase.google.com/docs/reference/js/firestore_.persistentlocalcache.md#persistentlocalcache_interface)

### persistentSingleTabManager(settings)

Creates an instance of `PersistentSingleTabManager`.

**Signature:**  

    export declare function persistentSingleTabManager(settings: PersistentSingleTabManagerSettings | undefined): PersistentSingleTabManager;

#### Parameters

| Parameter |                                                                                              Type                                                                                              |             Description             |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| settings  | [PersistentSingleTabManagerSettings](https://firebase.google.com/docs/reference/js/firestore_.persistentsingletabmanagersettings.md#persistentsingletabmanagersettings_interface) \| undefined | Configures the created tab manager. |

**Returns:**

[PersistentSingleTabManager](https://firebase.google.com/docs/reference/js/firestore_.persistentsingletabmanager.md#persistentsingletabmanager_interface)

## function(snapshot, ...)

### endAt(snapshot)

Creates a [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class) that modifies the result set to end at the provided document (inclusive). The end position is relative to the order of the query. The document must contain all of the fields provided in the orderBy of the query.

**Signature:**  

    export declare function endAt<AppModelType, DbModelType extends DocumentData>(snapshot: DocumentSnapshot<AppModelType, DbModelType>): QueryEndAtConstraint;

#### Parameters

| Parameter |                                                                         Type                                                                         |               Description               |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| snapshot  | [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\> | The snapshot of the document to end at. |

**Returns:**

[QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class)

A [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class) to pass to `query()`

### endBefore(snapshot)

Creates a [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class) that modifies the result set to end before the provided document (exclusive). The end position is relative to the order of the query. The document must contain all of the fields provided in the orderBy of the query.

**Signature:**  

    export declare function endBefore<AppModelType, DbModelType extends DocumentData>(snapshot: DocumentSnapshot<AppModelType, DbModelType>): QueryEndAtConstraint;

#### Parameters

| Parameter |                                                                         Type                                                                         |                 Description                 |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| snapshot  | [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\> | The snapshot of the document to end before. |

**Returns:**

[QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class)

A [QueryEndAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryendatconstraint.md#queryendatconstraint_class) to pass to `query()`

### startAfter(snapshot)

Creates a [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class) that modifies the result set to start after the provided document (exclusive). The starting position is relative to the order of the query. The document must contain all of the fields provided in the orderBy of the query.

**Signature:**  

    export declare function startAfter<AppModelType, DbModelType extends DocumentData>(snapshot: DocumentSnapshot<AppModelType, DbModelType>): QueryStartAtConstraint;

#### Parameters

| Parameter |                                                                         Type                                                                         |                 Description                  |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| snapshot  | [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\> | The snapshot of the document to start after. |

**Returns:**

[QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class)

A [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class) to pass to `query()`

### startAt(snapshot)

Creates a [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class) that modifies the result set to start at the provided document (inclusive). The starting position is relative to the order of the query. The document must contain all of the fields provided in the `orderBy` of this query.

**Signature:**  

    export declare function startAt<AppModelType, DbModelType extends DocumentData>(snapshot: DocumentSnapshot<AppModelType, DbModelType>): QueryStartAtConstraint;

#### Parameters

| Parameter |                                                                         Type                                                                         |                Description                |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| snapshot  | [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\> | The snapshot of the document to start at. |

**Returns:**

[QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class)

A [QueryStartAtConstraint](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstraint_class) to pass to `query()`.

## function(values, ...)

### vector(values)

Creates a new `VectorValue` constructed with a copy of the given array of numbers.

**Signature:**  

    export declare function vector(values?: number[]): VectorValue;

#### Parameters

| Parameter |    Type    |                              Description                              |
|-----------|------------|-----------------------------------------------------------------------|
| values    | number\[\] | Create a `VectorValue` instance with a copy of this array of numbers. |

**Returns:**

[VectorValue](https://firebase.google.com/docs/reference/js/firestore_.vectorvalue.md#vectorvalue_class)

A new `VectorValue` constructed with a copy of the given array of numbers.

## CACHE_SIZE_UNLIMITED

Constant used to indicate the LRU garbage collection should be disabled. Set this value as the `cacheSizeBytes` on the settings passed to the [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance.

**Signature:**  

    CACHE_SIZE_UNLIMITED = -1

## AddPrefixToKeys

Returns a new map where every key is prefixed with the outer key appended to a dot.

**Signature:**  

    export declare type AddPrefixToKeys<Prefix extends string, T extends Record<string, unknown>> = {
        [K in keyof T & string as `${Prefix}.${K}`]+?: string extends K ? any : T[K];
    };

## AggregateFieldType

The union of all `AggregateField` types that are supported by Firestore.

**Signature:**  

    export declare type AggregateFieldType = ReturnType<typeof sum> | ReturnType<typeof average> | ReturnType<typeof count>;

## AggregateSpecData

A type whose keys are taken from an `AggregateSpec`, and whose values are the result of the aggregation performed by the corresponding `AggregateField` from the input `AggregateSpec`.

**Signature:**  

    export declare type AggregateSpecData<T extends AggregateSpec> = {
        [P in keyof T]: T[P] extends AggregateField<infer U> ? U : never;
    };

## AggregateType

Union type representing the aggregate type to be performed.

**Signature:**  

    export declare type AggregateType = 'count' | 'avg' | 'sum';

## ChildUpdateFields

Helper for calculating the nested fields for a given type T1. This is needed to distribute union types such as `undefined | {...}` (happens for optional props) or `{a: A} | {b: B}`.

In this use case, `V` is used to distribute the union types of `T[K]` on `Record`, since `T[K]` is evaluated as an expression and not distributed.

See https://www.typescriptlang.org/docs/handbook/advanced-types.html#distributive-conditional-types

**Signature:**  

    export declare type ChildUpdateFields<K extends string, V> = V extends Record<string, unknown> ? AddPrefixToKeys<K, UpdateData<V>> : never;

## DocumentChangeType

The type of a `DocumentChange` may be 'added', 'removed', or 'modified'.

**Signature:**  

    export declare type DocumentChangeType = 'added' | 'removed' | 'modified';

## FirestoreErrorCode

The set of Firestore status codes. The codes are the same at the ones exposed by gRPC here: https://github.com/grpc/grpc/blob/master/doc/statuscodes.md

Possible values: - 'cancelled': The operation was cancelled (typically by the caller). - 'unknown': Unknown error or an error from a different error domain. - 'invalid-argument': Client specified an invalid argument. Note that this differs from 'failed-precondition'. 'invalid-argument' indicates arguments that are problematic regardless of the state of the system (e.g. an invalid field name). - 'deadline-exceeded': Deadline expired before operation could complete. For operations that change the state of the system, this error may be returned even if the operation has completed successfully. For example, a successful response from a server could have been delayed long enough for the deadline to expire. - 'not-found': Some requested document was not found. - 'already-exists': Some document that we attempted to create already exists. - 'permission-denied': The caller does not have permission to execute the specified operation. - 'resource-exhausted': Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space. - 'failed-precondition': Operation was rejected because the system is not in a state required for the operation's execution. - 'aborted': The operation was aborted, typically due to a concurrency issue like transaction aborts, etc. - 'out-of-range': Operation was attempted past the valid range. - 'unimplemented': Operation is not implemented or not supported/enabled. - 'internal': Internal errors. Means some invariants expected by underlying system has been broken. If you see one of these errors, something is very broken. - 'unavailable': The service is currently unavailable. This is most likely a transient condition and may be corrected by retrying with a backoff. - 'data-loss': Unrecoverable data loss or corruption. - 'unauthenticated': The request does not have valid authentication credentials for the operation.

**Signature:**  

    export declare type FirestoreErrorCode = 'cancelled' | 'unknown' | 'invalid-argument' | 'deadline-exceeded' | 'not-found' | 'already-exists' | 'permission-denied' | 'resource-exhausted' | 'failed-precondition' | 'aborted' | 'out-of-range' | 'unimplemented' | 'internal' | 'unavailable' | 'data-loss' | 'unauthenticated';

## FirestoreLocalCache

Union type from all supported SDK cache layer.

**Signature:**  

    export declare type FirestoreLocalCache = MemoryLocalCache | PersistentLocalCache;

## ListenSource

Describe the source a query listens to.

Set to `default` to listen to both cache and server changes. Set to `cache` to listen to changes in cache only.

**Signature:**  

    export declare type ListenSource = 'default' | 'cache';

## MemoryGarbageCollector

Union type from all support garbage collectors for memory local cache.

**Signature:**  

    export declare type MemoryGarbageCollector = MemoryEagerGarbageCollector | MemoryLruGarbageCollector;

## NestedUpdateFields

For each field (e.g. 'bar'), find all nested keys (e.g. {'bar.baz': T1, 'bar.qux': T2}). Intersect them together to make a single map containing all possible keys that are all marked as optional

**Signature:**  

    export declare type NestedUpdateFields<T extends Record<string, unknown>> = UnionToIntersection<{
        [K in keyof T & string]: ChildUpdateFields<K, T[K]>;
    }[keyof T & string]>;

## OrderByDirection

The direction of a [orderBy()](https://firebase.google.com/docs/reference/js/firestore_.md#orderby_006d61f) clause is specified as 'desc' or 'asc' (descending or ascending).

**Signature:**  

    export declare type OrderByDirection = 'desc' | 'asc';

## PartialWithFieldValue

Similar to TypeScript's `Partial<T>`, but allows nested fields to be omitted and FieldValues to be passed in as property values.

**Signature:**  

    export declare type PartialWithFieldValue<T> = Partial<T> | (T extends Primitive ? T : T extends {} ? {
        [K in keyof T]?: PartialWithFieldValue<T[K]> | FieldValue;
    } : never);

## PersistentTabManager

A union of all available tab managers.

**Signature:**  

    export declare type PersistentTabManager = PersistentSingleTabManager | PersistentMultipleTabManager;

## Primitive

Primitive types.

**Signature:**  

    export declare type Primitive = string | number | boolean | undefined | null;

## QueryConstraintType

Describes the different query constraints available in this SDK.

**Signature:**  

    export declare type QueryConstraintType = 'where' | 'orderBy' | 'limit' | 'limitToLast' | 'startAt' | 'startAfter' | 'endAt' | 'endBefore';

## QueryFilterConstraint

`QueryFilterConstraint` is a helper union type that represents [QueryFieldFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryfieldfilterconstraint.md#queryfieldfilterconstraint_class) and [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class).

**Signature:**  

    export declare type QueryFilterConstraint = QueryFieldFilterConstraint | QueryCompositeFilterConstraint;

## QueryNonFilterConstraint

`QueryNonFilterConstraint` is a helper union type that represents QueryConstraints which are used to narrow or order the set of documents, but that do not explicitly filter on a document field. `QueryNonFilterConstraint`s are created by invoking [orderBy()](https://firebase.google.com/docs/reference/js/firestore_.md#orderby_006d61f), [startAt()](https://firebase.google.com/docs/reference/js/firestore_.md#startat_9a4477f), [startAfter()](https://firebase.google.com/docs/reference/js/firestore_.md#startafter_9a4477f), [endBefore()](https://firebase.google.com/docs/reference/js/firestore_.md#endbefore_9a4477f), [endAt()](https://firebase.google.com/docs/reference/js/firestore_.md#endat_9a4477f), [limit()](https://firebase.google.com/docs/reference/js/firestore_.md#limit_ec46c78) or [limitToLast()](https://firebase.google.com/docs/reference/js/firestore_.md#limittolast_ec46c78) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains the `QueryConstraint`.

**Signature:**  

    export declare type QueryNonFilterConstraint = QueryOrderByConstraint | QueryLimitConstraint | QueryStartAtConstraint | QueryEndAtConstraint;

## SetOptions

An options object that configures the behavior of [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad), and calls. These calls can be configured to perform granular merges instead of overwriting the target documents in their entirety by providing a `SetOptions` with `merge: true`.

**Signature:**  

    export declare type SetOptions = {
        readonly merge?: boolean;
    } | {
        readonly mergeFields?: Array<string | FieldPath>;
    };

## TaskState

Represents the state of bundle loading tasks.

Both 'Error' and 'Success' are sinking state: task will abort or complete and there will be no more updates after they are reported.

**Signature:**  

    export declare type TaskState = 'Error' | 'Running' | 'Success';

## UnionToIntersection

Given a union type `U = T1 | T2 | ...`, returns an intersected type `(T1 & T2 & ...)`.

Uses distributive conditional types and inference from conditional types. This works because multiple candidates for the same type variable in contra-variant positions causes an intersection type to be inferred. https://www.typescriptlang.org/docs/handbook/advanced-types.html#type-inference-in-conditional-types https://stackoverflow.com/questions/50374908/transform-union-type-to-intersection-type

**Signature:**  

    export declare type UnionToIntersection<U> = (U extends unknown ? (k: U) => void : never) extends (k: infer I) => void ? I : never;

## UpdateData

Update data (for use with [updateDoc()](https://firebase.google.com/docs/reference/js/firestore_.md#updatedoc_51a65e3)) that consists of field paths (e.g. 'foo' or 'foo.baz') mapped to values. Fields that contain dots reference nested fields within the document. FieldValues can be passed in as property values.

**Signature:**  

    export declare type UpdateData<T> = T extends Primitive ? T : T extends {} ? {
        [K in keyof T]?: UpdateData<T[K]> | FieldValue;
    } & NestedUpdateFields<T> : Partial<T>;

## WhereFilterOp

Filter conditions in a [where()](https://firebase.google.com/docs/reference/js/firestore_.md#where_0fae4bf) clause are specified using the strings '\&lt;', '\&lt;=', '==', '!=', '\&gt;=', '\&gt;', 'array-contains', 'in', 'array-contains-any', and 'not-in'.

**Signature:**  

    export declare type WhereFilterOp = '<' | '<=' | '==' | '!=' | '>=' | '>' | 'array-contains' | 'in' | 'array-contains-any' | 'not-in';

## WithFieldValue

Allows FieldValues to be passed in as a property value while maintaining type safety.

**Signature:**  

    export declare type WithFieldValue<T> = T | (T extends Primitive ? T : T extends {} ? {
        [K in keyof T]: WithFieldValue<T[K]> | FieldValue;
    } : never);