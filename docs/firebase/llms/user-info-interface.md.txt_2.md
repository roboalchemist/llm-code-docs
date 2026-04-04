# Source: https://firebase.google.com/docs/reference/unity/class/firebase/auth/user-info-interface.md.txt

# Firebase.Auth.UserInfoInterface Class Reference

# Firebase.Auth.UserInfoInterface

Interface implemented by each identity provider.

## Summary

### Inheritance

Inherits from: [Firebase.Auth.IUserInfo](https://firebase.google.com/docs/reference/unity/interface/firebase/auth/i-user-info), SystemIDisposable  
Direct Known Subclasses:[Firebase.Auth.FirebaseUser](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user)

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/user-info-interface#class_firebase_1_1_auth_1_1_user_info_interface_1a410fbe565aec9e7070535d98576a41a3()` ||

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/user-info-interface#class_firebase_1_1_auth_1_1_user_info_interface_1ac850cb4d87feed0c70310e6ee6e35947` | `string` |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/user-info-interface#class_firebase_1_1_auth_1_1_user_info_interface_1af9fc098c1d3a53efb1b3b424682c423e` | `string` |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/user-info-interface#class_firebase_1_1_auth_1_1_user_info_interface_1af1b40c980ba1d6587c7e91c8aee00611` | `string` Gets the phone number for the user, in E.164 format. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/user-info-interface#class_firebase_1_1_auth_1_1_user_info_interface_1a11229d539451589608a6deef161eec09` | `System.Uri` Gets the photo url associated with the user, if any. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/user-info-interface#class_firebase_1_1_auth_1_1_user_info_interface_1a52a6c7eada192cb13c4f7b5a353da1cd` | `string` |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/user-info-interface#class_firebase_1_1_auth_1_1_user_info_interface_1ad8adecf60dee17ab3940f305b7527582` | `string` |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/user-info-interface#class_firebase_1_1_auth_1_1_user_info_interface_1a3d9c774fb268dd67ac46ac52c2b1a918()` | `void` |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/user-info-interface#class_firebase_1_1_auth_1_1_user_info_interface_1a3e5b38f9817679136c7bc8ddd0bbfe6a(bool disposing)` | `virtual void` |

## Properties

### DisplayName

```c#
string DisplayName
```

### Email

```c#
string Email
```

### PhoneNumber

```c#
string PhoneNumber
```
Gets the phone number for the user, in E.164 format.

### PhotoUrl

```c#
System.Uri PhotoUrl
```
Gets the photo url associated with the user, if any.

### ProviderId

```c#
string ProviderId
```

### UserId

```c#
string UserId
```

## Public functions

### Dispose

```c#
void Dispose()
```

### Dispose

```c#
virtual void Dispose(
  bool disposing
)
```

### UserInfoInterface

```c#
 UserInfoInterface()
```