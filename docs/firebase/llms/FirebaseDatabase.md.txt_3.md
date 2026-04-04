# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase.md.txt

# FirebaseDatabase

# FirebaseDatabase


```
class FirebaseDatabase
```

<br />

*** ** * ** ***

The entry point for accessing a Firebase Database. You can get an instance by calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase#getInstance()`. To access a location in the database and read or write data, use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase#getReference()`.

## Summary

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase#getInstance()()` Gets the default FirebaseDatabase instance. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase#getInstance(com.google.firebase.FirebaseApp)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` Gets an instance of FirebaseDatabase for a specific FirebaseApp. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase#getInstance(java.lang.String)(url: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Gets a FirebaseDatabase instance for the specified URL. |
| `synchronized java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase#getInstance(com.google.firebase.FirebaseApp,java.lang.String)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp, url: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Gets a FirebaseDatabase instance for the specified URL, using the specified FirebaseApp. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase#getReference()()` Gets a DatabaseReference for the database root node. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase#getReference(java.lang.String)(path: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Gets a DatabaseReference for the provided path. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase#getReferenceFromUrl(java.lang.String)(url: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Gets a DatabaseReference for the provided URL. |
| `java-static https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase#getSdkVersion()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase#goOffline()()` Shuts down our connection to the Firebase Database backend until `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase#goOnline()` is called. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase#goOnline()()` Resumes our connection to the Firebase Database backend after a previous `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase#goOffline()` call. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase#purgeOutstandingWrites()()` The Firebase Database client automatically queues writes and sends them to the server at the earliest opportunity, depending on network connectivity. |
| `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase#setLogLevel(com.google.firebase.database.Logger.Level)(logLevel: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Logger.Level)` By default, this is set to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Logger.Level#INFO`. |
| `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase#setPersistenceCacheSizeBytes(long)(cacheSizeInBytes: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` By default Firebase Database will use up to 10MB of disk space to cache data. |
| `synchronized https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase#setPersistenceEnabled(boolean)(isEnabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` The Firebase Database client will cache synchronized data and keep track of all writes you've initiated while your application is running. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase#useEmulator(java.lang.String,int)(host: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, port: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Modifies this FirebaseDatabase instance to communicate with the Realtime Database emulator. |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase#app()` |

## Public functions

### getInstance

```
java-static fun getInstance(): FirebaseDatabase
```

Gets the default FirebaseDatabase instance.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase` | A FirebaseDatabase instance. |

### getInstance

```
java-static fun getInstance(app: FirebaseApp): FirebaseDatabase
```

Gets an instance of FirebaseDatabase for a specific FirebaseApp.

| Parameters |
|---|---|
| `app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | The FirebaseApp to get a FirebaseDatabase for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase` | A FirebaseDatabase instance. |

### getInstance

```
java-static fun getInstance(url: String): FirebaseDatabase
```

Gets a FirebaseDatabase instance for the specified URL.

| Parameters |
|---|---|
| `url: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The URL to the Firebase Database instance you want to access. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase` | A FirebaseDatabase instance. |

### getInstance

```
synchronized java-static fun getInstance(app: FirebaseApp, url: String): FirebaseDatabase
```

Gets a FirebaseDatabase instance for the specified URL, using the specified FirebaseApp.

| Parameters |
|---|---|
| `app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | The FirebaseApp to get a FirebaseDatabase for. |
| `url: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The URL to the Firebase Database instance you want to access. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase` | A FirebaseDatabase instance. |

### getReference

```
fun getReference(): DatabaseReference
```

Gets a DatabaseReference for the database root node.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference` | A DatabaseReference pointing to the root node. |

### getReference

```
fun getReference(path: String): DatabaseReference
```

Gets a DatabaseReference for the provided path.

| Parameters |
|---|---|
| `path: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Path to a location in your FirebaseDatabase. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference` | A DatabaseReference pointing to the specified path. |

### getReferenceFromUrl

```
fun getReferenceFromUrl(url: String): DatabaseReference
```

Gets a DatabaseReference for the provided URL. The URL must be a URL to a path within this FirebaseDatabase. To create a DatabaseReference to a different database, create a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` with a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions` object configured with the appropriate database URL.

| Parameters |
|---|---|
| `url: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A URL to a path within your database. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference` | A DatabaseReference for the provided URL. |

### getSdkVersion

```
java-static fun getSdkVersion(): String
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The semver version for this build of the Firebase Database client |

### goOffline

```
fun goOffline(): Unit
```

Shuts down our connection to the Firebase Database backend until `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase#goOnline()` is called.

### goOnline

```
fun goOnline(): Unit
```

Resumes our connection to the Firebase Database backend after a previous `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/FirebaseDatabase#goOffline()` call.

### purgeOutstandingWrites

```
fun purgeOutstandingWrites(): Unit
```

The Firebase Database client automatically queues writes and sends them to the server at the earliest opportunity, depending on network connectivity. In some cases (e.g. offline usage) there may be a large number of writes waiting to be sent. Calling this method will purge all outstanding writes so they are abandoned.

All writes will be purged, including transactions and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#onDisconnect()` writes. The writes will be rolled back locally, perhaps triggering events for affected event listeners, and the client will not (re-)send them to the Firebase backend.

### setLogLevel

```
synchronized fun setLogLevel(logLevel: Logger.Level): Unit
```

By default, this is set to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Logger.Level#INFO`. This includes any internal errors (`https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Logger.Level#ERROR`) and any security debug messages (`https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Logger.Level#INFO`) that the client receives. Set to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Logger.Level#DEBUG` to turn on the diagnostic logging, and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Logger.Level#NONE` to disable all logging.

| Parameters |
|---|---|
| `logLevel: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Logger.Level` | The desired minimum log level |

### setPersistenceCacheSizeBytes

```
synchronized fun setPersistenceCacheSizeBytes(cacheSizeInBytes: Long): Unit
```

By default Firebase Database will use up to 10MB of disk space to cache data. If the cache grows beyond this size, Firebase Database will start removing data that hasn't been recently used. If you find that your application caches too little or too much data, call this method to change the cache size. This method must be called before creating your first Database reference and only needs to be called once per application.

Note that the specified cache size is only an approximation and the size on disk may temporarily exceed it at times. Cache sizes smaller than 1 MB or greater than 100 MB are not supported.

| Parameters |
|---|---|
| `cacheSizeInBytes: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The new size of the cache in bytes. |

### setPersistenceEnabled

```
synchronized fun setPersistenceEnabled(isEnabled: Boolean): Unit
```

The Firebase Database client will cache synchronized data and keep track of all writes you've initiated while your application is running. It seamlessly handles intermittent network connections and re-sends write operations when the network connection is restored.

However by default your write operations and cached data are only stored in-memory and will be lost when your app restarts. By setting this value to \`true\`, the data will be persisted to on-device (disk) storage and will thus be available again when the app is restarted (even when there is no network connectivity at that time). Note that this method must be called before creating your first Database reference and only needs to be called once per application.

| Parameters |
|---|---|
| `isEnabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | Set to true to enable disk persistence, set to false to disable it. |

### useEmulator

```
fun useEmulator(host: String, port: Int): Unit
```

Modifies this FirebaseDatabase instance to communicate with the Realtime Database emulator.

Note: Call this method before using the instance to do any database operations.

| Parameters |
|---|---|
| `host: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the emulator host (for example, 10.0.2.2) |
| `port: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | the emulator port (for example, 9000) |

## Public properties

### app

```
val app: FirebaseApp!
```