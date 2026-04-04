# Source: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference.md.txt

# FirebaseStorage Framework Reference

# StorageReference

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRStorageReference)
    open class StorageReference : NSObject

`StorageReference` represents a reference to a Google Cloud Storage object. Developers can
upload and download objects, as well as get/set object metadata, and delete an object at the
path. See the [Cloud docs](https://cloud.google.com/storage/) for more details.
[## Public APIs](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/Public-APIs)

- `


  ### [storage](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(py)storage)


  ` The `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage.html` service object which created this reference.

  #### Declaration

  Swift

      @objc
      public let storage: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage.html

- `


  ### [bucket](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(py)bucket)


  ` The name of the Google Cloud Storage bucket associated with this reference.
  For example, in `gs://bucket/path/to/object.txt`, the bucket would be 'bucket'.

  #### Declaration

  Swift

      @objc
      public var bucket: String { get }

- `


  ### [fullPath](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(py)fullPath)


  ` The full path to this object, not including the Google Cloud Storage bucket.
  In `gs://bucket/path/to/object.txt`, the full path would be: `path/to/object.txt`.

  #### Declaration

  Swift

      @objc
      public var fullPath: String { get }

- `


  ### [name](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(py)name)


  ` The short name of the object associated with this reference.

  In `gs://bucket/path/to/object.txt`, the name of the object would be `object.txt`.

  #### Declaration

  Swift

      @objc
      public var name: String { get }

- `


  ### [root()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)root)


  ` Creates a new `StorageReference` pointing to the root object.

  #### Declaration

  Swift

      @objc
      open func root() -> StorageReference

  #### Return Value

  A new `StorageReference` pointing to the root object.
- `


  ### [parent()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)parent)


  ` Creates a new `StorageReference` pointing to the parent of the current reference
  or `nil` if this instance references the root location.

      For example:
          path = foo/bar/baz   parent = foo/bar
          path = foo           parent = (root)
          path = (root)        parent = nil

  #### Declaration

  Swift

      @objc
      open func parent() -> StorageReference?

  #### Return Value

  A new `StorageReference` pointing to the parent of the current reference.
- `


  ### [child(_:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)child:)


  ` Creates a new `StorageReference` pointing to a child object of the current reference.

          path = foo      child = bar    newPath = foo/bar
          path = foo/bar  child = baz    ntask.impl.snapshotwPath = foo/bar/baz
      All leading and trailing slashes will be removed, and consecutive slashes will be
      compressed to single slashes. For example:
          child = /foo/bar     newPath = foo/bar
          child = foo/bar/     newPath = foo/bar
          child = foo///bar    newPath = foo/bar

  #### Declaration

  Swift

      @objc(child:)
      open func child(_ path: String) -> StorageReference

  #### Parameters

  |---|---|
  | ` path ` | The path to append to the current path. |

  #### Return Value

  A new `StorageReference` pointing to a child location of the current reference.
[## Uploads](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/Uploads)

- `


  ### [putData(_:metadata:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)putData:metadata:)


  ` Asynchronously uploads data to the currently specified `StorageReference`,
  without additional metadata.
  This is not recommended for large files, and one should instead upload a file from disk.

  #### Declaration

  Swift

      @discardableResult
      @objc(putData:metadata:)
      open func putData(_ uploadData: Data, metadata: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html? = nil) -> https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageUploadTask.html

  #### Parameters

  |---|---|
  | ` uploadData ` | The data to upload. |
  | ` metadata ` | `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html` containing additional information (MIME type, etc.) about the object being uploaded. |

  #### Return Value

  An instance of `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageUploadTask.html`, which can be used to monitor or manage the
  upload.
- `


  ### [__putData(_:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)putData:)


  ` Asynchronously uploads data to the currently specified `StorageReference`.
  This is not recommended for large files, and one should instead upload a file from disk.

  #### Declaration

  Swift

      @discardableResult
      @objc(putData:)
      open func __putData(_ uploadData: Data) -> https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageUploadTask.html

  #### Return Value

  An instance of `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageUploadTask.html`, which can be used to monitor or manage the
  upload.
- `


  ### [putData(_:metadata:completion:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)putData:metadata:completion:)


  ` Asynchronously uploads data to the currently specified `StorageReference`.
  This is not recommended for large files, and one should instead upload a file from disk.

  #### Declaration

  Swift

      @discardableResult
      @objc(putData:metadata:completion:)
      open func putData(_ uploadData: Data,
                        metadata: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html? = nil,
                        completion: ((_: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html?, _: Error?) -> Void)?) -> https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageUploadTask.html

  #### Parameters

  |---|---|
  | ` uploadData ` | The data to upload. |
  | ` metadata ` | `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html` containing additional information (MIME type, etc.) about the object being uploaded. |
  | ` completion ` | A closure that either returns the object metadata on success, or an error on failure. |

  #### Return Value

  An instance of `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageUploadTask.html`, which can be used to monitor or manage the
  upload.
- `


  ### [putFile(from:metadata:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)putFile:metadata:)


  ` Asynchronously uploads a file to the currently specified `StorageReference`.

  #### Declaration

  Swift

      @discardableResult
      @objc(putFile:metadata:)
      open func putFile(from fileURL: URL, metadata: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html? = nil) -> https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageUploadTask.html

  #### Parameters

  |---|---|
  | ` fileURL ` | A URL representing the system file path of the object to be uploaded. |
  | ` metadata ` | `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html` containing additional information (MIME type, etc.) about the object being uploaded. |

  #### Return Value

  An instance of `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageUploadTask.html`, which can be used to monitor or manage the
  upload.
- `


  ### [__putFile(from:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)putFile:)


  ` Asynchronously uploads a file to the currently specified `StorageReference`,
  without additional metadata.
  @param fileURL A URL representing the system file path of the object to be uploaded.
  @return An instance of StorageUploadTask, which can be used to monitor or manage the upload.

  #### Declaration

  Swift

      @discardableResult
      @objc(putFile:)
      open func __putFile(from fileURL: URL) -> https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageUploadTask.html

- `


  ### [putFile(from:metadata:completion:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)putFile:metadata:completion:)


  ` Asynchronously uploads a file to the currently specified `StorageReference`.

  #### Declaration

  Swift

      @discardableResult
      @objc(putFile:metadata:completion:)
      open func putFile(from fileURL: URL,
                        metadata: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html? = nil,
                        completion: ((_: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html?, _: Error?) -> Void)?) -> https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageUploadTask.html

  #### Parameters

  |---|---|
  | ` fileURL ` | A URL representing the system file path of the object to be uploaded. |
  | ` metadata ` | `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html` containing additional information (MIME type, etc.) about the object being uploaded. |
  | ` completion ` | A completion block that either returns the object metadata on success, or an error on failure. |

  #### Return Value

  An instance of `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageUploadTask.html`, which can be used to monitor or manage the
  upload.
[## Downloads](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/Downloads)

- `


  ### [getData(maxSize:completion:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)dataWithMaxSize:completion:)


  ` Asynchronously downloads the object at the `StorageReference` to a `Data` instance in memory.
  A `Data` buffer of the provided max size will be allocated, so ensure that the device has
  enough free
  memory to complete the download. For downloading large files, `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference.html#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)writeToFile:` may be a better
  option.

  #### Declaration

  Swift

      @discardableResult
      @objc(dataWithMaxSize:completion:)
      open func getData(maxSize: Int64,
                        completion: @escaping ((_: Data?, _: Error?) -> Void)) -> https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageDownloadTask.html

  #### Parameters

  |---|---|
  | ` maxSize ` | The maximum size in bytes to download. If the download exceeds this size, the task will be cancelled and an error will be returned. |
  | ` completion ` | A completion block that either returns the object data on success, or an error on failure. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageDownloadTask.html` that can be used to monitor or manage the download.
- `


  ### [downloadURL(completion:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)downloadURLWithCompletion:)


  ` Asynchronously retrieves a long lived download URL with a revokable token.
  This can be used to share the file with others, but can be revoked by a developer
  in the Firebase Console.

  #### Declaration

  Swift

      @objc(downloadURLWithCompletion:)
      open func downloadURL(completion: @escaping ((URL?, Error?) -> Void))

  #### Parameters

  |---|---|
  | ` completion ` | A completion block that either returns the URL on success, or an error on failure. |

- `


  ### [downloadURL()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/s:15FirebaseStorage0B9ReferenceC11downloadURL10Foundation0E0VyYaKF)


  ` Asynchronously retrieves a long lived download URL with a revokable token.
  This can be used to share the file with others, but can be revoked by a developer
  in the Firebase Console.
  Throws
  An error if the download URL could not be retrieved.

  #### Declaration

  Swift

      open func downloadURL() async throws -> URL

  #### Return Value

  The URL on success.
- `


  ### [write(toFile:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)writeToFile:)


  ` Asynchronously downloads the object at the current path to a specified system filepath.

  #### Declaration

  Swift

      @discardableResult
      @objc(writeToFile:)
      open func write(toFile fileURL: URL) -> https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageDownloadTask.html

  #### Parameters

  |---|---|
  | ` fileURL ` | A file system URL representing the path the object should be downloaded to. |

- `


  ### [write(toFile:completion:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)writeToFile:completion:)


  ` Asynchronously downloads the object at the current path to a specified system filepath.

  #### Declaration

  Swift

      @discardableResult
      @objc(writeToFile:completion:)
      open func write(toFile fileURL: URL,
                      completion: ((_: URL?, _: Error?) -> Void)?) -> https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageDownloadTask.html

  #### Parameters

  |---|---|
  | ` fileURL ` | A file system URL representing the path the object should be downloaded to. |
  | ` completion ` | A closure that fires when the file download completes, passed either a URL pointing to the file path of the downloaded file on success, or an error on failure. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageDownloadTask.html` that can be used to monitor or manage the download.
[## List Support](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/List-Support)

- `


  ### [listAll(completion:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)listAllWithCompletion:)


  ` Lists all items (files) and prefixes (folders) under this `StorageReference`.

  This is a helper method for calling `list()` repeatedly until there are no more results.

  Consistency of the result is not guaranteed if objects are inserted or removed while this
  operation is executing. All results are buffered in memory.

  `listAll(completion:)` is only available for projects using Firebase Rules Version 2.

  #### Declaration

  Swift

      @objc(listAllWithCompletion:)
      open func listAll(completion: @escaping ((https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageListResult.html?, Error?) -> Void))

  #### Parameters

  |---|---|
  | ` completion ` | A completion handler that will be invoked with all items and prefixes under the current `StorageReference`. |

- `


  ### [listAll()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/s:15FirebaseStorage0B9ReferenceC7listAllAA0B10ListResultCyYaKF)


  ` Lists all items (files) and prefixes (folders) under this StorageReference.
  This is a helper method for calling list() repeatedly until there are no more results.
  Consistency of the result is not guaranteed if objects are inserted or removed while this
  operation is executing. All results are buffered in memory.
  `listAll()` is only available for projects using Firebase Rules Version 2.
  Throws
  An error if the list operation failed.

  #### Declaration

  Swift

      open func listAll() async throws -> https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageListResult.html

  #### Return Value

  All items and prefixes under the current `StorageReference`.
- `


  ### [list(maxResults:completion:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)listWithMaxResults:completion:)


  ` List up to `maxResults` items (files) and prefixes (folders) under this StorageReference.

  "/" is treated as a path delimiter. Firebase Storage does not support unsupported object
  paths that end with "/" or contain two consecutive "/"s. All invalid objects in GCS will be
  filtered.

  Only available for projects using Firebase Rules Version 2.

  #### Declaration

  Swift

      @objc(listWithMaxResults:completion:)
      open func list(maxResults: Int64,
                     completion: @escaping ((_: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageListResult.html?, _: Error?) -> Void))

  #### Parameters

  |---|---|
  | ` maxResults ` | The maximum number of results to return in a single page. Must be greater than 0 and at most 1000. |
  | ` completion ` | A completion handler that will be invoked with up to `maxResults` items and prefixes under the current `StorageReference`. |

- `


  ### [list(maxResults:pageToken:completion:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)listWithMaxResults:pageToken:completion:)


  ` Resumes a previous call to `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference.html#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)listWithMaxResults:completion:`, starting after a pagination token.

  Returns the next set of items (files) and prefixes (folders) under this `StorageReference`.

  "/" is treated as a path delimiter. Storage does not support unsupported object
  paths that end with "/" or contain two consecutive "/"s. All invalid objects in GCS will be
  filtered.

  `list(maxResults:pageToken:completion:)`is only available for projects using Firebase Rules
  Version 2.

  #### Declaration

  Swift

      @objc(listWithMaxResults:pageToken:completion:)
      open func list(maxResults: Int64,
                     pageToken: String,
                     completion: @escaping ((_: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageListResult.html?, _: Error?) -> Void))

  #### Parameters

  |---|---|
  | ` maxResults ` | The maximum number of results to return in a single page. Must be greater than 0 and at most 1000. |
  | ` pageToken ` | A page token from a previous call to list. |
  | ` completion ` | A completion handler that will be invoked with the next items and prefixes under the current StorageReference. |

[## Metadata Operations](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/Metadata-Operations)

- `


  ### [getMetadata(completion:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)metadataWithCompletion:)


  ` Retrieves metadata associated with an object at the current path.

  #### Declaration

  Swift

      @objc(metadataWithCompletion:)
      open func getMetadata(completion: @escaping ((https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html?, Error?) -> Void))

  #### Parameters

  |---|---|
  | ` completion ` | A completion block which returns the object metadata on success, or an error on failure. |

- `


  ### [getMetadata()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/s:15FirebaseStorage0B9ReferenceC11getMetadataAA0bE0CyYaKF)


  ` Retrieves metadata associated with an object at the current path.
  Throws
  An error if the object metadata could not be retrieved.

  #### Declaration

  Swift

      open func getMetadata() async throws -> https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html

  #### Return Value

  The object metadata on success.
- `


  ### [updateMetadata(_:completion:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)updateMetadata:completion:)


  ` Updates the metadata associated with an object at the current path.

  #### Declaration

  Swift

      @objc(updateMetadata:completion:)
      open func updateMetadata(_ metadata: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html,
                               completion: ((_: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html?, _: Error?) -> Void)?)

  #### Parameters

  |---|---|
  | ` metadata ` | A `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html` object with the metadata to update. |
  | ` completion ` | A completion block which returns the `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html` on success, or an error on failure. |

- `


  ### [updateMetadata(_:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/s:15FirebaseStorage0B9ReferenceC14updateMetadatayAA0bE0CAFYaKF)


  ` Updates the metadata associated with an object at the current path.
  Throws
  An error if the metadata update operation failed.

  #### Declaration

  Swift

      open func updateMetadata(_ metadata: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html) async throws -> https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html

  #### Parameters

  |---|---|
  | ` metadata ` | A `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html` object with the metadata to update. |

  #### Return Value

  The object metadata on success.
[## Delete](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/Delete)

- `


  ### [delete(completion:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)deleteWithCompletion:)


  ` Deletes the object at the current path.

  #### Declaration

  Swift

      @objc(deleteWithCompletion:)
      open func delete(completion: ((Error?) -> Void)?)

  #### Parameters

  |---|---|
  | ` completion ` | A completion block which returns a nonnull error on failure. |

- `


  ### [delete()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/s:15FirebaseStorage0B9ReferenceC6deleteyyYaKF)


  ` Deletes the object at the current path.
  Throws
  An error if the delete operation failed.

  #### Declaration

  Swift

      open func delete() async throws

[## NSObject overrides](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/NSObject-overrides)

- `


  ### [copy()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)copy)


  ` NSObject override

  #### Declaration

  Swift

      override open func copy() -> Any

- `


  ### [isEqual(_:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)isEqual:)


  ` NSObject override

  #### Declaration

  Swift

      override open func isEqual(_ object: Any?) -> Bool

- `


  ### [hash](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(py)hash)


  ` NSObject override

  #### Declaration

  Swift

      override public var hash: Int { get }

- `


  ### [description](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(py)description)


  ` NSObject override

  #### Declaration

  Swift

      override public var description: String { get }

- `


  ### [data(maxSize:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/s:15FirebaseStorage0B9ReferenceC4data7maxSize10Foundation4DataVs5Int64V_tYaKF)


  ` Asynchronously downloads the object at the StorageReference to a Data object in memory.
  A Data object of the provided max size will be allocated, so ensure that the device has
  enough free memory to complete the download. For downloading large files, the `write`
  API may be a better option.
  Throws
  An error if the operation failed, for example if the data exceeded `maxSize`.

  #### Declaration

  Swift

      func data(maxSize: Int64) async throws -> Data

  #### Parameters

  |---|---|
  | ` maxSize ` | The maximum size in bytes to download. If the download exceeds this size, the task will be cancelled and an error will be thrown. |

  #### Return Value

  Data object.
- `


  ### [putDataAsync(_:metadata:onProgress:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/s:15FirebaseStorage0B9ReferenceC12putDataAsync_8metadata10onProgressAA0B8MetadataC10Foundation0E0V_AHSgySo10NSProgressCSgcSgtYaKF)


  ` Asynchronously uploads data to the currently specified StorageReference.
  This is not recommended for large files, and one should instead upload a file from disk
  from the Firebase Console.
  Throws
  An error if the operation failed, for example if Storage was unreachable.

  #### Declaration

  Swift

      func putDataAsync(_ uploadData: Data,
                        metadata: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html? = nil,
                        onProgress: ((Progress?) -> Void)? = nil) async throws -> https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html

  #### Parameters

  |---|---|
  | ` uploadData ` | The Data to upload. |
  | ` metadata ` | Optional StorageMetadata containing additional information (MIME type, etc.) about the object being uploaded. |
  | ` onProgress ` | An optional closure function to return a `Progress` instance while the upload proceeds. |

  #### Return Value

  StorageMetadata with additional information about the object being uploaded.
- `


  ### [putFileAsync(from:metadata:onProgress:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/s:15FirebaseStorage0B9ReferenceC12putFileAsync4from8metadata10onProgressAA0B8MetadataC10Foundation3URLV_AISgySo10NSProgressCSgcSgtYaKF)


  ` Asynchronously uploads a file to the currently specified StorageReference.
  Throws
  An error if the operation failed, for example if no file was present at the specified `url`.

  #### Declaration

  Swift

      func putFileAsync(from url: URL,
                        metadata: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html? = nil,
                        onProgress: ((Progress?) -> Void)? = nil) async throws -> https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html

  #### Parameters

  |---|---|
  | ` url ` | A URL representing the system file path of the object to be uploaded. |
  | ` metadata ` | Optional StorageMetadata containing additional information (MIME type, etc.) about the object being uploaded. |
  | ` onProgress ` | An optional closure function to return a `Progress` instance while the upload proceeds. |

  #### Return Value

  `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html` with additional information about the object being uploaded.
- `


  ### [writeAsync(toFile:onProgress:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/s:15FirebaseStorage0B9ReferenceC10writeAsync6toFile10onProgress10Foundation3URLVAI_ySo10NSProgressCSgcSgtYaKF)


  ` Asynchronously downloads the object at the current path to a specified system filepath.
  Throws
  An error if the operation failed, for example if Storage was unreachable or `fileURL` did not reference a valid path on disk.

  #### Declaration

  Swift

      func writeAsync(toFile fileURL: URL,
                      onProgress: ((Progress?) -> Void)? = nil) async throws -> URL

  #### Parameters

  |---|---|
  | ` fileURL ` | A URL representing the system file path of the object to be uploaded. |
  | ` onProgress ` | An optional closure function to return a `Progress` instance while the download proceeds. |

  #### Return Value

  A `URL` pointing to the file path of the downloaded file.
- `


  ### [list(maxResults:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/s:15FirebaseStorage0B9ReferenceC4list10maxResultsAA0B10ListResultCs5Int64V_tYaKF)


  ` List up to `maxResults` items (files) and prefixes (folders) under this StorageReference.

  "/" is treated as a path delimiter. Firebase Storage does not support unsupported object
  paths that end with "/" or contain two consecutive "/"s. All invalid objects in GCS will be
  filtered.

  Only available for projects using Firebase Rules Version 2.
  Throws
  An error if the operation failed, for example if Storage was unreachable or the storage reference referenced an invalid path.

  #### Declaration

  Swift

      func list(maxResults: Int64) async throws -> https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageListResult.html

  #### Parameters

  |---|---|
  | ` maxResults ` | The maximum number of results to return in a single page. Must be greater than 0 and at most 1000. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageListResult.html` containing the contents of the storage reference.
- `


  ### [list(maxResults:pageToken:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/s:15FirebaseStorage0B9ReferenceC4list10maxResults9pageTokenAA0B10ListResultCs5Int64V_SStYaKF)


  ` List up to `maxResults` items (files) and prefixes (folders) under this StorageReference.

  "/" is treated as a path delimiter. Firebase Storage does not support unsupported object
  paths that end with "/" or contain two consecutive "/"s. All invalid objects in GCS will be
  filtered.

  Only available for projects using Firebase Rules Version 2.
  Throws
  - An error if the operation failed, for example if Storage was unreachable or the storage reference referenced an invalid path.

  #### Declaration

  Swift

      func list(maxResults: Int64, pageToken: String) async throws -> https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageListResult.html

  #### Parameters

  |---|---|
  | ` maxResults ` | The maximum number of results to return in a single page. Must be greater than 0 and at most 1000. |
  | ` pageToken ` | A page token from a previous call to list. |

  #### Return Value

  <br />

  - completion A `Result` enum with either the list or an `Error`.

  <br />

- `


  ### [downloadURL(completion:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/s:15FirebaseStorage0B9ReferenceC11downloadURL10completionyys6ResultOy10Foundation0E0Vs5Error_pGc_tF)


  ` Asynchronously retrieves a long lived download URL with a revokable token.

  This can be used to share the file with others, but can be revoked by a developer
  in the Firebase Console.

  #### Declaration

  Swift

      func downloadURL(completion: @escaping (Result<URL, Error>) -> Void)

  #### Parameters

  |---|---|
  | ` completion ` | A completion block returning a `Result` enum with either a URL or an `Error`. |

- `


  ### [getData(maxSize:completion:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/s:15FirebaseStorage0B9ReferenceC7getData7maxSize10completionAA0B12DownloadTaskCs5Int64V_ys6ResultOy10Foundation0E0Vs5Error_pGctF)


  ` Asynchronously downloads the object at the `StorageReference` to a `Data` object.

  A `Data` of the provided max size will be allocated, so ensure that the device has enough
  memory to complete. For downloading large files, the `write` API may be a better option.

  #### Declaration

  Swift

      @discardableResult
      func getData(maxSize: Int64, completion: @escaping (Result<Data, Error>) -> Void)
        -> https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageDownloadTask.html

  #### Parameters

  |---|---|
  | ` maxSize ` | The maximum size in bytes to download. |
  | ` completion ` | A completion block returning a `Result` enum with either a `Data` object or an `Error`. |

  #### Return Value

  A StorageDownloadTask that can be used to monitor or manage the download.
- `


  ### [getMetadata(completion:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/s:15FirebaseStorage0B9ReferenceC11getMetadata10completionyys6ResultOyAA0bE0Cs5Error_pGc_tF)


  ` Retrieves metadata associated with an object at the current path.

  #### Declaration

  Swift

      func getMetadata(completion: @escaping (Result<https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html, Error>) -> Void)

  #### Parameters

  |---|---|
  | ` completion ` | A completion block which returns a `Result` enum with either the object metadata or an `Error`. |

- `


  ### [list(maxResults:pageToken:completion:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/s:15FirebaseStorage0B9ReferenceC4list10maxResults9pageToken10completionys5Int64V_SSys6ResultOyAA0b4ListK0Cs5Error_pGctF)


  ` Resumes a previous `list` call, starting after a pagination token.

  Returns the next set of items (files) and prefixes (folders) under this StorageReference.

  "/" is treated as a path delimiter. Firebase Storage does not support unsupported object
  paths that end with "/" or contain two consecutive "/"s. All invalid objects in GCS will be
  filtered.

  Only available for projects using Firebase Rules Version 2.

  #### Declaration

  Swift

      func list(maxResults: Int64,
                pageToken: String,
                completion: @escaping (Result<https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageListResult.html, Error>) -> Void)

  #### Parameters

  |---|---|
  | ` maxResults ` | The maximum number of results to return in a single page. Must be greater than 0 and at most 1000. |
  | ` pageToken ` | A page token from a previous call to list. |
  | ` completion ` | A completion handler that will be invoked with the next items and prefixes under the current StorageReference. It returns a `Result` enum with either the list or an `Error`. |

- `


  ### [list(maxResults:completion:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/s:15FirebaseStorage0B9ReferenceC4list10maxResults10completionys5Int64V_ys6ResultOyAA0b4ListI0Cs5Error_pGctF)


  ` List up to `maxResults` items (files) and prefixes (folders) under this StorageReference.

  "/" is treated as a path delimiter. Firebase Storage does not support unsupported object
  paths that end with "/" or contain two consecutive "/"s. All invalid objects in GCS will be
  filtered.

  Only available for projects using Firebase Rules Version 2.

  #### Declaration

  Swift

      func list(maxResults: Int64,
                completion: @escaping (Result<https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageListResult.html, Error>) -> Void)

  #### Parameters

  |---|---|
  | ` maxResults ` | The maximum number of results to return in a single page. Must be greater than 0 and at most 1000. |
  | ` completion ` | A completion handler that will be invoked with the next items and prefixes under the current `StorageReference`. It returns a `Result` enum with either the list or an `Error`. |

- `


  ### [listAll(completion:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/s:15FirebaseStorage0B9ReferenceC7listAll10completionyys6ResultOyAA0b4ListG0Cs5Error_pGc_tF)


  ` List all items (files) and prefixes (folders) under this StorageReference.

  This is a helper method for calling list() repeatedly until there are no more results.
  Consistency of the result is not guaranteed if objects are inserted or removed while this
  operation is executing. All results are buffered in memory.

  Only available for projects using Firebase Rules Version 2.

  #### Declaration

  Swift

      func listAll(completion: @escaping (Result<https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageListResult.html, Error>) -> Void)

  #### Parameters

  |---|---|
  | ` completion ` | A completion handler that will be invoked with all items and prefixes under the current StorageReference. It returns a `Result` enum with either the list or an `Error`. |

- `


  ### [putData(_:metadata:completion:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/s:15FirebaseStorage0B9ReferenceC7putData_8metadata10completionAA0B10UploadTaskC10Foundation0E0V_AA0B8MetadataCSgys6ResultOyAMs5Error_pGctF)


  ` Asynchronously uploads data to the currently specified `StorageReference`.
  This is not recommended for large files, and one should instead upload a file from disk.

  #### Declaration

  Swift

      @discardableResult
      func putData(_ uploadData: Data,
                   metadata: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html? = nil,
                   completion: @escaping (Result<https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html, Error>) -> Void)
        -> https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageUploadTask.html

  #### Parameters

  |---|---|
  | ` uploadData ` | The `Data` to upload. |
  | ` metadata ` | `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html` containing additional information (MIME type, etc.) about the object being uploaded. |
  | ` completion ` | A completion block that returns a `Result` enum with either the object metadata or an `Error`. |

  #### Return Value

  An instance of `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageUploadTask.html`, which can be used to monitor or manage
  the upload.
- `


  ### [putFile(from:metadata:completion:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/s:15FirebaseStorage0B9ReferenceC7putFile4from8metadata10completionAA0B10UploadTaskC10Foundation3URLV_AA0B8MetadataCSgys6ResultOyANs5Error_pGctF)


  ` Asynchronously uploads a file to the currently specified `StorageReference`.

  #### Declaration

  Swift

      @discardableResult
      func putFile(from: URL,
                   metadata: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html? = nil,
                   completion: @escaping (Result<https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html, Error>) -> Void)
        -> https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageUploadTask.html

  #### Parameters

  |---|---|
  | ` from ` | A URL representing the system file path of the object to be uploaded. |
  | ` metadata ` | `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html` containing additional information (MIME type, etc.) about the object being uploaded. |
  | ` completion ` | A completion block that returns a `Result` enum with either the object metadata or an `Error`. |

  #### Return Value

  An instance of `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageUploadTask.html`, which can be used to monitor or manage
  the upload.
- `


  ### [updateMetadata(_:completion:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/s:15FirebaseStorage0B9ReferenceC14updateMetadata_10completionyAA0bE0C_ys6ResultOyAGs5Error_pGctF)


  ` Updates the metadata associated with an object at the current path.

  #### Declaration

  Swift

      func updateMetadata(_ metadata: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html,
                          completion: @escaping (Result<https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html, Error>) -> Void)

  #### Parameters

  |---|---|
  | ` metadata ` | A `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.html` object with the metadata to update. |
  | ` completion ` | A completion block which returns a `Result` enum with either the object metadata or an `Error`. |

- `


  ### [write(toFile:completion:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference#/s:15FirebaseStorage0B9ReferenceC5write6toFile10completionAA0B12DownloadTaskC10Foundation3URLV_ys6ResultOyAKs5Error_pGctF)


  ` Asynchronously downloads the object at the current path to a specified system filepath.

  #### Declaration

  Swift

      @discardableResult
      func write(toFile: URL, completion: @escaping (Result<URL, Error>)
        -> Void) -> https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageDownloadTask.html

  #### Parameters

  |---|---|
  | ` toFile ` | A file system URL representing the path the object should be downloaded to. |
  | ` completion ` | A completion block that fires when the file download completes. The block returns a `Result` enum with either an NSURL pointing to the file path of the downloaded file or an `Error`. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageDownloadTask.html` that can be used to monitor or manage the download.