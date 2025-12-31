# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference.md.txt

# StorageReference

# StorageReference


```
class StorageReference : Comparable
```

<br />

*** ** * ** ***

Represents a reference to a Google Cloud Storage object. Developers can upload and download objects, get/set object metadata, and delete an object at a specified path. (see [Google Cloud Storage](https://cloud.google.com/storage/))

## Summary

|                                                                                                                                                    ### Public functions                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference)                                                                                                                                                                                                         | [child](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#child(java.lang.String))`(pathString: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns a new instance of [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference) pointing to a child location of the current reference.                                                                                                                                                                                                                                                      |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                                                                                                                                                                 | [compareTo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#compareTo(com.google.firebase.storage.StorageReference))`(other: `[StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference)`)`                                                                                                                                                                                                                                                                                                                                                                                         |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>`                                                                                                                                            | [delete](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#delete())`()` Deletes the object at this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference).                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                                                                                                                                                                         | [equals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#equals(java.lang.Object))`(other: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)`)`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[FileDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask)`!>` | [getActiveDownloadTasks](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getActiveDownloadTasks())`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)`)`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask)`!>`             | [getActiveUploadTasks](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getActiveUploadTasks())`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                                                                                                                                                                           | [getBucket](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getBucket())`()` Return the Google Cloud Storage bucket that holds this object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)`<`[Byte](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte/index.html)`>!>`                                               | [getBytes](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getBytes(long))`(maxDownloadSizeBytes: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)`)` Asynchronously downloads the object from this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference) A byte array will be allocated large enough to hold the entire file in memory.                                                                                                                                                                                                          |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)`!>`                                                                                                                                            | [getDownloadUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getDownloadUrl())`()` Asynchronously retrieves a long lived download URL with a revokable token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [FileDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask)                                                                                                                                                                                                         | [getFile](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getFile(java.io.File))`(destinationFile: `[File](https://developer.android.com/reference/kotlin/java/io/File.html)`)` Asynchronously downloads the object at this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference) to a specified system filepath.                                                                                                                                                                                                                                                              |
| [FileDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask)                                                                                                                                                                                                         | [getFile](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getFile(android.net.Uri))`(destinationUri: `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)`)` Asynchronously downloads the object at this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference) to a specified system filepath.                                                                                                                                                                                                                                                          |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[StorageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata)`!>`                                                                                                      | [getMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getMetadata())`()` Retrieves metadata associated with an object at this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference).                                                                                                                                                                                                                                                                                                                                                                                   |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                                                                                                                                                                           | [getName](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getName())`()` Returns the short name of this object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference)`?`                                                                                                                                                                                                      | [getParent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getParent())`()` Returns a new instance of [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference) pointing to the parent location or null if this instance references the root location.                                                                                                                                                                                                                                                                                                                            |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                                                                                                                                                                           | [getPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getPath())`()` Returns the full path to this object, not including the Google Cloud Storage bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference)                                                                                                                                                                                                         | [getRoot](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getRoot())`()` Returns a new instance of [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference) pointing to the root location.                                                                                                                                                                                                                                                                                                                                                                                        |
| [FirebaseStorage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage)                                                                                                                                                                                                           | [getStorage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getStorage())`()` Returns the [FirebaseStorage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage) service which created this reference.                                                                                                                                                                                                                                                                                                                                                                                           |
| [StreamDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask)                                                                                                                                                                                                     | [getStream](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getStream())`()` Asynchronously downloads the object at this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference) via a [InputStream](https://developer.android.com/reference/kotlin/java/io/InputStream.html).                                                                                                                                                                                                                                                                                                   |
| [StreamDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask)                                                                                                                                                                                                     | [getStream](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getStream(com.google.firebase.storage.StreamDownloadTask.StreamProcessor))`(processor: `[StreamDownloadTask.StreamProcessor](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.StreamProcessor)`)` Asynchronously downloads the object at this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference) via a [InputStream](https://developer.android.com/reference/kotlin/java/io/InputStream.html).                                                                  |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                                                                                                                                                                 | [hashCode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#hashCode())`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[ListResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult)`!>`                                                                                                                | [list](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#list(int))`(maxResults: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`)` List up to `maxResults` items (files) and prefixes (folders) under this StorageReference.                                                                                                                                                                                                                                                                                                                                                                                     |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[ListResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult)`!>`                                                                                                                | [list](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#list(int,java.lang.String))`(maxResults: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`, pageToken: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Resumes a previous call to [list](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#list(int)), starting after a pagination token.                                                                                                                                                                               |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[ListResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult)`!>`                                                                                                                | [listAll](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#listAll())`()` List all items (files) and prefixes (folders) under this StorageReference.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask)                                                                                                                                                                                                                     | [putBytes](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#putBytes(byte[]))`(bytes: `[ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)`)` Asynchronously uploads byte data to this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference).                                                                                                                                                                                                                                                                                               |
| [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask)                                                                                                                                                                                                                     | [putBytes](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#putBytes(byte[],com.google.firebase.storage.StorageMetadata))`(bytes: `[ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)`, metadata: `[StorageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata)`)` Asynchronously uploads byte data to this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference).                                                                                                                     |
| [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask)                                                                                                                                                                                                                     | [putFile](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#putFile(android.net.Uri))`(uri: `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)`)` Asynchronously uploads from a content URI to this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference).                                                                                                                                                                                                                                                                                              |
| [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask)                                                                                                                                                                                                                     | [putFile](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#putFile(android.net.Uri,com.google.firebase.storage.StorageMetadata))`(uri: `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)`, metadata: `[StorageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata)`)` Asynchronously uploads from a content URI to this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference).                                                                                                                    |
| [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask)                                                                                                                                                                                                                     | [putFile](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#putFile(android.net.Uri,com.google.firebase.storage.StorageMetadata,android.net.Uri))`(uri: `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)`, metadata: `[StorageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata)`?, existingUploadUri: `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)`?)` Asynchronously uploads from a content URI to this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference). |
| [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask)                                                                                                                                                                                                                     | [putStream](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#putStream(java.io.InputStream))`(stream: `[InputStream](https://developer.android.com/reference/kotlin/java/io/InputStream.html)`)` Asynchronously uploads a stream of data to this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference).                                                                                                                                                                                                                                                                         |
| [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask)                                                                                                                                                                                                                     | [putStream](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#putStream(java.io.InputStream,com.google.firebase.storage.StorageMetadata))`(stream: `[InputStream](https://developer.android.com/reference/kotlin/java/io/InputStream.html)`, metadata: `[StorageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata)`)` Asynchronously uploads a stream of data to this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference).                                                                                               |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                                                                                                                                                                                                                        | [toString](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#toString())`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[StorageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata)`!>`                                                                                                      | [updateMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#updateMetadata(com.google.firebase.storage.StorageMetadata))`(metadata: `[StorageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata)`)` Updates the metadata associated with this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference).                                                                                                                                                                                                                 |

## Public functions

### child

```
funÂ child(pathString:Â String):Â StorageReference
```

Returns a new instance of [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference) pointing to a child location of the current reference. All leading and trailing slashes will be removed, and consecutive slashes will be compressed to single slashes. For example:  

```kotlin
child = /foo/bar     path = foo/bar
child = foo/bar/     path = foo/bar
child = foo///bar    path = foo/bar
```  

|                                           Parameters                                           |
|------------------------------------------------------------------------------------------------|----------------------------------------|
| `pathString: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The relative path from this reference. |

|                                                      Returns                                                       |
|--------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference) | the child [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference). |

### compareTo

```
funÂ compareTo(other:Â StorageReference):Â Int
```  

### delete

```
funÂ delete():Â Task<Void!>
```

Deletes the object at this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference).  

|                                                                                     Returns                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | A [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) that indicates whether the operation succeeded or failed. |

### equals

```
funÂ equals(other:Â Any!):Â Boolean
```  

### getActiveDownloadTasks

```
funÂ getActiveDownloadTasks():Â (Mutable)List<FileDownloadTask!>
```  

|                                                                                                                                                          Returns                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)`)`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[FileDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask)`!>` | the set of active download tasks currently in progress or recently completed. |

### getActiveUploadTasks

```
funÂ getActiveUploadTasks():Â (Mutable)List<UploadTask!>
```  

|                                                                                                                                                    Returns                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)`)`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask)`!>` | the set of active upload tasks currently in progress or recently completed. |

### getBucket

```
funÂ getBucket():Â String
```

Return the Google Cloud Storage bucket that holds this object.  

|                                     Returns                                      |
|----------------------------------------------------------------------------------|-------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | the bucket. |

### getBytes

```
funÂ getBytes(maxDownloadSizeBytes:Â Long):Â Task<ByteArray<Byte>!>
```

Asynchronously downloads the object from this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference) A byte array will be allocated large enough to hold the entire file in memory. Therefore, using this method will impact memory usage of your process. If you are downloading many large files, [getStream](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getStream(com.google.firebase.storage.StreamDownloadTask.StreamProcessor)) may be a better option.  

|                                              Parameters                                              |
|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `maxDownloadSizeBytes: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | The maximum allowed size in bytes that will be allocated. Set this parameter to prevent out of memory conditions from occurring. If the download exceeds this limit, the task will fail and an [IndexOutOfBoundsException](https://developer.android.com/reference/kotlin/java/lang/IndexOutOfBoundsException.html) will be returned. |

|                                                                                                                                   Returns                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)`<`[Byte](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte/index.html)`>!>` | The bytes downloaded. |

### getDownloadUrl

```
funÂ getDownloadUrl():Â Task<Uri!>
```

Asynchronously retrieves a long lived download URL with a revokable token. This can be used to share the file with others, but can be revoked by a developer in the Firebase Console if desired.  

|                                                                                     Returns                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)`!>` | The [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html) representing the download URL. You can feed this URL into a [URL](https://developer.android.com/reference/kotlin/java/net/URL.html) and download the object via [openStream](https://developer.android.com/reference/kotlin/java/net/URL.html#openStream--). |

### getFile

```
funÂ getFile(destinationFile:Â File):Â FileDownloadTask
```

Asynchronously downloads the object at this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference) to a specified system filepath.  

|                                         Parameters                                          |
|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| `destinationFile: `[File](https://developer.android.com/reference/kotlin/java/io/File.html) | A [File](https://developer.android.com/reference/kotlin/java/io/File.html) representing the path the object should be downloaded to. |

|                                                      Returns                                                       |
|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FileDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask) | A [FileDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask) that can be used to monitor or manage the download. |

### getFile

```
funÂ getFile(destinationUri:Â Uri):Â FileDownloadTask
```

Asynchronously downloads the object at this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference) to a specified system filepath.  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `destinationUri: `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html) | A file system URI representing the path the object should be downloaded to. |

|                                                      Returns                                                       |
|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FileDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask) | A [FileDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask) that can be used to monitor or manage the download. |

### getMetadata

```
funÂ getMetadata():Â Task<StorageMetadata!>
```

Retrieves metadata associated with an object at this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference).  

