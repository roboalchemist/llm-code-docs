# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata.md.txt

# firebase::storage::Metadata Class Reference

# firebase::storage::Metadata


`#include <metadata.h>`

[Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata) stores default attributes such as size and content type.

## Summary

[Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata) for a [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference). You may also store custom metadata key value pairs. [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata) values may be used to authorize operations using declarative validation rules.

| ### Constructors and Destructors ||
|---|---|
| [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1ace7d2bf647dc01f7700dc5d5e9b2274f)`()` Create a default [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata) that you can modify and use. ||
| [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1a9c42ec15427bbb24418700d9fab83990)`(const `[Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata)` & other)` Copy constructor. ||
| [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1acfac57ee4abe694bfb1d23fb3e4321fb)`(`[Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata)` && other)` Move constructor. ||
| [~Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1abe1d3ea0871c4c58209ccf00600c5193)`()` ||

|                                                                                                                                                                                                                                                                                                                                                                                                     ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                      ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GetReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1ac9fba3eae4f9d2aca868c2935834dd95)`() const `                                                                                                                                       | [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) Return the associated [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) to which this [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata) belongs. |
| [bucket](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1a00c1aa11121e1a5231f917a9fa7eb80d)`() const `                                                                                                                                             | `const char *` Return the owning Google Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) bucket for the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).                                                                                                                                              |
| [cache_control](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1a702329105778c957ffcd959555b81e79)`() const `                                                                                                                                      | `const char *` Return the Cache Control setting of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).                                                                                                                                                                                                                                                                                  |
| [content_disposition](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1a1164ff1dae996ff3fa5297a780d8bb54)`() const `                                                                                                                                | `const char *` Return the content disposition of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).                                                                                                                                                                                                                                                                                    |
| [content_encoding](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1a7c2522085c32794516761d44631ca424)`() const `                                                                                                                                   | `const char *` Return the content encoding for the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).                                                                                                                                                                                                                                                                                      |
| [content_language](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1a2d7e4ec2e3d3eebc8867813e391ab61a)`() const `                                                                                                                                   | `const char *` Return the content language for the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).                                                                                                                                                                                                                                                                                      |
| [content_type](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1aa25fe4486b6fb51dd67331b3dc1c8f12)`() const `                                                                                                                                       | `const char *` Return the content type of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).                                                                                                                                                                                                                                                                                           |
| [creation_time](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1a7dfdaf438cb599f3867b38558050acbe)`() const `                                                                                                                                      | `int64_t` Return the time the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) was created in milliseconds since the epoch.                                                                                                                                                                                                                                                               |
| [custom_metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1a18c8612ecf75d8cce4b706701c334f4c)`() const `                                                                                                                                    | `std::map< std::string, std::string > *` Return a map of custom metadata key value pairs.                                                                                                                                                                                                                                                                                                                                                                                                           |
| [generation](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1a603bba427a09bb192683e4054c0dd76e)`() const `                                                                                                                                         | `int64_t` Return a version String indicating what version of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).                                                                                                                                                                                                                                                                        |
| [is_valid](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1a1de55086d5ce9d4dd21fc0b75faa3bf4)`() const `                                                                                                                                           | `bool` Returns true if this [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata) is valid, false if it is not valid.                                                                                                                                                                                                                                                                                                    |
| [md5_hash](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1a482ac9732756535e27ddfa8d61c44a8d)`() const `                                                                                                                                           | `const char *` MD5 hash of the data; encoded using base64.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [metadata_generation](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1a33074233122b47b58a646d0afffa2be2)`() const `                                                                                                                                | `int64_t` Return a version String indicating the version of this StorageMetadata.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [name](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1a9177c03f56c2f7117f945268e792f7fa)`() const `                                                                                                                                               | `const char *` Return a simple name of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) object.                                                                                                                                                                                                                                                                                       |
| [operator=](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1ad03bb71775e63604181c6f574cacc7a9)`(const `[Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata)` & other)` | [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata)` &` Copy assignment operator.                                                                                                                                                                                                                                                                                                                                      |
| [operator=](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1a74708e2017781519392d899084cd7915)`(`[Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata)` && other)`      | [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata)` &` Move assignment operator.                                                                                                                                                                                                                                                                                                                                      |
| [path](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1a77affcbee510663453ce079596152957)`() const `                                                                                                                                               | `const char *` Return the path of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) object.                                                                                                                                                                                                                                                                                            |
| [set_cache_control](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1a2179e837f2d03e2d6555d1342c7834f3)`(const char *cache_control)`                                                                                                                | `void` Set the Cache Control setting of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).                                                                                                                                                                                                                                                                                             |
| [set_cache_control](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1abff9cbcd914196e5fe9d2a5577a76b78)`(const std::string & cache_control)`                                                                                                        | `void` Set the Cache Control setting of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).                                                                                                                                                                                                                                                                                             |
| [set_content_disposition](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1a2a8642236a6d82e3cdd48d438e13eb6b)`(const char *disposition)`                                                                                                            | `void` Set the content disposition of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).                                                                                                                                                                                                                                                                                               |
| [set_content_disposition](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1adf667a05bbe421755dcd427d756056df)`(const std::string & disposition)`                                                                                                    | `void` Set the content disposition of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).                                                                                                                                                                                                                                                                                               |
| [set_content_encoding](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1af891c3d461d633bfcc88bff60ee1d31c)`(const char *encoding)`                                                                                                                  | `void` Set the content encoding for the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).                                                                                                                                                                                                                                                                                                 |
| [set_content_encoding](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1a9ccdabbe6a896e0e5fbc8ed39ee3e865)`(const std::string & encoding)`                                                                                                          | `void` Set the content encoding for the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).                                                                                                                                                                                                                                                                                                 |
| [set_content_language](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1a9ac2901ec8afb0894d4d8a82378ced44)`(const char *language)`                                                                                                                  | `void` Set the content language for the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).                                                                                                                                                                                                                                                                                                 |
| [set_content_language](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1acf13debd3ac1478fee8c58b19c82c645)`(const std::string & language)`                                                                                                          | `void` Set the content language for the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).                                                                                                                                                                                                                                                                                                 |
| [set_content_type](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1affded2c5e3cd42b4f324aed8e6bb80fe)`(const char *type)`                                                                                                                          | `void` Set the content type of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).                                                                                                                                                                                                                                                                                                      |
| [set_content_type](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1a0a6e97bc82d682756e402a074e91292b)`(const std::string & type)`                                                                                                                  | `void` Set the content type of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).                                                                                                                                                                                                                                                                                                      |
| [size_bytes](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1a3b07c7d4f03dd93d8856917037716141)`() const `                                                                                                                                         | `int64_t` Return the stored Size in bytes of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) object.                                                                                                                                                                                                                                                                                 |
| [updated_time](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata_1ad749c66974ecfcef02083f66ad5793b7)`() const `                                                                                                                                       | `int64_t` Return the time the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) was last updated in milliseconds since the epoch.                                                                                                                                                                                                                                                          |

