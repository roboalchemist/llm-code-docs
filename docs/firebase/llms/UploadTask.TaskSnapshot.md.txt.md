# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot.md.txt

# UploadTask.TaskSnapshot

# UploadTask.TaskSnapshot


```
public class UploadTask.TaskSnapshot extends StorageTask.SnapshotBase
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.storage.StorageTask.SnapshotBase](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.SnapshotBase) ||
|   | ↳ | [com.google.firebase.storage.UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) |

*** ** * ** ***

Encapsulates state about the running `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask`

## Summary

| ### Public methods |
|---|---|
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot#getBytesTransferred()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot#getMetadata()()` |
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot#getTotalByteCount()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/android/net/Uri.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot#getUploadSessionUri()()` |

| ### Extension functions |
|---|---|
| `final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot#(com.google.firebase.storage.UploadTask.TaskSnapshot).component1()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide bytesTransferred. |
| `final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot#(com.google.firebase.storage.UploadTask.TaskSnapshot).component2()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide totalByteCount. |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot#(com.google.firebase.storage.UploadTask.TaskSnapshot).component3()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide its metadata. |
| `final https://developer.android.com/reference/kotlin/android/net/Uri.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot#(com.google.firebase.storage.UploadTask.TaskSnapshot).component4()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide its uploadSessionUri. |

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
| `long` | the total bytes uploaded so far. |

### getMetadata

```
public @Nullable StorageMetadata getMetadata()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata` | the metadata for the object. After uploading, this will return the resulting final Metadata which will include the upload URL. |

### getTotalByteCount

```
public long getTotalByteCount()
```

| Returns |
|---|---|
| `long` | The number of bytes to upload. Will return -1 if uploading from a stream. |

### getUploadSessionUri

```
public @Nullable Uri getUploadSessionUri()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/android/net/Uri.html` | the session Uri, valid for approximately one week, which can be used to resume an upload later by passing this value into `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#putFile(android.net.Uri,com.google.firebase.storage.StorageMetadata,android.net.Uri)` |

## Extension functions

### StorageKt.component1

```
public final long StorageKt.component1(@NonNull UploadTask.TaskSnapshot receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide bytesTransferred.

| Returns |
|---|---|
| `long` | the bytesTransferred of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` |

### StorageKt.component2

```
public final long StorageKt.component2(@NonNull UploadTask.TaskSnapshot receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide totalByteCount.

| Returns |
|---|---|
| `long` | the totalByteCount of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` |

### StorageKt.component3

```
public final StorageMetadata StorageKt.component3(@NonNull UploadTask.TaskSnapshot receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide its metadata.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata` | the metadata of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` |

### StorageKt.component4

```
public final Uri StorageKt.component4(@NonNull UploadTask.TaskSnapshot receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` to provide its uploadSessionUri.

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/android/net/Uri.html` | the uploadSessionUri of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` |