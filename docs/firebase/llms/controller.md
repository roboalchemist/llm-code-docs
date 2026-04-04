# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller.md.txt

# firebase::storage::Controller Class Reference

# firebase::storage::Controller


`#include <controller.h>`

Controls an ongoing operation, allowing the caller to Pause, Resume or Cancel an ongoing download or upload.

## Summary

An instance of [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller) can be constructed and passed to [StorageReference::GetBytes()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a900b03399d3d879771d241cd70d455ff), [StorageReference::GetFile()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1a2909f324048c6e74c11d699b7c33fb9e), [StorageReference::PutBytes()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1af31e70df99a05baec43a785ccffa78c0), or [StorageReference::PutFile()](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference_1aaea029ebb63c744f6f6c1623e25af4f5) to become associated with it. Each [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller) can only be associated with one operation at a time.

A [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller) is also passed as an argument to [Listener](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/listener#classfirebase_1_1storage_1_1_listener)'s callbacks. The [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller) passed to a [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) operation is not the same object passed to [Listener](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/listener#classfirebase_1_1storage_1_1_listener) callbacks (though it refers to the same operation), so there are no restrictions on the lifetime of the [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller) the user creates (but the [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller) passed into a [Listener](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/listener#classfirebase_1_1storage_1_1_listener) callbacks should only be used from within that callback).

This class is currently not thread safe and can only be called on the main thread.

| ### Constructors and Destructors ||
|---|---|
| [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller_1aaeee611640b520cf00b68ed18a877904)`()` Default constructor. ||
| [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller_1a2b63ac34bc46027e130a1e6991e88da2)`(const `[Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller)` & other)` Copy constructor. ||
| [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller_1aef4b45aa340f575f4a366fd30a2dd1ea)`(`[Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller)` && other)` Move constructor. ||
| [~Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller_1a8c860ea35ac5116047993985c4b33c4b)`()` Destructor. ||

|                                                                                                                                                                                                                                                                                                                                                                                                        ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                        ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Cancel](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller_1ac165335731df6e29c9f26b97ab83bf30)`()`                                                                                                                                                          | `bool` Cancels the operation currently in progress.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [GetReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller_1a7de733724f63bfc83b2dab1a6302472a)`() const `                                                                                                                                             | [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) Returns the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) associated with this [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller). |
| [Pause](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller_1a10b5acbe4999f31d7cd3789a5424072c)`()`                                                                                                                                                           | `bool` Pauses the operation currently in progress.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Resume](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller_1a752be629bef74fcc762e6a14128503bd)`()`                                                                                                                                                          | `bool` Resumes the operation that is paused.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [bytes_transferred](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller_1a803a6ef9efbd42748d191a5cd48b8574)`() const `                                                                                                                                        | `int64_t` Returns the number of bytes transferred so far.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [is_paused](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller_1ad057e46e08c230ed8e3bcf21ff2ae269)`() const `                                                                                                                                                | `bool` Returns true if the operation is paused.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [is_valid](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller_1a6d85a368b04cecd2c2f3a761707d3802)`() const `                                                                                                                                                 | `bool` Returns true if this [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller) is valid, false if it is not valid.                                                                                                                                                                                                                                                                                         |
| [operator=](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller_1a464bed2f2e1e9709560cdffd23f7a699)`(const `[Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller)` & other)` | [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller)` &` Copy assignment operator.                                                                                                                                                                                                                                                                                                                           |
| [operator=](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller_1aa51c6379b0c09781c8c6b1124eda6a89)`(`[Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller)` && other)`      | [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller)` &` Move assignment operator.                                                                                                                                                                                                                                                                                                                           |
| [total_byte_count](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller_1a07c77fd36bc3b97eb4f55388f2f73cc5)`() const `                                                                                                                                         | `int64_t` Returns the total bytes to be transferred.                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## Public functions

### Cancel

```c++
bool Cancel()
```  
Cancels the operation currently in progress.

<br />

|                                    Details                                     ||
|-------------|-------------------------------------------------------------------|
| **Returns** | True if the operation was successfully canceled, false otherwise. |

### Controller

```c++
 Controller()
```  
Default constructor.

You may construct your own [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller) to pass into various [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) operations.  

### Controller

```c++
 Controller(
  const Controller & other
)
```  
Copy constructor.

<br />

|                                                                                                                                                                      Details                                                                                                                                                                      ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|------------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller) to copy from. | |

### Controller

```c++
 Controller(
  Controller && other
)
```  
Move constructor.

Moving is an efficient operation for [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller) instances.

<br />

|                                                                                                                                                                      Details                                                                                                                                                                      ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|------------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller) to move from. | |

### GetReference

```c++
StorageReference GetReference() const 
```  
Returns the [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) associated with this [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller).

<br />

|                                                                                                                                                                 Details                                                                                                                                                                  ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The [StorageReference](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/storage-reference#classfirebase_1_1storage_1_1_storage_reference) associated with this [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller). |

### Pause

```c++
bool Pause()
```  
Pauses the operation currently in progress.

<br />

|                                   Details                                    ||
|-------------|-----------------------------------------------------------------|
| **Returns** | True if the operation was successfully paused, false otherwise. |

### Resume

```c++
bool Resume()
```  
Resumes the operation that is paused.

<br />

|                                    Details                                    ||
|-------------|------------------------------------------------------------------|
| **Returns** | True if the operation was successfully resumed, false otherwise. |

### bytes_transferred

```c++
int64_t bytes_transferred() const 
```  
Returns the number of bytes transferred so far.

<br />

|                       Details                        ||
|-------------|-----------------------------------------|
| **Returns** | The number of bytes transferred so far. |

### is_paused

```c++
bool is_paused() const 
```  
Returns true if the operation is paused.  

### is_valid

```c++
bool is_valid() const 
```  
Returns true if this [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller) is valid, false if it is not valid.

An invalid [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller) is one that is not associated with an operation.

<br />

|                                                                                                                                                                   Details                                                                                                                                                                   ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | true if this [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller) is valid, false if this [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller) is invalid. |

### operator=

```c++
Controller & operator=(
  const Controller & other
)
```  
Copy assignment operator.

<br />

|                                                                                                                                                                      Details                                                                                                                                                                       ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|------------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller) to copy from. | |
| **Returns** | Reference to the destination [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller).                                                                                                                                                                  |

### operator=

```c++
Controller & operator=(
  Controller && other
)
```  
Move assignment operator.

Moving is an efficient operation for [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller) instances.

<br />

|                                                                                                                                                                      Details                                                                                                                                                                       ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|------------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller) to move from. | |
| **Returns** | Reference to the destination [Controller](https://firebase.google.com/docs/reference/cpp/class/firebase/storage/controller#classfirebase_1_1storage_1_1_controller).                                                                                                                                                                  |

### total_byte_count

```c++
int64_t total_byte_count() const 
```  
Returns the total bytes to be transferred.

<br />

|                                                   Details                                                   ||
|-------------|------------------------------------------------------------------------------------------------|
| **Returns** | The total bytes to be transferred. This will return -1 if the size of the transfer is unknown. |

### \~Controller

```c++
 ~Controller()
```  
Destructor.