## Public functions

### GetReference

```c++
StorageReference GetReference() const 
```  
Return the associated [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) to which this [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata) belongs.

<br />

|                                                                                                                                                                                                                                                                                                                                                          Details                                                                                                                                                                                                                                                                                                                                                          ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The associated [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) to which this [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata) belongs. If this [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata) is invalid or is not associated with any file, an invalid [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) is returned. |

### Metadata

```c++
 Metadata()
```  
Create a default [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata) that you can modify and use.  

### Metadata

```c++
 Metadata(
  const Metadata & other
)
```  
Copy constructor.

<br />

|                                                                                                                                                                Details                                                                                                                                                                ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata) to copy from. | |

### Metadata

```c++
 Metadata(
  Metadata && other
)
```  
Move constructor.

Moving is an efficient operation for [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata).

<br />

|                                                                                                                                                                Details                                                                                                                                                                ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata) to move from. | |

### bucket

```c++
const char * bucket() const 
```  
Return the owning Google Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) bucket for the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).

<br />

|                                                                                                                                                                    Details                                                                                                                                                                    ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The owning Google Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) bucket for the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference). |

### cache_control

```c++
const char * cache_control() const 
```  
Return the Cache Control setting of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).


**See also:**
<https://tools.ietf.org/html/rfc7234#section-5.2>

|                                                                                                  Details                                                                                                  ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The Cache Control setting of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference). |

### content_disposition

```c++
const char * content_disposition() const 
```  
Return the content disposition of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).


**See also:**
<https://tools.ietf.org/html/rfc6266>

|                                                                                                 Details                                                                                                 ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The content disposition of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference). |

### content_encoding

```c++
const char * content_encoding() const 
```  
Return the content encoding for the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).


**See also:**
<https://tools.ietf.org/html/rfc2616#section-14.11>

|                                                                                                Details                                                                                                ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The content encoding for the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference). |

### content_language

```c++
const char * content_language() const 
```  
Return the content language for the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).


**See also:**
<https://tools.ietf.org/html/rfc2616#section-14.12>

|                                                                                                Details                                                                                                ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The content language for the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference). |

### content_type

```c++
const char * content_type() const 
```  
Return the content type of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).


**See also:**
<https://tools.ietf.org/html/rfc2616#section-14.17>

|                                                                                             Details                                                                                              ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The content type of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference). |

### creation_time

```c++
int64_t creation_time() const 
```  
Return the time the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) was created in milliseconds since the epoch.

<br />

|                                                                                                              Details                                                                                                              ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The time the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) was created in milliseconds since the epoch. |

### custom_metadata

