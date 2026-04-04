# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.ProvideError.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.ProvideError.md.txt

# StorageTask.ProvideError

# StorageTask.ProvideError


```
protected interface StorageTask.ProvideError
```

<br />

Known direct subclasses  
[StorageTask.SnapshotBase](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase)  

|------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| [StorageTask.SnapshotBase](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase) | Base class for state. |

Known indirect subclasses  
[FileDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot), [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot), [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot)  

|--------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FileDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot)     | Encapsulates state about the running [FileDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask)     |
| [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) | Encapsulates state about the running [StreamDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask) |
| [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot)                 | Encapsulates state about the running [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask)                 |

*** ** * ** ***

An object that returns an exception.

## Summary

|                                  ### Public functions                                   |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html)`!` | [getError](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.ProvideError#getError())`()` |

## Public functions

### getError

```
funÂ getError():Â Exception!
```