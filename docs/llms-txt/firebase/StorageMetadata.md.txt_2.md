# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.md.txt

# StorageMetadata

# StorageMetadata


```
class StorageMetadata
```

<br />

*** ** * ** ***

Metadata for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`. Metadata stores default attributes such as size and content type. You may also store custom metadata key value pairs. Metadata values may be used to authorize operations using declarative validation rules.

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder` Creates a StorageMetadata object. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata#StorageMetadata()()` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata` object to hold metadata for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata#getBucket()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata#getCacheControl()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata#getContentDisposition()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata#getContentEncoding()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata#getContentLanguage()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata#getContentType()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata#getCreationTimeMillis()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata#getCustomMetadata(java.lang.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns custom metadata for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` |
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata#getCustomMetadataKeys()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata#getGeneration()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata#getMd5Hash()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata#getMetadataGeneration()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata#getName()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata#getPath()()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata#getReference()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata#getSizeBytes()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata#getUpdatedTimeMillis()()` |

## Public constructors

### StorageMetadata

```
StorageMetadata()
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata` object to hold metadata for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`

## Public functions

### getBucket

```
fun getBucket(): String?
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | the owning Google Cloud Storage bucket for the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` |

### getCacheControl

```
fun getCacheControl(): String?
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | the Cache Control setting of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` |

### getContentDisposition

```
fun getContentDisposition(): String?
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | the content disposition of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` |

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
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | the content type of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`. |

### getCreationTimeMillis

```
fun getCreationTimeMillis(): Long
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the time the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` was created. |

### getCustomMetadata

```
fun getCustomMetadata(key: String): String?
```

Returns custom metadata for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference`

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The key for which the metadata should be returned |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | the metadata stored in the object the given key. |

### getCustomMetadataKeys

```
fun getCustomMetadataKeys(): (Mutable)Set<String!>
```

| Returns |
|---|---|
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>` | the keys for custom metadata. |

### getGeneration

```
fun getGeneration(): String?
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | a version String indicating what version of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` |

### getMd5Hash

```
fun getMd5Hash(): String?
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | the MD5Hash of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` object |

### getMetadataGeneration

```
fun getMetadataGeneration(): String?
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | a version String indicating the version of this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata` |

### getName

```
fun getName(): String?
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | a simple name of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` object |

### getPath

```
fun getPath(): String
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the path of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` object |

### getReference

```
fun getReference(): StorageReference?
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference?` | the associated `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` for which this metadata belongs to. |

### getSizeBytes

```
fun getSizeBytes(): Long
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the stored Size in bytes of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` object |

### getUpdatedTimeMillis

```
fun getUpdatedTimeMillis(): Long
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the time the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference` was last updated. |