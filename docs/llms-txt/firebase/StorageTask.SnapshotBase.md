# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.SnapshotBase.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase.md.txt

# StorageTask.SnapshotBase

# StorageTask.SnapshotBase


```
class StorageTask.SnapshotBase : StorageTask.ProvideError
```

<br />

Known direct subclasses  
[FileDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot), [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot), [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot)  

|--------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FileDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot)     | Encapsulates state about the running [FileDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask)     |
| [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) | Encapsulates state about the running [StreamDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask) |
| [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot)                 | Encapsulates state about the running [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask)                 |

*** ** * ** ***

Base class for state.

## Summary

|                                                                                                                  ### Public constructors                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [SnapshotBase](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase#SnapshotBase(java.lang.Exception))`(error: `[Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html)`?)` |

|                                                 ### Public functions                                                 |
|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference)   | [getStorage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase#getStorage())`()` Returns the target of the upload.                                                                                              |
| [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>` | [getTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase#getTask())`()` Returns the [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask) for this state. |

|                                  ### Public properties                                  |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html)`!` | [error](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase#error()) |

## Public constructors

### SnapshotBase

```
SnapshotBase(error:Â Exception?)
```  

## Public functions

### getStorage

```
funÂ getStorage():Â StorageReference
```

Returns the target of the upload.  

### getTask

```
funÂ getTask():Â StorageTask<ResultT!>
```

Returns the [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask) for this state.  

## Public properties

### error

```
valÂ error:Â Exception!
```