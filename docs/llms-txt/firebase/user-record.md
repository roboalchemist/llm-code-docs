# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record.md.txt

# FirebaseAdmin.Auth.UserRecord

Contains metadata associated with a Firebase user account.

## Summary

Instances of this class are immutable and thread safe.

### Inheritance

Inherits from:[FirebaseAdmin.Auth.IUserInfo](https://firebase.google.com/docs/reference/admin/dotnet/interface/firebase-admin/auth/i-user-info)  
Direct Known Subclasses:[FirebaseAdmin.Auth.ExportedUserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/exported-user-record)

|                                                                                                                                                                                                             ### Properties                                                                                                                                                                                                              ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CustomClaims](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record_1ad70121e29831c38ad51d37f061292984)              | `IReadOnlyDictionary< string, object >` Gets the custom claims set on this user, as a non-null dictionary.                                                                                                                 |
| [Disabled](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record_1addd16ecfe2150706b5e3e2a817c29236)                  | `bool` Gets a value indicating whether the user account is disabled or not.                                                                                                                                                |
| [DisplayName](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record_1aa73515b57c739e2310fdc75de2b7bb76)               | `string` Gets the user's display name, if available.                                                                                                                                                                       |
| [Email](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record_1a01393283c59e2239e0e33cb98ed5f655)                     | `string` Gets the user's email address, if available.                                                                                                                                                                      |
| [EmailVerified](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record_1a488689d2bcd278fbdb657b165905f6de)             | `bool` Gets a value indicating whether the user's email address is verified or not.                                                                                                                                        |
| [PhoneNumber](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record_1a7f8710620c2804cc1f992b71ab91f089)               | `string` Gets the user's phone number, if available.                                                                                                                                                                       |
| [PhotoUrl](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record_1aa4126ec184f76a739493635a67b4fdd2)                  | `string` Gets the user's photo URL, if available.                                                                                                                                                                          |
| [ProviderData](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record_1af1a2c4393e1558ef133e35f63dc973cb)              | [IUserInfo](https://firebase.google.com/docs/reference/admin/dotnet/interface/firebase-admin/auth/i-user-info#interface_firebase_admin_1_1_auth_1_1_i_user_info)`[]` Gets a non-null array of provider data for this user. |
| [TenantId](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record_1af08996c402bca0eb49306bf7dcba1b76)                  | `string` Gets the user's tenant ID, if available.                                                                                                                                                                          |
| [TokensValidAfterTimestamp](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record_1a5bfa488082ceeae8e8b7c3305715c1b4) | `DateTime` Gets a timestamp that indicates the earliest point in time at which a valid ID token could have been issued to this user.                                                                                       |
| [Uid](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record_1a06baab9fd2a7fb71eaeb0b17ad0d3f87)                       | `string` Gets the user ID of this user.                                                                                                                                                                                    |
| [UserMetaData](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record_1aec0b8e14c32401b46b1737744a171157)              | [UserMetadata](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-metadata#class_firebase_admin_1_1_auth_1_1_user_metadata) Gets additional user metadata.                             |

|                                                                                                                             ### Public attributes                                                                                                                              ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| [ProviderId](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record#class_firebase_admin_1_1_auth_1_1_user_record_1a84ae333acb8346863f1b7a94fc398835)` => UserRecord.DefaultProviderId` | `string` Gets the ID of the identity provider. |

## Properties

### CustomClaims

```text
IReadOnlyDictionary< string, object > CustomClaims
```  
Gets the custom claims set on this user, as a non-null dictionary.

Possibly empty.  

### Disabled

```text
bool Disabled
```  
Gets a value indicating whether the user account is disabled or not.  

### DisplayName

```text
string DisplayName
```  
Gets the user's display name, if available.

Otherwise null.  

### Email

```text
string Email
```  
Gets the user's email address, if available.

Otherwise null.  

### EmailVerified

```text
bool EmailVerified
```  
Gets a value indicating whether the user's email address is verified or not.  

### PhoneNumber

```text
string PhoneNumber
```  
Gets the user's phone number, if available.

Otherwise null.  

### PhotoUrl

```text
string PhotoUrl
```  
Gets the user's photo URL, if available.

Otherwise null.  

### ProviderData

```text
IUserInfo[] ProviderData
```  
Gets a non-null array of provider data for this user.

Possibly empty.  

### TenantId

```text
string TenantId
```  
Gets the user's tenant ID, if available.

Otherwise null.  

### TokensValidAfterTimestamp

```text
DateTime TokensValidAfterTimestamp
```  
Gets a timestamp that indicates the earliest point in time at which a valid ID token could have been issued to this user.

Tokens issued prior to this timestamp are considered invalid.  

### Uid

```text
string Uid
```  
Gets the user ID of this user.  

### UserMetaData

```text
UserMetadata UserMetaData
```  
Gets additional user metadata.

This is guaranteed not to be null.

## Public attributes

### ProviderId

```text
string ProviderId => UserRecord.DefaultProviderId
```  
Gets the ID of the identity provider.

This returns the constant value`firebase`.