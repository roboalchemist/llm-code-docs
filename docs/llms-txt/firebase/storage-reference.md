# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference.md.txt

# Firebase.Storage.StorageReference Class Reference

# Firebase.Storage.StorageReference

Represents a reference to a Google Cloud [Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage) object.

## Summary

Represents a reference to a Google Cloud [Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage) object. Developers can upload and download objects, get/set object metadata, and delete an object at a specified path. (see [Google Cloud Storage](https://cloud.google.com/storage/))

|                                                                                                                                                                                                                                                                                                              ### Properties                                                                                                                                                                                                                                                                                                              ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Bucket](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference_1af002e71a87295594ec1f341810d231d2)  | `string` Return the Google Cloud [Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage) bucket that holds this object.                                                                                                                                                                                                                                                          |
| [Name](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference_1a2fd65ce408caa7404b15abfa41dd6eee)    | `string` Returns the short name of this object.                                                                                                                                                                                                                                                                                                                                                                                                |
| [Parent](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference_1a838c36ff815801001403983e4da24e4c)  | [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) Returns a new instance of [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) pointing to the parent location or null if this instance references the root location. |
| [Path](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference_1a60cd962a2c1de6b89ab6bf108a0f8207)    | `string` Returns the full path to this object, not including the Google Cloud [Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage) bucket.                                                                                                                                                                                                                                    |
| [Root](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference_1a30cfc2e5d0d72d3a60b62f1d6bf3f8c8)    | [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) Returns a new instance of [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) pointing to the root location.                                                         |
| [Storage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference_1acdd2c8c8b8762fd36349f848d5262a1b) | [FirebaseStorage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage) Returns the [FirebaseStorage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage) service which created this reference.                                                                      |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Child](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference_1abe51229f1470a55d43bd11894cd99120)`(string pathString)`                                                                                                                                                                                                                                                                                                                                                                                                                        | [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) Returns a new instance of [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) pointing to a child location of the current reference.                |
| [DeleteAsync](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference_1a005239a2305b6ccdbde6e6d57532bef2)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                   | `Task` Deletes the object at this [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)                                                                                                                                                                                                                              |
| [Equals](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference_1a4897eff45918a5442a2262227c239380)`(object other)`                                                                                                                                                                                                                                                                                                                                                                                                                            | `override bool` Compares two storage reference URIs.                                                                                                                                                                                                                                                                                                                                                                          |
| [GetBytesAsync](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference_1a53e2c704e19dc27f4ba9ec7fe4d30c14)`(long maxDownloadSizeBytes)`                                                                                                                                                                                                                                                                                                                                                                                                        | `Task< byte[]>` Downloads the object from this [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) A byte array will be allocated large enough to hold the entire file in memory.                                                                                                                                  |
| [GetBytesAsync](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference_1a9b672f13901eff36d70debb650e3bf33)`(long maxDownloadSizeBytes, IProgress< `[DownloadState](https://firebase.google.com/docs/reference/unity/class/firebase/storage/download-state#class_firebase_1_1_storage_1_1_download_state)` > progressHandler, CancellationToken cancelToken)`                                                                                                                                                                                   | `Task< byte[]>` Downloads the object from this [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) A byte array will be allocated large enough to hold the entire file in memory.                                                                                                                                  |
| [GetDownloadUrlAsync](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference_1af5c73d78af7ccab6812cb0aaa2043ee4)`()`                                                                                                                                                                                                                                                                                                                                                                                                                           | `Task< Uri >` Retrieves a long lived download URL with a revokable token.                                                                                                                                                                                                                                                                                                                                                     |
| [GetFileAsync](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference_1a508211331c961b5af65c6da8132ef59a)`(string destinationFilePath, IProgress< `[DownloadState](https://firebase.google.com/docs/reference/unity/class/firebase/storage/download-state#class_firebase_1_1_storage_1_1_download_state)` > progressHandler, CancellationToken cancelToken)`                                                                                                                                                                                   | `Task` Downloads the object at this [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) to a specified system filepath.                                                                                                                                                                                            |
| [GetHashCode](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference_1a02cb506cd3ef02ca1c1b4e0edc9561a0)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                   | `override int` Create a hash of the URI string used by this reference.                                                                                                                                                                                                                                                                                                                                                        |
| [GetMetadataAsync](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference_1a3c3eabdda76c874f5808f469c7dc66d1)`()`                                                                                                                                                                                                                                                                                                                                                                                                                              | `Task< `[StorageMetadata](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata)` >` Retrieves metadata associated with an object at this [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)                                   |
| [GetStreamAsync](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference_1ad607e5da989038b2d8b4088a24f78587)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                | `Task< Stream >` Downloads the object at this [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) via a Stream The resulting InputStream should be not be accessed on the main thread because calling into it may block the calling thread.                                                                        |
| [GetStreamAsync](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference_1aca2eef44c28082df303f99e75823be2f)`(Action< Stream > streamProcessor, IProgress< `[DownloadState](https://firebase.google.com/docs/reference/unity/class/firebase/storage/download-state#class_firebase_1_1_storage_1_1_download_state)` > progressHandler, CancellationToken cancelToken)`                                                                                                                                                                           | `Task` Downloads the object at this [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) via a Stream                                                                                                                                                                                                               |
| [PutBytesAsync](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference_1a125ad4ed3d2ce7509c63627804cd668c)`(byte[] bytes, `[MetadataChange](https://firebase.google.com/docs/reference/unity/class/firebase/storage/metadata-change#class_firebase_1_1_storage_1_1_metadata_change)` customMetadata, IProgress< `[UploadState](https://firebase.google.com/docs/reference/unity/class/firebase/storage/upload-state#class_firebase_1_1_storage_1_1_upload_state)` > progressHandler, CancellationToken cancelToken, Uri previousSessionUri)`   | `Task< `[StorageMetadata](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata)` >` Uploads byte data to this [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) This is not recommended for large files.                     |
| [PutFileAsync](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference_1a0b6fee3e69ca0b004e8675f7d867d925)`(string filePath, `[MetadataChange](https://firebase.google.com/docs/reference/unity/class/firebase/storage/metadata-change#class_firebase_1_1_storage_1_1_metadata_change)` customMetadata, IProgress< `[UploadState](https://firebase.google.com/docs/reference/unity/class/firebase/storage/upload-state#class_firebase_1_1_storage_1_1_upload_state)` > progressHandler, CancellationToken cancelToken, Uri previousSessionUri)` | `Task< `[StorageMetadata](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata)` >` Uploads from a content URI to this [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)                                                     |
| [PutStreamAsync](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference_1ad56641c76062cab644031624802c034d)`(Stream stream, `[MetadataChange](https://firebase.google.com/docs/reference/unity/class/firebase/storage/metadata-change#class_firebase_1_1_storage_1_1_metadata_change)` customMetadata, IProgress< `[UploadState](https://firebase.google.com/docs/reference/unity/class/firebase/storage/upload-state#class_firebase_1_1_storage_1_1_upload_state)` > progressHandler, CancellationToken cancelToken, Uri previousSessionUri)` | `Task< `[StorageMetadata](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata)` >` Uploads a stream of data to this [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) The stream will remain open at the end of the upload. |
| [ToString](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference_1a2d3174e239a7d683ee338ca5f6ddbb1a)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                      | `override string`                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Returns**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | This object in URI form, which can then be shared and passed into [FirebaseStorage.GetReferenceFromUrl](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage_1a42867cc9a73277ca6a8ff92595dd1cdf)                                                                                                                                          |
| [UpdateMetadataAsync](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference_1a4763f4a82ead4d28ad011eab6adfa41d)`(`[MetadataChange](https://firebase.google.com/docs/reference/unity/class/firebase/storage/metadata-change#class_firebase_1_1_storage_1_1_metadata_change)` metadata)`                                                                                                                                                                                                                                                        | `Task< `[StorageMetadata](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata)` >` Updates the metadata associated with this [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)                                              |

## Properties

### Bucket

```c#
string Bucket
```  
Return the Google Cloud [Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage) bucket that holds this object.

<br />

|         Details          ||
|-------------|-------------|
| **Returns** | the bucket. |

### Name

```c#
string Name
```  
Returns the short name of this object.

<br />

|        Details         ||
|-------------|-----------|
| **Returns** | the name. |

### Parent

```c#
StorageReference Parent
```  
Returns a new instance of [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) pointing to the parent location or null if this instance references the root location.

For example:  


          path = foo/bar/baz   parent = foo/bar
          path = foo           parent = (root)
          path = (root)        parent = (null)
        
<br />

<br />

|                                                                                        Details                                                                                         ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | the parent [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) |

### Path

```c#
string Path
```  
Returns the full path to this object, not including the Google Cloud [Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage) bucket.

<br />

|        Details         ||
|-------------|-----------|
| **Returns** | the path. |

### Root

```c#
StorageReference Root
```  
Returns a new instance of [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) pointing to the root location.

<br />

|                                                                                       Details                                                                                        ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | the root [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) |

### Storage

```c#
FirebaseStorage Storage
```  
Returns the [FirebaseStorage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage) service which created this reference.

<br />

|                                                                                        Details                                                                                        ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The [FirebaseStorage](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage) service. |

## Public functions

### Child

```c#
StorageReference Child(
  string pathString
)
```  
Returns a new instance of [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) pointing to a child location of the current reference.

All leading and trailing slashes will be removed, and consecutive slashes will be compressed to single slashes. For example:  


          child = /foo/bar     path = foo/bar
          child = foo/bar/     path = foo/bar
          child = foo///bar    path = foo/bar
        
<br />

<br />

|                                                                                        Details                                                                                        ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------------|----------------------------------------| | `pathString` | The relative path from this reference. |                                                      |
| **Returns** | the child [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) |

### DeleteAsync

```c#
Task DeleteAsync()
```  
Deletes the object at this [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)

<br />

|                                        Details                                        ||
|-------------|--------------------------------------------------------------------------|
| **Returns** | A Task which can be used to monitor the operation and obtain the result. |

### Equals

```c#
override bool Equals(
  object other
)
```  
Compares two storage reference URIs.

<br />

|                                   Details                                    ||
|-------------|-----------------------------------------------------------------|
| **Returns** | true if two references point to the same path, false otherwise. |

### GetBytesAsync

```c#
Task< byte[]> GetBytesAsync(
  long maxDownloadSizeBytes
)
```  
Downloads the object from this [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) A byte array will be allocated large enough to hold the entire file in memory.

Therefore, using this method will impact memory usage of your process. If you are downloading many large files, GetStream(StreamDownloadTask.StreamProcessor)

may be a better option.

<br />

|                                                                                                                                                                                                                                                                                 Details                                                                                                                                                                                                                                                                                  ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `maxDownloadSizeBytes` | The maximum allowed size in bytes that will be allocated. Set this parameter to prevent out of memory conditions from occurring. If the download exceeds this limit, the task will fail and an System.IndexOutOfRangeException will be returned. | |
| **Returns** | A Task which can be used to monitor the operation and obtain the result.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

### GetBytesAsync

```c#
Task< byte[]> GetBytesAsync(
  long maxDownloadSizeBytes,
  IProgress< DownloadState > progressHandler,
  CancellationToken cancelToken
)
```  
Downloads the object from this [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) A byte array will be allocated large enough to hold the entire file in memory.

Therefore, using this method will impact memory usage of your process. If you are downloading many large files, GetStream(StreamDownloadTask.StreamProcessor)

may be a better option.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `maxDownloadSizeBytes` | The maximum allowed size in bytes that will be allocated. Set this parameter to prevent out of memory conditions from occurring. If the download exceeds this limit, the task will fail and an System.IndexOutOfRangeException will be returned. | | `progressHandler`      | usually an instance of StorageProgress that will receive periodic updates during the operation. This value can be null.                                                                                                                          | | `cancelToken`          | A CancellationToken to control the operation and possibly later cancel it. This value may be CancellationToken.None to indicate no value.                                                                                                        | |
| **Returns** | A Task which can be used to monitor the operation and obtain the result.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

### GetDownloadUrlAsync

```c#
Task< Uri > GetDownloadUrlAsync()
```  
Retrieves a long lived download URL with a revokable token.

Retrieves a long lived download URL with a revokable token. This can be used to share the file with others, but can be revoked by a developer in the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) Console if desired.

<br />

|                                        Details                                        ||
|-------------|--------------------------------------------------------------------------|
| **Returns** | A Task which can be used to monitor the operation and obtain the result. |

### GetFileAsync

```c#
Task GetFileAsync(
  string destinationFilePath,
  IProgress< DownloadState > progressHandler,
  CancellationToken cancelToken
)
```  
Downloads the object at this [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) to a specified system filepath.

<br />

|                                                                                                                                                                                                                                                                                                                                               Details                                                                                                                                                                                                                                                                                                                                                ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------| | `destinationFilePath` | A file system URI representing the path the object should be downloaded to.                                                               | | `progressHandler`     | usually an instance of StorageProgress that will receive periodic updates during the operation. This value can be null.                   | | `cancelToken`         | A CancellationToken to control the operation and possibly later cancel it. This value may be CancellationToken.None to indicate no value. | |
| **Returns** | A Task which can be used to monitor the operation and obtain the result.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

### GetHashCode

```c#
override int GetHashCode()
```  
Create a hash of the URI string used by this reference.

<br />

|                  Details                   ||
|-------------|-------------------------------|
| **Returns** | Hash of this reference's URI. |

### GetMetadataAsync

```c#
Task< StorageMetadata > GetMetadataAsync()
```  
Retrieves metadata associated with an object at this [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)

<br />

|                                        Details                                        ||
|-------------|--------------------------------------------------------------------------|
| **Returns** | A Task which can be used to monitor the operation and obtain the result. |

### GetStreamAsync

```c#
Task< Stream > GetStreamAsync()
```  
Downloads the object at this [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) via a Stream The resulting InputStream should be not be accessed on the main thread because calling into it may block the calling thread.

<br />

|                             Details                             ||
|-------------|----------------------------------------------------|
| **Returns** | A Task which can be used to monitor the operation. |

### GetStreamAsync

```c#
Task GetStreamAsync(
  Action< Stream > streamProcessor,
  IProgress< DownloadState > progressHandler,
  CancellationToken cancelToken
)
```  
Downloads the object at this [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) via a Stream

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                 Details                                                                                                                                                                                                                                                                                                                                                                                                                                                  ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `streamProcessor` | A delegate that is responsible for reading data from the Stream The delegate is called on a background thread and exceptions thrown from this object will be returned as a failure to the Task | | `progressHandler` | usually an instance of StorageProgress that will receive periodic updates during the operation. This value can be null.                                                                        | | `cancelToken`     | A CancellationToken to control the operation and possibly later cancel it. This value may be CancellationToken.None to indicate no value.                                                      | |
| **Returns** | A Task which can be used to monitor the operation and obtain the result.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

### PutBytesAsync

```c#
Task< StorageMetadata > PutBytesAsync(
  byte[] bytes,
  MetadataChange customMetadata,
  IProgress< UploadState > progressHandler,
  CancellationToken cancelToken,
  Uri previousSessionUri
)
```  
Uploads byte data to this [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) This is not recommended for large files.

Instead upload a file via PutFile

or a Stream via PutStream

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `bytes`              | The byte\[\] to upload.                                                                                                                                                                                                                                                                      | | `customMetadata`     | [MetadataChange](https://firebase.google.com/docs/reference/unity/class/firebase/storage/metadata-change#class_firebase_1_1_storage_1_1_metadata_change) containing additional information (MIME type, etc.) about the object being uploaded.                                                | | `progressHandler`    | usually an instance of StorageProgress that will receive periodic updates during the operation. This value can be null.                                                                                                                                                                      | | `cancelToken`        | A CancellationToken to control the operation and possibly later cancel it. This value may be CancellationToken.None to indicate no value.                                                                                                                                                    | | `previousSessionUri` | A Uri previously obtained by [UploadState.UploadSessionUri](https://firebase.google.com/docs/reference/unity/class/firebase/storage/upload-state#class_firebase_1_1_storage_1_1_upload_state_1a397d1e3b789456f6cda7676a5d22340c) that can be used to resume a previously interrupted upload. | |
| **Returns** | A Task which can be used to monitor the upload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### PutFileAsync

```c#
Task< StorageMetadata > PutFileAsync(
  string filePath,
  MetadataChange customMetadata,
  IProgress< UploadState > progressHandler,
  CancellationToken cancelToken,
  Uri previousSessionUri
)
```  
Uploads from a content URI to this [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `filePath`           | The source of the upload. This should be a file system URI representing the path the object should be uploaded from.                                                                                                                                                                         | | `customMetadata`     | [MetadataChange](https://firebase.google.com/docs/reference/unity/class/firebase/storage/metadata-change#class_firebase_1_1_storage_1_1_metadata_change) containing additional information (MIME type, etc.) about the object being uploaded.                                                | | `progressHandler`    | usually an instance of StorageProgress that will receive periodic updates during the operation. This value can be null.                                                                                                                                                                      | | `cancelToken`        | A CancellationToken to control the operation and possibly later cancel it. This value may be CancellationToken.None to indicate no value.                                                                                                                                                    | | `previousSessionUri` | A Uri previously obtained by [UploadState.UploadSessionUri](https://firebase.google.com/docs/reference/unity/class/firebase/storage/upload-state#class_firebase_1_1_storage_1_1_upload_state_1a397d1e3b789456f6cda7676a5d22340c) that can be used to resume a previously interrupted upload. | |
| **Returns** | A Task which can be used to monitor the upload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### PutStreamAsync

```c#
Task< StorageMetadata > PutStreamAsync(
  Stream stream,
  MetadataChange customMetadata,
  IProgress< UploadState > progressHandler,
  CancellationToken cancelToken,
  Uri previousSessionUri
)
```  
Uploads a stream of data to this [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference) The stream will remain open at the end of the upload.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `stream`             | The Stream to upload.                                                                                                                                                                                                                                                                        | | `customMetadata`     | [MetadataChange](https://firebase.google.com/docs/reference/unity/class/firebase/storage/metadata-change#class_firebase_1_1_storage_1_1_metadata_change) containing additional information (MIME type, etc.) about the object being uploaded.                                                | | `progressHandler`    | usually an instance of StorageProgress that will receive periodic updates during the operation. This value can be null.                                                                                                                                                                      | | `cancelToken`        | A CancellationToken to control the operation and possibly later cancel it. This value may be CancellationToken.None to indicate no value.                                                                                                                                                    | | `previousSessionUri` | A Uri previously obtained by [UploadState.UploadSessionUri](https://firebase.google.com/docs/reference/unity/class/firebase/storage/upload-state#class_firebase_1_1_storage_1_1_upload_state_1a397d1e3b789456f6cda7676a5d22340c) that can be used to resume a previously interrupted upload. | |
| **Returns** | A Task which can be used to monitor the upload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### ToString

```c#
override string ToString()
```  
<br />

|                                                                                                                                              Details                                                                                                                                              ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | This object in URI form, which can then be shared and passed into [FirebaseStorage.GetReferenceFromUrl](https://firebase.google.com/docs/reference/unity/class/firebase/storage/firebase-storage#class_firebase_1_1_storage_1_1_firebase_storage_1a42867cc9a73277ca6a8ff92595dd1cdf) |

### UpdateMetadataAsync

```c#
Task< StorageMetadata > UpdateMetadataAsync(
  MetadataChange metadata
)
```  
Updates the metadata associated with this [StorageReference](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-reference#class_firebase_1_1_storage_1_1_storage_reference)

<br />

|                                                                                                                                                                                                                   Details                                                                                                                                                                                                                    ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `metadata` | A [MetadataChange](https://firebase.google.com/docs/reference/unity/class/firebase/storage/metadata-change#class_firebase_1_1_storage_1_1_metadata_change) object with the metadata to update. | |
| **Returns** | a System.Threading.Tasks.Task that will return the final [StorageMetadata](https://firebase.google.com/docs/reference/unity/class/firebase/storage/storage-metadata#class_firebase_1_1_storage_1_1_storage_metadata) once the operation is complete.                                                                                                                                                                            |