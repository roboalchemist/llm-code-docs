# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential.md.txt

# firebase::auth::Credential Class Reference

# firebase::auth::Credential


`#include <credential.h>`

Authentication credentials for an authentication provider.

## Summary

An authentication provider is a service that allows you to authenticate a user. Firebase provides email/password authentication, but there are also external authentication providers such as Facebook.

### Inheritance

Direct Known Subclasses:[firebase::auth::PhoneAuthCredential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-credential)

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential_1a92a6a552e35c83a72896b5373d5f3066()` ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential_1a223c90e467c2188935903e3d13e02a4f(const https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential & rhs)` Copy constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential_1a80200c59cf0ff15180eb7d699f6f13c1()` ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential_1a099cda6f9904b6c3d758b55565f2b770() const ` | `bool` Get whether this credential is valid. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential_1a75e6d30bf8ddbfe2fbdb6a0e69b22399(const https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential & rhs)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential &` Copy a [Credential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential_1a1c9a7968c43f57d829c8360306068433() const ` | `std::string` Gets the name of the Identification Provider (IDP) for the credential. |

## Public functions

### Credential

```c++
 Credential()
```

### Credential

```c++
 Credential(
  const Credential & rhs
)
```
Copy constructor.

### is_valid

```c++
bool is_valid() const 
```
Get whether this credential is valid.

A credential can be invalid in an error condition, e.g. empty username/password.

<br />

| Details ||
|---|---|
| **Returns** | True if the credential is valid, false otherwise. |

### operator=

```c++
Credential & operator=(
  const Credential & rhs
)
```
Copy a [Credential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential).

### provider

```c++
std::string provider() const 
```
Gets the name of the Identification Provider (IDP) for the credential.

### \~Credential

```c++
 ~Credential()
```