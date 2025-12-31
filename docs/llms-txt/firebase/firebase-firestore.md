# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore.md.txt

# Firebase.Firestore.FirebaseFirestore Class Reference

# Firebase.Firestore.FirebaseFirestore

Represents a Cloud [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) database and is the entry point for all Cloud [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) operations.

## Summary

|                                                                                                                                                                                                                                                                                                                                                                         ### Properties                                                                                                                                                                                                                                                                                                                                                                          ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [App](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1ae86b508da665139059867ecc93b31306)             | [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) Returns the [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) instance to which this [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) belongs.                                                                               |
| [DefaultInstance](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1a749529aa86720c4e2356fda3b1847afe) | `static `[FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) Gets the instance of [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) for the default [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) with the default `database name`. |
| [LogLevel](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1aad122e86847cc114fb99685c259b9918)        | `static `[LogLevel](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase_1ae165d1d7bc3d85e1c0463a2a1d9ced9a) Sets the log verbosity of all [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) instances.                                                                                                                                                                                                                                     |
| [Settings](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1af8696a1cc7249ef8b9a5822faced082e)        | [FirebaseFirestoreSettings](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore-settings#class_firebase_1_1_firestore_1_1_firebase_firestore_settings) The settings of this [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) object.                                                                                                                                                      |

|                                                                                                                                                                                                                                                                                                                                                                                                                                      ### Public static functions                                                                                                                                                                                                                                                                                                                                                                                                                                       ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GetInstance](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1a4d63d6d4648991227fc0a5a232b6130f)`(`[FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)` app)`                  | [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) Gets an instance of [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) for a specific [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) with the default `database name`. |
| [GetInstance](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1a942e0701562b63c95abfcb19355b6053)`(string database)`                                                                                                                                    | [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) Gets an instance of [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) for the default [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) with a spesific `database name`. |
| [GetInstance](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1a4c1e7de94917956a732b083f4c554b68)`(`[FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)` app, string database)` | [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) Gets an instance of [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) for a specific [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) with a spesific `database name`.  |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ClearPersistenceAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1a9d69ad6ee4a4af0ab87f2eef5e5be2cf)`()`                                                                                                                                                                                                                                                                                                                                                                      | `Task` Clears the persistent storage.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Collection](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1a76bd067ebaf630d635efe59b7e12b98e)`(string path)`                                                                                                                                                                                                                                                                                                                                                                      | [CollectionReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/collection-reference#class_firebase_1_1_firestore_1_1_collection_reference) Creates a local [CollectionReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/collection-reference#class_firebase_1_1_firestore_1_1_collection_reference) for the given path, which must include an odd number of slash-separated identifiers.       |
| [CollectionGroup](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1af5df021d7f7665b0536bdab45ae6cf42)`(string collectionId)`                                                                                                                                                                                                                                                                                                                                                         | [Query](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query) Creates and returns a new [Query](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query) that includes all documents in the database that are contained in a collection or subcollection with the given collection ID.                                            |
| [DisableNetworkAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1a5b2228b100fd1519b90f2b95732dd724)`()`                                                                                                                                                                                                                                                                                                                                                                        | `Task` Disables network access for this instance.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Document](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1aac775eab0ff99ecba88dca51138dcaeb)`(string path)`                                                                                                                                                                                                                                                                                                                                                                        | [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference) Creates a local [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference) for the given path, which must include an even number of slash-separated identifiers.                  |
| [EnableNetworkAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1a7f6e9538891b26d9f80c7944c942160c)`()`                                                                                                                                                                                                                                                                                                                                                                         | `Task` Re-enables network usage for this instance after a prior call to [FirebaseFirestore.DisableNetworkAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1a5b2228b100fd1519b90f2b95732dd724).                                                                                                                                                              |
| [GetNamedQueryAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1a20ad4aafb9a718afdce5ac176352a1dc)`(string queryName)`                                                                                                                                                                                                                                                                                                                                                         | `Task< `[Query](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query)` >` Reads a [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore)[Query](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query) from the local cache, identified by the given name. |
| [ListenForSnapshotsInSync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1a95daf80ec4a099629660e2bee7ef96df)`(Action callback)`                                                                                                                                                                                                                                                                                                                                                    | [ListenerRegistration](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/listener-registration#class_firebase_1_1_firestore_1_1_listener_registration) Attaches a listener for a snapshots-in-sync event.                                                                                                                                                                                                                                  |
| [LoadBundleAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1ab74ab48cfaf0e5dd985e7a60fa60dea0)`(string bundleData)`                                                                                                                                                                                                                                                                                                                                                           | `Task< `[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/load-bundle-task-progress#class_firebase_1_1_firestore_1_1_load_bundle_task_progress)` >` Loads a [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) bundle into the local cache.                                                                                              |
| [LoadBundleAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1ae3825a1b4f18a8d6eaa3586bddb8a9d8)`(string bundleData, System.EventHandler< `[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/load-bundle-task-progress#class_firebase_1_1_firestore_1_1_load_bundle_task_progress)` > progressHandler)`                                                                                                                        | `Task< `[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/load-bundle-task-progress#class_firebase_1_1_firestore_1_1_load_bundle_task_progress)` >` Loads a [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) bundle into the local cache, taking an System.EventHandler to monitor loading progress.                                   |
| [LoadBundleAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1aa9cae33c94a9fe15495e5177cd126c01)`(byte[] bundleData)`                                                                                                                                                                                                                                                                                                                                                           | `Task< `[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/load-bundle-task-progress#class_firebase_1_1_firestore_1_1_load_bundle_task_progress)` >` Loads a [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) bundle into the local cache.                                                                                              |
| [LoadBundleAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1ae12fe5931caf9c18b12653318e746c1a)`(byte[] bundleData, System.EventHandler< `[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/load-bundle-task-progress#class_firebase_1_1_firestore_1_1_load_bundle_task_progress)` > progressHandler)`                                                                                                                        | `Task< `[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/load-bundle-task-progress#class_firebase_1_1_firestore_1_1_load_bundle_task_progress)` >` Loads a [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) bundle into the local cache, taking an System.EventHandler to monitor loading progress.                                   |
| [RunTransactionAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1a5dd9d4668863426fefa06221068f3d6e)`(Func< `[Transaction](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/transaction#class_firebase_1_1_firestore_1_1_transaction)`, Task > callback)`                                                                                                                                                                                              | `Task` Runs a transaction asynchronously, with an asynchronous callback that doesn't return a value.                                                                                                                                                                                                                                                                                                                                                               |
| [RunTransactionAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1a88e8608bf7f1a216d2a33a123a371ab4)`(`[TransactionOptions](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/transaction-options#class_firebase_1_1_firestore_1_1_transaction_options)` options, Func< `[Transaction](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/transaction#class_firebase_1_1_firestore_1_1_transaction)`, Task > callback)`          | `Task` Runs a transaction asynchronously, with an asynchronous callback that doesn't return a value.                                                                                                                                                                                                                                                                                                                                                               |
| [RunTransactionAsync< T >](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1ad2630a3f8d257790cf12648f05bebb1c)`(Func< `[Transaction](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/transaction#class_firebase_1_1_firestore_1_1_transaction)`, Task< T >> callback)`                                                                                                                                                                                     | `Task< T >` Runs a transaction asynchronously, with an asynchronous callback that returns a value.                                                                                                                                                                                                                                                                                                                                                                 |
| [RunTransactionAsync< T >](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1ae1929948d2e62998dd5631ec89ebd8cb)`(`[TransactionOptions](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/transaction-options#class_firebase_1_1_firestore_1_1_transaction_options)` options, Func< `[Transaction](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/transaction#class_firebase_1_1_firestore_1_1_transaction)`, Task< T >> callback)` | `Task< T >` Runs a transaction asynchronously, with an asynchronous callback that returns a value.                                                                                                                                                                                                                                                                                                                                                                 |
| [StartBatch](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1ab2d183efdb86e5f3f52f42877b51ae4f)`()`                                                                                                                                                                                                                                                                                                                                                                                 | [WriteBatch](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/write-batch#class_firebase_1_1_firestore_1_1_write_batch) Creates a write batch, which can be used to commit multiple mutations atomically.                                                                                                                                                                                                                                 |
| [TerminateAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1a083e8274501d2b51bc11abd03d63149c)`()`                                                                                                                                                                                                                                                                                                                                                                             | `Task` Terminates this [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) instance.                                                                                                                                                                                                                                                             |
| [WaitForPendingWritesAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1aef0eedc7070139b0d50a8488cfe201ff)`()`                                                                                                                                                                                                                                                                                                                                                                  | `Task` Waits until all currently pending writes for the active user have been acknowledged by the backend.                                                                                                                                                                                                                                                                                                                                                         |

## Properties

### App

```c#
FirebaseApp App
```  
Returns the [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) instance to which this [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) belongs.  

### DefaultInstance

```c#
static FirebaseFirestore DefaultInstance
```  
Gets the instance of [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) for the default [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) with the default `database name`.

A [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) instance.  

### LogLevel

```c#
static LogLevel LogLevel
```  
Sets the log verbosity of all [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) instances.

The default verbosity level is [Info](https://firebase.google.com/docs/reference/unity/other/) Set to [Debug](https://firebase.google.com/docs/reference/unity/other/) to turn on the diagnostic logging.

The desired verbosity.  

### Settings

```c#
FirebaseFirestoreSettings Settings
```  
The settings of this [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) object.

To change the settings used by this [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) instance, simply change the values of the properties on this [FirebaseFirestoreSettings](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore-settings#class_firebase_1_1_firestore_1_1_firebase_firestore_settings) object.

Invoking any non-static method on this [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) instance will "lock
in" the settings. No changes are allowed to be made to the settings once they are locked in. Attempting to do so will result in an exception being thrown by the property setter.

## Public static functions

### GetInstance

```c#
FirebaseFirestore GetInstance(
  FirebaseApp app
)
```  
Gets an instance of [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) for a specific [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) with the default `database name`.

<br />

|                                                                                                                                                                                                                                                                                                                                                  Details                                                                                                                                                                                                                                                                                                                                                   ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `app` | The [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) for which to get a [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) instance. | |
| **Returns** | A [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

### GetInstance

```c#
FirebaseFirestore GetInstance(
  string database
)
```  
Gets an instance of [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) for the default [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) with a spesific `database name`.

<br />

|                                                                                            Details                                                                                             ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|---------------------------------------------------| | `database` | The customized name for the `database`. instance. |                                             |
| **Returns** | A [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) instance. |

### GetInstance

```c#
FirebaseFirestore GetInstance(
  FirebaseApp app,
  string database
)
```  
Gets an instance of [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) for a specific [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) with a spesific `database name`.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `app`       | The [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) for which to get a [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) | | Parameters  | |------------|---------------------------------------------------| | `database` | The customized name for the `database`. instance. |                                                                                                                                                                                    | | **Returns** | A [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) instance.                                                                                                                                        | |

## Public functions

### ClearPersistenceAsync

```c#
Task ClearPersistenceAsync()
```  
Clears the persistent storage.

This includes pending writes and cached documents.

Must be called while the [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) instance is not started (after the app is shut down or when the app is first initialized). On startup, this method must be called before other methods (other than getting or setting [FirebaseFirestoreSettings](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore-settings#class_firebase_1_1_firestore_1_1_firebase_firestore_settings)). If the [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) instance is still running, the task will complete with an error code of `FailedPrecondition`.

Note: [ClearPersistenceAsync()](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1a9d69ad6ee4a4af0ab87f2eef5e5be2cf) is primarily intended to help write reliable tests that use [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore). It uses the most efficient mechanism possible for dropping existing data but does not attempt to securely overwrite or otherwise make cached data unrecoverable. For applications that are sensitive to the disclosure of cache data in between user sessions we strongly recommend not to enable persistence in the first place.

<br />

|                                         Details                                         ||
|-------------|----------------------------------------------------------------------------|
| **Returns** | A Task which completes when the clear persistence operation has completed. |

### Collection

```c#
CollectionReference Collection(
  string path
)
```  
Creates a local [CollectionReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/collection-reference#class_firebase_1_1_firestore_1_1_collection_reference) for the given path, which must include an odd number of slash-separated identifiers.

This does not perform any remote operations.

<br />

|                                                            Details                                                             ||
|-------------|-------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------|---------------------------------------------| | `path` | The collection path, e.g. `col1/doc1/col2`. | |
| **Returns** | A collection reference.                                                                                           |

### CollectionGroup

```c#
Query CollectionGroup(
  string collectionId
)
```  
Creates and returns a new [Query](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query) that includes all documents in the database that are contained in a collection or subcollection with the given collection ID.

<br />

|                                                                                                                                                                                             Details                                                                                                                                                                                              ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `collectionId` | Identifies the collections to query over. Every collection or subcollection with this ID as the last segment of its path will be included. Must not contain a slash. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query).                                                                                                                                                                                                                                        |

### DisableNetworkAsync

```c#
Task DisableNetworkAsync()
```  
Disables network access for this instance.

While the network is disabled, any snapshot listeners or `GetSnapshotAsync` calls will return results from cache, and any write operations will be queued until network usage is re-enabled via a call to [FirebaseFirestore.EnableNetworkAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1a7f6e9538891b26d9f80c7944c942160c).

<br />

|                             Details                              ||
|-------------|-----------------------------------------------------|
| **Returns** | A task which completes once networking is disabled. |

### Document

```c#
DocumentReference Document(
  string path
)
```  
Creates a local [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference) for the given path, which must include an even number of slash-separated identifiers.

This does not perform any remote operations.

<br />

|                                                               Details                                                                ||
|-------------|-------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------|------------------------------------------------| | `path` | The document path, e.g. `col1/doc1/col2/doc2`. | |
| **Returns** | A document reference.                                                                                                   |

### EnableNetworkAsync

```c#
Task EnableNetworkAsync()
```  
Re-enables network usage for this instance after a prior call to [FirebaseFirestore.DisableNetworkAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1a5b2228b100fd1519b90f2b95732dd724).

<br />

|                             Details                             ||
|-------------|----------------------------------------------------|
| **Returns** | A task which completes once networking is enabled. |

### GetNamedQueryAsync

```c#
Task< Query > GetNamedQueryAsync(
  string queryName
)
```  
Reads a [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore)[Query](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query) from the local cache, identified by the given name.

Named queries are packaged into bundles on the server side (along with the resulting documents) and loaded into local cache using [FirebaseFirestore.LoadBundleAsync(string)](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1ab74ab48cfaf0e5dd985e7a60fa60dea0). Once in the local cache, you can use this method to extract a query by name.

<br />

|                                                                             Details                                                                             ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------------|---------------------------------------------------| | `queryName` | The name of the query to read from saved bundles. |            |
| **Returns** | A task that is completed with the query associated with the given name. The result of the returned task is set to null if no queries can be found. |

### ListenForSnapshotsInSync

```c#
ListenerRegistration ListenForSnapshotsInSync(
  Action callback
)
```  
Attaches a listener for a snapshots-in-sync event.

The snapshots-in-sync event indicates that all listeners affected by a given change have fired, even if a single server-generated change affects multiple listeners.

NOTE: The snapshots-in-sync event only indicates that listeners are in sync with each other, but does not relate to whether those snapshots are in sync with the server. Use [SnapshotMetadata](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/snapshot-metadata#class_firebase_1_1_firestore_1_1_snapshot_metadata) in the individual listeners to determine if a snapshot is from the cache or the server.

<br />

|                                                                                                                                                            Details                                                                                                                                                             ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|-----------------------------------------------------------------------------------------------------------------------------------------| | `callback` | A callback to be called every time all snapshot listeners are in sync with each other. The callback will be invoked on the main thread. | |
| **Returns** | A registration object that can be used to remove the listener.                                                                                                                                                                                                                                                    |

### LoadBundleAsync

```c#
Task< LoadBundleTaskProgress > LoadBundleAsync(
  string bundleData
)
```  
Loads a [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) bundle into the local cache.

<br />

|                                                                        Details                                                                         ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------------|--------------------------| | `bundleData` | The bundle to be loaded. |                                                   |
| **Returns** | A task that is completed when the loading is completed. The result of the task then contains the final progress of the loading operation. |

### LoadBundleAsync

```c#
Task< LoadBundleTaskProgress > LoadBundleAsync(
  string bundleData,
  System.EventHandler< LoadBundleTaskProgress > progressHandler
)
```  
Loads a [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) bundle into the local cache, taking an System.EventHandler to monitor loading progress.

<br />

|                                                                                                                                                                                                                                                              Details                                                                                                                                                                                                                                                              ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------------------|------------------------------------------------------------------------------------------------------------------------------------------------| | `bundleData`      | The bundle to be loaded.                                                                                                                       | | `progressHandler` | A System.EventHandler that is notified with progress updates, and completion or error updates. The handler will be invoked on the main thread. | |
| **Returns** | A task that is completed when the loading is completed. The result of the task then contains the final progress of the loading operation.                                                                                                                                                                                                                                                                                                                                                                            |

### LoadBundleAsync

```c#
Task< LoadBundleTaskProgress > LoadBundleAsync(
  byte[] bundleData
)
```  
Loads a [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) bundle into the local cache.

<br />

|                                                                              Details                                                                               ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------------|---------------------------------------------------------| | `bundleData` | The bundle to be loaded, as a UTF-8 encoded byte array. | |
| **Returns** | A task that is completed when the loading is completed. The result of the task then contains the final progress of the loading operation.             |

### LoadBundleAsync

```c#
Task< LoadBundleTaskProgress > LoadBundleAsync(
  byte[] bundleData,
  System.EventHandler< LoadBundleTaskProgress > progressHandler
)
```  
Loads a [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) bundle into the local cache, taking an System.EventHandler to monitor loading progress.

<br />

|                                                                                                                                                                                                                                                               Details                                                                                                                                                                                                                                                                ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------| | `bundleData`      | The bundle to be loaded, as a UTF8 encoded byte array.                                                                                          | | `progressHandler` | An System.EventHandler that is notified with progress updates, and completion or error updates. The handler will be invoked on the main thread. | |
| **Returns** | A task that is completed when the loading is completed. The result of the task then contains the final progress of the loading operation.                                                                                                                                                                                                                                                                                                                                                                               |

### RunTransactionAsync

```c#
Task RunTransactionAsync(
  Func< Transaction, Task > callback
)
```  
Runs a transaction asynchronously, with an asynchronous callback that doesn't return a value.

The specified callback is executed for a newly-created transaction.

`RunTransactionAsync` executes the given callback on the main thread and then attempts to commit the changes applied within the transaction. If any document read within the transaction has changed, the *callback* will be retried. If it fails to commit after 5 attempts, the transaction will fail.

The maximum number of writes allowed in a single transaction is 500, but note that each usage of [FieldValue.ServerTimestamp](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value_1a6a7acc0716c4387af701ed5b250575a2), [FieldValue.ArrayUnion](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value_1ac05084586564ce5d391bc35d9422d479), [FieldValue.ArrayRemove](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value_1a4bd53bf887e9f9e1425ccef0eb35026a), or [FieldValue.Increment](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value_1a9744159debfe114ea4d21ab2b0a81c19) inside a transaction counts as an additional write.

<br />

|                                                                                                                  Details                                                                                                                   ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|-----------------------------------------------------------------------------------------------| | `callback` | The callback to execute. Must not be `null`. The callback will be invoked on the main thread. | |
| **Returns** | A task which completes when the transaction has committed.                                                                                                                                                                    |

### RunTransactionAsync

```c#
Task RunTransactionAsync(
  TransactionOptions options,
  Func< Transaction, Task > callback
)
```  
Runs a transaction asynchronously, with an asynchronous callback that doesn't return a value.

The specified callback is executed for a newly-created transaction.

`RunTransactionAsync` executes the given callback on the main thread and then attempts to commit the changes applied within the transaction. If any document read within the transaction has changed, the *callback* will be retried. If it fails to commit after the maximum number of attempts specified in the given [TransactionOptions](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/transaction-options#class_firebase_1_1_firestore_1_1_transaction_options) object, the transaction will fail.

The maximum number of writes allowed in a single transaction is 500, but note that each usage of [FieldValue.ServerTimestamp](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value_1a6a7acc0716c4387af701ed5b250575a2), [FieldValue.ArrayUnion](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value_1ac05084586564ce5d391bc35d9422d479), [FieldValue.ArrayRemove](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value_1a4bd53bf887e9f9e1425ccef0eb35026a), or [FieldValue.Increment](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value_1a9744159debfe114ea4d21ab2b0a81c19) inside a transaction counts as an additional write.

<br />

|                                                                                                                                                                          Details                                                                                                                                                                          ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|-----------------------------------------------------------------------------------------------| | `options`  | The transaction options for controlling execution. Must not be `null`.                        | | `callback` | The callback to execute. Must not be `null`. The callback will be invoked on the main thread. | |
| **Returns** | A task which completes when the transaction has committed.                                                                                                                                                                                                                                                                                   |

### RunTransactionAsync\< T \>

```c#
Task< T > RunTransactionAsync< T >(
  Func< Transaction, Task< T >> callback
)
```  
Runs a transaction asynchronously, with an asynchronous callback that returns a value.

The specified callback is executed for a newly-created transaction.

`RunTransactionAsync` executes the given callback on the main thread and then attempts to commit the changes applied within the transaction. If any document read within the transaction has changed, the *callback* will be retried. If it fails to commit after 5 attempts, the transaction will fail.

The maximum number of writes allowed in a single transaction is 500, but note that each usage of [FieldValue.ServerTimestamp](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value_1a6a7acc0716c4387af701ed5b250575a2), [FieldValue.ArrayUnion](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value_1ac05084586564ce5d391bc35d9422d479), [FieldValue.ArrayRemove](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value_1a4bd53bf887e9f9e1425ccef0eb35026a), or [FieldValue.Increment](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value_1a9744159debfe114ea4d21ab2b0a81c19) inside a transaction counts as an additional write.

<br />

|                                                                                                                      Details                                                                                                                       ||
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Template Parameters | |-----|----------------------------------| | `T` | The result type of the callback. |                                                                                                                                         |
| Parameters          | |------------|-----------------------------------------------------------------------------------------------| | `callback` | The callback to execute. Must not be `null`. The callback will be invoked on the main thread. | |
| **Returns**         | A task which completes when the transaction has committed. The result of the task then contains the result of the callback.                                                                                                   |

### RunTransactionAsync\< T \>

```c#
Task< T > RunTransactionAsync< T >(
  TransactionOptions options,
  Func< Transaction, Task< T >> callback
)
```  
Runs a transaction asynchronously, with an asynchronous callback that returns a value.

The specified callback is executed for a newly-created transaction.

`RunTransactionAsync` executes the given callback on the main thread and then attempts to commit the changes applied within the transaction. If any document read within the transaction has changed, the *callback* will be retried. If it fails to commit after the maximum number of attempts specified in the given [TransactionOptions](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/transaction-options#class_firebase_1_1_firestore_1_1_transaction_options) object, the transaction will fail.

The maximum number of writes allowed in a single transaction is 500, but note that each usage of [FieldValue.ServerTimestamp](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value_1a6a7acc0716c4387af701ed5b250575a2), [FieldValue.ArrayUnion](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value_1ac05084586564ce5d391bc35d9422d479), [FieldValue.ArrayRemove](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value_1a4bd53bf887e9f9e1425ccef0eb35026a), or [FieldValue.Increment](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-value#class_firebase_1_1_firestore_1_1_field_value_1a9744159debfe114ea4d21ab2b0a81c19) inside a transaction counts as an additional write.

<br />

|                                                                                                                                                                              Details                                                                                                                                                                              ||
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Template Parameters | |-----|----------------------------------| | `T` | The result type of the callback. |                                                                                                                                                                                                                                                        |
| Parameters          | |------------|-----------------------------------------------------------------------------------------------| | `options`  | The transaction options for controlling execution. Must not be `null`.                        | | `callback` | The callback to execute. Must not be `null`. The callback will be invoked on the main thread. | |
| **Returns**         | A task which completes when the transaction has committed. The result of the task then contains the result of the callback.                                                                                                                                                                                                                  |

### StartBatch

```c#
WriteBatch StartBatch()
```  
Creates a write batch, which can be used to commit multiple mutations atomically.

<br />

|                    Details                    ||
|-------------|----------------------------------|
| **Returns** | A write batch for this database. |

### TerminateAsync

```c#
Task TerminateAsync()
```  
Terminates this [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) instance.

After calling `Terminate()`, only the [ClearPersistenceAsync()](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1a9d69ad6ee4a4af0ab87f2eef5e5be2cf) method may be used. Calling any other method will result in an error.

To restart after termination, simply create a new instance of [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) with [GetInstance()](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1a4d63d6d4648991227fc0a5a232b6130f) methods.

`Terminate()` does not cancel any pending writes, and any tasks that are awaiting a response from the server will not be resolved. The next time you start this instance, it will resume attempting to send these writes to the server.

Note: under normal circumstances, calling `Terminate()` is not required. This method is useful only when you want to force this instance to release all of its resources or in combination with `ClearPersistenceAsync` to ensure that all local state is destroyed between test runs.

<br />

|                                         Details                                         ||
|-------------|----------------------------------------------------------------------------|
| **Returns** | A Task which completes when the instance has been successfully terminated. |

### WaitForPendingWritesAsync

```c#
Task WaitForPendingWritesAsync()
```  
Waits until all currently pending writes for the active user have been acknowledged by the backend.

The returned Task completes immediately if there are no outstanding writes. Otherwise, the Task waits for all previously issued writes (including those written in a previous app session), but it does not wait for writes that were added after the method is called. If you wish to wait for additional writes, you have to call [WaitForPendingWritesAsync()](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1aef0eedc7070139b0d50a8488cfe201ff) again.

Any outstanding [WaitForPendingWritesAsync()](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1aef0eedc7070139b0d50a8488cfe201ff) Tasks are cancelled during user changes.

<br />

|                                                   Details                                                    ||
|-------------|-------------------------------------------------------------------------------------------------|
| **Returns** | A Task which completes when all currently pending writes have been acknowledged by the backend. |