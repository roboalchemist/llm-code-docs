# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings.md.txt

# firebase::firestore::Settings Class Reference

# firebase::firestore::Settings


`#include <settings.h>`

[Settings](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings) used to configure a [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance.

## Summary

| ### Constructors and Destructors ||
|---|---|
| [Settings](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings_1a6783528c414f5ee131f65da987fa76c2)`()` Creates the default settings. ||
| [Settings](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings_1a457de53694bf882185ed00b0a2f886b5)`(const `[Settings](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings)` & other)` Copy constructor. ||
| [Settings](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings_1acf543745405fb99b0cd497bf3471da87)`(`[Settings](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings)` && other)` Move constructor. ||

|                                                                                                                               ### Public static attributes                                                                                                                                ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [kCacheSizeUnlimited](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings_1ad6f41b6023bf01f01c9c85351f8e4250)` = -1` | `constexpr int64_t` Constant to use with `set_cache_size_bytes` to disable garbage collection. |

|                                                                                                                                                                                           ### Friend classes                                                                                                                                                                                            ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [operator<<](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings_1af43b34cb5375441d834d1eb84af3be04) | `friend std::ostream &` Outputs the string representation of these [Settings](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings) to the given stream. |

|                                                                                                                                                                                                                                                                         ### Public functions                                                                                                                                                                                                                                                                          ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ToString](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings_1af76c5107524993cf87281be89c72603f)`() const `                                                                                                                                                       | `std::string` Returns a string representation of these [Settings](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings) for logging/debugging purposes. |
| [cache_size_bytes](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings_1aa88d8d01a9e1283709551e3683148558)`() const `                                                                                                                                               | `int64_t` Returns cache size for on-disk data.                                                                                                                                                                              |
| [dispatch_queue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings_1a1e690c58e5fed6142dcaf3de310ba4e1)`() const `                                                                                                                                                 | `dispatch_queue_t` Returns a dispatch queue that [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) will use to execute callbacks.     |
| [host](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings_1a5759865418cad7e83e4092d1f90e6cac)`() const `                                                                                                                                                           | `const std::string &` Gets the host of the [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) backend to connect to.                   |
| [is_persistence_enabled](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings_1a723e27133b630801d6bb0f940efba103)`() const `                                                                                                                                         | `bool` Returns whether to enable local persistent storage.                                                                                                                                                                  |
| [is_ssl_enabled](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings_1a0b07eea815e4df1d3ebc0d963ded800e)`() const `                                                                                                                                                 | `bool` Returns whether to use SSL when communicating.                                                                                                                                                                       |
| [operator=](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings_1a09d9917b92102205ed55aa8860d28296)`(const `[Settings](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings)` & other)=default` | [Settings](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings)` &` Copy assignment operator.                                                          |
| [operator=](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings_1a7a70bcb23cf19b33000f226a7a715ceb)`(`[Settings](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings)` && other)=default`      | [Settings](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings)` &` Move assignment operator.                                                          |
| [set_cache_size_bytes](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings_1a465d081f63dbf2451925dd8fda198c58)`(int64_t value)`                                                                                                                                     | `void` Sets an approximate cache size threshold for the on-disk data.                                                                                                                                                       |
| [set_dispatch_queue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings_1a886a5c15d92bd99007e6c45031ecbbed)`(dispatch_queue_t queue)`                                                                                                                              | `void` Sets the dispatch queue that [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) will use to execute callbacks.                  |
| [set_host](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings_1ae495d07cec1fb143858f571d6cd1528f)`(std::string host)`                                                                                                                                              | `void` Sets the host of the [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) backend.                                                |
| [set_persistence_enabled](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings_1af2f49d96cb60235ea43820fe5a13427b)`(bool enabled)`                                                                                                                                   | `void` Enables or disables local persistent storage.                                                                                                                                                                        |
| [set_ssl_enabled](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings_1a7ef112a5c1ae38084aeb15960d370a1e)`(bool enabled)`                                                                                                                                           | `void` Enables or disables SSL for communication.                                                                                                                                                                           |

## Public static attributes

### kCacheSizeUnlimited

```c++
constexpr int64_t kCacheSizeUnlimited = -1
```  
Constant to use with `set_cache_size_bytes` to disable garbage collection.

## Friend classes

### operator\<\<

```c++
friend std::ostream & operator<<(std::ostream &out, const Settings &settings)
```  
Outputs the string representation of these [Settings](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings) to the given stream.

**See also:** [ToString()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings_1af76c5107524993cf87281be89c72603f) for comments on the representation format.

## Public functions

### Settings

```c++
 Settings()
```  
Creates the default settings.  

### Settings

```c++
 Settings(
  const Settings & other
)=default
```  
Copy constructor.

This performs a deep copy, creating an independent instance.

<br />

|                                                                                                                                                                    Details                                                                                                                                                                    ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|----------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [Settings](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings) to copy from. | |

### Settings

```c++
 Settings(
  Settings && other
)=default
```  
Move constructor.

Moving is more efficient than copying for [Settings](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings). After being moved from, [Settings](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings) is in a valid but unspecified state.

<br />

|                                                                                                                                                                         Details                                                                                                                                                                         ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|---------------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [Settings](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings) to move data from. | |

### ToString

```c++
std::string ToString() const 
```  
Returns a string representation of these [Settings](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings) for logging/debugging purposes.


| **Note:** the exact string representation is unspecified and subject to change; don't rely on the format of the string.

<br />

### cache_size_bytes

```c++
int64_t cache_size_bytes() const 
```  
Returns cache size for on-disk data.  

### dispatch_queue

```c++
dispatch_queue_t dispatch_queue() const 
```  
Returns a dispatch queue that [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) will use to execute callbacks.

The returned dispatch queue is used for all completion handlers and event handlers.

If no dispatch queue is explictly set by calling [set_dispatch_queue()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings_1a886a5c15d92bd99007e6c45031ecbbed) then a dedicated "callback queue" will be used; namely, the main thread will not be used for callbacks unless expliclty set to do so by a call to [set_dispatch_queue()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings_1a886a5c15d92bd99007e6c45031ecbbed).

<br />

| **Note:** This method is only available when `__OBJC__` is defined, such as when compiling for iOS or tvOS.
**See also:** [set_dispatch_queue(dispatch_queue_t)](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings_1a886a5c15d92bd99007e6c45031ecbbed) for information on how to explicitly set the dispatch queue to use.

<br />

### host

```c++
const std::string & host() const 
```  
Gets the host of the [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) backend to connect to.  

### is_persistence_enabled

```c++
bool is_persistence_enabled() const 
```  
Returns whether to enable local persistent storage.  

### is_ssl_enabled

```c++
bool is_ssl_enabled() const 
```  
Returns whether to use SSL when communicating.  

### operator=

```c++
Settings & operator=(
  const Settings & other
)=default
```  
Copy assignment operator.

This performs a deep copy, creating an independent instance.

<br />

|                                                                                                                                                                    Details                                                                                                                                                                     ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|----------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [Settings](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings) to copy from. | |
| **Returns** | Reference to the destination [Settings](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings).                                                                                                                                                                |

### operator=

```c++
Settings & operator=(
  Settings && other
)=default
```  
Move assignment operator.

Moving is more efficient than copying for [Settings](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings). After being moved from, [Settings](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings) is in a valid but unspecified state.

<br />

|                                                                                                                                                                         Details                                                                                                                                                                          ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|---------------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [Settings](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings) to move data from. | |
| **Returns** | Reference to the destination [Settings](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings).                                                                                                                                                                          |

### set_cache_size_bytes

```c++
void set_cache_size_bytes(
  int64_t value
)
```  
Sets an approximate cache size threshold for the on-disk data.

If the cache grows beyond this size, Cloud [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) will start removing data that hasn't been recently used. The size is not a guarantee that the cache will stay below that size, only that if the cache exceeds the given size, cleanup will be attempted.

By default, collection is enabled with a cache size of 100 MB. The minimum value is 1 MB.  

### set_dispatch_queue

```c++
void set_dispatch_queue(
  dispatch_queue_t queue
)
```  
Sets the dispatch queue that [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) will use to execute callbacks.

The specified dispatch queue will be used for all completion handlers and event handlers.

<br />

| **Note:** This method is only available when `__OBJC__` is defined, such as when compiling for iOS or tvOS.
**See also:** [dispatch_queue()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/settings#classfirebase_1_1firestore_1_1_settings_1a1e690c58e5fed6142dcaf3de310ba4e1) for the "get" counterpart to this method.

<br />

|                                            Details                                            ||
|------------|-----------------------------------------------------------------------------------|
| Parameters | |---------|----------------------------| | `queue` | The dispatch queue to use. | |

### set_host

```c++
void set_host(
  std::string host
)
```  
Sets the host of the [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) backend.

The default is "firestore.googleapis.com".

<br />

|                                 Details                                 ||
|------------|-------------------------------------------------------------|
| Parameters | |--------|------------------| | `host` | The host string. | |

### set_persistence_enabled

```c++
void set_persistence_enabled(
  bool enabled
)
```  
Enables or disables local persistent storage.

<br />

|                                                                Details                                                                ||
|------------|---------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------|----------------------------------------------| | `enabled` | Set true to enable local persistent storage. | |

### set_ssl_enabled

```c++
void set_ssl_enabled(
  bool enabled
)
```  
Enables or disables SSL for communication.

<br />

|                                                             Details                                                             ||
|------------|---------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------|-------------------------------------------| | `enabled` | Set true to enable SSL for communication. | |