# Source: https://firebase.google.com/docs/reference/cpp/namespace/firebase/storage.md.txt

# firebase::storage Namespace

# firebase::storage

Namespace for the Firebase C++ SDK for Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage).

## Summary

| ### Enumerations ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/storage#namespacefirebase_1_1storage_1a6afadb76bb776c1ac82bb1b154e2dc61{ https://firebase.google.com/docs/reference/cpp/namespace/firebase/storage#namespacefirebase_1_1storage_1a6afadb76bb776c1ac82bb1b154e2dc61a1c235f338bcbe295bbc4e92d25af8e92 = 0, https://firebase.google.com/docs/reference/cpp/namespace/firebase/storage#namespacefirebase_1_1storage_1a6afadb76bb776c1ac82bb1b154e2dc61ab66f0a397a2387e47b46414aa52f5b4f, https://firebase.google.com/docs/reference/cpp/namespace/firebase/storage#namespacefirebase_1_1storage_1a6afadb76bb776c1ac82bb1b154e2dc61a14c1f4601b4fd9b015da177fea8ffb0d, https://firebase.google.com/docs/reference/cpp/namespace/firebase/storage#namespacefirebase_1_1storage_1a6afadb76bb776c1ac82bb1b154e2dc61a53a5db7169926e0cef803abc0e0a0b1b, https://firebase.google.com/docs/reference/cpp/namespace/firebase/storage#namespacefirebase_1_1storage_1a6afadb76bb776c1ac82bb1b154e2dc61a1ae047e54284beae18860427d480cb41, https://firebase.google.com/docs/reference/cpp/namespace/firebase/storage#namespacefirebase_1_1storage_1a6afadb76bb776c1ac82bb1b154e2dc61a3f269c9f973358ae9f76e10ebf0d398e, https://firebase.google.com/docs/reference/cpp/namespace/firebase/storage#namespacefirebase_1_1storage_1a6afadb76bb776c1ac82bb1b154e2dc61a02598f7c508bf23242685051bfcb85f8, https://firebase.google.com/docs/reference/cpp/namespace/firebase/storage#namespacefirebase_1_1storage_1a6afadb76bb776c1ac82bb1b154e2dc61a2fb1db59927e9cf2ff2ce89985e88da5, https://firebase.google.com/docs/reference/cpp/namespace/firebase/storage#namespacefirebase_1_1storage_1a6afadb76bb776c1ac82bb1b154e2dc61a21b135004e6824e74fa97ec7bc7e4106, https://firebase.google.com/docs/reference/cpp/namespace/firebase/storage#namespacefirebase_1_1storage_1a6afadb76bb776c1ac82bb1b154e2dc61a716920b8d2f154e92d959fa263f929f7, https://firebase.google.com/docs/reference/cpp/namespace/firebase/storage#namespacefirebase_1_1storage_1a6afadb76bb776c1ac82bb1b154e2dc61ad033053c7d9cc62bfb3d2bd4430e8a31, https://firebase.google.com/docs/reference/cpp/namespace/firebase/storage#namespacefirebase_1_1storage_1a6afadb76bb776c1ac82bb1b154e2dc61ae24b79ad4bc3b69ab1e85b5008671457 }` | enumError code returned by Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) C++ functions. |

| ### Functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/storage#namespacefirebase_1_1storage_1aa24c7c9c29221a5be78d7a53ca880e13(https://firebase.google.com/docs/reference/cpp/namespace/firebase/storage#namespacefirebase_1_1storage_1a6afadb76bb776c1ac82bb1b154e2dc61 error)` | `const char *` Get the human-readable error message corresponding to an error code. |

| ### Classes ||
|---|---|
| [firebase::storage::Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller) | Controls an ongoing operation, allowing the caller to Pause, Resume or Cancel an ongoing download or upload. |
| [firebase::storage::Listener](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/listener) | Base class used to receive pause and progress events on a running read or write operation. |
| [firebase::storage::Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata) | [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata) stores default attributes such as size and content type. |
| [firebase::storage::Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage) | Entry point for the Firebase C++ SDK for Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage). |
| [firebase::storage::StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference) | Represents a reference to a Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) object. |

## Enumerations

### Error

```c++
 Error
```
Error code returned by Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) C++ functions.

| Properties ||
|---|---|
| `kErrorBucketNotFound` | No bucket is configured for Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage). |
| `kErrorCancelled` | User cancelled the operation. |
| `kErrorDownloadSizeExceeded` | Size of the downloaded file exceeds the amount of memory allocated for the download. |
| `kErrorNonMatchingChecksum` | File on the client does not match the checksum of the file received by the server. |
| `kErrorNone` | The operation was a success, no error occurred. |
| `kErrorObjectNotFound` | No object exists at the desired reference. |
| `kErrorProjectNotFound` | No project is configured for Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage). |
| `kErrorQuotaExceeded` | Quota on your Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) bucket has been exceeded. |
| `kErrorRetryLimitExceeded` | The maximum time limit on an operation (upload, download, delete, etc.) has been exceeded. |
| `kErrorUnauthenticated` | User is unauthenticated. |
| `kErrorUnauthorized` | User is not authorized to perform the desired action. |
| `kErrorUnknown` | An unknown error occurred. |

## Functions

### GetErrorMessage

```c++
const char * GetErrorMessage(
  Error error
)
```
Get the human-readable error message corresponding to an error code.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `error` | Error code to get the error message for. | |
| **Returns** | Statically-allocated string describing the error. |