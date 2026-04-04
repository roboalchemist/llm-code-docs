# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/pbkdf-sha1.md.txt

# FirebaseAdmin.Auth.Hash.PbkdfSha1 Class Reference

# FirebaseAdmin.Auth.Hash.PbkdfSha1

Represents the PBKDF SHA1 password hashing algorithm.

## Summary

Can be used as an instance of [UserImportHash](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-hash#class_firebase_admin_1_1_auth_1_1_user_import_hash) when importing users.

### Inheritance

Inherits from: [FirebaseAdmin.Auth.Hash.RepeatableHash](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/repeatable-hash)

| ### Constructors and Destructors ||
|---|---|
| [PbkdfSha1](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/pbkdf-sha1#class_firebase_admin_1_1_auth_1_1_hash_1_1_pbkdf_sha1_1a8c7f3fc250879ff70147462d11a43652)`()` Initializes a new instance of the [PbkdfSha1](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/pbkdf-sha1#class_firebase_admin_1_1_auth_1_1_hash_1_1_pbkdf_sha1) class. ||

|                                                                                                                                                                                                                  ### Properties                                                                                                                                                                                                                  ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MaxRounds](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/pbkdf-sha1#class_firebase_admin_1_1_auth_1_1_hash_1_1_pbkdf_sha1_1a31ae3fbee61eaa4283acd00b6b0cef90) | `override int` Gets the maximum number of rounds for a Pbkdf [Sha1](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/sha1#class_firebase_admin_1_1_auth_1_1_hash_1_1_sha1) hash, which is 120000. |
| [MinRounds](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/pbkdf-sha1#class_firebase_admin_1_1_auth_1_1_hash_1_1_pbkdf_sha1_1a21dc92e5fbba2b0e95da4748645bd088) | `override int` Gets the minimum number of rounds for a Pbkdf [Sha1](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/sha1#class_firebase_admin_1_1_auth_1_1_hash_1_1_sha1) hash, which is 0.      |

## Properties

### MaxRounds

```text
override int MaxRounds
```  
Gets the maximum number of rounds for a Pbkdf [Sha1](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/sha1#class_firebase_admin_1_1_auth_1_1_hash_1_1_sha1) hash, which is 120000.  

### MinRounds

```text
override int MinRounds
```  
Gets the minimum number of rounds for a Pbkdf [Sha1](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/sha1#class_firebase_admin_1_1_auth_1_1_hash_1_1_sha1) hash, which is 0.

## Public functions

### PbkdfSha1

```text
 PbkdfSha1()
```  
Initializes a new instance of the [PbkdfSha1](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/pbkdf-sha1#class_firebase_admin_1_1_auth_1_1_hash_1_1_pbkdf_sha1) class.

Defines the name of the hash to be equal to PBKDF_SHA1.