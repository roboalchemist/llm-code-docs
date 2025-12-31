# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/phone-identifier.md.txt

# FirebaseAdmin.Auth.PhoneIdentifier Class Reference

# FirebaseAdmin.Auth.PhoneIdentifier

Used for looking up an account by phone number.

## Summary

See AbstractFirebaseAuth.GetUsersAsync(IReadOnlyCollection{UserIdentifier}).

### Inheritance

Inherits from: [FirebaseAdmin.Auth.UserIdentifier](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-identifier)

| ### Constructors and Destructors ||
|---|---|
| [PhoneIdentifier](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/phone-identifier#class_firebase_admin_1_1_auth_1_1_phone_identifier_1a32b52fd6a07145bd1fb61854feaf1a7c)`(string phoneNumber)` Initializes a new instance of the [PhoneIdentifier](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/phone-identifier#class_firebase_admin_1_1_auth_1_1_phone_identifier) class. ||

|                                                                                                    ### Public functions                                                                                                     ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| [ToString](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/phone-identifier#class_firebase_admin_1_1_auth_1_1_phone_identifier_1a3d11c338e5e995a45ecdaf90e80b761a)`()` | `override string` |

## Public functions

### PhoneIdentifier

```text
 PhoneIdentifier(
  string phoneNumber
)
```  
Initializes a new instance of the [PhoneIdentifier](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/phone-identifier#class_firebase_admin_1_1_auth_1_1_phone_identifier) class.

<br />

|                                        Details                                        ||
|------------|---------------------------------------------------------------------------|
| Parameters | |---------------|------------------| | `phoneNumber` | The phoneNumber. | |

### ToString

```text
override string ToString()
```