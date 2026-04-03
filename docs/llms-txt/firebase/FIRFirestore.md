# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore.md.txt

# FirebaseFirestore Framework Reference

# FIRFirestore


    @interface FIRFirestore : NSObject

`Firestore` represents a Firestore Database and is the entry point for all Firestore
operations.
[## Initializing](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/Initializing)

- `
  ``
  ``
  `

  ### [+firestore](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(cm)firestore)

  `
  `  
  Creates, caches, and returns the default `Firestore` using the default `FirebaseApp`. Each
  subsequent invocation returns the same `Firestore` object.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)firestore;

  #### Return Value

  The default `Firestore` instance.
- `
  ``
  ``
  `

  ### [+firestoreForApp:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(cm)firestoreForApp:)

  `
  `  
  Creates, caches, and returns the default `Firestore` object for the specified *app* . Each
  subsequent invocation returns the same `Firestore` object.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)firestoreForApp:(nonnull FIRApp *)app;

  #### Parameters

  |-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*app*` ` | The `FirebaseApp` instance to use for authentication and as a source of the Google Cloud Project ID for your Firestore Database. If you want the default instance, you should explicitly set it to `FirebaseApp.app()`. |

  #### Return Value

  The default `Firestore` instance.
- `
  ``
  ``
  `

  ### [+firestoreForApp:database:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(cm)firestoreForApp:database:)

  `
  `  
  This method is in preview. API signature and functionality are subject to change.

  Creates, caches, and returns named `Firestore` object for the specified `FirebaseApp`. Each
  subsequent invocation returns the same `Firestore` object.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)firestoreForApp:(nonnull FIRApp *)app
                                     database:(nonnull NSString *)database;

  #### Parameters

  |------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*app*` `      | The `FirebaseApp` instance to use for authentication and as a source of the Google Cloud Project ID for your Firestore Database. If you want the default instance, you should explicitly set it to `FirebaseApp.app()`. |
  | ` `*database*` ` | The database name.                                                                                                                                                                                                      |

  #### Return Value

  The named `Firestore` instance.
- `
  ``
  ``
  `

  ### [+firestoreForDatabase:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(cm)firestoreForDatabase:)

  `
  `  
  This method is in preview. API signature and functionality are subject to change.

  Creates, caches, and returns named `Firestore` object for the default *app* . Each subsequent
  invocation returns the same `Firestore` object.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)firestoreForDatabase:(nonnull NSString *)database;

  #### Parameters

  |------------------|--------------------|
  | ` `*database*` ` | The database name. |

  #### Return Value

  The named `Firestore` instance.
- `
  ``
  ``
  `

  ### [settings](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(py)settings)

  `
  `  
  Custom settings used to configure this `Firestore` object.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy) https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestoreSettings.html *_Nonnull settings;

- `
  ``
  ``
  `

  ### [app](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(py)app)

  `
  `  
  The Firebase App associated with this Firestore instance.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) FIRApp *_Nonnull app;

[## Configure FieldIndexes](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/Configure-FieldIndexes)

- `
  ``
  ``
  `

  ### [persistentCacheIndexManager](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(py)persistentCacheIndexManager)

  `
  `  
  A PersistentCacheIndexManager which you can config persistent cache indexes used for
  local query execution.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) FIRPersistentCacheIndexManager *persistentCacheIndexManager;

- `
  ``
  ``
  `

  ### [-setIndexConfigurationFromJSON:completion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(im)setIndexConfigurationFromJSON:completion:)

  `
  `  
  Deprecated

  Instead of creating cache indexes manually, consider using `PersistentCacheIndexManager.enableIndexAutoCreation()` to let the SDK decide whether to create cache indexes for queries running locally.  
  NOTE: This preview method will be deprecated in a future major release. Consider using
  `PersistentCacheIndexManager.enableIndexAutoCreation()` to let the SDK decide whether to create
  cache indexes for queries running locally.

  Configures indexing for local query execution. Any previous index configuration is overridden.

  The index entries themselves are created asynchronously. You can continue to use queries
  that require indexing even if the indices are not yet available. Query execution will
  automatically start using the index once the index entries have been written.

  The method accepts the JSON format exported by the Firebase CLI (`firebase
  firestore:indexes`). If the JSON format is invalid, the completion block will be
  invoked with an NSError.  

  #### Declaration

  Objective-C  

      - (void)setIndexConfigurationFromJSON:(nonnull NSString *)json
                                 completion:(nullable void (^)(NSError *_Nullable))
                                                completion;

  #### Parameters

  |--------------------|---------------------------------------------------------------------------------------------------------------------------------|
  | ` `*json*` `       | The JSON format exported by the Firebase CLI.                                                                                   |
  | ` `*completion*` ` | A block to execute when setting is in a final state. The `error` parameter will be set if the block is invoked due to an error. |

