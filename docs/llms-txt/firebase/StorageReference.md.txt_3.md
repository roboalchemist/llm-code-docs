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

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#child(java.lang.String)(pathString: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` pointing to a child location of the current reference. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#compareTo(com.google.firebase.storage.StorageReference)(other: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference)` |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#delete()()` Deletes the object at this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#equals(java.lang.Object)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!)` |
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getActiveDownloadTasks()()` |
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getActiveUploadTasks()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getBucket()()` Return the Google Cloud Storage bucket that holds this object. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte/index.html>!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getBytes(long)(maxDownloadSizeBytes: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Asynchronously downloads the object from this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` A byte array will be allocated large enough to hold the entire file in memory. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/android/net/Uri.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getDownloadUrl()()` Asynchronously retrieves a long lived download URL with a revokable token. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getFile(java.io.File)(destinationFile: https://developer.android.com/reference/kotlin/java/io/File.html)` Asynchronously downloads the object at this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` to a specified system filepath. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getFile(android.net.Uri)(destinationUri: https://developer.android.com/reference/kotlin/android/net/Uri.html)` Asynchronously downloads the object at this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` to a specified system filepath. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getMetadata()()` Retrieves metadata associated with an object at this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getName()()` Returns the short name of this object. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getParent()()` Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` pointing to the parent location or null if this instance references the root location. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getPath()()` Returns the full path to this object, not including the Google Cloud Storage bucket. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getRoot()()` Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` pointing to the root location. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getStorage()()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` service which created this reference. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getStream()()` Asynchronously downloads the object at this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` via a `https://developer.android.com/reference/kotlin/java/io/InputStream.html`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getStream(com.google.firebase.storage.StreamDownloadTask.StreamProcessor)(processor: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.StreamProcessor)` Asynchronously downloads the object at this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` via a `https://developer.android.com/reference/kotlin/java/io/InputStream.html`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#hashCode()()` |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#list(int)(maxResults: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` List up to `maxResults` items (files) and prefixes (folders) under this StorageReference. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#list(int,java.lang.String)(maxResults: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, pageToken: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Resumes a previous call to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#list(int)`, starting after a pagination token. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#listAll()()` List all items (files) and prefixes (folders) under this StorageReference. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#putBytes(byte[])(bytes: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)` Asynchronously uploads byte data to this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#putBytes(byte[],com.google.firebase.storage.StorageMetadata)(bytes: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html, metadata: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata)` Asynchronously uploads byte data to this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#putFile(android.net.Uri)(uri: https://developer.android.com/reference/kotlin/android/net/Uri.html)` Asynchronously uploads from a content URI to this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#putFile(android.net.Uri,com.google.firebase.storage.StorageMetadata)(uri: https://developer.android.com/reference/kotlin/android/net/Uri.html, metadata: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata)` Asynchronously uploads from a content URI to this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#putFile(android.net.Uri,com.google.firebase.storage.StorageMetadata,android.net.Uri)(uri: https://developer.android.com/reference/kotlin/android/net/Uri.html, metadata: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata?, existingUploadUri: https://developer.android.com/reference/kotlin/android/net/Uri.html?)` Asynchronously uploads from a content URI to this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#putStream(java.io.InputStream)(stream: https://developer.android.com/reference/kotlin/java/io/InputStream.html)` Asynchronously uploads a stream of data to this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#putStream(java.io.InputStream,com.google.firebase.storage.StorageMetadata)(stream: https://developer.android.com/reference/kotlin/java/io/InputStream.html, metadata: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata)` Asynchronously uploads a stream of data to this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#toString()()` |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#updateMetadata(com.google.firebase.storage.StorageMetadata)(metadata: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata)` Updates the metadata associated with this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`. |

## Public functions

### child

```
fun child(pathString: String): StorageReference
```

Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` pointing to a child location of the current reference. All leading and trailing slashes will be removed, and consecutive slashes will be compressed to single slashes. For example:

```kotlin
child = /foo/bar     path = foo/bar
child = foo/bar/     path = foo/bar
child = foo///bar    path = foo/bar
```

| Parameters |
|---|---|
| `pathString: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The relative path from this reference. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` | the child `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`. |

### compareTo

```
fun compareTo(other: StorageReference): Int
```

### delete

```
fun delete(): Task<Void!>
```

Deletes the object at this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | A `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` that indicates whether the operation succeeded or failed. |

### equals

```
fun equals(other: Any!): Boolean
```

### getActiveDownloadTasks

```
fun getActiveDownloadTasks(): (Mutable)List<FileDownloadTask!>
```

| Returns |
|---|---|
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask!>` | the set of active download tasks currently in progress or recently completed. |

### getActiveUploadTasks

```
fun getActiveUploadTasks(): (Mutable)List<UploadTask!>
```

| Returns |
|---|---|
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask!>` | the set of active upload tasks currently in progress or recently completed. |

### getBucket

```
fun getBucket(): String
```

Return the Google Cloud Storage bucket that holds this object.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the bucket. |

### getBytes

```
fun getBytes(maxDownloadSizeBytes: Long): Task<ByteArray<Byte>!>
```

Asynchronously downloads the object from this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` A byte array will be allocated large enough to hold the entire file in memory. Therefore, using this method will impact memory usage of your process. If you are downloading many large files, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getStream(com.google.firebase.storage.StreamDownloadTask.StreamProcessor)` may be a better option.

| Parameters |
|---|---|
| `maxDownloadSizeBytes: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The maximum allowed size in bytes that will be allocated. Set this parameter to prevent out of memory conditions from occurring. If the download exceeds this limit, the task will fail and an `https://developer.android.com/reference/kotlin/java/lang/IndexOutOfBoundsException.html` will be returned. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte/index.html>!>` | The bytes downloaded. |

### getDownloadUrl

```
fun getDownloadUrl(): Task<Uri!>
```

Asynchronously retrieves a long lived download URL with a revokable token. This can be used to share the file with others, but can be revoked by a developer in the Firebase Console if desired.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/android/net/Uri.html!>` | The `https://developer.android.com/reference/kotlin/android/net/Uri.html` representing the download URL. You can feed this URL into a `https://developer.android.com/reference/kotlin/java/net/URL.html` and download the object via `https://developer.android.com/reference/kotlin/java/net/URL.html#openStream--`. |

### getFile

```
fun getFile(destinationFile: File): FileDownloadTask
```

Asynchronously downloads the object at this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` to a specified system filepath.

| Parameters |
|---|---|
| `destinationFile: https://developer.android.com/reference/kotlin/java/io/File.html` | A `https://developer.android.com/reference/kotlin/java/io/File.html` representing the path the object should be downloaded to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask` that can be used to monitor or manage the download. |

### getFile

```
fun getFile(destinationUri: Uri): FileDownloadTask
```

Asynchronously downloads the object at this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` to a specified system filepath.

| Parameters |
|---|---|
| `destinationUri: https://developer.android.com/reference/kotlin/android/net/Uri.html` | A file system URI representing the path the object should be downloaded to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask` that can be used to monitor or manage the download. |

### getMetadata

```
fun getMetadata(): Task<StorageMetadata!>
```

Retrieves metadata associated with an object at this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata!>` | the metadata. |

### getName

```
fun getName(): String
```

Returns the short name of this object.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the name. |

### getParent

```
fun getParent(): StorageReference?
```

Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` pointing to the parent location or null if this instance references the root location. For example:

```kotlin
path = foo/bar/baz   parent = foo/bar
path = foo           parent = (root)
path = (root)        parent = (null)
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference?` | the parent `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`. |

### getPath

```
fun getPath(): String
```

Returns the full path to this object, not including the Google Cloud Storage bucket.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the path. |

### getRoot

```
fun getRoot(): StorageReference
```

Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` pointing to the root location.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` | the root `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`. |

### getStorage

```
fun getStorage(): FirebaseStorage
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` service which created this reference.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` service. |

### getStream

```
fun getStream(): StreamDownloadTask
```

Asynchronously downloads the object at this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` via a `https://developer.android.com/reference/kotlin/java/io/InputStream.html`. The InputStream should be read on an `https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html` registered to run on a background thread via `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageTask#addOnSuccessListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnSuccessListener<? super ResultT>)`

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask` that can be used to monitor or manage the download. |

### getStream

```
fun getStream(processor: StreamDownloadTask.StreamProcessor): StreamDownloadTask
```

Asynchronously downloads the object at this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` via a `https://developer.android.com/reference/kotlin/java/io/InputStream.html`.

| Parameters |
|---|---|
| `processor: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.StreamProcessor` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.StreamProcessor` that is responsible for reading data from the `https://developer.android.com/reference/kotlin/java/io/InputStream.html`. The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask.StreamProcessor` is called on a background thread and checked exceptions thrown from this object will be returned as a failure to the `https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html` registered on the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask`. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StreamDownloadTask` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FileDownloadTask` that can be used to monitor or manage the download. |

### hashCode

```
fun hashCode(): Int
```

### list

```
fun list(maxResults: Int): Task<ListResult!>
```

List up to `maxResults` items (files) and prefixes (folders) under this StorageReference.

"/" is treated as a path delimiter. Cloud Storage for Firebase does not support object paths that end with "/" or contain two consecutive "/"s. All invalid objects in Google Cloud Storage will be filtered.

`list()` is only available for projects using [Firebase Rules Version 2](https://firebase.google.com/docs/rules/rules-behavior#security_rules_version_2).

| Parameters |
|---|---|
| `maxResults: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The maximum number of results to return in a single page. Must be greater than 0 and at most 1000. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult!>` | A a `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` that returns up to maxResults items and prefixes under the current StorageReference. |

### list

```
fun list(maxResults: Int, pageToken: String): Task<ListResult!>
```

Resumes a previous call to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#list(int)`, starting after a pagination token. Returns the next set of items (files) and prefixes (folders) under this StorageReference.

"/" is treated as a path delimiter. Cloud Storage for Firebase does not support object paths that end with "/" or contain two consecutive "/"s. All invalid objects in Google Cloud Storage will be filtered.

`list()` is only available for projects using [Firebase Rules Version 2](https://firebase.google.com/docs/rules/rules-behavior#security_rules_version_2).

| Parameters |
|---|---|
| `maxResults: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The maximum number of results to return in a single page. Must be greater than 0 and at most 1000. |
| `pageToken: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A page token from a previous call to list. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult!>` | A a `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` that returns the next items and prefixes under the current StorageReference. |

### listAll

```
fun listAll(): Task<ListResult!>
```

List all items (files) and prefixes (folders) under this StorageReference.

This is a helper method for calling `list()` repeatedly until there are no more results. Consistency of the result is not guaranteed if objects are inserted or removed while this operation is executing.

`listAll()` is only available for projects using [Firebase Rules Version 2](https://firebase.google.com/docs/rules/rules-behavior#security_rules_version_2).

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult!>` | A `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` that returns all items and prefixes under the current StorageReference. |

| Throws |
|---|---|
| `java.lang.OutOfMemoryError: https://developer.android.com/reference/kotlin/java/lang/OutOfMemoryError.html` | If there are too many items at this location. |

### putBytes

```
fun putBytes(bytes: ByteArray): UploadTask
```

Asynchronously uploads byte data to this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`. This is not recommended for large files. Instead upload a file via `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#putFile(android.net.Uri)` or an `https://developer.android.com/reference/kotlin/java/io/InputStream.html` via `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#putStream(java.io.InputStream)`.

| Parameters |
|---|---|
| `bytes: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | The byte array to upload. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` | An instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` which can be used to monitor and manage the upload. |

### putBytes

```
fun putBytes(bytes: ByteArray, metadata: StorageMetadata): UploadTask
```

Asynchronously uploads byte data to this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`. This is not recommended for large files. Instead upload a file via `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#putFile(android.net.Uri)` or a Stream via `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#putStream(java.io.InputStream)`.

| Parameters |
|---|---|
| `bytes: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | The byte\[\] to upload. |
| `metadata: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata` containing additional information (MIME type, etc.) about the object being uploaded. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` | An instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` which can be used to monitor and manage the upload. |

### putFile

```
fun putFile(uri: Uri): UploadTask
```

Asynchronously uploads from a content URI to this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`.

| Parameters |
|---|---|
| `uri: https://developer.android.com/reference/kotlin/android/net/Uri.html` | The source of the upload. This can be a file:// scheme or any content URI. A content resolver will be used to load the data. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` | An instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` which can be used to monitor or manage the upload. |

### putFile

```
fun putFile(uri: Uri, metadata: StorageMetadata): UploadTask
```

Asynchronously uploads from a content URI to this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`.

| Parameters |
|---|---|
| `uri: https://developer.android.com/reference/kotlin/android/net/Uri.html` | The source of the upload. This can be a file:// scheme or any content URI. A content resolver will be used to load the data. |
| `metadata: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata` containing additional information (MIME type, etc.) about the object being uploaded. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` | An instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` which can be used to monitor or manage the upload. |

### putFile

```
fun putFile(uri: Uri, metadata: StorageMetadata?, existingUploadUri: Uri?): UploadTask
```

Asynchronously uploads from a content URI to this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`.

| Parameters |
|---|---|
| `uri: https://developer.android.com/reference/kotlin/android/net/Uri.html` | The source of the upload. This can be a file:// scheme or any content URI. A content resolver will be used to load the data. |
| `metadata: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata` containing additional information (MIME type, etc.) about the object being uploaded. |
| `existingUploadUri: https://developer.android.com/reference/kotlin/android/net/Uri.html?` | If set, an attempt is made to resume an existing upload session as defined by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask.TaskSnapshot#getUploadSessionUri()`. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` | An instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` which can be used to monitor or manage the upload. |

### putStream

```
fun putStream(stream: InputStream): UploadTask
```

Asynchronously uploads a stream of data to this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`. The stream will remain open at the end of the upload.

| Parameters |
|---|---|
| `stream: https://developer.android.com/reference/kotlin/java/io/InputStream.html` | The `https://developer.android.com/reference/kotlin/java/io/InputStream.html` to upload. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` | An instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` which can be used to monitor and manage the upload. |

### putStream

```
fun putStream(stream: InputStream, metadata: StorageMetadata): UploadTask
```

Asynchronously uploads a stream of data to this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`. The stream will remain open at the end of the upload.

| Parameters |
|---|---|
| `stream: https://developer.android.com/reference/kotlin/java/io/InputStream.html` | The `https://developer.android.com/reference/kotlin/java/io/InputStream.html` to upload. |
| `metadata: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata` containing additional information (MIME type, etc.) about the object being uploaded. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` | An instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/UploadTask` which can be used to monitor and manage the upload. |

### toString

```
fun toString(): String!
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | This object in URI form, which can then be shared and passed into `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage#getReferenceFromUrl(java.lang.String)`. |

### updateMetadata

```
fun updateMetadata(metadata: StorageMetadata): Task<StorageMetadata!>
```

Updates the metadata associated with this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`.

| Parameters |
|---|---|
| `metadata: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata` object with the metadata to update. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata!>` | a `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` that will return the final `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata` once the operation is complete. |