|                                                                                                        Returns                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[StorageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata)`!>` | the metadata. |

### getName

```
funÂ getName():Â String
```

Returns the short name of this object.  

|                                     Returns                                      |
|----------------------------------------------------------------------------------|-----------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | the name. |

### getParent

```
funÂ getParent():Â StorageReference?
```

Returns a new instance of [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference) pointing to the parent location or null if this instance references the root location. For example:  

```kotlin
path = foo/bar/baz   parent = foo/bar
path = foo           parent = (root)
path = (root)        parent = (null)
```  

|                                                        Returns                                                        |
|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference)`?` | the parent [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference). |

### getPath

```
funÂ getPath():Â String
```

Returns the full path to this object, not including the Google Cloud Storage bucket.  

|                                     Returns                                      |
|----------------------------------------------------------------------------------|-----------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | the path. |

### getRoot

```
funÂ getRoot():Â StorageReference
```

Returns a new instance of [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference) pointing to the root location.  

|                                                      Returns                                                       |
|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference) | the root [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference). |

### getStorage

```
funÂ getStorage():Â FirebaseStorage
```

Returns the [FirebaseStorage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage) service which created this reference.  

|                                                     Returns                                                      |
|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseStorage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage) | The [FirebaseStorage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage) service. |

