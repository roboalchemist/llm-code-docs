# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference.md.txt

# StorageReference

# StorageReference


```
public class StorageReference implements Comparable
```

<br />

*** ** * ** ***

Represents a reference to a Google Cloud Storage object. Developers can upload and download objects, get/set object metadata, and delete an object at a specified path. (see [Google Cloud Storage](https://cloud.google.com/storage/))

## Summary

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#child(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pathString)` Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` pointing to a child location of the current reference. |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#compareTo(com.google.firebase.storage.StorageReference)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference other)` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#delete()()` Deletes the object at this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#equals(java.lang.Object)(https://developer.android.com/reference/kotlin/java/lang/Object.html other)` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#getActiveDownloadTasks()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#getActiveUploadTasks()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#getBucket()()` Return the Google Cloud Storage bucket that holds this object. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<byte[]>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#getBytes(long)(long maxDownloadSizeBytes)` Asynchronously downloads the object from this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` A byte array will be allocated large enough to hold the entire file in memory. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/android/net/Uri.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#getDownloadUrl()()` Asynchronously retrieves a long lived download URL with a revokable token. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#getFile(java.io.File)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/io/File.html destinationFile)` Asynchronously downloads the object at this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` to a specified system filepath. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#getFile(android.net.Uri)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/net/Uri.html destinationUri)` Asynchronously downloads the object at this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` to a specified system filepath. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#getMetadata()()` Retrieves metadata associated with an object at this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#getName()()` Returns the short name of this object. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#getParent()()` Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` pointing to the parent location or null if this instance references the root location. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#getPath()()` Returns the full path to this object, not including the Google Cloud Storage bucket. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#getRoot()()` Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` pointing to the root location. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#getStorage()()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` service which created this reference. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#getStream()()` Asynchronously downloads the object at this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` via a `https://developer.android.com/reference/kotlin/java/io/InputStream.html`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#getStream(com.google.firebase.storage.StreamDownloadTask.StreamProcessor)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.StreamProcessor processor)` Asynchronously downloads the object at this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` via a `https://developer.android.com/reference/kotlin/java/io/InputStream.html`. |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#hashCode()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#list(int)(int maxResults)` List up to `maxResults` items (files) and prefixes (folders) under this StorageReference. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#list(int,java.lang.String)(int maxResults, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pageToken)` Resumes a previous call to `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#list(int)`, starting after a pagination token. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#listAll()()` List all items (files) and prefixes (folders) under this StorageReference. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#putBytes(byte[])(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] bytes)` Asynchronously uploads byte data to this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#putBytes(byte[],com.google.firebase.storage.StorageMetadata)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] bytes, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata metadata)` Asynchronously uploads byte data to this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#putFile(android.net.Uri)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/net/Uri.html uri)` Asynchronously uploads from a content URI to this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#putFile(android.net.Uri,com.google.firebase.storage.StorageMetadata)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/net/Uri.html uri, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata metadata)` Asynchronously uploads from a content URI to this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#putFile(android.net.Uri,com.google.firebase.storage.StorageMetadata,android.net.Uri)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/net/Uri.html uri, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata metadata, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/android/net/Uri.html existingUploadUri )` Asynchronously uploads from a content URI to this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#putStream(java.io.InputStream)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/io/InputStream.html stream)` Asynchronously uploads a stream of data to this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#putStream(java.io.InputStream,com.google.firebase.storage.StorageMetadata)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/io/InputStream.html stream, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata metadata)` Asynchronously uploads a stream of data to this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`. |
| `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#toString()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#updateMetadata(com.google.firebase.storage.StorageMetadata)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata metadata)` Updates the metadata associated with this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`. |

## Public methods

### child

```
public @NonNull StorageReference child(@NonNull String pathString)
```

Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` pointing to a child location of the current reference. All leading and trailing slashes will be removed, and consecutive slashes will be compressed to single slashes. For example:

```
child = /foo/bar     path = foo/bar
child = foo/bar/     path = foo/bar
child = foo///bar    path = foo/bar
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pathString` | The relative path from this reference. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` | the child `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`. |

### compareTo

```
public int compareTo(@NonNull StorageReference other)
```

### delete

```
public @NonNull Task<Void> delete()
```

Deletes the object at this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html>` | A `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` that indicates whether the operation succeeded or failed. |

### equals

```
public boolean equals(Object other)
```

### getActiveDownloadTasks

```
public @NonNull List<FileDownloadTask> getActiveDownloadTasks()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask>` | the set of active download tasks currently in progress or recently completed. |

### getActiveUploadTasks

```
public @NonNull List<UploadTask> getActiveUploadTasks()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask>` | the set of active upload tasks currently in progress or recently completed. |

### getBucket

```
public @NonNull String getBucket()
```

Return the Google Cloud Storage bucket that holds this object.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | the bucket. |

### getBytes

```
public @NonNull Task<byte[]> getBytes(long maxDownloadSizeBytes)
```

Asynchronously downloads the object from this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` A byte array will be allocated large enough to hold the entire file in memory. Therefore, using this method will impact memory usage of your process. If you are downloading many large files, `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#getStream(com.google.firebase.storage.StreamDownloadTask.StreamProcessor)` may be a better option.

| Parameters |
|---|---|
| `long maxDownloadSizeBytes` | The maximum allowed size in bytes that will be allocated. Set this parameter to prevent out of memory conditions from occurring. If the download exceeds this limit, the task will fail and an `https://developer.android.com/reference/kotlin/java/lang/IndexOutOfBoundsException.html` will be returned. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<byte[]>` | The bytes downloaded. |

### getDownloadUrl

```
public @NonNull Task<Uri> getDownloadUrl()
```

Asynchronously retrieves a long lived download URL with a revokable token. This can be used to share the file with others, but can be revoked by a developer in the Firebase Console if desired.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/android/net/Uri.html>` | The `https://developer.android.com/reference/kotlin/android/net/Uri.html` representing the download URL. You can feed this URL into a `https://developer.android.com/reference/kotlin/java/net/URL.html` and download the object via `https://developer.android.com/reference/kotlin/java/net/URL.html#openStream--`. |

### getFile

```
public @NonNull FileDownloadTask getFile(@NonNull File destinationFile)
```

Asynchronously downloads the object at this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` to a specified system filepath.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/io/File.html destinationFile` | A `https://developer.android.com/reference/kotlin/java/io/File.html` representing the path the object should be downloaded to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask` that can be used to monitor or manage the download. |

### getFile

```
public @NonNull FileDownloadTask getFile(@NonNull Uri destinationUri)
```

Asynchronously downloads the object at this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` to a specified system filepath.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/net/Uri.html destinationUri` | A file system URI representing the path the object should be downloaded to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask` that can be used to monitor or manage the download. |

### getMetadata

```
public @NonNull Task<StorageMetadata> getMetadata()
```

Retrieves metadata associated with an object at this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata>` | the metadata. |

### getName

```
public @NonNull String getName()
```

Returns the short name of this object.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | the name. |

### getParent

```
public @Nullable StorageReference getParent()
```

Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` pointing to the parent location or null if this instance references the root location. For example:

```
path = foo/bar/baz   parent = foo/bar
path = foo           parent = (root)
path = (root)        parent = (null)
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` | the parent `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`. |

### getPath

```
public @NonNull String getPath()
```

Returns the full path to this object, not including the Google Cloud Storage bucket.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | the path. |

### getRoot

```
public @NonNull StorageReference getRoot()
```

Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` pointing to the root location.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` | the root `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`. |

### getStorage

```
public @NonNull FirebaseStorage getStorage()
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` service which created this reference.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` service. |

### getStream

```
public @NonNull StreamDownloadTask getStream()
```

Asynchronously downloads the object at this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` via a `https://developer.android.com/reference/kotlin/java/io/InputStream.html`. The InputStream should be read on an `https://developers.google.com/android/reference/com/google/android/gms/tasks/OnSuccessListener.html` registered to run on a background thread via `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageTask#addOnSuccessListener(java.util.concurrent.Executor,com.google.android.gms.tasks.OnSuccessListener<? super ResultT>)`

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask` that can be used to monitor or manage the download. |

### getStream

```
public @NonNull StreamDownloadTask getStream(@NonNull StreamDownloadTask.StreamProcessor processor)
```

Asynchronously downloads the object at this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` via a `https://developer.android.com/reference/kotlin/java/io/InputStream.html`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.StreamProcessor processor` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.StreamProcessor` that is responsible for reading data from the `https://developer.android.com/reference/kotlin/java/io/InputStream.html`. The `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask.StreamProcessor` is called on a background thread and checked exceptions thrown from this object will be returned as a failure to the `https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html` registered on the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask`. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StreamDownloadTask` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FileDownloadTask` that can be used to monitor or manage the download. |

### hashCode

```
public int hashCode()
```

### list

```
public @NonNull Task<ListResult> list(int maxResults)
```

List up to `maxResults` items (files) and prefixes (folders) under this StorageReference.

"/" is treated as a path delimiter. Cloud Storage for Firebase does not support object paths that end with "/" or contain two consecutive "/"s. All invalid objects in Google Cloud Storage will be filtered.

`list()` is only available for projects using [Firebase Rules Version 2](https://firebase.google.com/docs/rules/rules-behavior#security_rules_version_2).

| Parameters |
|---|---|
| `int maxResults` | The maximum number of results to return in a single page. Must be greater than 0 and at most 1000. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult>` | A a `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` that returns up to maxResults items and prefixes under the current StorageReference. |

### list

```
public @NonNull Task<ListResult> list(int maxResults, @NonNull String pageToken)
```

Resumes a previous call to `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#list(int)`, starting after a pagination token. Returns the next set of items (files) and prefixes (folders) under this StorageReference.

"/" is treated as a path delimiter. Cloud Storage for Firebase does not support object paths that end with "/" or contain two consecutive "/"s. All invalid objects in Google Cloud Storage will be filtered.

`list()` is only available for projects using [Firebase Rules Version 2](https://firebase.google.com/docs/rules/rules-behavior#security_rules_version_2).

| Parameters |
|---|---|
| `int maxResults` | The maximum number of results to return in a single page. Must be greater than 0 and at most 1000. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pageToken` | A page token from a previous call to list. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult>` | A a `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` that returns the next items and prefixes under the current StorageReference. |

### listAll

```
public @NonNull Task<ListResult> listAll()
```

List all items (files) and prefixes (folders) under this StorageReference.

This is a helper method for calling `list()` repeatedly until there are no more results. Consistency of the result is not guaranteed if objects are inserted or removed while this operation is executing.

`listAll()` is only available for projects using [Firebase Rules Version 2](https://firebase.google.com/docs/rules/rules-behavior#security_rules_version_2).

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult>` | A `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` that returns all items and prefixes under the current StorageReference. |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/OutOfMemoryError.html java.lang.OutOfMemoryError` | If there are too many items at this location. |

### putBytes

```
public @NonNull UploadTask putBytes(@NonNull byte[] bytes)
```

Asynchronously uploads byte data to this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`. This is not recommended for large files. Instead upload a file via `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#putFile(android.net.Uri)` or an `https://developer.android.com/reference/kotlin/java/io/InputStream.html` via `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#putStream(java.io.InputStream)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] bytes` | The byte array to upload. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` | An instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` which can be used to monitor and manage the upload. |

### putBytes

```
public @NonNull UploadTask putBytes(@NonNull byte[] bytes, @NonNull StorageMetadata metadata)
```

Asynchronously uploads byte data to this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`. This is not recommended for large files. Instead upload a file via `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#putFile(android.net.Uri)` or a Stream via `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#putStream(java.io.InputStream)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] bytes` | The byte\[\] to upload. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata metadata` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata` containing additional information (MIME type, etc.) about the object being uploaded. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` | An instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` which can be used to monitor and manage the upload. |

### putFile

```
public @NonNull UploadTask putFile(@NonNull Uri uri)
```

Asynchronously uploads from a content URI to this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/net/Uri.html uri` | The source of the upload. This can be a file:// scheme or any content URI. A content resolver will be used to load the data. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` | An instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` which can be used to monitor or manage the upload. |

### putFile

```
public @NonNull UploadTask putFile(@NonNull Uri uri, @NonNull StorageMetadata metadata)
```

Asynchronously uploads from a content URI to this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/net/Uri.html uri` | The source of the upload. This can be a file:// scheme or any content URI. A content resolver will be used to load the data. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata metadata` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata` containing additional information (MIME type, etc.) about the object being uploaded. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` | An instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` which can be used to monitor or manage the upload. |

### putFile

```
public @NonNull UploadTask putFile(
    @NonNull Uri uri,
    @Nullable StorageMetadata metadata,
    @Nullable Uri existingUploadUri
)
```

Asynchronously uploads from a content URI to this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/net/Uri.html uri` | The source of the upload. This can be a file:// scheme or any content URI. A content resolver will be used to load the data. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata metadata` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata` containing additional information (MIME type, etc.) about the object being uploaded. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/android/net/Uri.html existingUploadUri` | If set, an attempt is made to resume an existing upload session as defined by `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask.TaskSnapshot#getUploadSessionUri()`. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` | An instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` which can be used to monitor or manage the upload. |

### putStream

```
public @NonNull UploadTask putStream(@NonNull InputStream stream)
```

Asynchronously uploads a stream of data to this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`. The stream will remain open at the end of the upload.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/io/InputStream.html stream` | The `https://developer.android.com/reference/kotlin/java/io/InputStream.html` to upload. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` | An instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` which can be used to monitor and manage the upload. |

### putStream

```
public @NonNull UploadTask putStream(@NonNull InputStream stream, @NonNull StorageMetadata metadata)
```

Asynchronously uploads a stream of data to this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`. The stream will remain open at the end of the upload.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/io/InputStream.html stream` | The `https://developer.android.com/reference/kotlin/java/io/InputStream.html` to upload. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata metadata` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata` containing additional information (MIME type, etc.) about the object being uploaded. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` | An instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/UploadTask` which can be used to monitor and manage the upload. |

### toString

```
public String toString()
```

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/String.html` | This object in URI form, which can then be shared and passed into `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getReferenceFromUrl(java.lang.String)`. |

### updateMetadata

```
public @NonNull Task<StorageMetadata> updateMetadata(@NonNull StorageMetadata metadata)
```

Updates the metadata associated with this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata metadata` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata` object with the metadata to update. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata>` | a `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` that will return the final `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata` once the operation is complete. |