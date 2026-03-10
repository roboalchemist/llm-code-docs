# Source: https://firebase.google.com/docs/storage/web/upload-files.md.txt

# Upload files with Cloud Storage on Web

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

### Web

```javascript
import { getStorage, ref } from "firebase/storage";

// Create a root reference
const storage = getStorage();

// Create a reference to 'mountains.jpg'
const mountainsRef = ref(storage, 'mountains.jpg');

// Create a reference to 'images/mountains.jpg'
const mountainImagesRef = ref(storage, 'images/mountains.jpg');

// While the file names are the same, the references point to different files
mountainsRef.name === mountainImagesRef.name;           // true
mountainsRef.fullPath === mountainImagesRef.fullPath;   // false https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/storage-next/upload-files/storage_upload_ref.js#L8-L21
```

### Web

```javascript
// Create a root reference
var storageRef = firebase.storage().ref();

// Create a reference to 'mountains.jpg'
var mountainsRef = storageRef.child('mountains.jpg');

// Create a reference to 'images/mountains.jpg'
var mountainImagesRef = storageRef.child('images/mountains.jpg');

// While the file names are the same, the references point to different files
mountainsRef.name === mountainImagesRef.name;           // true
mountainsRef.fullPath === mountainImagesRef.fullPath;   // false https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/storage/upload-files.js#L6-L17
```

### Upload from a `Blob` or `File`

