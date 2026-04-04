# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage.md.txt

# FirebaseStorage

# FirebaseStorage


```
class FirebaseStorage
```

<br />

*** ** * ** ***

FirebaseStorage is a service that supports uploading and downloading large objects to Google Cloud Storage. Pass a custom instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage#getInstance(com.google.firebase.FirebaseApp)` which will initialize it with a storage location (bucket) specified via `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder#setStorageBucket(java.lang.String)`.

Otherwise, if you call `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage#getReference()` without a FirebaseApp, the FirebaseStorage instance will initialize with the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` obtainable from `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp#getInstance()`. The storage location in this case will come the JSON configuration file downloaded from the web.

## Summary

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage#getApp()()` The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` associated with this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` instance. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage#getInstance()()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage`, initialized with the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage#getInstance(com.google.firebase.FirebaseApp)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage`, initialized with a custom `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage#getInstance(java.lang.String)(url: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage`, initialized with the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and a custom Storage Bucket. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage#getInstance(com.google.firebase.FirebaseApp,java.lang.String)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp, url: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage`, initialized with a custom `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and a custom Storage Bucket. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage#getMaxChunkUploadRetry()()` Returns the maximum time to retry sending a chunk if a failure occurs |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage#getMaxDownloadRetryTimeMillis()()` Returns the maximum time to retry a download if a failure occurs. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage#getMaxOperationRetryTimeMillis()()` Returns the maximum time to retry operations other than upload and download if a failure occurs. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage#getMaxUploadRetryTimeMillis()()` Returns the maximum time to retry an upload if a failure occurs. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage#getReference()()` Creates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` initialized at the root Firebase Storage location. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage#getReference(java.lang.String)(location: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` initialized with a child Firebase Storage location. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage#getReferenceFromUrl(java.lang.String)(fullUrl: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` given a gs:// or https:// URL pointing to a Firebase Storage location. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage#setMaxChunkUploadRetry(long)(maxChunkRetryMillis: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Sets the maximum time to retry sending a chunk if a failure occurs |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage#setMaxDownloadRetryTimeMillis(long)(maxTransferRetryMillis: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Sets the maximum time to retry a download if a failure occurs. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage#setMaxOperationRetryTimeMillis(long)(maxTransferRetryMillis: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Sets the maximum time to retry operations other than upload and download if a failure occurs. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage#setMaxUploadRetryTimeMillis(long)(maxTransferRetryMillis: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Sets the maximum time to retry an upload if a failure occurs. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage#useEmulator(java.lang.String,int)(host: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, port: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Modifies this FirebaseStorage instance to communicate with the Storage emulator. |

## Public functions

### getApp

```
fun getApp(): FirebaseApp
```

The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` associated with this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` instance.

### getInstance

```
java-static fun getInstance(): FirebaseStorage
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage`, initialized with the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` | a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` instance. |

### getInstance

```
java-static fun getInstance(app: FirebaseApp): FirebaseStorage
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage`, initialized with a custom `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`

| Parameters |
|---|---|
| `app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | The custom `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` used for initialization. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` | a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` instance. |

### getInstance

```
java-static fun getInstance(url: String): FirebaseStorage
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage`, initialized with the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and a custom Storage Bucket.

| Parameters |
|---|---|
| `url: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The gs:// url to your Firebase Storage Bucket. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` | a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` instance. |

### getInstance

```
java-static fun getInstance(app: FirebaseApp, url: String): FirebaseStorage
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage`, initialized with a custom `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and a custom Storage Bucket.

| Parameters |
|---|---|
| `app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | The custom `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` used for initialization. |
| `url: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The gs:// url to your Firebase Storage Bucket. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` | a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage` instance. |

### getMaxChunkUploadRetry

```
fun getMaxChunkUploadRetry(): Long
```

Returns the maximum time to retry sending a chunk if a failure occurs

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | maximum time in milliseconds. Defaults to 1 minute. |

### getMaxDownloadRetryTimeMillis

```
fun getMaxDownloadRetryTimeMillis(): Long
```

Returns the maximum time to retry a download if a failure occurs.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | maximum time in milliseconds. Defaults to 10 minutes (600,000 milliseconds). |

### getMaxOperationRetryTimeMillis

```
fun getMaxOperationRetryTimeMillis(): Long
```

Returns the maximum time to retry operations other than upload and download if a failure occurs.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the maximum time in milliseconds. Defaults to 2 minutes (120,000 milliseconds). |

### getMaxUploadRetryTimeMillis

```
fun getMaxUploadRetryTimeMillis(): Long
```

Returns the maximum time to retry an upload if a failure occurs.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the maximum time in milliseconds. Defaults to 10 minutes (600,000 milliseconds). |

### getReference

```
fun getReference(): StorageReference
```

Creates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` initialized at the root Firebase Storage location.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` | An instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`. |

### getReference

```
fun getReference(location: String): StorageReference
```

Creates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` initialized with a child Firebase Storage location.

| Parameters |
|---|---|
| `location: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A relative path from the root to initialize the reference with, for instance "path/to/object" |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` | An instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` at the given child path. |

### getReferenceFromUrl

```
fun getReferenceFromUrl(fullUrl: String): StorageReference
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` given a gs:// or https:// URL pointing to a Firebase Storage location.

| Parameters |
|---|---|
| `fullUrl: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A gs:// or http\[s\]:// URL used to initialize the reference. For example, you can pass in a download URL retrieved from `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#getDownloadUrl()` or the uri retrieved from `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#toString()` An error is thrown if fullUrl is not associated with the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` used to initialize this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/FirebaseStorage`. |

### setMaxChunkUploadRetry

```
fun setMaxChunkUploadRetry(maxChunkRetryMillis: Long): Unit
```

Sets the maximum time to retry sending a chunk if a failure occurs

| Parameters |
|---|---|
| `maxChunkRetryMillis: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the maximum time in milliseconds. Defaults to 1 minute (60,000 milliseconds). |

### setMaxDownloadRetryTimeMillis

```
fun setMaxDownloadRetryTimeMillis(maxTransferRetryMillis: Long): Unit
```

Sets the maximum time to retry a download if a failure occurs.

| Parameters |
|---|---|
| `maxTransferRetryMillis: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the maximum time in milliseconds. Defaults to 10 minutes (600,000 milliseconds). |

### setMaxOperationRetryTimeMillis

```
fun setMaxOperationRetryTimeMillis(maxTransferRetryMillis: Long): Unit
```

Sets the maximum time to retry operations other than upload and download if a failure occurs.

| Parameters |
|---|---|
| `maxTransferRetryMillis: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the maximum time in milliseconds. Defaults to 2 minutes (120,000 milliseconds). |

### setMaxUploadRetryTimeMillis

```
fun setMaxUploadRetryTimeMillis(maxTransferRetryMillis: Long): Unit
```

Sets the maximum time to retry an upload if a failure occurs.

| Parameters |
|---|---|
| `maxTransferRetryMillis: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the maximum time in milliseconds. Defaults to 10 minutes (600,000 milliseconds). |

### useEmulator

```
fun useEmulator(host: String, port: Int): Unit
```

Modifies this FirebaseStorage instance to communicate with the Storage emulator.

Note: Call this method before using the instance to do any storage operations.

| Parameters |
|---|---|
| `host: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the emulator host (for example, 10.0.2.2) |
| `port: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | the emulator port (for example, 9000) |