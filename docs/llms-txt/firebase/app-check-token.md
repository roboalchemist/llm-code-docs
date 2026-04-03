# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/app-check/app-check-token.md.txt

# Firebase.AppCheck.AppCheckToken Struct Reference

# Firebase.AppCheck.AppCheckToken

Token used by the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) App Check service.

## Summary

Struct to hold tokens emitted by the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) App Check service which are minted upon a successful application verification. These tokens are the federated output of a verification flow, the structure of which is independent of the mechanism by which the application was verified.

|                                                                                                                                                        ### Properties                                                                                                                                                         ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [ExpireTime](https://firebase.google.com/docs/reference/unity/struct/firebase/app-check/app-check-token#struct_firebase_1_1_app_check_1_1_app_check_token_1a2b44f30293400260f5ff96b9a81a7def) | `DateTime` The time at which the token will expire.                                                                            |
| [Token](https://firebase.google.com/docs/reference/unity/struct/firebase/app-check/app-check-token#struct_firebase_1_1_app_check_1_1_app_check_token_1ac385c12f3d41d0bbd972af1163c39f1d)      | `string` A [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) App Check token. |

## Properties

### ExpireTime

```c#
DateTime Firebase::AppCheck::AppCheckToken::ExpireTime
```  
The time at which the token will expire.  

### Token

```c#
string Firebase::AppCheck::AppCheckToken::Token
```  
A [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) App Check token.