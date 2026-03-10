# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference.md.txt

# firebase::storage::StorageReference Class Reference

# firebase::storage::StorageReference


`#include <storage_reference.h>`

Represents a reference to a Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) object.

## Summary

Developers can upload and download objects, get/set object metadata, and delete an object at a specified path.

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a28b814fdcfbe819673ca79c503cae071()` Default constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a9378edb9a672361c0bc1fcb2818703fa(const https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference & reference)` Copy constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1ad405e1410c6f5c09d5f18e0fb51e8bb2(https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference && other)` Move constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a14455146f8474a638df0edb0dbebcc00()` ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a35c56015f8df53aa65fe522b71aff8a1(const char *path) const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference` Gets a reference to a location relative to this one. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a4a858af7b1f3cd0a37a686c7e35f4747(const std::string & path) const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference` Gets a reference to a location relative to this one. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a33d9c9d743736d128e2c0fd367ae3dd6()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Deletes the object at the current path. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a2e174ecd70fcad16669846fe67117ebc()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Returns the result of the most recent call to RemoveValue();. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a900b03399d3d879771d241cd70d455ff(void *buffer, size_t buffer_size, https://firebase.google.com/docs/reference/cpp/class/firebase/storage/listener#classfirebase_1_1storage_1_1_listener *listener, https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller *controller_out)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< size_t >` Asynchronously downloads the object from this [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1ad307042e2aa5a8e1a6e01f6aa2dae954()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< size_t >` Returns the result of the most recent call to [GetBytes()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a900b03399d3d879771d241cd70d455ff);. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a06e1a86dea092cee24b53e016710996a()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< std::string >` Asynchronously retrieves a long lived download URL with a revokable token. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1aefdad33fc57c8b9cefec8828c72eae0b()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< std::string >` Returns the result of the most recent call to [GetDownloadUrl()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a06e1a86dea092cee24b53e016710996a);. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a2909f324048c6e74c11d699b7c33fb9e(const char *path, https://firebase.google.com/docs/reference/cpp/class/firebase/storage/listener#classfirebase_1_1storage_1_1_listener *listener, https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller *controller_out)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< size_t >` Asynchronously downloads the object from this [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1adaad7ae86025602b1a162c09ec036316()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< size_t >` Returns the result of the most recent call to [GetFile()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a2909f324048c6e74c11d699b7c33fb9e);. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a78a50874c5ee78f5774734af1975c5d8()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata >` Retrieves metadata associated with an object at this [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a131529eaa289517a2873eaac64d2692f()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata >` Returns the result of the most recent call to [GetMetadata()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a78a50874c5ee78f5774734af1975c5d8);. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a47fedaa553ccd95ded10321b4e688fc6()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference` Returns a new instance of [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) pointing to the parent location or null if this instance references the root location. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1af31e70df99a05baec43a785ccffa78c0(const void *buffer, size_t buffer_size, https://firebase.google.com/docs/reference/cpp/class/firebase/storage/listener#classfirebase_1_1storage_1_1_listener *listener, https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller *controller_out)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata >` Asynchronously uploads data to the currently specified [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference), without additional metadata. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a24c4c81a1e9c40d73a4af40d9f4853ec(const void *buffer, size_t buffer_size, const https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata & metadata, https://firebase.google.com/docs/reference/cpp/class/firebase/storage/listener#classfirebase_1_1storage_1_1_listener *listener, https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller *controller_out)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata >` Asynchronously uploads data to the currently specified [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference), without additional metadata. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a068c3a79f4297432a13895108bb0f5c6()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata >` Returns the result of the most recent call to [PutBytes()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1af31e70df99a05baec43a785ccffa78c0);. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1aaea029ebb63c744f6f6c1623e25af4f5(const char *path, https://firebase.google.com/docs/reference/cpp/class/firebase/storage/listener#classfirebase_1_1storage_1_1_listener *listener, https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller *controller_out)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata >` Asynchronously uploads data to the currently specified [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference), without additional metadata. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1aa2b61e94a44326eda8e9e8c22a0de202(const char *path, const https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata & metadata, https://firebase.google.com/docs/reference/cpp/class/firebase/storage/listener#classfirebase_1_1storage_1_1_listener *listener, https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller *controller_out)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata >` Asynchronously uploads data to the currently specified [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference), without additional metadata. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a551ed170515a1a8a0b0f59e7aefb0615()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata >` Returns the result of the most recent call to [PutFile()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1aaea029ebb63c744f6f6c1623e25af4f5);. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1ae559d31b4a5d799d31a2ee845c1a74f8(const https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata & metadata)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata >` Updates the metadata associated with this [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a678399860ef138f40168063bb3d2405f()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata >` Returns the result of the most recent call to [UpdateMetadata()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1ae559d31b4a5d799d31a2ee845c1a74f8);. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1aba53e573fcd6fdcfcf04868d4accabda()` | `std::string` Return the Google Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) bucket that holds this object. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a9f88346a5dc431a8fa496be6f39cc0cb()` | `std::string` Return the full path of the storage reference, not including the Google Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) bucket. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a28925c57c1dd634dd019863e05c97f5e() const ` | `bool` Returns true if this [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) is valid, false if it is not valid. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a6f295a65b77a4109885219537508ab15()` | `std::string` Returns the short name of this object. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1add7ac57b0d413c7bf03a67edc48e9cef(const https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference & reference)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference &` Copy assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1ae4c5512eb317cc5415d2aeccc53de9d2(https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference && other)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference &` Move assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1ab25d9b68098b3d4fde55aa65adc5cb4f()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage *` Gets the [firebase::storage::Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) instance to which we refer. |

## Public functions

### Child

```c++
StorageReference Child(
  const char *path
) const 
```
Gets a reference to a location relative to this one.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `path` | Path relative to this reference's location. The pointer only needs to be valid during this call. | |
| **Returns** | Child relative to this location. |

### Child

```c++
StorageReference Child(
  const std::string & path
) const 
```
Gets a reference to a location relative to this one.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `path` | Path relative to this reference's location. | |
| **Returns** | Child relative to this location. |

### Delete

```c++
Future< void > Delete()
```
Deletes the object at the current path.

<br />

| Details ||
|---|---|
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) result, which will complete when the operation either succeeds or fails. When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) is completed, if its Error is kErrorNone, the operation succeeded. |

