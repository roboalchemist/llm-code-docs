# Source: https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-credential.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-credential.md.txt

# firebase::auth::PhoneAuthCredential Class Reference

# firebase::auth::PhoneAuthCredential


`#include <credential.h>`

Wraps phone number and verification information for authentication purposes.

## Summary

### Inheritance

Inherits from: [firebase::auth::Credential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential)

| ### Constructors and Destructors ||
|---|---|
| [PhoneAuthCredential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-credential#classfirebase_1_1auth_1_1_phone_auth_credential_1a016445a98a16e722980150bc2d10d91c)`()` ||
| [PhoneAuthCredential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-credential#classfirebase_1_1auth_1_1_phone_auth_credential_1a3e2ec8c6b54a60697969cdc2f76acbea)`(const `[PhoneAuthCredential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-credential#classfirebase_1_1auth_1_1_phone_auth_credential)` & rhs)` Copy constructor. ||

|                                                                                                                                                                                                                                                                                                                                  ### Public functions                                                                                                                                                                                                                                                                                                                                   ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [operator=](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-credential#classfirebase_1_1auth_1_1_phone_auth_credential_1a9f77f5ec379bb9a13bb64e694a819267)`(const `[PhoneAuthCredential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-credential#classfirebase_1_1auth_1_1_phone_auth_credential)` & rhs)` | [PhoneAuthCredential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-credential#classfirebase_1_1auth_1_1_phone_auth_credential)` &` Copy a [Credential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential). |
| [sms_code](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-credential#classfirebase_1_1auth_1_1_phone_auth_credential_1abf69940355c9398b02f147aec8eefbf8)`() const `                                                                                                                                                                        | `std::string` Gets the automatically retrieved SMS verification code if applicable.                                                                                                                                                                                                                          |

## Public functions

### PhoneAuthCredential

```c++
 PhoneAuthCredential()
```  

### PhoneAuthCredential

```c++
 PhoneAuthCredential(
  const PhoneAuthCredential & rhs
)
```  
Copy constructor.  

### operator=

```c++
PhoneAuthCredential & operator=(
  const PhoneAuthCredential & rhs
)
```  
Copy a [Credential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential).  

### sms_code

```c++
std::string sms_code() const 
```  
Gets the automatically retrieved SMS verification code if applicable.

This method is only supported on Android.