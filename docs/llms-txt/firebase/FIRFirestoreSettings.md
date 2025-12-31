# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestoreSettings.md.txt

# FirebaseFirestore Framework Reference

# FIRFirestoreSettings


    @interface FIRFirestoreSettings : NSObject <NSCopying>

Settings used to configure a `Firestore` instance.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestoreSettings#/c:objc(cs)FIRFirestoreSettings(im)init)

  `
  `  
  Creates and returns an empty `FirestoreSettings` object.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

  #### Return Value

  The created `FirestoreSettings` object.
- `
  ``
  ``
  `

  ### [host](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestoreSettings#/c:objc(cs)FIRFirestoreSettings(py)host)

  `
  `  
  The hostname to connect to.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy) NSString *_Nonnull host;

- `
  ``
  ``
  `

  ### [sslEnabled](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestoreSettings#/c:objc(cs)FIRFirestoreSettings(py)sslEnabled)

  `
  `  
  Whether to use SSL when connecting.  

  #### Declaration

  Objective-C  

      @property (nonatomic, getter=isSSLEnabled) BOOL sslEnabled;

- `
  ``
  ``
  `

  ### [dispatchQueue](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestoreSettings#/c:objc(cs)FIRFirestoreSettings(py)dispatchQueue)

  `
  `  
  A dispatch queue to be used to execute all completion handlers and event handlers. By default,
  the main queue is used.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong) dispatch_queue_t _Nonnull dispatchQueue;

- `
  ``
  ``
  `

  ### [persistenceEnabled](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestoreSettings#/c:objc(cs)FIRFirestoreSettings(py)persistenceEnabled)

  `
  `  
  Deprecated

  This field is deprecated. Use [cacheSettings](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestoreSettings.html#/c:objc(cs)FIRFirestoreSettings(py)cacheSettings) instead.  
  NOTE: This field will be deprecated in a future major release. Use the [cacheSettings](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestoreSettings.html#/c:objc(cs)FIRFirestoreSettings(py)cacheSettings) field
  instead to specify cache type, and other cache configurations.

  Set to false to disable local persistent storage.  

  #### Declaration

  Objective-C  

      @property (nonatomic, assign, unsafe_unretained, readwrite,
                getter=isPersistenceEnabled) BOOL persistenceEnabled;

- `
  ``
  ``
  `

  ### [cacheSizeBytes](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestoreSettings#/c:objc(cs)FIRFirestoreSettings(py)cacheSizeBytes)

  `
  `  
  Deprecated

  This field is deprecated. Use [cacheSettings](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestoreSettings.html#/c:objc(cs)FIRFirestoreSettings(py)cacheSettings) instead.  
  NOTE: This field will be deprecated in a future major release. Use the [cacheSettings](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestoreSettings.html#/c:objc(cs)FIRFirestoreSettings(py)cacheSettings) field
  instead to specify cache size, and other cache configurations.

  Sets the cache size threshold above which the SDK will attempt to collect least-recently-used
  documents. The size is not a guarantee that the cache will stay below that size, only that if
  the cache exceeds the given size, cleanup will be attempted. Cannot be set lower than 1MB.

  Set to `FirestoreCacheSizeUnlimited` to disable garbage collection entirely.  

  #### Declaration

  Objective-C  

      @property (nonatomic) int64_t cacheSizeBytes;

- `
  ``
  ``
  `

  ### [cacheSettings](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestoreSettings#/c:objc(cs)FIRFirestoreSettings(py)cacheSettings)

  `
  `  
  Specifies the cache used by the SDK. Available options are `PersistentCacheSettings`
  and `MemoryCacheSettings`, each with different configuration options.

  When unspecified, `PersistentCacheSettings` will be used by default.

  NOTE: setting this field and [cacheSizeBytes](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestoreSettings.html#/c:objc(cs)FIRFirestoreSettings(py)cacheSizeBytes) or [persistenceEnabled](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRFirestoreSettings.html#/c:objc(cs)FIRFirestoreSettings(py)persistenceEnabled) at the same time will throw
  an exception during SDK initialization. Instead, use the configuration in
  the `PersistentCacheSettings` object to specify the cache size.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong) id<https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Protocols.html#/c:objc(pl)FIRLocalCacheSettings, NSObject> _Nonnull cacheSettings;