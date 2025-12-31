# Source: https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata.md.txt

# Firebase.Storage.StorageMetadata Class Reference

# Firebase.Storage.StorageMetadata

Metadata for a [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) Metadata stores default attributes such as size and content type.

## Summary

You may also store custom metadata key value pairs. Metadata values may be used to authorize operations using declarative validation rules. This class is readonly. To create or change metadata, use [MetadataChange](https://firebase.google.com/docs/reference/unity/class/firebase/storage/metadata-change#class_firebase_1_1_storage_1_1_metadata_change).

| ### Constructors and Destructors ||
|---|---|
| [StorageMetadata](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata_1a23db2f7b5df675dce2b2bcf00bdf7618)`()` Creates a [StorageMetadata](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata) object to hold metadata for a [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) ||

|                                                                                                                                                                                                                                                         ### Properties                                                                                                                                                                                                                                                         ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Bucket](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata_1a8a18f6df6a82185983c24d6376cd9d71)             | `string`                                                                                                                                                                                                                                                                                                                    |
| **Returns**                                                                                                                                                                                       | the owning Google Cloud [Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage) bucket for the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) |
| [CacheControl](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata_1af8b2fafd2cce45de827d2d4221946a81)       | `string`                                                                                                                                                                                                                                                                                                                    |
| **Returns**                                                                                                                                                                                       | the Cache Control setting of the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)                                                                                                                             |
| [ContentDisposition](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata_1a7797928ffc6e41d6b463fa1ee174f0f8) | `string`                                                                                                                                                                                                                                                                                                                    |
| **Returns**                                                                                                                                                                                       | the content disposition of the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)                                                                                                                               |
| [ContentEncoding](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata_1ab67ee76f19b347e61528ad66144da239)    | `string`                                                                                                                                                                                                                                                                                                                    |
| **Returns**                                                                                                                                                                                       | the content encoding for the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)                                                                                                                                 |
| [ContentLanguage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata_1a26b6571dbfa60f6871ea2c16aece810e)    | `string`                                                                                                                                                                                                                                                                                                                    |
| **Returns**                                                                                                                                                                                       | the content language for the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)                                                                                                                                 |
| [ContentType](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata_1a6e78c51121d44d5bdf248d963e931226)        | `string`                                                                                                                                                                                                                                                                                                                    |
| **Returns**                                                                                                                                                                                       | the content type of the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)                                                                                                                                      |
| [CreationTimeMillis](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata_1a8627fde5deeb4d786dfb05fe7671b369) | `DateTime`                                                                                                                                                                                                                                                                                                                  |
| **Returns**                                                                                                                                                                                       | the time the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) was created.                                                                                                                                    |
| [CustomMetadataKeys](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata_1a69bfa407a702451d7e7b8d63dec14a8d) | `IEnumerable< string >`                                                                                                                                                                                                                                                                                                     |
| **Returns**                                                                                                                                                                                       | the keys for custom metadata.                                                                                                                                                                                                                                                                                               |
| [Generation](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata_1a150bcac4d3fc8416b210e2af86f41010)         | `string`                                                                                                                                                                                                                                                                                                                    |
| **Returns**                                                                                                                                                                                       | a version String indicating what version of the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)                                                                                                              |
| [Md5Hash](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata_1a84a903b7ab7e190388f9d6ca4c34e6f9)            | `string`                                                                                                                                                                                                                                                                                                                    |
| **Returns**                                                                                                                                                                                       | the MD5Hash of the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) object                                                                                                                                    |
| [MetadataGeneration](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata_1af927b7c579f5c7b8987a713a65c13c0d) | `string`                                                                                                                                                                                                                                                                                                                    |
| **Returns**                                                                                                                                                                                       | a version String indicating the version of this [StorageMetadata](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata)                                                                                                                 |
| [Name](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata_1a5fa3113ec207308a66246eea8f260337)               | `string`                                                                                                                                                                                                                                                                                                                    |
| **Returns**                                                                                                                                                                                       | a simple name of the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) object                                                                                                                                  |
| [Path](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata_1aa381a7c949b4571e9f2f96c076f23833)               | `string`                                                                                                                                                                                                                                                                                                                    |
| **Returns**                                                                                                                                                                                       | the path of the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) object                                                                                                                                       |
| [Reference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata_1abf1f252dd1f3b333749f94f657df0e75)          | [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)                                                                                                                                                              |
| **Returns**                                                                                                                                                                                       | the associated [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) for which this metadata belongs to.                                                                                                           |
| [SizeBytes](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata_1a858ea9e2c436c9e36e3c6862883a8ec3)          | `long`                                                                                                                                                                                                                                                                                                                      |
| **Returns**                                                                                                                                                                                       | the stored Size in bytes of the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) object                                                                                                                       |
| [UpdatedTimeMillis](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata_1a4749025f058036c247ba6a614f0684fe)  | `DateTime`                                                                                                                                                                                                                                                                                                                  |
| **Returns**                                                                                                                                                                                       | the time the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) was last updated.                                                                                                                               |

