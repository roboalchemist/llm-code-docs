# Source: https://firebase.google.com/docs/storage/android/file-metadata.md.txt

# Use file metadata with Cloud Storage on Android

<br />

After uploading a file to Cloud Storage reference, you can also get
and update the file metadata, for example to view or update the content type.
Files can also store custom key/value pairs with additional file metadata.

> [!NOTE]
> **Note:** By default, a Cloud Storage for Firebase bucket requires Firebase Authentication to perform any action on the bucket's data or files. You can change your Firebase Security Rules for Cloud Storage to [allow unauthenticated access for specific situations](https://firebase.google.com/docs/storage/security/rules-conditions#public). However, for most situations, we strongly recommend [restricting access and setting up robust security rules](https://firebase.google.com/docs/storage/security/get-started) (especially for production apps). Note that if you use Google App Engine and have a default Cloud Storage bucket with a name format of `*.appspot.com`, you may need to consider [how your security rules impact access to App Engine files](https://firebase.google.com/docs/storage/gcp-integration#security-rules-and-app-engine-files).

## Get File Metadata

File metadata contains common properties such as `name`, `size`, and
`contentType` (often referred to as MIME type) in addition to some less
common ones like `contentDisposition` and `timeCreated`. This metadata can be
retrieved from a Cloud Storage reference using
the `getMetadata()` method.

### Kotlin

```kotlin
// Create a storage reference from our app
val storageRef = storage.reference

// Get reference to the file
val forestRef = storageRef.child("images/forest.jpg")
```

```kotlin
forestRef.metadata.addOnSuccessListener { metadata ->
    // Metadata now contains the metadata for 'images/forest.jpg'
}.addOnFailureListener {
    // Uh-oh, an error occurred!
}
```

### Java

```java
// Create a storage reference from our app
StorageReference storageRef = storage.getReference();

// Get reference to the file
StorageReference forestRef = storageRef.child("images/forest.jpg");
```

```java
forestRef.getMetadata().addOnSuccessListener(new OnSuccessListener<StorageMetadata>() {
    @Override
    public void onSuccess(StorageMetadata storageMetadata) {
        // Metadata now contains the metadata for 'images/forest.jpg'
    }
}).addOnFailureListener(new OnFailureListener() {
    @Override
    public void onFailure(@NonNull Exception exception) {
        // Uh-oh, an error occurred!
    }
});
```

## Update File Metadata

You can update file metadata at any time after the file upload completes by
using the `updateMetadata()` method. Refer to the
[full list](https://firebase.google.com/docs/storage/android/file-metadata#file-metadata-properties) for more information on what properties
can be updated. Only the properties specified in the metadata are updated,
all others are left unmodified.

### Kotlin

```kotlin
// Create a storage reference from our app
val storageRef = storage.reference

// Get reference to the file
val forestRef = storageRef.child("images/forest.jpg")
```

```kotlin
// Create file metadata including the content type
val metadata = storageMetadata {
    contentType = "image/jpg"
    setCustomMetadata("myCustomProperty", "myValue")
}

// Update metadata properties
forestRef.updateMetadata(metadata).addOnSuccessListener { updatedMetadata ->
    // Updated metadata is in updatedMetadata
}.addOnFailureListener {
    // Uh-oh, an error occurred!
}
```

### Java

```java
// Create a storage reference from our app
StorageReference storageRef = storage.getReference();

// Get reference to the file
StorageReference forestRef = storageRef.child("images/forest.jpg");
```

```java
// Create file metadata including the content type
StorageMetadata metadata = new StorageMetadata.Builder()
        .setContentType("image/jpg")
        .setCustomMetadata("myCustomProperty", "myValue")
        .build();

// Update metadata properties
forestRef.updateMetadata(metadata)
        .addOnSuccessListener(new OnSuccessListener<StorageMetadata>() {
            @Override
            public void onSuccess(StorageMetadata storageMetadata) {
                // Updated metadata is in storageMetadata
            }
        })
        .addOnFailureListener(new OnFailureListener() {
            @Override
            public void onFailure(@NonNull Exception exception) {
                // Uh-oh, an error occurred!
            }
        });
```

You can delete writable metadata properties by passing `null`:

### Kotlin

```kotlin
// Create file metadata with property to delete
val metadata = storageMetadata {
    contentType = null
}

// Delete the metadata property
forestRef.updateMetadata(metadata).addOnSuccessListener { updatedMetadata ->
    // updatedMetadata.contentType should be null
}.addOnFailureListener {
    // Uh-oh, an error occurred!
}
```

### Java

```java
// Create file metadata with property to delete
StorageMetadata metadata = new StorageMetadata.Builder()
        .setContentType(null)
        .build();

// Delete the metadata property
forestRef.updateMetadata(metadata)
        .addOnSuccessListener(new OnSuccessListener<StorageMetadata>() {
            @Override
            public void onSuccess(StorageMetadata storageMetadata) {
                // metadata.contentType should be null
            }
        })
        .addOnFailureListener(new OnFailureListener() {
            @Override
            public void onFailure(@NonNull Exception exception) {
                // Uh-oh, an error occurred!
            }
        });
```

## Handle Errors

There are a number of reasons why errors may occur on getting or updating
metadata, including the file not existing, or the user not having permission
to access the desired file. More information on errors can be found in the
[Handle Errors](https://firebase.google.com/docs/storage/android/handle-errors)
section of the docs.

## Custom Metadata

You can specify custom metadata using the `setCustomMetadata()` method in the
`StorageMetadata.Builder` class.

### Kotlin

```kotlin
val metadata = storageMetadata {
    setCustomMetadata("location", "Yosemite, CA, USA")
    setCustomMetadata("activity", "Hiking")
}
```

### Java

```java
StorageMetadata metadata = new StorageMetadata.Builder()
        .setCustomMetadata("location", "Yosemite, CA, USA")
        .setCustomMetadata("activity", "Hiking")
        .build();
```

You can store app-specific data for each file in custom metadata, but we highly
recommend using a database (such as the
[Firebase Realtime Database](https://firebase.google.com/docs/database/android/start))
to store and synchronize this type of data.

## File Metadata Properties

A full list of metadata properties on a file is available below:

| Property Getter | Type | Setter Exists |
|---|---|---|
| `getBucket` | `String` | NO |
| `getGeneration` | `String` | NO |
| `getMetadataGeneration` | `String` | NO |
| `getPath` | `String` | NO |
| `getName` | `String` | NO |
| `getSizeBytes` | `long` | NO |
| `getCreationTimeMillis` | `long` | NO |
| `getUpdatedTimeMillis` | `long` | NO |
| `getMd5Hash` | `String` | NO |
| `getCacheControl` | `String` | YES |
| `getContentDisposition` | `String` | YES |
| `getContentEncoding` | `String` | YES |
| `getContentLanguage` | `String` | YES |
| `getContentType` | `String` | YES |
| `getCustomMetadata` | `String` | YES |
| `getCustomMetadataKeys` | `Set<String>` | NO |

Uploading, downloading, and updating files is important, but so is being able
to remove them. Let's learn how to
[delete files](https://firebase.google.com/docs/storage/android/delete-files)
from Cloud Storage.