- `
  ``
  ``
  `

  ### [-setIndexConfigurationFromStream:completion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(im)setIndexConfigurationFromStream:completion:)

  `
  `  
  Deprecated

  Instead of creating cache indexes manually, consider using `PersistentCacheIndexManager.enableIndexAutoCreation()` to let the SDK decide whether to create cache indexes for queries running locally.  
  NOTE: This preview method will be deprecated in a future major release. Consider using
  `PersistentCacheIndexManager.enableIndexAutoCreation()` to let the SDK decide whether to create
  cache indexes for queries running locally.

  Configures indexing for local query execution. Any previous index configuration is overridden.

  The index entries themselves are created asynchronously. You can continue to use queries
  that require indexing even if the indices are not yet available. Query execution will
  automatically start using the index once the index entries have been written.

  Indexes are only supported with LevelDB persistence. Invoke `set_persistence_enabled(true)`
  before setting an index configuration. If LevelDB is not enabled, any index configuration
  will be rejected.

  The method accepts the JSON format exported by the Firebase CLI (`firebase
  firestore:indexes`). If the JSON format is invalid, this method ignores the changes.  

  #### Declaration

  Objective-C  

      - (void)setIndexConfigurationFromStream:(nonnull NSInputStream *)stream
                                   completion:(nullable void (^)(NSError *_Nullable))
                                                  completion;

  #### Parameters

  |--------------------|---------------------------------------------------------------------------------------------------------------------------------|
  | ` `*stream*` `     | An input stream from which the configuration can be read.                                                                       |
  | ` `*completion*` ` | A block to execute when setting is in a final state. The `error` parameter will be set if the block is invoked due to an error. |

[## Collections and Documents](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/Collections-and-Documents)

- `
  ``
  ``
  `

  ### [-collectionWithPath:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(im)collectionWithPath:)

  `
  `  
  Gets a `CollectionReference` referring to the collection at the specified path within the
  database.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRCollectionReference.html *)collectionWithPath:
          (nonnull NSString *)collectionPath;

  #### Parameters

  |------------------------|--------------------------------------------------------------------------------------|
  | ` `*collectionPath*` ` | The slash-separated path of the collection for which to get a `CollectionReference`. |

  #### Return Value

  The `CollectionReference` at the specified *collectionPath*.
- `
  ``
  ``
  `

  ### [-documentWithPath:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(im)documentWithPath:)

  `
  `  
  Gets a `DocumentReference` referring to the document at the specified path within the
  database.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference.html *)documentWithPath:
          (nonnull NSString *)documentPath;

  #### Parameters

  |----------------------|----------------------------------------------------------------------------------|
  | ` `*documentPath*` ` | The slash-separated path of the document for which to get a `DocumentReference`. |

  #### Return Value

The `DocumentReference` for the specified *documentPath*.  
[## Collection Group Queries](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/Collection-Group-Queries)

- `
  ``
  ``
  `

  ### [-collectionGroupWithID:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(im)collectionGroupWithID:)

  `
  `  
  Creates and returns a new `Query` that includes all documents in the database that are contained
  in a collection or subcollection with the given collectionID.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery.html *)collectionGroupWithID:(nonnull NSString *)collectionID;

  #### Parameters

  |----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*collectionID*` ` | Identifies the collections to query over. Every collection or subcollection with this ID as the last segment of its path will be included. Cannot contain a slash. |

  #### Return Value

