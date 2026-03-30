# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot.md.txt

# StreamDownloadTask.TaskSnapshot

# StreamDownloadTask.TaskSnapshot


```
public class StreamDownloadTask.TaskSnapshot extends StorageTask.SnapshotBase
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.storage.StorageTask.SnapshotBase](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.SnapshotBase) ||
|   | ↳ | [com.google.firebase.storage.StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) |

*** ** * ** ***

Encapsulates state about the running `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask`

## Summary

| ### Public methods |
|---|---|
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot#getBytesTransferred()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/io/InputStream.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot#getStream()()` |
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot#getTotalByteCount()()` |

| ### Extension functions |
|---|---|
| `final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot#(com.google.firebase.storage.StreamDownloadTask.TaskSnapshot).component1()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` to provide bytesTransferred. |
| `final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot#(com.google.firebase.storage.StreamDownloadTask.TaskSnapshot).component2()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` to provide totalByteCount. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/io/InputStream.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot#(com.google.firebase.storage.StreamDownloadTask.TaskSnapshot).component3()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` to provide its stream. |

| ### Inherited fields |
|---|
| From [com.google.firebase.storage.StorageTask.SnapshotBase](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.SnapshotBase) |---|---| | `final https://developer.android.com/reference/kotlin/java/lang/Exception.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.SnapshotBase#error()` | |

| ### Inherited methods |
|---|
| From [com.google.firebase.storage.StorageTask.SnapshotBase](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.SnapshotBase) |---|---| | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Exception.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.SnapshotBase#getError()()` Returns the last error encountered. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.SnapshotBase#getStorage()()` Returns the target of the upload. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.SnapshotBase#getTask()()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask` for this state. | |

## Public methods

### getBytesTransferred

```
public long getBytesTransferred()
```

| Returns |
|---|---|
| `long` | the total bytes downloaded so far. |

### getStream

```
public @NonNull InputStream getStream()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/io/InputStream.html` | The stream that represents downloaded bytes from Storage. This stream should be closed either in `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.StreamProcessor#doInBackground(com.google.firebase.storage.StreamDownloadTask.TaskSnapshot,java.io.InputStream)` or in `https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html`, `https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html` |

### getTotalByteCount

```
public long getTotalByteCount()
```

| Returns |
|---|---|
| `long` | the total bytes of the download. |

## Extension functions

### StorageKt.component1

```
public final long StorageKt.component1(@NonNull StreamDownloadTask.TaskSnapshot receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` to provide bytesTransferred.

| Returns |
|---|---|
| `long` | the bytesTransferred of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` |

### StorageKt.component2

```
public final long StorageKt.component2(@NonNull StreamDownloadTask.TaskSnapshot receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` to provide totalByteCount.

| Returns |
|---|---|
| `long` | the totalByteCount of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` |

### StorageKt.component3

```
public final @NonNull InputStream StorageKt.component3(@NonNull StreamDownloadTask.TaskSnapshot receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` to provide its stream.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/io/InputStream.html` | the stream of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` |