Once you've created an appropriate reference, you then call the `uploadBytes()`
method. `uploadBytes()` takes files via the JavaScript
[File](https://developer.mozilla.org/en-US/docs/Web/API/File) and
[Blob](https://developer.mozilla.org/en-US/docs/Web/API/Blob) APIs and uploads
them to Cloud Storage.

### Web

```javascript
import { getStorage, ref, uploadBytes } from "firebase/storage";

const storage = getStorage();
const storageRef = ref(storage, 'some-child');

// 'file' comes from the Blob or File API
uploadBytes(storageRef, file).then((snapshot) => {
  console.log('Uploaded a blob or file!');
});
```

### Web

```javascript
// 'file' comes from the Blob or File API
ref.put(file).then((snapshot) => {
  console.log('Uploaded a blob or file!');
});
```

### Upload from a Byte Array

In addition to the `File` and `Blob` types, `uploadBytes()` can also upload a
`Uint8Array` to Cloud Storage.

### Web

```javascript
import { getStorage, ref, uploadBytes } from "firebase/storage";

const storage = getStorage();
const storageRef = ref(storage, 'some-child');

const bytes = new Uint8Array([0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x2c, 0x20, 0x77, 0x6f, 0x72, 0x6c, 0x64, 0x21]);
uploadBytes(storageRef, bytes).then((snapshot) => {
  console.log('Uploaded an array!');
});
```

### Web

```javascript
var bytes = new Uint8Array([0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x2c, 0x20, 0x77, 0x6f, 0x72, 0x6c, 0x64, 0x21]);
ref.put(bytes).then((snapshot) => {
  console.log('Uploaded an array!');
});
```

### Upload from a String

If a `Blob`, `File`, or `Uint8Array` isn't available, you can use the
`uploadString()` method to upload a raw, `base64`, `base64url`, or `data_url`
encoded string to Cloud Storage.

### Web

```javascript
import { getStorage, ref, uploadString } from "firebase/storage";

const storage = getStorage();
const storageRef = ref(storage, 'some-child');

// Raw string is the default if no format is provided
const message = 'This is my message.';
uploadString(storageRef, message).then((snapshot) => {
  console.log('Uploaded a raw string!');
});

// Base64 formatted string
const message2 = '5b6p5Y+344GX44G+44GX44Gf77yB44GK44KB44Gn44Go44GG77yB';
uploadString(storageRef, message2, 'base64').then((snapshot) => {
  console.log('Uploaded a base64 string!');
});

// Base64url formatted string
const message3 = '5b6p5Y-344GX44G-44GX44Gf77yB44GK44KB44Gn44Go44GG77yB';
uploadString(storageRef, message3, 'base64url').then((snapshot) => {
  console.log('Uploaded a base64url string!');
});

// Data URL string
const message4 = 'data:text/plain;base64,5b6p5Y+344GX44G+44GX44Gf77yB44GK44KB44Gn44Go44GG77yB';
uploadString(storageRef, message4, 'data_url').then((snapshot) => {
  console.log('Uploaded a data_url string!');
});
```

### Web

```javascript
// Raw string is the default if no format is provided
var message = 'This is my message.';
ref.putString(message).then((snapshot) => {
  console.log('Uploaded a raw string!');
});

// Base64 formatted string
var message = '5b6p5Y+344GX44G+44GX44Gf77yB44GK44KB44Gn44Go44GG77yB';
ref.putString(message, 'base64').then((snapshot) => {
  console.log('Uploaded a base64 string!');
});

// Base64url formatted string
var message = '5b6p5Y-344GX44G-44GX44Gf77yB44GK44KB44Gn44Go44GG77yB';
ref.putString(message, 'base64url').then((snapshot) => {
  console.log('Uploaded a base64url string!');
});

// Data URL string
var message = 'data:text/plain;base64,5b6p5Y+344GX44G+44GX44Gf77yB44GK44KB44Gn44Go44GG77yB';
ref.putString(message, 'data_url').then((snapshot) => {
  console.log('Uploaded a data_url string!');
});
```

Since the reference defines the full path to the file, make sure that you are
uploading to a non-empty path.

## Add File Metadata

When uploading a file, you can also specify metadata for that file.
This metadata contains typical file metadata properties such as `name`, `size`,
and `contentType` (commonly referred to as MIME type). Cloud Storage
automatically infers the content type from the file extension where the file is
stored on disk, but if you specify a `contentType` in the metadata it will
override the auto-detected type. If no `contentType` metadata is specified and
the file doesn't have a file extension, Cloud Storage defaults to the
type `application/octet-stream`. More information on file metadata can be found
in the [Use File Metadata](https://firebase.google.com/docs/storage/web/file-metadata)
section.

### Web

```javascript
import { getStorage, ref, uploadBytes } from "firebase/storage";

const storage = getStorage();
const storageRef = ref(storage, 'images/mountains.jpg');

// Create file metadata including the content type
/** @type {any} */
const metadata = {
  contentType: 'image/jpeg',
};

// Upload the file and metadata
const uploadTask = uploadBytes(storageRef, file, metadata);
```

### Web

```javascript
// Create file metadata including the content type
var metadata = {
  contentType: 'image/jpeg',
};

// Upload the file and metadata
var uploadTask = storageRef.child('images/mountains.jpg').put(file, metadata);
```

## Manage Uploads

In addition to starting uploads, you can pause, resume, and cancel uploads using
the `pause()`, `resume()`, and `cancel()` methods. Calling `pause()` or
`resume()` will raise `pause` or `running` state changes. Calling the
`cancel()` method results in the upload failing and returning an error
indicating that the upload was canceled.

### Web

```javascript
import { getStorage, ref, uploadBytesResumable } from "firebase/storage";

const storage = getStorage();
const storageRef = ref(storage, 'images/mountains.jpg');

// Upload the file and metadata
const uploadTask = uploadBytesResumable(storageRef, file);

// Pause the upload
uploadTask.pause();

// Resume the upload
uploadTask.resume();

// Cancel the upload
uploadTask.cancel();
```

### Web

```javascript
// Upload the file and metadata
var uploadTask = storageRef.child('images/mountains.jpg').put(file);

// Pause the upload
uploadTask.pause();

// Resume the upload
uploadTask.resume();

// Cancel the upload
uploadTask.cancel();
```

## Monitor Upload Progress

While uploading, the upload task may raise progress events in
the `state_changed` observer, such as:

| Event Type | Typical Usage |
|---|---|
| `running` | This event fires when the task starts or resumes uploading, and is often used in conjunction with the `pause` event. For larger uploads this event may fire multiple times as a progress update. |
| `pause` | This event fires any time the upload is paused, and is often used in conjunction with the `running` event. |

When an event occurs, a `TaskSnapshot` object is passed back. This snapshot
is an immutable view of the task at the time the event occurred.
This object contains the following properties:

| Property | Type | Description |
|---|---|---|
| `bytesTransferred` | `Number` | The total number of bytes that have been transferred when this snapshot was taken. |
| `totalBytes` | `Number` | The total number of bytes expected to be uploaded. |
| `state` | `firebase.storage.TaskState` | Current state of the upload. |
| `metadata` | `firebaseStorage.Metadata` | Before upload completes, the metadata sent to the server. After upload completes, the metadata the server sent back. |
| `task` | `firebaseStorage.UploadTask` | The task this is a snapshot of, which can be used to \`pause\`, \`resume\`, or \`cancel\` the task. |
| `ref` | `firebaseStorage.Reference` | The reference this task came from. |

These changes in state, combined with the properties of the `TaskSnapshot`
provide a simple yet powerful way to monitor upload events.

### Web

```javascript
import { getStorage, ref, uploadBytesResumable, getDownloadURL } from "firebase/storage";

const storage = getStorage();
const storageRef = ref(storage, 'images/rivers.jpg');

const uploadTask = uploadBytesResumable(storageRef, file);

// Register three observers:
// 1. 'state_changed' observer, called any time the state changes
// 2. Error observer, called on failure
// 3. Completion observer, called on successful completion
uploadTask.on('state_changed', 
  (snapshot) => {
    // Observe state change events such as progress, pause, and resume
    // Get task progress, including the number of bytes uploaded and the total number of bytes to be uploaded
    const progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
    console.log('Upload is ' + progress + '% done');
    switch (snapshot.state) {
      case 'paused':
        console.log('Upload is paused');
        break;
      case 'running':
        console.log('Upload is running');
        break;
    }
  }, 
  (error) => {
    // Handle unsuccessful uploads
  }, 
  () => {
    // Handle successful uploads on complete
    // For instance, get the download URL: https://firebasestorage.googleapis.com/...
    getDownloadURL(uploadTask.snapshot.ref).then((downloadURL) => {
      console.log('File available at', downloadURL);
    });
  }
);
```

### Web

```javascript
var uploadTask = storageRef.child('images/rivers.jpg').put(file);

// Register three observers:
// 1. 'state_changed' observer, called any time the state changes
// 2. Error observer, called on failure
// 3. Completion observer, called on successful completion
uploadTask.on('state_changed', 
  (snapshot) => {
    // Observe state change events such as progress, pause, and resume
    // Get task progress, including the number of bytes uploaded and the total number of bytes to be uploaded
    var progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
    console.log('Upload is ' + progress + '% done');
    switch (snapshot.state) {
      case firebase.storage.TaskState.PAUSED: // or 'paused'
        console.log('Upload is paused');
        break;
      case firebase.storage.TaskState.RUNNING: // or 'running'
        console.log('Upload is running');
        break;
    }
  }, 
  (error) => {
    // Handle unsuccessful uploads
  }, 
  () => {
    // Handle successful uploads on complete
    // For instance, get the download URL: https://firebasestorage.googleapis.com/...
    uploadTask.snapshot.ref.getDownloadURL().then((downloadURL) => {
      console.log('File available at', downloadURL);
    });
  }
);
```

## Error Handling

There are a number of reasons why errors may occur on upload, including
the local file not existing, or the user not having permission to upload
the desired file. More information on errors can be found in the
[Handle Errors](https://firebase.google.com/docs/storage/web/handle-errors)
section of the docs.

## Full Example

A full example of an upload with progress monitoring and error handling
is shown below:

### Web

```javascript
import { getStorage, ref, uploadBytesResumable, getDownloadURL } from "firebase/storage";

const storage = getStorage();

// Create the file metadata
/** @type {any} */
const metadata = {
  contentType: 'image/jpeg'
};

// Upload file and metadata to the object 'images/mountains.jpg'
const storageRef = ref(storage, 'images/' + file.name);
const uploadTask = uploadBytesResumable(storageRef, file, metadata);

// Listen for state changes, errors, and completion of the upload.
uploadTask.on('state_changed',
  (snapshot) => {
    // Get task progress, including the number of bytes uploaded and the total number of bytes to be uploaded
    const progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
    console.log('Upload is ' + progress + '% done');
    switch (snapshot.state) {
      case 'paused':
        console.log('Upload is paused');
        break;
      case 'running':
        console.log('Upload is running');
        break;
    }
  }, 
  (error) => {
    // A full list of error codes is available at
    // https://firebase.google.com/docs/storage/web/handle-errors
    switch (error.code) {
      case 'storage/unauthorized':
        // User doesn't have permission to access the object
        break;
      case 'storage/canceled':
        // User canceled the upload
        break;

      // ...

      case 'storage/unknown':
        // Unknown error occurred, inspect error.serverResponse
        break;
    }
  }, 
  () => {
    // Upload completed successfully, now we can get the download URL
    getDownloadURL(uploadTask.snapshot.ref).then((downloadURL) => {
      console.log('File available at', downloadURL);
    });
  }
);
```

### Web

```javascript
// Create the file metadata
var metadata = {
  contentType: 'image/jpeg'
};

// Upload file and metadata to the object 'images/mountains.jpg'
var uploadTask = storageRef.child('images/' + file.name).put(file, metadata);

// Listen for state changes, errors, and completion of the upload.
uploadTask.on(firebase.storage.TaskEvent.STATE_CHANGED, // or 'state_changed'
  (snapshot) => {
    // Get task progress, including the number of bytes uploaded and the total number of bytes to be uploaded
    var progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
    console.log('Upload is ' + progress + '% done');
    switch (snapshot.state) {
      case firebase.storage.TaskState.PAUSED: // or 'paused'
        console.log('Upload is paused');
        break;
      case firebase.storage.TaskState.RUNNING: // or 'running'
        console.log('Upload is running');
        break;
    }
  }, 
  (error) => {
    // A full list of error codes is available at
    // https://firebase.google.com/docs/storage/web/handle-errors
    switch (error.code) {
      case 'storage/unauthorized':
        // User doesn't have permission to access the object
        break;
      case 'storage/canceled':
        // User canceled the upload
        break;

      // ...

      case 'storage/unknown':
        // Unknown error occurred, inspect error.serverResponse
        break;
    }
  }, 
  () => {
    // Upload completed successfully, now we can get the download URL
    uploadTask.snapshot.ref.getDownloadURL().then((downloadURL) => {
      console.log('File available at', downloadURL);
    });
  }
);
```

Now that you've uploaded files, let's learn how to
[download them](https://firebase.google.com/docs/storage/web/download-files)
from Cloud Storage.