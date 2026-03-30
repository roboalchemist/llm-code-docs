# Source: https://firebase.google.com/docs/storage/web/download-files.md.txt

# Download files with Cloud Storage on Web

<br />

Cloud Storage for Firebase allows you to quickly and easily download
files from a [Cloud Storage](https://cloud.google.com/storage)
bucket provided and managed by Firebase.

> [!NOTE]
> **Note:** By default, a Cloud Storage for Firebase bucket requires Firebase Authentication to perform any action on the bucket's data or files. You can change your Firebase Security Rules for Cloud Storage to [allow unauthenticated access for specific situations](https://firebase.google.com/docs/storage/security/rules-conditions#public). However, for most situations, we strongly recommend [restricting access and setting up robust security rules](https://firebase.google.com/docs/storage/security/get-started) (especially for production apps). Note that if you use Google App Engine and have a default Cloud Storage bucket with a name format of `*.appspot.com`, you may need to consider [how your security rules impact access to App Engine files](https://firebase.google.com/docs/storage/gcp-integration#security-rules-and-app-engine-files).

## Create a Reference

To download a file, first
[create a Cloud Storage reference](https://firebase.google.com/docs/storage/web/create-reference)
to the file you want to download.

You can create a reference by appending child paths to the root of your
Cloud Storage bucket, or you can create a reference from an existing
`gs://` or `https://` URL referencing an object in Cloud Storage.

### Web

```javascript
import { getStorage, ref } from "firebase/storage";

// Create a reference with an initial file path and name
const storage = getStorage();
const pathReference = ref(storage, 'images/stars.jpg');

// Create a reference from a Google Cloud Storage URI
const gsReference = ref(storage, 'gs://bucket/images/stars.jpg');

// Create a reference from an HTTPS URL
// Note that in the URL, characters are URL escaped!
const httpsReference = ref(storage, 'https://firebasestorage.googleapis.com/b/bucket/o/images%20stars.jpg');  
```

### Web

```javascript
// Create a reference with an initial file path and name
var storage = firebase.storage();
var pathReference = storage.ref('images/stars.jpg');

// Create a reference from a Google Cloud Storage URI
var gsReference = storage.refFromURL('gs://bucket/images/stars.jpg');

// Create a reference from an HTTPS URL
// Note that in the URL, characters are URL escaped!
var httpsReference = storage.refFromURL('https://firebasestorage.googleapis.com/b/bucket/o/images%20stars.jpg');  
```

## Download Data via URL

You can get the download URL for a file by calling the
`getDownloadURL()` method on a Cloud Storage reference.

### Web

```javascript
import { getStorage, ref, getDownloadURL } from "firebase/storage";

const storage = getStorage();
getDownloadURL(ref(storage, 'images/stars.jpg'))
  .then((url) => {
    // `url` is the download URL for 'images/stars.jpg'

    // This can be downloaded directly:
    const xhr = new XMLHttpRequest();
    xhr.responseType = 'blob';
    xhr.onload = (event) => {
      const blob = xhr.response;
    };
    xhr.open('GET', url);
    xhr.send();

    // Or inserted into an <img> element
    const img = document.getElementById('myimg');
    img.setAttribute('src', url);
  })
  .catch((error) => {
    // Handle any errors
  });
```

### Web

```javascript
storageRef.child('images/stars.jpg').getDownloadURL()
  .then((url) => {
    // `url` is the download URL for 'images/stars.jpg'

    // This can be downloaded directly:
    var xhr = new XMLHttpRequest();
    xhr.responseType = 'blob';
    xhr.onload = (event) => {
      var blob = xhr.response;
    };
    xhr.open('GET', url);
    xhr.send();

    // Or inserted into an <img> element
    var img = document.getElementById('myimg');
    img.setAttribute('src', url);
  })
  .catch((error) => {
    // Handle any errors
  });
```

## Download Data Directly from the SDK

From version 9.5 and higher, the SDK provides these functions for direct
download:

- [`getBlob()`](https://firebase.google.com/docs/reference/js/storage#getblob)
- [`getBytes()`](https://firebase.google.com/docs/reference/js/storage#getbytes)
- [`getStream()`](https://firebase.google.com/docs/reference/js/storage#getstream)

Using these functions, you can bypass downloading from a URL, and instead
return data in your code. This allows for finer-grained access control via
[Firebase Security Rules](https://firebase.google.com/docs/storage/security).

> [!NOTE]
> **Note:** `getStream()` is available only for Node.js, and `getBlob()` is available only for browser-like environments.

### CORS Configuration

To download data directly in the browser, you must configure your
Cloud Storage bucket for cross-origin access (CORS). This can be done
with the `gsutil` command line tool, which you can
[install from here](https://cloud.google.com/storage/docs/gsutil_install).

If you don't want any domain-based restrictions (the most common scenario),
copy this JSON to a file named `cors.json`:

```
[
  {
    "origin": ["*"],
    "method": ["GET"],
    "maxAgeSeconds": 3600
  }
]
```

<br />

Run `gsutil cors set cors.json gs://<your-cloud-storage-bucket>` to deploy
these restrictions.

For more information, refer to the
[Google Cloud Storage documentation](https://cloud.google.com/storage/docs/cross-origin).

## Handle Errors

There are a number of reasons why errors may occur on download, including the
file not existing, or the user not having permission to access the desired file.
More information on errors can be found in the
[Handle Errors](https://firebase.google.com/docs/storage/web/handle-errors)
section of the docs.

## Full Example

A full example of a download with error handling is shown below:

### Web

```javascript
import { getStorage, ref, getDownloadURL } from "firebase/storage";

// Create a reference to the file we want to download
const storage = getStorage();
const starsRef = ref(storage, 'images/stars.jpg');

// Get the download URL
getDownloadURL(starsRef)
  .then((url) => {
    // Insert url into an <img> tag to "download"
  })
  .catch((error) => {
    // A full list of error codes is available at
    // https://firebase.google.com/docs/storage/web/handle-errors
    switch (error.code) {
      case 'storage/object-not-found':
        // File doesn't exist
        break;
      case 'storage/unauthorized':
        // User doesn't have permission to access the object
        break;
      case 'storage/canceled':
        // User canceled the upload
        break;

      // ...

      case 'storage/unknown':
        // Unknown error occurred, inspect the server response
        break;
    }
  });
```

### Web

```javascript
// Create a reference to the file we want to download
var starsRef = storageRef.child('images/stars.jpg');

// Get the download URL
starsRef.getDownloadURL()
.then((url) => {
  // Insert url into an <img> tag to "download"
})
.catch((error) => {
  // A full list of error codes is available at
  // https://firebase.google.com/docs/storage/web/handle-errors
  switch (error.code) {
    case 'storage/object-not-found':
      // File doesn't exist
      break;
    case 'storage/unauthorized':
      // User doesn't have permission to access the object
      break;
    case 'storage/canceled':
      // User canceled the upload
      break;

    // ...

    case 'storage/unknown':
      // Unknown error occurred, inspect the server response
      break;
  }
});
```

You can also [get or update metadata](https://firebase.google.com/docs/storage/web/file-metadata)
for files that are stored in Cloud Storage.