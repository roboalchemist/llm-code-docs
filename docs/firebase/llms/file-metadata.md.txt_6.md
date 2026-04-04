# Source: https://firebase.google.com/docs/storage/web/file-metadata.md.txt

# Use file metadata with Cloud Storage on Web

<br />

After uploading a file to Cloud Storage reference, you can also get
or update the file metadata, for example to update the content type. Files
can also store custom key/value pairs with additional file metadata.

> [!NOTE]
> **Note:** By default, a Cloud Storage for Firebase bucket requires Firebase Authentication to perform any action on the bucket's data or files. You can change your Firebase Security Rules for Cloud Storage to [allow unauthenticated access for specific situations](https://firebase.google.com/docs/storage/security/rules-conditions#public). However, for most situations, we strongly recommend [restricting access and setting up robust security rules](https://firebase.google.com/docs/storage/security/get-started) (especially for production apps). Note that if you use Google App Engine and have a default Cloud Storage bucket with a name format of `*.appspot.com`, you may need to consider [how your security rules impact access to App Engine files](https://firebase.google.com/docs/storage/gcp-integration#security-rules-and-app-engine-files).

## Get File Metadata

File metadata contains common properties such as `name`, `size`, and
`contentType` (often referred to as MIME type) in addition to some less
common ones like `contentDisposition` and `timeCreated`. This metadata can be
retrieved from a Cloud Storage reference using
the `getMetadata()` method. `getMetadata()` returns a `Promise` containing the
complete metadata, or an error if the `Promise` rejects.

### Web

```javascript
import { getStorage, ref, getMetadata } from "firebase/storage";

// Create a reference to the file whose metadata we want to retrieve
const storage = getStorage();
const forestRef = ref(storage, 'images/forest.jpg');

// Get metadata properties
getMetadata(forestRef)
  .then((metadata) => {
    // Metadata now contains the metadata for 'images/forest.jpg'
  })
  .catch((error) => {
    // Uh-oh, an error occurred!
  });
```

### Web

```javascript
// Create a reference to the file whose metadata we want to retrieve
var forestRef = storageRef.child('images/forest.jpg');

// Get metadata properties
forestRef.getMetadata()
  .then((metadata) => {
    // Metadata now contains the metadata for 'images/forest.jpg'
  })
  .catch((error) => {
    // Uh-oh, an error occurred!
  });
```

## Update File Metadata

You can update file metadata at any time after the file upload completes by
using the `updateMetadata()` method. Refer to the
[full list](https://firebase.google.com/docs/storage/web/file-metadata#file_metadata_properties) for more information on what properties
can be updated. Only the properties specified in the metadata are updated,
all others are left unmodified. `updateMetadata()` returns a `Promise`
containing the complete metadata, or an error if the `Promise` rejects.

### Web

```javascript
import { getStorage, ref, updateMetadata } from "firebase/storage";

// Create a reference to the file whose metadata we want to change
const storage = getStorage();
const forestRef = ref(storage, 'images/forest.jpg');

// Create file metadata to update
const newMetadata = {
  cacheControl: 'public,max-age=300',
  contentType: 'image/jpeg'
};

// Update metadata properties
updateMetadata(forestRef, newMetadata)
  .then((metadata) => {
    // Updated metadata for 'images/forest.jpg' is returned in the Promise
  }).catch((error) => {
    // Uh-oh, an error occurred!
  });
```

### Web

```javascript
// Create a reference to the file whose metadata we want to change
var forestRef = storageRef.child('images/forest.jpg');

// Create file metadata to update
var newMetadata = {
  cacheControl: 'public,max-age=300',
  contentType: 'image/jpeg'
};

// Update metadata properties
forestRef.updateMetadata(newMetadata)
  .then((metadata) => {
    // Updated metadata for 'images/forest.jpg' is returned in the Promise
  }).catch((error) => {
    // Uh-oh, an error occurred!
  });
```

You can delete a metadata property by setting it to `null`:

### Web

```javascript
import { getStorage, ref, updateMetadata } from "firebase/storage";

const storage = getStorage();
const forestRef = ref(storage, 'images/forest.jpg');

// Create file metadata with property to delete
const deleteMetadata = {
  contentType: null
};

// Delete the metadata property
updateMetadata(forestRef, deleteMetadata)
  .then((metadata) => {
    // metadata.contentType should be null
  }).catch((error) => {
    // Uh-oh, an error occurred!
  });
```

### Web

```javascript
// Create file metadata with property to delete
var deleteMetadata = {
  contentType: null
};

// Delete the metadata property
forestRef.updateMetadata(deleteMetadata)
  .then((metadata) => {
    // metadata.contentType should be null
  }).catch((error) => {
    // Uh-oh, an error occurred!
  });
```

## Handle Errors

There are a number of reasons why errors may occur on getting or updating
metadata, including the file not existing, or the user not having permission
to access the desired file. More information on errors can be found in the
[Handle Errors](https://firebase.google.com/docs/storage/web/handle-errors)
section of the docs.

## Custom Metadata

You can specify custom metadata as an object containing `String` properties.

### Web

```javascript
const metadata = {
  customMetadata: {
    'location': 'Yosemite, CA, USA',
    'activity': 'Hiking'
  }
};
```

### Web

```javascript
var metadata = {
  customMetadata: {
    'location': 'Yosemite, CA, USA',
    'activity': 'Hiking'
  }
};
```

You can use custom metadata for storing additional app specific data for each
file, but we highly recommend using a database (such as the
[Firebase Realtime Database](https://firebase.google.com/docs/database))
to store and synchronize this type of data.

## File Metadata Properties

A full list of metadata properties on a file is available below:

| Property | Type | Writable |
|---|---|---|
| `bucket` | string | NO |
| `generation` | string | NO |
| `metageneration` | string | NO |
| `fullPath` | string | NO |
| `name` | string | NO |
| `size` | number | NO |
| `timeCreated` | string | NO |
| `updated` | string | NO |
| `md5Hash` | string | YES on upload, NO on updateMetadata |
| `cacheControl` | string | YES |
| `contentDisposition` | string | YES |
| `contentEncoding` | string | YES |
| `contentLanguage` | string | YES |
| `contentType` | string | YES |
| `customMetadata` | Object containing string-\>string mappings | YES |

> [!NOTE]
> **Note:** at present, setting the `md5Hash` property on upload doesn't affect the upload, as hash verification is not yet implemented.

Uploading, downloading, and updating files is important, but so is being able
to remove them. Let's learn how to
[delete files](https://firebase.google.com/docs/storage/web/delete-files)
from Cloud Storage.