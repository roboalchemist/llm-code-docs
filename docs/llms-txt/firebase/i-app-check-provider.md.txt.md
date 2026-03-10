# Source: https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider.md.txt

# Firebase.AppCheck.IAppCheckProvider

Interface for a provider that generates [AppCheckToken](https://firebase.google.com/docs/reference/unity/struct/firebase/app-check/app-check-token#struct_firebase_1_1_app_check_1_1_app_check_token)s.

## Summary

This provider can be called at any time by any [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) library that depends (optionally or otherwise) on [AppCheckToken](https://firebase.google.com/docs/reference/unity/struct/firebase/app-check/app-check-token#struct_firebase_1_1_app_check_1_1_app_check_token)s. This provider is responsible for determining if it can create a new token at the time of the call and returning that new token if it can. The provider must also supply a token when GetLimitedUseTokenAsync is called. In the case a provider does not support limited use tokens an default implementation returning a non-limited use token is recommended.

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider#interface_firebase_1_1_app_check_1_1_i_app_check_provider_1ae1366a8dcbccc93b4e0df989ae66f17c()` | `System.Threading.Tasks.Task< https://firebase.google.com/docs/reference/unity/struct/firebase/app-check/app-check-token#struct_firebase_1_1_app_check_1_1_app_check_token >` Returns a limited-use [AppCheckToken](https://firebase.google.com/docs/reference/unity/struct/firebase/app-check/app-check-token#struct_firebase_1_1_app_check_1_1_app_check_token) or throws an exception with an error code and error message. |
| `https://firebase.google.com/docs/reference/unity/interface/firebase/app-check/i-app-check-provider#interface_firebase_1_1_app_check_1_1_i_app_check_provider_1a1baff1bfe9f974bb4fdd71cb7658f16b()` | `System.Threading.Tasks.Task< https://firebase.google.com/docs/reference/unity/struct/firebase/app-check/app-check-token#struct_firebase_1_1_app_check_1_1_app_check_token >` Returns an [AppCheckToken](https://firebase.google.com/docs/reference/unity/struct/firebase/app-check/app-check-token#struct_firebase_1_1_app_check_1_1_app_check_token) or throws an exception with an error code and error message. |

## Public functions

### GetLimitedUseTokenAsync

```c#
System.Threading.Tasks.Task< AppCheckToken > GetLimitedUseTokenAsync()
```
Returns a limited-use [AppCheckToken](https://firebase.google.com/docs/reference/unity/struct/firebase/app-check/app-check-token#struct_firebase_1_1_app_check_1_1_app_check_token) or throws an exception with an error code and error message.

### GetTokenAsync

```c#
System.Threading.Tasks.Task< AppCheckToken > GetTokenAsync()
```
Returns an [AppCheckToken](https://firebase.google.com/docs/reference/unity/struct/firebase/app-check/app-check-token#struct_firebase_1_1_app_check_1_1_app_check_token) or throws an exception with an error code and error message.