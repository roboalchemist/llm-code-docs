# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/auth/auth-result.md.txt

# Firebase.Auth.AuthResult Class Reference

# Firebase.Auth.AuthResult

The result of operations that can affect authentication state.

## Summary

### Inheritance

Inherits from: SystemIDisposable

| ### Constructors and Destructors ||
|---|---|
| [AuthResult](https://firebase.google.com/docs/reference/unity/class/firebase/auth/auth-result#class_firebase_1_1_auth_1_1_auth_result_1a2355c91e604aa0264f5baa74c343dbcc)`()` ||

|                                                                                                                                                                                                                                                          ### Properties                                                                                                                                                                                                                                                           ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AdditionalUserInfo](https://firebase.google.com/docs/reference/unity/class/firebase/auth/auth-result#class_firebase_1_1_auth_1_1_auth_result_1a2e79e631c6b488d7bef980785ccbc942) | [AdditionalUserInfo](https://firebase.google.com/docs/reference/unity/class/firebase/auth/additional-user-info#class_firebase_1_1_auth_1_1_additional_user_info) Identity-provider specific information for the user, if the provider is one of Facebook, GitHub, Google, or Twitter.                                                          |
| [Credential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/auth-result#class_firebase_1_1_auth_1_1_auth_result_1a14aed856498032036063a22b30e6379d)         | [Credential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/credential#class_firebase_1_1_auth_1_1_credential) A [Credential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/credential#class_firebase_1_1_auth_1_1_credential) instance for the recently signed-in user.                          |
| [User](https://firebase.google.com/docs/reference/unity/class/firebase/auth/auth-result#class_firebase_1_1_auth_1_1_auth_result_1aa028c87cb8a6719d06d8334db56e13e2)               | [FirebaseUser](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user) The currently signed-in [FirebaseUser](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user), or null if there isn't one. |

|                                                                                       ### Public functions                                                                                       ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| [Dispose](https://firebase.google.com/docs/reference/unity/class/firebase/auth/auth-result#class_firebase_1_1_auth_1_1_auth_result_1a089bc4cb334d059a4b9c3022fd1d6295)`()`               | `void` |
| [Dispose](https://firebase.google.com/docs/reference/unity/class/firebase/auth/auth-result#class_firebase_1_1_auth_1_1_auth_result_1a0c0071d3ace31f1e07b6f19cae9ea7e8)`(bool disposing)` | `void` |

## Properties

### AdditionalUserInfo

```c#
AdditionalUserInfo AdditionalUserInfo
```  
Identity-provider specific information for the user, if the provider is one of Facebook, GitHub, Google, or Twitter.  

### Credential

```c#
Credential Credential
```  
A [Credential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/credential#class_firebase_1_1_auth_1_1_credential) instance for the recently signed-in user.  

### User

```c#
FirebaseUser User
```  
The currently signed-in [FirebaseUser](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user), or null if there isn't one.

## Public functions

### AuthResult

```c#
 AuthResult()
```  

### Dispose

```c#
void Dispose()
```  

### Dispose

```c#
void Dispose(
  bool disposing
)
```