# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/google-auth-provider.md.txt

# firebase::auth::GoogleAuthProvider Class Reference

# firebase::auth::GoogleAuthProvider


`#include <credential.h>`

Use an ID token and access token provided by Google to authenticate.

## Summary

| ### Public static attributes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/google-auth-provider#classfirebase_1_1auth_1_1_google_auth_provider_1af27fc68b0be005bf9a1035d6eac9f6a5` | `const char *const` The string used to identify this provider. |

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/google-auth-provider#classfirebase_1_1auth_1_1_google_auth_provider_1ae8e704941c24348f4d04f5d77a059d95(const char *id_token, const char *access_token)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential` Generate a credential from the given Google ID token and/or access token. |

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
  const char *id_token,
  const char *access_token
)
```
Generate a credential from the given Google ID token and/or access token.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `id_token` | Google Sign-In ID token. | | `access_token` | Google Sign-In access token. | |
| **Returns** | New [Credential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential). |