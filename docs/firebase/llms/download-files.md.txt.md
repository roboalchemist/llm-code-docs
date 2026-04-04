# Source: https://firebase.google.com/docs/storage/android/download-files.md.txt

# Download files with Cloud Storage on Android

<br />

Cloud Storage for Firebase allows you to quickly and easily download
files from a [Cloud Storage](https://cloud.google.com/storage)
bucket provided and managed by Firebase.

> [!NOTE]
> **Note:** By default, a Cloud Storage for Firebase bucket requires Firebase Authentication to perform any action on the bucket's data or files. You can change your Firebase Security Rules for Cloud Storage to [allow unauthenticated access for specific situations](https://firebase.google.com/docs/storage/security/rules-conditions#public). However, for most situations, we strongly recommend [restricting access and setting up robust security rules](https://firebase.google.com/docs/storage/security/get-started) (especially for production apps). Note that if you use Google App Engine and have a default Cloud Storage bucket with a name format of `*.appspot.com`, you may need to consider [how your security rules impact access to App Engine files](https://firebase.google.com/docs/storage/gcp-integration#security-rules-and-app-engine-files).

## Create a Reference

To download a file, first
[create a Cloud Storage reference](https://firebase.google.com/docs/storage/android/create-reference)
to the file you want to download.

You can create a reference by appending child paths to the root of your
Cloud Storage bucket, or you can create a reference from an existing
`gs://` or `https://` URL referencing an object in Cloud Storage.

### Kotlin

```kotlin
// Create a storage reference from our app
val storageRef = storage.reference

// Create a reference with an initial file path and name
val pathReference = storageRef.child("images/stars.jpg")

// Create a reference to a file from a Google Cloud Storage URI
val gsReference = storage.getReferenceFromUrl("gs://bucket/images/stars.jpg")

// Create a reference from an HTTPS URL
// Note that in the URL, characters are URL escaped!
val httpsReference = storage.getReferenceFromUrl(
    "https://firebasestorage.googleapis.com/b/bucket/o/images%20stars.jpg",
)
```

### Java

```java
// Create a storage reference from our app
StorageReference storageRef = storage.getReference();

// Create a reference with an initial file path and name
StorageReference pathReference = storageRef.child("images/stars.jpg");

// Create a reference to a file from a Google Cloud Storage URI
StorageReference gsReference = storage.getReferenceFromUrl("gs://bucket/images/stars.jpg");

// Create a reference from an HTTPS URL
// Note that in the URL, characters are URL escaped!
StorageReference httpsReference = storage.getReferenceFromUrl("https://firebasestorage.googleapis.com/b/bucket/o/images%20stars.jpg");
```

## Download Files

Once you have a reference, you can download files from Cloud Storage
by calling the `getBytes()` or `getStream()`. If you prefer to download the file
with another library, you can get a download URL with `getDownloadUrl()`.

### Download in memory

Download the file to a `byte[]` with the `getBytes()` method. This is the
easiest way to download a file, but it must load the entire contents of
your file into memory. If you request a file larger than your app's available
memory, your app will crash. To protect against memory issues, `getBytes()`
takes a maximum amount of bytes to download. Set the maximum size to something
you know your app can handle, or use another download method.

### Kotlin

```kotlin
var islandRef = storageRef.child("images/island.jpg")

val ONE_MEGABYTE: Long = 1024 * 1024
islandRef.getBytes(ONE_MEGABYTE).addOnSuccessListener {
    // Data for "images/island.jpg" is returned, use this as needed
}.addOnFailureListener {
    // Handle any errors
}
```

### Java

```java
StorageReference islandRef = storageRef.child("images/island.jpg");

final long ONE_MEGABYTE = 1024 * 1024;
islandRef.getBytes(ONE_MEGABYTE).addOnSuccessListener(new OnSuccessListener<byte[]>() {
    @Override
    public void onSuccess(byte[] bytes) {
        // Data for "images/island.jpg" is returns, use this as needed
    }
}).addOnFailureListener(new OnFailureListener() {
    @Override
    public void onFailure(@NonNull Exception exception) {
        // Handle any errors
    }
});
```

### Download to a local file

The `getFile()` method downloads a file directly to a local device. Use this if
your users want to have access to the file while offline or to share the file in a
different app. `getFile()` returns a `DownloadTask` which you can use to manage
your download and monitor the status of the download.

### Kotlin

```kotlin
islandRef = storageRef.child("images/island.jpg")

val localFile = File.createTempFile("images", "jpg")

islandRef.getFile(localFile).addOnSuccessListener {
    // Local temp file has been created
}.addOnFailureListener {
    // Handle any errors
}
```

### Java

```java
islandRef = storageRef.child("images/island.jpg");

File localFile = File.createTempFile("images", "jpg");

islandRef.getFile(localFile).addOnSuccessListener(new OnSuccessListener<FileDownloadTask.TaskSnapshot>() {
    @Override
    public void onSuccess(FileDownloadTask.TaskSnapshot taskSnapshot) {
        // Local temp file has been created
    }
}).addOnFailureListener(new OnFailureListener() {
    @Override
    public void onFailure(@NonNull Exception exception) {
        // Handle any errors
    }
});
```

If you want to actively manage your download, see
[Manage Downloads](https://firebase.google.com/docs/storage/android/download-files#manage_downloads) for more information.

## Download Data via URL

If you already have download infrastructure based around URLs, or just want
a URL to share, you can get the download URL for a file by calling the
`getDownloadUrl()` method on a Cloud Storage reference.

### Kotlin

```kotlin
storageRef.child("users/me/profile.png").downloadUrl.addOnSuccessListener {
    // Got the download URL for 'users/me/profile.png'
}.addOnFailureListener {
    // Handle any errors
}
```

### Java

```java
storageRef.child("users/me/profile.png").getDownloadUrl().addOnSuccessListener(new OnSuccessListener<Uri>() {
    @Override
    public void onSuccess(Uri uri) {
        // Got the download URL for 'users/me/profile.png'
    }
}).addOnFailureListener(new OnFailureListener() {
    @Override
    public void onFailure(@NonNull Exception exception) {
        // Handle any errors
    }
});
```

## Downloading Images with FirebaseUI

[FirebaseUI](https://github.com/firebase/FirebaseUI-Android) provides simple,
customizable, and production-ready native mobile bindings to eliminate
boilerplate code and promote Google best practices. Using FirebaseUI you can
quickly and easily download, cache, and display images
from Cloud Storage using our integration with
[Glide](https://github.com/bumptech/glide).

First, add FirebaseUI to your `app/build.gradle`:

```
dependencies {
    // FirebaseUI Storage only
    implementation 'com.firebaseui:firebase-ui-storage:9.0.0'
}
```

Then you can load images directly from Cloud Storage into an `ImageView`:

### Kotlin

```kotlin
// Reference to an image file in Cloud Storage
val storageReference = Firebase.storage.reference

// ImageView in your Activity
val imageView = findViewById<ImageView>(R.id.imageView)

// Download directly from StorageReference using Glide
// (See MyAppGlideModule for Loader registration)
Glide.with(context)
    .load(storageReference)
    .into(imageView)
```

### Java

```java
// Reference to an image file in Cloud Storage
StorageReference storageReference = FirebaseStorage.getInstance().getReference();

// ImageView in your Activity
ImageView imageView = findViewById(R.id.imageView);

// Download directly from StorageReference using Glide
// (See MyAppGlideModule for Loader registration)
Glide.with(context)
        .load(storageReference)
        .into(imageView);
```

## Handle Activity Lifecycle Changes

Downloads continue in the background even after [activity lifecycle](http://developer.android.com/reference/android/app/Activity.html#ActivityLifecycle) changes (such
as presenting a dialog or rotating the screen). Any listeners you had attached
will also remain attached. This could cause unexpected results if they get
called after the activity is stopped.

You can solve this problem by subscribing your listeners with an activity scope
to automatically unregister them when the activity stops. Then, use the
`getActiveDownloadTasks` method when the activity restarts to obtain download
tasks that are still running or recently completed.

The example below demonstrates this and also shows how to persist the storage
reference path used.

### Kotlin

```kotlin
override fun onSaveInstanceState(outState: Bundle) {
    super.onSaveInstanceState(outState)

    // If there's a download in progress, save the reference so you can query it later
    outState.putString("reference", storageRef.toString())
}

override fun onRestoreInstanceState(savedInstanceState: Bundle) {
    super.onRestoreInstanceState(savedInstanceState)

    // If there was a download in progress, get its reference and create a new StorageReference
    val stringRef = savedInstanceState.getString("reference") ?: return

    storageRef = Firebase.storage.getReferenceFromUrl(stringRef)

    // Find all DownloadTasks under this StorageReference (in this example, there should be one)
    val tasks = storageRef.activeDownloadTasks

    if (tasks.size > 0) {
        // Get the task monitoring the download
        val task = tasks[0]

        // Add new listeners to the task using an Activity scope
        task.addOnSuccessListener(this) {
            // Success!
            // ...
        }
    }
}
```

### Java

```java
@Override
protected void onSaveInstanceState(Bundle outState) {
    super.onSaveInstanceState(outState);

    // If there's a download in progress, save the reference so you can query it later
    if (mStorageRef != null) {
        outState.putString("reference", mStorageRef.toString());
    }
}

@Override
protected void onRestoreInstanceState(Bundle savedInstanceState) {
    super.onRestoreInstanceState(savedInstanceState);

    // If there was a download in progress, get its reference and create a new StorageReference
    final String stringRef = savedInstanceState.getString("reference");
    if (stringRef == null) {
        return;
    }
    mStorageRef = FirebaseStorage.getInstance().getReferenceFromUrl(stringRef);

    // Find all DownloadTasks under this StorageReference (in this example, there should be one)
    List<FileDownloadTask> tasks = mStorageRef.getActiveDownloadTasks();
    if (tasks.size() > 0) {
        // Get the task monitoring the download
        FileDownloadTask task = tasks.get(0);

        // Add new listeners to the task using an Activity scope
        task.addOnSuccessListener(this, new OnSuccessListener<FileDownloadTask.TaskSnapshot>() {
            @Override
            public void onSuccess(FileDownloadTask.TaskSnapshot state) {
                // Success!
                // ...
            }
        });
    }
}
```

## Handle Errors

There are a number of reasons why errors may occur on download, including the
file not existing, or the user not having permission to access the desired file.
More information on errors can be found in the
[Handle Errors](https://firebase.google.com/docs/storage/android/handle-errors)
section of the docs.

## Full Example

A full example of a download with error handling is shown below:

### Kotlin

```kotlin
storageRef.child("users/me/profile.png").getBytes(Long.MAX_VALUE).addOnSuccessListener {
    // Use the bytes to display the image
}.addOnFailureListener {
    // Handle any errors
}
```

### Java

```java
storageRef.child("users/me/profile.png").getBytes(Long.MAX_VALUE).addOnSuccessListener(new OnSuccessListener<byte[]>() {
    @Override
    public void onSuccess(byte[] bytes) {
        // Use the bytes to display the image
    }
}).addOnFailureListener(new OnFailureListener() {
    @Override
    public void onFailure(@NonNull Exception exception) {
        // Handle any errors
    }
});
```

You can also [get and update metadata](https://firebase.google.com/docs/storage/android/file-metadata)
for files that are stored in Cloud Storage.