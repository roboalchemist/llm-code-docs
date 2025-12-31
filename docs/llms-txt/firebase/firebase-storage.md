# Source: https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage.md.txt

# Firebase.Storage.FirebaseStorage

[FirebaseStorage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage)is a service that supports uploading and downloading large objects to Google Cloud[Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage).

## Summary

[FirebaseStorage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage)is a service that supports uploading and downloading large objects to Google Cloud[Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage). Pass a custom instance of[Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)to[GetInstance](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage_1a8a4cf4c5a660256ca31ca398d5680077)which will initialize it with a storage location (bucket) specified via[AppOptions.StorageBucket](https://firebase.google.com/docs/reference/unity/class/firebase/app-options#class_firebase_1_1_app_options_1ae4076f95925babcf7946ce8300c11485)

Otherwise, if you call[DefaultInstance](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage_1a8d7a0f2d42ba1479c2b1a179e7ce6eca)without a[FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app), the[FirebaseStorage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage)instance will initialize with the default[Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)obtainable from[FirebaseApp.DefaultInstance](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app_1abf8fab1b5c3d7a745b7d4fd933e5a0fd). The storage location in this case will come the JSON configuration file downloaded from the web.

|                                                                                                                                                                                                                                                                                                                                                   ### Properties                                                                                                                                                                                                                                                                                                                                                    ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [App](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage_1ad8b3d0df68802da38c8786e52271d61c)                   | [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) The[Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)associated with this[FirebaseStorage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage)instance.                                                   |
| [DefaultInstance](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage_1a8d7a0f2d42ba1479c2b1a179e7ce6eca)       | `static `[FirebaseStorage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage) Returns the[FirebaseStorage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage), initialized with the default[Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) |
| [LogLevel](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage_1a529dd50e105fc2a641e01a4cdc817132)              | [LogLevel](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase_1ae165d1d7bc3d85e1c0463a2a1d9ced9a) Sets or Gets how verbose Cloud[Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage)Logging will be.                                                                                                                                                                                                     |
| [MaxDownloadRetryTime](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage_1a695239fdc4c02b07c4f01a3822484bd1)  | `TimeSpan` Returns the maximum time to retry a download if a failure occurs.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [MaxOperationRetryTime](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage_1a0135c615d2a372ad5fece765c95f9c85) | `TimeSpan` Sets the maximum time to retry operations other than upload and download if a failure occurs.                                                                                                                                                                                                                                                                                                                                                                                                      |
| [MaxUploadRetryTime](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage_1a12c02bd2493bb86377c12dd736888709)    | `TimeSpan` Returns the maximum time to retry an upload if a failure occurs.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [RootReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage_1a1f1b34d16f458d6090bd4409d9dc9f02)         | [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) Creates a new[StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)initialized at the root Cloud[Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage)location.         |

|                                                                                                                                                                                                                                                                                                                                                                                                          ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                           ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GetReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage_1a1792cf963b5f1275e424f83392a8c047)`(string location)`       | [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) Creates a new[StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)initialized with a child Cloud[Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage)location.                                                                                                            |
| [GetReferenceFromUrl](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage_1a42867cc9a73277ca6a8ff92595dd1cdf)`(string fullUrl)` | [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) Creates a[StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)given a gs:// or<https://>URL pointing to a[Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage)location. |
| [Url](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage_1a33a4c5bcad67895c6cf12c9ddb5da7f5)`()`                               | `string` Returns a gs:// url to the Cloud[Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage)Bucket, or an empty string if this[Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage)was created with default parameters.                                                                                                                                                                                                                                                         |
| [UseEmulator](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage_1a8fd170db3f4e61c78667b69d5ca90bb1)`(string host, int port)`  | `void` Configures the[Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage)SDK to use an emulated backend instead of the default remote backend.                                                                                                                                                                                                                                                                                                                                                                                                   |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ### Public static functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GetInstance](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage_1a8a4cf4c5a660256ca31ca398d5680077)`(`[FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)` app, string url)` | [FirebaseStorage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage) Returns the[FirebaseStorage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage), initialized with a custom[Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)                                                                                                                                           |
| [GetInstance](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage_1a147cf2dfb55fcf76d59edb571bdd6b6e)`(string url)`                                                                                                                                    | [FirebaseStorage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage) Returns the[FirebaseStorage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage), initialized with the default[Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)and a custom[Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage)Bucket |

