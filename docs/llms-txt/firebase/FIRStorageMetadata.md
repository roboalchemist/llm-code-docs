# Source: https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata.md.txt

# FirebaseStorage Framework Reference

# FIRStorageMetadata


    @interface FIRStorageMetadata : NSObject

Class which represents the metadata on an object in Firebase Storage. This metadata is
returned on successful operations, and can be used to retrieve download URLs, content types,
and a Storage reference to the object in question. Full documentation can be found at the GCS
Objects#resource docs.  
See
<https://cloud.google.com/storage/docs/json_api/v1/objects#resource>
- `
  ``
  ``
  `

  ### [bucket](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)bucket)

  `
  `  
  The name of the bucket containing this object.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly) NSString *_Nonnull bucket;

- `
  ``
  ``
  `

  ### [cacheControl](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)cacheControl)

  `
  `  
  Cache-Control directive for the object data.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy) NSString *_Nullable cacheControl;

- `
  ``
  ``
  `

  ### [contentDisposition](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)contentDisposition)

  `
  `  
  Content-Disposition of the object data.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy) NSString *_Nullable contentDisposition;

- `
  ``
  ``
  `

  ### [contentEncoding](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)contentEncoding)

  `
  `  
  Content-Encoding of the object data.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy) NSString *_Nullable contentEncoding;

- `
  ``
  ``
  `

  ### [contentLanguage](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)contentLanguage)

  `
  `  
  Content-Language of the object data.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy) NSString *_Nullable contentLanguage;

- `
  ``
  ``
  `

  ### [contentType](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)contentType)

  `
  `  
  Content-Type of the object data.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy) NSString *_Nullable contentType;

- `
  ``
  ``
  `

  ### [md5Hash](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)md5Hash)

  `
  `  
  MD5 hash of the data; encoded using base64.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly) NSString *_Nullable md5Hash;

- `
  ``
  ``
  `

  ### [generation](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)generation)

  `
  `  
  The content generation of this object. Used for object versioning.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) int64_t generation;

- `
  ``
  ``
  `

  ### [customMetadata](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)customMetadata)

  `
  `  
  User-provided metadata, in key/value pairs.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy) NSDictionary<NSString *, NSString *> *_Nullable customMetadata;

- `
  ``
  ``
  `

  ### [metageneration](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)metageneration)

  `
  `  
  The version of the metadata for this object at this generation. Used
  for preconditions and for detecting changes in metadata. A metageneration number is only
  meaningful in the context of a particular generation of a particular object.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) int64_t metageneration;

- `
  ``
  ``
  `

  ### [name](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)name)

  `
  `  
  The name of this object, in gs://bucket/path/to/object.txt, this is object.txt.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly) NSString *_Nullable name;

- `
  ``
  ``
  `

  ### [path](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)path)

  `
  `  
  The full path of this object, in gs://bucket/path/to/object.txt, this is path/to/object.txt.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly) NSString *_Nullable path;

- `
  ``
  ``
  `

  ### [size](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)size)

  `
  `  
  Content-Length of the data in bytes.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) int64_t size;

- `
  ``
  ``
  `

  ### [timeCreated](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)timeCreated)

  `
  `  
  The creation time of the object in RFC 3339 format.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly) NSDate *_Nullable timeCreated;

- `
  ``
  ``
  `

  ### [updated](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)updated)

  `
  `  
  The modification time of the object metadata in RFC 3339 format.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly) NSDate *_Nullable updated;

- `
  ``
  ``
  `

  ### [storageReference](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)storageReference)

  `
  `  
  Never used API  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) SWIFT_DEPRECATED https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageReference.html *storageReference;

- `
  ``
  ``
  `

  ### [-dictionaryRepresentation](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(im)dictionaryRepresentation)

  `
  `  
  Creates a Dictionary from the contents of the metadata.  

  #### Declaration

  Objective-C  

      - (NSDictionary<NSString *, NSObject *> *_Nonnull)dictionaryRepresentation;

  #### Return Value

  A Dictionary that represents the contents of the metadata.
- `
  ``
  ``
  `

  ### [isFile](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)isFile)

  `
  `  
  Determines if the current metadata represents a "file".  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) BOOL isFile;

- `
  ``
  ``
  `

  ### [isFolder](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)isFolder)

  `
  `  
  Determines if the current metadata represents a "folder".  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) BOOL isFolder;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(im)init)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

- `
  ``
  ``
  `

  ### [-initWithDictionary:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(im)initWithDictionary:)

  `
  `  
  Creates an instance of StorageMetadata from the contents of a dictionary.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)initWithDictionary:
          (NSDictionary<NSString *, NSObject *> *_Nonnull)dictionary;

  #### Return Value

  An instance of StorageMetadata that represents the contents of a dictionary.
- `
  ``
  ``
  `

  ### [-copy](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(im)copy)

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

  ### [-isEqual:](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(im)isEqual:)

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

  ### [hash](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)hash)

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

  ### [description](https://firebase.google.com/docs/reference/ios/firebasestorage/api/reference/Classes/FIRStorageMetadata#/c:@M@FirebaseStorage@objc(cs)FIRStorageMetadata(py)description)

  `
  `  
  Undocumented  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, copy) NSString * _Nonnull description