# Source: https://firebase.google.com/docs/reference/unity/class/firebase/app-check/firebase-app-check.md.txt

# Firebase.AppCheck.FirebaseAppCheck

[Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) App Check object.

## Summary

App Check helps protect your API resources from abuse by preventing unauthorized clients from accessing your backend resources.

With App Check, devices running your app will use an AppCheckProvider that attests to one or both of the following:

- Requests originate from your authentic app
- Requests originate from an authentic, untampered device

<br />

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/app-check/firebase-app-check#class_firebase_1_1_app_check_1_1_firebase_app_check_1a9391de983e65bb3b02be510da293e512` | `static https://firebase.google.com/docs/reference/unity/class/firebase/app-check/firebase-app-check#class_firebase_1_1_app_check_1_1_firebase_app_check` Gets the instance of [FirebaseAppCheck](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/firebase-app-check#class_firebase_1_1_app_check_1_1_firebase_app_check) associated with the default [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) instance. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/app-check/firebase-app-check#class_firebase_1_1_app_check_1_1_firebase_app_check_1a9b44661ff7646164cca19b8365cbbb0c` | `EventHandler< https://firebase.google.com/docs/reference/unity/class/firebase/app-check/token-changed-event-args#class_firebase_1_1_app_check_1_1_token_changed_event_args >` |

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/app-check/firebase-app-check#class_firebase_1_1_app_check_1_1_firebase_app_check_1a1017373ad82f686b0876ec36682698d8(https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app app)` | `https://firebase.google.com/docs/reference/unity/class/firebase/app-check/firebase-app-check#class_firebase_1_1_app_check_1_1_firebase_app_check` Gets the instance of [FirebaseAppCheck](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/firebase-app-check#class_firebase_1_1_app_check_1_1_firebase_app_check) associated with the given [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) instance. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/app-check/firebase-app-check#class_firebase_1_1_app_check_1_1_firebase_app_check_1ad58804b72473ed1c329e5c26098e138c(https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider-factory#interface_firebase_1_1_app_check_1_1_i_app_check_provider_factory factory)` | `void` Installs the given [IAppCheckProviderFactory](https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider-factory#interface_firebase_1_1_app_check_1_1_i_app_check_provider_factory), overwriting any that were previously associated with this [FirebaseAppCheck](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/firebase-app-check#class_firebase_1_1_app_check_1_1_firebase_app_check) instance. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/app-check/firebase-app-check#class_firebase_1_1_app_check_1_1_firebase_app_check_1a7fbd03c1ac0065e3e4b0ac7dc0be178b(bool forceRefresh)` | `System.Threading.Tasks.Task< https://firebase.google.com/docs/reference/unity/struct/firebase/app-check/app-check-token#struct_firebase_1_1_app_check_1_1_app_check_token >` Requests a [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) App Check token. This method should be used ONLY if you need to authorize requests to a non-Firebase backend. Requests to [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) backends are authorized automatically if configured. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/app-check/firebase-app-check#class_firebase_1_1_app_check_1_1_firebase_app_check_1a7976521cebcce0074a68a4d73f58921a()` | `System.Threading.Tasks.Task< https://firebase.google.com/docs/reference/unity/struct/firebase/app-check/app-check-token#struct_firebase_1_1_app_check_1_1_app_check_token >` Requests a [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) App Check token. This method should be used ONLY if you need to authorize requests to a non-Firebase backend. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/app-check/firebase-app-check#class_firebase_1_1_app_check_1_1_firebase_app_check_1a5663ff8344b39567bc68e7d81f8cd93b(bool isTokenAutoRefreshEnabled)` | `void` Sets the {. |

## Properties

### DefaultInstance

```c#
static FirebaseAppCheck DefaultInstance
```
Gets the instance of [FirebaseAppCheck](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/firebase-app-check#class_firebase_1_1_app_check_1_1_firebase_app_check) associated with the default [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) instance.

### TokenChanged

```c#
EventHandler< TokenChangedEventArgs > TokenChanged
```

## Public static functions

### GetInstance

```c#
FirebaseAppCheck GetInstance(
  FirebaseApp app
)
```
Gets the instance of [FirebaseAppCheck](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/firebase-app-check#class_firebase_1_1_app_check_1_1_firebase_app_check) associated with the given [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) instance.

### SetAppCheckProviderFactory

```c#
void SetAppCheckProviderFactory(
  IAppCheckProviderFactory factory
)
```
Installs the given [IAppCheckProviderFactory](https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider-factory#interface_firebase_1_1_app_check_1_1_i_app_check_provider_factory), overwriting any that were previously associated with this [FirebaseAppCheck](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/firebase-app-check#class_firebase_1_1_app_check_1_1_firebase_app_check) instance.

Automatic token refreshing will only occur if the global isDataCollectionDefaultEnabled flag is set to true. To allow automatic token refreshing for [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) App Check without changing the isDataCollectionDefaultEnabled flag for other [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) SDKs, call [SetTokenAutoRefreshEnabled(bool)](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/firebase-app-check#class_firebase_1_1_app_check_1_1_firebase_app_check_1a5663ff8344b39567bc68e7d81f8cd93b) after installing the factory.

This method should be called before initializing the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) App.

## Public functions

### GetAppCheckTokenAsync

```c#
System.Threading.Tasks.Task< AppCheckToken > GetAppCheckTokenAsync(
  bool forceRefresh
)
```
Requests a [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) App Check token. This method should be used ONLY if you need to authorize requests to a non-Firebase backend. Requests to [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) backends are authorized automatically if configured.

### GetLimitedUseAppCheckTokenAsync

```c#
System.Threading.Tasks.Task< AppCheckToken > GetLimitedUseAppCheckTokenAsync()
```
Requests a [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) App Check token. This method should be used ONLY if you need to authorize requests to a non-Firebase backend.

Returns limited-use tokens that are intended for use with your non-Firebase backend endpoints that are protected with Replay Protection. This method does not affect the token generation behavior of the [GetAppCheckTokenAsync()](https://firebase.google.com/docs/reference/unity/class/firebase/app-check/firebase-app-check#class_firebase_1_1_app_check_1_1_firebase_app_check_1a7fbd03c1ac0065e3e4b0ac7dc0be178b) method.

### SetTokenAutoRefreshEnabled

```c#
void SetTokenAutoRefreshEnabled(
  bool isTokenAutoRefreshEnabled
)
```
Sets the {.


```c#
isTokenAutoRefreshEnabled} flag. 
```

<br />