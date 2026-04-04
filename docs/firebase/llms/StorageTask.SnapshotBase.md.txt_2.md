# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase.md.txt

# StorageTask.SnapshotBase

# StorageTask.SnapshotBase


```
class StorageTask.SnapshotBase : StorageTask.ProvideError
```

<br />

Known direct subclasses [FileDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot), [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot), [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot` | Encapsulates state about the running `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` | Encapsulates state about the running `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot` | Encapsulates state about the running `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` |

*** ** * ** ***

Base class for state.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase#SnapshotBase(java.lang.Exception)(error: https://developer.android.com/reference/kotlin/java/lang/Exception.html?)` |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase#getStorage()()` Returns the target of the upload. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase#getTask()()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask` for this state. |

| ### Public properties |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/Exception.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase#error()` |

## Public constructors

### SnapshotBase

```
SnapshotBase(error: Exception?)
```

## Public functions

### getStorage

```
fun getStorage(): StorageReference
```

Returns the target of the upload.

### getTask

```
fun getTask(): StorageTask<ResultT!>
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask` for this state.

## Public properties

### error

```
val error: Exception!
```