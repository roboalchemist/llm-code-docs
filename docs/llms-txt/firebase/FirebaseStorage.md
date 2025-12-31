# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage.md.txt

# FirebaseStorage

# FirebaseStorage


```
public class FirebaseStorage
```

<br />

*** ** * ** ***

FirebaseStorage is a service that supports uploading and downloading large objects to Google Cloud Storage. Pass a custom instance of [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) to [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getInstance(com.google.firebase.FirebaseApp)) which will initialize it with a storage location (bucket) specified via [setStorageBucket](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions.Builder#setStorageBucket(java.lang.String)).

Otherwise, if you call [getReference](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getReference()) without a FirebaseApp, the FirebaseStorage instance will initialize with the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) obtainable from [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#getInstance()). The storage location in this case will come the JSON configuration file downloaded from the web.

## Summary

|                                                                                                    ### Public methods                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)                        | [getApp](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getApp())`()` The [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) associated with this [FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage) instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `static @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage) | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getInstance())`()` Returns the [FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage), initialized with the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `static @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage) | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getInstance(com.google.firebase.FirebaseApp))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app)` Returns the [FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage), initialized with a custom [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)                                                                                                                                                                                                                                   |
| `static @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage) | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getInstance(java.lang.String))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` url)` Returns the [FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage), initialized with the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) and a custom Storage Bucket.                                                                                                                                                                                                                                     |
| `static @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage) | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getInstance(com.google.firebase.FirebaseApp,java.lang.String))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` url)` Returns the [FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage), initialized with a custom [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) and a custom Storage Bucket. |
| `long`                                                                                                                                                                                                                   | [getMaxChunkUploadRetry](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getMaxChunkUploadRetry())`()` Returns the maximum time to retry sending a chunk if a failure occurs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `long`                                                                                                                                                                                                                   | [getMaxDownloadRetryTimeMillis](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getMaxDownloadRetryTimeMillis())`()` Returns the maximum time to retry a download if a failure occurs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `long`                                                                                                                                                                                                                   | [getMaxOperationRetryTimeMillis](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getMaxOperationRetryTimeMillis())`()` Returns the maximum time to retry operations other than upload and download if a failure occurs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `long`                                                                                                                                                                                                                   | [getMaxUploadRetryTimeMillis](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getMaxUploadRetryTimeMillis())`()` Returns the maximum time to retry an upload if a failure occurs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[StorageReference](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference)      | [getReference](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getReference())`()` Creates a new [StorageReference](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference) initialized at the root Firebase Storage location.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[StorageReference](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference)      | [getReference](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getReference(java.lang.String))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` location)` Creates a new [StorageReference](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference) initialized with a child Firebase Storage location.                                                                                                                                                                                                                                                                                                                                   |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[StorageReference](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference)      | [getReferenceFromUrl](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getReferenceFromUrl(java.lang.String))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` fullUrl)` Creates a [StorageReference](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference) given a gs:// or https:// URL pointing to a Firebase Storage location.                                                                                                                                                                                                                                                                                                       |
| `void`                                                                                                                                                                                                                   | [setMaxChunkUploadRetry](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#setMaxChunkUploadRetry(long))`(long maxChunkRetryMillis)` Sets the maximum time to retry sending a chunk if a failure occurs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `void`                                                                                                                                                                                                                   | [setMaxDownloadRetryTimeMillis](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#setMaxDownloadRetryTimeMillis(long))`(long maxTransferRetryMillis)` Sets the maximum time to retry a download if a failure occurs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `void`                                                                                                                                                                                                                   | [setMaxOperationRetryTimeMillis](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#setMaxOperationRetryTimeMillis(long))`(long maxTransferRetryMillis)` Sets the maximum time to retry operations other than upload and download if a failure occurs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `void`                                                                                                                                                                                                                   | [setMaxUploadRetryTimeMillis](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#setMaxUploadRetryTimeMillis(long))`(long maxTransferRetryMillis)` Sets the maximum time to retry an upload if a failure occurs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `void`                                                                                                                                                                                                                   | [useEmulator](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#useEmulator(java.lang.String,int))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` host, int port)` Modifies this FirebaseStorage instance to communicate with the Storage emulator.                                                                                                                                                                                                                                                                                                                                                                                                                                |

## Public methods

### getApp

```
publicÂ @NonNull FirebaseAppÂ getApp()
```

The [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) associated with this [FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage) instance.  

### getInstance

```
publicÂ staticÂ @NonNull FirebaseStorageÂ getInstance()
```

Returns the [FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage), initialized with the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).  

|                                                                                                      Returns                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage) | a [FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage) instance. |

### getInstance

```
publicÂ staticÂ @NonNull FirebaseStorageÂ getInstance(@NonNull FirebaseAppÂ app)
```

Returns the [FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage), initialized with a custom [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)  

|                                                                                               Parameters                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app` | The custom [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) used for initialization. |

|                                                                                                      Returns                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage) | a [FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage) instance. |

### getInstance

```
publicÂ staticÂ @NonNull FirebaseStorageÂ getInstance(@NonNull StringÂ url)
```

Returns the [FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage), initialized with the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) and a custom Storage Bucket.  

|                                                                                      Parameters                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` url` | The gs:// url to your Firebase Storage Bucket. |

|                                                                                                      Returns                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage) | a [FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage) instance. |

### getInstance

```
publicÂ staticÂ @NonNull FirebaseStorageÂ getInstance(@NonNull FirebaseAppÂ app,Â @NonNull StringÂ url)
```

Returns the [FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage), initialized with a custom [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) and a custom Storage Bucket.  

|                                                                                               Parameters                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app` | The custom [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) used for initialization. |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` url`                    | The gs:// url to your Firebase Storage Bucket.                                                                                        |

