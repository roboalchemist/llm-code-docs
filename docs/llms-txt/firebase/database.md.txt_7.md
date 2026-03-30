# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/database/database.md.txt

# firebase::database::Database Class Reference

# firebase::database::Database


`#include <database.h>`

Entry point for the Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) C++ SDK.

## Summary

To use the SDK, call [firebase::database::Database::GetInstance()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1a09214ba62dbbdb86d3e48c452a97b6c1) to obtain an instance of [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database), then use [GetReference()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1adc2324f618f325e72f9e4b924519d6bd) to obtain references to child paths within the database. From there you can set data via Query::SetValue(), get data via [Query::GetValue()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/query#classfirebase_1_1database_1_1_query_1a562ab39d0575e2c8a8fbe2315ed52fb8), attach listeners, and more.

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1a4d704d84e11475a9ef0dd188346ab982()` Destructor for the [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) object. ||

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1a09214ba62dbbdb86d3e48c452a97b6c1(::https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app *app, https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478 *init_result_out)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database *` Get an instance of [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) corresponding to the given [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1a7cc6b25916dcbf1a352d3e3bf6de7a6d(::https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app *app, const char *url, https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478 *init_result_out)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database *` Gets an instance of FirebaseDatabase for the specified URL. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1adc2324f618f325e72f9e4b924519d6bd() const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference` Get a [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) to the root of the database. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1a51c770863a8076e426ce2b4a76ea5882(const char *path) const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference` Get a [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) for the specified path. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1a91b0d75a4241d5a30d50c1c8682c76fb(const char *url) const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference` Get a [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) for the provided URL, which must belong to the database URL this instance is already connected to. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1aa2cf08220af5ce6c8d1d51416fce2fc1()` | `void` Shuts down the connection to the Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) backend until [GoOnline()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1a683f584177a99d4288988f6870d57f19) is called. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1a683f584177a99d4288988f6870d57f19()` | `void` Resumes the connection to the Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) backend after a previous [GoOffline()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1aa2cf08220af5ce6c8d1d51416fce2fc1) call. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1a3e7d319ea9e0797f990e22ce4f8d3f63()` | `void` Purge all pending writes to the Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) server. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1a1a1992d59678ff5dca36b9d6507d5022() const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app *` Get the [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) that this [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) was created with. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1ae32369a14c4745e82810126b1ee32689() const ` | `https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a52d8f08cc8edeccdb334bf5c121aa698` Get the log verbosity of this [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) instance. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1a572cf0e0327c87e7a6a36f270dfec16b(https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a52d8f08cc8edeccdb334bf5c121aa698 log_level)` | `void` Set the log verbosity of this [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) instance. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1a80516f5ad9bed9465098b07224fe4eda(bool enabled)` | `void` Sets whether pending write data will persist between application exits. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1a367e2a6cd2ebb643b44a2bc0a2eb14af() const ` | `const char *` Get the URL that this [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) was created with. |

## Public static functions

### GetInstance

```c++
Database * GetInstance(
  ::firebase::App *app,
  InitResult *init_result_out
)
```
Get an instance of [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) corresponding to the given [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app).

Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) uses [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) to communicate with Firebase Authentication to authenticate users to the [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) server backend.

If you call [GetInstance()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1a09214ba62dbbdb86d3e48c452a97b6c1) multiple times with the same [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app), you will get the same instance of [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `app` | Your instance of [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app). Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) will use this to communicate with Firebase Authentication. | | `init_result_out` | Optional: If provided, write the init result here. Will be set to kInitResultSuccess if initialization succeeded, or kInitResultFailedMissingDependency on Android if Google Play services is not available on the current device. | |
| **Returns** | An instance of [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) corresponding to the given [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app). |

### GetInstance

```c++
Database * GetInstance(
  ::firebase::App *app,
  const char *url,
  InitResult *init_result_out
)
```
Gets an instance of FirebaseDatabase for the specified URL.

If you call [GetInstance()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1a09214ba62dbbdb86d3e48c452a97b6c1) multiple times with the same [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) and URL, you will get the same instance of [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `app` | Your instance of [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app). Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) will use this to communicate with Firebase Authentication. | | `url` | The URL of your Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database). This overrides any url specified in the [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) options. | | `init_result_out` | Optional: If provided, write the init result here. Will be set to kInitResultSuccess if initialization succeeded, or kInitResultFailedMissingDependency on Android if Google Play services is not available on the current device. | |
| **Returns** | An instance of [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) corresponding to the given [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) and URL. |

