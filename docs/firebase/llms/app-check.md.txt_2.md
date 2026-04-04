# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check.md.txt

# firebase::app_check::AppCheck Class Reference

# firebase::app_check::AppCheck


`#include <app_check.h>`

Firebase [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) Check object.

## Summary

[App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) Check helps protect your API resources from abuse by preventing unauthorized clients from accessing your backend resources.

With [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) Check, devices running your app will use an [AppCheckProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider#classfirebase_1_1app__check_1_1_app_check_provider) that attests to one or both of the following:

- Requests originate from your authentic app
- Requests originate from an authentic, untampered device

<br />

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check_1a3e45a64dc4abe307b6fe2d5582a667b6()` Destructor. ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check_1a3e7439d63ade51c66456b695face3936(https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-listener#classfirebase_1_1app__check_1_1_app_check_listener *listener)` | `void` Registers an [AppCheckListener](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-listener#classfirebase_1_1app__check_1_1_app_check_listener) to changes in the token state. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check_1ae9ac2e41ffc484721d7343d78f852448(bool force_refresh)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/struct/firebase/app-check/app-check-token#structfirebase_1_1app__check_1_1_app_check_token >` Requests a Firebase [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) Check token. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check_1a0318f539d3d91754e9202f88b1c7ff83()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/struct/firebase/app-check/app-check-token#structfirebase_1_1app__check_1_1_app_check_token >` Returns the result of the most recent call to [GetAppCheckToken()](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check_1ae9ac2e41ffc484721d7343d78f852448);. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check_1aeda964041317b387a343c02379961c52(https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-listener#classfirebase_1_1app__check_1_1_app_check_listener *listener)` | `void` Unregisters an [AppCheckListener](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-listener#classfirebase_1_1app__check_1_1_app_check_listener) to changes in the token state. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check_1a8550e8e32e26c53d4d793a3135125fa9(bool is_token_auto_refresh_enabled)` | `void` Sets the isTokenAutoRefreshEnabled flag. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check_1ae002dc4c8c0ded51636e0ce9266b9a76()` | `::https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app *` Get the [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) that this [AppCheck](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check) was created with. |

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check_1ae43a5ff0f596e1fe553182ca8ef2b5ab(::https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app *app)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check *` Gets the instance of [AppCheck](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check) associated with the given [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) instance. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check_1a4fcaddd90087f702ce90de7c6734c6ef(https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider-factory#classfirebase_1_1app__check_1_1_app_check_provider_factory *factory)` | `void` Installs the given [AppCheckProviderFactory](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider-factory#classfirebase_1_1app__check_1_1_app_check_provider_factory), overwriting any that were previously associated with this [AppCheck](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check) instance. |

## Public functions

### AddAppCheckListener

```c++
void AddAppCheckListener(
  AppCheckListener *listener
)
```
Registers an [AppCheckListener](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-listener#classfirebase_1_1app__check_1_1_app_check_listener) to changes in the token state.

This method should be used ONLY if you need to authorize requests to a non-Firebase backend. Requests to Firebase backends are authorized automatically if configured.

### GetAppCheckToken

```c++
Future< AppCheckToken > GetAppCheckToken(
  bool force_refresh
)
```
Requests a Firebase [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) Check token.

This method should be used ONLY if you need to authorize requests to a non-Firebase backend. Requests to Firebase backends are authorized automatically if configured.

### GetAppCheckTokenLastResult

```c++
Future< AppCheckToken > GetAppCheckTokenLastResult()
```
Returns the result of the most recent call to [GetAppCheckToken()](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check_1ae9ac2e41ffc484721d7343d78f852448);.

### RemoveAppCheckListener

```c++
void RemoveAppCheckListener(
  AppCheckListener *listener
)
```
Unregisters an [AppCheckListener](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-listener#classfirebase_1_1app__check_1_1_app_check_listener) to changes in the token state.

### SetTokenAutoRefreshEnabled

```c++
void SetTokenAutoRefreshEnabled(
  bool is_token_auto_refresh_enabled
)
```
Sets the isTokenAutoRefreshEnabled flag.

### app

```c++
::firebase::App * app()
```
Get the [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) that this [AppCheck](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check) was created with.

<br />

| Details ||
|---|---|
| **Returns** | The [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) this [AppCheck](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check) was created with. |

### \~AppCheck

```c++
 ~AppCheck()
```
Destructor.

You may delete an instance of [AppCheck](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check) when you are finished using it to shut down the [AppCheck](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check) library.

## Public static functions

### GetInstance

```c++
AppCheck * GetInstance(
  ::firebase::App *app
)
```
Gets the instance of [AppCheck](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check) associated with the given [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) instance.

### SetAppCheckProviderFactory

```c++
void SetAppCheckProviderFactory(
  AppCheckProviderFactory *factory
)
```
Installs the given [AppCheckProviderFactory](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check-provider-factory#classfirebase_1_1app__check_1_1_app_check_provider_factory), overwriting any that were previously associated with this [AppCheck](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check) instance.

Any AppCheckTokenListeners attached to this [AppCheck](https://firebase.google.com/docs/reference/cpp/class/firebase/app-check/app-check#classfirebase_1_1app__check_1_1_app_check) instance will be transferred from existing factories to the newly installed one.

Automatic token refreshing will only occur if the global isDataCollectionDefaultEnabled flag is set to true. To allow automatic token refreshing for Firebase [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) Check without changing the isDataCollectionDefaultEnabled flag for other Firebase SDKs, call setTokenAutoRefreshEnabled(bool) after installing the factory.

This method should be called before initializing the Firebase [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app).