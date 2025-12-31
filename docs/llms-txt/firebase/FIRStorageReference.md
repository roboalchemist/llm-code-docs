# Source: https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference.md.txt

# FirebaseStorage Framework Reference

# FIRStorageReference


    @interface FIRStorageReference : NSObject

`StorageReference` represents a reference to a Google Cloud Storage object. Developers can
upload and download objects, as well as get/set object metadata, and delete an object at the
path. See the Cloud docs for more details: <https://cloud.google.com/storage/>
- `
  ``
  ``
  `

  ### [storage](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(py)storage)

  `
  `  
  The `Storage` service object which created this reference.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorage.html *_Nonnull storage;

- `
  ``
  ``
  `

  ### [bucket](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(py)bucket)

  `
  `  
  The name of the Google Cloud Storage bucket associated with this reference.
  For example, in `gs://bucket/path/to/object.txt`, the bucket would be 'bucket'.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly) NSString *_Nonnull bucket;

- `
  ``
  ``
  `

  ### [fullPath](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(py)fullPath)

  `
  `  
  The full path to this object, not including the Google Cloud Storage bucket.
  In `gs://bucket/path/to/object.txt`, the full path would be: `path/to/object.txt`  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly) NSString *_Nonnull fullPath;

- `
  ``
  ``
  `

  ### [name](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(py)name)

  `
  `  
  The short name of the object associated with this reference.
  In `gs://bucket/path/to/object.txt`, the name of the object would be `object.txt`.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly) NSString *_Nonnull name;

- `
  ``
  ``
  `

  ### [-root](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)root)

  `
  `  
  Creates a new `StorageReference` pointing to the root object.

  returns:
  A new `StorageReference` pointing to the root object.  

  #### Declaration

  Objective-C  

      - (FIRStorageReference *_Nonnull)root;

- `
  ``
  ``
  `

  ### [-parent](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)parent)

  `
  `  
  Creates a new `StorageReference` pointing to the parent of the current reference
  or `nil` if this instance references the root location.
  For example:
  path = foo/bar/baz parent = foo/bar
  path = foo parent = (root)
  path = (root) parent = nil

  returns:
  A new `StorageReference` pointing to the parent of the current reference.  

  #### Declaration

  Objective-C  

      - (FIRStorageReference *_Nullable)parent;

- `
  ``
  ``
  `

  ### [-child:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)child:)

  `
  `  
  Creates a new `StorageReference` pointing to a child object of the current reference.
  path = foo child = bar newPath = foo/bar
  path = foo/bar child = baz ntask.impl.snapshotwPath = foo/bar/baz
  All leading and trailing slashes will be removed, and consecutive slashes will be
  compressed to single slashes. For example:
  child = /foo/bar newPath = foo/bar
  child = foo/bar/ newPath = foo/bar
  child = foo///bar newPath = foo/bar
  \\param path The path to append to the current path.

  returns:
  A new `StorageReference` pointing to a child location of the current reference.  

  #### Declaration

  Objective-C  

      - (FIRStorageReference *_Nonnull)child:(NSString *_Nonnull)path;

- `
  ``
  ``
  `

  ### [-putData:metadata:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)putData:metadata:)

  `
  `  
  Asynchronously uploads data to the currently specified `StorageReference`,
  without additional metadata.
  This is not recommended for large files, and one should instead upload a file from disk.
  \\param uploadData The data to upload.

  \\param metadata `StorageMetadata` containing additional information (MIME type, etc.)
  about the object being uploaded.

  returns:
  An instance of `StorageUploadTask`, which can be used to monitor or manage the upload.  

  #### Declaration

  Objective-C  

      - (https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageUploadTask.html *_Nonnull)putData:(NSData *_Nonnull)uploadData
                                       metadata:
                                           (https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata.html *_Nullable)metadata;

- `
  ``
  ``
  `

  ### [-putData:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)putData:)

  `
  `  
  Asynchronously uploads data to the currently specified `StorageReference`.
  This is not recommended for large files, and one should instead upload a file from disk.
  \\param uploadData The data to upload.

  returns:
  An instance of `StorageUploadTask`, which can be used to monitor or manage the upload.  

  #### Declaration

  Objective-C  

      - (https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageUploadTask.html *_Nonnull)putData:(NSData *_Nonnull)uploadData;

- `
  ``
  ``
  `

  ### [-putData:metadata:completion:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)putData:metadata:completion:)

  `
  `  
  Asynchronously uploads data to the currently specified `StorageReference`.
  This is not recommended for large files, and one should instead upload a file from disk.
  \\param uploadData The data to upload.

  \\param metadata `StorageMetadata` containing additional information (MIME type, etc.)
  about the object being uploaded.

  \\param completion A closure that either returns the object metadata on success,
  or an error on failure.

  returns:
  An instance of `StorageUploadTask`, which can be used to monitor or manage the upload.  

  #### Declaration

  Objective-C  

      - (https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageUploadTask.html *_Nonnull)
             putData:(NSData *_Nonnull)uploadData
            metadata:(https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata.html *_Nullable)metadata
          completion:(void (^_Nullable)(https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata.html *_Nullable,
                                        NSError *_Nullable))completion;

