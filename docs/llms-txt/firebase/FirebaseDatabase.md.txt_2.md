# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase.md.txt

# FirebaseDatabase

# FirebaseDatabase


```
public class FirebaseDatabase
```

<br />

*** ** * ** ***

The entry point for accessing a Firebase Database. You can get an instance by calling `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase#getInstance()`. To access a location in the database and read or write data, use `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase#getReference()`.

## Summary

| ### Public fields |
|---|---|
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase#app()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase#getApp()()` Returns the FirebaseApp instance to which this FirebaseDatabase belongs. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase#getInstance()()` Gets the default FirebaseDatabase instance. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase#getInstance(com.google.firebase.FirebaseApp)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app)` Gets an instance of FirebaseDatabase for a specific FirebaseApp. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase#getInstance(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html url)` Gets a FirebaseDatabase instance for the specified URL. |
| `synchronized static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase#getInstance(com.google.firebase.FirebaseApp,java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html url)` Gets a FirebaseDatabase instance for the specified URL, using the specified FirebaseApp. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase#getReference()()` Gets a DatabaseReference for the database root node. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase#getReference(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html path)` Gets a DatabaseReference for the provided path. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase#getReferenceFromUrl(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html url)` Gets a DatabaseReference for the provided URL. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase#getSdkVersion()()` |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase#goOffline()()` Shuts down our connection to the Firebase Database backend until `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase#goOnline()` is called. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase#goOnline()()` Resumes our connection to the Firebase Database backend after a previous `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase#goOffline()` call. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase#purgeOutstandingWrites()()` The Firebase Database client automatically queues writes and sends them to the server at the earliest opportunity, depending on network connectivity. |
| `synchronized void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase#setLogLevel(com.google.firebase.database.Logger.Level)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Logger.Level logLevel)` By default, this is set to `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Logger.Level#INFO`. |
| `synchronized void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase#setPersistenceCacheSizeBytes(long)(long cacheSizeInBytes)` By default Firebase Database will use up to 10MB of disk space to cache data. |
| `synchronized void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase#setPersistenceEnabled(boolean)(boolean isEnabled)` The Firebase Database client will cache synchronized data and keep track of all writes you've initiated while your application is running. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase#useEmulator(java.lang.String,int)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html host, int port)` Modifies this FirebaseDatabase instance to communicate with the Realtime Database emulator. |

## Public fields

### app

```
public final FirebaseApp app
```

## Public methods

### getApp

```
public @NonNull FirebaseApp getApp()
```

Returns the FirebaseApp instance to which this FirebaseDatabase belongs.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` | The FirebaseApp instance to which this FirebaseDatabase belongs. |

### getInstance

```
public static @NonNull FirebaseDatabase getInstance()
```

Gets the default FirebaseDatabase instance.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` | A FirebaseDatabase instance. |

### getInstance

```
public static @NonNull FirebaseDatabase getInstance(@NonNull FirebaseApp app)
```

Gets an instance of FirebaseDatabase for a specific FirebaseApp.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app` | The FirebaseApp to get a FirebaseDatabase for. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` | A FirebaseDatabase instance. |

### getInstance

```
public static @NonNull FirebaseDatabase getInstance(@NonNull String url)
```

Gets a FirebaseDatabase instance for the specified URL.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html url` | The URL to the Firebase Database instance you want to access. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` | A FirebaseDatabase instance. |

### getInstance

```
synchronized public static @NonNull FirebaseDatabase getInstance(@NonNull FirebaseApp app, @NonNull String url)
```

Gets a FirebaseDatabase instance for the specified URL, using the specified FirebaseApp.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app` | The FirebaseApp to get a FirebaseDatabase for. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html url` | The URL to the Firebase Database instance you want to access. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase` | A FirebaseDatabase instance. |

### getReference

```
public @NonNull DatabaseReference getReference()
```

Gets a DatabaseReference for the database root node.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference` | A DatabaseReference pointing to the root node. |

