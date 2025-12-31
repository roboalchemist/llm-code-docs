# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/exported-user-record.md.txt

# FirebaseAdmin.Auth.ExportedUserRecord Class Reference

# FirebaseAdmin.Auth.ExportedUserRecord

Contains metadata associated with a Firebase user account, along with password hash and salt.

## Summary

Instances of this class are immutable and thread safe.

### Inheritance

Inherits from: [FirebaseAdmin.Auth.UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record)

|                                                                                                                                    ### Properties                                                                                                                                    ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| [PasswordHash](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/exported-user-record#class_firebase_admin_1_1_auth_1_1_exported_user_record_1ac8d9cf5323306530e978f7816658517d) | `string` Gets the user's password hash as a base64-encoded string. |
| [PasswordSalt](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/exported-user-record#class_firebase_admin_1_1_auth_1_1_exported_user_record_1a6439ec7b21fd8312335a3ffe469de0ea) | `string` Gets the user's password salt as a base64-encoded string. |

## Properties

### PasswordHash

```text
string PasswordHash
```  
Gets the user's password hash as a base64-encoded string.

If the Firebase [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth) hashing algorithm (SCRYPT) was used to create the user account, returns the base64-encoded password hash of the user. If a different hashing algorithm was used to create this user, as is typical when migrating from another [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth) system, returns an empty string. Returns null if no password is set.  

### PasswordSalt

```text
string PasswordSalt
```  
Gets the user's password salt as a base64-encoded string.

If the Firebase [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth) hashing algorithm (SCRYPT) was used to create the user account, returns the base64-encoded password salt of the user. If a different hashing algorithm was used to create this user, as is typical when migrating from another [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth) system, returns an empty string. Returns null if no password is set.