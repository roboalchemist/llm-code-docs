# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/twitter-auth-provider.md.txt

# firebase::auth::TwitterAuthProvider Class Reference

# firebase::auth::TwitterAuthProvider


`#include <credential.h>`

Use a token and secret provided by Twitter to authenticate.

## Summary

| ### Public static attributes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/twitter-auth-provider#classfirebase_1_1auth_1_1_twitter_auth_provider_1ac3dee562cc22ffae3bef8da6ce079cd7` | `const char *const` The string used to identify this provider. |

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/twitter-auth-provider#classfirebase_1_1auth_1_1_twitter_auth_provider_1a8e1bbdeb3d161a0ff880f86d1b7947ad(const char *token, const char *secret)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential` Generate a credential from the given Twitter token and password. |

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
  const char *token,
  const char *secret
)
```
Generate a credential from the given Twitter token and password.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `token` | The Twitter OAuth token. | | `secret` | The Twitter OAuth secret. | |
| **Returns** | New [Credential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential). |