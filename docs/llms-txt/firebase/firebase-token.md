# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token.md.txt

# FirebaseAdmin.Auth.FirebaseToken Class Reference

# FirebaseAdmin.Auth.FirebaseToken

Represents a valid, decoded Firebase ID token.

## Summary

It can be used to get the `Uid` and other claims available in the token.

|                                                                                                                                                                             ### Properties                                                                                                                                                                             ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Audience](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token_1ac5d569ee58c9d8b39c31f6fa04359088)              | `string` Gets the audience claim that identifies the audience that the JWT is intended for.                                                             |
| [Claims](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token_1adee2c4bbda3ee99ae55ccb18be367f3a)                | `IReadOnlyDictionary< string, object >` Gets all other claims present in the JWT as a readonly dictionary.                                              |
| [ExpirationTimeSeconds](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token_1aa61c90772ca9ea3206fa0e92d5c08fc1) | `long` Gets the expiration time claim that identifies the expiration time (in seconds) on or after which the token MUST NOT be accepted for processing. |
| [IssuedAtTimeSeconds](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token_1a9200a5395586efc54d300155b5f4568e)   | `long` Gets the issued at claim that identifies the time (in seconds) at which the JWT was issued.                                                      |
| [Issuer](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token_1adf4ea099ac54cebbcddf18f72483b491)                | `string` Gets the issuer claim that identifies the principal that issued the JWT.                                                                       |
| [Subject](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token_1aa3c512852864eee21e62276176a5350f)               | `string` Gets the subject claim identifying the principal that is the subject of the JWT.                                                               |
| [TenantId](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token_1a3974cc2a8996d9ec9ea26b86e672c3f5)              | `string` Gets the ID of the tenant the user belongs to, if available.                                                                                   |
| [Uid](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token_1ac22a3a61f7c0e5f2e07ea912fc6c169a)                   | `string` Gets the User ID of the user to which this ID token belongs.                                                                                   |

## Properties

### Audience

```text
string Audience
```  
Gets the audience claim that identifies the audience that the JWT is intended for.  

### Claims

```text
IReadOnlyDictionary< string, object > Claims
```  
Gets all other claims present in the JWT as a readonly dictionary.

This can be used to access custom claims of the token.  

### ExpirationTimeSeconds

```text
long ExpirationTimeSeconds
```  
Gets the expiration time claim that identifies the expiration time (in seconds) on or after which the token MUST NOT be accepted for processing.  

### IssuedAtTimeSeconds

```text
long IssuedAtTimeSeconds
```  
Gets the issued at claim that identifies the time (in seconds) at which the JWT was issued.  

### Issuer

```text
string Issuer
```  
Gets the issuer claim that identifies the principal that issued the JWT.  

### Subject

```text
string Subject
```  
Gets the subject claim identifying the principal that is the subject of the JWT.  

### TenantId

```text
string TenantId
```  
Gets the ID of the tenant the user belongs to, if available.

Returns null if the ID token is not scoped to a tenant.  

### Uid

```text
string Uid
```  
Gets the User ID of the user to which this ID token belongs.

This is same as [Subject](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-token#class_firebase_admin_1_1_auth_1_1_firebase_token_1aa3c512852864eee21e62276176a5350f).