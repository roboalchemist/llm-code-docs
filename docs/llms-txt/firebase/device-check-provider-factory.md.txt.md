# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/device-check-provider-factory.md.txt

# firebase::app_check::DeviceCheckProviderFactory Class Reference

# firebase::app_check::DeviceCheckProviderFactory


`#include <device_check_provider.h>`

Implementation of an [AppCheckProviderFactory](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider-factory#classfirebase_1_1app__check_1_1_app_check_provider_factory) that builds DeviceCheckProviders.

## Summary

This is the default implementation.

### Inheritance

Inherits from: [firebase::app_check::AppCheckProviderFactory](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider-factory)

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/device-check-provider-factory#classfirebase_1_1app__check_1_1_device_check_provider_factory_1a0f2c150f0e6ec6021f06b53d8c0f006c()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/device-check-provider-factory#classfirebase_1_1app__check_1_1_device_check_provider_factory *` Gets an instance of this class for installation into a [firebase::app_check::AppCheck](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check) instance. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/device-check-provider-factory#classfirebase_1_1app__check_1_1_device_check_provider_factory_1ab3c7e24a3fad749e81fce4b10f1b2869(https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app *app) override` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider#classfirebase_1_1app__check_1_1_app_check_provider *` Gets the [AppCheckProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider#classfirebase_1_1app__check_1_1_app_check_provider) associated with the given [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) instance, or creates one if none already exists. |

## Public static functions

### GetInstance

```c++
DeviceCheckProviderFactory * GetInstance()
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