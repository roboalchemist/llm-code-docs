# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot.md.txt

# UploadTask.TaskSnapshot

# UploadTask.TaskSnapshot


```
public class UploadTask.TaskSnapshot extends StorageTask.SnapshotBase
```

<br />

|---|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)                                                                            |||
| â³ | [com.google.firebase.storage.StorageTask.SnapshotBase](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.SnapshotBase)  ||
|   | â³ | [com.google.firebase.storage.UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) |

*** ** * ** ***

Encapsulates state about the running [UploadTask](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask)

## Summary

|                                                                                                 ### Public methods                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `long`                                                                                                                                                                                                              | [getBytesTransferred](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot#getBytesTransferred())`()` |
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[StorageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata) | [getMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot#getMetadata())`()`                 |
| `long`                                                                                                                                                                                                              | [getTotalByteCount](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot#getTotalByteCount())`()`     |
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)                                        | [getUploadSessionUri](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot#getUploadSessionUri())`()` |

|                                                  ### Extension functions                                                  |
|---------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final long`                                                                                                              | [StorageKt](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt)`.`[component1](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot#(com.google.firebase.storage.UploadTask.TaskSnapshot).component1())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot)` receiver)` Destructuring declaration for [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) to provide bytesTransferred.     |
| `final long`                                                                                                              | [StorageKt](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt)`.`[component2](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot#(com.google.firebase.storage.UploadTask.TaskSnapshot).component2())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot)` receiver)` Destructuring declaration for [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) to provide totalByteCount.       |
| `final `[StorageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata) | [StorageKt](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt)`.`[component3](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot#(com.google.firebase.storage.UploadTask.TaskSnapshot).component3())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot)` receiver)` Destructuring declaration for [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) to provide its metadata.         |
| `final `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)                                        | [StorageKt](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt)`.`[component4](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot#(com.google.firebase.storage.UploadTask.TaskSnapshot).component4())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot)` receiver)` Destructuring declaration for [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) to provide its uploadSessionUri. |

|                                                                                                                                                                                                                                                                                                     ### Inherited fields                                                                                                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [com.google.firebase.storage.StorageTask.SnapshotBase](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.SnapshotBase) |----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------| | `final `[Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html) | [error](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.SnapshotBase#error()) | |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ### Inherited methods                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [com.google.firebase.storage.StorageTask.SnapshotBase](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.SnapshotBase) |----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html)                               | [getError](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.SnapshotBase#getError())`()` Returns the last error encountered.                                                                                                 | | `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[StorageReference](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference)  | [getStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.SnapshotBase#getStorage())`()` Returns the target of the upload.                                                                                               | | `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[StorageTask](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask)`<ResultT>` | [getTask](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask.SnapshotBase#getTask())`()` Returns the [StorageTask](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask) for this state. | |

## Public methods

### getBytesTransferred

```
publicÂ longÂ getBytesTransferred()
```  

| Returns |
|---------|----------------------------------|
| `long`  | the total bytes uploaded so far. |

### getMetadata

```
publicÂ @Nullable StorageMetadataÂ getMetadata()
```  

|                                                                                                       Returns                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[StorageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata) | the metadata for the object. After uploading, this will return the resulting final Metadata which will include the upload URL. |

### getTotalByteCount

```
publicÂ longÂ getTotalByteCount()
```  

| Returns |
|---------|---------------------------------------------------------------------------|
| `long`  | The number of bytes to upload. Will return -1 if uploading from a stream. |

### getUploadSessionUri

```
publicÂ @Nullable UriÂ getUploadSessionUri()
```  

|                                                                                   Returns                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html) | the session Uri, valid for approximately one week, which can be used to resume an upload later by passing this value into [putFile](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#putFile(android.net.Uri,com.google.firebase.storage.StorageMetadata,android.net.Uri)) |

## Extension functions

### StorageKt.component1

```
publicÂ finalÂ longÂ StorageKt.component1(@NonNull UploadTask.TaskSnapshotÂ receiver)
```

Destructuring declaration for [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) to provide bytesTransferred.  

| Returns |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `long`  | the bytesTransferred of the [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) |

### StorageKt.component2

```
publicÂ finalÂ longÂ StorageKt.component2(@NonNull UploadTask.TaskSnapshotÂ receiver)
```

Destructuring declaration for [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) to provide totalByteCount.  

| Returns |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `long`  | the totalByteCount of the [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) |

### StorageKt.component3

```
publicÂ finalÂ StorageMetadataÂ StorageKt.component3(@NonNull UploadTask.TaskSnapshotÂ receiver)
```

Destructuring declaration for [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) to provide its metadata.  

|                                                      Returns                                                      |
|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [StorageMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata) | the metadata of the [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) |

### StorageKt.component4

```
publicÂ finalÂ UriÂ StorageKt.component4(@NonNull UploadTask.TaskSnapshotÂ receiver)
```

Destructuring declaration for [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) to provide its uploadSessionUri.  

|                                  Returns                                   |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html) | the uploadSessionUri of the [UploadTask.TaskSnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot) |