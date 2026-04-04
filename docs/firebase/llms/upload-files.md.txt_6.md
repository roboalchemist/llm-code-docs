# Source: https://firebase.google.com/docs/storage/unity/upload-files.md.txt

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
[create a Cloud Storage reference](https://firebase.google.com/docs/storage/unity/create-reference)
to the file you want to upload.

You can create a reference by appending child paths to the root of your
Cloud Storage bucket, or you can create a reference from an existing
`gs://` or `https://` URL referencing an object in Cloud Storage.

```c#
// Create a root reference
StorageReference storageRef = storage.RootReference;

// Create a reference to "mountains.jpg"
StorageReference mountainsRef = storageRef.Child("mountains.jpg");

// Create a reference to 'images/mountains.jpg'
StorageReference mountainImagesRef =
    storageRef.Child("images/mountains.jpg");

// While the file names are the same, the references point to different files
Assert.AreEqual(mountainsRef.Name, mountainImagesRef.Name);
Assert.AreNotEqual(mountainsRef.Path, mountainImagesRef.Path);
```

You cannot upload data with a reference to the root of your
Cloud Storage bucket. Your reference must point to a child URL.

## Upload Files

Once you have a reference, you can upload files to Cloud Storage
in two ways:

1. Upload from a byte array in memory
2. Upload from a file path representing a file on device

### Upload from data in memory

The `PutBytesAsync()` method is the simplest way to upload a file to
Cloud Storage. `PutBytesAsync()` takes a byte\[\]
and returns a `System.Task<Firebase.Storage.StorageMetadata>` which will
contain information about the file when the task completes. You can optionally
use an `IProgress<UploadState>` (typically `StorageProgress<UploadState>`) to
monitor your upload status.

```c#
// Data in memory
var customBytes = new byte[] {
    /*...*/
};

// Create a reference to the file you want to upload
StorageReference riversRef = storageRef.Child("images/rivers.jpg");

// Upload the file to the path "images/rivers.jpg"
riversRef.PutBytesAsync(customBytes)
    .ContinueWith((Task<StorageMetadata> task) => {
        if (task.IsFaulted || task.IsCanceled) {
            Debug.Log(task.Exception.ToString());
            // Uh-oh, an error occurred!
        }
        else {
            // Metadata contains file metadata such as size, content-type, and md5hash.
            StorageMetadata metadata = task.Result;
            string md5Hash = metadata.Md5Hash;
            Debug.Log("Finished uploading...");
            Debug.Log("md5 hash = " + md5Hash);
        }
    });
```

### Upload from a local file

You can upload local files on the devices, such as photos and videos from the
camera, with the `PutFileAsync()` method. `PutFileAsync()` takes a `string`
representing the path to the file and returns a
`System.Task<Firebase.Storage.StorageMetadata>` which will contain
information about the file when the task completes. You can optionally
use an `IProgress<UploadState>` (typically `StorageProgress<UploadState>`) to
monitor your upload status.

```c#
// File located on disk
string localFile = "...";

// Create a reference to the file you want to upload
StorageReference riversRef = storageRef.Child("images/rivers.jpg");

// Upload the file to the path "images/rivers.jpg"
riversRef.PutFileAsync(localFile)
    .ContinueWith((Task<StorageMetadata> task) => {
        if (task.IsFaulted || task.IsCanceled) {
            Debug.Log(task.Exception.ToString());
            // Uh-oh, an error occurred!
        }
        else {
            // Metadata contains file metadata such as size, content-type, and download URL.
            StorageMetadata metadata = task.Result;
            string md5Hash = metadata.Md5Hash;
            Debug.Log("Finished uploading...");
            Debug.Log("md5 hash = " + md5Hash);
        }
    });
```

If you want to actively monitor your upload, you can use a `StorageProgress`
class or your own class that implements `IProgress<UploadState>`, with the
`PutFileAsync()` or `PutBytesAsync()` methods.
See [Manage Uploads](https://firebase.google.com/docs/storage/unity/upload-files#manage_uploads) for more information.

## Add File Metadata

You can also include metadata when you upload files. This metadata contains
typical file metadata properties such as `Name`, `Size`, and `ContentType`
(commonly referred to as MIME type). The `PutFileAsync()` method automatically
infers the content type from the filename extension, but you can override the
auto-detected type by specifying `ContentType` in the metadata. If you do not
provide a `ContentType` and Cloud Storage cannot infer a default from
the file extension, Cloud Storage uses `application/octet-stream`. See
the [Use File Metadata](https://firebase.google.com/docs/storage/unity/file-metadata)
section for more information about file metadata.

```c#
// Create storage reference
StorageReference mountainsRef = storageRef.Child("images/mountains.jpg");

byte[] customBytes = new byte[] {
    /*...*/
};
string localFile = "...";

// Create file metadata including the content type
var newMetadata = new MetadataChange();
newMetadata.ContentType = "image/jpeg";

// Upload data and metadata
mountainsRef.PutBytesAsync(customBytes, newMetadata, null,
    CancellationToken.None); // .ContinueWithOnMainThread(...
// Upload file and metadata
mountainsRef.PutFileAsync(localFile, newMetadata, null,
    CancellationToken.None); // .ContinueWithOnMainThread(...
```

## Monitor Upload Progress

You can attach listeners to uploads in order to monitor the progress of the
upload. The listener follows the standard `System.IProgress<T>`
interface. You can use an instance of the `StorageProgress` class, to provide
your own `Action<T>` as a callback for progress ticks.

```c#
// Start uploading a file
var task = storageRef.Child("images/mountains.jpg")
    .PutFileAsync(localFile, null,
        new StorageProgress<UploadState>(state => {
            // called periodically during the upload
            Debug.Log(String.Format("Progress: {0} of {1} bytes transferred.",
                state.BytesTransferred, state.TotalByteCount));
        }), CancellationToken.None, null);

task.ContinueWithOnMainThread(resultTask => {
    if (!resultTask.IsFaulted && !resultTask.IsCanceled) {
        Debug.Log("Upload finished.");
    }
});
```

## Error Handling

There are a number of reasons why errors may occur on upload, including
the local file not existing, or the user not having permission to upload
the desired file. You can find more information about errors in the
[Handle Errors](https://firebase.google.com/docs/storage/unity/handle-errors)
section of the docs.

## Next Steps

Now that you've uploaded files, let's learn how to
[download them](https://firebase.google.com/docs/storage/unity/download-files)
from Cloud Storage.