- `
  ``
  ``
  `

  ### [-putFile:metadata:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)putFile:metadata:)

  `
  `  
  Asynchronously uploads a file to the currently specified `StorageReference`.
  `putData` should be used instead of `putFile` in Extensions.
  \\param fileURL A URL representing the system file path of the object to be uploaded.

  \\param metadata `StorageMetadata` containing additional information (MIME type, etc.)
  about the object being uploaded.

  returns:
  An instance of `StorageUploadTask`, which can be used to monitor or manage the upload.  

  #### Declaration

  Objective-C  

      - (https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageUploadTask.html *_Nonnull)putFile:(NSURL *_Nonnull)fileURL
                                       metadata:
                                           (https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata.html *_Nullable)metadata;

- `
  ``
  ``
  `

  ### [-putFile:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)putFile:)

  `
  `  
  Asynchronously uploads a file to the currently specified `StorageReference`,
  without additional metadata.
  `putData` should be used instead of `putFile` in Extensions.  

  #### Declaration

  Objective-C  

      - (https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageUploadTask.html *_Nonnull)putFile:(NSURL *_Nonnull)fileURL;

  #### Parameters

  |-----------------|-----------------------------------------------------------------------|
  | ` `*fileURL*` ` | A URL representing the system file path of the object to be uploaded. |

  #### Return Value

  An instance of StorageUploadTask, which can be used to monitor or manage the upload.
- `
  ``
  ``
  `

  ### [-putFile:metadata:completion:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)putFile:metadata:completion:)

  `
  `  
  Asynchronously uploads a file to the currently specified `StorageReference`.
  `putData` should be used instead of `putFile` in Extensions.
  \\param fileURL A URL representing the system file path of the object to be uploaded.

  \\param metadata `StorageMetadata` containing additional information (MIME type, etc.)
  about the object being uploaded.

  \\param completion A completion block that either returns the object metadata on success,
  or an error on failure.

  returns:
  An instance of `StorageUploadTask`, which can be used to monitor or manage the upload.  

  #### Declaration

  Objective-C  

      - (https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageUploadTask.html *_Nonnull)
             putFile:(NSURL *_Nonnull)fileURL
            metadata:(https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata.html *_Nullable)metadata
          completion:(void (^_Nullable)(https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata.html *_Nullable,
                                        NSError *_Nullable))completion;

- `
  ``
  ``
  `

  ### [-dataWithMaxSize:completion:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)dataWithMaxSize:completion:)

  `
  `  
  Asynchronously downloads the object at the `StorageReference` to a `Data` instance in memory.
  A `Data` buffer of the provided max size will be allocated, so ensure that the device has enough free
  memory to complete the download. For downloading large files, `write(toFile:)` may be a better option.
  \\param maxSize The maximum size in bytes to download. If the download exceeds this size,
  the task will be cancelled and an error will be returned.

  \\param completion A completion block that either returns the object data on success,
  or an error on failure.

  returns:
  An `StorageDownloadTask` that can be used to monitor or manage the download.  

  #### Declaration

  Objective-C  

      - (https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageDownloadTask.html *_Nonnull)
          dataWithMaxSize:(int64_t)maxSize
               completion:(void (^_Nonnull)(NSData *_Nullable,
                                            NSError *_Nullable))completion;

- `
  ``
  ``
  `

  ### [-downloadURLWithCompletion:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)downloadURLWithCompletion:)

  `
  `  
  Asynchronously retrieves a long lived download URL with a revokable token.
  This can be used to share the file with others, but can be revoked by a developer
  in the Firebase Console.
  \\param completion A completion block that either returns the URL on success,
  or an error on failure.  

  #### Declaration

  Objective-C  

      - (void)downloadURLWithCompletion:
          (void (^_Nonnull)(NSURL *_Nullable, NSError *_Nullable))completion;

- `
  ``
  ``
  `

  ### [-writeToFile:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)writeToFile:)

  `
  `  
  Asynchronously downloads the object at the current path to a specified system filepath.
  - Returns An `StorageDownloadTask` that can be used to monitor or manage the download.

  \\param fileURL A file system URL representing the path the object should be downloaded to.  

  #### Declaration

  Objective-C  

      - (https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageDownloadTask.html *_Nonnull)writeToFile:(NSURL *_Nonnull)fileURL;

- `
  ``
  ``
  `

  ### [-writeToFile:completion:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)writeToFile:completion:)

  `
  `  
  Asynchronously downloads the object at the current path to a specified system filepath.
  \\param fileURL A file system URL representing the path the object should be downloaded to.

  \\param completion A closure that fires when the file download completes, passed either
  a URL pointing to the file path of the downloaded file on success,
  or an error on failure.

  returns:
  A `StorageDownloadTask` that can be used to monitor or manage the download.  

  #### Declaration

  Objective-C  

      - (https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageDownloadTask.html *_Nonnull)
          writeToFile:(NSURL *_Nonnull)fileURL
           completion:
               (void (^_Nullable)(NSURL *_Nullable, NSError *_Nullable))completion;

