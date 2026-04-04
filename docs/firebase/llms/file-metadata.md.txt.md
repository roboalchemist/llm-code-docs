# Source: https://firebase.google.com/docs/storage/cpp/file-metadata.md.txt

# Use file metadata with Cloud Storage for C++

<br />

After uploading a file to Cloud Storage reference, you can also get
and update the file metadata, for example to update the content type. Files
can also store custom key/value pairs with additional file metadata.

> [!NOTE]
> **Note:** By default, a Cloud Storage for Firebase bucket requires Firebase Authentication to perform any action on the bucket's data or files. You can change your Firebase Security Rules for Cloud Storage to [allow unauthenticated access for specific situations](https://firebase.google.com/docs/storage/security/rules-conditions#public). However, for most situations, we strongly recommend [restricting access and setting up robust security rules](https://firebase.google.com/docs/storage/security/get-started) (especially for production apps). Note that if you use Google App Engine and have a default Cloud Storage bucket with a name format of `*.appspot.com`, you may need to consider [how your security rules impact access to App Engine files](https://firebase.google.com/docs/storage/gcp-integration#security-rules-and-app-engine-files).

## Get File Metadata

File metadata contains common properties such as `name`, `size`, and
`content_type` (often referred to as MIME type) in addition to some less common
ones like `content_disposition` and `time_created`. This metadata can be
retrieved from a Cloud Storage reference using the `GetMetadata`
method.

```c++
// Create reference to the file whose metadata we want to retrieve
StorageReference forest_ref = storage_ref.Child("images/forest.jpg");

// Get metadata properties
Future future = forest_ref.GetMetadata();

// Wait for Future to complete...

if (future.Error() != firebase::storage::kErrorNone) {
  // Uh-oh, an error occurred!
} else {
  // We can now retrieve the metadata for 'images/forest.jpg'
  Metadata* metadata = future.Result();
}
```

## Update File Metadata

You can update file metadata at any time after the file upload completes by
using the `UpdateMetadata` method. Refer to the
[full list](https://firebase.google.com/docs/storage/cpp/file-metadata#file_metadata_properties) for more information on what properties
can be updated. Only the properties specified in the metadata are updated,
all others are left unmodified.

```c++
// Create reference to the file whose metadata we want to change
firebase::storage::StorageReference forest_ref = storage_ref.child("images/forest.jpg");

// Create file metadata to update
Metadata new_metadata;
newMetadata.set_cache_control("public,max-age=300");
newMetadata.set_content_type("image/jpeg");

// Update metadata properties
Future future = forest_ref.UpdateMetadata(new_metadata);

// Wait for Future to complete...

if (future.Error() != firebase::storage::kErrorNone) {
  // Uh-oh, an error occurred!
} else {
  // We can now retrieve the updated metadata for 'images/forest.jpg'
  Metadata* metadata = future.Result();
}
```

You can delete writable metadata properties by passing the empty string:

```c++
// Create file metadata with property to delete
StorageMetadata new_metadata;
new_metadata.set_content_type("");

// Delete the metadata property
Future future = forest_ref.UpdateMetadata(new_metadata);

// Wait for Future to complete...

if (future.Error() != 0) {
  // Uh-oh, an error occurred!
} else {
  // metadata.content_type() should be an empty string
  Metadata* metadata = future.Result();
}
```

## Handle Errors

There are a number of reasons why errors may occur on getting or updating
metadata, including the file not existing, or the user not having permission
to access the desired file. More information on errors can be found in the
[Handle Errors](https://firebase.google.com/docs/storage/cpp/handle-errors)
section of the docs.

## Custom Metadata

You can specify custom metadata as an `std::map` containing `std::string`
properties.

```c++
std::map<std::string, std::string>* custom_metadata = metadata.custom_metadata();
custom_metadata->insert(std::make_pair("location", "Yosemite, CA, USA");
custom_metadata->insert(std::make_pair("activity", "Hiking");
```

You can store app-specific data for each file in custom metadata, but we highly
recommend using a database (such as the
[Firebase Realtime Database](https://firebase.google.com/docs/database)) to store and synchronize this type of
data.

## File Metadata Properties

A full list of metadata properties on a file is available below:

| Property | Type | Writable |
|---|---|---|
| `bucket` | const char\* | NO |
| `generation` | const char\* | NO |
| `metageneration` | const char\* | NO |
| `full_path` | const char\* | NO |
| `name` | const char\* | NO |
| `size` | int64_t | NO |
| `time_created` | int64_t | NO |
| `updated` | int64_t | NO |
| `cache_control` | const char\* | YES |
| `content_disposition` | const char\* | YES |
| `content_encoding` | const char\* | YES |
| `content_language` | const char\* | YES |
| `content_type` | const char\* | YES |
| `download_urls` | std::vector\<std::string\> | NO |
| `custom_metadata` | std::map\<std::string, std::string\> | YES |

## Next Steps

Uploading, downloading, and updating files is important, but so is being able
to remove them. Let's learn how to
[delete files](https://firebase.google.com/docs/storage/cpp/delete-files)
from Cloud Storage.