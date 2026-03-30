# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/debug-app-check-provider-factory.md.txt

# firebase::app_check::DebugAppCheckProviderFactory Class Reference

# firebase::app_check::DebugAppCheckProviderFactory


`#include <debug_provider.h>`

Implementation of an [AppCheckProviderFactory](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider-factory#classfirebase_1_1app__check_1_1_app_check_provider_factory) that builds DebugAppCheckProviders.

## Summary

DebugAppCheckProvider can exchange a debug token registered in the Firebase console for a Firebase [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) Check token. The debug provider is designed to enable testing applications on a simulator or test environment.

NOTE: Do not use the debug provider in applications used by real users.

### Inheritance

Inherits from: [firebase::app_check::AppCheckProviderFactory](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider-factory)

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/debug-app-check-provider-factory#classfirebase_1_1app__check_1_1_debug_app_check_provider_factory_1acbaff43d7007ba00e7fc1803364e3858()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/debug-app-check-provider-factory#classfirebase_1_1app__check_1_1_debug_app_check_provider_factory *` Gets an instance of this class for installation into a [firebase::app_check::AppCheck](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check) instance. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/debug-app-check-provider-factory#classfirebase_1_1app__check_1_1_debug_app_check_provider_factory_1a5f9df07e44d3702dd10e0137e90989fd(https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app *app) override` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider#classfirebase_1_1app__check_1_1_app_check_provider *` Gets the [AppCheckProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider#classfirebase_1_1app__check_1_1_app_check_provider) associated with the given [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) instance, or creates one if none already exists. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/debug-app-check-provider-factory#classfirebase_1_1app__check_1_1_debug_app_check_provider_factory_1a9e86d28c9242413103fc2fbf34d45c41(const std::string & token)` | `void` Sets the Debug Token to use when communicating with the backend. |

## Public static functions

### GetInstance

```c++
DebugAppCheckProviderFactory * GetInstance()
```
Gets an instance of this class for installation into a [firebase::app_check::AppCheck](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check) instance.

## Public functions

### CreateProvider

```c++
virtual firebase::app_check::AppCheckProvider * CreateProvider(
  App *app
) override
```
Gets the [AppCheckProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider#classfirebase_1_1app__check_1_1_app_check_provider) associated with the given [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) instance, or creates one if none already exists.

### SetDebugToken

```c++
void SetDebugToken(
  const std::string & token
)
```
Sets the Debug Token to use when communicating with the backend.

This should match a debug token set in the Firebase console for your [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app).