|                                                                                                                                                                                                 ### Public functions                                                                                                                                                                                                  ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GetCustomMetadata](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata_1ad5104c064cef8bb2516f215c67dc8fee)`(string key)` | `string` Returns custom metadata for a [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) |

## Properties

### Bucket

```c#
string Bucket
```  
<br />

|                                                                                                                                                                 Details                                                                                                                                                                  ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | the owning Google Cloud [Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage) bucket for the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) |

### CacheControl

```c#
string CacheControl
```  
<br />

|                                                                                                   Details                                                                                                    ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | the Cache Control setting of the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) |

### ContentDisposition

```c#
string ContentDisposition
```  
<br />

|                                                                                                  Details                                                                                                   ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | the content disposition of the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) |

### ContentEncoding

```c#
string ContentEncoding
```  
<br />

|                                                                                                 Details                                                                                                  ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | the content encoding for the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) |

### ContentLanguage

```c#
string ContentLanguage
```  
<br />

|                                                                                                 Details                                                                                                  ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | the content language for the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) |

### ContentType

```c#
string ContentType
```  
<br />

|                                                                                               Details                                                                                               ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | the content type of the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) |

### CreationTimeMillis

```c#
DateTime CreationTimeMillis
```  
<br />

|                                                                                                Details                                                                                                ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | the time the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) was created. |

### CustomMetadataKeys

```c#
IEnumerable< string > CustomMetadataKeys
```  
<br />

|                  Details                   ||
|-------------|-------------------------------|
| **Returns** | the keys for custom metadata. |

### Generation

```c#
string Generation
```  
<br />

|                                                                                                           Details                                                                                                           ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | a version String indicating what version of the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) |

### Md5Hash

```c#
string Md5Hash
```  
<br />

|                                                                                                Details                                                                                                ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | the MD5Hash of the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) object |

### MetadataGeneration

```c#
string MetadataGeneration
```  
<br />

|                                                                                                         Details                                                                                                          ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | a version String indicating the version of this [StorageMetadata](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata) |

### Name

```c#
string Name
```  
<br />

|                                                                                                 Details                                                                                                 ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | a simple name of the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) object |

### Path

```c#
string Path
```  
<br />

|                                                                                              Details                                                                                               ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | the path of the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) object |

### Reference

```c#
StorageReference Reference
```  
<br />

|                                                                                                            Details                                                                                                             ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | the associated [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) for which this metadata belongs to. |

### SizeBytes

```c#
long SizeBytes
```  
<br />

|                                                                                                      Details                                                                                                       ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | the stored Size in bytes of the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) object |

### UpdatedTimeMillis

```c#
DateTime UpdatedTimeMillis
```  
<br />

|                                                                                                  Details                                                                                                   ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | the time the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) was last updated. |

## Public functions

### GetCustomMetadata

```c#
string GetCustomMetadata(
  string key
)
```  
Returns custom metadata for a [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)

<br />

|                                                                 Details                                                                  ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|---------------------------------------------------| | `key` | The key for which the metadata should be returned | |
| **Returns** | the metadata stored in the object the given key.                                                                            |

### StorageMetadata

```c#
 StorageMetadata()
```  
Creates a [StorageMetadata](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata) object to hold metadata for a [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)