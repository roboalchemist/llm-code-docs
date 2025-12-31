# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FirestoreSettings.md.txt

# FirebaseFirestore Framework Reference

# FirestoreSettings

    class FirestoreSettings : NSObject, NSCopying

Settings used to configure a [Firestore](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Firestore.html) instance.
- `
  ``
  ``
  `

  ### [init()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FirestoreSettings#/c:objc(cs)FIRFirestoreSettings(im)init)

  `
  `  
  Creates and returns an empty `FirestoreSettings` object.  

  #### Declaration

  Swift  

      init()

  #### Return Value

  The created `FirestoreSettings` object.
- `
  ``
  ``
  `

  ### [host](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FirestoreSettings#/c:objc(cs)FIRFirestoreSettings(py)host)

  `
  `  
  The hostname to connect to.  

  #### Declaration

  Swift  

      var host: String { get set }

- `
  ``
  ``
  `

  ### [isSSLEnabled](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FirestoreSettings#/c:objc(cs)FIRFirestoreSettings(py)sslEnabled)

  `
  `  
  Whether to use SSL when connecting.  

  #### Declaration

  Swift  

      var isSSLEnabled: Bool { get set }

- `
  ``
  ``
  `

  ### [dispatchQueue](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FirestoreSettings#/c:objc(cs)FIRFirestoreSettings(py)dispatchQueue)

  `
  `  
  A dispatch queue to be used to execute all completion handlers and event handlers. By default,
  the main queue is used.  

  #### Declaration

  Swift  

      var dispatchQueue: dispatch_queue_t { get set }

- `
  ``
  ``
  `

  ### [isPersistenceEnabled](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FirestoreSettings#/c:objc(cs)FIRFirestoreSettings(py)persistenceEnabled)

  `
  `  
  Deprecated

  This field is deprecated. Use [cacheSettings](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FirestoreSettings.html#/c:objc(cs)FIRFirestoreSettings(py)cacheSettings) instead.  
  NOTE: This field will be deprecated in a future major release. Use the [cacheSettings](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FirestoreSettings.html#/c:objc(cs)FIRFirestoreSettings(py)cacheSettings) field
  instead to specify cache type, and other cache configurations.

  Set to false to disable local persistent storage.  

  #### Declaration

  Swift  

      var isPersistenceEnabled: Bool { get set }

- `
  ``
  ``
  `

  ### [cacheSizeBytes](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FirestoreSettings#/c:objc(cs)FIRFirestoreSettings(py)cacheSizeBytes)

  `
  `  
  Deprecated

  This field is deprecated. Use [cacheSettings](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FirestoreSettings.html#/c:objc(cs)FIRFirestoreSettings(py)cacheSettings) instead.  
  NOTE: This field will be deprecated in a future major release. Use the [cacheSettings](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FirestoreSettings.html#/c:objc(cs)FIRFirestoreSettings(py)cacheSettings) field
  instead to specify cache size, and other cache configurations.

  Sets the cache size threshold above which the SDK will attempt to collect least-recently-used
  documents. The size is not a guarantee that the cache will stay below that size, only that if
  the cache exceeds the given size, cleanup will be attempted. Cannot be set lower than 1MB.

  Set to [FirestoreCacheSizeUnlimited](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Constants.html#/c:@kFIRFirestoreCacheSizeUnlimited) to disable garbage collection entirely.  

  #### Declaration

  Swift  

      var cacheSizeBytes: Int64 { get set }

- `
  ``
  ``
  `

  ### [cacheSettings](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FirestoreSettings#/c:objc(cs)FIRFirestoreSettings(py)cacheSettings)

  `
  `  
  Specifies the cache used by the SDK. Available options are [PersistentCacheSettings](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/PersistentCacheSettings.html)
  and [MemoryCacheSettings](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/MemoryCacheSettings.html), each with different configuration options.

  When unspecified, [PersistentCacheSettings](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/PersistentCacheSettings.html) will be used by default.

  NOTE: setting this field and [cacheSizeBytes](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FirestoreSettings.html#/c:objc(cs)FIRFirestoreSettings(py)cacheSizeBytes) or `persistenceEnabled` at the same time will throw
  an exception during SDK initialization. Instead, use the configuration in
  the [PersistentCacheSettings](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/PersistentCacheSettings.html) object to specify the cache size.  

  #### Declaration

  Swift  

      var cacheSettings: any NSObjectProtocol & FIRLocalCacheSettings { get set }