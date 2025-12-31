# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/twitter-auth-provider.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/auth/twitter-auth-provider.md.txt

# Firebase.Auth.TwitterAuthProvider Class Reference

# Firebase.Auth.TwitterAuthProvider

Use a token and secret provided by Twitter to authenticate.

## Summary

|                                                                                                 ### Properties                                                                                                 ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| [ProviderId](https://firebase.google.com/docs/reference/unity/class/firebase/auth/twitter-auth-provider#class_firebase_1_1_auth_1_1_twitter_auth_provider_1a3e60b56a16bd3b08efffc2d4873eab74) | `static string` |

|                                                                                                                                                                      ### Public static functions                                                                                                                                                                      ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [GetCredential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/twitter-auth-provider#class_firebase_1_1_auth_1_1_twitter_auth_provider_1a2d206927ae8272c3e86088f25d8d9836)`(string token, string secret)` | [Credential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/credential#class_firebase_1_1_auth_1_1_credential) |

## Properties

### ProviderId

```c#
static string ProviderId
```  

## Public static functions

### GetCredential

```c#
Credential GetCredential(
  string token,
  string secret
)
```