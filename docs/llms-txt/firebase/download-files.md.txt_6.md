# Source: https://firebase.google.com/docs/storage/unity/download-files.md.txt

<br />

Cloud Storage for Firebase allows you to quickly and easily download
files from a [Cloud Storage](https://cloud.google.com/storage)
bucket provided and managed by Firebase.

> [!NOTE]
> **Note:** By default, a Cloud Storage for Firebase bucket requires Firebase Authentication to perform any action on the bucket's data or files. You can change your Firebase Security Rules for Cloud Storage to [allow unauthenticated access for specific situations](https://firebase.google.com/docs/storage/security/rules-conditions#public). However, for most situations, we strongly recommend [restricting access and setting up robust security rules](https://firebase.google.com/docs/storage/security/get-started) (especially for production apps). Note that if you use Google App Engine and have a default Cloud Storage bucket with a name format of `*.appspot.com`, you may need to consider [how your security rules impact access to App Engine files](https://firebase.google.com/docs/storage/gcp-integration#security-rules-and-app-engine-files).

## Create a Reference

To download a file, first
[create a Cloud Storage reference](https://firebase.google.com/docs/storage/unity/create-reference)
to the file you want to download.

You can create a reference by appending child paths to the root of your
Cloud Storage bucket, or you can create a reference from an existing
`gs://` or `https://` URL referencing an object in Cloud Storage.

```c#
// Create a reference with an initial file path and name
StorageReference pathReference =
    storage.GetReference("images/stars.jpg");

// Create a reference from a Google Cloud Storage URI
StorageReference gsReference =
    storage.GetReferenceFromUrl("gs://bucket/images/stars.jpg");

// Create a reference from an HTTPS URL
// Note that in the URL, characters are URL escaped!
StorageReference httpsReference =
    storage.GetReferenceFromUrl("https://firebasestorage.googleapis.com/b/bucket/o/images%20stars.jpg");
```

## Download Files

Once you have a reference, you can download files from Cloud Storage
in four ways:

1. Download from a URL
2. Download to a byte array
3. Download with a Stream
4. Download to a local file

The method you will use to retrieve your files will depend on how you want to
consume the data in your game.

### Download from a URL

If you want to use a URL with Unity's [`WWW`](https://docs.unity3d.com/ScriptReference/WWW.html) or [`UnityWebRequest`](https://docs.unity3d.com/ScriptReference/Networking.UnityWebRequest.html) you can
get a download URL for a file by calling `GetDownloadUrlAsync()`.

```c#
// Fetch the download URL
reference.GetDownloadUrlAsync().ContinueWithOnMainThread(task => {
    if (!task.IsFaulted && !task.IsCanceled) {
        Debug.Log("Download URL: " + task.Result);
        // ... now download the file via WWW or UnityWebRequest.
    }
});
```

### Download to a byte array

You can download the file to a byte buffer in memory using the `GetBytesAsync()` method.
This method will load the entire contents of your file into memory.
If you request a file larger than your app's available memory, your app will crash.
To protect against memory issues, make sure to set the max size to something
you know your app can handle, or use another download method.

```c#
// Download in memory with a maximum allowed size of 1MB (1 * 1024 * 1024 bytes)
const long maxAllowedSize = 1 * 1024 * 1024;
reference.GetBytesAsync(maxAllowedSize).ContinueWithOnMainThread(task => {
    if (task.IsFaulted || task.IsCanceled) {
        Debug.LogException(task.Exception);
        // Uh-oh, an error occurred!
    }
    else {
        byte[] fileContents = task.Result;
        Debug.Log("Finished downloading!");
    }
});
```

### Download via a Stream

Downloading the file with a Stream allows you to process the data as its loaded.
This gives you maximum flexibility when dealing with your download. Call
`GetStreamAsync()` and pass your own stream processor as the first argument.
This delegate will get called on a background thread with a Stream which
allows you to perform latency intensive operations or calculations such as
storing the contents to disk.

```c#
// Download via a Stream
reference.GetStreamAsync(stream => {
    // Do something with the stream here.
    //
    // This code runs on a background thread which reduces the impact
    // to your framerate.
    //
    // If you want to do something on the main thread, you can do that in the
    // progress eventhandler (second argument) or ContinueWith to execute it
    // at task completion.
}, null, CancellationToken.None);
```

`GetStreamAsync()` takes an optional arguments after the stream processor that
allows you to cancel the operation or get notified of progress.

### Download to a local file

The `GetFileAsync()` method downloads a file directly to a local device. Use this if
your users want to have access to the file while offline or to share the file in a
different app.

```c#
// Create local filesystem URL
string localUrl = "file:///local/images/island.jpg";

// Download to the local filesystem
reference.GetFileAsync(localUrl).ContinueWithOnMainThread(task => {
    if (!task.IsFaulted && !task.IsCanceled) {
        Debug.Log("File downloaded.");
    }
});
```

You can attach listeners to downloads in order to monitor the progress of the
download. The listener follows the standard `System.IProgress<T>`
interface. You can use an instance of the `StorageProgress` class, to provide
your own `Action<T>` as a callback for progress ticks.

```c#
// Create local filesystem URL
string localUrl = "file:///local/images/island.jpg";

// Start downloading a file
Task task = reference.GetFileAsync(localFile,
    new StorageProgress<DownloadState>(state => {
        // called periodically during the download
        Debug.Log(String.Format(
            "Progress: {0} of {1} bytes transferred.",
            state.BytesTransferred,
            state.TotalByteCount
        ));
    }), CancellationToken.None);

task.ContinueWithOnMainThread(resultTask => {
    if (!resultTask.IsFaulted && !resultTask.IsCanceled) {
        Debug.Log("Download finished.");
    }
});
```

## Handle Errors

There are a number of reasons why errors may occur on download, including the
file not existing, or the user not having permission to access the desired file.
More information on errors can be found in the
[Handle Errors](https://firebase.google.com/docs/storage/unity/handle-errors)
section of the docs.

## Next Steps

You can also [get and update metadata](https://firebase.google.com/docs/storage/unity/file-metadata)
for files that are stored in Cloud Storage.