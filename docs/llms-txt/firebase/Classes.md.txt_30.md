# Source: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes.md.txt

# FirebaseStorage Framework Reference

# Classes

The following classes are available globally.
- `


  ### [StorageReference](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference)


  ` `StorageReference` represents a reference to a Google Cloud Storage object. Developers can
  upload and download objects, as well as get/set object metadata, and delete an object at the
  path. See the [Cloud docs](https://cloud.google.com/storage/) for more details.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRStorageReference)
      open class StorageReference : NSObject

- `


  ### [Storage](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage)


  ` Firebase Storage is a service that supports uploading and downloading binary objects,
  such as images, videos, and other files to Google Cloud Storage. Instances of `Storage`
  are not thread-safe, but can be accessed from any thread.

  If you call `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(cm)storage`, the instance will initialize with the default `FirebaseApp`,
  `FirebaseApp.app()`, and the storage location will come from the provided
  `GoogleService-Info.plist`.

  If you provide a custom instance of `FirebaseApp`,
  the storage location will be specified via the `FirebaseOptions.storageBucket` property.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRStorage)
      open class Storage : NSObject

- `


  ### [StorageDownloadTask](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageDownloadTask)


  ` `StorageDownloadTask` implements resumable downloads from an object in Firebase Storage.

  Downloads can be returned on completion with a completion handler, and can be monitored
  by attaching observers, or controlled by calling `pause()`, `resume()`,
  or `cancel()`.

  Downloads can currently be returned as `Data` in memory, or as a `URL` to a file on disk.

  Downloads are performed on a background queue, and callbacks are raised on the developer
  specified `callbackQueue` in Storage, or the main queue if left unspecified.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRStorageDownloadTask)
      open class StorageDownloadTask : https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageObservableTask, https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Protocols/StorageTaskManagement

- `


  ### [StorageListResult](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageListResult)


  ` Contains the prefixes and items returned by a `StorageReference.list()` call.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRStorageListResult)
      open class StorageListResult : NSObject

- `


  ### [StorageMetadata](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata)


  ` Class which represents the metadata on an object in Firebase Storage.

  This metadata is
  returned on successful operations, and can be used to retrieve download URLs, content types,
  and a Storage reference to the object in question. Full documentation can be found in the
  [GCS documentation](https://cloud.google.com/storage/docs/json_api/v1/objects#resource)

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRStorageMetadata)
      open class StorageMetadata : NSObject

- `


  ### [StorageObservableTask](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageObservableTask)


  ` An extended `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageTask` providing observable semantics that can be used for responding to changes
  in task state.

  Observers produce a `StorageHandle`, which is used to keep track of and remove specific
  observers at a later date.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRStorageObservableTask)
      open class StorageObservableTask : https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageTask

- `


  ### [StorageTask](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageTask)


  ` A superclass to all Storage tasks, including `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageUploadTask`
  and `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageDownloadTask`, to provide state transitions, event raising, and common storage
  for metadata and errors.

  Callbacks are always fired on the developer-specified callback queue.
  If no queue is specified, it defaults to the main queue.
  This class is thread-safe.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRStorageTask)
      open class StorageTask : NSObject

- `


  ### [StorageTaskSnapshot](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageTaskSnapshot)


  ` `StorageTaskSnapshot` represents an immutable view of a task.
  A snapshot contains a task, storage reference, metadata (if it exists),
  progress, and an error (if one occurred).

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRStorageTaskSnapshot)
      open class StorageTaskSnapshot : NSObject

- `


  ### [StorageUploadTask](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageUploadTask)


  ` `StorageUploadTask` implements resumable uploads to a file in Firebase Storage.

  Uploads can be returned on completion with a completion callback, and can be monitored
  by attaching observers, or controlled by calling `pause()`, `resume()`,
  or `cancel()`.

  Uploads can be initialized from `Data` in memory, or a URL to a file on disk.

  Uploads are performed on a background queue, and callbacks are raised on the developer
  specified `callbackQueue` in Storage, or the main queue if unspecified.

  #### Declaration

  Swift

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc(FIRStorageUploadTask)
      open class StorageUploadTask: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageObservableTask,
        https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Protocols/StorageTaskManagement