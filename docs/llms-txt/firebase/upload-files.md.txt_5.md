# Source: https://firebase.google.com/docs/storage/flutter/upload-files.md.txt

# Upload files with Cloud Storage on Flutter

<br />

Cloud Storage for Firebase allows you to quickly and easily upload files to a
[Cloud Storage](https://cloud.google.com/storage) bucket provided
and managed by Firebase.

> [!NOTE]
> **Note:** By default, a Cloud Storage for Firebase bucket requires Firebase Authentication to perform any action on the bucket's data or files. You can change your Firebase Security Rules for Cloud Storage to [allow unauthenticated access for specific situations](https://firebase.google.com/docs/storage/security/rules-conditions#public). However, for most situations, we strongly recommend [restricting access and setting up robust security rules](https://firebase.google.com/docs/storage/security/get-started) (especially for production apps). Note that if you use Google App Engine and have a default Cloud Storage bucket with a name format of `*.appspot.com`, you may need to consider [how your security rules impact access to App Engine files](https://firebase.google.com/docs/storage/gcp-integration#security-rules-and-app-engine-files).

> [!NOTE]
> **Note:** For Spark plan projects, Firebase blocks upload and hosting of certain executable file types for Windows (files with `.exe`, `.dll` and `.bat` extensions), Android (`.apk` extension) and Apple (`.ipa` extension) by Cloud Storage for Firebase and Firebase Hosting. This policy exists to prevent abuse on our platform. Projects on the Blaze plan are not affected. For more information, see [this FAQ](https://firebase.google.com/support/faq#storage-exe-restrictions).

## Upload Files

To upload a file to Cloud Storage, you first create a reference to the
full path of the file, including the file name.

    // Create a storage reference from our app
    final storageRef = FirebaseStorage.instance.ref();

    // Create a reference to "mountains.jpg"
    final mountainsRef = storageRef.child("mountains.jpg");

    // Create a reference to 'images/mountains.jpg'
    final mountainImagesRef = storageRef.child("images/mountains.jpg");

    // While the file names are the same, the references point to different files
    assert(mountainsRef.name == mountainImagesRef.name);
    assert(mountainsRef.fullPath != mountainImagesRef.fullPath);

Once you've created an appropriate reference, you then call the
`putFile()`, `putString()`, or `putData()` method to upload the file
to Cloud Storage.

You cannot upload data with a reference to the root of your
Cloud Storage bucket. Your reference must point to a child URL.

### Upload from a file

To upload a file, you must first get the absolute path to its on-device
location. For example, if a file exists within the application's documents
directory, use the official [`path_provider`](https://pub.dev/packages/path_provider)
package to generate a file path and pass it to `putFile()`:

    Directory appDocDir = await getApplicationDocumentsDirectory();
    String filePath = '${appDocDir.absolute}/file-to-upload.png';
    File file = File(filePath);

    try {
      await mountainsRef.putFile(file);
    } on firebase_core.FirebaseException catch (e) {
      // ...
    }

### Upload from a String

You can upload data as a raw, `base64`, `base64url`, or `data_url` encoded
string using the `putString()` method. For example, to upload a text string
encoded as a Data URL:

    String dataUrl = 'data:text/plain;base64,SGVsbG8sIFdvcmxkIQ==';

    try {
      await mountainsRef.putString(dataUrl, format: PutStringFormat.dataUrl);
    } on FirebaseException catch (e) {
      // ...
    }

### Uploading raw data

You can upload lower-level typed data in the form of a [`Uint8List`](https://api.dart.dev/stable/2.9.2/dart-typed_data/Uint8List-class.html)
for those cases where uploading a string or `File` is not practical. In this
case, call the `putData()` method with your data:

    try {
      // Upload raw data.
      await mountainsRef.putData(data);
    } on firebase_core.FirebaseException catch (e) {
      // ...
    }

## Get a download URL

After uploading a file, you can get a URL to download the file by calling
the `getDownloadUrl()` method on the `Reference`:

    await mountainsRef.getDownloadURL();

## Add File Metadata

You can also include metadata when you upload files.
This metadata contains typical file metadata properties such as `contentType`
(commonly referred to as MIME type). The `putFile()` method
automatically infers the MIME type from the `File` extension, but you can
override the auto-detected type by specifying `contentType` in the metadata. If
you do not provide a `contentType` and Cloud Storage cannot infer a
default from the file extension, Cloud Storage uses
`application/octet-stream`. See [Use File Metadata](https://firebase.google.com/docs/storage/flutter/file-metadata).

    try {
      await mountainsRef.putFile(file, SettableMetadata(
        contentType: "image/jpeg",
      ));
    } on firebase_core.FirebaseException catch (e) {
      // ...
    }

## Manage Uploads

In addition to starting uploads, you can pause, resume, and cancel uploads using
the `pause()`, `resume()`, and `cancel()` methods. Pause and resume events
raise `pause` and `progress` state changes respectively. Canceling an
upload causes the upload to fail with an error indicating that the
upload was canceled.

    final task = mountainsRef.putFile(largeFile);

    // Pause the upload.
    bool paused = await task.pause();
    print('paused, $paused');

    // Resume the upload.
    bool resumed = await task.resume();
    print('resumed, $resumed');

    // Cancel the upload.
    bool canceled = await task.cancel();
    print('canceled, $canceled');

## Monitor Upload Progress

You can listen to a task's event stream to handle success, failure, progress, or pauses in your
upload task:

| Event Type | Typical Usage |
|---|---|
| `TaskState.running` | Emitted periodically as data is transferred and can be used to populate an upload/download indicator. |
| `TaskState.paused` | Emitted any time the task is paused. |
| `TaskState.success` | Emitted when the task has successfully completed. |
| `TaskState.canceled` | Emitted any time the task is canceled. |
| `TaskState.error` | Emitted when the upload has failed. This can happen due to network timeouts, authorization failures, or if you cancel the task. |

    mountainsRef.putFile(file).snapshotEvents.listen((taskSnapshot) {
      switch (taskSnapshot.state) {
        case TaskState.running:
          // ...
          break;
        case TaskState.paused:
          // ...
          break;
        case TaskState.success:
          // ...
          break;
        case TaskState.canceled:
          // ...
          break;
        case TaskState.error:
          // ...
          break;
      }
    });

## Error Handling

There are a number of reasons why errors may occur on upload, including
the local file not existing, or the user not having permission to upload
the desired file. You can find more information about errors in the
[Handle Errors](https://firebase.google.com/docs/storage/flutter/handle-errors) section of the docs.

## Full Example

A full example of an upload with progress monitoring and error handling
is shown below:

    final appDocDir = await getApplicationDocumentsDirectory();
    final filePath = "${appDocDir.absolute}/path/to/mountains.jpg";
    final file = File(filePath);

    // Create the file metadata
    final metadata = SettableMetadata(contentType: "image/jpeg");

    // Create a reference to the Firebase Storage bucket
    final storageRef = FirebaseStorage.instance.ref();

    // Upload file and metadata to the path 'images/mountains.jpg'
    final uploadTask = storageRef
        .child("images/path/to/mountains.jpg")
        .putFile(file, metadata);

    // Listen for state changes, errors, and completion of the upload.
    uploadTask.snapshotEvents.listen((TaskSnapshot taskSnapshot) {
      switch (taskSnapshot.state) {
        case TaskState.running:
          final progress =
              100.0 * (taskSnapshot.bytesTransferred / taskSnapshot.totalBytes);
          print("Upload is $progress% complete.");
          break;
        case TaskState.paused:
          print("Upload is paused.");
          break;
        case TaskState.canceled:
          print("Upload was canceled");
          break;
        case TaskState.error:
          // Handle unsuccessful uploads
          break;
        case TaskState.success:
          // Handle successful uploads on complete
          // ...
          break;
      }
    });

Now that you've uploaded files, let's learn how to [download them](https://firebase.google.com/docs/storage/flutter/download-files)
from Cloud Storage.