### DeleteLastResult

```c++
Future< void > DeleteLastResult()
```
Returns the result of the most recent call to RemoveValue();.

<br />

| Details ||
|---|---|
| **Returns** | The result of the most recent call to RemoveValue(); |

### GetBytes

```c++
Future< size_t > GetBytes(
  void *buffer,
  size_t buffer_size,
  Listener *listener,
  Controller *controller_out
)
```
Asynchronously downloads the object from this [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).

A byte array will be allocated large enough to hold the entire file in memory. Therefore, using this method will impact memory usage of your process.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `buffer` | A byte buffer to read the data into. This buffer must be valid for the duration of the transfer. | | `buffer_size` | The size of the byte buffer. | | `listener` | A listener that will respond to events on this read operation. If not nullptr, a listener that will respond to events on this read operation. The caller is responsible for allocating and deallocating the listener. The same listener can be used for multiple operations. | | `controller_out` | Controls the write operation, providing the ability to pause, resume or cancel an ongoing write operation. If not nullptr, this method will output a [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller) here that you can use to control the write operation. | |
| **Returns** | A future that returns the number of bytes read. |

### GetBytesLastResult

```c++
Future< size_t > GetBytesLastResult()
```
Returns the result of the most recent call to [GetBytes()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a900b03399d3d879771d241cd70d455ff);.

<br />

| Details ||
|---|---|
| **Returns** | The result of the most recent call to [GetBytes()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a900b03399d3d879771d241cd70d455ff); |

### GetDownloadUrl

```c++
Future< std::string > GetDownloadUrl()
```
Asynchronously retrieves a long lived download URL with a revokable token.

This can be used to share the file with others, but can be revoked by a developer in the Firebase Console if desired.

<br />

| Details ||
|---|---|
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) result, which will complete when the operation either succeeds or fails. When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) is completed, if its Error is kErrorNone, the operation succeeded and the URL is returned. |

### GetDownloadUrlLastResult

```c++
Future< std::string > GetDownloadUrlLastResult()
```
Returns the result of the most recent call to [GetDownloadUrl()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a06e1a86dea092cee24b53e016710996a);.

<br />

| Details ||
|---|---|
| **Returns** | The result of the most recent call to [GetDownloadUrl()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a06e1a86dea092cee24b53e016710996a); |

### GetFile

```c++
Future< size_t > GetFile(
  const char *path,
  Listener *listener,
  Controller *controller_out
)
```
Asynchronously downloads the object from this [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).

