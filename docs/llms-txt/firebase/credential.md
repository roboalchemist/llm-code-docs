# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/auth/credential.md.txt

# Firebase.Auth.Credential Class Reference

# Firebase.Auth.Credential

Authentication credentials for an authentication provider.

## Summary

An authentication provider is a service that allows you to authenticate a user. [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) provides email/password authentication, but there are also external authentication providers such as Facebook.

### Inheritance

Inherits from: SystemIDisposable  
Direct Known Subclasses:[Firebase.Auth.PhoneAuthCredential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-credential)

| ### Constructors and Destructors ||
|---|---|
| [Credential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/credential#class_firebase_1_1_auth_1_1_credential_1a0f8fcd892ae1e97fd218f7f74187bd05)`()` ||

|                                                                                 ### Properties                                                                                  ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| [Provider](https://firebase.google.com/docs/reference/unity/class/firebase/auth/credential#class_firebase_1_1_auth_1_1_credential_1a492150cc0854ccfaa2d5fb9ec88ae79c) | `string` |

|                                                                                          ### Public functions                                                                                          ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| [Dispose](https://firebase.google.com/docs/reference/unity/class/firebase/auth/credential#class_firebase_1_1_auth_1_1_credential_1a4c9743ff7103082da48aa911aee715f5)`()`               | `void`         |
| [Dispose](https://firebase.google.com/docs/reference/unity/class/firebase/auth/credential#class_firebase_1_1_auth_1_1_credential_1a989e9c794d964c7c45f9c471d46d1f35)`(bool disposing)` | `virtual void` |
| [IsValid](https://firebase.google.com/docs/reference/unity/class/firebase/auth/credential#class_firebase_1_1_auth_1_1_credential_1acd9af81b02e1362baf0cb3c13de0e236)`()`               | `bool`         |

## Properties

### Provider

```c#
string Provider
```  

## Public functions

### Credential

```c#
 Credential()
```  

### Dispose

```c#
void Dispose()
```  

### Dispose

```c#
virtual void Dispose(
  bool disposing
)
```  

### IsValid

```c#
bool IsValid()
```