# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/additional-user-info.md.txt

# firebase::auth::AdditionalUserInfo Struct Reference

# firebase::auth::AdditionalUserInfo


`#include <user.h>`

Additional user data returned from an identity provider.

## Summary

| ### Public attributes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/additional-user-info#structfirebase_1_1auth_1_1_additional_user_info_1a7052241b279c9a1535655d61d5257d9f` | `std::map< https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant, https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant >` Additional identity-provider specific information. |
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/additional-user-info#structfirebase_1_1auth_1_1_additional_user_info_1a22f21833ad85e87385a4d76a9526cb69` | `std::string` The provider identifier. |
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/additional-user-info#structfirebase_1_1auth_1_1_additional_user_info_1af2d15f430bb4cf7d23ff695b7011c8fb` | `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential` On a nonce-based credential link failure where the user has already linked to the provider, the Firebase auth service may provide an updated [Credential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential). |
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/additional-user-info#structfirebase_1_1auth_1_1_additional_user_info_1a176357fc06d2fc2a89bf3a8fa7601747` | `std::string` The name of the user. |

## Public attributes

### profile

```c++
std::map< Variant, Variant > firebase::auth::AdditionalUserInfo::profile
```
Additional identity-provider specific information.

Most likely a hierarchical key-value mapping, like a parsed JSON file. Note we use map instead of unordered_map to support older compilers.

### provider_id

```c++
std::string firebase::auth::AdditionalUserInfo::provider_id
```
The provider identifier.

### updated_credential

```c++
Credential firebase::auth::AdditionalUserInfo::updated_credential
```
On a nonce-based credential link failure where the user has already linked to the provider, the Firebase auth service may provide an updated [Credential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential).

If is_valid returns true on this credential, then it may be passed to a new [firebase::auth::Auth::SignInWithCredential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a16d92dd01886a3327afe08f65e0fa2b8) request to sign the user in with the provider.

### user_name

```c++
std::string firebase::auth::AdditionalUserInfo::user_name
```
The name of the user.