# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result.md.txt

# firebase::auth::AuthResult Struct Reference

# firebase::auth::AuthResult


`#include <user.h>`

The result of operations that can affect authentication state.

## Summary

| ### Public attributes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result_1aef94bf126d5ef8027d3dc075cf35f856` | `https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/additional-user-info#structfirebase_1_1auth_1_1_additional_user_info` Identity-provider specific information for the user, if the provider is one of Facebook, GitHub, Google, or Twitter. |
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result_1a44b78f50ef2707b6cb731b5163d5826b` | `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential` A [Credential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential) instance for the recently signed-in user. |
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result_1a531cac980c6c47951ceeb67e3870ea94` | `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user` The currently signed-in [User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user), or an invalid [User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user) if there isn't one (i.e. |

## Public attributes

### additional_user_info

```c++
AdditionalUserInfo firebase::auth::AuthResult::additional_user_info
```
Identity-provider specific information for the user, if the provider is one of Facebook, GitHub, Google, or Twitter.

### credential

```c++
Credential firebase::auth::AuthResult::credential
```
A [Credential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential) instance for the recently signed-in user.

This is not supported on desktop platforms.

### user

```c++
User firebase::auth::AuthResult::user
```
The currently signed-in [User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user), or an invalid [User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user) if there isn't one (i.e.

if the user is signed-out then is_valid() will return false).