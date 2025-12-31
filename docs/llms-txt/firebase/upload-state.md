# Source: https://firebase.google.com/docs/reference/unity/class/firebase/storage/upload-state.md.txt

# Firebase.Storage.UploadState Class Reference

# Firebase.Storage.UploadState

[UploadState](https://firebase.google.com/docs/reference/unity/class/firebase/storage/upload-state#class_firebase_1_1_storage_1_1_upload_state) contains information for an upload in progress.

## Summary

|                                                                                                                                                                                                                                                                         ### Properties                                                                                                                                                                                                                                                                          ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [BytesTransferred](https://firebase.google.com/docs/reference/unity/class/firebase/storage/upload-state#class_firebase_1_1_storage_1_1_upload_state_1abf5c9c32b9fc1cd0e136fbc55e41648d) | `long` The total number of bytes uploaded so far.                                                                                                                                                                                                                                                                                                                      |
| [Metadata](https://firebase.google.com/docs/reference/unity/class/firebase/storage/upload-state#class_firebase_1_1_storage_1_1_upload_state_1a474366246e517e1b921632a53c21bc94)         | [StorageMetadata](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata)                                                                                                                                                                                                            |
| **Returns**                                                                                                                                                                             | the metadata for the object.                                                                                                                                                                                                                                                                                                                                           |
| [Reference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/upload-state#class_firebase_1_1_storage_1_1_upload_state_1a14817f7ea66637c46824ff72498093f5)        | [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) Returns the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) associated with this upload. |
| [TotalByteCount](https://firebase.google.com/docs/reference/unity/class/firebase/storage/upload-state#class_firebase_1_1_storage_1_1_upload_state_1a5cafb0080919af0de4fc2886cc7fb8b4)   | `long` The total number of bytes to upload.                                                                                                                                                                                                                                                                                                                            |
| [UploadSessionUri](https://firebase.google.com/docs/reference/unity/class/firebase/storage/upload-state#class_firebase_1_1_storage_1_1_upload_state_1a397d1e3b789456f6cda7676a5d22340c) | `Uri`                                                                                                                                                                                                                                                                                                                                                                  |
| **Returns**                                                                                                                                                                             | the session Uri, valid for approximately one week, which can be used to resume an upload later by passing this value into an upload.                                                                                                                                                                                                                                   |

## Properties

### BytesTransferred

```c#
long BytesTransferred
```  
The total number of bytes uploaded so far.

<br />

|                         Details                         ||
|-------------|--------------------------------------------|
| **Returns** | the total number of bytes uploaded so far. |

### Metadata

```c#
StorageMetadata Metadata
```  
<br />

|                  Details                  ||
|-------------|------------------------------|
| **Returns** | the metadata for the object. |

After uploading, this will return the resulting final Metadata which will include the upload URL.  

### Reference

```c#
StorageReference Reference
```  
Returns the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) associated with this upload.

<br />

|                                                                                                   Details                                                                                                    ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) associated with this upload. |

### TotalByteCount

```c#
long TotalByteCount
```  
The total number of bytes to upload.

<br />

|                                    Details                                     ||
|-------------|-------------------------------------------------------------------|
| **Returns** | the total number of bytes to upload or -1 if the size is unknown. |

### UploadSessionUri

```c#
Uri UploadSessionUri
```  
<br />

|                                                                      Details                                                                      ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | the session Uri, valid for approximately one week, which can be used to resume an upload later by passing this value into an upload. |