A byte array will be allocated large enough to hold the entire file in memory. Therefore, using this method will impact memory usage of your process.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `path` | Path to local file on device to download into. | | `listener` | A listener that will respond to events on this read operation. If not nullptr, a listener that will respond to events on this read operation. The caller is responsible for allocating and deallocating the listener. The same listener can be used for multiple operations. | | `controller_out` | Controls the write operation, providing the ability to pause, resume or cancel an ongoing write operation. If not nullptr, this method will output a [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller) here that you can use to control the write operation. | |
| **Returns** | A future that returns the number of bytes read. |

### GetFileLastResult

```c++
Future< size_t > GetFileLastResult()
```
Returns the result of the most recent call to [GetFile()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a2909f324048c6e74c11d699b7c33fb9e);.

<br />

| Details ||
|---|---|
| **Returns** | The result of the most recent call to [GetFile()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a2909f324048c6e74c11d699b7c33fb9e); |

### GetMetadata

```c++
Future< Metadata > GetMetadata()
```
Retrieves metadata associated with an object at this [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).

<br />

| Details ||
|---|---|
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) result, which will complete when the operation either succeeds or fails. When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) is completed, if its Error is kErrorNone, the operation succeeded and the [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata) is returned. |

### GetMetadataLastResult

```c++
Future< Metadata > GetMetadataLastResult()
```
Returns the result of the most recent call to [GetMetadata()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a78a50874c5ee78f5774734af1975c5d8);.

<br />

| Details ||
|---|---|
| **Returns** | The result of the most recent call to [GetMetadata()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a78a50874c5ee78f5774734af1975c5d8); |

### GetParent

```c++
StorageReference GetParent()
```
Returns a new instance of [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) pointing to the parent location or null if this instance references the root location.

<br />

| Details ||
|---|---|
| **Returns** | The parent [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference). |

### PutBytes

```c++
Future< Metadata > PutBytes(
  const void *buffer,
  size_t buffer_size,
  Listener *listener,
  Controller *controller_out
)
```
Asynchronously uploads data to the currently specified [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference), without additional metadata.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `buffer` | A byte buffer to write data from. This buffer must be valid for the duration of the transfer. | | `buffer_size` | The size of the byte buffer. | | `listener` | A listener that will respond to events on this read operation. If not nullptr, a listener that will respond to events on this write operation. The caller is responsible for allocating and deallocating the listener. The same listener can be used for multiple operations. | | `controller_out` | Controls the write operation, providing the ability to pause, resume or cancel an ongoing write operation. If not nullptr, this method will output a [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller) here that you can use to control the write operation. | |
| **Returns** | A future that returns the [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata). |

### PutBytes

```c++
Future< Metadata > PutBytes(
  const void *buffer,
  size_t buffer_size,
  const Metadata & metadata,
  Listener *listener,
  Controller *controller_out
)
```
Asynchronously uploads data to the currently specified [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference), without additional metadata.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `buffer` | A byte buffer to write data from. This buffer must be valid for the duration of the transfer. | | `buffer_size` | The number of bytes to write. | | `metadata` | [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata) containing additional information (MIME type, etc.) about the object being uploaded. | | `listener` | A listener that will respond to events on this read operation. If not nullptr, a listener that will respond to events on this write operation. The caller is responsible for allocating and deallocating the listener. The same listener can be used for multiple operations. | | `controller_out` | Controls the write operation, providing the ability to pause, resume or cancel an ongoing write operation. If not nullptr, this method will output a [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller) here that you can use to control the write operation. | |
| **Returns** | A future that returns the [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata). |

### PutBytesLastResult

```c++
Future< Metadata > PutBytesLastResult()
```
Returns the result of the most recent call to [PutBytes()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1af31e70df99a05baec43a785ccffa78c0);.

<br />

| Details ||
|---|---|
| **Returns** | The result of the most recent call to [PutBytes()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1af31e70df99a05baec43a785ccffa78c0); |

### PutFile

```c++
Future< Metadata > PutFile(
  const char *path,
  Listener *listener,
  Controller *controller_out
)
```
Asynchronously uploads data to the currently specified [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference), without additional metadata.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `path` | Path to local file on device to upload to Firebase [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage). | | `listener` | A listener that will respond to events on this read operation. If not nullptr, a listener that will respond to events on this write operation. The caller is responsible for allocating and deallocating the listener. The same listener can be used for multiple operations. | | `controller_out` | Controls the write operation, providing the ability to pause, resume or cancel an ongoing write operation. If not nullptr, this method will output a [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller) here that you can use to control the write operation. | |
| **Returns** | A future that returns the [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata). |

