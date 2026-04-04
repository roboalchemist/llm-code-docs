# Source: https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes.md.txt

# FirebaseStorage Framework Reference

# Classes

The following classes are available globally.
- `


  ### [FIRStorage](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorage)


  ` Firebase Storage is a service that supports uploading and downloading binary objects,
  such as images, videos, and other files to Google Cloud Storage. Instances of `Storage`
  are not thread-safe, but can be accessed from any thread.
  If you call `Storage.storage()`, the instance will initialize with the default `FirebaseApp`,
  `FirebaseApp.app()`, and the storage location will come from the provided
  `GoogleService-Info.plist`.
  If you provide a custom instance of `FirebaseApp`,
  the storage location will be specified via the `FirebaseOptions.storageBucket` property.

  #### Declaration

  Objective-C


      @interface FIRStorage : NSObject

- `


  ### [FIRStorageTask](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageTask)


  ` A superclass to all Storage tasks, including `StorageUploadTask`
  and `StorageDownloadTask`, to provide state transitions, event raising, and common storage
  for metadata and errors.
  Callbacks are always fired on the developer-specified callback queue.
  If no queue is specified, it defaults to the main queue.
  This class is thread-safe.

  #### Declaration

  Objective-C


      @interface FIRStorageTask : NSObject

- `


  ### [FIRStorageObservableTask](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageObservableTask)


  ` An extended `StorageTask` providing observable semantics that can be used for responding to changes
  in task state.
  Observers produce a `StorageHandle`, which is used to keep track of and remove specific
  observers at a later date.

  #### Declaration

  Objective-C


      @interface FIRStorageObservableTask : https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageTask

- `


  ### [FIRStorageDownloadTask](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageDownloadTask)


  ` `StorageDownloadTask` implements resumable downloads from an object in Firebase Storage.
  Downloads can be returned on completion with a completion handler, and can be monitored
  by attaching observers, or controlled by calling `pause()`, `resume()`,
  or `cancel()`.
  Downloads can currently be returned as `Data` in memory, or as a `URL` to a file on disk.
  Downloads are performed on a background queue, and callbacks are raised on the developer
  specified `callbackQueue` in Storage, or the main queue if left unspecified.

  #### Declaration

  Objective-C


      @interface FIRStorageDownloadTask
          : https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageObservableTask <https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Protocols/FIRStorageTaskManagement>

- `


  ### [FIRStorageListResult](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageListResult)


  ` Contains the prefixes and items returned by a `StorageReference.list()` call.

  #### Declaration

  Objective-C


      @interface FIRStorageListResult : NSObject

- `


  ### [FIRStorageMetadata](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata)


  ` Class which represents the metadata on an object in Firebase Storage. This metadata is
  returned on successful operations, and can be used to retrieve download URLs, content types,
  and a Storage reference to the object in question. Full documentation can be found at the GCS
  Objects#resource docs.
  See
  <https://cloud.google.com/storage/docs/json_api/v1/objects#resource>

  #### Declaration

  Objective-C


      @interface FIRStorageMetadata : NSObject

- `


  ### [FIRStorageReference](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference)


  ` `StorageReference` represents a reference to a Google Cloud Storage object. Developers can
  upload and download objects, as well as get/set object metadata, and delete an object at the
  path. See the Cloud docs for more details: <https://cloud.google.com/storage/>

  #### Declaration

  Objective-C


      @interface FIRStorageReference : NSObject

- `


  ### [FIRStorageTaskSnapshot](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageTaskSnapshot)


  ` `StorageTaskSnapshot` represents an immutable view of a task.
  A snapshot contains a task, storage reference, metadata (if it exists),
  progress, and an error (if one occurred).

  #### Declaration

  Objective-C


      @interface FIRStorageTaskSnapshot : NSObject

- `


  ### [FIRStorageUploadTask](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageUploadTask)


  ` `StorageUploadTask` implements resumable uploads to a file in Firebase Storage.
  Uploads can be returned on completion with a completion callback, and can be monitored
  by attaching observers, or controlled by calling `pause()`, `resume()`,
  or `cancel()`.
  Uploads can be initialized from `Data` in memory, or a URL to a file on disk.
  Uploads are performed on a background queue, and callbacks are raised on the developer
  specified `callbackQueue` in Storage, or the main queue if unspecified.
  Currently all uploads must be initiated and managed on the main queue.

  #### Declaration

  Objective-C


      @interface FIRStorageUploadTask
          : https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageObservableTask <https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Protocols/FIRStorageTaskManagement>