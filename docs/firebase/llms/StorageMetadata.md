# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata.md.txt

# FirebaseStorage Framework Reference

# StorageMetadata

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRStorageMetadata)
    open class StorageMetadata : NSObject

Class which represents the metadata on an object in Firebase Storage.

This metadata is
returned on successful operations, and can be used to retrieve download URLs, content types,
and a Storage reference to the object in question. Full documentation can be found in the
[GCS documentation](https://cloud.google.com/storage/docs/json_api/v1/objects#resource)
[## Public APIs](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/Public-APIs)

- `
  ``
  ``
  `

  ### [bucket](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)bucket)

  `
  `  
  The name of the bucket containing this object.  

  #### Declaration

  Swift  

      @objc
      public let bucket: String

- `
  ``
  ``
  `

  ### [cacheControl](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)cacheControl)

  `
  `  
  Cache-Control directive for the object data.  

  #### Declaration

  Swift  

      @objc
      public var cacheControl: String?

- `
  ``
  ``
  `

  ### [contentDisposition](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)contentDisposition)

  `
  `  
  Content-Disposition of the object data.  

  #### Declaration

  Swift  

      @objc
      public var contentDisposition: String?

- `
  ``
  ``
  `

  ### [contentEncoding](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)contentEncoding)

  `
  `  
  Content-Encoding of the object data.  

  #### Declaration

  Swift  

      @objc
      public var contentEncoding: String?

- `
  ``
  ``
  `

  ### [contentLanguage](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)contentLanguage)

  `
  `  
  Content-Language of the object data.  

  #### Declaration

  Swift  

      @objc
      public var contentLanguage: String?

- `
  ``
  ``
  `

  ### [contentType](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)contentType)

  `
  `  
  Content-Type of the object data.  

  #### Declaration

  Swift  

      @objc
      public var contentType: String?

- `
  ``
  ``
  `

  ### [md5Hash](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)md5Hash)

  `
  `  
  MD5 hash of the data; encoded using base64.  

  #### Declaration

  Swift  

      @objc
      public let md5Hash: String?

- `
  ``
  ``
  `

  ### [generation](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)generation)

  `
  `  
  The content generation of this object. Used for object versioning.  

  #### Declaration

  Swift  

      @objc
      public let generation: Int64

- `
  ``
  ``
  `

  ### [customMetadata](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)customMetadata)

  `
  `  
  User-provided metadata, in key/value pairs.  

  #### Declaration

  Swift  

      @objc
      public var customMetadata: [String : String]?

- `
  ``
  ``
  `

  ### [metageneration](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)metageneration)

  `
  `  
  The version of the metadata for this object at this generation. Used
  for preconditions and for detecting changes in metadata. A metageneration number is only
  meaningful in the context of a particular generation of a particular object.  

  #### Declaration

  Swift  

      @objc
      public let metageneration: Int64

- `
  ``
  ``
  `

  ### [name](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)name)

  `
  `  
  The name of this object, in gs://bucket/path/to/object.txt, this is object.txt.  

  #### Declaration

  Swift  

      @objc
      public internal(set) var name: String? { get }

- `
  ``
  ``
  `

  ### [path](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)path)

  `
  `  
  The full path of this object, in gs://bucket/path/to/object.txt, this is path/to/object.txt.  

  #### Declaration

  Swift  

      @objc
      public internal(set) var path: String? { get }

- `
  ``
  ``
  `

  ### [size](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)size)

  `
  `  
  Content-Length of the data in bytes.  

  #### Declaration

  Swift  

      @objc
      public let size: Int64

- `
  ``
  ``
  `

  ### [timeCreated](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)timeCreated)

  `
  `  
  The creation time of the object in RFC 3339 format.  

  #### Declaration

  Swift  

      @objc
      public let timeCreated: Date?

- `
  ``
  ``
  `

  ### [updated](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)updated)

  `
  `  
  The modification time of the object metadata in RFC 3339 format.  

  #### Declaration

  Swift  

      @objc
      public let updated: Date?

- `
  ``
  ``
  `

  ### [storageReference](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)storageReference)

  `
  `  
  Never used API  

  #### Declaration

  Swift  

      @available(*, deprecated)
      @objc
      public let storageReference: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference.html?

- `
  ``
  ``
  `

  ### [dictionaryRepresentation()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(im)dictionaryRepresentation)

  `
  `  
  Creates a Dictionary from the contents of the metadata.
  @return A Dictionary that represents the contents of the metadata.  

  #### Declaration

  Swift  

      @objc
      open func dictionaryRepresentation() -> [String : AnyHashable]

- `
  ``
  ``
  `

  ### [isFile](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)isFile)

  `
  `  
  Determines if the current metadata represents a "file".  

  #### Declaration

  Swift  

      @objc
      public var isFile: Bool { get }

- `
  ``
  ``
  `

  ### [isFolder](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)isFolder)

  `
  `  
  Determines if the current metadata represents a "folder".  

  #### Declaration

  Swift  

      @objc
      public var isFolder: Bool { get }

[## Public Initializers](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/Public-Initializers)

- `
  ``
  ``
  `

  ### [init()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(im)init)

  `
  `  
  Creates an empty instance of StorageMetadata.
  @return An empty instance of StorageMetadata.  

  #### Declaration

  Swift  

      override public convenience init()

- `
  ``
  ``
  `

  ### [init(dictionary:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(im)initWithDictionary:)

  `
  `  
  Creates an instance of StorageMetadata from the contents of a dictionary.
  @return An instance of StorageMetadata that represents the contents of a dictionary.  

  #### Declaration

  Swift  

      @objc
      public init(dictionary: [String : AnyHashable])

[## NSObject overrides](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/NSObject-overrides)

- `
  ``
  ``
  `

  ### [copy()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(im)copy)

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

  ### [isEqual(_:)](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(im)isEqual:)

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

  ### [hash](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)hash)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      override public var hash: Int { get }

- `
  ``
  ``
  `

  ### [description](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)description)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      override public var description: String { get }