### PutFile

```c++
Future< Metadata > PutFile(
  const char *path,
  const Metadata & metadata,
  Listener *listener,
  Controller *controller_out
)
```
Asynchronously uploads data to the currently specified [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference), without additional metadata.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `path` | Path to local file on device to upload to Firebase [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage). | | `metadata` | [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata) containing additional information (MIME type, etc.) about the object being uploaded. | | `listener` | A listener that will respond to events on this read operation. If not nullptr, a listener that will respond to events on this write operation. The caller is responsible for allocating and deallocating the listener. The same listener can be used for multiple operations. | | `controller_out` | Controls the write operation, providing the ability to pause, resume or cancel an ongoing write operation. If not nullptr, this method will output a [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller) here that you can use to control the write operation. | |
| **Returns** | A future that returns the [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata). |

### PutFileLastResult

```c++
Future< Metadata > PutFileLastResult()
```
Returns the result of the most recent call to [PutFile()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1aaea029ebb63c744f6f6c1623e25af4f5);.

<br />

| Details ||
|---|---|
| **Returns** | The result of the most recent call to [PutFile()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1aaea029ebb63c744f6f6c1623e25af4f5); |

### StorageReference

```c++
 StorageReference()
```
Default constructor.

This creates an invalid [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference). Attempting to perform any operations on this reference will fail unless a valid [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) has been assigned to it.

### StorageReference

```c++
 StorageReference(
  const StorageReference & reference
)
```
Copy constructor.

It's totally okay (and efficient) to copy [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) instances, as they simply point to the same location.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `reference` | [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) to copy from. | |

### StorageReference

```c++
 StorageReference(
  StorageReference && other
)
```
Move constructor.

Moving is an efficient operation for [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) instances.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) to move data from. | |

### UpdateMetadata

```c++
Future< Metadata > UpdateMetadata(
  const Metadata & metadata
)
```
Updates the metadata associated with this [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference).

<br />

| Details ||
|---|---|
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) result, which will complete when the operation either succeeds or fails. When the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) is completed, if its Error is kErrorNone, the operation succeeded and the [Metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/metadata#classfirebase_1_1storage_1_1_metadata) is returned. |

### UpdateMetadataLastResult

```c++
Future< Metadata > UpdateMetadataLastResult()
```
Returns the result of the most recent call to [UpdateMetadata()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1ae559d31b4a5d799d31a2ee845c1a74f8);.

<br />

| Details ||
|---|---|
| **Returns** | The result of the most recent call to [UpdateMetadata()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1ae559d31b4a5d799d31a2ee845c1a74f8); |

### bucket

```c++
std::string bucket()
```
Return the Google Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) bucket that holds this object.

<br />

| Details ||
|---|---|
| **Returns** | The bucket. |

### full_path

```c++
std::string full_path()
```
Return the full path of the storage reference, not including the Google Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) bucket.

<br />

| Details ||
|---|---|
| **Returns** | Full path to the storage reference, not including GCS bucket. For example, for the reference "gs://bucket/path/to/object.txt", the full path would be "path/to/object.txt". |

### is_valid

```c++
bool is_valid() const 
```
Returns true if this [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) is valid, false if it is not valid.

An invalid [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) indicates that the reference is uninitialized (created with the default constructor) or that there was an error retrieving the reference.

<br />

| Details ||
|---|---|
| **Returns** | true if this [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) is valid, false if this [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) is invalid. |

### name

```c++
std::string name()
```
Returns the short name of this object.

<br />

| Details ||
|---|---|
| **Returns** | the short name of this object. |

### operator=

```c++
StorageReference & operator=(
  const StorageReference & reference
)
```
Copy assignment operator.

It's totally okay (and efficient) to copy [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) instances, as they simply point to the same location.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `reference` | [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) to copy from. | |
| **Returns** | Reference to the destination [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference). |

### operator=

```c++
StorageReference & operator=(
  StorageReference && other
)
```
Move assignment operator.

Moving is an efficient operation for [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) instances.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) to move data from. | |
| **Returns** | Reference to the destination [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference). |

### storage

```c++
Storage * storage()
```
Gets the [firebase::storage::Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) instance to which we refer.

The pointer will remain valid indefinitely.

<br />

| Details ||
|---|---|
| **Returns** | The [firebase::storage::Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) instance that this [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) refers to. |

### \~StorageReference

```c++
 ~StorageReference()
```