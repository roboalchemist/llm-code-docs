# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot.md.txt

# FileDownloadTask.TaskSnapshot

# FileDownloadTask.TaskSnapshot


```
class FileDownloadTask.TaskSnapshot : StorageTask.SnapshotBase
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.storage.StorageTask.SnapshotBase](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase) ||
|   | ↳ | [com.google.firebase.storage.FileDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot) |

*** ** * ** ***

Encapsulates state about the running `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask`

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot#getBytesTransferred()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot#getTotalByteCount()()` |

| ### Extension functions |
|---|---|
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot#(com.google.firebase.storage.FileDownloadTask.TaskSnapshot).component1()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot` to provide bytesTransferred. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot#(com.google.firebase.storage.FileDownloadTask.TaskSnapshot).component2()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot` to provide totalByteCount. |

| ### Inherited functions |
|---|
| From [com.google.firebase.storage.StorageTask.SnapshotBase](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase) |---|---| | `https://developer.android.com/reference/kotlin/java/lang/Exception.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase#getError()()` Returns the last error encountered. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase#getStorage()()` Returns the target of the upload. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask<ResultT!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase#getTask()()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask` for this state. | |

| ### Inherited properties |
|---|
| From [com.google.firebase.storage.StorageTask.SnapshotBase](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase) |---|---| | `https://developer.android.com/reference/kotlin/java/lang/Exception.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase#error()` | |

## Public functions

### getBytesTransferred

```
fun getBytesTransferred(): Long
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the total bytes downloaded so far. |

### getTotalByteCount

```
fun getTotalByteCount(): Long
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the total bytes to upload.. |

## Extension functions

### component1

```
operator fun FileDownloadTask.TaskSnapshot.component1(): Long
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot` to provide bytesTransferred.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the bytesTransferred of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot` |

### component2

```
operator fun FileDownloadTask.TaskSnapshot.component2(): Long
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot` to provide totalByteCount.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the totalByteCount of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot` |