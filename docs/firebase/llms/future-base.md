# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/future-base.md.txt

# firebase::FutureBase Class Reference

# firebase::FutureBase


`#include <future.h>`

Type-independent return type of asynchronous calls.

## Summary

**See also:** [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) for code samples.

### Inheritance

Direct Known Subclasses:[firebase::Future\< ResultType \>](https://firebase.google.com/docs/reference/cpp/class/firebase/future)

| ### Constructors and Destructors ||
|---|---|
| [FutureBase](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1a062803984339e749d55b5a1825cb3b4d)`()` Construct an untyped future. ||
| [FutureBase](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1a51a2b6f8648a193e0139c740a37abcb9)`(const `[FutureBase](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base)` & rhs)` Copy constructor and operator. ||
| [~FutureBase](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1ac146ddf6ffc96c21fc767ff38040436c)`()` ||

|                                                                                                                                 ### Public types                                                                                                                                  ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| [CompletionCallback](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1a3baf21408009be7f238a5544533fa552)`)(const FutureBase &result_data, void *user_data)` | typedef `void(*` Function pointer for a completion callback. |

|                                                                                                                                                                                                                                                                                                                                                                                                                                         ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                                          ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [OnCompletion](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1a963b7b47edaecabcd58303632d9e45ca)`(`[CompletionCallback](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1a3baf21408009be7f238a5544533fa552)` callback, void *user_data) const ` | `void` Register a single callback that will be called at most once, when the future is completed.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [OnCompletion](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1a17367c459119adb0b637bfb661a3df54)`(std::function< void(const `[FutureBase](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base)` &)> callback) const `                               | `void` Register a single callback that will be called at most once, when the future is completed.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Release](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1a195aacd8c035957b705cff98daa1920f)`()`                                                                                                                                                                                                         | `void` Explicitly release the internal resources for a future.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [error](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1ab7a9ffdf8f16b4473291219d244db26c)`() const `                                                                                                                                                                                                    | `int` When [status()](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1a7b1a3fdc54483440d1ec8d0dc4a64883) is [firebase::kFutureStatusComplete](https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1aa31afaaff6e6fe7cf1f2a13961273fbaa33e40478e42949d7dc59951089f56921), returns the API-defined error code.                                                                                                                               |
| [error_message](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1a178f199bd811180cf7769426f3dd2b41)`() const `                                                                                                                                                                                            | `const char *` When [status()](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1a7b1a3fdc54483440d1ec8d0dc4a64883) is [firebase::kFutureStatusComplete](https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1aa31afaaff6e6fe7cf1f2a13961273fbaa33e40478e42949d7dc59951089f56921), returns the API-defined error message, as human-readable text, or an empty string if the API does not provide a human readable description of the error. |
| [operator!=](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1a50966a86ca2fe4e8fe0b7a95374ab24d)`(const `[FutureBase](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base)` & rhs) const `                                                            | `bool` Returns true if the two Futures reference different results.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [operator=](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1a47cd5926a0158c4fbed6ff1571ad8cd2)`(const `[FutureBase](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base)` & rhs)`                                                                    | [FutureBase](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base)` &` Copy an untyped future.                                                                                                                                                                                                                                                                                                                                                                                  |
| [operator==](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1a3d35e64ceed08b2d2b0c0b83eebf9b55)`(const `[FutureBase](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base)` & rhs) const `                                                            | `bool` Returns true if the two Futures reference the same result.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [result_void](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1ab9405dc13966db21732138d10691b954)`() const `                                                                                                                                                                                              | `const void *` Result of the asynchronous call, or nullptr if the result is still pending.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [status](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1a7b1a3fdc54483440d1ec8d0dc4a64883)`() const `                                                                                                                                                                                                   | [FutureStatus](https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1aa31afaaff6e6fe7cf1f2a13961273fba) Completion status of the asynchronous call.                                                                                                                                                                                                                                                                                                                                                 |

## Public types

### CompletionCallback

```c++
void(* CompletionCallback)(const FutureBase &result_data, void *user_data)
```  
Function pointer for a completion callback.

When we call this, we will send the completed future, along with the user data that you specified when you set up the callback.

## Public functions

### FutureBase

```c++
 FutureBase()
```  
Construct an untyped future.  

### FutureBase

```c++
 FutureBase(
  const FutureBase & rhs
)
```  
Copy constructor and operator.

Increment the reference count when creating a copy of the future.  

### OnCompletion

```c++
void OnCompletion(
  CompletionCallback callback,
  void *user_data
) const 
```  
Register a single callback that will be called at most once, when the future is completed.

If you call any [OnCompletion()](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1a963b7b47edaecabcd58303632d9e45ca) method more than once on the same future, only the most recent callback you registered with [OnCompletion()](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1a963b7b47edaecabcd58303632d9e45ca) will be called. When your callback is called, the user_data that you supplied here will be passed back as the second parameter.

<br />

|                                                                                                                         Details                                                                                                                          ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-------------|--------------------------------------------------------------| | `callback`  | Function pointer to your callback.                           | | `user_data` | Optional user data. We will pass this back to your callback. | |

### OnCompletion

```c++
void OnCompletion(
  std::function< void(const FutureBase &)> callback
) const 
```  
Register a single callback that will be called at most once, when the future is completed.

If you call any [OnCompletion()](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1a963b7b47edaecabcd58303632d9e45ca) method more than once on the same future, only the most recent callback you registered with [OnCompletion()](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1a963b7b47edaecabcd58303632d9e45ca) will be called.
| **Note:** This method is not available when using STLPort on Android, as `std::function` is not supported on STLPort.

<br />

|                                                Details                                                ||
|------------|-------------------------------------------------------------------------------------------|
| Parameters | |------------|-----------------------------| | `callback` | Function or lambda to call. | |

### Release

```c++
void Release()
```  
Explicitly release the internal resources for a future.

[Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) will become invalid.  

### error

```c++
int error() const 
```  
When [status()](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1a7b1a3fdc54483440d1ec8d0dc4a64883) is [firebase::kFutureStatusComplete](https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1aa31afaaff6e6fe7cf1f2a13961273fbaa33e40478e42949d7dc59951089f56921), returns the API-defined error code.

Otherwise, return value is undefined.  

### error_message

```c++
const char * error_message() const 
```  
When [status()](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1a7b1a3fdc54483440d1ec8d0dc4a64883) is [firebase::kFutureStatusComplete](https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1aa31afaaff6e6fe7cf1f2a13961273fbaa33e40478e42949d7dc59951089f56921), returns the API-defined error message, as human-readable text, or an empty string if the API does not provide a human readable description of the error.


| **Note:** The returned pointer is only valid for the lifetime of the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) or its copies.

<br />

### operator!=

```c++
bool operator!=(
  const FutureBase & rhs
) const 
```  
Returns true if the two Futures reference different results.  

### operator=

```c++
FutureBase & operator=(
  const FutureBase & rhs
)
```  
Copy an untyped future.  

### operator==

```c++
bool operator==(
  const FutureBase & rhs
) const 
```  
Returns true if the two Futures reference the same result.  

### result_void

```c++
const void * result_void() const 
```  
Result of the asynchronous call, or nullptr if the result is still pending.

Cast is required since GetFutureResult() returns void\*.  

### status

```c++
FutureStatus status() const 
```  
Completion status of the asynchronous call.  

### \~FutureBase

```c++
 ~FutureBase()
```