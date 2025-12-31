# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/sha1.md.txt

# FirebaseAdmin.Auth.Hash.Sha1 Class Reference

# FirebaseAdmin.Auth.Hash.Sha1

Represents the SHA1 password hashing algorithm.

## Summary

Can be used as an instance of [UserImportHash](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-hash#class_firebase_admin_1_1_auth_1_1_user_import_hash) when importing users.

### Inheritance

Inherits from: [FirebaseAdmin.Auth.Hash.RepeatableHash](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/repeatable-hash)

| ### Constructors and Destructors ||
|---|---|
| [Sha1](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/sha1#class_firebase_admin_1_1_auth_1_1_hash_1_1_sha1_1a4b931f7013fee3df12f8414ad844c93a)`()` Initializes a new instance of the [Sha1](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/sha1#class_firebase_admin_1_1_auth_1_1_hash_1_1_sha1) class. ||

|                                                                                                                                ### Properties                                                                                                                                 ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [MaxRounds](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/sha1#class_firebase_admin_1_1_auth_1_1_hash_1_1_sha1_1a606502bfc8c6f7422fbe8288cf43991e) | `override int` Gets the maximum number of rounds for a SHA1 hash, which is 8192. |
| [MinRounds](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/sha1#class_firebase_admin_1_1_auth_1_1_hash_1_1_sha1_1a66bdf9abe0dcbc9e1552c573bfbccece) | `override int` Gets the minimum number of rounds for a SHA1 hash, which is 1.    |

## Properties

### MaxRounds

```text
override int MaxRounds
```  
Gets the maximum number of rounds for a SHA1 hash, which is 8192.  

### MinRounds

```text
override int MinRounds
```  
Gets the minimum number of rounds for a SHA1 hash, which is 1.

## Public functions

### Sha1

```text
 Sha1()
```  
Initializes a new instance of the [Sha1](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/sha1#class_firebase_admin_1_1_auth_1_1_hash_1_1_sha1) class.

Defines the name of the hash to be equal to SHA1.