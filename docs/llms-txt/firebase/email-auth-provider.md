# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/email-auth-provider.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/auth/email-auth-provider.md.txt

# Firebase.Auth.EmailAuthProvider Class Reference

# Firebase.Auth.EmailAuthProvider

Use email and password to authenticate.

## Summary

Allows developers to use the email and password credentials as they could other auth providers. For example, this can be used to change passwords, log in, etc.

|                                                                                               ### Properties                                                                                               ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| [ProviderId](https://firebase.google.com/docs/reference/unity/class/firebase/auth/email-auth-provider#class_firebase_1_1_auth_1_1_email_auth_provider_1a636c9923fd54ccb85d23bb4718132fa6) | `static string` |

|                                                                                                                                                                     ### Public static functions                                                                                                                                                                     ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [GetCredential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/email-auth-provider#class_firebase_1_1_auth_1_1_email_auth_provider_1a0a4f7bfd051e1ec5282d72b56e42fadf)`(string email, string password)` | [Credential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/credential#class_firebase_1_1_auth_1_1_credential) |

## Properties

### ProviderId

```c#
static string ProviderId
```  

## Public static functions

### GetCredential

```c#
Credential GetCredential(
  string email,
  string password
)
```