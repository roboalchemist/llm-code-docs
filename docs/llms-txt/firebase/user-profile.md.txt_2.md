# Source: https://firebase.google.com/docs/reference/unity/class/firebase/auth/user-profile.md.txt

# Firebase.Auth.UserProfile Class Reference

# Firebase.Auth.UserProfile

Parameters to the UpdateUserProfile() function.

## Summary

For fields you don't want to update, pass NULL. For fields you want to reset, pass "".

### Inheritance

Inherits from: SystemIDisposable

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/user-profile#class_firebase_1_1_auth_1_1_user_profile_1a4821729751b36f5fa9de4775f79267b3()` ||

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/user-profile#class_firebase_1_1_auth_1_1_user_profile_1a5af825875d09e4e4c9c116fd5ce00d18` | `string` Gets or sets the display name associated with the user. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/user-profile#class_firebase_1_1_auth_1_1_user_profile_1a6a0eb22ba3e47afcb8e83e7f20a13cb6` | `System.Uri` User photo URI. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/user-profile#class_firebase_1_1_auth_1_1_user_profile_1a6656073bfff72775026aea32072125f8()` | `void` |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/user-profile#class_firebase_1_1_auth_1_1_user_profile_1a2d29ccbd40f4c4639f3d3a490d3b540e(bool disposing)` | `void` |

## Properties

### DisplayName

```c#
string DisplayName
```
Gets or sets the display name associated with the user.

### PhotoUrl

```c#
System.Uri PhotoUrl
```
User photo URI.

The photo url associated with the user, if any.

## Public functions

### Dispose

```c#
void Dispose()
```

### Dispose

```c#
void Dispose(
  bool disposing
)
```

### UserProfile

```c#
 UserProfile()
```