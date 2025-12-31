# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider-factory.md.txt

# firebase::app_check::AppCheckProviderFactory Class Reference

# firebase::app_check::AppCheckProviderFactory


**This is an abstract class.**


`#include <app_check.h>`

Interface for a factory that generates [AppCheckProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider#classfirebase_1_1app__check_1_1_app_check_provider)s.

## Summary

### Inheritance

Direct Known Subclasses:[firebase::app_check::AppAttestProviderFactory](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-attest-provider-factory), [firebase::app_check::DebugAppCheckProviderFactory](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/debug-app-check-provider-factory), [firebase::app_check::DeviceCheckProviderFactory](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/device-check-provider-factory), [firebase::app_check::PlayIntegrityProviderFactory](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/play-integrity-provider-factory)

| ### Constructors and Destructors ||
|---|---|
| [~AppCheckProviderFactory](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider-factory#classfirebase_1_1app__check_1_1_app_check_provider_factory_1aee0624a608e1ac6a712e59749f7879e0)`()` ||

|                                                                                                                                                                                                                                                                                                                                                                                                                        ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                         ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CreateProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider-factory#classfirebase_1_1app__check_1_1_app_check_provider_factory_1a97b71d4c5418a949a4ade9bf4e112652)`(`[App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app)` *app)=0` | `virtual `[AppCheckProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider#classfirebase_1_1app__check_1_1_app_check_provider)` *` Gets the [AppCheckProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider#classfirebase_1_1app__check_1_1_app_check_provider) associated with the given [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) instance, or creates one if none already exists. |

## Public functions

### CreateProvider

```c++
virtual AppCheckProvider * CreateProvider(
  App *app
)=0
```  
Gets the [AppCheckProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider#classfirebase_1_1app__check_1_1_app_check_provider) associated with the given [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) instance, or creates one if none already exists.  

### \~AppCheckProviderFactory

```c++
virtual  ~AppCheckProviderFactory()=0
```