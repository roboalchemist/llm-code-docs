# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot.md.txt

# StreamDownloadTask.TaskSnapshot

# StreamDownloadTask.TaskSnapshot


```
class StreamDownloadTask.TaskSnapshot : StorageTask.SnapshotBase
```

<br />

|---|---|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                                                  |||
| â³ | [com.google.firebase.storage.StorageTask.SnapshotBase](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask.SnapshotBase)                  ||
|   | â³ | [com.google.firebase.storage.StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) |

*** ** * ** ***

Encapsulates state about the running [StreamDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask)

## Summary

|                                  ### Public functions                                  |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)           | [getBytesTransferred](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot#getBytesTransferred())`()` |
| [InputStream](https://developer.android.com/reference/kotlin/java/io/InputStream.html) | [getStream](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot#getStream())`()`                     |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)           | [getTotalByteCount](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot#getTotalByteCount())`()`     |

|                                      ### Extension functions                                      |
|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `operator `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)           | [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot)`.`[component1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot#(com.google.firebase.storage.StreamDownloadTask.TaskSnapshot).component1())`()` Destructuring declaration for [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) to provide bytesTransferred. |
| `operator `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)           | [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot)`.`[component2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot#(com.google.firebase.storage.StreamDownloadTask.TaskSnapshot).component2())`()` Destructuring declaration for [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) to provide totalByteCount.   |
| `operator `[InputStream](https://developer.android.com/reference/kotlin/java/io/InputStream.html) | [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot)`.`[component3](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot#(com.google.firebase.storage.StreamDownloadTask.TaskSnapshot).component3())`()` Destructuring declaration for [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) to provide its stream.       |

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

### getStream

```
funÂ getStream():Â InputStream
```  

|                                        Returns                                         |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [InputStream](https://developer.android.com/reference/kotlin/java/io/InputStream.html) | The stream that represents downloaded bytes from Storage. This stream should be closed either in [doInBackground](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.StreamProcessor#doInBackground(com.google.firebase.storage.StreamDownloadTask.TaskSnapshot,java.io.InputStream)) or in [OnSuccessListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html), [OnFailureListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html) |

### getTotalByteCount

```
funÂ getTotalByteCount():Â Long
```  

|                                   Returns                                    |
|------------------------------------------------------------------------------|----------------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | the total bytes of the download. |

## Extension functions

### component1

```
operatorÂ funÂ StreamDownloadTask.TaskSnapshot.component1():Â Long
```

Destructuring declaration for [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) to provide bytesTransferred.  

|                                   Returns                                    |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | the bytesTransferred of the [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) |

### component2

```
operatorÂ funÂ StreamDownloadTask.TaskSnapshot.component2():Â Long
```

Destructuring declaration for [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) to provide totalByteCount.  

|                                   Returns                                    |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | the totalByteCount of the [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) |

### component3

```
operatorÂ funÂ StreamDownloadTask.TaskSnapshot.component3():Â InputStream
```

Destructuring declaration for [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) to provide its stream.  

|                                        Returns                                         |
|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [InputStream](https://developer.android.com/reference/kotlin/java/io/InputStream.html) | the stream of the [StreamDownloadTask.TaskSnapshot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.TaskSnapshot) |