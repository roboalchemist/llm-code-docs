# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.md.txt

# StorageMetadata

# StorageMetadata


```
public class StorageMetadata
```

<br />

*** ** * ** ***

Metadata for a `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`. Metadata stores default attributes such as size and content type. You may also store custom metadata key value pairs. Metadata values may be used to authorize operations using declarative validation rules.

## Summary

| ### Nested types |
|---|
| `public class https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder` Creates a StorageMetadata object. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata#StorageMetadata()()` Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata` object to hold metadata for a `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata#getBucket()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata#getCacheControl()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata#getContentDisposition()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata#getContentEncoding()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata#getContentLanguage()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata#getContentType()()` |
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata#getCreationTimeMillis()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata#getCustomMetadata(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key)` Returns custom metadata for a `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Set.html<https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata#getCustomMetadataKeys()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata#getGeneration()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata#getMd5Hash()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata#getMetadataGeneration()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata#getName()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata#getPath()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata#getReference()()` |
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata#getSizeBytes()()` |
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata#getUpdatedTimeMillis()()` |

## Public constructors

### StorageMetadata

```
public StorageMetadata()
```

Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata` object to hold metadata for a `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`

## Public methods

### getBucket

```
public @Nullable String getBucket()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | the owning Google Cloud Storage bucket for the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` |

### getCacheControl

```
public @Nullable String getCacheControl()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | the Cache Control setting of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` |

### getContentDisposition

```
public @Nullable String getContentDisposition()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | the content disposition of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` |

### getContentEncoding

```
public @Nullable String getContentEncoding()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | the content encoding for the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` |

### getContentLanguage

```
public @Nullable String getContentLanguage()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | the content language for the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` |

### getContentType

```
public @Nullable String getContentType()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | the content type of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`. |

### getCreationTimeMillis

```
public long getCreationTimeMillis()
```

| Returns |
|---|---|
| `long` | the time the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` was created. |

### getCustomMetadata

```
public @Nullable String getCustomMetadata(@NonNull String key)
```

Returns custom metadata for a `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | The key for which the metadata should be returned |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | the metadata stored in the object the given key. |

### getCustomMetadataKeys

```
public @NonNull Set<String> getCustomMetadataKeys()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Set.html<https://developer.android.com/reference/kotlin/java/lang/String.html>` | the keys for custom metadata. |

### getGeneration

```
public @Nullable String getGeneration()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | a version String indicating what version of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` |

### getMd5Hash

```
public @Nullable String getMd5Hash()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | the MD5Hash of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` object |

### getMetadataGeneration

```
public @Nullable String getMetadataGeneration()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | a version String indicating the version of this `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata` |

### getName

```
public @Nullable String getName()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | a simple name of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` object |

### getPath

```
public @NonNull String getPath()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | the path of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` object |

### getReference

```
public @Nullable StorageReference getReference()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` | the associated `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` for which this metadata belongs to. |

### getSizeBytes

```
public long getSizeBytes()
```

| Returns |
|---|---|
| `long` | the stored Size in bytes of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` object |

### getUpdatedTimeMillis

```
public long getUpdatedTimeMillis()
```

| Returns |
|---|---|
| `long` | the time the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` was last updated. |