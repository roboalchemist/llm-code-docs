# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-hash.md.txt

# FirebaseAdmin.Auth.UserImportHash Class Reference

# FirebaseAdmin.Auth.UserImportHash


**This is an abstract class.**

Represents a hash algorithm and the related configuration parameters used to hash user passwords.

## Summary

An instance of this class must be specified if importing any users with password hashes (see [UserImportOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-options#class_firebase_admin_1_1_auth_1_1_user_import_options)).

This is not expected to be extended in user code. Applications should use one of the provided concrete implementations in the namespace. See [documentation](https://firebase.google.com/docs/auth/admin/import-users) for more details on available options.

### Inheritance

Direct Known Subclasses:[FirebaseAdmin.Auth.Hash.Bcrypt](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/bcrypt), [FirebaseAdmin.Auth.Hash.Hmac](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/hmac), [FirebaseAdmin.Auth.Hash.RepeatableHash](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/repeatable-hash), [FirebaseAdmin.Auth.Hash.StandardScrypt](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/standard-scrypt)

|                                                                                                                                                                                                                  ### Protected functions                                                                                                                                                                                                                   ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GetHashConfiguration](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-hash#class_firebase_admin_1_1_auth_1_1_user_import_hash_1ae2087de32878d8b50e6008e61c8f28d9)`()`          | `virtual abstract IReadOnlyDictionary< string, object >` Retrieves dictionary with the specified properties of the hashing algorithm.                                                                                       |
| [UserImportHash](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-hash#class_firebase_admin_1_1_auth_1_1_user_import_hash_1a8fe15e6669e6a953d9e9aabd97843d4e)`(string hashName)` | ` ` ` `Initializes a new instance of the [UserImportHash](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-hash#class_firebase_admin_1_1_auth_1_1_user_import_hash) class. ` ` |

## Protected functions

### GetHashConfiguration

```text
virtual abstract IReadOnlyDictionary< string, object > GetHashConfiguration()
```  
Retrieves dictionary with the specified properties of the hashing algorithm.

<br />

|                                        Details                                        ||
|-------------|--------------------------------------------------------------------------|
| **Returns** | Dictionary containing the specified properties of the hashing algorithm. |

### UserImportHash

```text
 UserImportHash(
  string hashName
)
```  
Initializes a new instance of the [UserImportHash](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-hash#class_firebase_admin_1_1_auth_1_1_user_import_hash) class.

<br />

|                                                       Details                                                       ||
|------------|---------------------------------------------------------------------------------------------------------|
| Parameters | |------------|------------------------------------| | `hashName` | The name of the hashing algorithm. | |