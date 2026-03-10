# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/play-integrity-provider-factory.md.txt

# firebase::app_check::PlayIntegrityProviderFactory Class Reference

# firebase::app_check::PlayIntegrityProviderFactory


`#include <play_integrity_provider.h>`

Implementation of an [AppCheckProviderFactory](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider-factory#classfirebase_1_1app__check_1_1_app_check_provider_factory) that builds PlayIntegrityProviders.

## Summary

This is the default implementation.

### Inheritance

Inherits from: [firebase::app_check::AppCheckProviderFactory](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider-factory)

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/play-integrity-provider-factory#classfirebase_1_1app__check_1_1_play_integrity_provider_factory_1a5805df42238ff631e9b4f1a60ded4e0b()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/play-integrity-provider-factory#classfirebase_1_1app__check_1_1_play_integrity_provider_factory *` Gets an instance of this class for installation into a [firebase::app_check::AppCheck](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check) instance. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/play-integrity-provider-factory#classfirebase_1_1app__check_1_1_play_integrity_provider_factory_1a70227bf7b334548a119d4a46f7729e89(https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app *app) override` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider#classfirebase_1_1app__check_1_1_app_check_provider *` Gets the [AppCheckProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider#classfirebase_1_1app__check_1_1_app_check_provider) associated with the given [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) instance, or creates one if none already exists. |

## Public static functions

### GetInstance

```c++
PlayIntegrityProviderFactory * GetInstance()
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