The created `Query`.  
[## Transactions and Write Batches](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/Transactions-and-Write-Batches)

- `
  ``
  ``
  `

  ### [-runTransactionWithBlock:completion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(im)runTransactionWithBlock:completion:)

  `
  `  
  Executes the given updateBlock and then attempts to commit the changes applied within an atomic
  transaction.

  The maximum number of writes allowed in a single transaction is 500, but note that each usage of
  `FieldValue.serverTimestamp()`, `FieldValue.arrayUnion()`, `FieldValue.arrayRemove()`, or
  `FieldValue.increment()` inside a transaction counts as an additional write.

  In the updateBlock, a set of reads and writes can be performed atomically using the
  `Transaction` object passed to the block. After the updateBlock is run, Firestore will attempt
  to apply the changes to the server. If any of the data read has been modified outside of this
  transaction since being read, then the transaction will be retried by executing the updateBlock
  again. If the transaction still fails after 5 retries, then the transaction will fail.

  Since the updateBlock may be executed multiple times, it should avoiding doing anything that
  would cause side effects.

  Any value maybe be returned from the updateBlock. If the transaction is successfully committed,
  then the completion block will be passed that value. The updateBlock also has an `NSErrorPointer`
  out parameter. If this is set, then the transaction will not attempt to commit, and the given
  error will be passed to the completion block.

  The `Transaction` object passed to the updateBlock contains methods for accessing documents
  and collections. Unlike other firestore access, data accessed with the transaction will not
  reflect local changes that have not been committed. For this reason, it is required that all
  reads are performed before any writes. Transactions must be performed while online. Otherwise,
  reads will fail, the final commit will fail, and the completion block will return an error.  

  #### Declaration

  Objective-C  

      - (void)runTransactionWithBlock:
                  (nonnull id _Nullable (^)(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRTransaction.html *_Nonnull,
                                            NSError *_Nullable *_Nullable))updateBlock
                           completion:
                               (nonnull void (^)(id _Nullable,
                                                 NSError *_Nullable))completion;

  #### Parameters

  |---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*updateBlock*` ` | The block to execute within the transaction context.                                                                                            |
  | ` `*completion*` `  | The block to call with the result or error of the transaction. This block will run even if the client is offline, unless the process is killed. |

- `
  ``
  ``
  `

  ### [-runTransactionWithOptions:block:completion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(im)runTransactionWithOptions:block:completion:)

  `
  `  
  Executes the given updateBlock and then attempts to commit the changes applied within an atomic
  transaction.

  The maximum number of writes allowed in a single transaction is 500, but note that each usage of
  `FieldValue.serverTimestamp()`, `FieldValue.arrayUnion()`, `FieldValue.arrayRemove()`, or
  `FieldValue.increment()` inside a transaction counts as an additional write.

  In the updateBlock, a set of reads and writes can be performed atomically using the
  `Transaction` object passed to the block. After the updateBlock is run, Firestore will attempt
  to apply the changes to the server. If any of the data read has been modified outside of this
  transaction since being read, then the transaction will be retried by executing the updateBlock
  again. If the transaction still fails after the attempting the number of times specified by the
  `max_attempts` property of the given `TransactionOptions` object, then the transaction will fail.
  If the given `TransactionOptions` is `nil`, then the default `max_attempts` of 5 will be used.

  Since the updateBlock may be executed multiple times, it should avoiding doing anything that
  would cause side effects.

  Any value maybe be returned from the updateBlock. If the transaction is successfully committed,
  then the completion block will be passed that value. The updateBlock also has an `NSErrorPointer`
  out parameter. If this is set, then the transaction will not attempt to commit, and the given
  error will be passed to the completion block.

  The `Transaction` object passed to the updateBlock contains methods for accessing documents
  and collections. Unlike other firestore access, data accessed with the transaction will not
  reflect local changes that have not been committed. For this reason, it is required that all
  reads are performed before any writes. Transactions must be performed while online. Otherwise,
  reads will fail, the final commit will fail, and the completion block will return an error.  

  #### Declaration

  Objective-C  

      - (void)runTransactionWithOptions:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRTransactionOptions.html *_Nullable)options
                                  block:(nonnull id _Nullable (^)(
                                            https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRTransaction.html *_Nonnull,
                                            NSError *_Nullable *_Nullable))updateBlock
                             completion:
                                 (nonnull void (^)(id _Nullable,
                                                   NSError *_Nullable))completion;

  #### Parameters

  |---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*options*` `     | The transaction options for controlling execution, or `nil` to use the default transaction options.                                             |
  | ` `*updateBlock*` ` | The block to execute within the transaction context.                                                                                            |
  | ` `*completion*` `  | The block to call with the result or error of the transaction. This block will run even if the client is offline, unless the process is killed. |

- `
  ``
  ``
  `

  ### [-batch](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(im)batch)

  `
  `  
  Creates a write batch, used for performing multiple writes as a single
  atomic operation.

  The maximum number of writes allowed in a single batch is 500, but note that each usage of
  `FieldValue.serverTimestamp()`, `FieldValue.arrayUnion()`, `FieldValue.arrayRemove()`, or
  `FieldValue.increment()` inside a batch counts as an additional write.

  Unlike transactions, write batches are persisted offline and therefore are preferable when you
  don't need to condition your writes on read data.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRWriteBatch.html *)batch;

