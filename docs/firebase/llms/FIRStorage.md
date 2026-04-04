# Source: https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorage.md.txt

# FirebaseStorage Framework Reference

# FIRStorage


    @interface FIRStorage : NSObject

Firebase Storage is a service that supports uploading and downloading binary objects,
such as images, videos, and other files to Google Cloud Storage. Instances of `Storage`
are not thread-safe, but can be accessed from any thread.
If you call `Storage.storage()`, the instance will initialize with the default `FirebaseApp`,
`FirebaseApp.app()`, and the storage location will come from the provided
`GoogleService-Info.plist`.
If you provide a custom instance of `FirebaseApp`,
the storage location will be specified via the `FirebaseOptions.storageBucket` property.
- `
  ``
  ``
  `

  ### [+storage](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(cm)storage)

  `
  `  
  The default `Storage` instance.

  returns:
  An instance of `Storage`, configured with the default `FirebaseApp`.  

  #### Declaration

  Objective-C  

      + (FIRStorage *_Nonnull)storage;

- `
  ``
  ``
  `

  ### [+storageWithURL:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(cm)storageWithURL:)

  `
  `  
  A method used to create `Storage` instances initialized with a custom storage bucket URL.
  Any `StorageReferences` generated from this instance of `Storage` will reference files
  and directories within the specified bucket.
  \\param url The `gs://` URL to your Firebase Storage bucket.

  returns:
  A `Storage` instance, configured with the custom storage bucket.  

  #### Declaration

  Objective-C  

      + (FIRStorage *_Nonnull)storageWithURL:(NSString *_Nonnull)url;

- `
  ``
  ``
  `

  ### [+storageForApp:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(cm)storageForApp:)

  `
  `  
  Creates an instance of `Storage`, configured with a custom `FirebaseApp`. `StorageReference`s
  generated from a resulting instance will reference files in the Firebase project
  associated with custom `FirebaseApp`.
  \\param app The custom `FirebaseApp` used for initialization.

  returns:
  A `Storage` instance, configured with the custom `FirebaseApp`.  

  #### Declaration

  Objective-C  

      + (FIRStorage *_Nonnull)storageForApp:(FIRApp *_Nonnull)app;

- `
  ``
  ``
  `

  ### [+storageForApp:URL:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(cm)storageForApp:URL:)

  `
  `  
  Creates an instance of `Storage`, configured with a custom `FirebaseApp` and a custom storage
  bucket URL.
  \\param app The custom `FirebaseApp` used for initialization.

  \\param url The `gs://` url to your Firebase Storage bucket.

  returns:
  the `Storage` instance, configured with the custom `FirebaseApp` and storage bucket URL.  

  #### Declaration

  Objective-C  

      + (FIRStorage *_Nonnull)storageForApp:(FIRApp *_Nonnull)app
                                        URL:(NSString *_Nonnull)url;

- `
  ``
  ``
  `

  ### [app](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(py)app)

  `
  `  
  The `FirebaseApp` associated with this Storage instance.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) FIRApp *_Nonnull app;

- `
  ``
  ``
  `

  ### [maxUploadRetryTime](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(py)maxUploadRetryTime)

  `
  `  
  The maximum time in seconds to retry an upload if a failure occurs.
  Defaults to 10 minutes (600 seconds).  

  #### Declaration

  Objective-C  

      @property (nonatomic) NSTimeInterval maxUploadRetryTime;

- `
  ``
  ``
  `

  ### [maxDownloadRetryTime](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(py)maxDownloadRetryTime)

  `
  `  
  The maximum time in seconds to retry a download if a failure occurs.
  Defaults to 10 minutes (600 seconds).  

  #### Declaration

  Objective-C  

      @property (nonatomic) NSTimeInterval maxDownloadRetryTime;

- `
  ``
  ``
  `

  ### [maxOperationRetryTime](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(py)maxOperationRetryTime)

  `
  `  
  The maximum time in seconds to retry operations other than upload and download if a failure occurs.
  Defaults to 2 minutes (120 seconds).  

  #### Declaration

  Objective-C  

      @property (nonatomic) NSTimeInterval maxOperationRetryTime;

- `
  ``
  ``
  `

  ### [uploadChunkSizeBytes](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(py)uploadChunkSizeBytes)

  `
  `  
  Specify the maximum upload chunk size. Values less than 256K (262144) will be rounded up to 256K. Values
  above 256K will be rounded down to the nearest 256K multiple. The default is no maximum.  

  #### Declaration

  Swift  

      @objc
      public var uploadChunkSizeBytes: Int64

- `
  ``
  ``
  `

  ### [callbackQueue](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(py)callbackQueue)

  `
  `  
  A `DispatchQueue` that all developer callbacks are fired on. Defaults to the main queue.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong) dispatch_queue_t _Nonnull callbackQueue;

- `
  ``
  ``
  `

  ### [-reference](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(im)reference)

  `
  `  
  Creates a `StorageReference` initialized at the root Firebase Storage location.

  returns:
  An instance of `StorageReference` referencing the root of the storage bucket.  

  #### Declaration

  Objective-C  

      - (https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference.html *_Nonnull)reference;

- `
  ``
  ``
  `

  ### [-referenceForURL:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(im)referenceForURL:)

  `
  `  
  Creates a StorageReference given a `gs://`, `http://`, or `https://` URL pointing to a
  Firebase Storage location. For example, you can pass in an `https://` download URL retrieved from
  `StorageReference.downloadURL(completion:)` or the `gs://` URL from
  `StorageReference.description`.
  \\param url A gs // or https:// URL to initialize the reference with.

  throws:
  Throws a fatal error if `url` is not associated with the `FirebaseApp` used to initialize
  this Storage instance.

  returns:
  An instance of StorageReference at the given child path.  

  #### Declaration

  Objective-C  

      - (https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference.html *_Nonnull)referenceForURL:(NSString *_Nonnull)url;

- `
  ``
  ``
  `

  ### [-referenceWithPath:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(im)referenceWithPath:)

  `
  `  
  Creates a `StorageReference` initialized at a location specified by the `path` parameter.
  \\param path A relative path from the root of the storage bucket,
  for instance @"path/to/object".

  returns:
  An instance of `StorageReference` pointing to the given path.  

  #### Declaration

  Objective-C  

      - (https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference.html *_Nonnull)referenceWithPath:(NSString *_Nonnull)path;

- `
  ``
  ``
  `

  ### [-useEmulatorWithHost:port:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(im)useEmulatorWithHost:port:)

  `
  `  
  Configures the Storage SDK to use an emulated backend instead of the default remote backend.
  This method should be called before invoking any other methods on a new instance of `Storage`.  

  #### Declaration

  Objective-C  

      - (void)useEmulatorWithHost:(NSString *_Nonnull)host port:(NSInteger)port;

- `
  ``
  ``
  `

  ### [-copy](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(im)copy)

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

  ### [-isEqual:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(im)isEqual:)

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

  ### [hash](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(py)hash)

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

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(im)init)

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

  ### [+new](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(cm)new)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)new SWIFT_UNAVAILABLE_MSG("-init is unavailable");