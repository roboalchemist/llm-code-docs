# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageMetadata.Builder.md.txt

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

|                                                                                                                                                                         ### Public constructors                                                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#Builder())`()` Creates an empty set of metadata.                                                                                                                                                                                                         |
| [Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#Builder(com.google.firebase.storage.StorageMetadata))`(original: `[StorageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata)`)` Used to create a modified version of the original set of metadata. |

|                                                       ### Public functions                                                       |
|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [StorageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata)                 | [build](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#build())`()`                                                                                                                                                                                                                                                                                                                   |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                                              | [getCacheControl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#getCacheControl())`()`                                                                                                                                                                                                                                                                                               |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                                              | [getContentDisposition](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#getContentDisposition())`()`                                                                                                                                                                                                                                                                                   |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                                              | [getContentEncoding](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#getContentEncoding())`()`                                                                                                                                                                                                                                                                                         |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                                              | [getContentLanguage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#getContentLanguage())`()`                                                                                                                                                                                                                                                                                         |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                                              | [getContentType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#getContentType())`()`                                                                                                                                                                                                                                                                                                 |
| [StorageMetadata.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder) | [setCacheControl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#setCacheControl(java.lang.String))`(cacheControl: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Sets the Cache Control header for the [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference)                     |
| [StorageMetadata.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder) | [setContentDisposition](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#setContentDisposition(java.lang.String))`(contentDisposition: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Changes the content disposition for the [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference) |
| [StorageMetadata.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder) | [setContentEncoding](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#setContentEncoding(java.lang.String))`(contentEncoding: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Changes the content encoding for the [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference)             |
| [StorageMetadata.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder) | [setContentLanguage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#setContentLanguage(java.lang.String))`(contentLanguage: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Changes the content language for the [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference)             |
| [StorageMetadata.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder) | [setContentType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#setContentType(java.lang.String))`(contentType: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Changes the content Type of this associated [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference)                  |
| [StorageMetadata.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder) | [setCustomMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata.Builder#setCustomMetadata(java.lang.String,java.lang.String))`(key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Sets custom metadata                                                  |

## Public constructors

### Builder

```
Builder()
```

Creates an empty set of metadata.  

### Builder

```
Builder(original:Â StorageMetadata)
```

Used to create a modified version of the original set of metadata.  

|                                                          Parameters                                                          |
|------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| `original: `[StorageMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageMetadata) | The source of the metadata to build from. |

## Public functions

### build

```
funÂ build():Â StorageMetadata
```  

### getCacheControl

```
funÂ getCacheControl():Â String?
```  

|                                       Returns                                       |
|-------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | the Cache Control header for the [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference) |

### getContentDisposition

```
funÂ getContentDisposition():Â String?
```  

|                                       Returns                                       |
|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | the content disposition for the [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference) |

### getContentEncoding

```
funÂ getContentEncoding():Â String?
```  

|                                       Returns                                       |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | the content encoding for the [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference) |

### getContentLanguage

```
funÂ getContentLanguage():Â String?
```  

|                                       Returns                                       |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | the content language for the [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference) |

### getContentType

```
funÂ getContentType():Â String?
```  

|                                       Returns                                       |
|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | the Content Type of this associated [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference) |

### setCacheControl

```
funÂ setCacheControl(cacheControl:Â String?):Â StorageMetadata.Builder
```

Sets the Cache Control header for the [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference)  

|                                             Parameters                                              |
|-----------------------------------------------------------------------------------------------------|--------------------------------|
| `cacheControl: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | the new Cache Control setting. |

### setContentDisposition

```
funÂ setContentDisposition(contentDisposition:Â String?):Â StorageMetadata.Builder
```

Changes the content disposition for the [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference)  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|-------------------------------------|
| `contentDisposition: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | the new content disposition to use. |

### setContentEncoding

```
funÂ setContentEncoding(contentEncoding:Â String?):Â StorageMetadata.Builder
```

Changes the content encoding for the [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference)  

|                                               Parameters                                               |
|--------------------------------------------------------------------------------------------------------|--------------------------|
| `contentEncoding: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | the new encoding to use. |

### setContentLanguage

```
funÂ setContentLanguage(contentLanguage:Â String?):Â StorageMetadata.Builder
```

Changes the content language for the [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference)  

|                                               Parameters                                               |
|--------------------------------------------------------------------------------------------------------|---------------------------|
| `contentLanguage: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | the new content language. |

### setContentType

```
funÂ setContentType(contentType:Â String?):Â StorageMetadata.Builder
```

Changes the content Type of this associated [StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference)  

|                                             Parameters                                             |
|----------------------------------------------------------------------------------------------------|-----------------------|
| `contentType: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | the new Content Type. |

### setCustomMetadata

```
funÂ setCustomMetadata(key:Â String,Â value:Â String?):Â StorageMetadata.Builder
```

Sets custom metadata  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|--------------------------|
| `key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)      | the key of the new value |
| `value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | the value to set.        |