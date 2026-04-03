# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/md5.md.txt

# FirebaseAdmin.Auth.Hash.Md5 Class Reference

# FirebaseAdmin.Auth.Hash.Md5

Represents the MD5 password hashing algorithm.

## Summary

Can be used as an instance of [UserImportHash](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-hash#class_firebase_admin_1_1_auth_1_1_user_import_hash) when importing users.

### Inheritance

Inherits from: [FirebaseAdmin.Auth.Hash.RepeatableHash](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/repeatable-hash)

| ### Constructors and Destructors ||
|---|---|
| [Md5](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/md5#class_firebase_admin_1_1_auth_1_1_hash_1_1_md5_1a0a240710c32a656bccbccea8d8a84761)`()` Initializes a new instance of the [Md5](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/md5#class_firebase_admin_1_1_auth_1_1_hash_1_1_md5) class. ||

|                                                                                                                               ### Properties                                                                                                                                ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [MaxRounds](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/md5#class_firebase_admin_1_1_auth_1_1_hash_1_1_md5_1a21aa7636b3988628fa3d7f951ef41dea) | `override int` Gets the maximum number of rounds for an MD5 hash, which is 8192. |
| [MinRounds](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/md5#class_firebase_admin_1_1_auth_1_1_hash_1_1_md5_1afa5de63dffef7ba186e62c75f4939a6a) | `override int` Gets the minimum number of rounds for an MD5 hash, which is 0.    |

## Properties

### MaxRounds

```text
override int MaxRounds
```  
Gets the maximum number of rounds for an MD5 hash, which is 8192.  

### MinRounds

```text
override int MinRounds
```  
Gets the minimum number of rounds for an MD5 hash, which is 0.

## Public functions

### Md5

```text
 Md5()
```  
Initializes a new instance of the [Md5](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/md5#class_firebase_admin_1_1_auth_1_1_hash_1_1_md5) class.

Defines the name of the hash to be equal to MD5.