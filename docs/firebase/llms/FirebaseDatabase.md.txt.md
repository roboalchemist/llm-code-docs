# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase.md.txt

# FirebaseDatabase

public class **FirebaseDatabase** extends Object  
The entry point for accessing a Firebase Database. You can get an instance by calling `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase#getInstance()`. To access a location in the database and read or write data, use
`https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase#getReference()`.

### Public Method Summary

|---|---|
| [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) | [getApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase#getApp())() Returns the FirebaseApp instance to which this FirebaseDatabase belongs. |
| static [FirebaseDatabase](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase) | [getInstance](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase#getInstance(java.lang.String))(String url) Gets a FirebaseDatabase instance for the specified URL. |
| static [FirebaseDatabase](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase) | [getInstance](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase#getInstance())() Gets the default FirebaseDatabase instance. |
| static [FirebaseDatabase](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase) | [getInstance](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase#getInstance(com.google.firebase.FirebaseApp))([FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) app) Gets an instance of FirebaseDatabase for a specific FirebaseApp. |
| synchronized static [FirebaseDatabase](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase) | [getInstance](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase#getInstance(com.google.firebase.FirebaseApp, java.lang.String))([FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) app, String url) Gets a FirebaseDatabase instance for the specified URL, using the specified FirebaseApp. |
| [DatabaseReference](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference) | [getReference](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase#getReference())() Gets a DatabaseReference for the database root node. |
| [DatabaseReference](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference) | [getReference](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase#getReference(java.lang.String))(String path) Gets a DatabaseReference for the provided path. |
| [DatabaseReference](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference) | [getReferenceFromUrl](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase#getReferenceFromUrl(java.lang.String))(String url) Gets a DatabaseReference for the provided URL. |
| static String | [getSdkVersion](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase#getSdkVersion())() |
| void | [goOffline](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase#goOffline())() Shuts down our connection to the Firebase Database backend until `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase#goOnline()` is called. |
| void | [goOnline](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase#goOnline())() Resumes our connection to the Firebase Database backend after a previous `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase#goOffline()` call. |
| void | [purgeOutstandingWrites](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase#purgeOutstandingWrites())() The Firebase Database client automatically queues writes and sends them to the server at the earliest opportunity, depending on network connectivity. |
| void | [setPersistenceCacheSizeBytes](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase#setPersistenceCacheSizeBytes(long))(long cacheSizeInBytes) By default Firebase Database will use up to 10MB of disk space to cache data. |
| synchronized void | [setPersistenceEnabled](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase#setPersistenceEnabled(boolean))(boolean isEnabled) The Firebase Database client will cache synchronized data and keep track of all writes you've initiated while your application is running. |

### Inherited Method Summary

From class java.lang.Object

|---|---|
| Object | clone() |
| boolean | equals(Object arg0) |
| void | finalize() |
| final Class\<?\> | getClass() |
| int | hashCode() |
| final void | notify() |
| final void | notifyAll() |
| String | toString() |
| final void | wait(long arg0, int arg1) |
| final void | wait(long arg0) |
| final void | wait() |

## Public Methods

#### public [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp)
**getApp**
()

Returns the FirebaseApp instance to which this FirebaseDatabase belongs.

##### Returns

- The FirebaseApp instance to which this FirebaseDatabase belongs.

#### public static [FirebaseDatabase](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase)
**getInstance**
(String url)

Gets a FirebaseDatabase instance for the specified URL.

##### Parameters

| url | The URL to the Firebase Database instance you want to access. |
|---|---|

##### Returns

- A FirebaseDatabase instance.

#### public static [FirebaseDatabase](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase)
**getInstance**
()

Gets the default FirebaseDatabase instance.

##### Returns

- A FirebaseDatabase instance.

#### public static [FirebaseDatabase](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase)
**getInstance**
([FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) app)

Gets an instance of FirebaseDatabase for a specific FirebaseApp.

##### Parameters

| app | The FirebaseApp to get a FirebaseDatabase for. |
|---|---|

##### Returns

- A FirebaseDatabase instance.

#### public static synchronized [FirebaseDatabase](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase)
**getInstance**
([FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) app, String url)

Gets a FirebaseDatabase instance for the specified URL, using the specified FirebaseApp.

##### Parameters

| app | The FirebaseApp to get a FirebaseDatabase for. |
| url | The URL to the Firebase Database instance you want to access. |
|---|---|

##### Returns

- A FirebaseDatabase instance.

#### public [DatabaseReference](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference)
**getReference**
()

Gets a DatabaseReference for the database root node.

##### Returns

- A DatabaseReference pointing to the root node.

#### public [DatabaseReference](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference)
**getReference**
(String path)

Gets a DatabaseReference for the provided path.

##### Parameters

| path | Path to a location in your FirebaseDatabase. |
|---|---|

##### Returns

- A DatabaseReference pointing to the specified path.

#### public [DatabaseReference](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference)
**getReferenceFromUrl**
(String url)

Gets a DatabaseReference for the provided URL. The URL must be a URL to a path within this
FirebaseDatabase. To create a DatabaseReference to a different database, create a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp` with a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions` object configured with the appropriate database
URL.

##### Parameters

| url | A URL to a path within your database. |
|---|---|

##### Returns

- A DatabaseReference for the provided URL.

#### public static String
**getSdkVersion**
()

<br />

##### Returns

- The version for this build of the Firebase Database client

#### public void
**goOffline**
()

Shuts down our connection to the Firebase Database backend until `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase#goOnline()` is called.

#### public void
**goOnline**
()

Resumes our connection to the Firebase Database backend after a previous `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase#goOffline()`
call.

#### public void
**purgeOutstandingWrites**
()

The Firebase Database client automatically queues writes and sends them to the server at the
earliest opportunity, depending on network connectivity. In some cases (e.g. offline usage)
there may be a large number of writes waiting to be sent. Calling this method will purge all
outstanding writes so they are abandoned.

All writes will be purged, including transactions and `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#onDisconnect()`
writes. The writes will be rolled back locally, perhaps triggering events for affected event
listeners, and the client will not (re-)send them to the Firebase backend.

#### public void
**setPersistenceCacheSizeBytes**
(long cacheSizeInBytes)

By default Firebase Database will use up to 10MB of disk space to cache data. If the cache
grows beyond this size, Firebase Database will start removing data that hasn't been recently
used. If you find that your application caches too little or too much data, call this method to
change the cache size. This method must be called before creating your first Database reference
and only needs to be called once per application.

Note that the specified cache size is only an approximation and the size on disk may
temporarily exceed it at times. Cache sizes smaller than 1 MB or greater than 100 MB are not
supported.

##### Parameters

| cacheSizeInBytes | The new size of the cache in bytes. |
|---|---|

#### public synchronized void
**setPersistenceEnabled**
(boolean isEnabled)

The Firebase Database client will cache synchronized data and keep track of all writes you've
initiated while your application is running. It seamlessly handles intermittent network
connections and re-sends write operations when the network connection is restored.

However by default your write operations and cached data are only stored in-memory and will
be lost when your app restarts. By setting this value to `true`, the data will be
persisted to on-device (disk) storage and will thus be available again when the app is
restarted (even when there is no network connectivity at that time). Note that this method
must be called before creating your first Database reference and only needs to be called once
per application.

##### Parameters

| isEnabled | Set to true to enable disk persistence, set to false to disable it. |
|---|---|