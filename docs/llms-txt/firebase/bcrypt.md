# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/bcrypt.md.txt

# FirebaseAdmin.Auth.Hash.Bcrypt Class Reference

# FirebaseAdmin.Auth.Hash.Bcrypt

Represents the [Bcrypt](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/bcrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_bcrypt) password hashing algorithm.

## Summary

Can be used as an instance of [UserImportHash](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-hash#class_firebase_admin_1_1_auth_1_1_user_import_hash) when importing users.

### Inheritance

Inherits from: [FirebaseAdmin.Auth.UserImportHash](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-hash)

| ### Constructors and Destructors ||
|---|---|
| [Bcrypt](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/bcrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_bcrypt_1a66adf0762eb32a1e684f37ae3ed9f11f)`()` Initializes a new instance of the [Bcrypt](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/bcrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_bcrypt) class. ||

|                                                                                                                                                                                                                                              ### Protected functions                                                                                                                                                                                                                                              ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GetHashConfiguration](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/bcrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_bcrypt_1a1150a7f2e37d2742564ef90a68038a76)`()` | `virtual override IReadOnlyDictionary< string, object >` Returns an empty dictionary representing no options for the [Bcrypt](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/bcrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_bcrypt) hashing algorithm. |

## Public functions

### Bcrypt

```text
 Bcrypt()
```  
Initializes a new instance of the [Bcrypt](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/bcrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_bcrypt) class.

Defines name to be equal to BCRYPT.

## Protected functions

### GetHashConfiguration

```text
virtual override IReadOnlyDictionary< string, object > GetHashConfiguration()
```  
Returns an empty dictionary representing no options for the [Bcrypt](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/bcrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_bcrypt) hashing algorithm.

<br />

|                   Details                    ||
|-------------|---------------------------------|
| **Returns** | Dictionary defining no options. |