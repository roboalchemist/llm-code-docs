# Source: https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database.md.txt

# Firebase.Database.FirebaseDatabase Class Reference

# Firebase.Database.FirebaseDatabase

The entry point for accessing a [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database).

## Summary

The entry point for accessing a [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database). You can get an instance by calling [DefaultInstance](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database_1ab5e0767658d246776a04aeea58bdaae4) . To access a location in the database and read or write data, use [GetReference()](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database_1a14abf592cc102d221661588fcd21ad50)

|                                                                                                                                                                                                                                                                                                                                                                   ### Properties                                                                                                                                                                                                                                                                                                                                                                   ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [App](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database_1adcba0cbc5fd041982f20dff4db3c72b2)             | [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) Returns the [Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) instance to which this [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) belongs.                                                                  |
| [DefaultInstance](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database_1ab5e0767658d246776a04aeea58bdaae4) | `static `[FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) Gets the instance of [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) for the default Firebase.App.                                                                                                                                                  |
| [LogLevel](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database_1ac643cbd7988989fb84fdec82adc10547)        | [LogLevel](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase_1ae165d1d7bc3d85e1c0463a2a1d9ced9a) By default, this is set to [Info](https://firebase.google.com/docs/reference/unity/other/) This includes any internal errors ( [Error](https://firebase.google.com/docs/reference/unity/other/) ) and any security debug messages ( [Info](https://firebase.google.com/docs/reference/unity/other/) ) that the client receives.                                                                          |
| [RootReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database_1a62a38edd5fa1c1f7308ff77bf1c7296b)   | [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) Gets a [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) for the root location of this [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database). |

|                                                                                                                                                                                                                                                                                                                                                                                                                 ### Public static functions                                                                                                                                                                                                                                                                                                                                                                                                                 ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GetInstance](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database_1a3c53b60af753c05ee54b4d60a47c1f28)`(`[FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)` app)`             | [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) Gets an instance of [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) for a specific [Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app). |
| [GetInstance](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database_1a09a327124d0bdf5bab77e49bf531eedd)`(String url)`                                                                                                                                    | [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) Gets an instance of [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) for the specified URL.                                                                                                                               |
| [GetInstance](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database_1a70c6f2332980a8a5b5b77db47a2254ce)`(`[FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)` app, String url)` | [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) Gets a [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) instance for the specified URL, using the specified FirebsaeApp.                                                                                                  |

|                                                                                                                                                                                                                                                                                                                                                  ### Public functions                                                                                                                                                                                                                                                                                                                                                   ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GetReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database_1a14abf592cc102d221661588fcd21ad50)`(string path)`           | [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) Gets a [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) for the provided path.                                                                                                                         |
| [GetReferenceFromUrl](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database_1a9c24d7992b955ab76603336895b054d4)`(Uri url)`        | [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) Gets a [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) for the provided URL.                                                                                                                          |
| [GetReferenceFromUrl](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database_1a15300a09c4ed1ab1de7a0976b0e48257)`(string url)`     | [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) Gets a [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) for the provided URL.                                                                                                                          |
| [GoOffline](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database_1a016f3d989495f55c1bacb74a688f29c6)`()`                         | `void` Shuts down our connection to the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) backend until [GoOnline()](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database_1a999af2e5c582df66be287cd3029badd1) is called.     |
| [GoOnline](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database_1a999af2e5c582df66be287cd3029badd1)`()`                          | `void` Resumes our connection to the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) backend after a previous [GoOffline()](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database_1a016f3d989495f55c1bacb74a688f29c6) Call. |
| [PurgeOutstandingWrites](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database_1a875f2d34051a803371b52698cdf0387c)`()`            | `void` The [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) client automatically queues writes and sends them to the server at the earliest opportunity, depending on network connectivity.                                                                                                                         |
| [SetPersistenceEnabled](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database_1ac8f14e1025014f9255781de704e013ae)`(bool enabled)` | `void` Sets whether pending write data will persist between application exits.                                                                                                                                                                                                                                                                                                                                                                                                                |

## Properties

### App

```c#
FirebaseApp App
```  
Returns the [Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) instance to which this [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) belongs.

<br />

|                                                                                                                                                                        Details                                                                                                                                                                         ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The [Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) instance to which this [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) belongs. |

### DefaultInstance

```c#
static FirebaseDatabase DefaultInstance
```  
Gets the instance of [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) for the default Firebase.App.

A [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) instance.  

### LogLevel

