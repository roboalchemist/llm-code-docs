# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/o-auth-provider.md.txt

# firebase::auth::OAuthProvider Class Reference

# firebase::auth::OAuthProvider


`#include <credential.h>`

OAuth2.0+UserInfo auth provider (OIDC compliant and non-compliant).

## Summary

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/o-auth-provider#classfirebase_1_1auth_1_1_o_auth_provider_1ae55846af54eb69df3f8af05bd583d003(const char *provider_id, const char *id_token, const char *access_token)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential` Generate a credential for an OAuth2 provider. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/o-auth-provider#classfirebase_1_1auth_1_1_o_auth_provider_1a0689664c5877e71f3ba9a6949a848d53(const char *provider_id, const char *id_token, const char *raw_nonce, const char *access_token)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential` Generate a credential for an OAuth2 provider. |

## Public static functions

### GetCredential

```c++
Credential GetCredential(
  const char *provider_id,
  const char *id_token,
  const char *access_token
)
```
Generate a credential for an OAuth2 provider.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `provider_id` | Name of the OAuth2 provider TODO(jsanmiya) add examples. | | `id_token` | The authentication token (OIDC only). | | `access_token` | TODO(jsanmiya) add explanation (currently missing from Android and iOS implementations). | |

### GetCredential

```c++
Credential GetCredential(
  const char *provider_id,
  const char *id_token,
  const char *raw_nonce,
  const char *access_token
)
```
Generate a credential for an OAuth2 provider.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `provider_id` | Name of the OAuth2 provider. | | `id_token` | The authentication token (OIDC only). | | `raw_nonce` | The raw nonce associated with the [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) credential being created. | | `access_token` | The access token associated with the [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) credential to be created, if available. This value may be null. | |