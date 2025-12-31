# Source: https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDatabase.md.txt

# FirebaseDatabase Framework Reference

# FIRDatabase


    @interface FIRDatabase : NSObject

The entry point for accessing a Firebase Database. You can get an instance
by calling `Database.database()`. To access a location in the database and
read or write data, use `FIRDatabase.reference()`.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDatabase#/c:objc(cs)FIRDatabase(im)init)

  `
  `  
  Unavailable

  use the database method instead  
  The NSObject initializer that has been marked as unavailable. Use the
  `database` class method instead.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

- `
  ``
  ``
  `

  ### [+database](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDatabase#/c:objc(cs)FIRDatabase(cm)database)

  `
  `  
  Gets the instance of `Database` for the default `FirebaseApp`.  

  #### Declaration

  Objective-C  

      + (nonnull FIRDatabase *)database;

  #### Return Value

  A `Database` instance.
- `
  ``
  ``
  `

  ### [+databaseWithURL:](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDatabase#/c:objc(cs)FIRDatabase(cm)databaseWithURL:)

  `
  `  
  Gets a `Database` instance for the specified URL.  

  #### Declaration

  Objective-C  

      + (nonnull FIRDatabase *)databaseWithURL:(nonnull NSString *)url;

  #### Parameters

  |-------------|---------------------------------------------------------------|
  | ` `*url*` ` | The URL to the Firebase Database instance you want to access. |

  #### Return Value

  A `Database` instance.
- `
  ``
  ``
  `

  ### [+databaseForApp:URL:](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDatabase#/c:objc(cs)FIRDatabase(cm)databaseForApp:URL:)

  `
  `  
  Gets a `Database` instance for the specified URL, using the specified
  `FirebaseApp`.  

  #### Declaration

  Objective-C  

      + (nonnull FIRDatabase *)databaseForApp:(nonnull FIRApp *)app
                                          URL:(nonnull NSString *)url;

  #### Parameters

  |-------------|---------------------------------------------------------------|
  | ` `*app*` ` | The app to get a `Database` for.                              |
  | ` `*url*` ` | The URL to the Firebase Database instance you want to access. |

  #### Return Value

  A `Database` instance.
- `
  ``
  ``
  `

  ### [+databaseForApp:](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDatabase#/c:objc(cs)FIRDatabase(cm)databaseForApp:)

  `
  `  
  Gets an instance of `Database` for a specific `FirebaseApp`.  

  #### Declaration

  Objective-C  

      + (nonnull FIRDatabase *)databaseForApp:(nonnull FIRApp *)app;

  #### Parameters

  |-------------|----------------------------------|
  | ` `*app*` ` | The app to get a `Database` for. |

  #### Return Value

  A `Database` instance.
- `
  ``
  ``
  `

  ### [app](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDatabase#/c:objc(cs)FIRDatabase(py)app)

  `
  `  
  The app instance to which this `Database` belongs.  

  #### Declaration

  Objective-C  

      @property (nonatomic, weak, readonly) FIRApp *_Nullable app;

- `
  ``
  ``
  `

  ### [-reference](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDatabase#/c:objc(cs)FIRDatabase(im)reference)

  `
  `  
  Gets a `DatabaseReference` for the root of your Firebase Database.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDatabaseReference.html *)reference;

- `
  ``
  ``
  `

  ### [-referenceWithPath:](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDatabase#/c:objc(cs)FIRDatabase(im)referenceWithPath:)

  `
  `  
  Gets a `DatabaseReference` for the provided path.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDatabaseReference.html *)referenceWithPath:(nonnull NSString *)path;

  #### Parameters

  |--------------|-----------------------------------------------|
  | ` `*path*` ` | Path to a location in your Firebase Database. |

  #### Return Value

  A `DatabaseReference` pointing to the specified path.
- `
  ``
  ``
  `

  ### [-referenceFromURL:](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDatabase#/c:objc(cs)FIRDatabase(im)referenceFromURL:)

  `
  `  
  Gets a `DatabaseReference` for the provided URL. The URL must be a URL to a
  path within this Firebase Database. To create a `DatabaseReference` to a
  different database, create a `FirebaseApp` with an `Options` object
  configured with the appropriate database URL.  

  #### Declaration

  Objective-C  

      - (nonnull https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDatabaseReference.html *)referenceFromURL:
          (nonnull NSString *)databaseUrl;

  #### Parameters

  |---------------------|---------------------------------------|
  | ` `*databaseUrl*` ` | A URL to a path within your database. |

  #### Return Value

  A `DatabaseReference` for the provided URL.