## Properties

### App

```c#
FirebaseApp App
```  
The[Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)associated with this[FirebaseStorage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage)instance.  

### DefaultInstance

```c#
static FirebaseStorage DefaultInstance
```  
Returns the[FirebaseStorage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage), initialized with the default[Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)

a[FirebaseStorage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage)instance.  

### LogLevel

```c#
LogLevel LogLevel
```  
Sets or Gets how verbose Cloud[Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage)Logging will be.

To obtain more debug information, set this toLogLevel.Verbose  

### MaxDownloadRetryTime

```c#
TimeSpan MaxDownloadRetryTime
```  
Returns the maximum time to retry a download if a failure occurs.

maximum time which defaults to 10 minutes (600,000 milliseconds).  

### MaxOperationRetryTime

```c#
TimeSpan MaxOperationRetryTime
```  
Sets the maximum time to retry operations other than upload and download if a failure occurs.  

### MaxUploadRetryTime

```c#
TimeSpan MaxUploadRetryTime
```  
Returns the maximum time to retry an upload if a failure occurs.

<br />

|                                      Details                                       ||
|-------------|-----------------------------------------------------------------------|
| **Returns** | the maximum time which defaults to 10 minutes (600,000 milliseconds). |

### RootReference

```c#
StorageReference RootReference
```  
Creates a new[StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)initialized at the root Cloud[Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage)location.

<br />

|                                                                                          Details                                                                                          ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | An instance of[StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) |

## Public functions

### GetReference

```c#
StorageReference GetReference(
  string location
)
```  
Creates a new[StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)initialized with a child Cloud[Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage)location.

<br />

|                                                                                                                  Details                                                                                                                   ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|-----------------------------------------------------------------------------------------------| | `location` | A relative path from the root to initialize the reference with, for instance "path/to/object" | |
| **Returns** | An instance of[StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)at the given child path.                          |

### GetReferenceFromUrl

```c#
StorageReference GetReferenceFromUrl(
  string fullUrl
)
```  
Creates a[StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)given a gs:// or<https://>URL pointing to a[Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage)location.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `fullUrl` | A gs:// or http\[s\]:// URL used to initialize the reference. For example, you can pass in a download URL retrieved from[StorageReference.GetDownloadUrlAsync](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference_1af5c73d78af7ccab6812cb0aaa2043ee4)or the uri retrieved from[StorageReference.ToString()](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference_1a2d3174e239a7d683ee338ca5f6ddbb1a)An error is thrown if fullUrl is not associated with the[Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)used to initialize this[FirebaseStorage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage) | |

### Url

```c#
string Url()
```  
Returns a gs:// url to the Cloud[Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage)Bucket, or an empty string if this[Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage)was created with default parameters.  

### UseEmulator

```c#
void UseEmulator(
  string host,
  int port
)
```  
Configures the[Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage)SDK to use an emulated backend instead of the default remote backend.

This method should be called before invoking any other methods on a new instance of[Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage)

<br />

|                                                                                                 Details                                                                                                  ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------|---------------------------------------------------| | `host` | The host that the storage emulator is running on. | | `port` | The port that the storage emulator is running on. | |

## Public static functions

### GetInstance

```c#
FirebaseStorage GetInstance(
  FirebaseApp app,
  string url
)
```  
Returns the[FirebaseStorage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage), initialized with a custom[Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)

<br />

|                                                                                                                                                                                                                                                                                Details                                                                                                                                                                                                                                                                                ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `app` | The custom[Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)used for initialization. | | `url` | The gs:// url to your Cloud[Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage)Bucket.                | |
| **Returns** | a[FirebaseStorage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage)instance.                                                                                                                                                                                                                                                                                                                                                                                    |

### GetInstance

```c#
FirebaseStorage GetInstance(
  string url
)
```  
Returns the[FirebaseStorage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage), initialized with the default[Firebase.FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)and a custom[Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage)Bucket

<br />

|                                                                                                                                                                       Details                                                                                                                                                                        ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|---------------------------------------------------------------------------------------------------------------------------------------------------------| | `url` | The gs:// url to your Cloud[Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage)Bucket. | |
| **Returns** | a[FirebaseStorage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage)instance.                                                                                                                                                                   |