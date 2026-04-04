# Source: https://firebase.google.com/docs/reference/unity/class/firebase/storage/download-state.md.txt

# Firebase.Storage.DownloadState Class Reference

# Firebase.Storage.DownloadState

[DownloadState](https://firebase.google.com/docs/reference/unity/class/firebase/storage/download-state#class_firebase_1_1_storage_1_1_download_state) contains information for a download in progress.

## Summary

It is sent to a StorageProgress handler during the operation.

|                                                                                                                                                                                                                                                                            ### Properties                                                                                                                                                                                                                                                                             ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [BytesTransferred](https://firebase.google.com/docs/reference/unity/class/firebase/storage/download-state#class_firebase_1_1_storage_1_1_download_state_1aa44d93d22909420964fa83194e67d152) | `long` The total number of bytes downloaded so far.                                                                                                                                                                                                                                                                                                                      |
| [Reference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/download-state#class_firebase_1_1_storage_1_1_download_state_1a02f50301ed03af0465c7ad4897890ee0)        | [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) Returns the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) associated with this download. |
| [TotalByteCount](https://firebase.google.com/docs/reference/unity/class/firebase/storage/download-state#class_firebase_1_1_storage_1_1_download_state_1ad6fed86074c174a64873b52fe1936731)   | `long` The total number of bytes to download.                                                                                                                                                                                                                                                                                                                            |

## Properties

### BytesTransferred

```c#
long BytesTransferred
```  
The total number of bytes downloaded so far.

<br />

|                          Details                          ||
|-------------|----------------------------------------------|
| **Returns** | the total number of bytes downloaded so far. |

### Reference

```c#
StorageReference Reference
```  
Returns the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) associated with this download.

<br />

|                                                                                                    Details                                                                                                     ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | the [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) associated with this download. |

### TotalByteCount

```c#
long TotalByteCount
```  
The total number of bytes to download.

<br />

|                                     Details                                      ||
|-------------|---------------------------------------------------------------------|
| **Returns** | The total number of bytes to download or -1 if the size is unknown. |