# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/standard-scrypt.md.txt

# FirebaseAdmin.Auth.Hash.StandardScrypt Class Reference

# FirebaseAdmin.Auth.Hash.StandardScrypt

Represents the Standard [Scrypt](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_scrypt) password hashing algorithm.

## Summary

Can be used as an instance of [UserImportHash](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-hash#class_firebase_admin_1_1_auth_1_1_user_import_hash) when importing users.

### Inheritance

Inherits from: [FirebaseAdmin.Auth.UserImportHash](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-hash)

| ### Constructors and Destructors ||
|---|---|
| [StandardScrypt](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/standard-scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_standard_scrypt_1a9de28deebf2822c9d6e2782547481ad5)`()` Initializes a new instance of the [StandardScrypt](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/standard-scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_standard_scrypt) class. ||

|                                                                                                                                         ### Properties                                                                                                                                         ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [BlockSize](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/standard-scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_standard_scrypt_1a5ca5153fe7e5566d8e4af212a0082e04)        | `int` Gets or sets the block size for the hashing algorithm.         |
| [DerivedKeyLength](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/standard-scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_standard_scrypt_1aaf42d3e402d351daef8d816a97a3073b) | `int` Gets or sets the derived key length for the hashing algorithm. |
| [MemoryCost](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/standard-scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_standard_scrypt_1a32d2455fd9c65d291bc992b01c5daa4e)       | `int` Gets or sets memory cost for the hashing algorithm.            |
| [Parallelization](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/standard-scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_standard_scrypt_1a249d039b3a212b5306aa9dd79d38d66e)  | `int` Gets or sets parallelization of the hashing algorithm.         |

|                                                                                                                                                          ### Protected functions                                                                                                                                                          ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [GetHashConfiguration](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/standard-scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_standard_scrypt_1a87fb5fe08a51c29526bf3926b83a1052)`()` | `virtual override IReadOnlyDictionary< string, object >` Returns the options for the hashing algorithm. |

## Properties

### BlockSize

```text
int BlockSize
```  
Gets or sets the block size for the hashing algorithm.

The size cannot be negative.  

### DerivedKeyLength

```text
int DerivedKeyLength
```  
Gets or sets the derived key length for the hashing algorithm.

The length cannot be negative.  

### MemoryCost

```text
int MemoryCost
```  
Gets or sets memory cost for the hashing algorithm.

The memory cost cannot be negative.  

### Parallelization

```text
int Parallelization
```  
Gets or sets parallelization of the hashing algorithm.

The parallelization factor cannot be negative.

## Public functions

### StandardScrypt

```text
 StandardScrypt()
```  
Initializes a new instance of the [StandardScrypt](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/standard-scrypt#class_firebase_admin_1_1_auth_1_1_hash_1_1_standard_scrypt) class.

Defines the name of the hash to be equal to STANDARD_SCRYPT.

## Protected functions

### GetHashConfiguration

```text
virtual override IReadOnlyDictionary< string, object > GetHashConfiguration()
```  
Returns the options for the hashing algorithm.

<br />

|                                                      Details                                                      ||
|-------------|------------------------------------------------------------------------------------------------------|
| **Returns** | Dictionary defining options such as derived key length, block size, parallelization and memory cost. |