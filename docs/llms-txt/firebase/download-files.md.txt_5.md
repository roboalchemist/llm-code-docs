# Source: https://firebase.google.com/docs/storage/ios/download-files.md.txt

# Download files with Cloud Storage on Apple platforms

<br />

Cloud Storage for Firebase allows you to quickly and easily download
files from a [Cloud Storage](https://cloud.google.com/storage)
bucket provided and managed by Firebase.

> [!NOTE]
> **Note:** By default, a Cloud Storage for Firebase bucket requires Firebase Authentication to perform any action on the bucket's data or files. You can change your Firebase Security Rules for Cloud Storage to [allow unauthenticated access for specific situations](https://firebase.google.com/docs/storage/security/rules-conditions#public). However, for most situations, we strongly recommend [restricting access and setting up robust security rules](https://firebase.google.com/docs/storage/security/get-started) (especially for production apps). Note that if you use Google App Engine and have a default Cloud Storage bucket with a name format of `*.appspot.com`, you may need to consider [how your security rules impact access to App Engine files](https://firebase.google.com/docs/storage/gcp-integration#security-rules-and-app-engine-files).

## Create a Reference

To download a file, first
[create a Cloud Storage reference](https://firebase.google.com/docs/storage/ios/create-reference)
to the file you want to download.

You can create a reference by appending child paths to the root of your
Cloud Storage bucket, or you can create a reference from an existing
`gs://` or `https://` URL referencing an object in Cloud Storage.

### Swift

```swift
// Create a reference with an initial file path and name
let pathReference = storage.reference(withPath: "images/stars.jpg")

// Create a reference from a Google Cloud Storage URI
let gsReference = storage.reference(forURL: "gs://<your-firebase-storage-bucket>/images/stars.jpg")

// Create a reference from an HTTPS URL
// Note that in the URL, characters are URL escaped!
let httpsReference = storage.reference(forURL: "https://firebasestorage.googleapis.com/b/bucket/o/images%20stars.jpg")
```

### Objective-C

```objective-c
// Create a reference with an initial file path and name
FIRStorageReference *pathReference = [storage referenceWithPath:@"images/stars.jpg"];

// Create a reference from a Google Cloud Storage URI
FIRStorageReference *gsReference = [storage referenceForURL:@"gs://<your-firebase-storage-bucket>/images/stars.jpg"];

// Create a reference from an HTTPS URL
// Note that in the URL, characters are URL escaped!
FIRStorageReference *httpsReference = [storage referenceForURL:@"https://firebasestorage.googleapis.com/b/bucket/o/images%20stars.jpg"];
  
```

## Download Files

Once you have a reference, you can download files from Cloud Storage
in three ways:

1. Download to `NSData` in memory
2. Download to an `NSURL` representing a file on device
3. Generate an `NSURL` representing the file online

### Download in memory

Download the file to an `NSData` object in memory using the
`dataWithMaxSize:completion:` method. This is the easiest way to quickly
download a file, but it must load entire contents of your file into memory.
If you request a file larger than your app's available memory, your app will
crash. To protect against memory issues, make sure to set the max size
to something you know your app can handle, or use another
download method.

### Swift

```swift
// Create a reference to the file you want to download
let islandRef = storageRef.child("images/island.jpg")

// Download in memory with a maximum allowed size of 1MB (1 * 1024 * 1024 bytes)
islandRef.getData(maxSize: 1 * 1024 * 1024) { data, error in
  if let error = error {
    // Uh-oh, an error occurred!
  } else {
    // Data for "images/island.jpg" is returned
    let image = UIImage(data: data!)
  }
}
    
```

### Objective-C

```objective-c
// Create a reference to the file you want to download
FIRStorageReference *islandRef = [storageRef child:@"images/island.jpg"];

// Download in memory with a maximum allowed size of 1MB (1 * 1024 * 1024 bytes)
[islandRef dataWithMaxSize:1 * 1024 * 1024 completion:^(NSData *data, NSError *error){
  if (error != nil) {
    // Uh-oh, an error occurred!
  } else {
    // Data for "images/island.jpg" is returned
    UIImage *islandImage = [UIImage imageWithData:data];
  }
}];
    
```

### Download to a local file

The `writeToFile:completion:` method downloads a file directly to a local
device. Use this if your users want to have access to the file while
offline or to share in a different app. `writeToFile:completion:` returns an
`FIRStorageDownloadTask` which you can use to manage your download and monitor
the status of the upload.

### Swift

```swift
// Create a reference to the file you want to download
let islandRef = storageRef.child("images/island.jpg")

// Create local filesystem URL
let localURL = URL(string: "path/to/image")!

// Download to the local filesystem
let downloadTask = islandRef.write(toFile: localURL) { url, error in
  if let error = error {
    // Uh-oh, an error occurred!
  } else {
    // Local file URL for "images/island.jpg" is returned
  }
}
    
```

### Objective-C

```objective-c
// Create a reference to the file you want to download
FIRStorageReference *islandRef = [storageRef child:@"images/island.jpg"];

// Create local filesystem URL
NSURL *localURL = [NSURL URLWithString:@"path/to/image"];

// Download to the local filesystem
FIRStorageDownloadTask *downloadTask = [islandRef writeToFile:localURL completion:^(NSURL *URL, NSError *error){
  if (error != nil) {
    // Uh-oh, an error occurred!
  } else {
    // Local file URL for "images/island.jpg" is returned
  }
}];
    
```

If you want to actively manage your download, you can use the `writeToFile:`
method and observe the download task, rather than use the completion handler.
See [Manage Downloads](https://firebase.google.com/docs/storage/ios/download-files#manage_downloads) for more information.

### Generate a download URL

If you already have download infrastructure based around URLs, or just want
a URL to share, you can get the download URL for a file by calling the
`downloadURLWithCompletion:` method on a Cloud Storage reference.

### Swift

```swift
// Create a reference to the file you want to download
let starsRef = storageRef.child("images/stars.jpg")

// Fetch the download URL
starsRef.downloadURL { url, error in
  if let error = error {
    // Handle any errors
  } else {
    // Get the download URL for 'images/stars.jpg'
  }
}
    
```

### Objective-C

```objective-c
// Create a reference to the file you want to download
FIRStorageReference *starsRef = [storageRef child:@"images/stars.jpg"];

// Fetch the download URL
[starsRef downloadURLWithCompletion:^(NSURL *URL, NSError *error){
  if (error != nil) {
    // Handle any errors
  } else {
    // Get the download URL for 'images/stars.jpg'
  }
}];
    
```

## Downloading Images with FirebaseUI

[FirebaseUI](https://github.com/firebase/FirebaseUI-iOS) provides simple,
customizable, and production-ready native mobile bindings to eliminate
boilerplate code and promote Google best practices. Using FirebaseUI you can
quickly and easily download, cache, and display images
from Cloud Storage using our integration with
[SDWebImage](https://github.com/rs/SDWebImage).

First, add FirebaseUI to your `Podfile`:

```
pod 'FirebaseStorageUI'
```

Then you can load images directly from Cloud Storage into a
`UIImageView`:

### Swift

```swift
// Reference to an image file in Firebase Storage
let reference = storageRef.child("images/stars.jpg")

// UIImageView in your ViewController
let imageView: UIImageView = self.imageView

// Placeholder image
let placeholderImage = UIImage(named: "placeholder.jpg")

// Load the image using SDWebImage
imageView.sd_setImage(with: reference, placeholderImage: placeholderImage)
    
```

### Objective-C

```objective-c
// Reference to an image file in Firebase Storage
FIRStorageReference *reference = [storageRef child:@"images/stars.jpg"];

// UIImageView in your ViewController
UIImageView *imageView = self.imageView;

// Placeholder image
UIImage *placeholderImage;

// Load the image using SDWebImage
[imageView sd_setImageWithStorageReference:reference placeholderImage:placeholderImage];
    
```

## Manage Downloads

In addition to starting downloads, you can pause, resume, and cancel downloads
using the `pause`, `resume`, and `cancel` methods. These methods raise `pause`,
`resume`, and `cancel` events that you can observe.

### Swift

```swift
// Start downloading a file
let downloadTask = storageRef.child("images/mountains.jpg").write(toFile: localFile)

// Pause the download
downloadTask.pause()

// Resume the download
downloadTask.resume()

// Cancel the download
downloadTask.cancel()
    
```

### Objective-C

```objective-c
// Start downloading a file
FIRStorageDownloadTask *downloadTask = [[storageRef child:@"images/mountains.jpg"] writeToFile:localFile];

// Pause the download
[downloadTask pause];

// Resume the download
[downloadTask resume];

// Cancel the download
[downloadTask cancel];
    
```

## Monitor Download Progress

You can attach observers to `FIRStorageDownloadTask`s in order to monitor the
progress of the download. Adding an observer returns a `FIRStorageHandle`
that can be used to remove the observer.

### Swift

```swift
// Add a progress observer to a download task
let observer = downloadTask.observe(.progress) { snapshot in
  // A progress event occurred
}
    
```

### Objective-C

```objective-c
// Add a progress observer to a download task
NSString *observer = [downloadTask observeStatus:FIRStorageTaskStatusProgress
                                         handler:^(FIRStorageTaskSnapshot *snapshot) {
  // A progress event occurred
}];
    
```

These observers can be registered to an `FIRStorageTaskStatus` event:

| \`FIRStorageTaskStatus\` Event | Typical Usage |
|---|---|
| `FIRStorageTaskStatusResume` | This event fires when the task starts or resumes downloading, and is often used in conjunction with the `FIRStorageTaskStatusPause` event. |
| `FIRStorageTaskStatusProgress` | This event fires any time data is downloaded from Cloud Storage, and can be used to populate a download progress indicator. |
| `FIRStorageTaskStatusPause` | This event fires any time the download is paused, and is often used in conjunction with the `FIRStorageTaskStatusResume` event. |
| `FIRStorageTaskStatusSuccess` | This event fires when a download has completed successfully. |
| `FIRStorageTaskStatusFailure` | This event fires when a download has failed. Inspect the error to determine the failure reason. |

When an event occurs, an `FIRStorageTaskSnapshot` object is passed back. This
snapshot is an immutable view of the task, at the time the event occurred.
This object contains the following properties:

| Property | Type | Description |
|---|---|---|
| `progress` | `NSProgress` | An `NSProgress` object containing the progress of the download. |
| `error` | `NSError` | An error that occurred during download, if any. |
| `metadata` | `FIRStorageMetadata` | `nil` on downloads. |
| `task` | `FIRStorageDownloadTask` | The task this is a snapshot of, which can be used to manage (`pause`, `resume`, `cancel`) the task. |
| `reference` | `FIRStorageReference` | The reference this task came from. |

You can also remove observers, either individually, by status, or by removing
all of them.

### Swift

```swift
// Create a task listener handle
let observer = downloadTask.observe(.progress) { snapshot in
// A progress event occurred
}

// Remove an individual observer
downloadTask.removeObserver(withHandle: observer)

// Remove all observers of a particular status
downloadTask.removeAllObservers(for: .progress)

// Remove all observers
downloadTask.removeAllObservers()
    
```

### Objective-C

```objective-c
// Create a task listener handle
NSString *observer = [downloadTask observeStatus:FIRStorageTaskStatusProgress
                                         handler:^(FIRStorageTaskSnapshot *snapshot) {
  // A progress event occurred
}];

// Remove an individual observer
[downloadTask removeObserverWithHandle:observer];

// Remove all observers of a particular status
[downloadTask removeAllObserversForStatus:FIRStorageTaskStatusProgress];

// Remove all observers
[downloadTask removeAllObservers];
    
```

To prevent memory leaks, all observers are removed after an
`FIRStorageTaskStatusSuccess` or `FIRStorageTaskStatusFailure` occurs.

## Handle Errors

There are a number of reasons why errors may occur on download, including the
file not existing, or the user not having permission to access the desired file.
More information on errors can be found in the
[Handle Errors](https://firebase.google.com/docs/storage/ios/handle-errors)
section of the docs.

## Full Example

A full example of downloading to a local file with error handling is shown below:

### Swift

```swift
// Create a reference to the file we want to download
let starsRef = storageRef.child("images/stars.jpg")

// Start the download (in this case writing to a file)
let downloadTask = storageRef.write(toFile: localURL)

// Observe changes in status
downloadTask.observe(.resume) { snapshot in
  // Download resumed, also fires when the download starts
}

downloadTask.observe(.pause) { snapshot in
  // Download paused
}

downloadTask.observe(.progress) { snapshot in
  // Download reported progress
  let percentComplete = 100.0 * Double(snapshot.progress!.completedUnitCount)
    / Double(snapshot.progress!.totalUnitCount)
}

downloadTask.observe(.success) { snapshot in
  // Download completed successfully
}

// Errors only occur in the "Failure" case
downloadTask.observe(.failure) { snapshot in
  guard let errorCode = (snapshot.error as? NSError)?.code else {
    return
  }
  guard let error = StorageErrorCode(rawValue: errorCode) else {
    return
  }
  switch (error) {
  case .objectNotFound:
    // File doesn't exist
    break
  case .unauthorized:
    // User doesn't have permission to access file
    break
  case .cancelled:
    // User cancelled the download
    break

  /* ... */

  case .unknown:
    // Unknown error occurred, inspect the server response
    break
  default:
    // Another error occurred. This is a good place to retry the download.
    break
  }
}
    
```

### Objective-C

```objective-c
// Create a reference to the file we want to download
FIRStorageReference *starsRef = [storageRef child:@"images/stars.jpg"];

// Start the download (in this case writing to a file)
FIRStorageDownloadTask *downloadTask = [storageRef writeToFile:localURL];

// Observe changes in status
[downloadTask observeStatus:FIRStorageTaskStatusResume handler:^(FIRStorageTaskSnapshot *snapshot) {
  // Download resumed, also fires when the download starts
}];

[downloadTask observeStatus:FIRStorageTaskStatusPause handler:^(FIRStorageTaskSnapshot *snapshot) {
  // Download paused
}];

[downloadTask observeStatus:FIRStorageTaskStatusProgress handler:^(FIRStorageTaskSnapshot *snapshot) {
  // Download reported progress
  double percentComplete = 100.0 * (snapshot.progress.completedUnitCount) / (snapshot.progress.totalUnitCount);
}];

[downloadTask observeStatus:FIRStorageTaskStatusSuccess handler:^(FIRStorageTaskSnapshot *snapshot) {
  // Download completed successfully
}];

// Errors only occur in the "Failure" case
[downloadTask observeStatus:FIRStorageTaskStatusFailure handler:^(FIRStorageTaskSnapshot *snapshot) {
  if (snapshot.error != nil) {
    switch (snapshot.error.code) {
      case FIRStorageErrorCodeObjectNotFound:
        // File doesn't exist
        break;

      case FIRStorageErrorCodeUnauthorized:
        // User doesn't have permission to access file
        break;

      case FIRStorageErrorCodeCancelled:
        // User canceled the upload
        break;

      /* ... */

      case FIRStorageErrorCodeUnknown:
        // Unknown error occurred, inspect the server response
        break;
    }
  }
}];
    
```

You can also [get and update metadata](https://firebase.google.com/docs/storage/ios/file-metadata)
for files that are stored in Cloud Storage.