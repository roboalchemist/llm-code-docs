# Source: https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-credential.md.txt

# Firebase.Auth.PhoneAuthCredential Class Reference

# Firebase.Auth.PhoneAuthCredential

Wraps phone number and verification information for authentication purposes.

## Summary

### Inheritance

Inherits from: [Firebase.Auth.Credential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/credential)

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-credential#class_firebase_1_1_auth_1_1_phone_auth_credential_1a5528c4680dce17afcd9095dd0d0b0c11()` ||
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-credential#class_firebase_1_1_auth_1_1_phone_auth_credential_1ae8aa33681fe5e00831a8dc9e154443f2(https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-credential#class_firebase_1_1_auth_1_1_phone_auth_credential rhs)` ||

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-credential#class_firebase_1_1_auth_1_1_phone_auth_credential_1afc6250c2d9c5044e922fdbb8bcea5270` | `string` Gets the auto-retrieved SMS verification code if applicable. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-credential#class_firebase_1_1_auth_1_1_phone_auth_credential_1a961fa3f956ab0b0e78828ac2920e113f(bool disposing)` | `virtual override void` |

## Properties

### SmsCode

```c#
string SmsCode
```
Gets the auto-retrieved SMS verification code if applicable.

This method is supported on Android devices only. It will return empty strings on other platforms.

When SMS verification is used, you will be called back first via [PhoneAuthProvider.CodeSent](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider_1a96f9a8f73784ca4c9ebe01e571ab218f), and later [PhoneAuthProvider.VerificationCompleted](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider_1a64e9a7b72b2cf3f5e6da45b08b8ee66d) with a [PhoneAuthCredential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-credential#class_firebase_1_1_auth_1_1_phone_auth_credential) containing a non-null SMS code if auto-retrieval succeeded. If [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) used another approach to verify the phone number and triggers a callback via [PhoneAuthProvider.VerificationCompleted](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider_1a64e9a7b72b2cf3f5e6da45b08b8ee66d), then the SMS code can be null.

## Public functions

### Dispose

```c#
virtual override void Dispose(
  bool disposing
)
```

### PhoneAuthCredential

```c#
 PhoneAuthCredential()
```

### PhoneAuthCredential

```c#
 PhoneAuthCredential(
  PhoneAuthCredential rhs
)
```