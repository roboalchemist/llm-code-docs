# Source: https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-exception.md.txt

# Firebase.Storage.StorageException Class Reference

# Firebase.Storage.StorageException

Represents an Exception resulting from an operation on a [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)

## Summary

### Inheritance

Inherits from: Exception

|                                                                                                                                    ### Public attributes                                                                                                                                     ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [ErrorBucketNotFound](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-exception#class_firebase_1_1_storage_1_1_storage_exception_1acd74645df5b29b0fb21a3101b3cb3375)` = -13011`     | `const int`                                                             |
| **Returns**                                                                                                                                                                                                         | The specified bucket could not be found on the server.                  |
| [ErrorCanceled](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-exception#class_firebase_1_1_storage_1_1_storage_exception_1a4fe1b1089fcbd021af9acdb6e4c8806b)` = -13040`           | `const int`                                                             |
| **Returns**                                                                                                                                                                                                         | The operation was canceled from the client.                             |
| [ErrorInvalidChecksum](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-exception#class_firebase_1_1_storage_1_1_storage_exception_1afa1979bc1ac1d96b1e2a7dbda4017114)` = -13031`    | `const int`                                                             |
| **Returns**                                                                                                                                                                                                         | There was an error validating the operation due to a checksum failure.  |
| [ErrorNotAuthenticated](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-exception#class_firebase_1_1_storage_1_1_storage_exception_1abdbb7d69c70f28441420855b55fb52d7)` = -13020`   | `const int`                                                             |
| **Returns**                                                                                                                                                                                                         | The given signin credentials are not valid.                             |
| [ErrorNotAuthorized](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-exception#class_firebase_1_1_storage_1_1_storage_exception_1ae51f3cf28bc5b4ce36712e68bb6ba719)` = -13021`      | `const int`                                                             |
| **Returns**                                                                                                                                                                                                         | The given signin credentials are not allowed to perform this operation. |
| [ErrorObjectNotFound](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-exception#class_firebase_1_1_storage_1_1_storage_exception_1ae2725c102c1d563a9174bc93452e14e6)` = -13010`     | `const int`                                                             |
| **Returns**                                                                                                                                                                                                         | The specified object could not be found on the server.                  |
| [ErrorProjectNotFound](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-exception#class_firebase_1_1_storage_1_1_storage_exception_1a2f2de8422da0a17332453b3dcf449ebf)` = -13012`    | `const int`                                                             |
| **Returns**                                                                                                                                                                                                         | The specified project could not be found on the server.                 |
| [ErrorQuotaExceeded](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-exception#class_firebase_1_1_storage_1_1_storage_exception_1abb7d2fb532ed0a55069f5ab847f733af)` = -13013`      | `const int`                                                             |
| **Returns**                                                                                                                                                                                                         | Free Tier quota has been exceeded.                                      |
| [ErrorRetryLimitExceeded](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-exception#class_firebase_1_1_storage_1_1_storage_exception_1ad16fe19d9b3dc978a8a884c358346748)` = -13030` | `const int`                                                             |
| **Returns**                                                                                                                                                                                                         | The retry timeout was exceeded.                                         |
| [ErrorUnknown](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-exception#class_firebase_1_1_storage_1_1_storage_exception_1a95bac5ecad71639f3137d396f0b70514)` = -13000`            | `const int`                                                             |
| **Returns**                                                                                                                                                                                                         | An unknown error has occurred.                                          |

|                                                                                                                                              ### Properties                                                                                                                                               ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [ErrorCode](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-exception#class_firebase_1_1_storage_1_1_storage_exception_1a764390d9bc195f25ad8f6cbfc641918b)              | `int`                                                                                            |
| **Returns**                                                                                                                                                                                             | A code that indicates the type of error that occurred.                                           |
| [HttpResultCode](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-exception#class_firebase_1_1_storage_1_1_storage_exception_1a6325f13b8c24f6380f533e40eb0773ea)         | `int`                                                                                            |
| **Returns**                                                                                                                                                                                             | the Http result code (if one exists) from a network operation.                                   |
| [IsRecoverableException](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-exception#class_firebase_1_1_storage_1_1_storage_exception_1acb90bf876161e54fe2b4a6243a0c261d) | `bool`                                                                                           |
| **Returns**                                                                                                                                                                                             | True if this request failed due to a network condition that may be resolved in a future attempt. |

## Public attributes

### ErrorBucketNotFound

```c#
const int ErrorBucketNotFound = -13011
```  
<br />

|                               Details                               ||
|-------------|--------------------------------------------------------|
| **Returns** | The specified bucket could not be found on the server. |

### ErrorCanceled

```c#
const int ErrorCanceled = -13040
```  
<br />

|                         Details                          ||
|-------------|---------------------------------------------|
| **Returns** | The operation was canceled from the client. |

### ErrorInvalidChecksum

```c#
const int ErrorInvalidChecksum = -13031
```  
<br />

|                                       Details                                       ||
|-------------|------------------------------------------------------------------------|
| **Returns** | There was an error validating the operation due to a checksum failure. |

### ErrorNotAuthenticated

```c#
const int ErrorNotAuthenticated = -13020
```  
<br />

|                         Details                          ||
|-------------|---------------------------------------------|
| **Returns** | The given signin credentials are not valid. |

### ErrorNotAuthorized

```c#
const int ErrorNotAuthorized = -13021
```  
<br />

|                                       Details                                        ||
|-------------|-------------------------------------------------------------------------|
| **Returns** | The given signin credentials are not allowed to perform this operation. |

### ErrorObjectNotFound

```c#
const int ErrorObjectNotFound = -13010
```  
<br />

|                               Details                               ||
|-------------|--------------------------------------------------------|
| **Returns** | The specified object could not be found on the server. |

### ErrorProjectNotFound

```c#
const int ErrorProjectNotFound = -13012
```  
<br />

|                               Details                                ||
|-------------|---------------------------------------------------------|
| **Returns** | The specified project could not be found on the server. |

### ErrorQuotaExceeded

```c#
const int ErrorQuotaExceeded = -13013
```  
<br />

|                     Details                     ||
|-------------|------------------------------------|
| **Returns** | Free Tier quota has been exceeded. |

Change your pricing plan to avoid this error.  

### ErrorRetryLimitExceeded

```c#
const int ErrorRetryLimitExceeded = -13030
```  
<br />

|                   Details                    ||
|-------------|---------------------------------|
| **Returns** | The retry timeout was exceeded. |

Check your network connection or increase the value of one of [FirebaseStorage.MaxDownloadRetryTime](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage_1a695239fdc4c02b07c4f01a3822484bd1)[FirebaseStorage.MaxUploadRetryTime](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage_1a12c02bd2493bb86377c12dd736888709) or [FirebaseStorage.MaxOperationRetryTime](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage_1a0135c615d2a372ad5fece765c95f9c85)  

### ErrorUnknown

```c#
const int ErrorUnknown = -13000
```  
<br />

|                   Details                   ||
|-------------|--------------------------------|
| **Returns** | An unknown error has occurred. |

See the inner exception or [StorageException.HttpResultCode](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-exception#class_firebase_1_1_storage_1_1_storage_exception_1a6325f13b8c24f6380f533e40eb0773ea) for more information.

## Properties

### ErrorCode

```c#
int ErrorCode
```  
<br />

|                               Details                               ||
|-------------|--------------------------------------------------------|
| **Returns** | A code that indicates the type of error that occurred. |

This value will be one of the set of constants defined on [StorageException](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-exception#class_firebase_1_1_storage_1_1_storage_exception).  

### HttpResultCode

```c#
int HttpResultCode
```  
<br />

|                                   Details                                   ||
|-------------|----------------------------------------------------------------|
| **Returns** | the Http result code (if one exists) from a network operation. |

### IsRecoverableException

```c#
bool IsRecoverableException
```  
<br />

|                                                    Details                                                    ||
|-------------|--------------------------------------------------------------------------------------------------|
| **Returns** | True if this request failed due to a network condition that may be resolved in a future attempt. |