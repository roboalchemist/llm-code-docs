# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask.TaskSnapshot.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot.md.txt

# FileDownloadTask.TaskSnapshot

# FileDownloadTask.TaskSnapshot


```
class FileDownloadTask.TaskSnapshot : StorageTask.SnapshotBase
```

<br />

|---|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                                              |||
| â³ | [com.google.firebase.storage.StorageTask.SnapshotBase](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase)              ||
|   | â³ | [com.google.firebase.storage.FileDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot) |

*** ** * ** ***

Encapsulates state about the running [FileDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask)

## Summary

|                             ### Public functions                             |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | [getBytesTransferred](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot#getBytesTransferred())`()` |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | [getTotalByteCount](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot#getTotalByteCount())`()`     |

|                                 ### Extension functions                                 |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `operator `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | [FileDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot)`.`[component1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot#(com.google.firebase.storage.FileDownloadTask.TaskSnapshot).component1())`()` Destructuring declaration for [FileDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot) to provide bytesTransferred. |
| `operator `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | [FileDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot)`.`[component2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot#(com.google.firebase.storage.FileDownloadTask.TaskSnapshot).component2())`()` Destructuring declaration for [FileDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot) to provide totalByteCount.   |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ### Inherited functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [com.google.firebase.storage.StorageTask.SnapshotBase](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase) |----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | [Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html)`?`                              | [getError](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase#getError())`()` Returns the last error encountered.                                                                                                | | [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference)   | [getStorage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase#getStorage())`()` Returns the target of the upload.                                                                                              | | [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask)`<ResultT!>` | [getTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase#getTask())`()` Returns the [StorageTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask) for this state. | |

|                                                                                                                                                                                                                                                                                            ### Inherited properties                                                                                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [com.google.firebase.storage.StorageTask.SnapshotBase](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase) |-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------| | [Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html)`!` | [error](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase#error()) | |

## Public functions

### getBytesTransferred

```
funÂ getBytesTransferred():Â Long
```  

|                                   Returns                                    |
|------------------------------------------------------------------------------|------------------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | the total bytes downloaded so far. |

### getTotalByteCount

```
funÂ getTotalByteCount():Â Long
```  

|                                   Returns                                    |
|------------------------------------------------------------------------------|-----------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | the total bytes to upload.. |

## Extension functions

### component1

```
operatorÂ funÂ FileDownloadTask.TaskSnapshot.component1():Â Long
```

Destructuring declaration for [FileDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot) to provide bytesTransferred.  

|                                   Returns                                    |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | the bytesTransferred of the [FileDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot) |

### component2

```
operatorÂ funÂ FileDownloadTask.TaskSnapshot.component2():Â Long
```

Destructuring declaration for [FileDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot) to provide totalByteCount.  

|                                   Returns                                    |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | the totalByteCount of the [FileDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask.TaskSnapshot) |