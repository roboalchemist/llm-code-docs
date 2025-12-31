# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-provider.md.txt

# FirebaseAdmin.Auth.UserProvider Class Reference

# FirebaseAdmin.Auth.UserProvider

Represents a user identity provider that can be associated with a Firebase user.

## Summary

|                                                                                                                                  ### Properties                                                                                                                                  ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [DisplayName](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-provider#class_firebase_admin_1_1_auth_1_1_user_provider_1a5f9e2906e5ed743b8b20188b6f78a76d) | `string` Gets or sets the user's display name.                                |
| [Email](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-provider#class_firebase_admin_1_1_auth_1_1_user_provider_1ac9a9895f2614a67d9a47e46697fb18c7)       | `string` Gets or sets the user's email address.                               |
| [PhotoUrl](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-provider#class_firebase_admin_1_1_auth_1_1_user_provider_1a18ae0d0b23257d3d4705c6ba8cfffde4)    | `string` Gets or sets the photo URL of the user.                              |
| [ProviderId](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-provider#class_firebase_admin_1_1_auth_1_1_user_provider_1add2a93cda8724b2c1b0b6e72f9ee4bc5)  | `string` Gets or sets the ID of the identity provider.                        |
| [Uid](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-provider#class_firebase_admin_1_1_auth_1_1_user_provider_1a06f91cdd890682ce6b2ff470d87d90a2)         | `string` Gets or sets the user's unique ID assigned by the identity provider. |

## Properties

### DisplayName

```text
string DisplayName
```  
Gets or sets the user's display name.  

### Email

```text
string Email
```  
Gets or sets the user's email address.  

### PhotoUrl

```text
string PhotoUrl
```  
Gets or sets the photo URL of the user.  

### ProviderId

```text
string ProviderId
```  
Gets or sets the ID of the identity provider.

This can be a short domain name (e.g. google.com) or the identifier of an OpenID identity provider. This field is required.  

### Uid

```text
string Uid
```  
Gets or sets the user's unique ID assigned by the identity provider.

This field is required.