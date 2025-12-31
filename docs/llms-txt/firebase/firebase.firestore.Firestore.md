# Source: https://firebase.google.com/docs/reference/js/v8/firebase.firestore.Firestore.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore.md.txt

# Firestore | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/node/firebase).
- [firestore](https://firebase.google.com/docs/reference/node/firebase.firestore).
- Firestore

The Cloud Firestore service interface.

Do not call this constructor directly. Instead, use
[`firebase.firestore()`](https://firebase.google.com/docs/reference/node/firebase.firestore).

## Index

### Constructors

- [constructor](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore#constructor)

### Properties

- [app](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore#app)

### Methods

- [batch](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore#batch)
- [clearPersistence](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore#clearpersistence)
- [collection](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore#collection)
- [collectionGroup](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore#collectiongroup)
- [disableNetwork](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore#disablenetwork)
- [doc](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore#doc)
- [enableNetwork](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore#enablenetwork)
- [enablePersistence](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore#enablepersistence)
- [loadBundle](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore#loadbundle)
- [namedQuery](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore#namedquery)
- [onSnapshotsInSync](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore#onsnapshotsinsync)
- [runTransaction](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore#runtransaction)
- [settings](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore#settings)
- [terminate](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore#terminate)
- [useEmulator](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore#useemulator)
- [waitForPendingWrites](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore#waitforpendingwrites)

## Constructors

### Private constructor

- new Firestore ( ) : [Firestore](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore)
-

  #### Returns [Firestore](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore)

## Properties

### app

app: [App](https://firebase.google.com/docs/reference/node/firebase.app.App)  
The [app](https://firebase.google.com/docs/reference/node/firebase.app.App) associated with this `Firestore` service
instance.

## Methods

### batch

- batch ( ) : [WriteBatch](https://firebase.google.com/docs/reference/node/firebase.firestore.WriteBatch)
- Creates a write batch, used for performing multiple writes as a single
  atomic operation. The maximum number of writes allowed in a single WriteBatch
  is 500, but note that each usage of `FieldValue.serverTimestamp()`,
  `FieldValue.arrayUnion()`, `FieldValue.arrayRemove()`, or
  `FieldValue.increment()` inside a WriteBatch counts as an additional write.

  #### Returns [WriteBatch](https://firebase.google.com/docs/reference/node/firebase.firestore.WriteBatch)

  A `WriteBatch` that can be used to atomically execute multiple writes.

### clearPersistence

- clearPersistence ( ) : Promise \< void \>
- Clears the persistent storage. This includes pending writes and cached
  documents.

  Must be called while the firestore instance is not started (after the app
  is shutdown or when the app is first initialized). On startup, this
  method must be called before other methods (other than settings()). If
  the firestore instance is still running, the promise will be rejected
  with the error code of `failed-precondition`.

  Note: clearPersistence() is primarily intended to help write reliable
  tests that use Cloud Firestore. It uses an efficient mechanism for
  dropping existing data but does not attempt to securely overwrite or
  otherwise make cached data unrecoverable. For applications that are
  sensitive to the disclosure of cached data in between user sessions, we
  strongly recommend not enabling persistence at all.

  #### Returns Promise\<void\>

  A promise that is resolved when the persistent storage is
  cleared. Otherwise, the promise is rejected with an error.

### collection

- collection ( collectionPath : string ) : [CollectionReference](https://firebase.google.com/docs/reference/node/firebase.firestore.CollectionReference) \< [DocumentData](https://firebase.google.com/docs/reference/node/firebase.firestore#documentdata) \>
- Gets a `CollectionReference` instance that refers to the collection at
  the specified path.

  #### Parameters

  -

    ##### collectionPath: string

    A slash-separated path to a collection.

  #### Returns [CollectionReference](https://firebase.google.com/docs/reference/node/firebase.firestore.CollectionReference)\<[DocumentData](https://firebase.google.com/docs/reference/node/firebase.firestore#documentdata)\>

  The `CollectionReference` instance.

### collectionGroup

- collectionGroup ( collectionId : string ) : [Query](https://firebase.google.com/docs/reference/node/firebase.firestore.Query) \< [DocumentData](https://firebase.google.com/docs/reference/node/firebase.firestore#documentdata) \>
- Creates and returns a new Query that includes all documents in the
  database that are contained in a collection or subcollection with the
  given collectionId.

  #### Parameters

  -

    ##### collectionId: string

    Identifies the collections to query over. Every
    collection or subcollection with this ID as the last segment of its path
    will be included. Cannot contain a slash.

  #### Returns [Query](https://firebase.google.com/docs/reference/node/firebase.firestore.Query)\<[DocumentData](https://firebase.google.com/docs/reference/node/firebase.firestore#documentdata)\>

  The created Query.

### disableNetwork

- disableNetwork ( ) : Promise \< void \>
- Disables network usage for this instance. It can be re-enabled via
  [`enableNetwork()`](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore#enablenetwork). While
  the network is disabled, any snapshot listeners or get() calls will return
  results from cache, and any write operations will be queued until the network
  is restored.

  #### Returns Promise\<void\>

  A promise that is resolved once the network has been
  disabled.

### doc

- doc ( documentPath : string ) : [DocumentReference](https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentReference) \< [DocumentData](https://firebase.google.com/docs/reference/node/firebase.firestore#documentdata) \>
- Gets a `DocumentReference` instance that refers to the document at the
  specified path.

  #### Parameters

  -

    ##### documentPath: string

    A slash-separated path to a document.

  #### Returns [DocumentReference](https://firebase.google.com/docs/reference/node/firebase.firestore.DocumentReference)\<[DocumentData](https://firebase.google.com/docs/reference/node/firebase.firestore#documentdata)\>

  The `DocumentReference` instance.

### enableNetwork

- enableNetwork ( ) : Promise \< void \>
- Re-enables use of the network for this Firestore instance after a prior
  call to [`disableNetwork()`](https://firebase.google.com/docs/reference/node/firebase.firestore.Firestore#disablenetwork).

  #### Returns Promise\<void\>

  A promise that is resolved once the network has been
  enabled.

### enablePersistence

- enablePersistence ( settings ? : [PersistenceSettings](https://firebase.google.com/docs/reference/node/firebase.firestore.PersistenceSettings) ) : Promise \< void \>
- Attempts to enable persistent storage, if possible.

  Must be called before any other methods (other than settings() and
  clearPersistence()).

  If this fails, enablePersistence() will reject the promise it returns.
  Note that even after this failure, the firestore instance will remain
  usable, however offline persistence will be disabled.

  There are several reasons why this can fail, which can be identified by
  the `code` on the error.
  - failed-precondition: The app is already open in another browser tab.
  - unimplemented: The browser is incompatible with the offline persistence implementation.

  #### Parameters

  -

    ##### Optional settings: [PersistenceSettings](https://firebase.google.com/docs/reference/node/firebase.firestore.PersistenceSettings)

    Optional settings object to configure persistence.

  #### Returns Promise\<void\>

  A promise that represents successfully enabling persistent
  storage.

### loadBundle

- loadBundle ( bundleData : ArrayBuffer \| ReadableStream \< Uint8Array \> \| string ) : [LoadBundleTask](https://firebase.google.com/docs/reference/node/firebase.firestore.LoadBundleTask)
- Loads a Firestore bundle into the local cache.

  #### Parameters

  -

    ##### bundleData: ArrayBuffer \| ReadableStream\<Uint8Array\> \| string

    An object representing the bundle to be loaded. Valid objects are `ArrayBuffer`,
    `ReadableStream<Uint8Array>` or `string`.

  #### Returns [LoadBundleTask](https://firebase.google.com/docs/reference/node/firebase.firestore.LoadBundleTask)

  A `LoadBundleTask` object, which notifies callers with progress updates, and completion
  or error events. It can be used as a `Promise<LoadBundleTaskProgress>`.

### namedQuery

- namedQuery ( name : string ) : Promise \< [Query](https://firebase.google.com/docs/reference/node/firebase.firestore.Query) \< [DocumentData](https://firebase.google.com/docs/reference/node/firebase.firestore#documentdata) \> \| null \>
- Reads a Firestore `Query` from local cache, identified by the given name.

  The named queries are packaged into bundles on the server side (along
  with resulting documents), and loaded to local cache using `loadBundle`. Once in local
  cache, use this method to extract a `Query` by name.

  #### Parameters

  -

    ##### name: string

  #### Returns Promise\<[Query](https://firebase.google.com/docs/reference/node/firebase.firestore.Query)\<[DocumentData](https://firebase.google.com/docs/reference/node/firebase.firestore#documentdata)\> \| null\>

### onSnapshotsInSync

- onSnapshotsInSync ( observer : { complete ?: ( ) =\> void ; error ?: ( error : [FirestoreError](https://firebase.google.com/docs/reference/node/firebase.firestore.FirestoreError) ) =\> void ; next ?: ( value : void ) =\> void } ) : ( ) =\> void
- Attaches a listener for a snapshots-in-sync event. The snapshots-in-sync
  event indicates that all listeners affected by a given change have fired,
  even if a single server-generated change affects multiple listeners.

  NOTE: The snapshots-in-sync event only indicates that listeners are in sync
  with each other, but does not relate to whether those snapshots are in sync
  with the server. Use SnapshotMetadata in the individual listeners to
  determine if a snapshot is from the cache or the server.

  #### Parameters

  -

    ##### observer: { complete?: () =\> void; error?: (error: [FirestoreError](https://firebase.google.com/docs/reference/node/firebase.firestore.FirestoreError)) =\> void; next?: (value: void) =\> void }

    A single object containing `next` and `error` callbacks.
    -

      ##### Optional complete?: () =\> void

      -
        - (): void

        <!-- -->

        -

          #### Returns void

    -

      ##### Optional error?: (error: [FirestoreError](https://firebase.google.com/docs/reference/node/firebase.firestore.FirestoreError)) =\> void

      -
        - (error: [FirestoreError](https://firebase.google.com/docs/reference/node/firebase.firestore.FirestoreError)): void

        <!-- -->

        -

          #### Parameters

          -

            ##### error: [FirestoreError](https://firebase.google.com/docs/reference/node/firebase.firestore.FirestoreError)

          #### Returns void

    -

      ##### Optional next?: (value: void) =\> void

      -
        - (value: void): void

        <!-- -->

        -

          #### Parameters

          -

            ##### value: void

          #### Returns void

  #### Returns () =\> void

  An unsubscribe function that can be called to cancel the snapshot
  listener.
  -
    - (): void

    <!-- -->

    -

      #### Returns void

- onSnapshotsInSync ( onSync : ( ) =\> void ) : ( ) =\> void
- Attaches a listener for a snapshots-in-sync event. The snapshots-in-sync
  event indicates that all listeners affected by a given change have fired,
  even if a single server-generated change affects multiple listeners.

  NOTE: The snapshots-in-sync event only indicates that listeners are in sync
  with each other, but does not relate to whether those snapshots are in sync
  with the server. Use SnapshotMetadata in the individual listeners to
  determine if a snapshot is from the cache or the server.

  #### Parameters

  -

    ##### onSync: () =\> void

    A callback to be called every time all snapshot listeners are
    in sync with each other.
    -
      - (): void

      <!-- -->

      -

        #### Returns void

  #### Returns () =\> void

  An unsubscribe function that can be called to cancel the snapshot
  listener.
  -
    - (): void

    <!-- -->

    -

      #### Returns void

### runTransaction

- runTransaction \< T \> ( updateFunction : ( transaction : [Transaction](https://firebase.google.com/docs/reference/node/firebase.firestore.Transaction) ) =\> Promise \< T \> ) : Promise \< T \>
- Executes the given `updateFunction` and then attempts to commit the changes
  applied within the transaction. If any document read within the transaction
  has changed, Cloud Firestore retries the `updateFunction`. If it fails to
  commit after 5 attempts, the transaction fails.

  The maximum number of writes allowed in a single transaction is 500, but
  note that each usage of `FieldValue.serverTimestamp()`,
  `FieldValue.arrayUnion()`, `FieldValue.arrayRemove()`, or
  `FieldValue.increment()` inside a transaction counts as an additional write.

  #### Type parameters

  -

    #### T

  #### Parameters

  -

    ##### updateFunction: (transaction: [Transaction](https://firebase.google.com/docs/reference/node/firebase.firestore.Transaction)) =\> Promise\<T\>

    The function to execute within the transaction context.
    -
      - (transaction: [Transaction](https://firebase.google.com/docs/reference/node/firebase.firestore.Transaction)): Promise\<T\>

      <!-- -->

      -

        #### Parameters

        -

          ##### transaction: [Transaction](https://firebase.google.com/docs/reference/node/firebase.firestore.Transaction)

        #### Returns Promise\<T\>

  #### Returns Promise\<T\>

  If the transaction completed successfully or was explicitly aborted
  (the `updateFunction` returned a failed promise),
  the promise returned by the updateFunction is returned here. Else, if the
  transaction failed, a rejected promise with the corresponding failure
  error will be returned.

### settings

- settings ( settings : [Settings](https://firebase.google.com/docs/reference/node/firebase.firestore.Settings) ) : void
- Specifies custom settings to be used to configure the `Firestore`
  instance. Must be set before invoking any other methods.

  #### Parameters

  -

    ##### settings: [Settings](https://firebase.google.com/docs/reference/node/firebase.firestore.Settings)

    The settings to use.

  #### Returns void

### terminate

- terminate ( ) : Promise \< void \>
- Terminates this Firestore instance.

  After calling `terminate()` only the `clearPersistence()` method may be used. Any other method
  will throw a `FirestoreError`.

  To restart after termination, create a new instance of FirebaseFirestore with
  `firebase.firestore()`.

  Termination does not cancel any pending writes, and any promises that are awaiting a response
  from the server will not be resolved. If you have persistence enabled, the next time you
  start this instance, it will resume sending these writes to the server.

  Note: Under normal circumstances, calling `terminate()` is not required. This
  method is useful only when you want to force this instance to release all of its resources or
  in combination with `clearPersistence()` to ensure that all local state is destroyed
  between test runs.

  #### Returns Promise\<void\>

  A promise that is resolved when the instance has been successfully terminated.

### useEmulator

- useEmulator ( host : string , port : number , options ? : { mockUserToken ?: [EmulatorMockTokenOptions](https://firebase.google.com/docs/reference/node/firebase.firestore#emulatormocktokenoptions) \| string } ) : void
- Modify this instance to communicate with the Cloud Firestore emulator.

  Note: this must be called before this instance has been used to do any operations.

  #### Parameters

  -

    ##### host: string

    the emulator host (ex: localhost).
  -

    ##### port: number

    the emulator port (ex: 9000).
  -

    ##### Optional options: { mockUserToken?: [EmulatorMockTokenOptions](https://firebase.google.com/docs/reference/node/firebase.firestore#emulatormocktokenoptions) \| string }

    -

      ##### Optional mockUserToken?: [EmulatorMockTokenOptions](https://firebase.google.com/docs/reference/node/firebase.firestore#emulatormocktokenoptions) \| string

      the mock auth token to use for unit
      testing Security Rules.

  #### Returns void

### waitForPendingWrites

- waitForPendingWrites ( ) : Promise \< void \>
- Waits until all currently pending writes for the active user have been acknowledged by the
  backend.

  The returned Promise resolves immediately if there are no outstanding writes. Otherwise, the
  Promise waits for all previously issued writes (including those written in a previous app
  session), but it does not wait for writes that were added after the method is called. If you
  want to wait for additional writes, call `waitForPendingWrites()` again.

  Any outstanding `waitForPendingWrites()` Promises are rejected during user changes.

  #### Returns Promise\<void\>

  A Promise which resolves when all currently pending writes have been
acknowledged by the backend.