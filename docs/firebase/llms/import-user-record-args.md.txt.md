# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/import-user-record-args.md.txt

# FirebaseAdmin.Auth.ImportUserRecordArgs Class Reference

# FirebaseAdmin.Auth.ImportUserRecordArgs

Represents a user account to be imported to Firebase [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth) via the AbstractFirebaseAuth.ImportUsersAsync(IEnumerable{ImportUserRecordArgs}) API.

## Summary

Must contain at least a user ID string.

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/import-user-record-args#class_firebase_admin_1_1_auth_1_1_import_user_record_args_1ac381737c404c8bcf44b3c2498b83fc2a` | `IReadOnlyDictionary< string, object >` Gets or sets the custom claims. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/import-user-record-args#class_firebase_admin_1_1_auth_1_1_import_user_record_args_1a97999afdbf8f24334a037413359f0320` | `bool` Gets or sets the disabled value, null signifies that it was not specified. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/import-user-record-args#class_firebase_admin_1_1_auth_1_1_import_user_record_args_1a2b0f5ec44387afcb97bc6d1651c42223` | `string` Gets or sets the display name of the user. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/import-user-record-args#class_firebase_admin_1_1_auth_1_1_import_user_record_args_1a7f5a86683b65eb679dd6ad36e0d9575b` | `string` Gets or sets the email address of the user. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/import-user-record-args#class_firebase_admin_1_1_auth_1_1_import_user_record_args_1acc2a6dd5e8c52f88e65027891b342807` | `bool` Gets or sets if the email was verified, null signifies that it was not specified. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/import-user-record-args#class_firebase_admin_1_1_auth_1_1_import_user_record_args_1ad464c6108bab6baf3b16a352d8d7def1` | `byte[]` Gets or sets the password hash. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/import-user-record-args#class_firebase_admin_1_1_auth_1_1_import_user_record_args_1ac8bc0a68016fcd2ac85eefa12e325cab` | `byte[]` Gets or sets the password salt. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/import-user-record-args#class_firebase_admin_1_1_auth_1_1_import_user_record_args_1a41883c3ac0e6f153990dadf70ffdcfcc` | `string` Gets or sets phone number of the user. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/import-user-record-args#class_firebase_admin_1_1_auth_1_1_import_user_record_args_1a7cd4bf621c8619a909a6a1fa277eda5d` | `string` Gets or sets the photo URL. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/import-user-record-args#class_firebase_admin_1_1_auth_1_1_import_user_record_args_1ab96d9d14f0b2442ee775cc14f8029706` | `string` Gets or sets the user ID of the user. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/import-user-record-args#class_firebase_admin_1_1_auth_1_1_import_user_record_args_1a0a9dc812f49e6e1f4a1f99cdca4e08a5` | `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-metadata#class_firebase_admin_1_1_auth_1_1_user_metadata` Gets or sets the user metadata. |
| `https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/import-user-record-args#class_firebase_admin_1_1_auth_1_1_import_user_record_args_1a19eb4747b8acfa98af9df9cae4809150` | `IEnumerable< https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-provider#class_firebase_admin_1_1_auth_1_1_user_provider >` Gets or sets the user providers. |

## Properties

### CustomClaims

```
IReadOnlyDictionary< string, object > CustomClaims
```
Gets or sets the custom claims.

### Disabled

```
bool Disabled
```
Gets or sets the disabled value, null signifies that it was not specified.

### DisplayName

```
string DisplayName
```
Gets or sets the display name of the user.

### Email

```
string Email
```
Gets or sets the email address of the user.

### EmailVerified

```
bool EmailVerified
```
Gets or sets if the email was verified, null signifies that it was not specified.

### PasswordHash

```
byte[] PasswordHash
```
Gets or sets the password hash.

### PasswordSalt

```
byte[] PasswordSalt
```
Gets or sets the password salt.

### PhoneNumber

```
string PhoneNumber
```
Gets or sets phone number of the user.

### PhotoUrl

```
string PhotoUrl
```
Gets or sets the photo URL.

### Uid

```
string Uid
```
Gets or sets the user ID of the user.

### UserMetadata

```
UserMetadata UserMetadata
```
Gets or sets the user metadata.

### UserProviders

```
IEnumerable< UserProvider > UserProviders
```
Gets or sets the user providers.