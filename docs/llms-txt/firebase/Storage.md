# Source: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage.md.txt

# FirebaseStorage Framework Reference

# Storage

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRStorage)
    open class Storage : NSObject

Firebase Storage is a service that supports uploading and downloading binary objects,
such as images, videos, and other files to Google Cloud Storage. Instances of `Storage`
are not thread-safe, but can be accessed from any thread.

If you call [Storage.storage()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage.html#/c:@M@FirebaseStorage@objc(cs)FIRStorage(cm)storage), the instance will initialize with the default `FirebaseApp`,
`FirebaseApp.app()`, and the storage location will come from the provided
`GoogleService-Info.plist`.

If you provide a custom instance of `FirebaseApp`,
the storage location will be specified via the `FirebaseOptions.storageBucket` property.
[## Public APIs](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage#/Public-APIs)

- `
  ``
  ``
  `

  ### [storage()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(cm)storage)

  `
  `  
  The default `Storage` instance.  

  #### Declaration

  Swift  

      @objc(storage)
      open class func storage() -> Storage

  #### Return Value

  An instance of `Storage`, configured with the default `FirebaseApp`.
- `
  ``
  ``
  `

  ### [storage(url:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(cm)storageWithURL:)

  `
  `  
  A method used to create `Storage` instances initialized with a custom storage bucket URL.

  Any `StorageReferences` generated from this instance of `Storage` will reference files
  and directories within the specified bucket.  

  #### Declaration

  Swift  

      @objc(storageWithURL:)
      open class func storage(url: String) -> Storage

  #### Parameters

  |-------------|--------------------------------------------------|
  | ` `*url*` ` | The `gs://` URL to your Firebase Storage bucket. |

  #### Return Value

  A `Storage` instance, configured with the custom storage bucket.
- `
  ``
  ``
  `

  ### [storage(app:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(cm)storageForApp:)

  `
  `  
  Creates an instance of `Storage`, configured with a custom `FirebaseApp`. [StorageReference](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference.html)s
  generated from a resulting instance will reference files in the Firebase project
  associated with custom `FirebaseApp`.  

  #### Declaration

  Swift  

      @objc(storageForApp:)
      open class func storage(app: FirebaseApp) -> Storage

  #### Parameters

  |-------------|---------------------------------------------------|
  | ` `*app*` ` | The custom `FirebaseApp` used for initialization. |

  #### Return Value

  A `Storage` instance, configured with the custom `FirebaseApp`.
- `
  ``
  ``
  `

  ### [storage(app:url:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(cm)storageForApp:URL:)

  `
  `  
  Creates an instance of `Storage`, configured with a custom `FirebaseApp` and a custom storage
  bucket URL.  

  #### Declaration

  Swift  

      @objc(storageForApp:URL:)
      open class func storage(app: FirebaseApp, url: String) -> Storage

  #### Parameters

  |-------------|---------------------------------------------------|
  | ` `*app*` ` | The custom `FirebaseApp` used for initialization. |
  | ` `*url*` ` | The `gs://` url to your Firebase Storage bucket.  |

  #### Return Value

  The `Storage` instance, configured with the custom `FirebaseApp` and storage bucket
  URL.
- `
  ``
  ``
  `

  ### [app](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(py)app)

  `
  `  
  The `FirebaseApp` associated with this Storage instance.  

  #### Declaration

  Swift  

      @objc
      public let app: FirebaseApp

- `
  ``
  ``
  `

  ### [maxUploadRetryTime](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(py)maxUploadRetryTime)

  `
  `  
  The maximum time in seconds to retry an upload if a failure occurs.
  Defaults to 10 minutes (600 seconds).  

  #### Declaration

  Swift  

      @objc
      public var maxUploadRetryTime: TimeInterval { get set }

- `
  ``
  ``
  `

  ### [maxDownloadRetryTime](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(py)maxDownloadRetryTime)

  `
  `  
  The maximum time in seconds to retry a download if a failure occurs.
  Defaults to 10 minutes (600 seconds).  

  #### Declaration

  Swift  

      @objc
      public var maxDownloadRetryTime: TimeInterval { get set }

- `
  ``
  ``
  `

  ### [maxOperationRetryTime](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(py)maxOperationRetryTime)

  `
  `  
  The maximum time in seconds to retry operations other than upload and download if a failure
  occurs.
  Defaults to 2 minutes (120 seconds).  

  #### Declaration

  Swift  

      @objc
      public var maxOperationRetryTime: TimeInterval { get set }

- `
  ``
  ``
  `

  ### [uploadChunkSizeBytes](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(py)uploadChunkSizeBytes)

  `
  `  
  Specify the maximum upload chunk size. Values less than 256K (262144) will be rounded up to
  256K. Values
  above 256K will be rounded down to the nearest 256K multiple. The default is no maximum.  

  #### Declaration

  Swift  

      @objc
      public var uploadChunkSizeBytes: Int64

- `
  ``
  ``
  `

  ### [callbackQueue](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(py)callbackQueue)

  `
  `  
  A `DispatchQueue` that all developer callbacks are fired on. Defaults to the main queue.  

  #### Declaration

  Swift  

      @objc
      public var callbackQueue: DispatchQueue

- `
  ``
  ``
  `

  ### [reference()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(im)reference)

  `
  `  
  Creates a [StorageReference](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference.html) initialized at the root Firebase Storage location.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc
      open func reference() -> https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference.html

  #### Return Value

  An instance of [StorageReference](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference.html) referencing the root of the storage bucket.
- `
  ``
  ``
  `

  ### [reference(forURL:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(im)referenceForURL:)

  `
  `  
  Creates a StorageReference given a `gs://`, `http://`, or `https://` URL pointing to a
  Firebase Storage location.

  For example, you can pass in an `https://` download URL retrieved from
  [StorageReference.downloadURL(completion:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference.html#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)downloadURLWithCompletion:) or the `gs://` URL from
  [StorageReference.description](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference.html#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(py)description).  
  Throws
  Throws a fatal error if `url` is not associated with the `FirebaseApp` used to initialize this Storage instance.  

  #### Declaration

  Swift  

      @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
      @objc
      open func reference(forURL url: String) -> https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference.html

  #### Parameters

  |-------------|-----------------------------------------------------------|
  | ` `*url*` ` | A gs:// or https:// URL to initialize the reference with. |

  #### Return Value

  An instance of StorageReference at the given child path.
- `
  ``
  ``
  `

  ### [reference(for:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage#/s:15FirebaseStorage0B0C9reference3forAA0B9ReferenceC10Foundation3URLV_tKF)

  `
  `  
  Creates a StorageReference given a `gs://`, `http://`, or `https://` URL pointing to a
  Firebase Storage location.

  For example, you can pass in an `https://` download URL retrieved from
  [StorageReference.downloadURL(completion:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference.html#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(im)downloadURLWithCompletion:) or the `gs://` URL from
  [StorageReference.description](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference.html#/c:@M@FirebaseStorage@objc(cs)FIRStorageReference(py)description).  
  Throws
  Throws an Error if `url` is not associated with the `FirebaseApp` used to initialize this Storage instance.  

  #### Declaration

  Swift  

      open func reference(for url: URL) throws -> https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference.html

  #### Parameters

  |-------------|-----------------------------------------------------------|
  | ` `*url*` ` | A gs:// or https:// URL to initialize the reference with. |

  #### Return Value

  An instance of StorageReference at the given child path.
- `
  ``
  ``
  `

  ### [reference(withPath:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(im)referenceWithPath:)

  `
  `  
  Creates a [StorageReference](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference.html) initialized at a location specified by the `path` parameter.  

  #### Declaration

  Swift  

      @objc(referenceWithPath:)
      open func reference(withPath path: String) -> https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference.html

  #### Parameters

  |--------------|--------------------------------------------------------------------------------------|
  | ` `*path*` ` | A relative path from the root of the storage bucket, for instance @"path/to/object". |

  #### Return Value

  An instance of [StorageReference](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference.html) pointing to the given path.
- `
  ``
  ``
  `

  ### [useEmulator(withHost:port:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(im)useEmulatorWithHost:port:)

  `
  `  
  Configures the Storage SDK to use an emulated backend instead of the default remote backend.

  This method should be called before invoking any other methods on a new instance of `Storage`.  

  #### Declaration

  Swift  

      @objc
      open func useEmulator(withHost host: String, port: Int)

  #### Parameters

  |--------------|---------------------------------|
  | ` `*host*` ` | A string specifying the host.   |
  | ` `*port*` ` | The port specified as an `Int`. |

[## NSObject overrides](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage#/NSObject-overrides)

- `
  ``
  ``
  `

  ### [copy()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(im)copy)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      override open func copy() -> Any

- `
  ``
  ``
  `

  ### [isEqual(_:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(im)isEqual:)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      override open func isEqual(_ object: Any?) -> Bool

- `
  ``
  ``
  `

  ### [hash](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/Storage#/c:@M@FirebaseStorage@objc(cs)FIRStorage(py)hash)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      override public var hash: Int { get }