- `
  ``
  ``
  `

  ### [-listAllWithCompletion:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)listAllWithCompletion:)

  `
  `  
  Lists all items (files) and prefixes (folders) under this `StorageReference`.
  This is a helper method for calling `list()` repeatedly until there are no more results.
  Consistency of the result is not guaranteed if objects are inserted or removed while this
  operation is executing. All results are buffered in memory.
  `listAll(completion:)` is only available for projects using Firebase Rules Version 2.
  \\param completion A completion handler that will be invoked with all items and prefixes under
  the current `StorageReference`.  

  #### Declaration

  Objective-C  

      - (void)listAllWithCompletion:(void (^_Nonnull)(https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageListResult.html *_Nullable,
                                                      NSError *_Nullable))completion;

- `
  ``
  ``
  `

  ### [-listWithMaxResults:completion:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)listWithMaxResults:completion:)

  `
  `  
  List up to `maxResults` items (files) and prefixes (folders) under this StorageReference.
  "/" is treated as a path delimiter. Firebase Storage does not support unsupported object
  paths that end with "/" or contain two consecutive "/"s. All invalid objects in GCS will be
  filtered.
  `list(maxResults:completion:)` is only available for projects using Firebase Rules Version 2.
  \\param maxResults The maximum number of results to return in a single page. Must be greater
  than 0 and at most 1000.

  \\param completion A completion handler that will be invoked with up to `maxResults` items and
  prefixes under the current `StorageReference`.  

  #### Declaration

  Objective-C  

      - (void)listWithMaxResults:(int64_t)maxResults
                      completion:(void (^_Nonnull)(https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageListResult.html *_Nullable,
                                                   NSError *_Nullable))completion;

- `
  ``
  ``
  `

  ### [-listWithMaxResults:pageToken:completion:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)listWithMaxResults:pageToken:completion:)

  `
  `  
  Resumes a previous call to `list(maxResults:completion:)`, starting after a pagination token.
  Returns the next set of items (files) and prefixes (folders) under this `StorageReference`.
  "/" is treated as a path delimiter. Storage does not support unsupported object
  paths that end with "/" or contain two consecutive "/"s. All invalid objects in GCS will be
  filtered.
  `list(maxResults:pageToken:completion:)`is only available for projects using Firebase Rules
  Version 2.
  \\param maxResults The maximum number of results to return in a single page. Must be greater
  than 0 and at most 1000.

  \\param pageToken A page token from a previous call to list.

  \\param completion A completion handler that will be invoked with the next items and prefixes
  under the current StorageReference.  

  #### Declaration

  Objective-C  

      - (void)listWithMaxResults:(int64_t)maxResults
                       pageToken:(NSString *_Nonnull)pageToken
                      completion:(void (^_Nonnull)(https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageListResult.html *_Nullable,
                                                   NSError *_Nullable))completion;

- `
  ``
  ``
  `

  ### [-metadataWithCompletion:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)metadataWithCompletion:)

  `
  `  
  Retrieves metadata associated with an object at the current path.
  \\param completion A completion block which returns the object metadata on success,
  or an error on failure.  

  #### Declaration

  Objective-C  

      - (void)metadataWithCompletion:(void (^_Nonnull)(https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata.html *_Nullable,
                                                       NSError *_Nullable))completion;

- `
  ``
  ``
  `

  ### [-updateMetadata:completion:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)updateMetadata:completion:)

  `
  `  
  Updates the metadata associated with an object at the current path.
  \\param metadata A `StorageMetadata` object with the metadata to update.

  \\param completion A completion block which returns the `StorageMetadata` on success,
  or an error on failure.  

  #### Declaration

  Objective-C  

      - (void)updateMetadata:(https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata.html *_Nonnull)metadata
                  completion:(void (^_Nullable)(https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata.html *_Nullable,
                                                NSError *_Nullable))completion;

- `
  ``
  ``
  `

  ### [-deleteWithCompletion:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)deleteWithCompletion:)

  `
  `  
  Deletes the object at the current path.
  \\param completion A completion block which returns a nonnull error on failure.  

  #### Declaration

  Objective-C  

      - (void)deleteWithCompletion:(void (^_Nullable)(NSError *_Nullable))completion;

- `
  ``
  ``
  `

  ### [-copy](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)copy)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      - (id _Nonnull)copy SWIFT_WARN_UNUSED_RESULT;

- `
  ``
  ``
  `

  ### [-isEqual:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)isEqual:)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      - (BOOL)isEqual:(id _Nullable)object SWIFT_WARN_UNUSED_RESULT;

- `
  ``
  ``
  `

  ### [hash](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(py)hash)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSUInteger hash

- `
  ``
  ``
  `

  ### [description](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(py)description)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, copy) NSString * _Nonnull description

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)init)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init SWIFT_UNAVAILABLE;

- `
  ``
  ``
  `

  ### [+new](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(cm)new)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)new SWIFT_UNAVAILABLE_MSG("-init is unavailable");