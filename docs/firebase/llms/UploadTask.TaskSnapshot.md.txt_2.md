# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot.md.txt

# UploadTask.TaskSnapshot

# UploadTask.TaskSnapshot


```
class UploadTask.TaskSnapshot : StorageTask.SnapshotBase
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.storage.StorageTask.SnapshotBase](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase) ||
|   | ↳ | [com.google.firebase.storage.UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot) |

*** ** * ** ***

Encapsulates state about the running `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask`

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot#getBytesTransferred()()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot#getMetadata()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot#getTotalByteCount()()` |
| `https://developer.android.com/reference/kotlin/android/net/Uri.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot#getUploadSessionUri()()` |

| ### Extension functions |
|---|---|
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot#(com.google.firebase.storage.UploadTask.TaskSnapshot).component1()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide bytesTransferred. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot#(com.google.firebase.storage.UploadTask.TaskSnapshot).component2()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide totalByteCount. |
| `operator https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot#(com.google.firebase.storage.UploadTask.TaskSnapshot).component3()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide its metadata. |
| `operator https://developer.android.com/reference/kotlin/android/net/Uri.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot#(com.google.firebase.storage.UploadTask.TaskSnapshot).component4()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide its uploadSessionUri. |

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
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the total bytes uploaded so far. |

### getMetadata

```
fun getMetadata(): StorageMetadata?
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata?` | the metadata for the object. After uploading, this will return the resulting final Metadata which will include the upload URL. |

### getTotalByteCount

```
fun getTotalByteCount(): Long
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The number of bytes to upload. Will return -1 if uploading from a stream. |

### getUploadSessionUri

```
fun getUploadSessionUri(): Uri?
```

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/android/net/Uri.html?` | the session Uri, valid for approximately one week, which can be used to resume an upload later by passing this value into `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#putFile(android.net.Uri,com.google.firebase.storage.StorageMetadata,android.net.Uri)` |

## Extension functions

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
operator fun UploadTask.TaskSnapshot.component2(): Long
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide totalByteCount.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the totalByteCount of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot` |

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