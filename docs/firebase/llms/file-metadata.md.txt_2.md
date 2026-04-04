# Source: https://firebase.google.com/docs/storage/unity/file-metadata.md.txt

<br />

After uploading a file to Cloud Storage reference, you can also get
and update the file metadata, for example to update the content type. Files
can also store custom key/value pairs with additional file metadata.

> [!NOTE]
> **Note:** By default, a Cloud Storage for Firebase bucket requires Firebase Authentication to perform any action on the bucket's data or files. You can change your Firebase Security Rules for Cloud Storage to [allow unauthenticated access for specific situations](https://firebase.google.com/docs/storage/security/rules-conditions#public). However, for most situations, we strongly recommend [restricting access and setting up robust security rules](https://firebase.google.com/docs/storage/security/get-started) (especially for production apps). Note that if you use Google App Engine and have a default Cloud Storage bucket with a name format of `*.appspot.com`, you may need to consider [how your security rules impact access to App Engine files](https://firebase.google.com/docs/storage/gcp-integration#security-rules-and-app-engine-files).

## Get File Metadata

File metadata contains common properties such as `Name`, `SizeBytes`, and
`ContentType` (often referred to as MIME type) in addition to some
less common ones like `ContentDisposition` and `CreationTimeMillis`. This
metadata can be retrieved from a Cloud Storage reference using the
`GetMetadataAsync` method.

```c#
// Create reference to the file whose metadata we want to retrieve
StorageReference forestRef =
    storageRef.Child("images/forest.jpg");

// Get metadata properties
forestRef.GetMetadataAsync().ContinueWithOnMainThread(task => {
    if (!task.IsFaulted && !task.IsCanceled) {
        StorageMetadata meta = task.Result;
        // do stuff with meta
    }
});
```

## Update File Metadata

You can update file metadata at any time after the file upload completes by
using the `UpdateMetadataAsync` method which takes a `MetadataChange` object.
Refer to the [full list](https://firebase.google.com/docs/storage/unity/file-metadata#file_metadata_properties) for more information on what
properties can be updated. Only the properties specified in the metadata are
updated, all others are left unmodified.

```c#
// Create reference to the file whose metadata we want to change
StorageReference forestRef = storageRef.Child("images/forest.jpg");

// Create file metadata to update
var newMetadata = new MetadataChange();
newMetadata.CacheControl = "public,max-age=300";
newMetadata.ContentType = "image/jpeg";

// Update metadata properties
forestRef.UpdateMetadataAsync(newMetadata).ContinueWithOnMainThread(task => {
    if (!task.IsFaulted && !task.IsCanceled) {
        // access the updated meta data
        StorageMetadata meta = task.Result;
    }
});
```

You can delete writable metadata properties by passing the empty string:

```c#
// Create file metadata to update
var newMetadata = new MetadataChange();
newMetadata.ContentType = "";

// Update metadata properties
forestRef.UpdateMetadataAsync(newMetadata).ContinueWithOnMainThread(task => {
    if (!task.IsFaulted && !task.IsCanceled) {
        StorageMetadata meta = task.Result;
        // meta.ContentType should be an empty string now
    }
});
```

## Handle Errors

There are a number of reasons why errors may occur on getting or updating
metadata, including the file not existing, or the user not having permission
to access the desired file. More information on errors can be found in the
[Handle Errors](https://firebase.google.com/docs/storage/unity/handle-errors)
section of the docs.

## Custom Metadata

You can specify custom metadata as a `Dictionary<string, string>`.

```c#
var newMetadata = new MetadataChange {
    CustomMetadata = new Dictionary<string, string> {
        {"location", "Yosemite, CA, USA"},
        {"activity", "Hiking"}
    }
};

// UpdateMetadataAsync
```

You can store app-specific data for each file in custom metadata, but we highly
recommend using a database (such as the
[Firebase Realtime Database](https://firebase.google.com/docs/database)) to store and synchronize this type of
data.

## File Metadata Properties

A full list of metadata properties on a file is available below:

| Property | Type | Modifyable in MetadataChange |
|---|---|---|
| `Bucket` | `string` | NO |
| `Generation` | `string` | NO |
| `MetadataGeneration` | `string` | NO |
| `Path` | `string` | NO |
| `Name` | `string` | NO |
| `SizeBytes` | `long` | NO |
| `CreationTimeMillis` | `long` | NO |
| `UpdatedTimeMillis` | `long` | NO |
| `CacheControl` | `string` | YES |
| `ContentDisposition` | `string` | YES |
| `ContentEncoding` | `string` | YES |
| `ContentLanguage` | `string` | YES |
| `ContentType` | `string` | YES |
| `DownloadUrl` | `Uri` | NO |
| `DownloadUrls` | `IList<Uri>` | NO |
| `CustomMetadataKeys` | `IEnumerable<string>` | YES |

## Next Steps

Uploading, downloading, and updating files is important, but so is being able
to remove them. Let's learn how to
[delete files](https://firebase.google.com/docs/storage/unity/delete-files)
from Cloud Storage.