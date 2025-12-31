# Source: https://firebase.google.com/docs/storage/web/download-files.md.txt

# Source: https://firebase.google.com/docs/storage/flutter/download-files.md.txt

# Source: https://firebase.google.com/docs/storage/android/download-files.md.txt

# Source: https://firebase.google.com/docs/storage/unity/download-files.md.txt

# Source: https://firebase.google.com/docs/storage/ios/download-files.md.txt

# Source: https://firebase.google.com/docs/storage/cpp/download-files.md.txt

# Source: https://firebase.google.com/docs/storage/unity/download-files.md.txt

# Source: https://firebase.google.com/docs/storage/ios/download-files.md.txt

# Source: https://firebase.google.com/docs/storage/cpp/download-files.md.txt

<br />

Cloud Storage for Firebaseallows you to quickly and easily download files from a[Cloud Storage](https://cloud.google.com/storage)bucket provided and managed by Firebase.
| **Note:** By default, aCloud Storage for Firebasebucket requiresFirebase Authenticationto perform any action on the bucket's data or files. You can change yourFirebase Security RulesforCloud Storageto[allow unauthenticated access for specific situations](https://firebase.google.com/docs/storage/security/rules-conditions#public). However, for most situations, we strongly recommend[restricting access and setting up robust security rules](https://firebase.google.com/docs/storage/security/get-started)(especially for production apps). Note that if you useGoogleApp Engineand have a defaultCloud Storagebucket with a name format of`*.appspot.com`, you may need to consider[how your security rules impact access toApp Enginefiles](https://firebase.google.com/docs/storage/gcp-integration#security-rules-and-app-engine-files).

## Create a Reference

To download a file, first[create aCloud Storagereference](https://firebase.google.com/docs/storage/cpp/create-reference)to the file you want to download.

You can create a reference by appending child paths to the root of yourCloud Storagebucket, or you can create a reference from an existing`gs://`or`https://`URL referencing an object inCloud Storage.  

```c++
// Create a reference with an initial file path and name
StorageReference path_reference = storage->GetReference("images/stars.jpg");

// Create a reference from a Cloud Storage URI
StorageReference gs_reference = storage->GetReferenceFromUrl("gs://bucket/images/stars.jpg");

// Create a reference from an HTTPS URL
// Note that in the URL, characters are URL escaped!
StorageReference https_reference = storage->GetReferenceFromUrl("https://firebasestorage.googleapis.com/b/bucket/o/images%20stars.jpg");
```

## Download Files

Once you have a reference, you can download files fromCloud Storagein three ways:

1. Download to a buffer in memory
2. Download to an specific path on the device
3. Generate an string URL representing the file online

### Download in memory

Download the file to a byte buffer in memory using the`GetBytes()`method. This is the easiest way to quickly download a file, but it must load entire contents of your file into memory. If you request a file larger than your app's available memory, your app will crash. To protect against memory issues, make sure to set the max size to something you know your app can handle, or use another download method.  

```c++
// Create a reference to the file you want to download
StorageReference island_ref = storage_ref.Child("images/island.jpg");

// Download in memory with a maximum allowed size of 1MB (1 * 1024 * 1024 bytes)
const size_t kMaxAllowedSize = 1 * 1024 * 1024
int8_t byte_buffer[kMaxAllowedSize];
firebase::Future<size_t> future = island_ref.GetBytes(byte_buffer, kMaxAllowedSize);
```

At the point the request has been made but we have to wait for the Future to complete before we can read the file. Since games typically run in a loop, and are less callback driven than other applications, you'll typically poll for completion.  

```c++
// In the game loop that polls for the result...

if (future.status() != firebase::kFutureStatusPending) {
  if (future.status() != firebase::kFutureStatusComplete) {
    LogMessage("ERROR: GetBytes() returned an invalid future.");
    // Handle the error...
  } else if (future.Error() != firebase::storage::kErrorNone) {
    LogMessage("ERROR: GetBytes() returned error %d: %s", future.Error(),
               future.error_message());
    // Handle the error...
  } else {
    // byte_buffer is now populated with data for "images/island.jpg"
  }
}
```

### Download to a local file

The`GetFile()`method downloads a file directly to a local device. Use this if your users want to have access to the file while offline or to share in a different app.  

```c++
// Create a reference to the file you want to download
StorageReference islandRef = storage_ref.Child("images/island.jpg"];

// Create local filesystem URL
const char* local_url = "file:///local/images/island.jpg";

// Download to the local filesystem
Future<size_t> future = islandRef.GetFile(local_url);

// Wait for Future to complete...

if (future.Error() != firebase::storage::kErrorNone) {
  // Uh-oh, an error occurred!
} else {
  // The file has been downloaded to local file URL "images/island.jpg"
}
```

`GetFile()`takes an optional`Controller`argument which you can use to manage your download. See[Manage Downloads](https://firebase.google.com/docs/storage/cpp/download-files#manage_downloads)for more information.

### Generate a download URL

If you already have download infrastructure based around URLs, or just want a URL to share, you can get the download URL for a file by calling the`GetDownloadUrl()`method on aCloud Storagereference.  

```c++
// Create a reference to the file you want to download
StorageReference stars_ref = storage_ref.Child("images/stars.jpg");

// Fetch the download URL
firebase::Future<std::string> future = stars_ref.GetDownloadUrl();

// Wait for Future to complete...

if (future.Error() != firebase::storage::kErrorNone) {
  // Uh-oh, an error occurred!
} else {
  // Get the download URL for 'images/stars.jpg'
  std::string download_url = future.Result();
}
```

## Manage Downloads

In addition to starting downloads, you can pause, resume, and cancel downloads using the`Pause()`,`Resume()`, and`Cancel()`methods on`Controller`, which you may optionally pass to the`GetBytes()`or`GetFile()`methods.  

```c++
// Start downloading a file
Controller controller;
storage_ref.Child("images/mountains.jpg").GetFile(local_file, nullptr, &controller);

// Pause the download
controller.Pause();

// Resume the download
controller.Resume();

// Cancel the download
controller.Cancel();
```

## Monitor Download Progress

You can attach listeners to downloads in order to monitor the progress of the download.  

```c++
class MyListener : public firebase::storage::Listener {
 public:
  virtual void OnProgress(firebase::storage::Controller* controller) {
    // A progress event occurred
  }
};

{
  // Start uploading a file
  MyEventListener my_listener;
  storage_ref.Child("images/mountains.jpg").GetFile(local_file, my_listener);
}
```

## Handle Errors

There are a number of reasons why errors may occur on download, including the file not existing, or the user not having permission to access the desired file. More information on errors can be found in the[Handle Errors](https://firebase.google.com/docs/storage/cpp/handle-errors)section of the docs.

## Next Steps

You can also[get and update metadata](https://firebase.google.com/docs/storage/cpp/file-metadata)for files that are stored inCloud Storage.