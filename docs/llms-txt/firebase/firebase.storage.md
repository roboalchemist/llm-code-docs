# Source: https://firebase.google.com/docs/reference/node/firebase.storage.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.storage.md.txt

# storage | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- storage

### Callable

- storage ( app ? : [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App) ) : [Storage](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Storage)
- Gets the [`Storage`](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Storage) service for the default
  app or a given app.

  `firebase.storage()` can be called with no arguments to access the default
  app's [`Storage`](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Storage) service or as
  `firebase.storage(app)` to access the
  [`Storage`](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Storage) service associated with a
  specific app.

  example
  :

          // Get the Storage service for the default app
          var defaultStorage = firebase.storage();


  example
  :

          // Get the Storage service for a given app
          var otherStorage = firebase.storage(otherApp);


  #### Parameters

  -

    ##### Optional app: [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App)

    The app to create a storage service for.
    If not passed, uses the default app.

  #### Returns [Storage](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Storage)

## Index

### Enumerations

- [StorageErrorCode](https://firebase.google.com/docs/reference/js/v8/firebase.storage.StorageErrorCode)

### Interfaces

- [FirebaseStorageError](https://firebase.google.com/docs/reference/js/v8/firebase.storage.FirebaseStorageError)
- [FullMetadata](https://firebase.google.com/docs/reference/js/v8/firebase.storage.FullMetadata)
- [ListOptions](https://firebase.google.com/docs/reference/js/v8/firebase.storage.ListOptions)
- [ListResult](https://firebase.google.com/docs/reference/js/v8/firebase.storage.ListResult)
- [Reference](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Reference)
- [SettableMetadata](https://firebase.google.com/docs/reference/js/v8/firebase.storage.SettableMetadata)
- [Storage](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Storage)
- [StorageObserver](https://firebase.google.com/docs/reference/js/v8/firebase.storage.StorageObserver)
- [UploadMetadata](https://firebase.google.com/docs/reference/js/v8/firebase.storage.UploadMetadata)
- [UploadTask](https://firebase.google.com/docs/reference/js/v8/firebase.storage.UploadTask)
- [UploadTaskSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.storage.UploadTaskSnapshot)

### Type aliases

- [StringFormat](https://firebase.google.com/docs/reference/js/v8/firebase.storage#stringformat)
- [TaskEvent](https://firebase.google.com/docs/reference/js/v8/firebase.storage#taskevent)
- [TaskState](https://firebase.google.com/docs/reference/js/v8/firebase.storage#taskstate)

### Variables

- [StringFormat](https://firebase.google.com/docs/reference/js/v8/firebase.storage#stringformat-1)
- [TaskEvent](https://firebase.google.com/docs/reference/js/v8/firebase.storage#taskevent-1)
- [TaskState](https://firebase.google.com/docs/reference/js/v8/firebase.storage#taskstate-1)

## Type aliases

### StringFormat

StringFormat: string  

### TaskEvent

TaskEvent: string  
An event that is triggered on a task.

see

:   [firebase.storage.UploadTask.on](https://firebase.google.com/docs/reference/js/v8/firebase.storage.UploadTask#on)

### TaskState

TaskState: string  
Represents the current state of a running upload.

## Variables

### StringFormat

StringFormat: { BASE64: [StringFormat](https://firebase.google.com/docs/reference/js/v8/firebase.storage#stringformat); BASE64URL: [StringFormat](https://firebase.google.com/docs/reference/js/v8/firebase.storage#stringformat); DATA_URL: [StringFormat](https://firebase.google.com/docs/reference/js/v8/firebase.storage#stringformat); RAW: [StringFormat](https://firebase.google.com/docs/reference/js/v8/firebase.storage#stringformat) }  

#### Type declaration

-

  ##### BASE64: [StringFormat](https://firebase.google.com/docs/reference/js/v8/firebase.storage#stringformat)

  Indicates the string should be interpreted as base64-encoded data.
  Padding characters (trailing '='s) are optional.
  Example: The string 'rWmO++E6t7/rlw==' becomes the byte sequence
  ad 69 8e fb e1 3a b7 bf eb 97
-

  ##### BASE64URL: [StringFormat](https://firebase.google.com/docs/reference/js/v8/firebase.storage#stringformat)

  Indicates the string should be interpreted as base64url-encoded data.
  Padding characters (trailing '='s) are optional.
  Example: The string 'rWmO--E6t7_rlw==' becomes the byte sequence
  ad 69 8e fb e1 3a b7 bf eb 97
-

  ##### DATA_URL: [StringFormat](https://firebase.google.com/docs/reference/js/v8/firebase.storage#stringformat)

  Indicates the string is a data URL, such as one obtained from
  canvas.toDataURL().
  Example: the string 'data:application/octet-stream;base64,aaaa'
  becomes the byte sequence
  69 a6 9a
  (the content-type "application/octet-stream" is also applied, but can
  be overridden in the metadata object).
-

  ##### RAW: [StringFormat](https://firebase.google.com/docs/reference/js/v8/firebase.storage#stringformat)

  Indicates the string should be interpreted "raw", that is, as normal text.
  The string will be interpreted as UTF-16, then uploaded as a UTF-8 byte
  sequence.
  Example: The string 'Hello! \\ud83d\\ude0a' becomes the byte sequence
  48 65 6c 6c 6f 21 20 f0 9f 98 8a

### TaskEvent

TaskEvent: { STATE_CHANGED: [TaskEvent](https://firebase.google.com/docs/reference/js/v8/firebase.storage#taskevent) }  

#### Type declaration

-

  ##### STATE_CHANGED: [TaskEvent](https://firebase.google.com/docs/reference/js/v8/firebase.storage#taskevent)

  For this event,
  - The \`next\` function is triggered on progress updates and when the task is paused/resumed with a [firebase.storage.UploadTaskSnapshot](https://firebase.google.com/docs/reference/js/v8/firebase.storage.UploadTaskSnapshot) as the first argument.
  - The \`error\` function is triggered if the upload is canceled or fails for another reason.
  - The \`complete\` function is triggered if the upload completes successfully.

### TaskState

TaskState: { CANCELED: [TaskState](https://firebase.google.com/docs/reference/js/v8/firebase.storage#taskstate); ERROR: [TaskState](https://firebase.google.com/docs/reference/js/v8/firebase.storage#taskstate); PAUSED: [TaskState](https://firebase.google.com/docs/reference/js/v8/firebase.storage#taskstate); RUNNING: [TaskState](https://firebase.google.com/docs/reference/js/v8/firebase.storage#taskstate); SUCCESS: [TaskState](https://firebase.google.com/docs/reference/js/v8/firebase.storage#taskstate) }  

#### Type declaration

-

  ##### CANCELED: [TaskState](https://firebase.google.com/docs/reference/js/v8/firebase.storage#taskstate)

-

  ##### ERROR: [TaskState](https://firebase.google.com/docs/reference/js/v8/firebase.storage#taskstate)

-

  ##### PAUSED: [TaskState](https://firebase.google.com/docs/reference/js/v8/firebase.storage#taskstate)

-

  ##### RUNNING: [TaskState](https://firebase.google.com/docs/reference/js/v8/firebase.storage#taskstate)

-

  ##### SUCCESS: [TaskState](https://firebase.google.com/docs/reference/js/v8/firebase.storage#taskstate)