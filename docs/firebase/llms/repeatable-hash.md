# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/repeatable-hash.md.txt

# FirebaseAdmin.Auth.Hash.RepeatableHash Class Reference

# FirebaseAdmin.Auth.Hash.RepeatableHash

An abstract [UserImportHash](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-hash#class_firebase_admin_1_1_auth_1_1_user_import_hash) implementation for specifying a `Rounds` count in a given range.

## Summary

### Inheritance

Inherits from: [FirebaseAdmin.Auth.UserImportHash](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-hash)  
Direct Known Subclasses:[FirebaseAdmin.Auth.Hash.Md5](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/md5), [FirebaseAdmin.Auth.Hash.Pbkdf2Sha256](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/pbkdf2-sha256), [FirebaseAdmin.Auth.Hash.PbkdfSha1](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/pbkdf-sha1), [FirebaseAdmin.Auth.Hash.Scrypt](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/scrypt), [FirebaseAdmin.Auth.Hash.Sha1](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/sha1), [FirebaseAdmin.Auth.Hash.Sha256](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/sha256), [FirebaseAdmin.Auth.Hash.Sha512](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/sha512)

|                                                                                                                                                     ### Properties                                                                                                                                                      ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [MaxRounds](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/repeatable-hash#class_firebase_admin_1_1_auth_1_1_hash_1_1_repeatable_hash_1a35e78af7ea66f37f800801816401330f) | `abstract int` Gets the maximum number of rounds for that respective repeatable hash implementation. |
| [MinRounds](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/repeatable-hash#class_firebase_admin_1_1_auth_1_1_hash_1_1_repeatable_hash_1a50b59dc4da7b82c5b7d1e035475dff08) | `abstract int` Gets the minimum number of rounds for that respective repeatable hash implementation. |
| [Rounds](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/repeatable-hash#class_firebase_admin_1_1_auth_1_1_hash_1_1_repeatable_hash_1aad3c00c3bb4c0075d82e90968d014346)    | `int` Gets or sets the number of rounds for the repeatable hash.                                     |

|                                                                                                                                                                                    ### Protected functions                                                                                                                                                                                     ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GetHashConfiguration](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/repeatable-hash#class_firebase_admin_1_1_auth_1_1_hash_1_1_repeatable_hash_1a995501f67088761285fee6322974d985)`()` | `virtual override IReadOnlyDictionary< string, object >` Returns a dictionary specifying the number of rounds the hashing algorithm was set to iterate over. |

## Properties

### MaxRounds

```text
abstract int MaxRounds
```  
Gets the maximum number of rounds for that respective repeatable hash implementation.  

### MinRounds

```text
abstract int MinRounds
```  
Gets the minimum number of rounds for that respective repeatable hash implementation.  

### Rounds

```text
int Rounds
```  
Gets or sets the number of rounds for the repeatable hash.

## Protected functions

### GetHashConfiguration

```text
virtual override IReadOnlyDictionary< string, object > GetHashConfiguration()
```  
Returns a dictionary specifying the number of rounds the hashing algorithm was set to iterate over.

<br />

|                         Details                          ||
|-------------|---------------------------------------------|
| **Returns** | Dictionary containing the number of rounds. |