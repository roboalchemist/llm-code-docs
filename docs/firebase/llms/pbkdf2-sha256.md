# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/pbkdf2-sha256.md.txt

# FirebaseAdmin.Auth.Hash.Pbkdf2Sha256 Class Reference

# FirebaseAdmin.Auth.Hash.Pbkdf2Sha256

Represents the PBKDF2 SHA256 password hashing algorithm.

## Summary

Can be used as an instance of [UserImportHash](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-hash#class_firebase_admin_1_1_auth_1_1_user_import_hash) when importing users.

### Inheritance

Inherits from: [FirebaseAdmin.Auth.Hash.RepeatableHash](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/repeatable-hash)

| ### Constructors and Destructors ||
|---|---|
| [Pbkdf2Sha256](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/pbkdf2-sha256#class_firebase_admin_1_1_auth_1_1_hash_1_1_pbkdf2_sha256_1ad3d1bbab40bcf978ff01262a765573f8)`()` Initializes a new instance of the [Pbkdf2Sha256](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/pbkdf2-sha256#class_firebase_admin_1_1_auth_1_1_hash_1_1_pbkdf2_sha256) class. ||

|                                                                                                                                                                                                                        ### Properties                                                                                                                                                                                                                         ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MaxRounds](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/pbkdf2-sha256#class_firebase_admin_1_1_auth_1_1_hash_1_1_pbkdf2_sha256_1a8ff50a616b4b1143b10526e8d99e2d0b) | `override int` Gets the maximum number of rounds for a Pbkdf2 [Sha256](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/sha256#class_firebase_admin_1_1_auth_1_1_hash_1_1_sha256) hash, which is 120000. |
| [MinRounds](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/pbkdf2-sha256#class_firebase_admin_1_1_auth_1_1_hash_1_1_pbkdf2_sha256_1aea2fde70768353ac3d177eea24be7fee) | `override int` Gets the minimum number of rounds for a Pbkdf2 [Sha256](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/sha256#class_firebase_admin_1_1_auth_1_1_hash_1_1_sha256) hash, which is 0.      |

## Properties

### MaxRounds

```text
override int MaxRounds
```  
Gets the maximum number of rounds for a Pbkdf2 [Sha256](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/sha256#class_firebase_admin_1_1_auth_1_1_hash_1_1_sha256) hash, which is 120000.  

### MinRounds

```text
override int MinRounds
```  
Gets the minimum number of rounds for a Pbkdf2 [Sha256](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/sha256#class_firebase_admin_1_1_auth_1_1_hash_1_1_sha256) hash, which is 0.

## Public functions

### Pbkdf2Sha256

```text
 Pbkdf2Sha256()
```  
Initializes a new instance of the [Pbkdf2Sha256](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/pbkdf2-sha256#class_firebase_admin_1_1_auth_1_1_hash_1_1_pbkdf2_sha256) class.

Defines the name of the hash to be equal to PBKDF2_SHA256.