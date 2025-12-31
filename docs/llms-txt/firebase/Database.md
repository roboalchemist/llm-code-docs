# Source: https://firebase.google.com/docs/reference/swift/firebasedatabaseswift/api/reference/Extensions/Database.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database.md.txt

# FirebaseDatabase Framework Reference

# Database

    class Database : NSObject

The entry point for accessing a Firebase Database. You can get an instance
by calling [Database.database()](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database.html#/c:objc(cs)FIRDatabase(cm)database). To access a location in the database and
read or write data, use `FIRDatabase.reference()`.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database#/c:objc(cs)FIRDatabase(im)init)

  `
  `  
  Unavailable

  use the database method instead  
  The NSObject initializer that has been marked as unavailable. Use the
  `database` class method instead.
- `
  ``
  ``
  `

  ### [database()](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database#/c:objc(cs)FIRDatabase(cm)database)

  `
  `  
  Gets the instance of `Database` for the default `FirebaseApp`.  

  #### Declaration

  Swift  

      class func database() -> Database

  #### Return Value

  A `Database` instance.
- `
  ``
  ``
  `

  ### [database(url:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database#/c:objc(cs)FIRDatabase(cm)databaseWithURL:)

  `
  `  
  Gets a `Database` instance for the specified URL.  

  #### Declaration

  Swift  

      class func database(url: String) -> Database

  #### Parameters

  |-------------|---------------------------------------------------------------|
  | ` `*url*` ` | The URL to the Firebase Database instance you want to access. |

  #### Return Value

  A `Database` instance.
- `
  ``
  ``
  `

  ### [database(app:url:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database#/c:objc(cs)FIRDatabase(cm)databaseForApp:URL:)

  `
  `  
  Gets a `Database` instance for the specified URL, using the specified
  `FirebaseApp`.  

  #### Declaration

  Swift  

      class func database(app: FIRApp, url: String) -> Database

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

  ### [database(app:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database#/c:objc(cs)FIRDatabase(cm)databaseForApp:)

  `
  `  
  Gets an instance of `Database` for a specific `FirebaseApp`.  

  #### Declaration

  Swift  

      class func database(app: FIRApp) -> Database

  #### Parameters

  |-------------|----------------------------------|
  | ` `*app*` ` | The app to get a `Database` for. |

  #### Return Value

  A `Database` instance.
- `
  ``
  ``
  `

  ### [app](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database#/c:objc(cs)FIRDatabase(py)app)

  `
  `  
  The app instance to which this `Database` belongs.  

  #### Declaration

  Swift  

      weak var app: FIRApp? { get }

- `
  ``
  ``
  `

  ### [reference()](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database#/c:objc(cs)FIRDatabase(im)reference)

  `
  `  
  Gets a [DatabaseReference](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseReference.html) for the root of your Firebase Database.  

  #### Declaration

  Swift  

      func reference() -> https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseReference.html

- `
  ``
  ``
  `

  ### [reference(withPath:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database#/c:objc(cs)FIRDatabase(im)referenceWithPath:)

  `
  `  
  Gets a [DatabaseReference](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseReference.html) for the provided path.  

  #### Declaration

  Swift  

      func reference(withPath path: String) -> https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseReference.html

  #### Parameters

  |--------------|-----------------------------------------------|
  | ` `*path*` ` | Path to a location in your Firebase Database. |

  #### Return Value

  A [DatabaseReference](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseReference.html) pointing to the specified path.
- `
  ``
  ``
  `

  ### [reference(fromURL:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database#/c:objc(cs)FIRDatabase(im)referenceFromURL:)

  `
  `  
  Gets a [DatabaseReference](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseReference.html) for the provided URL. The URL must be a URL to a
  path within this Firebase Database. To create a [DatabaseReference](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseReference.html) to a
  different database, create a `FirebaseApp` with an `Options` object
  configured with the appropriate database URL.  

  #### Declaration

  Swift  

      func reference(fromURL databaseUrl: String) -> https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseReference.html

  #### Parameters

  |---------------------|---------------------------------------|
  | ` `*databaseUrl*` ` | A URL to a path within your database. |

  #### Return Value

  A [DatabaseReference](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseReference.html) for the provided URL.
- `
  ``
  ``
  `

  ### [purgeOutstandingWrites()](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database#/c:objc(cs)FIRDatabase(im)purgeOutstandingWrites)

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

  Swift  

      func purgeOutstandingWrites()

- `
  ``
  ``
  `

  ### [goOffline()](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database#/c:objc(cs)FIRDatabase(im)goOffline)

  `
  `  
  Shuts down the connection to the Firebase Database backend until [goOnline()](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database.html#/c:objc(cs)FIRDatabase(im)goOnline)
  is called.  

  #### Declaration

  Swift  

      func goOffline()

- `
  ``
  ``
  `

  ### [goOnline()](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database#/c:objc(cs)FIRDatabase(im)goOnline)

  `
  `  
  Resumes the connection to the Firebase Database backend after a previous
  goOffline() call.  

  #### Declaration

  Swift  

      func goOnline()

- `
  ``
  ``
  `

  ### [isPersistenceEnabled](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database#/c:objc(cs)FIRDatabase(py)persistenceEnabled)

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
  creating your first [DatabaseReference](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseReference.html) and only needs to be called once per
  application.  

  #### Declaration

  Swift  

      var isPersistenceEnabled: Bool { get set }

- `
  ``
  ``
  `

  ### [persistenceCacheSizeBytes](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database#/c:objc(cs)FIRDatabase(py)persistenceCacheSizeBytes)

  `
  `  
  By default the Firebase Database client will use up to 10MB of disk space to
  cache data. If the cache grows beyond this size, the client will start
  removing data that hasn't been recently used. If you find that your
  application caches too little or too much data, call this method to change
  the cache size. This property must be set before creating your first
  [DatabaseReference](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DatabaseReference.html) and only needs to be called once per application.

  Note that the specified cache size is only an approximation and the size on
  disk may temporarily exceed it at times. Cache sizes smaller than 1 MB or
  greater than 100 MB are not supported.  

  #### Declaration

  Swift  

      var persistenceCacheSizeBytes: UInt { get set }

- `
  ``
  ``
  `

  ### [callbackQueue](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database#/c:objc(cs)FIRDatabase(py)callbackQueue)

  `
  `  
  Sets the dispatch queue on which all events are raised. The default queue is
  the main queue.

  Note that this must be set before creating your first Database reference.  

  #### Declaration

  Swift  

      var callbackQueue: dispatch_queue_t { get set }

- `
  ``
  ``
  `

  ### [setLoggingEnabled(_:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database#/c:objc(cs)FIRDatabase(cm)setLoggingEnabled:)

  `
  `  
  Enables verbose diagnostic logging.  

  #### Declaration

  Swift  

      class func setLoggingEnabled(_ enabled: Bool)

  #### Parameters

  |-----------------|-------------------------------------------|
  | ` `*enabled*` ` | true to enable logging, false to disable. |

- `
  ``
  ``
  `

  ### [sdkVersion()](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database#/c:objc(cs)FIRDatabase(cm)sdkVersion)

  `
  `  
  Retrieve the Firebase Database SDK version.  

  #### Declaration

  Swift  

      class func sdkVersion() -> String

- `
  ``
  ``
  `

  ### [useEmulator(withHost:port:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database#/c:objc(cs)FIRDatabase(im)useEmulatorWithHost:port:)

  `
  `  
  Configures the database to use an emulated backend instead of the default
  remote backend.  

  #### Declaration

  Swift  

      func useEmulator(withHost host: String, port: Int)

- `
  ``
  ``
  `

  ### [Encoder](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database#/s:So11FIRDatabaseC16FirebaseDatabaseE7Encodera)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      typealias Encoder = FirebaseDataEncoder

- `
  ``
  ``
  `

  ### [Decoder](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database#/s:So11FIRDatabaseC16FirebaseDatabaseE7Decodera)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      typealias Decoder = FirebaseDataDecoder