# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder.md.txt

# StorageMetadata.Builder

# StorageMetadata.Builder


```
class StorageMetadata.Builder
```

<br />

*** ** * ** ***

Creates a StorageMetadata object.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#Builder()()` Creates an empty set of metadata. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#Builder(com.google.firebase.storage.StorageMetadata)(original: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata)` Used to create a modified version of the original set of metadata. |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#build()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#getCacheControl()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#getContentDisposition()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#getContentEncoding()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#getContentLanguage()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#getContentType()()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#setCacheControl(java.lang.String)(cacheControl: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Sets the Cache Control header for the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#setContentDisposition(java.lang.String)(contentDisposition: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Changes the content disposition for the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#setContentEncoding(java.lang.String)(contentEncoding: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Changes the content encoding for the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#setContentLanguage(java.lang.String)(contentLanguage: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Changes the content language for the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#setContentType(java.lang.String)(contentType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Changes the content Type of this associated `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#setCustomMetadata(java.lang.String,java.lang.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Sets custom metadata |

## Public constructors

### Builder

```
Builder()
```

Creates an empty set of metadata.

### Builder

```
Builder(original: StorageMetadata)
```

Used to create a modified version of the original set of metadata.

| Parameters |
|---|---|
| `original: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata` | The source of the metadata to build from. |

## Public functions

### build

```
fun build(): StorageMetadata
```

### getCacheControl

```
fun getCacheControl(): String?
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | the Cache Control header for the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` |

### getContentDisposition

```
fun getContentDisposition(): String?
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | the content disposition for the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` |

### getContentEncoding

```
fun getContentEncoding(): String?
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | the content encoding for the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` |

### getContentLanguage

```
fun getContentLanguage(): String?
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | the content language for the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` |

### getContentType

```
fun getContentType(): String?
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | the Content Type of this associated `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` |

### setCacheControl

```
fun setCacheControl(cacheControl: String?): StorageMetadata.Builder
```

Sets the Cache Control header for the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`

| Parameters |
|---|---|
| `cacheControl: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | the new Cache Control setting. |

### setContentDisposition

```
fun setContentDisposition(contentDisposition: String?): StorageMetadata.Builder
```

Changes the content disposition for the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`

| Parameters |
|---|---|
| `contentDisposition: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | the new content disposition to use. |

### setContentEncoding

```
fun setContentEncoding(contentEncoding: String?): StorageMetadata.Builder
```

Changes the content encoding for the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`

| Parameters |
|---|---|
| `contentEncoding: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | the new encoding to use. |

### setContentLanguage

```
fun setContentLanguage(contentLanguage: String?): StorageMetadata.Builder
```

Changes the content language for the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`

| Parameters |
|---|---|
| `contentLanguage: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | the new content language. |

### setContentType

```
fun setContentType(contentType: String?): StorageMetadata.Builder
```

Changes the content Type of this associated `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`

| Parameters |
|---|---|
| `contentType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | the new Content Type. |

### setCustomMetadata

```
fun setCustomMetadata(key: String, value: String?): StorageMetadata.Builder
```

Sets custom metadata

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the key of the new value |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | the value to set. |