# Source: https://firebase.google.com/docs/storage/cpp/upload-files.md.txt

# Upload Files with Cloud Storage for C++

<br />

Cloud Storage for Firebase allows you to quickly and easily upload files to a
[Cloud Storage](https://cloud.google.com/storage) bucket provided
and managed by Firebase.

> [!NOTE]
> **Note:** By default, a Cloud Storage for Firebase bucket requires Firebase Authentication to perform any action on the bucket's data or files. You can change your Firebase Security Rules for Cloud Storage to [allow unauthenticated access for specific situations](https://firebase.google.com/docs/storage/security/rules-conditions#public). However, for most situations, we strongly recommend [restricting access and setting up robust security rules](https://firebase.google.com/docs/storage/security/get-started) (especially for production apps). Note that if you use Google App Engine and have a default Cloud Storage bucket with a name format of `*.appspot.com`, you may need to consider [how your security rules impact access to App Engine files](https://firebase.google.com/docs/storage/gcp-integration#security-rules-and-app-engine-files).

> [!NOTE]
> **Note:** For Spark plan projects, Firebase blocks upload and hosting of certain executable file types for Windows (files with `.exe`, `.dll` and `.bat` extensions), Android (`.apk` extension) and Apple (`.ipa` extension) by Cloud Storage for Firebase and Firebase Hosting. This policy exists to prevent abuse on our platform. Projects on the Blaze plan are not affected. For more information, see [this FAQ](https://firebase.google.com/support/faq#storage-exe-restrictions).

## Create a Reference

To upload a file, first
[create a Cloud Storage reference](https://firebase.google.com/docs/storage/cpp/create-reference)
to the location in Cloud Storage you want to upload the file to.

You can create a reference by appending child paths to the root of your
Cloud Storage bucket:

```c++
// Create a root reference
StorageReference storage_ref = storage->GetReference();

// Create a reference to "mountains.jpg"
StorageReference mountains_ref = storage_ref.Child("mountains.jpg");

// Create a reference to 'images/mountains.jpg'
StorageReference mountain_images_ref = storage_ref.Child("images/mountains.jpg");

// While the file names are the same, the references point to different files
mountains_ref.name() == mountain_images_ref.name();           // true
mountains_ref.full_path() == mountain_images_ref.full_path(); // false
```

You cannot upload data with a reference to the root of your
Cloud Storage bucket. Your reference must point to a child URL.

## Upload Files

Once you have a reference, you can upload files to Cloud Storage
in two ways:

1. Upload from a byte buffer in memory
2. Upload from a file path representing a file on device

### Upload from data in memory

The `PutData()` method is the simplest way to upload a file to
Cloud Storage. `PutData()` takes a byte buffer and returns a
`Future<Metadata>` which will contain information about the file
when the Future completes. You can use a `Controller` to manage your upload and
monitor its status.

```c++
// Data in memory
const size_t kByteBufferSize = ...
uint8_t byte_buffer[kByteBufferSize] = { ... };

// Create a reference to the file you want to upload
StorageReference rivers_ref = storage_ref.Child("images/rivers.jpg");

// Upload the file to the path "images/rivers.jpg"
Future future = rivers_ref.PutBytes(byte_buffer, kByteBufferSize);
```

At the point the request has been made but we have to wait for the Future to
complete before the file is uploaded. Since games typically run in a loop, and
are less callback driven than other applications, you'll typically poll for
completion.

```c++
if (future.status() != firebase::kFutureStatusPending) {
  if (future.status() != firebase::kFutureStatusComplete) {
    LogMessage("ERROR: GetData() returned an invalid future.");
    // Handle the error...
  } else if (future.Error() != firebase::storage::kErrorNone) {
    LogMessage("ERROR: GetData() returned error %d: %s", future.Error(),
               future.error_message());
    // Handle the error...
    }
  } else {
    // Metadata contains file metadata such as size, content-type, and download URL.
    Metadata* metadata = future.Result();
    std::string download_url = metadata->download_url();
  }
}
```

### Upload from a local file

You can upload local files on the devices, such as photos and videos from the
camera, with the `PutFile()` method. `PutFile()` takes a `std::string`
representing the path to the file and returns a
`Future<Metadata>` which will contain
information about the file when the Future completes. You can use a
`Controller` to manage your upload and monitor its status.

```c++
// File located on disk
std::string local_file = ...

// Create a reference to the file you want to upload
StorageReference rivers_ref = storage_ref.Child("images/rivers.jpg");

// Upload the file to the path "images/rivers.jpg"
Future future = rivers_ref.PutFile(localFile);

// Wait for Future to complete...

if (future.Error() != firebase::storage::kErrorNone) {
  // Uh-oh, an error occurred!
} else {
  // Metadata contains file metadata such as size, content-type, and download URL.
  Metadata* metadata = future.Result();
  std::string download_url = metadata->download_url();
}
```

If you want to actively manage your upload, you can supply a `Controller` to the
`PutFile()` or `PutBytes()` methods. This allows you to use the controller to
observe the ongoing upload operation. See [Manage Uploads](https://firebase.google.com/docs/storage/cpp/upload-files#manage_uploads) for
more information.

## Add File Metadata

You can also include metadata when you upload files. This metadata contains
typical file metadata properties such as `name`, `size`, and `content_type`
(commonly referred to as MIME type). The `PutFile()` method automatically infers
the content type from the filename extension, but you can override the
auto-detected type by specifying `content_type` in the metadata. If you do not
provide a `content_type` and Cloud Storage cannot infer a default from
the file extension, Cloud Storage uses `application/octet-stream`. See
the [Use File Metadata](https://firebase.google.com/docs/storage/cpp/file-metadata)
section for more information about file metadata.

```c++
// Create storage reference
StorageReference mountains_ref = storage_ref.Child("images/mountains.jpg");

// Create file metadata including the content type
StorageMetadata metadata;
metadata.set_content_type("image/jpeg");

// Upload data and metadata
mountains_ref.PutBytes(data, metadata);

// Upload file and metadata
mountains_ref.PutFile(local_file, metadata);
```

## Manage Uploads

In addition to starting uploads, you can pause, resume, and cancel uploads using
the `Pause()`, `Resume()`, and `Cancel()` methods on `Controller`, which you may
optionally pass to the `PutBytes()` or `PutFile()` methods.

```c++
// Start uploading a file
firebase::storage::Controller controller;
storage_ref.Child("images/mountains.jpg").PutFile(local_file, nullptr, &controller);

// Pause the upload
controller.Pause();

// Resume the upload
controller.Resume();

// Cancel the upload
controller.Cancel();
```

## Monitor Upload Progress

You can attach listeners to uploads in order to monitor the progress of the
upload.

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
  storage_ref.Child("images/mountains.jpg").PutFile(local_file, my_listener);
}
```

## Error Handling

There are a number of reasons why errors may occur on upload, including
the local file not existing, or the user not having permission to upload
the desired file. You can find more information about errors in the
[Handle Errors](https://firebase.google.com/docs/storage/cpp/handle-errors)
section of the docs.

## Next Steps

Now that you've uploaded files, let's learn how to
[download them](https://firebase.google.com/docs/storage/cpp/download-files)
from Cloud Storage.