```c#
LogLevel LogLevel
```  
By default, this is set to [Info](https://firebase.google.com/docs/reference/unity/other/) This includes any internal errors ( [Error](https://firebase.google.com/docs/reference/unity/other/) ) and any security debug messages ( [Info](https://firebase.google.com/docs/reference/unity/other/) ) that the client receives.

Set to [Debug](https://firebase.google.com/docs/reference/unity/other/) to turn on the diagnostic logging.

On Android this can only be set before any operations have been performed with the object.

The desired minimum log level  

### RootReference

```c#
DatabaseReference RootReference
```  
Gets a [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) for the root location of this [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database).

A [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) instance.

## Public static functions

### GetInstance

```c#
FirebaseDatabase GetInstance(
  FirebaseApp app
)
```  
Gets an instance of [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) for a specific [Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app).

<br />

|                                                                                                                                                                                                                                                                                                                                       Details                                                                                                                                                                                                                                                                                                                                        ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `app` | The [Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) to get a [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) for. | |
| **Returns** | A [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

### GetInstance

```c#
FirebaseDatabase GetInstance(
  String url
)
```  
Gets an instance of [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) for the specified URL.

<br />

|                                                                                                                                                                                                                                                                                      Details                                                                                                                                                                                                                                                                                       ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `url` | The URL to the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) instance you want to access. | |
| **Returns** | A [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) instance.                                                                                                                                                                                                                                                                                                                                                                                          |

### GetInstance

```c#
FirebaseDatabase GetInstance(
  FirebaseApp app,
  String url
)
```  
Gets a [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) instance for the specified URL, using the specified FirebsaeApp.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `app` | The [Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) to get a [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) for. | | `url` | The URL to the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) instance you want to access.                                                  | |
| **Returns** | A [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database) instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## Public functions

### GetReference

```c#
DatabaseReference GetReference(
  string path
)
```  
Gets a [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) for the provided path.

<br />

|                                                                                                                                                                                                             Details                                                                                                                                                                                                              ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `path` | Path to a location in your [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database). | |
| **Returns** | A [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) pointing to the specified path.                                                                                                                                                                                                               |

### GetReferenceFromUrl

```c#
DatabaseReference GetReferenceFromUrl(
  Uri url
)
```  
Gets a [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) for the provided URL.

Gets a [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) for the provided URL. The URL must be a URL to a path within this [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database). To create a [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) to a different database, create a [Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) with a Firebase.FirebaseOptions

object configured with the appropriate database URL.

<br />

|                                                                                                 Details                                                                                                  ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|---------------------------------------| | `url` | A URL to a path within your database. |                                                                                         |
| **Returns** | A [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) for the provided URL. |

### GetReferenceFromUrl

```c#
DatabaseReference GetReferenceFromUrl(
  string url
)
```  
Gets a [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) for the provided URL.

Gets a [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) for the provided URL. The URL must be a URL to a path within this [FirebaseDatabase](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database). To create a [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) to a different database, create a [Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) with a Firebase.FirebaseOptions

object configured with the appropriate database URL.

<br />

|                                                                                                 Details                                                                                                  ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|---------------------------------------| | `url` | A URL to a path within your database. |                                                                                         |
| **Returns** | A [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference) for the provided URL. |

### GoOffline

```c#
void GoOffline()
```  
Shuts down our connection to the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) backend until [GoOnline()](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database_1a999af2e5c582df66be287cd3029badd1) is called.  

### GoOnline

```c#
void GoOnline()
```  
Resumes our connection to the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) backend after a previous [GoOffline()](https://firebase.google.com/docs/reference/unity/class/firebase/database/firebase-database#class_firebase_1_1_database_1_1_firebase_database_1a016f3d989495f55c1bacb74a688f29c6) Call.  

### PurgeOutstandingWrites

```c#
void PurgeOutstandingWrites()
```  
The [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) client automatically queues writes and sends them to the server at the earliest opportunity, depending on network connectivity.

The [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) client automatically queues writes and sends them to the server at the earliest opportunity, depending on network connectivity. In some cases (e.g. offline usage) there may be a large number of writes waiting to be sent. Calling this method will purge all outstanding writes so they are abandoned. All writes will be purged, including transactions and [DatabaseReference.OnDisconnect()](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference_1a34b15ad902d14db74fc767dc4560b699) writes. The writes will be rolled back locally, perhaps triggering events for affected event listeners, and the client will not (re-)send them to the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) backend.  

### SetPersistenceEnabled

```c#
void SetPersistenceEnabled(
  bool enabled
)
```  
Sets whether pending write data will persist between application exits.

The [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) client will cache synchronized data and keep track of all writes you've initiated while your application is running. It seamlessly handles intermittent network connections and re-sends write operations when the network connection is restored. However by default your write operations and cached data are only stored in-memory and will be lost when your app restarts. By setting this value to true, the data will be persisted to on-device (disk) storage and will thus be available again when the app is restarted (even when there is no network connectivity at that time).

Note:SetPersistenceEnabled should be called before creating any instances of [DatabaseReference](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#class_firebase_1_1_database_1_1_database_reference), and only needs to be called once per application.

<br />

|                                                                                                                                               Details                                                                                                                                               ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------|-----------------------------------------------------------------------------------------------------------------------------| | `enabled` | Set this to true to persist write data to on-device (disk) storage, or false to discard pending writes when the app exists. | |