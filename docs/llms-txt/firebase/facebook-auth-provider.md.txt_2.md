# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/facebook-auth-provider.md.txt

# firebase::auth::FacebookAuthProvider Class Reference

# firebase::auth::FacebookAuthProvider


`#include <credential.h>`

Use an access token provided by Facebook to authenticate.

## Summary

| ### Public static attributes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/facebook-auth-provider#classfirebase_1_1auth_1_1_facebook_auth_provider_1adf4734567dcef06d7fb45e9423e2ec46` | `const char *const` The string used to identify this provider. |

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/facebook-auth-provider#classfirebase_1_1auth_1_1_facebook_auth_provider_1af651062585428cb113e4bf6e727d13d4(const char *access_token)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential` Generate a credential from the given Facebook token. |

## Public static attributes

### kProviderId

```c++
const char *const kProviderId
```
The string used to identify this provider.

## Public static functions

### GetCredential

```c++
Credential GetCredential(
  const char *access_token
)
```
Generate a credential from the given Facebook token.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `access_token` | Facebook token to generate the credential from. | |
| **Returns** | New [Credential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential). |