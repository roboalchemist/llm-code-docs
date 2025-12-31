# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/o-auth-provider.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/auth/o-auth-provider.md.txt

# Firebase.Auth.OAuthProvider Class Reference

# Firebase.Auth.OAuthProvider

OAuth2.0+UserInfo auth provider (OIDC compliant and non-compliant).

## Summary

|                                                                                                                                                                                     ### Public static functions                                                                                                                                                                                      ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [GetCredential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/o-auth-provider#class_firebase_1_1_auth_1_1_o_auth_provider_1a8a77e4f06f2f0f55f4b3f346ed9c4083)`(string ProviderId, string idToken, string accessToken)`                  | [Credential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/credential#class_firebase_1_1_auth_1_1_credential) |
| [GetCredential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/o-auth-provider#class_firebase_1_1_auth_1_1_o_auth_provider_1a6cd50768f224fe84003ccdc8817eeb56)`(string ProviderId, string idToken, string rawNonce, string accessToken)` | [Credential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/credential#class_firebase_1_1_auth_1_1_credential) |

## Public static functions

### GetCredential

```c#
Credential GetCredential(
  string ProviderId,
  string idToken,
  string accessToken
)
```  

### GetCredential

```c#
Credential GetCredential(
  string ProviderId,
  string idToken,
  string rawNonce,
  string accessToken
)
```