## Public functions

### GetReference

```c++
DatabaseReference GetReference() const 
```
Get a [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) to the root of the database.

<br />

| Details ||
|---|---|
| **Returns** | A [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) to the root of the database. |

### GetReference

```c++
DatabaseReference GetReference(
  const char *path
) const 
```
Get a [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) for the specified path.

<br />

| Details ||
|---|---|
| **Returns** | A [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) to the specified path in the database. If you specified an invalid path, the reference's DatabaseReference::IsValid() will return false. |

### GetReferenceFromUrl

```c++
DatabaseReference GetReferenceFromUrl(
  const char *url
) const 
```
Get a [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) for the provided URL, which must belong to the database URL this instance is already connected to.

<br />

| Details ||
|---|---|
| **Returns** | A [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference) to the specified path in the database. If you specified an invalid path, the reference's DatabaseReference::IsValid() will return false. |

### GoOffline

```c++
void GoOffline()
```
Shuts down the connection to the Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) backend until [GoOnline()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1a683f584177a99d4288988f6870d57f19) is called.

### GoOnline

```c++
void GoOnline()
```
Resumes the connection to the Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) backend after a previous [GoOffline()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1aa2cf08220af5ce6c8d1d51416fce2fc1) call.

### PurgeOutstandingWrites

```c++
void PurgeOutstandingWrites()
```
Purge all pending writes to the Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) server.

The Firebase Realtime [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) client automatically queues writes and sends them to the server at the earliest opportunity, depending on network connectivity. In some cases (e.g. offline usage) there may be a large number of writes waiting to be sent. Calling this method will purge all outstanding writes so they are abandoned. All writes will be purged, including transactions and onDisconnect() writes. The writes will be rolled back locally, perhaps triggering events for affected event listeners, and the client will not (re-)send them to the Firebase backend.

### app

```c++
App * app() const 
```
Get the [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) that this [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) was created with.

<br />

| Details ||
|---|---|
| **Returns** | The [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) this [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) was created with. |

### log_level

```c++
LogLevel log_level() const 
```
Get the log verbosity of this [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) instance.

<br />

| Details ||
|---|---|
| **Returns** | Get the currently configured logging verbosity. |

### set_log_level

```c++
void set_log_level(
  LogLevel log_level
)
```
Set the log verbosity of this [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) instance.

The log filtering is cumulative with Firebase [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app). That is, this library's log messages will only be displayed if they are not filtered out by this library's log level setting and by Firebase [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app)'s log level setting.


> [!NOTE]
> **Note:** On Android this can only be set before any operations have been performed with the object.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `log_level` | Log level, by default this is set to kLogLevelInfo. | |

### set_persistence_enabled

```c++
void set_persistence_enabled(
  bool enabled
)
```
Sets whether pending write data will persist between application exits.

The Firebase [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) client will cache synchronized data and keep track of all writes you've initiated while your application is running. It seamlessly handles intermittent network connections and re-sends write operations when the network connection is restored. However by default your write operations and cached data are only stored in-memory and will be lost when your app restarts. By setting this value to `true`, the data will be persisted to on-device (disk) storage and will thus be available again when the app is restarted (even when there is no network connectivity at that time).


> [!NOTE]
> **Note:** SetPersistenceEnabled should be called before creating any instances of [DatabaseReference](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database-reference#classfirebase_1_1database_1_1_database_reference), and only needs to be called once per application.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `enabled` | Set this to true to persist write data to on-device (disk) storage, or false to discard pending writes when the app exists. | |

### url

```c++
const char * url() const 
```
Get the URL that this [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) was created with.

<br />

| Details ||
|---|---|
| **Returns** | The URL this [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) was created with, or an empty string if this [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) was created with default parameters. This string will remain valid in memory for the lifetime of this [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database). |

### \~Database

```c++
 ~Database()
```
Destructor for the [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) object.

When deleted, this instance will be removed from the cache of [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) objects. If you call [GetInstance()](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database_1a09214ba62dbbdb86d3e48c452a97b6c1) in the future with the same [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app), a new [Database](https://firebase.google.com/docs/reference/cpp/class/firebase/database/database#classfirebase_1_1database_1_1_database) instance will be created.