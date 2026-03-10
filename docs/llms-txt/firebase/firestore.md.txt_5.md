# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore.md.txt

# firebase::firestore::Firestore Class Reference

# firebase::firestore::Firestore


`#include <firestore.h>`

Entry point for the Firebase [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) C++ SDK.

## Summary

To use the SDK, call [firebase::firestore::Firestore::GetInstance()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a70e6c3b21fa6422ba9083d5493ccb3ab) to obtain an instance of [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore), then use [Collection()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a83b02dae6bb331080ec27ca1f813c258) or [Document()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a0b6c26a1ca9f4d56e741083f21c24162) to obtain references to child paths within the database. From there, you can set data via [CollectionReference::Add()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference_1a7c2d173c29e6264ef9e0cba8cc367505) and [DocumentReference::Set()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1ace49a9db5c4c1f68ab85a36b1738eebc), or get data via [CollectionReference::Get()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a3bf794938d8680d31b799c3f58664375) and [DocumentReference::Get()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1a7c1711d91dd8e025642bb1bc793dc6c8), attach listeners, and more.


> [!NOTE]
> **Note:** [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

<br />

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1af30801a3e89994a9a024ec0a263af21e(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore & src)` Deleted copy constructor; [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) must be created with [Firestore::GetInstance()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a70e6c3b21fa6422ba9083d5493ccb3ab). ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a2928d0f91f517f15a73c5ad6a4ed94bd()` Destructor for the [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) object. ||

| ### Friend classes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1afa20e8bdfeec8f8191cd8ad8a2a8ce77` | `friend class` |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a03b5b43aafe5e8742f2af98d5fb5054a` | `friend class` |

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a70e6c3b21fa6422ba9083d5493ccb3ab(::https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app *app, https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478 *init_result_out)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore *` Returns an instance of [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) corresponding to the given [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with default database ID. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1ac6ddc65ddfd623a99351b35a1f652b2b(https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478 *init_result_out)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore *` Returns an instance of [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) corresponding to the default [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with default database ID. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a30ad1071f7335b85309a36055b0ced11(::https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app *app, const char *db_name, https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478 *init_result_out)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore *` Returns an instance of [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) corresponding to the given [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with the given database ID. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a02498c868f03bbee43816475cc36cd3c(const char *db_name, https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478 *init_result_out)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore *` Returns an instance of [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) corresponding to the default [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with the given database ID. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1af10daa3d7a5af55931934cfed8a62bee(https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a52d8f08cc8edeccdb334bf5c121aa698 log_level)` | `void` Sets the log verbosity of all [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instances. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a377bf2232a3234157152be9ecb70814d(std::function< void()> callback)` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration` Attaches a listener for a snapshots-in-sync event. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a76345e1002be861441e844deae3981ee()` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Clears the persistent storage. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a83b02dae6bb331080ec27ca1f813c258(const char *collection_path) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference` Returns a [CollectionReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference) instance that refers to the collection at the specified path within the database. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1acef772624e1337ebe47bf09e66f795d5(const std::string & collection_path) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference` Returns a [CollectionReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference) instance that refers to the collection at the specified path within the database. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a1b459a494f2b291541bef6eac2228bc8(const char *collection_id) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Returns a [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) instance that includes all documents in the database that are contained in a collection or subcollection with the given collection_id. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1ac58367f229aa63d270f0bda4b6315734(const std::string & collection_id) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Returns a [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) instance that includes all documents in the database that are contained in a collection or subcollection with the given collection_id. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a5f5170387a4b5822386c0b613f4c299d()` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Disables network access for this instance. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a0b6c26a1ca9f4d56e741083f21c24162(const char *document_path) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` Returns a [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) instance that refers to the document at the specified path within the database. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1afff0490b3fff857a95555ea881b0ccbf(const std::string & document_path) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` Returns a [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) instance that refers to the document at the specified path within the database. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1af09f56940a5c79b93f7cd2cfe022bd9f()` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Re-enables network usage for this instance after a prior call to [DisableNetwork()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a5f5170387a4b5822386c0b613f4c299d). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a1c5fe987b5a850f731885884f22173fd(const std::string & bundle)` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/load-bundle-task-progress#classfirebase_1_1firestore_1_1_load_bundle_task_progress >` Loads a [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) bundle into the local cache. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a050055b05cbc75def348eda07418b0a1(const std::string & bundle, std::function< void(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/load-bundle-task-progress#classfirebase_1_1firestore_1_1_load_bundle_task_progress &)> progress_callback)` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/load-bundle-task-progress#classfirebase_1_1firestore_1_1_load_bundle_task_progress >` Loads a [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) bundle into the local cache, with the provided callback executed for progress updates. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a826cad4b2bc5541aa277ddd42797f2cf(const std::string & query_name)` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query >` Reads a [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore)`https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` from the local cache, identified by the given name. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1ad82d5378fb9807f472d3d2bdaa12e696(std::function< https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1acbed0dcd73b55ce5a9d9c3d07bb9cac5(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction#classfirebase_1_1firestore_1_1_transaction &, std::string &)> update)` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Executes the given update and then attempts to commit the changes applied within the transaction. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a4e8df1780d39c194e001557a108a332e(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options options, std::function< https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1acbed0dcd73b55ce5a9d9c3d07bb9cac5(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction#classfirebase_1_1firestore_1_1_transaction &, std::string &)> update)` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Executes the given update and then attempts to commit the changes applied within the transaction. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a963f7afb651d465d1617dc9717f0b537()` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Terminates this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore` instance. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a6b13e14eab5940f54d9de303dcbc0799()` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Waits until all currently pending writes for the active user have been acknowledged by the backend. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1ad81ddd53717b00ba4a94214c8af1872c() const ` | `virtual const https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app *` Returns the [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) that this [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) was created with. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a8a6f824bb5b32ce55bbca12c09602a56()` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app *` Returns the [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) that this [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) was created with. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1aad9671551841c1ad6833e611aebaef2f() const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch` Creates a write batch, used for performing multiple writes as a single atomic operation. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a83c511b700d0eca272d7928dd372dae9(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore & src)=delete` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore &` Deleted copy assignment operator; [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) must be created with [Firestore::GetInstance()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a70e6c3b21fa6422ba9083d5493ccb3ab). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a1f66673a54ef76ffd3123cabad46b405(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings settings)` | `virtual void` Sets any custom settings used to configure this [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) object. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a1f447d52e8356465964edaf698f3aca5() const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings` Returns the settings used by this [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) object. |

| ### Protected functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a0578e000e0f165b6e28a10be038e66ab()=default` | ` ``` Default constructor, to be used only for mocking `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore`. `` |

## Friend classes

### csharp::ApiHeaders

```c++
friend class csharp::ApiHeaders
```

### csharp::TransactionManager

```c++
friend class csharp::TransactionManager
```

## Public static functions

### GetInstance

```c++
Firestore * GetInstance(
  ::firebase::App *app,
  InitResult *init_result_out
)
```
Returns an instance of [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) corresponding to the given [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with default database ID.

Firebase [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) uses [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) to communicate with Firebase Authentication to authenticate users to the [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) server backend.

If you call [GetInstance()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a70e6c3b21fa6422ba9083d5493ccb3ab) multiple times with the same [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app), you will get the same instance of [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `app` | Your instance of [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app). Firebase [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) will use this to communicate with Firebase Authentication. | | `init_result_out` | If provided, the initialization result will be written here. Will be set to [firebase::kInitResultSuccess](https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478a11c8441be81525f6c644baf36f8aed3b) if initialization succeeded, or [firebase::kInitResultFailedMissingDependency](https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478a1c28184b82cd2bece405e416ebc24b5d) on Android if Google Play services is not available on the current device. | |
| **Returns** | An instance of [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) corresponding to the given [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with default database ID. |

### GetInstance

```c++
Firestore * GetInstance(
  InitResult *init_result_out
)
```
Returns an instance of [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) corresponding to the default [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with default database ID.

Firebase [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) uses the default [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) to communicate with Firebase Authentication to authenticate users to the [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) server backend.

If you call [GetInstance()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a70e6c3b21fa6422ba9083d5493ccb3ab) multiple times, you will get the same instance.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `init_result_out` | If provided, the initialization result will be written here. Will be set to [firebase::kInitResultSuccess](https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478a11c8441be81525f6c644baf36f8aed3b) if initialization succeeded, or [firebase::kInitResultFailedMissingDependency](https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478a1c28184b82cd2bece405e416ebc24b5d) on Android if Google Play services is not available on the current device. | |
| **Returns** | An instance of [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) corresponding to the default [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with default database ID. |

### GetInstance

```c++
Firestore * GetInstance(
  ::firebase::App *app,
  const char *db_name,
  InitResult *init_result_out
)
```
Returns an instance of [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) corresponding to the given [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with the given database ID.

Firebase [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) uses [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) to communicate with Firebase Authentication to authenticate users to the [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) server backend.

If you call [GetInstance()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a70e6c3b21fa6422ba9083d5493ccb3ab) multiple times with the same [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app), you will get the same instance of [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `app` | Your instance of [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app). Firebase [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) will use this to communicate with Firebase Authentication. | | `db_name` | Name of the database. Firebase [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) will use this to communicate with Firebase Authentication. | | `init_result_out` | If provided, the initialization result will be written here. Will be set to [firebase::kInitResultSuccess](https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478a11c8441be81525f6c644baf36f8aed3b) if initialization succeeded, or [firebase::kInitResultFailedMissingDependency](https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478a1c28184b82cd2bece405e416ebc24b5d) on Android if Google Play services is not available on the current device. | |
| **Returns** | An instance of [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) corresponding to the given [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with the given database ID. |

### GetInstance

```c++
Firestore * GetInstance(
  const char *db_name,
  InitResult *init_result_out
)
```
Returns an instance of [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) corresponding to the default [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with the given database ID.

Firebase [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) uses [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) to communicate with Firebase Authentication to authenticate users to the [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) server backend.

If you call [GetInstance()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a70e6c3b21fa6422ba9083d5493ccb3ab) multiple times with the same [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app), you will get the same instance of [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `db_name` | Name of the database. Firebase [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) will use this to communicate with Firebase Authentication. | | `init_result_out` | If provided, the initialization result will be written here. Will be set to [firebase::kInitResultSuccess](https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478a11c8441be81525f6c644baf36f8aed3b) if initialization succeeded, or [firebase::kInitResultFailedMissingDependency](https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478a1c28184b82cd2bece405e416ebc24b5d) on Android if Google Play services is not available on the current device. | |
| **Returns** | An instance of [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) corresponding to the default [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with the given database ID. |

### set_log_level

```c++
void set_log_level(
  LogLevel log_level
)
```
Sets the log verbosity of all [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instances.

The default verbosity level is `kLogLevelInfo`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `log_level` | The desired verbosity. | |

## Public functions

### AddSnapshotsInSyncListener

```c++
virtual ListenerRegistration AddSnapshotsInSyncListener(
  std::function< void()> callback
)
```
Attaches a listener for a snapshots-in-sync event.

Server-generated updates and local changes can affect multiple snapshot listeners. The snapshots-in-sync event indicates that all listeners affected by a given change have fired.

NOTE: The snapshots-in-sync event only indicates that listeners are in sync with each other, but does not relate to whether those snapshots are in sync with the server. Use `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata` in the individual listeners to determine if a snapshot is from the cache or the server.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `callback` | A callback to be called every time all snapshot listeners are in sync with each other. | |
| **Returns** | A `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration` object that can be used to remove the listener. |

### ClearPersistence

```c++
virtual Future< void > ClearPersistence()
```
Clears the persistent storage.

This includes pending writes and cached documents.

Must be called while the [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance is not started (after the app is shut down or when the app is first initialized). On startup, this method must be called before other methods (other than `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a1f447d52e8356465964edaf698f3aca5` and `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a1f66673a54ef76ffd3123cabad46b405`). If the [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance is still running, the function will complete with an error code of `FailedPrecondition`.

Note: `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a76345e1002be861441e844deae3981ee` is primarily intended to help write reliable tests that use [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore). It uses the most efficient mechanism possible for dropping existing data but does not attempt to securely overwrite or otherwise make cached data unrecoverable. For applications that are sensitive to the disclosure of cache data in between user sessions we strongly recommend not to enable persistence in the first place.

### Collection

```c++
virtual CollectionReference Collection(
  const char *collection_path
) const 
```
Returns a [CollectionReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference) instance that refers to the collection at the specified path within the database.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `collection_path` | A slash-separated path to a collection. | |
| **Returns** | The [CollectionReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference) instance. |

### Collection

```c++
virtual CollectionReference Collection(
  const std::string & collection_path
) const 
```
Returns a [CollectionReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference) instance that refers to the collection at the specified path within the database.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `collection_path` | A slash-separated path to a collection. | |
| **Returns** | The [CollectionReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference) instance. |

### CollectionGroup

```c++
virtual Query CollectionGroup(
  const char *collection_id
) const 
```
Returns a [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) instance that includes all documents in the database that are contained in a collection or subcollection with the given collection_id.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `collection_id` | Identifies the collections to query over. Every collection or subcollection with this ID as the last segment of its path will be included. Cannot contain a slash. | |
| **Returns** | The [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) instance. |

### CollectionGroup

```c++
virtual Query CollectionGroup(
  const std::string & collection_id
) const 
```
Returns a [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) instance that includes all documents in the database that are contained in a collection or subcollection with the given collection_id.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `collection_id` | Identifies the collections to query over. Every collection or subcollection with this ID as the last segment of its path will be included. Cannot contain a slash. | |
| **Returns** | The [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) instance. |

### DisableNetwork

```c++
virtual Future< void > DisableNetwork()
```
Disables network access for this instance.

While the network is disabled, any snapshot listeners or Get() calls will return results from cache, and any write operations will be queued until network usage is re-enabled via a call to [EnableNetwork()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1af09f56940a5c79b93f7cd2cfe022bd9f).

If the network was already disabled, calling `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a5f5170387a4b5822386c0b613f4c299d` again is a no-op.

### Document

```c++
virtual DocumentReference Document(
  const char *document_path
) const 
```
Returns a [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) instance that refers to the document at the specified path within the database.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `document_path` | A slash-separated path to a document. | |
| **Returns** | The [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) instance. |

### Document

```c++
virtual DocumentReference Document(
  const std::string & document_path
) const 
```
Returns a [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) instance that refers to the document at the specified path within the database.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `document_path` | A slash-separated path to a document. | |
| **Returns** | The [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) instance. |

### EnableNetwork

```c++
virtual Future< void > EnableNetwork()
```
Re-enables network usage for this instance after a prior call to [DisableNetwork()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a5f5170387a4b5822386c0b613f4c299d).

If the network is currently enabled, calling `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1af09f56940a5c79b93f7cd2cfe022bd9f` is a no-op.

### Firestore

```c++
 Firestore(
  const Firestore & src
)=delete
```
Deleted copy constructor; [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) must be created with [Firestore::GetInstance()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a70e6c3b21fa6422ba9083d5493ccb3ab).

### LoadBundle

```c++
virtual Future< LoadBundleTaskProgress > LoadBundle(
  const std::string & bundle
)
```
Loads a [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) bundle into the local cache.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `bundle` | A string containing the bundle to be loaded. | |
| **Returns** | A `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future` that is resolved when the loading is either completed or aborted due to an error. |

### LoadBundle

```c++
virtual Future< LoadBundleTaskProgress > LoadBundle(
  const std::string & bundle,
  std::function< void(const LoadBundleTaskProgress &)> progress_callback
)
```
Loads a [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) bundle into the local cache, with the provided callback executed for progress updates.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `bundle` | A string containing the bundle to be loaded. | | `progress_callback` | A callback that is called with progress updates, and completion or error updates. | |
| **Returns** | A `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future` that is resolved when the loading is either completed or aborted due to an error. |

### NamedQuery

```c++
virtual Future< Query > NamedQuery(
  const std::string & query_name
)
```
Reads a [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore)`https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` from the local cache, identified by the given name.

Named queries are packaged into bundles on the server side (along with the resulting documents) and loaded into local cache using `LoadBundle`. Once in the local cache, you can use this method to extract a query by name.

If a query cannot be found, the returned future will complete with its `error()` set to a non-zero error code.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `query_name` | The name of the query to read from saved bundles. | |

### RunTransaction

```c++
virtual Future< void > RunTransaction(
  std::function< Error(Transaction &, std::string &)> update
)
```
Executes the given update and then attempts to commit the changes applied within the transaction.

If any document read within the transaction has changed, the update function will be retried. If it fails to commit after 5 attempts, the transaction will fail.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `update` | function or lambda to execute within the transaction context. The string reference parameter can be used to set the error message. | |
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) that will be resolved when the transaction finishes. |

### RunTransaction

```c++
virtual Future< void > RunTransaction(
  TransactionOptions options,
  std::function< Error(Transaction &, std::string &)> update
)
```
Executes the given update and then attempts to commit the changes applied within the transaction.

If any document read within the transaction has changed, the update function will be retried. If it fails to commit after the `max_attempts` specified in the given `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction-options#classfirebase_1_1firestore_1_1_transaction_options`, the transaction will fail.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `options` | The transaction options for controlling execution. | | `update` | function or lambda to execute within the transaction context. The string reference parameter can be used to set the error message. | |
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) that will be resolved when the transaction finishes. |

### Terminate

```c++
virtual Future< void > Terminate()
```
Terminates this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore` instance.

After calling `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a963f7afb651d465d1617dc9717f0b537`, only the `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a76345e1002be861441e844deae3981ee` method may be used. Calling any other methods will result in an error.

To restart after termination, simply create a new instance of `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore` with `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a70e6c3b21fa6422ba9083d5493ccb3ab`.

`https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a963f7afb651d465d1617dc9717f0b537` does not cancel any pending writes and any tasks that are awaiting a response from the server will not be resolved. The next time you start this instance, it will resume attempting to send these writes to the server.

Note: under normal circumstances, calling `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a963f7afb651d465d1617dc9717f0b537` is not required. This method is useful only when you want to force this instance to release all of its resources or in combination with `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a76345e1002be861441e844deae3981ee` to ensure that all local state is destroyed between test runs.

<br />

| Details ||
|---|---|
| **Returns** | A `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future` that is resolved when the instance has been successfully terminated. |

### WaitForPendingWrites

```c++
virtual Future< void > WaitForPendingWrites()
```
Waits until all currently pending writes for the active user have been acknowledged by the backend.

The returned future is resolved immediately without error if there are no outstanding writes. Otherwise, the future is resolved when all previously issued writes (including those written in a previous app session) have been acknowledged by the backend. The future does not wait for writes that were added after the method is called. If you wish to wait for additional writes, you have to call `WaitForPendingWrites` again.

Any outstanding `WaitForPendingWrites` futures are resolved with an error during user change.

### app

```c++
virtual const App * app() const 
```
Returns the [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) that this [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) was created with.

<br />

| Details ||
|---|---|
| **Returns** | The [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) this [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) was created with. |

### app

```c++
virtual App * app()
```
Returns the [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) that this [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) was created with.

<br />

| Details ||
|---|---|
| **Returns** | The [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) this [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) was created with. |

### batch

```c++
virtual WriteBatch batch() const 
```
Creates a write batch, used for performing multiple writes as a single atomic operation.

Unlike transactions, write batches are persisted offline and therefore are preferable when you don't need to condition your writes on read data.

<br />

| Details ||
|---|---|
| **Returns** | The created [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch) object. |

### operator=

```c++
Firestore & operator=(
  const Firestore & src
)=delete
```
Deleted copy assignment operator; [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) must be created with [Firestore::GetInstance()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a70e6c3b21fa6422ba9083d5493ccb3ab).

### set_settings

```c++
virtual void set_settings(
  Settings settings
)
```
Sets any custom settings used to configure this [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) object.

### settings

```c++
virtual Settings settings() const 
```
Returns the settings used by this [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) object.

### \~Firestore

```c++
virtual  ~Firestore()
```
Destructor for the [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) object.

When deleted, this instance will be removed from the cache of [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) objects. If you call [GetInstance()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a70e6c3b21fa6422ba9083d5493ccb3ab) in the future with the same [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app), a new [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance will be created.

## Protected functions

### Firestore

```c++
 Firestore()=default
```
Default constructor, to be used only for mocking `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore`.