[## Logging](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/Logging)

- `
  ``
  ``
  `

  ### [+enableLogging:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(cm)enableLogging:)

  `
  `  
  Enables or disables logging from the Firestore client.  

  #### Declaration

  Objective-C  

      + (void)enableLogging:(BOOL)logging;

[## Network](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/Network)

- `
  ``
  ``
  `

  ### [-useEmulatorWithHost:port:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(im)useEmulatorWithHost:port:)

  `
  `  
  Configures Firestore to connect to an emulated host instead of the default remote backend. After
  Firestore has been used (i.e. a document reference has been instantiated), this value cannot be
  changed.  

  #### Declaration

  Objective-C  

      - (void)useEmulatorWithHost:(nonnull NSString *)host port:(NSInteger)port;

- `
  ``
  ``
  `

  ### [-enableNetworkWithCompletion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(im)enableNetworkWithCompletion:)

  `
  `  
  Re-enables usage of the network by this Firestore instance after a prior call to
  `disableNetwork(completion:)`. Completion block, if provided, will be called once network uasge
  has been enabled.  

  #### Declaration

  Objective-C  

      - (void)enableNetworkWithCompletion:
          (nullable void (^)(NSError *_Nullable))completion;

- `
  ``
  ``
  `

  ### [-disableNetworkWithCompletion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(im)disableNetworkWithCompletion:)

  `
  `  
  Disables usage of the network by this Firestore instance. It can be re-enabled by via
  `enableNetwork`. While the network is disabled, any snapshot listeners or get calls will return
  results from cache and any write operations will be queued until the network is restored. The
  completion block, if provided, will be called once network usage has been disabled.  

  #### Declaration

  Objective-C  

      - (void)disableNetworkWithCompletion:
          (nullable void (^)(NSError *_Nullable))completion;

- `
  ``
  ``
  `

  ### [-clearPersistenceWithCompletion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(im)clearPersistenceWithCompletion:)

  `
  `  
  Clears the persistent storage. This includes pending writes and cached documents.

  Must be called while the firestore instance is not started (after the app is shutdown or when
  the app is first initialized). On startup, this method must be called before other methods
  (other than `Firestore.settings`). If the firestore instance is still running, the function
  will complete with an error code of `FailedPrecondition`.

  Note: `clearPersistence(completion:)` is primarily intended to help write reliable tests that
  use Firestore. It uses the most efficient mechanism possible for dropping existing data but
  does not attempt to securely overwrite or otherwise make cached data unrecoverable. For
  applications that are sensitive to the disclosure of cache data in between user sessions we
  strongly recommend not to enable persistence in the first place.  

  #### Declaration

  Objective-C  

      - (void)clearPersistenceWithCompletion:
          (nullable void (^)(NSError *_Nullable))completion;

- `
  ``
  ``
  `

  ### [-waitForPendingWritesWithCompletion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(im)waitForPendingWritesWithCompletion:)

  `
  `  
  Waits until all currently pending writes for the active user have been acknowledged by the
  backend.

  The completion block is called immediately without error if there are no outstanding writes.
  Otherwise, the completion block is called when all previously issued writes (including those
  written in a previous app session) have been acknowledged by the backend. The completion
  block does not wait for writes that were added after the method is called. If you
  wish to wait for additional writes, you have to call `waitForPendingWrites` again.

  Any outstanding `waitForPendingWrites(completion:)` completion blocks are called with an error
  during user change.  

  #### Declaration

  Objective-C  

      - (void)waitForPendingWritesWithCompletion:
          (nonnull void (^)(NSError *_Nullable))completion;

- `
  ``
  ``
  `

  ### [-addSnapshotsInSyncListener:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(im)addSnapshotsInSyncListener:)

  `
  `  
  Attaches a listener for a snapshots-in-sync event. The snapshots-in-sync event indicates that all
  listeners affected by a given change have fired, even if a single server-generated change affects
  multiple listeners.

  NOTE: The snapshots-in-sync event only indicates that listeners are in sync with each other, but
  does not relate to whether those snapshots are in sync with the server. Use SnapshotMetadata in
  the individual listeners to determine if a snapshot is from the cache or the server.  

  #### Declaration

  Objective-C  

      - (nonnull id<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols/FIRListenerRegistration.html>)addSnapshotsInSyncListener:
          (nonnull void (^)(void))listener;

  #### Parameters

  |------------------|----------------------------------------------------------------------------------------|
  | ` `*listener*` ` | A callback to be called every time all snapshot listeners are in sync with each other. |

  #### Return Value

A `ListenerRegistration` object that can be used to remove the listener.  
[## Terminating](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/Terminating)

- `
  ``
  ``
  `

  ### [-terminateWithCompletion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(im)terminateWithCompletion:)

  `
  `  
  Terminates this `Firestore` instance.

  After calling `terminate` only the `clearPersistence` method may be used. Any other method will
  throw an error.

  To restart after termination, simply create a new instance of `Firestore` with the `firestore`
  method.

  Termination does not cancel any pending writes and any tasks that are awaiting a response from
  the server will not be resolved. The next time you start this instance, it will resume attempting
  to send these writes to the server.

  Note: Under normal circumstances, calling this method is not required. This method is useful only
  when you want to force this instance to release all of its resources or in combination with
  `clearPersistence` to ensure that all local state is destroyed between test runs.  

  #### Declaration

  Objective-C  

      - (void)terminateWithCompletion:
          (nullable void (^)(NSError *_Nullable))completion;

  #### Parameters

  |--------------------|---------------------------------------------------------|
  | ` `*completion*` ` | A block to execute once everything has been terminated. |

[## Bundles](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/Bundles)

- `
  ``
  ``
  `

  ### [-loadBundle:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(im)loadBundle:)

  `
  `  
  Loads a Firestore bundle into the local cache.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRLoadBundleTask.html *)loadBundle:(nonnull NSData *)bundleData;

  #### Parameters

  |--------------------|------------------------------------|
  | ` `*bundleData*` ` | Data from the bundle to be loaded. |

  #### Return Value

  A `LoadBundleTask` which allows registered observers
  to receive progress updates and completion or error events.
- `
  ``
  ``
  `

  ### [-loadBundle:completion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(im)loadBundle:completion:)

  `
  `  
  Loads a Firestore bundle into the local cache.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRLoadBundleTask.html *)
          loadBundle:(nonnull NSData *)bundleData
          completion:(nullable void (^)(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRLoadBundleTaskProgress.html *_Nullable,
                                        NSError *_Nullable))completion;

  #### Parameters

  |--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*bundleData*` ` | Data from the bundle to be loaded.                                                                                                                                                                                                               |
  | ` `*completion*` ` | A block to execute when loading is in a final state. The `error` parameter will be set if the block is invoked due to an error. If observers are registered to the `LoadBundleTask`, this block will be called after all observers are notified. |

  #### Return Value

  A `LoadBundleTask` which allows registered observers to receive progress updates and
  completion or error events.
- `
  ``
  ``
  `

  ### [-loadBundleStream:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(im)loadBundleStream:)

  `
  `  
  Loads a Firestore bundle into the local cache.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRLoadBundleTask.html *)loadBundleStream:
          (nonnull NSInputStream *)bundleStream;

  #### Parameters

  |----------------------|----------------------------------------------------|
  | ` `*bundleStream*` ` | An input stream from which the bundle can be read. |

  #### Return Value

  A `LoadBundleTask` which allows registered observers to receive progress updates and
  completion or error events.
- `
  ``
  ``
  `

  ### [-loadBundleStream:completion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(im)loadBundleStream:completion:)

  `
  `  
  Loads a Firestore bundle into the local cache.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRLoadBundleTask.html *)
          loadBundleStream:(nonnull NSInputStream *)bundleStream
                completion:(nullable void (^)(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRLoadBundleTaskProgress.html *_Nullable,
                                              NSError *_Nullable))completion;

  #### Parameters

  |----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*bundleStream*` ` | An input stream from which the bundle can be read.                                                                                                                                                                                                           |
  | ` `*completion*` `   | A block to execute when the loading is in a final state. The `error` parameter of the block will be set if it is due to an error. If observers are registered to the returning `LoadBundleTask`, this block will be called after all observers are notified. |

  #### Return Value

  A `LoadBundleTask` which allow registering observers to receive progress updates, and
  completion or error events.
- `
  ``
  ``
  `

  ### [-getQueryNamed:completion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestore#/c:objc(cs)FIRFirestore(im)getQueryNamed:completion:)

  `
  `  
  Reads a `Query` from the local cache, identified by the given name.

  Named queries are packaged into bundles on the server side (along with the resulting documents)
  and loaded into local cache using `loadBundle`. Once in the local cache, you can use this method
  to extract a query by name.  

  #### Declaration

  Objective-C  

      - (void)getQueryNamed:(nonnull NSString *)name
                 completion:(nonnull void (^)(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery.html *_Nullable))completion;

  #### Parameters

  |--------------------|---------------------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | A block to execute with the query read from the local cache. If no query can be found, its parameter will be `nil`. |