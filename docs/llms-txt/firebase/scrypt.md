# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/scrypt.md.txt

# FirebaseAdmin.Auth.Hash.Scrypt Class Reference

# FirebaseAdmin.Auth.Hash.Scrypt

Represents the [Scrypt](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_scrypt) password hashing algorithm.

## Summary

This is the [modified Scrypt algorithm](https://github.com/firebase/scrypt) used by Firebase [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth). See [StandardScrypt](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/standard-scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_standard_scrypt) for the standard [Scrypt](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_scrypt) algorithm. Can be used as an instance of [UserImportHash](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-hash#class_firebase_admin_1_1_auth_1_1_user_import_hash) when importing users.

### Inheritance

Inherits from: [FirebaseAdmin.Auth.Hash.RepeatableHash](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/repeatable-hash)

| ### Constructors and Destructors ||
|---|---|
| [Scrypt](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_scrypt_1ae81e4a22c9e6ad9f3fd3e62eff59f2de)`()` Initializes a new instance of the [Scrypt](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_scrypt) class. ||

|                                                                                                                                                                                                             ### Properties                                                                                                                                                                                                              ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Key](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_scrypt_1af313d92d4fa014092b7961227ebc77e6)           | `byte[]` Gets or sets the signer key for the hashing algorithm.                                                                                                                                                                    |
| [MaxRounds](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_scrypt_1ab92f2e4cfee521ff5a00fa727ed0f61a)     | `override int` Gets the maximum number of rounds for a [Scrypt](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_scrypt) hash, which is 8. |
| [MemoryCost](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_scrypt_1a4b3fa76c995dd482ee39b0034e6cc961)    | `int` Gets or sets the memory cost for the hashing algorithm.                                                                                                                                                                      |
| [MinRounds](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_scrypt_1a81b5bab66907464da4ad19dd55f385cd)     | `override int` Gets the minimum number of rounds for a [Scrypt](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_scrypt) hash, which is 0. |
| [SaltSeparator](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_scrypt_1ac7c07e508c91ab62f59c2d060943b295) | `byte[]` Gets or sets the salt separator for the hashing algorithm.                                                                                                                                                                |

|                                                                                                                                                 ### Protected functions                                                                                                                                                 ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [GetHashConfiguration](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_scrypt_1a87fc68b6b5ce114d611ad2fec5548b75)`()` | `virtual override IReadOnlyDictionary< string, object >` Returns the options for the hashing algorithm. |

## Properties

### Key

```text
byte[] Key
```  
Gets or sets the signer key for the hashing algorithm.  

### MaxRounds

```text
override int MaxRounds
```  
Gets the maximum number of rounds for a [Scrypt](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_scrypt) hash, which is 8.  

### MemoryCost

```text
int MemoryCost
```  
Gets or sets the memory cost for the hashing algorithm.  

### MinRounds

```text
override int MinRounds
```  
Gets the minimum number of rounds for a [Scrypt](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_scrypt) hash, which is 0.  

### SaltSeparator

```text
byte[] SaltSeparator
```  
Gets or sets the salt separator for the hashing algorithm.

## Public functions

### Scrypt

```text
 Scrypt()
```  
Initializes a new instance of the [Scrypt](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_scrypt) class.

Defines the name of the hash to be equal to SCRYPT.

## Protected functions

### GetHashConfiguration

```text
virtual override IReadOnlyDictionary< string, object > GetHashConfiguration()
```  
Returns the options for the hashing algorithm.

<br />

|                           Details                            ||
|-------------|-------------------------------------------------|
| **Returns** | Dictionary defining options such as signer key. |