|                                                                                                      Returns                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage) | a [FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage) instance. |

### getMaxChunkUploadRetry

```
publicÂ longÂ getMaxChunkUploadRetry()
```

Returns the maximum time to retry sending a chunk if a failure occurs  

| Returns |
|---------|-----------------------------------------------------|
| `long`  | maximum time in milliseconds. Defaults to 1 minute. |

### getMaxDownloadRetryTimeMillis

```
publicÂ longÂ getMaxDownloadRetryTimeMillis()
```

Returns the maximum time to retry a download if a failure occurs.  

| Returns |
|---------|------------------------------------------------------------------------------|
| `long`  | maximum time in milliseconds. Defaults to 10 minutes (600,000 milliseconds). |

### getMaxOperationRetryTimeMillis

```
publicÂ longÂ getMaxOperationRetryTimeMillis()
```

Returns the maximum time to retry operations other than upload and download if a failure occurs.  

| Returns |
|---------|---------------------------------------------------------------------------------|
| `long`  | the maximum time in milliseconds. Defaults to 2 minutes (120,000 milliseconds). |

### getMaxUploadRetryTimeMillis

```
publicÂ longÂ getMaxUploadRetryTimeMillis()
```

Returns the maximum time to retry an upload if a failure occurs.  

| Returns |
|---------|----------------------------------------------------------------------------------|
| `long`  | the maximum time in milliseconds. Defaults to 10 minutes (600,000 milliseconds). |

### getReference

```
publicÂ @NonNull StorageReferenceÂ getReference()
```

Creates a new [StorageReference](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference) initialized at the root Firebase Storage location.  

|                                                                                                       Returns                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[StorageReference](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference) | An instance of [StorageReference](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference). |

### getReference

```
publicÂ @NonNull StorageReferenceÂ getReference(@NonNull StringÂ location)
```

Creates a new [StorageReference](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference) initialized with a child Firebase Storage location.  

|                                                                                        Parameters                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` location` | A relative path from the root to initialize the reference with, for instance "path/to/object" |

|                                                                                                       Returns                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[StorageReference](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference) | An instance of [StorageReference](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference) at the given child path. |

### getReferenceFromUrl

```
publicÂ @NonNull StorageReferenceÂ getReferenceFromUrl(@NonNull StringÂ fullUrl)
```

Creates a [StorageReference](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference) given a gs:// or https:// URL pointing to a Firebase Storage location.  

|                                                                                        Parameters                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` fullUrl` | A gs:// or http\[s\]:// URL used to initialize the reference. For example, you can pass in a download URL retrieved from [getDownloadUrl](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#getDownloadUrl()) or the uri retrieved from [toString](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#toString()) An error is thrown if fullUrl is not associated with the [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) used to initialize this [FirebaseStorage](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage). |

### setMaxChunkUploadRetry

```
publicÂ voidÂ setMaxChunkUploadRetry(longÂ maxChunkRetryMillis)
```

Sets the maximum time to retry sending a chunk if a failure occurs  

|         Parameters         |
|----------------------------|-------------------------------------------------------------------------------|
| `long maxChunkRetryMillis` | the maximum time in milliseconds. Defaults to 1 minute (60,000 milliseconds). |

### setMaxDownloadRetryTimeMillis

```
publicÂ voidÂ setMaxDownloadRetryTimeMillis(longÂ maxTransferRetryMillis)
```

Sets the maximum time to retry a download if a failure occurs.  

|          Parameters           |
|-------------------------------|----------------------------------------------------------------------------------|
| `long maxTransferRetryMillis` | the maximum time in milliseconds. Defaults to 10 minutes (600,000 milliseconds). |

### setMaxOperationRetryTimeMillis

```
publicÂ voidÂ setMaxOperationRetryTimeMillis(longÂ maxTransferRetryMillis)
```

Sets the maximum time to retry operations other than upload and download if a failure occurs.  

|          Parameters           |
|-------------------------------|---------------------------------------------------------------------------------|
| `long maxTransferRetryMillis` | the maximum time in milliseconds. Defaults to 2 minutes (120,000 milliseconds). |

### setMaxUploadRetryTimeMillis

```
publicÂ voidÂ setMaxUploadRetryTimeMillis(longÂ maxTransferRetryMillis)
```

Sets the maximum time to retry an upload if a failure occurs.  

|          Parameters           |
|-------------------------------|----------------------------------------------------------------------------------|
| `long maxTransferRetryMillis` | the maximum time in milliseconds. Defaults to 10 minutes (600,000 milliseconds). |

### useEmulator

```
publicÂ voidÂ useEmulator(@NonNull StringÂ host,Â intÂ port)
```

Modifies this FirebaseStorage instance to communicate with the Storage emulator.

Note: Call this method before using the instance to do any storage operations.  

|                                                                                      Parameters                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` host` | the emulator host (for example, 10.0.2.2) |
| `int port`                                                                                                                                                                            | the emulator port (for example, 9000)     |