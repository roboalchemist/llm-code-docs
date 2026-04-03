# Source: https://firebase.google.com/docs/reference/admin/dotnet/interface/firebase-admin/auth/i-user-info.md.txt

# Source: https://firebase.google.com/docs/reference/unity/interface/firebase/auth/i-user-info.md.txt

# Firebase.Auth.IUserInfo Interface Reference

# Firebase.Auth.IUserInfo

Interface implemented by each identity provider.

## Summary

### Inheritance

Direct Known Subclasses:[Firebase.Auth.UserInfoInterface](https://firebase.google.com/docs/reference/unity/class/firebase/auth/user-info-interface)

|                                                                                                                      ### Properties                                                                                                                       ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [DisplayName](https://firebase.google.com/docs/reference/unity/interface/firebase/auth/i-user-info#interface_firebase_1_1_auth_1_1_i_user_info_1a99b66c4536e80d36a6c63348fef11397) | `string` Gets the display name associated with the user, if any.      |
| [Email](https://firebase.google.com/docs/reference/unity/interface/firebase/auth/i-user-info#interface_firebase_1_1_auth_1_1_i_user_info_1a7a3a2a0467e2ec3f26dab709e6b6972c)       | `string` Gets email associated with the user, if any.                 |
| [PhotoUrl](https://firebase.google.com/docs/reference/unity/interface/firebase/auth/i-user-info#interface_firebase_1_1_auth_1_1_i_user_info_1adb0b92f360f8421b99df5518481aa67d)    | `System.Uri` Gets the photo url associated with the user, if any.     |
| [ProviderId](https://firebase.google.com/docs/reference/unity/interface/firebase/auth/i-user-info#interface_firebase_1_1_auth_1_1_i_user_info_1a564a1f66b452bf677d2a8d87f05bbf7a)  | `string` Gets the provider ID for the user (For example, "Facebook"). |
| [UserId](https://firebase.google.com/docs/reference/unity/interface/firebase/auth/i-user-info#interface_firebase_1_1_auth_1_1_i_user_info_1a1524d36845f380647b4119da5b918232)      | `string` Gets the unique user ID for the user.                        |

## Properties

### DisplayName

```c#
string DisplayName
```  
Gets the display name associated with the user, if any.  

### Email

```c#
string Email
```  
Gets email associated with the user, if any.  

### PhotoUrl

```c#
System.Uri PhotoUrl
```  
Gets the photo url associated with the user, if any.  

### ProviderId

```c#
string ProviderId
```  
Gets the provider ID for the user (For example, "Facebook").  

### UserId

```c#
string UserId
```  
Gets the unique user ID for the user.


| **Note:** The user's ID, unique to the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) project. Do NOT use this value to authenticate with your backend server, if you have one. Use User.Token() instead.

<br />