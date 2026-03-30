# Source: https://firebase.google.com/docs/reference/admin/dotnet/interface/firebase-admin/auth/i-user-info.md.txt

# FirebaseAdmin.Auth.IUserInfo Interface Reference

# FirebaseAdmin.Auth.IUserInfo

A collection of standard profile information for a user.

## Summary

Used to expose profile information returned by an identity provider.

### Inheritance

Direct Known Subclasses:[FirebaseAdmin.Auth.ProviderUserInfo](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/provider-user-info), [FirebaseAdmin.Auth.UserRecord](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/user-record)

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/admin/dotnet/interface/firebase-admin/auth/i-user-info#interface_firebase_admin_1_1_auth_1_1_i_user_info_1a97e8e12267a4d96e732d3205e14c1906` | `string` Gets the user's display name, if available. |
| `https://firebase.google.com/docs/reference/admin/dotnet/interface/firebase-admin/auth/i-user-info#interface_firebase_admin_1_1_auth_1_1_i_user_info_1a8f76ddcec68131add1a97ffbeed1d7f5` | `string` Gets the user's email address, if available. |
| `https://firebase.google.com/docs/reference/admin/dotnet/interface/firebase-admin/auth/i-user-info#interface_firebase_admin_1_1_auth_1_1_i_user_info_1a715205e1be97af4d7b9e60f9e4fbb682` | `string` Gets the user's phone number, if available. |
| `https://firebase.google.com/docs/reference/admin/dotnet/interface/firebase-admin/auth/i-user-info#interface_firebase_admin_1_1_auth_1_1_i_user_info_1ad4944eaf3957eaf3be0d92f0352c1616` | `string` Gets the user's photo URL, if available. |
| `https://firebase.google.com/docs/reference/admin/dotnet/interface/firebase-admin/auth/i-user-info#interface_firebase_admin_1_1_auth_1_1_i_user_info_1ae7f25b889c4669366ef1fc82ce3ba700` | `string` Gets the ID of the identity provider. |
| `https://firebase.google.com/docs/reference/admin/dotnet/interface/firebase-admin/auth/i-user-info#interface_firebase_admin_1_1_auth_1_1_i_user_info_1ad497b5ae48d3623fd303ec3d130a9846` | `string` Gets the user's unique ID assigned by the identity provider. |

## Properties

### DisplayName

```
string DisplayName
```
Gets the user's display name, if available.

Otherwise null.

### Email

```
string Email
```
Gets the user's email address, if available.

Otherwise null.

### PhoneNumber

```
string PhoneNumber
```
Gets the user's phone number, if available.

Otherwise null.

### PhotoUrl

```
string PhotoUrl
```
Gets the user's photo URL, if available.

Otherwise null.

### ProviderId

```
string ProviderId
```
Gets the ID of the identity provider.

This can be a short domain name (e.g. google.com) or the identifier of an OpenID identity provider.

### Uid

```
string Uid
```
Gets the user's unique ID assigned by the identity provider.