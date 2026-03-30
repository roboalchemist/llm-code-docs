# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.SnapshotBase.md.txt

# StorageTask.SnapshotBase

# StorageTask.SnapshotBase


```
public class StorageTask.SnapshotBase implements StorageTask.ProvideError
```

<br />

Known direct subclasses [FileDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask.TaskSnapshot), [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot), [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot)

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask.TaskSnapshot` | Encapsulates state about the running `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask` |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot` | Encapsulates state about the running `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask` |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot` | Encapsulates state about the running `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` |

*** ** * ** ***

Base class for state.

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/Exception.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.SnapshotBase#error()` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.SnapshotBase#SnapshotBase(java.lang.Exception)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Exception.html error)` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Exception.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.SnapshotBase#getError()()` Returns the last error encountered. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.SnapshotBase#getStorage()()` Returns the target of the upload. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask<ResultT>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.SnapshotBase#getTask()()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask` for this state. |

## Public fields

### error

```
public final Exception error
```

## Public constructors

### SnapshotBase

```
public SnapshotBase(@Nullable Exception error)
```

## Public methods

### getError

```
public @Nullable Exception getError()
```

Returns the last error encountered.

### getStorage

```
public @NonNull StorageReference getStorage()
```

Returns the target of the upload.

### getTask

```
public @NonNull StorageTask<ResultT> getTask()
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask` for this state.