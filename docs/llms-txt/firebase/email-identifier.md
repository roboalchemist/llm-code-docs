# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/email-identifier.md.txt

# FirebaseAdmin.Auth.EmailIdentifier Class Reference

# FirebaseAdmin.Auth.EmailIdentifier

Used for looking up an account by email.

## Summary

See AbstractFirebaseAuth.GetUsersAsync(IReadOnlyCollection{UserIdentifier}).

### Inheritance

Inherits from: [FirebaseAdmin.Auth.UserIdentifier](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-identifier)

| ### Constructors and Destructors ||
|---|---|
| [EmailIdentifier](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/email-identifier#class_firebase_admin_1_1_auth_1_1_email_identifier_1a32da5326fb59151bc2006f4ef7b2fa0b)`(string email)` Initializes a new instance of the [EmailIdentifier](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/email-identifier#class_firebase_admin_1_1_auth_1_1_email_identifier) class. ||

|                                                                                                    ### Public functions                                                                                                     ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| [ToString](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/email-identifier#class_firebase_admin_1_1_auth_1_1_email_identifier_1a81512a76b895519449b867c88ae417ba)`()` | `override string` |

## Public functions

### EmailIdentifier

```text
 EmailIdentifier(
  string email
)
```  
Initializes a new instance of the [EmailIdentifier](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/email-identifier#class_firebase_admin_1_1_auth_1_1_email_identifier) class.

<br />

|                            Details                            ||
|------------|---------------------------------------------------|
| Parameters | |---------|------------| | `email` | The email. | |

### ToString

```text
override string ToString()
```