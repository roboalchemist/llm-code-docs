# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/hmac.md.txt

# FirebaseAdmin.Auth.Hash.Hmac Class Reference

# FirebaseAdmin.Auth.Hash.Hmac

Base class for [Hmac](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/hmac#class_firebase_admin_1_1_auth_1_1_hash_1_1_hmac) type hashes.

## Summary

### Inheritance

Inherits from: [FirebaseAdmin.Auth.UserImportHash](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-import-hash)  
Direct Known Subclasses:[FirebaseAdmin.Auth.Hash.HmacMd5](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/hmac-md5), [FirebaseAdmin.Auth.Hash.HmacSha1](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/hmac-sha1), [FirebaseAdmin.Auth.Hash.HmacSha256](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/hmac-sha256), [FirebaseAdmin.Auth.Hash.HmacSha512](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/hmac-sha512)

|                                                                                                           ### Properties                                                                                                           ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| [Key](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/hmac#class_firebase_admin_1_1_auth_1_1_hash_1_1_hmac_1a1f3c6a10595836d2dbc8630e6991f3e9) | `byte[]` Gets or sets the key for the hash. |

|                                                                                                                                                               ### Protected functions                                                                                                                                                               ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [GetHashConfiguration](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/hash/hmac#class_firebase_admin_1_1_auth_1_1_hash_1_1_hmac_1ae2a0b606f4ef1a851afa61ed25e44670)`()` | `virtual override IReadOnlyDictionary< string, object >` Verifies that the is key non-empty or null and returns the options dictionary. |

## Properties

### Key

```text
byte[] Key
```  
Gets or sets the key for the hash.

## Protected functions

### GetHashConfiguration

```text
virtual override IReadOnlyDictionary< string, object > GetHashConfiguration()
```  
Verifies that the is key non-empty or null and returns the options dictionary.

<br />

|                                   Details                                    ||
|-------------|-----------------------------------------------------------------|
| **Returns** | Returns the dictionary containing an entry for the signing key. |