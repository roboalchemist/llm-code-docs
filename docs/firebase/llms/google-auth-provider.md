# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/google-auth-provider.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/auth/google-auth-provider.md.txt

# Firebase.Auth.GoogleAuthProvider Class Reference

# Firebase.Auth.GoogleAuthProvider

Use an ID token and access token provided by Google to authenticate.

## Summary

|                                                                                                ### Properties                                                                                                ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| [ProviderId](https://firebase.google.com/docs/reference/unity/class/firebase/auth/google-auth-provider#class_firebase_1_1_auth_1_1_google_auth_provider_1ab23c10781107b3af076640a21b119e44) | `static string` |

|                                                                                                                                                                        ### Public static functions                                                                                                                                                                         ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [GetCredential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/google-auth-provider#class_firebase_1_1_auth_1_1_google_auth_provider_1a68952a1ba2bbf1662128442470ff3385)`(string idToken, string accessToken)` | [Credential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/credential#class_firebase_1_1_auth_1_1_credential) |

## Properties

### ProviderId

```c#
static string ProviderId
```  

## Public static functions

### GetCredential

```c#
Credential GetCredential(
  string idToken,
  string accessToken
)
```