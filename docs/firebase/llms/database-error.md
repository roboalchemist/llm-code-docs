# Source: https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error.md.txt

# Firebase.Database.DatabaseError Class Reference

# Firebase.Database.DatabaseError

Instances of [DatabaseError](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error) are passed within event arguments when an operation failed.

## Summary

Instances of [DatabaseError](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error) are passed to callbacks when an operation failed. They contain a description of the specific error that occurred.

|                                                                                                                                ### Public attributes                                                                                                                                ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [Disconnected](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error_1a3978feb45e8710ac332006e21c78a898)` = -4`       | `const int` The operation had to be aborted due to a network disconnect.    |
| [ExpiredToken](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error_1a80749131bf858642f58114a43e338b20)` = -6`       | `const int` The supplied auth token has expired.                            |
| [InvalidToken](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error_1a02e0d23443e7c78dc3a109fc8d3a8032)` = -7`       | `const int` The specified authentication token is invalid.                  |
| [MaxRetries](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error_1ab24ff9b6f7518aea37bb793f3ddc7c59)` = -8`         | `const int` The transaction had too many retries.                           |
| [NetworkError](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error_1a9e21f25df86ce9cca32daeb374a2afe8)` = -24`      | `const int` The operation could not be performed due to a network error.    |
| [OperationFailed](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error_1a2b3e9bba2ddf2fb7debc9f13dd695f6d)` = -2`    | `const int` The server indicated that this operation failed.                |
| [OverriddenBySet](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error_1a9735af52f0b3611bc0c74e756e8383fc)` = -9`    | `const int` The transaction was overridden by a subsequent set.             |
| [PermissionDenied](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error_1a2113f0a91d75b7709fa368e418cb4983)` = -3`   | `const int` This client does not have permission to perform this operation. |
| [Unavailable](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error_1aaccb31bbf09037bc92c5a7467027d271)` = -10`       | `const int` The service is unavailable.                                     |
| [UnknownError](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error_1aa51169d8c4b46b2c024ea9b80d030ce3)` = -999`     | `const int` An unknown error occurred.                                      |
| [UserCodeException](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error_1a5ff89ea327ab4d1a142f0f46865f47b6)` = -11` | `const int` An exception occurred in user code.                             |
| [WriteCanceled](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error_1a52e1b14858e0219737051f2dce2154df)` = -25`     | `const int` The write was canceled locally.                                 |

|                                                                                                                                                                                                    ### Properties                                                                                                                                                                                                    ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Code](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error_1a56c757dfeb8a1777c976b28dccbce42b)    | `int`                                                                                                                                                                                                                          |
| **Returns**                                                                                                                                                                          | One of the defined status codes declared under [DatabaseError](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error), depending on the error |
| [Details](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error_1a8e8bdd604e6509729d53c04e0bd483d6) | `string`                                                                                                                                                                                                                       |
| **Returns**                                                                                                                                                                          | Human-readable details on the error and additional information.                                                                                                                                                                |
| [Message](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error_1affd00817e333be43c9137d6dad40d121) | `string`                                                                                                                                                                                                                       |
| **Returns**                                                                                                                                                                          | A human-readable description of the error                                                                                                                                                                                      |

|                                                                                                                                                                                                                                                                                                                            ### Public functions                                                                                                                                                                                                                                                                                                                             ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ToException](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error_1a06a15ba14894ead260579959696e1a6c)`()` | [DatabaseException](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-exception#class_firebase_1_1_database_1_1_database_exception) Can be used if a third party needs an Exception from [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) for integration purposes. |
| [ToString](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error_1af92b7d70968c32c61400e5bbb8a75190)`()`    | `override string`                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## Public attributes

### Disconnected

```c#
const int Disconnected = -4
```  
The operation had to be aborted due to a network disconnect.  

### ExpiredToken

```c#
const int ExpiredToken = -6
```  
The supplied auth token has expired.  

### InvalidToken

```c#
const int InvalidToken = -7
```  
The specified authentication token is invalid.

The specified authentication token is invalid. This can occur when the token is malformed, expired, or the secret that was used to generate it has been revoked.  

### MaxRetries

```c#
const int MaxRetries = -8
```  
The transaction had too many retries.  

### NetworkError

```c#
const int NetworkError = -24
```  
The operation could not be performed due to a network error.  

### OperationFailed

```c#
const int OperationFailed = -2
```  
The server indicated that this operation failed.  

### OverriddenBySet

```c#
const int OverriddenBySet = -9
```  
The transaction was overridden by a subsequent set.  

### PermissionDenied

```c#
const int PermissionDenied = -3
```  
This client does not have permission to perform this operation.  

### Unavailable

```c#
const int Unavailable = -10
```  
The service is unavailable.  

### UnknownError

```c#
const int UnknownError = -999
```  
An unknown error occurred.

An unknown error occurred. Please refer to the error message and error details for more information.  

### UserCodeException

```c#
const int UserCodeException = -11
```  
An exception occurred in user code.  

### WriteCanceled

```c#
const int WriteCanceled = -25
```  
The write was canceled locally.

## Properties

### Code

```c#
int Code
```  
<br />

|                                                                                                                   Details                                                                                                                   ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | One of the defined status codes declared under [DatabaseError](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-error#class_firebase_1_1_database_1_1_database_error), depending on the error |

### Details

```c#
string Details
```  
<br />

|                                   Details                                    ||
|-------------|-----------------------------------------------------------------|
| **Returns** | Human-readable details on the error and additional information. |

### Message

```c#
string Message
```  
<br />

|                        Details                         ||
|-------------|-------------------------------------------|
| **Returns** | A human-readable description of the error |

## Public functions

### ToException

```c#
DatabaseException ToException()
```  
Can be used if a third party needs an Exception from [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database#namespace_firebase_1_1_database) for integration purposes.

<br />

|                                            Details                                             ||
|-------------|-----------------------------------------------------------------------------------|
| **Returns** | An exception wrapping this error, with an appropriate message and no stack trace. |

### ToString

```c#
override string ToString()
```