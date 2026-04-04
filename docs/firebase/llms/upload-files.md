# Source: https://firebase.google.com/docs/storage/web/upload-files.md.txt

# Source: https://firebase.google.com/docs/storage/ios/upload-files.md.txt

# Source: https://firebase.google.com/docs/storage/unity/upload-files.md.txt

# Source: https://firebase.google.com/docs/storage/flutter/upload-files.md.txt

# Source: https://firebase.google.com/docs/storage/cpp/upload-files.md.txt

# Source: https://firebase.google.com/docs/storage/android/upload-files.md.txt

# Source: https://firebase.google.com/docs/storage/unity/upload-files.md.txt

# Source: https://firebase.google.com/docs/storage/flutter/upload-files.md.txt

# Source: https://firebase.google.com/docs/storage/cpp/upload-files.md.txt

# Source: https://firebase.google.com/docs/storage/android/upload-files.md.txt

<br />

Cloud Storage for Firebaseallows you to quickly and easily upload files to a[Cloud Storage](https://cloud.google.com/storage)bucket provided and managed by Firebase.
| **Note:** By default, aCloud Storage for Firebasebucket requiresFirebase Authenticationto perform any action on the bucket's data or files. You can change yourFirebase Security RulesforCloud Storageto[allow unauthenticated access for specific situations](https://firebase.google.com/docs/storage/security/rules-conditions#public). However, for most situations, we strongly recommend[restricting access and setting up robust security rules](https://firebase.google.com/docs/storage/security/get-started)(especially for production apps). Note that if you useGoogleApp Engineand have a defaultCloud Storagebucket with a name format of`*.appspot.com`, you may need to consider[how your security rules impact access toApp Enginefiles](https://firebase.google.com/docs/storage/gcp-integration#security-rules-and-app-engine-files).
| **Note:** For Spark plan projects, Firebase blocks upload and hosting of certain executable file types for Windows (files with`.exe`,`.dll`and`.bat`extensions), Android (`.apk`extension) and Apple (`.ipa`extension) byCloud Storage for FirebaseandFirebase Hosting. This policy exists to prevent abuse on our platform. Projects on the Blaze plan are not affected. For more information, see[this FAQ](https://firebase.google.com/support/faq#storage-exe-restrictions).

## Upload Files

To upload a file toCloud Storage, you first create a reference to the full path of the file, including the file name.  

### Kotlin

```kotlin
// Create a storage reference from our app
val storageRef = storage.reference

// Create a reference to "mountains.jpg"
val mountainsRef = storageRef.child("mountains.jpg")

// Create a reference to 'images/mountains.jpg'
val mountainImagesRef = storageRef.child("images/mountains.jpg")

// While the file names are the same, the references point to different files
mountainsRef.name == mountainImagesRef.name // true
mountainsRef.path == mountainImagesRef.path // false  
https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/storage/app/src/main/java/com/google/firebase/referencecode/storage/kotlin/StorageActivity.kt#L129-L140
```

### Java

```java
// Create a storage reference from our app
StorageReference storageRef = storage.getReference();

// Create a reference to "mountains.jpg"
StorageReference mountainsRef = storageRef.child("mountains.jpg");

// Create a reference to 'images/mountains.jpg'
StorageReference mountainImagesRef = storageRef.child("images/mountains.jpg");

// While the file names are the same, the references point to different files
mountainsRef.getName().equals(mountainImagesRef.getName());    // true
mountainsRef.getPath().equals(mountainImagesRef.getPath());    // false  
https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/storage/app/src/main/java/com/google/firebase/referencecode/storage/StorageActivity.java#L158-L169
```

Once you've created an appropriate reference, you then call the`putBytes()`,`putFile()`, or`putStream()`method to upload the file toCloud Storage.

You cannot upload data with a reference to the root of yourCloud Storagebucket. Your reference must point to a child URL.

### Upload from data in memory

The`putBytes()`method is the simplest way to upload a file toCloud Storage.`putBytes()`takes a`byte[]`and returns an`UploadTask`that you can use to manage and monitor the status of the upload.  

### Kotlin

```kotlin
// Get the data from an ImageView as bytes
imageView.isDrawingCacheEnabled = true
imageView.buildDrawingCache()
val bitmap = (imageView.drawable as BitmapDrawable).bitmap
val baos = ByteArrayOutputStream()
bitmap.compress(Bitmap.CompressFormat.JPEG, 100, baos)
val data = baos.toByteArray()

var uploadTask = mountainsRef.putBytes(data)
uploadTask.addOnFailureListener {
    // Handle unsuccessful uploads
}.addOnSuccessListener { taskSnapshot ->
    // taskSnapshot.metadata contains file metadata such as size, content-type, etc.
    // ...
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/storage/app/src/main/java/com/google/firebase/referencecode/storage/kotlin/StorageActivity.kt#L145-L159
```

### Java

```java
// Get the data from an ImageView as bytes
imageView.setDrawingCacheEnabled(true);
imageView.buildDrawingCache();
Bitmap bitmap = ((BitmapDrawable) imageView.getDrawable()).getBitmap();
ByteArrayOutputStream baos = new ByteArrayOutputStream();
bitmap.compress(Bitmap.CompressFormat.JPEG, 100, baos);
byte[] data = baos.toByteArray();

UploadTask uploadTask = mountainsRef.putBytes(data);
uploadTask.addOnFailureListener(new OnFailureListener() {
    @Override
    public void onFailure(@NonNull Exception exception) {
        // Handle unsuccessful uploads
    }
}).addOnSuccessListener(new OnSuccessListener<UploadTask.TaskSnapshot>() {
    @Override
    public void onSuccess(UploadTask.TaskSnapshot taskSnapshot) {
        // taskSnapshot.getMetadata() contains file metadata such as size, content-type, etc.
        // ...
    }
});https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/storage/app/src/main/java/com/google/firebase/referencecode/storage/StorageActivity.java#L176-L196
```

Because`putBytes()`accepts a`byte[]`, it requires your app to hold the entire contents of a file in memory at once. Consider using`putStream()`or`putFile()`to use less memory.

### Upload from a stream

The`putStream()`method is the most versatile way to upload a file toCloud Storage.`putStream()`takes an`InputStream`and returns an`UploadTask`that you can use to manage and monitor the status of the upload.  

### Kotlin

```kotlin
val stream = FileInputStream(File("path/to/images/rivers.jpg"))

uploadTask = mountainsRef.putStream(stream)
uploadTask.addOnFailureListener {
    // Handle unsuccessful uploads
}.addOnSuccessListener { taskSnapshot ->
    // taskSnapshot.metadata contains file metadata such as size, content-type, etc.
    // ...
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/storage/app/src/main/java/com/google/firebase/referencecode/storage/kotlin/StorageActivity.kt#L163-L171
```

### Java

```java
InputStream stream = new FileInputStream(new File("path/to/images/rivers.jpg"));

uploadTask = mountainsRef.putStream(stream);
uploadTask.addOnFailureListener(new OnFailureListener() {
    @Override
    public void onFailure(@NonNull Exception exception) {
        // Handle unsuccessful uploads
    }
}).addOnSuccessListener(new OnSuccessListener<UploadTask.TaskSnapshot>() {
    @Override
    public void onSuccess(UploadTask.TaskSnapshot taskSnapshot) {
        // taskSnapshot.getMetadata() contains file metadata such as size, content-type, etc.
        // ...
    }
});https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/storage/app/src/main/java/com/google/firebase/referencecode/storage/StorageActivity.java#L200-L214
```

### Upload from a local file

You can upload local files on the device, such as photos and videos from the camera, with the`putFile()`method.`putFile()`takes a`File`and returns an`UploadTask`which you can use to manage and monitor the status of the upload.  

### Kotlin

```kotlin
var file = Uri.fromFile(File("path/to/images/rivers.jpg"))
val riversRef = storageRef.child("images/${file.lastPathSegment}")
uploadTask = riversRef.putFile(file)

// Register observers to listen for when the download is done or if it fails
uploadTask.addOnFailureListener {
    // Handle unsuccessful uploads
}.addOnSuccessListener { taskSnapshot ->
    // taskSnapshot.metadata contains file metadata such as size, content-type, etc.
    // ...
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/storage/app/src/main/java/com/google/firebase/referencecode/storage/kotlin/StorageActivity.kt#L175-L185
```

### Java

```java
Uri file = Uri.fromFile(new File("path/to/images/rivers.jpg"));
StorageReference riversRef = storageRef.child("images/"+file.getLastPathSegment());
uploadTask = riversRef.putFile(file);

// Register observers to listen for when the download is done or if it fails
uploadTask.addOnFailureListener(new OnFailureListener() {
    @Override
    public void onFailure(@NonNull Exception exception) {
        // Handle unsuccessful uploads
    }
}).addOnSuccessListener(new OnSuccessListener<UploadTask.TaskSnapshot>() {
    @Override
    public void onSuccess(UploadTask.TaskSnapshot taskSnapshot) {
        // taskSnapshot.getMetadata() contains file metadata such as size, content-type, etc.
        // ...
    }
});https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/storage/app/src/main/java/com/google/firebase/referencecode/storage/StorageActivity.java#L218-L234
```

## Get a download URL

After uploading a file, you can get a URL to download the file by calling the`getDownloadUrl()`method on the`StorageReference`:  

### Kotlin

```kotlin
val ref = storageRef.child("images/mountains.jpg")
uploadTask = ref.putFile(file)

val urlTask = uploadTask.continueWithTask { task ->
    if (!task.isSuccessful) {
        task.exception?.let {
            throw it
        }
    }
    ref.downloadUrl
}.addOnCompleteListener { task ->
    if (task.isSuccessful) {
        val downloadUri = task.result
    } else {
        // Handle failures
        // ...
    }
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/storage/app/src/main/java/com/google/firebase/referencecode/storage/kotlin/StorageActivity.kt#L252-L269
```

### Java

```java
final StorageReference ref = storageRef.child("images/mountains.jpg");
uploadTask = ref.putFile(file);

Task<Uri> urlTask = uploadTask.continueWithTask(new Continuation<UploadTask.TaskSnapshot, Task<Uri>>() {
    @Override
    public Task<Uri> then(@NonNull Task<UploadTask.TaskSnapshot> task) throws Exception {
        if (!task.isSuccessful()) {
            throw task.getException();
        }

        // Continue with the task to get the download URL
        return ref.getDownloadUrl();
    }
}).addOnCompleteListener(new OnCompleteListener<Uri>() {
    @Override
    public void onComplete(@NonNull Task<Uri> task) {
        if (task.isSuccessful()) {
            Uri downloadUri = task.getResult();
        } else {
            // Handle failures
            // ...
        }
    }
});https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/storage/app/src/main/java/com/google/firebase/referencecode/storage/StorageActivity.java#L315-L338
```

## Add File Metadata

You can also include metadata when you upload files. This metadata contains typical file metadata properties such as`name`,`size`, and`contentType`(commonly referred to as MIME type). The`putFile()`method automatically infers the MIME type from the`File`extension, but you can override the auto-detected type by specifying`contentType`in the metadata. If you do not provide a`contentType`andCloud Storagecannot infer a default from the file extension,Cloud Storageuses`application/octet-stream`. See the[Use File Metadata](https://firebase.google.com/docs/storage/android/file-metadata)section for more information about file metadata.  

### Kotlin

```kotlin
// Create file metadata including the content type
var metadata = storageMetadata {
    contentType = "image/jpg"
}

// Upload the file and metadata
uploadTask = storageRef.child("images/mountains.jpg").putFile(file, metadata)https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/storage/app/src/main/java/com/google/firebase/referencecode/storage/kotlin/StorageActivity.kt#L189-L195
```

### Java

```java
// Create file metadata including the content type
StorageMetadata metadata = new StorageMetadata.Builder()
        .setContentType("image/jpg")
        .build();

// Upload the file and metadata
uploadTask = storageRef.child("images/mountains.jpg").putFile(file, metadata);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/storage/app/src/main/java/com/google/firebase/referencecode/storage/StorageActivity.java#L238-L244
```

## Manage Uploads

In addition to starting uploads, you can pause, resume, and cancel uploads using the`pause()`,`resume()`, and`cancel()`methods. Pause and resume events raise`pause`and`progress`state changes respectively. Canceling an upload causes the upload to fail with an error indicating that the upload was canceled.  

### Kotlin

```kotlin
uploadTask = storageRef.child("images/mountains.jpg").putFile(file)

// Pause the upload
uploadTask.pause()

// Resume the upload
uploadTask.resume()

// Cancel the upload
uploadTask.cancel()https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/storage/app/src/main/java/com/google/firebase/referencecode/storage/kotlin/StorageActivity.kt#L199-L208
```

### Java

```java
uploadTask = storageRef.child("images/mountains.jpg").putFile(file);

// Pause the upload
uploadTask.pause();

// Resume the upload
uploadTask.resume();

// Cancel the upload
uploadTask.cancel();https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/storage/app/src/main/java/com/google/firebase/referencecode/storage/StorageActivity.java#L248-L257
```

## Monitor Upload Progress

You can add listeners to handle success, failure, progress, or pauses in your upload task:

|    Listener Type     |                                                                    Typical Usage                                                                    |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `OnProgressListener` | This listener is called periodically as data is transferred and can be used to populate an upload/download indicator.                               |
| `OnPausedListener`   | This listener is called any time the task is paused.                                                                                                |
| `OnSuccessListener`  | This listener is called when the task has successfully completed.                                                                                   |
| `OnFailureListener`  | This listener is called any time the upload has failed. This can happen due to network timeouts, authorization failures, or if you cancel the task. |

`OnFailureListener`is called with an`Exception`instance. Other listeners are called with an`UploadTask.TaskSnapshot`object. This object is an immutable view of the task at the time the event occurred. An`UploadTask.TaskSnapshot`contains the following properties:

|       Property        |        Type        |                                                                                Description                                                                                 |
|-----------------------|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `getDownloadUrl`      | `String`           | A URL that can be used to download the object. This is a public unguessable URL that can be shared with other clients. This value is populated once an upload is complete. |
| `getError`            | `Exception`        | If the task failed, this will have the cause as an Exception.                                                                                                              |
| `getBytesTransferred` | `long`             | The total number of bytes that have been transferred when this snapshot was taken.                                                                                         |
| `getTotalByteCount`   | `long`             | The total number of bytes expected to be uploaded.                                                                                                                         |
| `getUploadSessionUri` | `String`           | A URI that can be used to continue this task via another call to putFile.                                                                                                  |
| `getMetadata`         | `StorageMetadata`  | Before an upload completes, this is the metadata being sent to the server. After the upload completes, this is the metadata returned by the server.                        |
| `getTask`             | `UploadTask`       | The task that created this snapshot. Use this task to cancel, pause, or resume the upload.                                                                                 |
| `getStorage`          | `StorageReference` | The`StorageReference`used to create the`UploadTask`.                                                                                                                       |

The`UploadTask`event listeners provide a simple and powerful way to monitor upload events.  

### Kotlin

```kotlin
// Observe state change events such as progress, pause, and resume
// You'll need to import com.google.firebase.storage.component1 and
// com.google.firebase.storage.component2
uploadTask.addOnProgressListener { (bytesTransferred, totalByteCount) ->
    val progress = (100.0 * bytesTransferred) / totalByteCount
    Log.d(TAG, "Upload is $progress% done")
}.addOnPausedListener {
    Log.d(TAG, "Upload is paused")
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/storage/app/src/main/java/com/google/firebase/referencecode/storage/kotlin/StorageActivity.kt#L212-L220
```

### Java

```java
// Observe state change events such as progress, pause, and resume
uploadTask.addOnProgressListener(new OnProgressListener<UploadTask.TaskSnapshot>() {
    @Override
    public void onProgress(UploadTask.TaskSnapshot taskSnapshot) {
        double progress = (100.0 * taskSnapshot.getBytesTransferred()) / taskSnapshot.getTotalByteCount();
        Log.d(TAG, "Upload is " + progress + "% done");
    }
}).addOnPausedListener(new OnPausedListener<UploadTask.TaskSnapshot>() {
    @Override
    public void onPaused(UploadTask.TaskSnapshot taskSnapshot) {
        Log.d(TAG, "Upload is paused");
    }
});https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/storage/app/src/main/java/com/google/firebase/referencecode/storage/StorageActivity.java#L261-L273
```

## Handle Activity Lifecycle Changes

Uploads continue in the background even after[activity lifecycle](http://developer.android.com/reference/android/app/Activity.html#ActivityLifecycle)changes (such as presenting a dialog or rotating the screen). Any listeners you had attached will also remain attached. This could cause unexpected results if they get called after the activity is stopped.

You can solve this problem by subscribing your listeners with an activity scope to automatically unregister them when the activity stops. Then, use the`getActiveUploadTasks`method when the activity restarts to obtain upload tasks that are still running or recently completed.

The example below demonstrates this and also shows how to persist the storage reference path used.  

### Kotlin

```kotlin
override fun onSaveInstanceState(outState: Bundle) {
    super.onSaveInstanceState(outState)

    // If there's an upload in progress, save the reference so you can query it later
    outState.putString("reference", storageRef.toString())
}

override fun onRestoreInstanceState(savedInstanceState: Bundle) {
    super.onRestoreInstanceState(savedInstanceState)

    // If there was an upload in progress, get its reference and create a new StorageReference
    val stringRef = savedInstanceState.getString("reference") ?: return

    storageRef = Firebase.storage.getReferenceFromUrl(stringRef)

    // Find all UploadTasks under this StorageReference (in this example, there should be one)

    val tasks = storageRef.activeUploadTasks

    if (tasks.size > 0) {
        // Get the task monitoring the upload
        val task = tasks[0]

        // Add new listeners to the task using an Activity scope
        task.addOnSuccessListener(this) {
            // Success!
            // ...
        }
    }
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/storage/app/src/main/java/com/google/firebase/referencecode/storage/kotlin/UploadActivity.kt#L25-L54
```

### Java

```java
@Override
protected void onSaveInstanceState(Bundle outState) {
    super.onSaveInstanceState(outState);

    // If there's an upload in progress, save the reference so you can query it later
    if (mStorageRef != null) {
        outState.putString("reference", mStorageRef.toString());
    }
}

@Override
protected void onRestoreInstanceState(Bundle savedInstanceState) {
    super.onRestoreInstanceState(savedInstanceState);

    // If there was an upload in progress, get its reference and create a new StorageReference
    final String stringRef = savedInstanceState.getString("reference");
    if (stringRef == null) {
        return;
    }
    mStorageRef = FirebaseStorage.getInstance().getReferenceFromUrl(stringRef);

    // Find all UploadTasks under this StorageReference (in this example, there should be one)
    List<UploadTask> tasks = mStorageRef.getActiveUploadTasks();
    if (tasks.size() > 0) {
        // Get the task monitoring the upload
        UploadTask task = tasks.get(0);

        // Add new listeners to the task using an Activity scope
        task.addOnSuccessListener(this, new OnSuccessListener<UploadTask.TaskSnapshot>() {
            @Override
            public void onSuccess(UploadTask.TaskSnapshot state) {
                // Success!
                // ...
            }
        });
    }
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/storage/app/src/main/java/com/google/firebase/referencecode/storage/UploadActivity.java#L29-L65
```

`getActiveUploadTasks`retrieves all active upload tasks at and below the provided reference, so you may need to handle multiple tasks.

## Continuing Uploads Across Process Restarts

If your process is shut down, any uploads in progress will be interrupted. However, you can continue uploading once the process restarts by resuming the upload session with the server. This can save time and bandwidth by not starting the upload from the start of the file.

To do this, begin uploading via`putFile`. On the resulting`StorageTask`, call`getUploadSessionUri`and save the resulting value in persistent storage (such as SharedPreferences).  

### Kotlin

```kotlin
uploadTask = storageRef.putFile(localFile)
uploadTask.addOnProgressListener { taskSnapshot ->
    sessionUri = taskSnapshot.uploadSessionUri
    if (sessionUri != null && !saved) {
        saved = true
        // A persisted session has begun with the server.
        // Save this to persistent storage in case the process dies.
    }
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/storage/app/src/main/java/com/google/firebase/referencecode/storage/kotlin/UploadActivity.kt#L63-L71
```

### Java

```java
uploadTask = mStorageRef.putFile(localFile);
uploadTask.addOnProgressListener(new OnProgressListener<UploadTask.TaskSnapshot>() {
    @Override
    public void onProgress(UploadTask.TaskSnapshot taskSnapshot) {
        Uri sessionUri = taskSnapshot.getUploadSessionUri();
        if (sessionUri != null && !mSaved) {
            mSaved = true;
            // A persisted session has begun with the server.
            // Save this to persistent storage in case the process dies.
        }
    }
});https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/storage/app/src/main/java/com/google/firebase/referencecode/storage/UploadActivity.java#L74-L85
```

After your process restarts with an interrupted upload, call putFile again. But this time also pass the Uri that was saved.  

### Kotlin

```kotlin
// resume the upload task from where it left off when the process died.
// to do this, pass the sessionUri as the last parameter
uploadTask = storageRef.putFile(
    localFile,
    storageMetadata { },
    sessionUri,
)https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/storage/app/src/main/java/com/google/firebase/referencecode/storage/kotlin/UploadActivity.kt#L75-L81
```

### Java

```java
//resume the upload task from where it left off when the process died.
//to do this, pass the sessionUri as the last parameter
uploadTask = mStorageRef.putFile(localFile,
        new StorageMetadata.Builder().build(), sessionUri);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/storage/app/src/main/java/com/google/firebase/referencecode/storage/UploadActivity.java#L89-L92
```

Sessions last one week. If you attempt to resume a session after it has expired or if it had experienced an error, you will receive a failure callback. It is your responsibility to ensure the file has not changed between uploads.

## Error Handling

There are a number of reasons why errors may occur on upload, including the local file not existing, or the user not having permission to upload the desired file. You can find more information about errors in the[Handle Errors](https://firebase.google.com/docs/storage/android/handle-errors)section of the docs.

## Full Example

A full example of an upload with progress monitoring and error handling is shown below:  

### Kotlin

```kotlin
// File or Blob
file = Uri.fromFile(File("path/to/mountains.jpg"))

// Create the file metadata
metadata = storageMetadata {
    contentType = "image/jpeg"
}

// Upload file and metadata to the path 'images/mountains.jpg'
uploadTask = storageRef.child("images/${file.lastPathSegment}").putFile(file, metadata)

// Listen for state changes, errors, and completion of the upload.
// You'll need to import com.google.firebase.storage.component1 and
// com.google.firebase.storage.component2
uploadTask.addOnProgressListener { (bytesTransferred, totalByteCount) ->
    val progress = (100.0 * bytesTransferred) / totalByteCount
    Log.d(TAG, "Upload is $progress% done")
}.addOnPausedListener {
    Log.d(TAG, "Upload is paused")
}.addOnFailureListener {
    // Handle unsuccessful uploads
}.addOnSuccessListener {
    // Handle successful uploads on complete
    // ...
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/storage/app/src/main/java/com/google/firebase/referencecode/storage/kotlin/StorageActivity.kt#L224-L248
```

### Java

```java
// File or Blob
file = Uri.fromFile(new File("path/to/mountains.jpg"));

// Create the file metadata
metadata = new StorageMetadata.Builder()
        .setContentType("image/jpeg")
        .build();

// Upload file and metadata to the path 'images/mountains.jpg'
uploadTask = storageRef.child("images/"+file.getLastPathSegment()).putFile(file, metadata);

// Listen for state changes, errors, and completion of the upload.
uploadTask.addOnProgressListener(new OnProgressListener<UploadTask.TaskSnapshot>() {
    @Override
    public void onProgress(UploadTask.TaskSnapshot taskSnapshot) {
        double progress = (100.0 * taskSnapshot.getBytesTransferred()) / taskSnapshot.getTotalByteCount();
        Log.d(TAG, "Upload is " + progress + "% done");
    }
}).addOnPausedListener(new OnPausedListener<UploadTask.TaskSnapshot>() {
    @Override
    public void onPaused(UploadTask.TaskSnapshot taskSnapshot) {
        Log.d(TAG, "Upload is paused");
    }
}).addOnFailureListener(new OnFailureListener() {
    @Override
    public void onFailure(@NonNull Exception exception) {
        // Handle unsuccessful uploads
    }
}).addOnSuccessListener(new OnSuccessListener<UploadTask.TaskSnapshot>() {
    @Override
    public void onSuccess(UploadTask.TaskSnapshot taskSnapshot) {
        // Handle successful uploads on complete
        // ...
    }
});https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/storage/app/src/main/java/com/google/firebase/referencecode/storage/StorageActivity.java#L277-L311
```

Now that you've uploaded files, let's learn how to[download them](https://firebase.google.com/docs/storage/android/download-files)fromCloud Storage.