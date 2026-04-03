# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/additional-user-info.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/auth/additional-user-info.md.txt

# Firebase.Auth.AdditionalUserInfo Class Reference

# Firebase.Auth.AdditionalUserInfo

Additional user data returned from an identity provider.

## Summary

### Inheritance

Inherits from: SystemIDisposable

|                                                                                                                                                              ### Properties                                                                                                                                                              ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [Profile](https://firebase.google.com/docs/reference/unity/class/firebase/auth/additional-user-info#class_firebase_1_1_auth_1_1_additional_user_info_1a9a49ab391199bbec5a0ff5aff32fdb0a)           | `global::System.Collections.Generic.IDictionary< string, object >` Additional identity-provider specific information.                |
| [ProviderId](https://firebase.google.com/docs/reference/unity/class/firebase/auth/additional-user-info#class_firebase_1_1_auth_1_1_additional_user_info_1af9a2ed4cdceb8423f222078f7edef6a7)        | `string` The provider identifier.                                                                                                    |
| [UpdatedCredential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/additional-user-info#class_firebase_1_1_auth_1_1_additional_user_info_1a1fee636533729827a97786a04ce2def6) | [Credential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/credential#class_firebase_1_1_auth_1_1_credential) |
| [UserName](https://firebase.google.com/docs/reference/unity/class/firebase/auth/additional-user-info#class_firebase_1_1_auth_1_1_additional_user_info_1aacdc97113298201edd0cf50793228afe)          | `string` The name of the user.                                                                                                       |

|                                                                                                ### Public functions                                                                                                ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| [Dispose](https://firebase.google.com/docs/reference/unity/class/firebase/auth/additional-user-info#class_firebase_1_1_auth_1_1_additional_user_info_1a7c70682680e6146590ce1ac317955fd5)`()`               | `void` |
| [Dispose](https://firebase.google.com/docs/reference/unity/class/firebase/auth/additional-user-info#class_firebase_1_1_auth_1_1_additional_user_info_1a213920f55fea67abe082d636e7b4241e)`(bool disposing)` | `void` |

## Properties

### Profile

```c#
global::System.Collections.Generic.IDictionary< string, object > Profile
```  
Additional identity-provider specific information.

Most likely a hierarchical key-value mapping, like a parsed JSON file.  

### ProviderId

```c#
string ProviderId
```  
The provider identifier.  

### UpdatedCredential

```c#
Credential UpdatedCredential
```  

### UserName

```c#
string UserName
```  
The name of the user.

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