```c++
std::map< std::string, std::string > * custom_metadata() const 
```  
Return a map of custom metadata key value pairs.

The pointer returned is only valid during the lifetime of the [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata) object that owns it.

<br />

|                  Details                   ||
|-------------|-------------------------------|
| **Returns** | The keys for custom metadata. |

### generation

```c++
int64_t generation() const 
```  
Return a version String indicating what version of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).

<br />

|                                                                                                    Details                                                                                                     ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A value indicating the version of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference). |

### is_valid

```c++
bool is_valid() const 
```  
Returns true if this [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata) is valid, false if it is not valid.

An invalid [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata) is returned when a method such as [StorageReference::GetMetadata()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a78a50874c5ee78f5774734af1975c5d8) completes with an error.

<br />

|                                                                                                                                                             Details                                                                                                                                                             ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | true if this [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata) is valid, false if this [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata) is invalid. |

### md5_hash

```c++
const char * md5_hash() const 
```  
MD5 hash of the data; encoded using base64.

<br />

|                         Details                          ||
|-------------|---------------------------------------------|
| **Returns** | MD5 hash of the data; encoded using base64. |

### metadata_generation

```c++
int64_t metadata_generation() const 
```  
Return a version String indicating the version of this StorageMetadata.

<br />

|                               Details                                ||
|-------------|---------------------------------------------------------|
| **Returns** | A value indicating the version of this StorageMetadata. |

### name

```c++
const char * name() const 
```  
Return a simple name of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) object.

<br />

|                                                                                               Details                                                                                                ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A simple name of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) object. |

### operator=

```c++
Metadata & operator=(
  const Metadata & other
)
```  
Copy assignment operator.

<br />

|                                                                                                                                                                Details                                                                                                                                                                 ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata) to copy from. | |
| **Returns** | Reference to the destination [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata).                                                                                                                                                            |

### operator=

```c++
Metadata & operator=(
  Metadata && other
)
```  
Move assignment operator.

Moving is an efficient operation for [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata).

<br />

|                                                                                                                                                                Details                                                                                                                                                                 ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata) to move from. | |
| **Returns** | Reference to the destination [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata).                                                                                                                                                            |

### path

```c++
const char * path() const 
```  
Return the path of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) object.

<br />

|                                                                                             Details                                                                                             ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The path of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) object. |

### set_cache_control

```c++
void set_cache_control(
  const char *cache_control
)
```  
Set the Cache Control setting of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).


**See also:**
<https://tools.ietf.org/html/rfc7234#section-5.2>  

### set_cache_control

```c++
void set_cache_control(
  const std::string & cache_control
)
```  
Set the Cache Control setting of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).


**See also:**
<https://tools.ietf.org/html/rfc7234#section-5.2>  

### set_content_disposition

```c++
void set_content_disposition(
  const char *disposition
)
```  
Set the content disposition of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).


**See also:**
<https://tools.ietf.org/html/rfc6266>  

### set_content_disposition

```c++
void set_content_disposition(
  const std::string & disposition
)
```  
Set the content disposition of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).


**See also:**
<https://tools.ietf.org/html/rfc6266>  

### set_content_encoding

```c++
void set_content_encoding(
  const char *encoding
)
```  
Set the content encoding for the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).


**See also:**
<https://tools.ietf.org/html/rfc2616#section-14.11>  

### set_content_encoding

```c++
void set_content_encoding(
  const std::string & encoding
)
```  
Set the content encoding for the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).


**See also:**
<https://tools.ietf.org/html/rfc2616#section-14.11>  

### set_content_language

```c++
void set_content_language(
  const char *language
)
```  
Set the content language for the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).


**See also:**
<https://tools.ietf.org/html/rfc2616#section-14.12>  

### set_content_language

```c++
void set_content_language(
  const std::string & language
)
```  
Set the content language for the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).

This must be an ISO 639-1 two-letter language code. E.g. "zh", "es", "en".


**See also:**
<https://www.loc.gov/standards/iso639-2/php/code_list.php>  

### set_content_type

```c++
void set_content_type(
  const char *type
)
```  
Set the content type of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).


**See also:**
<https://tools.ietf.org/html/rfc2616#section-14.17>  

### set_content_type

```c++
void set_content_type(
  const std::string & type
)
```  
Set the content type of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).


**See also:**
<https://tools.ietf.org/html/rfc2616#section-14.17>  

### size_bytes

```c++
int64_t size_bytes() const 
```  
Return the stored Size in bytes of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) object.

<br />

|                                                                                                     Details                                                                                                     ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The stored Size in bytes of the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) object. |

### updated_time

```c++
int64_t updated_time() const 
```  
Return the time the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) was last updated in milliseconds since the epoch.

<br />

|                                                                                                                Details                                                                                                                 ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The time the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) was last updated in milliseconds since the epoch. |

### \~Metadata

```c++
 ~Metadata()
```