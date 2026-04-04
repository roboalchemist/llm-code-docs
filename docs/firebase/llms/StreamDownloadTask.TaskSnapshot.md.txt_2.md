# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot.md.txt

# StreamDownloadTask.TaskSnapshot

# StreamDownloadTask.TaskSnapshot


```
class StreamDownloadTask.TaskSnapshot : StorageTask.SnapshotBase
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.storage.StorageTask.SnapshotBase](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase) ||
|   | ↳ | [com.google.firebase.storage.StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) |

*** ** * ** ***

Encapsulates state about the running `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask`

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot#getBytesTransferred()()` |
| `https://developer.android.com/reference/kotlin/java/io/InputStream.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot#getStream()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot#getTotalByteCount()()` |

| ### Extension functions |
|---|---|
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot#(com.google.firebase.storage.StreamDownloadTask.TaskSnapshot).component1()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` to provide bytesTransferred. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot#(com.google.firebase.storage.StreamDownloadTask.TaskSnapshot).component2()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` to provide totalByteCount. |
| `operator https://developer.android.com/reference/kotlin/java/io/InputStream.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot#(com.google.firebase.storage.StreamDownloadTask.TaskSnapshot).component3()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` to provide its stream. |

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

### getStream

```
fun getStream(): InputStream
```

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/java/io/InputStream.html` | The stream that represents downloaded bytes from Storage. This stream should be closed either in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.StreamProcessor#doInBackground(com.google.firebase.storage.StreamDownloadTask.TaskSnapshot,java.io.InputStream)` or in `https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html`, `https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html` |

### getTotalByteCount

```
fun getTotalByteCount(): Long
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the total bytes of the download. |

## Extension functions

### component1

```
operator fun StreamDownloadTask.TaskSnapshot.component1(): Long
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` to provide bytesTransferred.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the bytesTransferred of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` |

### component2

```
operator fun StreamDownloadTask.TaskSnapshot.component2(): Long
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` to provide totalByteCount.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the totalByteCount of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` |

### component3

```
operator fun StreamDownloadTask.TaskSnapshot.component3(): InputStream
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` to provide its stream.

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/java/io/InputStream.html` | the stream of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` |