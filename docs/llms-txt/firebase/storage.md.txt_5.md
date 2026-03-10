# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage.md.txt

# firebase::storage::Storage Class Reference

# firebase::storage::Storage


`#include <storage.h>`

Entry point for the Firebase C++ SDK for Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage).

## Summary

To use the SDK, call [firebase::storage::Storage::GetInstance()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage_1a0900312e320094efd1f72ffbca3e14f3) to obtain an instance of [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage), then use [GetReference()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage_1ae7250dea993fe4add7902a0eef6ea8d2) to obtain references to child blobs. From there you can upload data with StorageReference::PutStream(), get data via StorageReference::GetStream().

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage_1a684ce7fca43a5122169195b31ca29563()` Destructor. ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage_1ae7250dea993fe4add7902a0eef6ea8d2() const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference` Get a [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) to the root of the database. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage_1ae0ab6d171cb571068403af5897d70ae4(const char *path) const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference` Get a [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) for the specified path. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage_1a0b88769b3121ea105a6a69f601ce1680(const std::string & path) const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference` Get a [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) for the specified path. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage_1a9a5130a80c6a520436d5fd6432ad52a6(const char *url) const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference` Get a [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) for the provided URL. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage_1a4162b901ecfc640c06e78f4041b633a0(const std::string & url) const ` | `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference` Get a [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) for the provided URL. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage_1a5d06c3324ac0cda68585dca4336a7de7(const std::string & host, int port)` | `void` Configures the [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) SDK to use an emulated backend instead of the default remote backend. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage_1aac7729ac67ed493aed04c0cc51567c8b(const char *host, int port)` | `void` Configures the [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) SDK to use an emulated backend instead of the default remote backend. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage_1a2e743fd5f75a47a1115eb9b4fadaef3d()` | `::https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app *` Get the firease::App that this [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) was created with. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage_1aff19f227824708589afe9c9b1df57456()` | `double` Returns the maximum time in seconds to retry a download if a failure occurs. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage_1adfc88ec0a3929b4f1aa541a6cb83724f()` | `double` Returns the maximum time to retry operations other than upload and download if a failure occurs. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage_1a8edee2fbdb726e94f40f2bd1ea4309c9()` | `double` Returns the maximum time to retry an upload if a failure occurs. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage_1ac6e638b08fe1f2a20de990052094720a(double max_transfer_retry_seconds)` | `void` Sets the maximum time to retry a download if a failure occurs. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage_1a74ff037cfdbd291ee804c5fdd056e8e1(double max_transfer_retry_seconds)` | `void` Sets the maximum time to retry operations other than upload and download if a failure occurs. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage_1a2be9c12e8134817bfbebb87e321b716a(double max_transfer_retry_seconds)` | `void` Sets the maximum time to retry an upload if a failure occurs. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage_1a9e2d0b1cc78aab3fb0fa8eb8dc2e6072()` | `std::string` Get the URL that this [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) was created with. |

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage_1a0900312e320094efd1f72ffbca3e14f3(::https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app *app, https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478 *init_result_out)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage *` Get an instance of [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) corresponding to the given [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage_1a0a2ebb959d1977aa7a362b59d88b1216(::https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app *app, const char *url, https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478 *init_result_out)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage *` Get an instance of [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) corresponding to the given [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app), with the given Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) URL. |

## Public functions

### GetReference

```c++
StorageReference GetReference() const 
```
Get a [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) to the root of the database.

### GetReference

```c++
StorageReference GetReference(
  const char *path
) const 
```
Get a [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) for the specified path.

### GetReference

```c++
StorageReference GetReference(
  const std::string & path
) const 
```
Get a [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) for the specified path.

### GetReferenceFromUrl

```c++
StorageReference GetReferenceFromUrl(
  const char *url
) const 
```
Get a [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) for the provided URL.

### GetReferenceFromUrl

```c++
StorageReference GetReferenceFromUrl(
  const std::string & url
) const 
```
Get a [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) for the provided URL.

### UseEmulator

```c++
void UseEmulator(
  const std::string & host,
  int port
)
```
Configures the [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) SDK to use an emulated backend instead of the default remote backend.

This method should be called before invoking any other methods on a new instance of [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage)

### UseEmulator

```c++
void UseEmulator(
  const char *host,
  int port
)
```
Configures the [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) SDK to use an emulated backend instead of the default remote backend.

This method should be called before invoking any other methods on a new instance of [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage)

### app

```c++
::firebase::App * app()
```
Get the firease::App that this [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) was created with.

<br />

| Details ||
|---|---|
| **Returns** | The [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) this [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) was created with. |

### max_download_retry_time

```c++
double max_download_retry_time()
```
Returns the maximum time in seconds to retry a download if a failure occurs.

### max_operation_retry_time

```c++
double max_operation_retry_time()
```
Returns the maximum time to retry operations other than upload and download if a failure occurs.

### max_upload_retry_time

```c++
double max_upload_retry_time()
```
Returns the maximum time to retry an upload if a failure occurs.

### set_max_download_retry_time

```c++
void set_max_download_retry_time(
  double max_transfer_retry_seconds
)
```
Sets the maximum time to retry a download if a failure occurs.

Defaults to 600 seconds (10 minutes).

### set_max_operation_retry_time

```c++
void set_max_operation_retry_time(
  double max_transfer_retry_seconds
)
```
Sets the maximum time to retry operations other than upload and download if a failure occurs.

Defaults to 120 seconds (2 minutes).

### set_max_upload_retry_time

```c++
void set_max_upload_retry_time(
  double max_transfer_retry_seconds
)
```
Sets the maximum time to retry an upload if a failure occurs.

Defaults to 600 seconds (10 minutes).

### url

```c++
std::string url()
```
Get the URL that this [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) was created with.

<br />

| Details ||
|---|---|
| **Returns** | The URL this [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) was created with, or an empty string if this [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) was created with default parameters. |

### \~Storage

```c++
 ~Storage()
```
Destructor.

You may delete an instance of [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) when you are finished using it, to shut down the [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) library.

## Public static functions

### GetInstance

```c++
Storage * GetInstance(
  ::firebase::App *app,
  InitResult *init_result_out
)
```
Get an instance of [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) corresponding to the given [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app).

Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) uses [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) to communicate with Firebase Authentication to authenticate users to the server backend.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `app` | An instance of [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app). Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) will use this to communicate with Firebase Authentication. | | `init_result_out` | Optional: If provided, write the init result here. Will be set to kInitResultSuccess if initialization succeeded, or kInitResultFailedMissingDependency on Android if Google Play services is not available on the current device. | |
| **Returns** | An instance of [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) corresponding to the given [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app). |

### GetInstance

```c++
Storage * GetInstance(
  ::firebase::App *app,
  const char *url,
  InitResult *init_result_out
)
```
Get an instance of [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) corresponding to the given [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app), with the given Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) URL.

Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) uses [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) to communicate with Firebase Authentication to authenticate users to the server backend.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `app` | An instance of [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app). Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) will use this to communicate with Firebase Authentication. | | `url` | Cloud [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) URL. | | `init_result_out` | Optional: If provided, write the init result here. Will be set to kInitResultSuccess if initialization succeeded, or kInitResultFailedMissingDependency on Android if Google Play services is not available on the current device. | |
| **Returns** | An instance of [Storage](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage#classfirebase_1_1storage_1_1_storage) corresponding to the given [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app). |