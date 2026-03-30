# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage.md.txt

# FirebaseStorage

# FirebaseStorage


```
public class FirebaseStorage
```

<br />

*** ** * ** ***

FirebaseStorage is a service that supports uploading and downloading large objects to Google Cloud Storage. Pass a custom instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` to `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getInstance(com.google.firebase.FirebaseApp)` which will initialize it with a storage location (bucket) specified via `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions.Builder#setStorageBucket(java.lang.String)`.

Otherwise, if you call `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getReference()` without a FirebaseApp, the FirebaseStorage instance will initialize with the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` obtainable from `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp#getInstance()`. The storage location in this case will come the JSON configuration file downloaded from the web.

## Summary

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getApp()()` The `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` associated with this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` instance. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getInstance()()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage`, initialized with the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getInstance(com.google.firebase.FirebaseApp)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app)` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage`, initialized with a custom `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getInstance(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html url)` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage`, initialized with the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and a custom Storage Bucket. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getInstance(com.google.firebase.FirebaseApp,java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html url)` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage`, initialized with a custom `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and a custom Storage Bucket. |
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getMaxChunkUploadRetry()()` Returns the maximum time to retry sending a chunk if a failure occurs |
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getMaxDownloadRetryTimeMillis()()` Returns the maximum time to retry a download if a failure occurs. |
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getMaxOperationRetryTimeMillis()()` Returns the maximum time to retry operations other than upload and download if a failure occurs. |
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getMaxUploadRetryTimeMillis()()` Returns the maximum time to retry an upload if a failure occurs. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getReference()()` Creates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` initialized at the root Firebase Storage location. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getReference(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html location)` Creates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` initialized with a child Firebase Storage location. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#getReferenceFromUrl(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fullUrl)` Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` given a gs:// or https:// URL pointing to a Firebase Storage location. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#setMaxChunkUploadRetry(long)(long maxChunkRetryMillis)` Sets the maximum time to retry sending a chunk if a failure occurs |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#setMaxDownloadRetryTimeMillis(long)(long maxTransferRetryMillis)` Sets the maximum time to retry a download if a failure occurs. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#setMaxOperationRetryTimeMillis(long)(long maxTransferRetryMillis)` Sets the maximum time to retry operations other than upload and download if a failure occurs. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#setMaxUploadRetryTimeMillis(long)(long maxTransferRetryMillis)` Sets the maximum time to retry an upload if a failure occurs. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage#useEmulator(java.lang.String,int)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html host, int port)` Modifies this FirebaseStorage instance to communicate with the Storage emulator. |

## Public methods

### getApp

```
public @NonNull FirebaseApp getApp()
```

The `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` associated with this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` instance.

### getInstance

```
public static @NonNull FirebaseStorage getInstance()
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage`, initialized with the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` | a `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` instance. |

### getInstance

```
public static @NonNull FirebaseStorage getInstance(@NonNull FirebaseApp app)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage`, initialized with a custom `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app` | The custom `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` used for initialization. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` | a `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` instance. |

### getInstance

```
public static @NonNull FirebaseStorage getInstance(@NonNull String url)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage`, initialized with the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and a custom Storage Bucket.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html url` | The gs:// url to your Firebase Storage Bucket. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` | a `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` instance. |

### getInstance

```
public static @NonNull FirebaseStorage getInstance(@NonNull FirebaseApp app, @NonNull String url)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage`, initialized with a custom `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and a custom Storage Bucket.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app` | The custom `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` used for initialization. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html url` | The gs:// url to your Firebase Storage Bucket. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` | a `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage` instance. |

### getMaxChunkUploadRetry

```
public long getMaxChunkUploadRetry()
```

Returns the maximum time to retry sending a chunk if a failure occurs

| Returns |
|---|---|
| `long` | maximum time in milliseconds. Defaults to 1 minute. |

### getMaxDownloadRetryTimeMillis

```
public long getMaxDownloadRetryTimeMillis()
```

Returns the maximum time to retry a download if a failure occurs.

| Returns |
|---|---|
| `long` | maximum time in milliseconds. Defaults to 10 minutes (600,000 milliseconds). |

### getMaxOperationRetryTimeMillis

```
public long getMaxOperationRetryTimeMillis()
```

Returns the maximum time to retry operations other than upload and download if a failure occurs.

| Returns |
|---|---|
| `long` | the maximum time in milliseconds. Defaults to 2 minutes (120,000 milliseconds). |

### getMaxUploadRetryTimeMillis

```
public long getMaxUploadRetryTimeMillis()
```

Returns the maximum time to retry an upload if a failure occurs.

| Returns |
|---|---|
| `long` | the maximum time in milliseconds. Defaults to 10 minutes (600,000 milliseconds). |

### getReference

```
public @NonNull StorageReference getReference()
```

Creates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` initialized at the root Firebase Storage location.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` | An instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`. |

### getReference

```
public @NonNull StorageReference getReference(@NonNull String location)
```

Creates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` initialized with a child Firebase Storage location.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html location` | A relative path from the root to initialize the reference with, for instance "path/to/object" |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` | An instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` at the given child path. |

### getReferenceFromUrl

```
public @NonNull StorageReference getReferenceFromUrl(@NonNull String fullUrl)
```

Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` given a gs:// or https:// URL pointing to a Firebase Storage location.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fullUrl` | A gs:// or http\[s\]:// URL used to initialize the reference. For example, you can pass in a download URL retrieved from `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#getDownloadUrl()` or the uri retrieved from `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#toString()` An error is thrown if fullUrl is not associated with the `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` used to initialize this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage`. |

### setMaxChunkUploadRetry

```
public void setMaxChunkUploadRetry(long maxChunkRetryMillis)
```

Sets the maximum time to retry sending a chunk if a failure occurs

| Parameters |
|---|---|
| `long maxChunkRetryMillis` | the maximum time in milliseconds. Defaults to 1 minute (60,000 milliseconds). |

### setMaxDownloadRetryTimeMillis

```
public void setMaxDownloadRetryTimeMillis(long maxTransferRetryMillis)
```

Sets the maximum time to retry a download if a failure occurs.

| Parameters |
|---|---|
| `long maxTransferRetryMillis` | the maximum time in milliseconds. Defaults to 10 minutes (600,000 milliseconds). |

### setMaxOperationRetryTimeMillis

```
public void setMaxOperationRetryTimeMillis(long maxTransferRetryMillis)
```

Sets the maximum time to retry operations other than upload and download if a failure occurs.

| Parameters |
|---|---|
| `long maxTransferRetryMillis` | the maximum time in milliseconds. Defaults to 2 minutes (120,000 milliseconds). |

### setMaxUploadRetryTimeMillis

```
public void setMaxUploadRetryTimeMillis(long maxTransferRetryMillis)
```

Sets the maximum time to retry an upload if a failure occurs.

| Parameters |
|---|---|
| `long maxTransferRetryMillis` | the maximum time in milliseconds. Defaults to 10 minutes (600,000 milliseconds). |

### useEmulator

```
public void useEmulator(@NonNull String host, int port)
```

Modifies this FirebaseStorage instance to communicate with the Storage emulator.

Note: Call this method before using the instance to do any storage operations.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html host` | the emulator host (for example, 10.0.2.2) |
| `int port` | the emulator port (for example, 9000) |