### getStream

```
funÂ getStream():Â StreamDownloadTask
```

Asynchronously downloads the object at this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference) via a [InputStream](https://developer.android.com/reference/kotlin/java/io/InputStream.html). The InputStream should be read on an [OnSuccessListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html) registered to run on a background thread via [addOnSuccessListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnSuccessListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnSuccessListener<? super ResultT>))  

|                                                        Returns                                                         |
|------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [StreamDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask) | A [FileDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask) that can be used to monitor or manage the download. |

### getStream

```
funÂ getStream(processor:Â StreamDownloadTask.StreamProcessor):Â StreamDownloadTask
```

Asynchronously downloads the object at this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference) via a [InputStream](https://developer.android.com/reference/kotlin/java/io/InputStream.html).  

|                                                                             Parameters                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `processor: `[StreamDownloadTask.StreamProcessor](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.StreamProcessor) | A [StreamDownloadTask.StreamProcessor](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.StreamProcessor) that is responsible for reading data from the [InputStream](https://developer.android.com/reference/kotlin/java/io/InputStream.html). The [StreamDownloadTask.StreamProcessor](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.StreamProcessor) is called on a background thread and checked exceptions thrown from this object will be returned as a failure to the [OnFailureListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html) registered on the [StreamDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask). |

|                                                        Returns                                                         |
|------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [StreamDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask) | A [FileDownloadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask) that can be used to monitor or manage the download. |

### hashCode

```
funÂ hashCode():Â Int
```  

### list

```
funÂ list(maxResults:Â Int):Â Task<ListResult!>
```

List up to `maxResults` items (files) and prefixes (folders) under this StorageReference.

"/" is treated as a path delimiter. Cloud Storage for Firebase does not support object paths that end with "/" or contain two consecutive "/"s. All invalid objects in Google Cloud Storage will be filtered.

`list()` is only available for projects using [Firebase Rules Version 2](https://firebase.google.com/docs/rules/rules-behavior#security_rules_version_2).  

|                                        Parameters                                        |
|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| `maxResults: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | The maximum number of results to return in a single page. Must be greater than 0 and at most 1000. |

|                                                                                                   Returns                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[ListResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult)`!>` | A a [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) that returns up to maxResults items and prefixes under the current StorageReference. |

### list

```
funÂ list(maxResults:Â Int,Â pageToken:Â String):Â Task<ListResult!>
```

Resumes a previous call to [list](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#list(int)), starting after a pagination token. Returns the next set of items (files) and prefixes (folders) under this StorageReference.

"/" is treated as a path delimiter. Cloud Storage for Firebase does not support object paths that end with "/" or contain two consecutive "/"s. All invalid objects in Google Cloud Storage will be filtered.

`list()` is only available for projects using [Firebase Rules Version 2](https://firebase.google.com/docs/rules/rules-behavior#security_rules_version_2).  

|                                          Parameters                                           |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| `maxResults: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)      | The maximum number of results to return in a single page. Must be greater than 0 and at most 1000. |
| `pageToken: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | A page token from a previous call to list.                                                         |

|                                                                                                   Returns                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[ListResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult)`!>` | A a [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) that returns the next items and prefixes under the current StorageReference. |

### listAll

```
funÂ listAll():Â Task<ListResult!>
```

List all items (files) and prefixes (folders) under this StorageReference.

This is a helper method for calling `list()` repeatedly until there are no more results. Consistency of the result is not guaranteed if objects are inserted or removed while this operation is executing.

`listAll()` is only available for projects using [Firebase Rules Version 2](https://firebase.google.com/docs/rules/rules-behavior#security_rules_version_2).  

|                                                                                                   Returns                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[ListResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult)`!>` | A [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) that returns all items and prefixes under the current StorageReference. |

|                                                                   Throws                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| `java.lang.OutOfMemoryError: `[java.lang.OutOfMemoryError](https://developer.android.com/reference/kotlin/java/lang/OutOfMemoryError.html) | If there are too many items at this location. |

### putBytes

```
funÂ putBytes(bytes:Â ByteArray):Â UploadTask
```

Asynchronously uploads byte data to this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference). This is not recommended for large files. Instead upload a file via [putFile](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#putFile(android.net.Uri)) or an [InputStream](https://developer.android.com/reference/kotlin/java/io/InputStream.html) via [putStream](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#putStream(java.io.InputStream)).  

|                                            Parameters                                            |
|--------------------------------------------------------------------------------------------------|---------------------------|
| `bytes: `[ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html) | The byte array to upload. |

|                                                Returns                                                 |
|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask) | An instance of [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask) which can be used to monitor and manage the upload. |

### putBytes

```
funÂ putBytes(bytes:Â ByteArray,Â metadata:Â StorageMetadata):Â UploadTask
```

Asynchronously uploads byte data to this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference). This is not recommended for large files. Instead upload a file via [putFile](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#putFile(android.net.Uri)) or a Stream via [putStream](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#putStream(java.io.InputStream)).  

|                                                          Parameters                                                          |
|------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `bytes: `[ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)                             | The byte\[\] to upload.                                                                                                                                                                               |
| `metadata: `[StorageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata) | [StorageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata) containing additional information (MIME type, etc.) about the object being uploaded. |

|                                                Returns                                                 |
|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask) | An instance of [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask) which can be used to monitor and manage the upload. |

### putFile

```
funÂ putFile(uri:Â Uri):Â UploadTask
```

Asynchronously uploads from a content URI to this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference).  

|                                    Parameters                                     |
|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| `uri: `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html) | The source of the upload. This can be a file:// scheme or any content URI. A content resolver will be used to load the data. |

|                                                Returns                                                 |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask) | An instance of [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask) which can be used to monitor or manage the upload. |

### putFile

```
funÂ putFile(uri:Â Uri,Â metadata:Â StorageMetadata):Â UploadTask
```

Asynchronously uploads from a content URI to this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference).  

|                                                          Parameters                                                          |
|------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `uri: `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)                                            | The source of the upload. This can be a file:// scheme or any content URI. A content resolver will be used to load the data.                                                                          |
| `metadata: `[StorageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata) | [StorageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata) containing additional information (MIME type, etc.) about the object being uploaded. |

|                                                Returns                                                 |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask) | An instance of [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask) which can be used to monitor or manage the upload. |

### putFile

```
funÂ putFile(uri:Â Uri,Â metadata:Â StorageMetadata?,Â existingUploadUri:Â Uri?):Â UploadTask
```

Asynchronously uploads from a content URI to this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference).  

|                                                           Parameters                                                            |
|---------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `uri: `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)                                               | The source of the upload. This can be a file:// scheme or any content URI. A content resolver will be used to load the data.                                                                                                      |
| `metadata: `[StorageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata)`?` | [StorageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata) containing additional information (MIME type, etc.) about the object being uploaded.                             |
| `existingUploadUri: `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)`?`                              | If set, an attempt is made to resume an existing upload session as defined by [getUploadSessionUri](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot#getUploadSessionUri()). |

|                                                Returns                                                 |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask) | An instance of [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask) which can be used to monitor or manage the upload. |

### putStream

```
funÂ putStream(stream:Â InputStream):Â UploadTask
```

Asynchronously uploads a stream of data to this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference). The stream will remain open at the end of the upload.  

|                                            Parameters                                            |
|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| `stream: `[InputStream](https://developer.android.com/reference/kotlin/java/io/InputStream.html) | The [InputStream](https://developer.android.com/reference/kotlin/java/io/InputStream.html) to upload. |

|                                                Returns                                                 |
|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask) | An instance of [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask) which can be used to monitor and manage the upload. |

### putStream

```
funÂ putStream(stream:Â InputStream,Â metadata:Â StorageMetadata):Â UploadTask
```

Asynchronously uploads a stream of data to this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference). The stream will remain open at the end of the upload.  

|                                                          Parameters                                                          |
|------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `stream: `[InputStream](https://developer.android.com/reference/kotlin/java/io/InputStream.html)                             | The [InputStream](https://developer.android.com/reference/kotlin/java/io/InputStream.html) to upload.                                                                                                 |
| `metadata: `[StorageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata) | [StorageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata) containing additional information (MIME type, etc.) about the object being uploaded. |

|                                                Returns                                                 |
|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask) | An instance of [UploadTask](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask) which can be used to monitor and manage the upload. |

### toString

```
funÂ toString():Â String!
```  

|                                       Returns                                       |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | This object in URI form, which can then be shared and passed into [getReferenceFromUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage#getReferenceFromUrl(java.lang.String)). |

### updateMetadata

```
funÂ updateMetadata(metadata:Â StorageMetadata):Â Task<StorageMetadata!>
```

Updates the metadata associated with this [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference).  

|                                                          Parameters                                                          |
|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| `metadata: `[StorageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata) | A [StorageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata) object with the metadata to update. |

|                                                                                                        Returns                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[StorageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata)`!>` | a [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) that will return the final [StorageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata) once the operation is complete. |