### getReference

```
public @NonNull DatabaseReference getReference(@NonNull String path)
```

Gets a DatabaseReference for the provided path.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html path` | Path to a location in your FirebaseDatabase. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference` | A DatabaseReference pointing to the specified path. |

### getReferenceFromUrl

```
public @NonNull DatabaseReference getReferenceFromUrl(@NonNull String url)
```

Gets a DatabaseReference for the provided URL. The URL must be a URL to a path within this FirebaseDatabase. To create a DatabaseReference to a different database, create a `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` with a `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions` object configured with the appropriate database URL.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html url` | A URL to a path within your database. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference` | A DatabaseReference for the provided URL. |

### getSdkVersion

```
public static @NonNull String getSdkVersion()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | The semver version for this build of the Firebase Database client |

### goOffline

```
public void goOffline()
```

Shuts down our connection to the Firebase Database backend until `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase#goOnline()` is called.

### goOnline

```
public void goOnline()
```

Resumes our connection to the Firebase Database backend after a previous `https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase#goOffline()` call.

### purgeOutstandingWrites

```
public void purgeOutstandingWrites()
```

The Firebase Database client automatically queues writes and sends them to the server at the earliest opportunity, depending on network connectivity. In some cases (e.g. offline usage) there may be a large number of writes waiting to be sent. Calling this method will purge all outstanding writes so they are abandoned.

All writes will be purged, including transactions and `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#onDisconnect()` writes. The writes will be rolled back locally, perhaps triggering events for affected event listeners, and the client will not (re-)send them to the Firebase backend.

### setLogLevel

```
synchronized public void setLogLevel(@NonNull Logger.Level logLevel)
```

By default, this is set to `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Logger.Level#INFO`. This includes any internal errors (`https://firebase.google.com/docs/reference/android/com/google/firebase/database/Logger.Level#ERROR`) and any security debug messages (`https://firebase.google.com/docs/reference/android/com/google/firebase/database/Logger.Level#INFO`) that the client receives. Set to `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Logger.Level#DEBUG` to turn on the diagnostic logging, and `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Logger.Level#NONE` to disable all logging.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/Logger.Level logLevel` | The desired minimum log level |

### setPersistenceCacheSizeBytes

```
synchronized public void setPersistenceCacheSizeBytes(long cacheSizeInBytes)
```

By default Firebase Database will use up to 10MB of disk space to cache data. If the cache grows beyond this size, Firebase Database will start removing data that hasn't been recently used. If you find that your application caches too little or too much data, call this method to change the cache size. This method must be called before creating your first Database reference and only needs to be called once per application.

Note that the specified cache size is only an approximation and the size on disk may temporarily exceed it at times. Cache sizes smaller than 1 MB or greater than 100 MB are not supported.

| Parameters |
|---|---|
| `long cacheSizeInBytes` | The new size of the cache in bytes. |

### setPersistenceEnabled

```
synchronized public void setPersistenceEnabled(boolean isEnabled)
```

The Firebase Database client will cache synchronized data and keep track of all writes you've initiated while your application is running. It seamlessly handles intermittent network connections and re-sends write operations when the network connection is restored.

However by default your write operations and cached data are only stored in-memory and will be lost when your app restarts. By setting this value to \`true\`, the data will be persisted to on-device (disk) storage and will thus be available again when the app is restarted (even when there is no network connectivity at that time). Note that this method must be called before creating your first Database reference and only needs to be called once per application.

| Parameters |
|---|---|
| `boolean isEnabled` | Set to true to enable disk persistence, set to false to disable it. |

### useEmulator

```
public void useEmulator(@NonNull String host, int port)
```

Modifies this FirebaseDatabase instance to communicate with the Realtime Database emulator.

Note: Call this method before using the instance to do any database operations.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html host` | the emulator host (for example, 10.0.2.2) |
| `int port` | the emulator port (for example, 9000) |