# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/module-initializer.md.txt

# firebase::ModuleInitializer Class Reference

# firebase::ModuleInitializer


`#include <util.h>`

Utility class to help with initializing Firebase modules.

## Summary

This optional class handles a basic Firebase C++ SDK code pattern: attempt to initialize a Firebase module, and if the initialization fails on Android due to Google Play services being unavailable, prompt the user to update/enable Google Play services on their device.

If the developer wants more advanced behavior (for example, wait to prompt the user to update or enable Google Play services until later, or opt not to use Firebase modules), they can still initialize each Firebase module individually, and use [google_play_services::MakeAvailable()](https://firebase.google.com/docs/reference/cpp/namespace/google-play-services#namespacegoogle__play__services_1a9b9a9a553ee7476d697260c685074520) directly if any initializations fail.

| ### Constructors and Destructors ||
|---|---|
| [ModuleInitializer](https://firebase.google.com/docs/reference/cpp/class/firebase/module-initializer#classfirebase_1_1_module_initializer_1a1f3a90e6499d1085fe1cf24c4db4e913)`()` ||
| [~ModuleInitializer](https://firebase.google.com/docs/reference/cpp/class/firebase/module-initializer#classfirebase_1_1_module_initializer_1a4089203a9ee61bb3ca8e0b0e0f6e4354)`()` ||

|                                                                                                                                                                                                                       ### Public types                                                                                                                                                                                                                       ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [InitializerFn](https://firebase.google.com/docs/reference/cpp/class/firebase/module-initializer#classfirebase_1_1_module_initializer_1a49631e5dc96192b19dd233e92247b3a4)`)(App *app, void *context)` | typedef [InitResult](https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a8f058cad989f8f1a6c5b42a77a8c3478)`(*` Initialization function, which should initialize a single Firebase module and return the InitResult. |

|                                                                                                                                                                                                                                                                                                                                                                                                     ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                     ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Initialize](https://firebase.google.com/docs/reference/cpp/class/firebase/module-initializer#classfirebase_1_1_module_initializer_1a99212e8f9418bacd23eab5e26ffa693d)`(`[App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app)` *app, void *context, const `[InitializerFn](https://firebase.google.com/docs/reference/cpp/class/firebase/module-initializer#classfirebase_1_1_module_initializer_1a49631e5dc96192b19dd233e92247b3a4)` *init_fns, size_t init_fns_count)` | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Initialize Firebase modules by calling one or more user-supplied functions, each of which must initialize at most one library, and should return the InitResult of the initialization. |
| [Initialize](https://firebase.google.com/docs/reference/cpp/class/firebase/module-initializer#classfirebase_1_1_module_initializer_1a8e73d8127898d542954d5af8f551e41d)`(`[App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app)` *app, void *context, `[InitializerFn](https://firebase.google.com/docs/reference/cpp/class/firebase/module-initializer#classfirebase_1_1_module_initializer_1a49631e5dc96192b19dd233e92247b3a4)` init_fn)`                                | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Initialize one Firebase module by calling a single user-supplied function that should initialize a Firebase module and return the InitResult.                                          |
| [InitializeLastResult](https://firebase.google.com/docs/reference/cpp/class/firebase/module-initializer#classfirebase_1_1_module_initializer_1a82684fa3aaf42840814eb3fee6c8de4b)`()`                                                                                                                                                                                                                                                                                                                               | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Get the result of the most recent call to.                                                                                                                                             |

## Public types

### InitializerFn

```c++
InitResult(* InitializerFn)(App *app, void *context)
```  
Initialization function, which should initialize a single Firebase module and return the InitResult.

## Public functions

### Initialize

```c++
Future< void > Initialize(
  App *app,
  void *context,
  const InitializerFn *init_fns,
  size_t init_fns_count
)
```  
Initialize Firebase modules by calling one or more user-supplied functions, each of which must initialize at most one library, and should return the InitResult of the initialization.

This function will run the initializers in order, checking the return value of each. On Android, if the InitResult returned is kInitResultFailedMissingDependency, this indicates that Google Play services is not available and a Firebase module requires it. This function will attempt to fix Google Play services, and will retry initializations where it left off, beginning with the one that failed.


| **Note:** If a pending [Initialize()](https://firebase.google.com/docs/reference/cpp/class/firebase/module-initializer#classfirebase_1_1_module_initializer_1a99212e8f9418bacd23eab5e26ffa693d) is already running, this function will return the existing [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) rather than adding any new functions to the initializer list.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `app`            | The [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) that will be passed to the initializers, as well as used to fix Google Play services on Android if needed.    | | `context`        | User-defined context, which will be passed to the initializer functions. If you don't need this, you can use nullptr.                                                                                                      | | `init_fns`       | Your initialization functions to call, in an array. At their simplest, these will each simply call a single Firebase module's Initialize(app) and return the result, but you can perform more complex logic if you prefer. | | `init_fns_count` | Number of initialization functions in the supplied array.                                                                                                                                                                  | |
| **Returns** | A future result. When all of the initializers are completed, the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) will be completed with Error() = 0. If an initializer fails and the situation cannot be fixed, the [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) will be completed with Error() equal to the number of initializers that did not succeed (since they are run in order, this tells you which ones failed).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

### Initialize

```c++
Future< void > Initialize(
  App *app,
  void *context,
  InitializerFn init_fn
)
```  
Initialize one Firebase module by calling a single user-supplied function that should initialize a Firebase module and return the InitResult.

**See also:**Initialize(::firebase::App\*, void\*, const InitializerFn\*) for more information.  

### InitializeLastResult

```c++
Future< void > InitializeLastResult()
```  
Get the result of the most recent call to.

**See also:** [Initialize()](https://firebase.google.com/docs/reference/cpp/class/firebase/module-initializer#classfirebase_1_1_module_initializer_1a99212e8f9418bacd23eab5e26ffa693d).  

### ModuleInitializer

```c++
 ModuleInitializer()
```  

### \~ModuleInitializer

```c++
virtual  ~ModuleInitializer()
```