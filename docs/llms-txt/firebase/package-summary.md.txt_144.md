# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary.md.txt

# com.google.firebase.storage

# com.google.firebase.storage

## Interfaces

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnPausedListener` | A listener that is called if the Task is paused via `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ControllableTask#pause()`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnProgressListener` | A listener that is called periodically during execution of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ControllableTask`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.ProvideError` | An object that returns an exception. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.StreamProcessor` | A callback that is used to handle the stream download |

## Classes

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/CancellableTask` | Represents an asynchronous operation that can be canceled. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ControllableTask` | Represents an asynchronous operation that can be paused, resumed and canceled. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask` | A task that downloads bytes of a GCS blob to a specified File. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot` | Encapsulates state about the running `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` | FirebaseStorage is a service that supports uploading and downloading large objects to Google Cloud Storage. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult` | Contains the prefixes and items returned by a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#list(int)` call. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata` | Metadata for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder` | Creates a StorageMetadata object. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` | Represents a reference to a Google Cloud Storage object. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask` | A controllable Task that has a synchronized state machine. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase` | Base class for state. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask` | A task that downloads bytes of a GCS blob. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` | Encapsulates state about the running `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState` | Used to emit events about the progress of storage tasks. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState.InProgress` | Called periodically as data is transferred and can be used to populate an upload/download indicator. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState.Paused` | Called any time the upload/download is paused. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` | An controllable task that uploads and fires events for success, progress and failure. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot` | Encapsulates state about the running `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` |

## Exceptions

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException` | Represents an Exception resulting from an operation on a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`. |

## Annotations

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException.ErrorCode` | An `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageException.ErrorCode` indicates the source of a failed StorageTask or operation. |

## Top-level functions summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary#storageMetadata(kotlin.Function1)(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary#storageMetadata(kotlin.Function1)` function. |

## Extension functions summary

|---|---|
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary#(com.google.firebase.storage.FileDownloadTask.TaskSnapshot).component1()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot` to provide bytesTransferred. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary#(com.google.firebase.storage.ListResult).component1()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult` to provide its items. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary#(com.google.firebase.storage.StreamDownloadTask.TaskSnapshot).component1()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` to provide bytesTransferred. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary#(com.google.firebase.storage.UploadTask.TaskSnapshot).component1()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide bytesTransferred. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary#(com.google.firebase.storage.FileDownloadTask.TaskSnapshot).component2()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot` to provide totalByteCount. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary#(com.google.firebase.storage.ListResult).component2()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult` to provide its prefixes. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary#(com.google.firebase.storage.StreamDownloadTask.TaskSnapshot).component2()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` to provide totalByteCount. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary#(com.google.firebase.storage.UploadTask.TaskSnapshot).component2()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide totalByteCount. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary#(com.google.firebase.storage.ListResult).component3()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult` to provide its pageToken. |
| `operator https://developer.android.com/reference/kotlin/java/io/InputStream.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary#(com.google.firebase.storage.StreamDownloadTask.TaskSnapshot).component3()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` to provide its stream. |
| `operator https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary#(com.google.firebase.storage.UploadTask.TaskSnapshot).component3()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide its metadata. |
| `operator https://developer.android.com/reference/kotlin/android/net/Uri.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary#(com.google.firebase.storage.UploadTask.TaskSnapshot).component4()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide its uploadSessionUri. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary#(com.google.firebase.Firebase).storage(com.google.firebase.FirebaseApp,kotlin.String)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp, url: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and storage bucket `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary#(com.google.firebase.Firebase).storage(com.google.firebase.FirebaseApp,kotlin.String)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary#(com.google.firebase.Firebase).storage(com.google.firebase.FirebaseApp)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary#(com.google.firebase.Firebase).storage(kotlin.String)(url: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` instance for a custom storage bucket at `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary#(com.google.firebase.Firebase).storage(kotlin.String)`. |

## Extension properties summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary#(com.google.firebase.Firebase).storage()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/TaskState<T>>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<T>.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary#(com.google.firebase.storage.StorageTask).taskState()` Starts listening to this task's progress and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. |

## Top-level functions

### storageMetadata

```
fun storageMetadata(init: StorageMetadata.Builder.() -> Unit): StorageMetadata
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary#storageMetadata(kotlin.Function1)` function.

## Extension functions

### component1

```
operator fun FileDownloadTask.TaskSnapshot.component1(): Long
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot` to provide bytesTransferred.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the bytesTransferred of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot` |

### component1

```
operator fun ListResult.component1(): List<StorageReference>
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult` to provide its items.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference>` | the items of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult` |

### component1

```
operator fun StreamDownloadTask.TaskSnapshot.component1(): Long
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` to provide bytesTransferred.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the bytesTransferred of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` |

### component1

```
operator fun UploadTask.TaskSnapshot.component1(): Long
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide bytesTransferred.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the bytesTransferred of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot` |

### component2

```
operator fun FileDownloadTask.TaskSnapshot.component2(): Long
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot` to provide totalByteCount.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the totalByteCount of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot` |

### component2

```
operator fun ListResult.component2(): List<StorageReference>
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult` to provide its prefixes.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference>` | the prefixes of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult` |

### component2

```
operator fun StreamDownloadTask.TaskSnapshot.component2(): Long
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` to provide totalByteCount.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the totalByteCount of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` |

### component2

```
operator fun UploadTask.TaskSnapshot.component2(): Long
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide totalByteCount.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the totalByteCount of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot` |

### component3

```
operator fun ListResult.component3(): String?
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult` to provide its pageToken.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | the pageToken of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult` |

### component3

```
operator fun StreamDownloadTask.TaskSnapshot.component3(): InputStream
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` to provide its stream.

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/java/io/InputStream.html` | the stream of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` |

### component3

```
operator fun UploadTask.TaskSnapshot.component3(): StorageMetadata?
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide its metadata.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata?` | the metadata of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot` |

### component4

```
operator fun UploadTask.TaskSnapshot.component4(): Uri?
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide its uploadSessionUri.

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/android/net/Uri.html?` | the uploadSessionUri of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot` |

### storage

```
fun Firebase.storage(app: FirebaseApp, url: String): FirebaseStorage
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and storage bucket `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary#(com.google.firebase.Firebase).storage(com.google.firebase.FirebaseApp,kotlin.String)`.

### storage

```
fun Firebase.storage(app: FirebaseApp): FirebaseStorage
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

### storage

```
fun Firebase.storage(url: String): FirebaseStorage
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` instance for a custom storage bucket at `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/package-summary#(com.google.firebase.Firebase).storage(kotlin.String)`.

## Extension properties

### storage

```
val Firebase.storage: FirebaseStorage
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

### taskState

```
val StorageTask<T>.taskState: Flow<TaskState<T>>
```

Starts listening to this task's progress and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, it attaches the following listeners: `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnProgressListener`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/OnPausedListener`, `https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener.html`.

- When the flow completes the listeners will be removed.