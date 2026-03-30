# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/git-hub-auth-provider.md.txt

# firebase::auth::GitHubAuthProvider Class Reference

# firebase::auth::GitHubAuthProvider


`#include <credential.h>`

Use an access token provided by GitHub to authenticate.

## Summary

| ### Public static attributes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/git-hub-auth-provider#classfirebase_1_1auth_1_1_git_hub_auth_provider_1a7e0c4de698f8d7498ef86aad0087a0cc` | `const char *const` The string used to identify this provider. |

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/git-hub-auth-provider#classfirebase_1_1auth_1_1_git_hub_auth_provider_1a0000b4bf671a49afe471b288ec220e34(const char *token)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential` Generate a credential from the given GitHub token. |

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
  const char *token
)
```
Generate a credential from the given GitHub token.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `token` | The GitHub OAuth access token. | |
| **Returns** | New [Credential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential). |