- `
  ``
  ``
  `

  ### [-purgeOutstandingWrites](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDatabase#/c:objc(cs)FIRDatabase(im)purgeOutstandingWrites)

  `
  `  
  The Firebase Database client automatically queues writes and sends them to
  the server at the earliest opportunity, depending on network connectivity. In
  some cases (e.g. offline usage) there may be a large number of writes waiting
  to be sent. Calling this method will purge all outstanding writes so they are
  abandoned.

  All writes will be purged, including transactions and onDisconnect writes.
  The writes will be rolled back locally, perhaps triggering events for
  affected event listeners, and the client will not (re-)send them to the
  Firebase Database backend.  

  #### Declaration

  Objective-C  

      - (void)purgeOutstandingWrites;

- `
  ``
  ``
  `

  ### [-goOffline](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDatabase#/c:objc(cs)FIRDatabase(im)goOffline)

  `
  `  
  Shuts down the connection to the Firebase Database backend until `goOnline()`
  is called.  

  #### Declaration

  Objective-C  

      - (void)goOffline;

- `
  ``
  ``
  `

  ### [-goOnline](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDatabase#/c:objc(cs)FIRDatabase(im)goOnline)

  `
  `  
  Resumes the connection to the Firebase Database backend after a previous
  goOffline() call.  

  #### Declaration

  Objective-C  

      - (void)goOnline;

- `
  ``
  ``
  `

  ### [persistenceEnabled](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDatabase#/c:objc(cs)FIRDatabase(py)persistenceEnabled)

  `
  `  
  The Firebase Database client will cache synchronized data and keep track of
  all writes you've initiated while your application is running. It seamlessly
  handles intermittent network connections and re-sends write operations when
  the network connection is restored.

  However by default your write operations and cached data are only stored
  in-memory and will be lost when your app restarts. By setting this value to
  `true`, the data will be persisted to on-device (disk) storage and will thus
  be available again when the app is restarted (even when there is no network
  connectivity at that time). Note that this property must be set before
  creating your first `DatabaseReference` and only needs to be called once per
  application.  

  #### Declaration

  Objective-C  

      @property (nonatomic) BOOL persistenceEnabled;

- `
  ``
  ``
  `

  ### [persistenceCacheSizeBytes](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDatabase#/c:objc(cs)FIRDatabase(py)persistenceCacheSizeBytes)

  `
  `  
  By default the Firebase Database client will use up to 10MB of disk space to
  cache data. If the cache grows beyond this size, the client will start
  removing data that hasn't been recently used. If you find that your
  application caches too little or too much data, call this method to change
  the cache size. This property must be set before creating your first
  `DatabaseReference` and only needs to be called once per application.

  Note that the specified cache size is only an approximation and the size on
  disk may temporarily exceed it at times. Cache sizes smaller than 1 MB or
  greater than 100 MB are not supported.  

  #### Declaration

  Objective-C  

      @property (nonatomic) NSUInteger persistenceCacheSizeBytes;

- `
  ``
  ``
  `

  ### [callbackQueue](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDatabase#/c:objc(cs)FIRDatabase(py)callbackQueue)

  `
  `  
  Sets the dispatch queue on which all events are raised. The default queue is
  the main queue.

  Note that this must be set before creating your first Database reference.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong) dispatch_queue_t _Nonnull callbackQueue;

- `
  ``
  ``
  `

  ### [+setLoggingEnabled:](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDatabase#/c:objc(cs)FIRDatabase(cm)setLoggingEnabled:)

  `
  `  
  Enables verbose diagnostic logging.  

  #### Declaration

  Objective-C  

      + (void)setLoggingEnabled:(BOOL)enabled;

  #### Parameters

  |-----------------|-------------------------------------------|
  | ` `*enabled*` ` | true to enable logging, false to disable. |

- `
  ``
  ``
  `

  ### [+sdkVersion](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDatabase#/c:objc(cs)FIRDatabase(cm)sdkVersion)

  `
  `  
  Retrieve the Firebase Database SDK version.  

  #### Declaration

  Objective-C  

      + (nonnull NSString *)sdkVersion;

- `
  ``
  ``
  `

  ### [-useEmulatorWithHost:port:](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDatabase#/c:objc(cs)FIRDatabase(im)useEmulatorWithHost:port:)

  `
  `  
  Configures the database to use an emulated backend instead of the default
  remote backend.  

  #### Declaration

  Objective-C  

      - (void)useEmulatorWithHost:(nonnull NSString *)host port:(NSInteger)port;