# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder.md.txt

# StorageMetadata.Builder

# StorageMetadata.Builder


```
public class StorageMetadata.Builder
```

<br />

*** ** * ** ***

Creates a StorageMetadata object.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder#Builder()()` Creates an empty set of metadata. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder#Builder(com.google.firebase.storage.StorageMetadata)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata original)` Used to create a modified version of the original set of metadata. |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder#build()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder#getCacheControl()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder#getContentDisposition()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder#getContentEncoding()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder#getContentLanguage()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder#getContentType()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder#setCacheControl(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html cacheControl)` Sets the Cache Control header for the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder#setContentDisposition(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html contentDisposition)` Changes the content disposition for the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder#setContentEncoding(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html contentEncoding)` Changes the content encoding for the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder#setContentLanguage(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html contentLanguage)` Changes the content language for the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder#setContentType(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html contentType)` Changes the content Type of this associated `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder#setCustomMetadata(java.lang.String,java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html value)` Sets custom metadata |

## Public constructors

### Builder

```
public Builder()
```

Creates an empty set of metadata.

### Builder

```
public Builder(@NonNull StorageMetadata original)
```

Used to create a modified version of the original set of metadata.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata original` | The source of the metadata to build from. |

## Public methods

### build

```
public @NonNull StorageMetadata build()
```

### getCacheControl

```
public @Nullable String getCacheControl()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | the Cache Control header for the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` |

### getContentDisposition

```
public @Nullable String getContentDisposition()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | the content disposition for the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` |

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
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | the Content Type of this associated `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference` |

### setCacheControl

```
public @NonNull StorageMetadata.Builder setCacheControl(@Nullable String cacheControl)
```

Sets the Cache Control header for the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html cacheControl` | the new Cache Control setting. |

### setContentDisposition

```
public @NonNull StorageMetadata.Builder setContentDisposition(@Nullable String contentDisposition)
```

Changes the content disposition for the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html contentDisposition` | the new content disposition to use. |

### setContentEncoding

```
public @NonNull StorageMetadata.Builder setContentEncoding(@Nullable String contentEncoding)
```

Changes the content encoding for the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html contentEncoding` | the new encoding to use. |

### setContentLanguage

```
public @NonNull StorageMetadata.Builder setContentLanguage(@Nullable String contentLanguage)
```

Changes the content language for the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html contentLanguage` | the new content language. |

### setContentType

```
public @NonNull StorageMetadata.Builder setContentType(@Nullable String contentType)
```

Changes the content Type of this associated `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference`

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html contentType` | the new Content Type. |

### setCustomMetadata

```
public @NonNull StorageMetadata.Builder setCustomMetadata(@NonNull String key, @Nullable String value)
```

Sets custom metadata

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | the key of the new value |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html value` | the value to set. |