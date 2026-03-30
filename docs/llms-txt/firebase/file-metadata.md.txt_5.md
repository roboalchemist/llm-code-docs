# Source: https://firebase.google.com/docs/storage/ios/file-metadata.md.txt

# Use file metadata with Cloud Storage on Apple platforms

<br />

After uploading a file to Cloud Storage reference, you can also get
and update the file metadata, for example to update the content type. Files
can also store custom key/value pairs with additional file metadata.

> [!NOTE]
> **Note:** By default, a Cloud Storage for Firebase bucket requires Firebase Authentication to perform any action on the bucket's data or files. You can change your Firebase Security Rules for Cloud Storage to [allow unauthenticated access for specific situations](https://firebase.google.com/docs/storage/security/rules-conditions#public). However, for most situations, we strongly recommend [restricting access and setting up robust security rules](https://firebase.google.com/docs/storage/security/get-started) (especially for production apps). Note that if you use Google App Engine and have a default Cloud Storage bucket with a name format of `*.appspot.com`, you may need to consider [how your security rules impact access to App Engine files](https://firebase.google.com/docs/storage/gcp-integration#security-rules-and-app-engine-files).

## Get File Metadata

File metadata contains common properties such as `name`, `size`, and
`contentType` (often referred to as MIME type) in addition to some less
common ones like `contentDisposition` and `timeCreated`. This metadata can be
retrieved from a Cloud Storage reference using
the `metadataWithCompletion:` method.

### Swift

```swift
// Create reference to the file whose metadata we want to retrieve
let forestRef = storageRef.child("images/forest.jpg")

// Get metadata properties
do {
  let metadata = try await forestRef.getMetadata()
} catch {
  // ...
}
    
```

### Objective-C

```objective-c
// Create reference to the file whose metadata we want to retrieve
FIRStorageReference *forestRef = [storageRef child:@"images/forest.jpg"];

// Get metadata properties
[forestRef metadataWithCompletion:^(FIRStorageMetadata *metadata, NSError *error) {
  if (error != nil) {
    // Uh-oh, an error occurred!
  } else {
    // Metadata now contains the metadata for 'images/forest.jpg'
  }
}];
  
```

## Update File Metadata

You can update file metadata at any time after the file upload completes by
using the `updateMetadata:withCompletion:` method. Refer to the
[full list](https://firebase.google.com/docs/storage/ios/file-metadata#file_metadata_properties) for more information on what properties
can be updated. Only the properties specified in the metadata are updated,
all others are left unmodified.

### Swift

```swift
// Create reference to the file whose metadata we want to change
let forestRef = storageRef.child("images/forest.jpg")

// Create file metadata to update
let newMetadata = StorageMetadata()
newMetadata.cacheControl = "public,max-age=300"
newMetadata.contentType = "image/jpeg"

// Update metadata properties
do {
  let updatedMetadata = try await forestRef.updateMetadata(newMetadata)
} catch {
  // ...
}
    
```

### Objective-C

```objective-c
// Create reference to the file whose metadata we want to change
FIRStorageReference *forestRef = [storageRef child:@"images/forest.jpg"];

// Create file metadata to update
FIRStorageMetadata *newMetadata = [[FIRStorageMetadata alloc] init];
newMetadata.cacheControl = @"public,max-age=300";
newMetadata.contentType = @"image/jpeg";

// Update metadata properties
[forestRef updateMetadata:newMetadata completion:^(FIRStorageMetadata *metadata, NSError *error){
  if (error != nil) {
    // Uh-oh, an error occurred!
  } else {
    // Updated metadata for 'images/forest.jpg' is returned
  }
}];
  
```

You can delete writable metadata properties by setting them to `nil`:

### Objective-C

```objective-c
FIRStorageMetadata *newMetadata = [[FIRStorageMetadata alloc] init];
newMetadata.contentType = nil;

// Delete the metadata property
[forestRef updateMetadata:newMetadata completion:^(FIRStorageMetadata *metadata, NSError *error){
  if (error != nil) {
    // Uh-oh, an error occurred!
  } else {
    // metadata.contentType should be nil
  }
}];
```

### Swift

```swift
let newMetadata = StorageMetadata()
newMetadata.contentType = nil

do {
  // Delete the metadata property
  let updatedMetadata = try await forestRef.updateMetadata(newMetadata)
} catch {
  // ...
}
```

## Handle Errors

There are a number of reasons why errors may occur on getting or updating
metadata, including the file not existing, or the user not having permission
to access the desired file. More information on errors can be found in the
[Handle Errors](https://firebase.google.com/docs/storage/ios/handle-errors)
section of the docs.

## Custom Metadata

You can specify custom metadata as an `NSDictionary` containing `NSString`
properties.

### Swift

```swift
let metadata = [
  "customMetadata": [
    "location": "Yosemite, CA, USA",
    "activity": "Hiking"
  ]
]
    
```

### Objective-C

```objective-c
NSDictionary *metadata = @{
  @"customMetadata": @{
    @"location": @"Yosemite, CA, USA",
    @"activity": @"Hiking"
  }
};
```

You can store app-specific data for each file in custom metadata, but we highly
recommend using a database (such as the
[Firebase Realtime Database](https://firebase.google.com/docs/database)) to store and synchronize this type of
data.

## File Metadata Properties

A full list of metadata properties on a file is available below:

| Property | Type | Writable |
|---|---|---|
| `bucket` | String | No |
| `generation` | String | No |
| `metageneration` | String | No |
| `fullPath` | String | No |
| `name` | String | No |
| `size` | Int64 | No |
| `timeCreated` | Date | No |
| `updated` | Date | No |
| `md5Hash` | String | Yes |
| `cacheControl` | String | Yes |
| `contentDisposition` | String | Yes |
| `contentEncoding` | String | Yes |
| `contentLanguage` | String | Yes |
| `contentType` | String | Yes |
| `customMetadata` | \[String: String\] | Yes |

> [!NOTE]
> **Note:** at present, setting the `md5Hash` property on upload doesn't affect the upload, as hash verification is not yet implemented.

Uploading, downloading, and updating files is important, but so is being able
to remove them. Let's learn how to
[delete files](https://firebase.google.com/docs/storage/ios/delete-files)
from Cloud Storage.