# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/future.md.txt

# firebase::Future Class Reference

# firebase::Future


`#include <future.h>`

Type-specific version of [FutureBase](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base).

## Summary

The Firebase C++ SDK uses this class to return results from asynchronous operations. All Firebase C++ functions and method calls that operate asynchronously return a [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future), and provide a "LastResult" function to retrieve the most recent [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) result.


```c++
// You can retrieve the Future from the function call directly, like this:
Future< SampleResultType > future = firebase::SampleAsyncOperation();

// Or you can retrieve it later, like this:
firebase::SampleAsyncOperation();
// [...]
Future< SampleResultType > future =
    firebase::SampleAsyncOperationLastResult();
```

<br />

When you have a [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) from an asynchronous operation, it will eventually complete. Once it is complete, you can check for errors (a nonzero [error()](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1ab7a9ffdf8f16b4473291219d244db26c) means an error occurred) and get the result data if no error occurred by calling [result()](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future_1a919675755a271575134464a01788b41d).

There are two ways to find out that a [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) has completed. You can poll its [status()](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1a7b1a3fdc54483440d1ec8d0dc4a64883), or set an [OnCompletion()](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future_1a334de3fc89aefc4704c89f3fb7ba1c08) callback:


```c++
// Check whether the status is kFutureStatusComplete.
if (future.status() == firebase::kFutureStatusComplete) {
  if (future.error() == 0) {
    DoSomethingWithResultData(future.result());
  }
  else {
    LogMessage("Error %d: %s", future.error(), future.error_message());
  }
}

// Or, set an OnCompletion callback, which accepts a C++11 lambda or
// function pointer. You can pass your own user data to the callback. In
// most cases, the callback will be running in a different thread, so take
// care to make sure your code is thread-safe.
future.OnCompletion([](const Future< SampleResultType >& completed_future,
                       void* user_data) {
  // We are probably in a different thread right now.
  if (completed_future.error() == 0) {
    DoSomethingWithResultData(completed_future.result());
  }
  else {
    LogMessage("Error %d: %s",
               completed_future.error(),
               completed_future.error_message());
  }
}, user_data);
```

<br />

<br />

|                                                                                                                                                             Details                                                                                                                                                              ||
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Template Parameters | |--------------|------------------------------------------------------------------------------------------------------------------------------------| | `ResultType` | The type of this [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)'s result. | |

### Inheritance

Inherits from: [firebase::FutureBase](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base)

| ### Constructors and Destructors ||
|---|---|
| [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future_1a3b44ecf20054fee31c757d48f4abd47b)`()` Construct a future. ||

|                                                                                                                                    ### Public types                                                                                                                                    ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| [TypedCompletionCallback](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future_1a5355f6f1b10287964dd262cfcae47a27)`)(const Future< ResultType > &result_data, void *user_data)` | typedef `void(*` Function pointer for a completion callback. |

|                                                                                                                                                                                                                 ### Public functions                                                                                                                                                                                                                  ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [OnCompletion](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future_1a334de3fc89aefc4704c89f3fb7ba1c08)`(`[TypedCompletionCallback](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future_1a5355f6f1b10287964dd262cfcae47a27)` callback, void *user_data) const ` | `void` Register a single callback that will be called at most once, when the future is completed. |
| [OnCompletion](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future_1a032aec46e1b33e7a5ea2a2989f60b247)`(std::function< void(const `[Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< ResultType > &)> callback) const `                          | `void` Register a single callback that will be called at most once, when the future is completed. |
| [result](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future_1a919675755a271575134464a01788b41d)`() const `                                                                                                                                                                                              | `const ResultType *` Result of the asynchronous call, or nullptr if the result is still pending.  |

## Public types

### TypedCompletionCallback

```c++
void(* TypedCompletionCallback)(const Future< ResultType > &result_data, void *user_data)
```  
Function pointer for a completion callback.

When we call this, we will send the completed future, along with the user data that you specified when you set up the callback.

## Public functions

### Future

```c++
 Future()
```  
Construct a future.  

### OnCompletion

```c++
void OnCompletion(
  TypedCompletionCallback callback,
  void *user_data
) const 
```  
Register a single callback that will be called at most once, when the future is completed.

If you call any [OnCompletion()](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future_1a334de3fc89aefc4704c89f3fb7ba1c08) method more than once on the same future, only the most recent callback you registered will be called.

When your callback is called, the user_data that you supplied here will be passed back as the second parameter.


| **Note:** This is the same callback as [FutureBase::OnCompletion()](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1a963b7b47edaecabcd58303632d9e45ca), so you can't expect to set both and have both run; again, only the most recently registered one will run.

<br />

|                                                                                                                         Details                                                                                                                          ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-------------|--------------------------------------------------------------| | `callback`  | Function pointer to your callback.                           | | `user_data` | Optional user data. We will pass this back to your callback. | |

### OnCompletion

```c++
void OnCompletion(
  std::function< void(const Future< ResultType > &)> callback
) const 
```  
Register a single callback that will be called at most once, when the future is completed.

If you call any [OnCompletion()](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future_1a334de3fc89aefc4704c89f3fb7ba1c08) method more than once on the same future, only the most recent callback you registered will be called.


| **Note:** This method is not available when using STLPort on Android, as `std::function` is not supported on STLPort.
| **Note:** This is the same callback as [FutureBase::OnCompletion()](https://firebase.google.com/docs/reference/cpp/class/firebase/future-base#classfirebase_1_1_future_base_1a963b7b47edaecabcd58303632d9e45ca), so you can't expect to set both and have both run; again, only the most recently registered one will run.

<br />

|                                                Details                                                ||
|------------|-------------------------------------------------------------------------------------------|
| Parameters | |------------|-----------------------------| | `callback` | Function or lambda to call. | |

### result

```c++
const ResultType * result() const 
```  
Result of the asynchronous call, or nullptr if the result is still pending.

Allows the API to provide a type-specific interface.