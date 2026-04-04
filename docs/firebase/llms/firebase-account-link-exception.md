# Source: https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-account-link-exception.md.txt

# Firebase.Auth.FirebaseAccountLinkException Class Reference

# Firebase.Auth.FirebaseAccountLinkException

Exception thrown for failed Account Link Attempts.

## Summary

Represents a [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Auth](https://firebase.google.com/docs/reference/unity/namespace/firebase/auth#namespace_firebase_1_1_auth) error when attempting to link an account. UserInfo contains additional information about the account as returned by the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Auth](https://firebase.google.com/docs/reference/unity/namespace/firebase/auth#namespace_firebase_1_1_auth) service, and may include a valid UpdatedCredential which can be used to sign in to the service through Firebase.Auth.SignInWithCredential.

### Inheritance

Inherits from: Exception

| ### Constructors and Destructors ||
|---|---|
| [FirebaseAccountLinkException](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-account-link-exception#class_firebase_1_1_auth_1_1_firebase_account_link_exception_1a6f9cc9cea45983a12b16105fe8c1c447)`(int errorCode, string message, `[AuthResult](https://firebase.google.com/docs/reference/unity/class/firebase/auth/auth-result#class_firebase_1_1_auth_1_1_auth_result)` authResult)` Initializes a new [FirebaseAccountLinkException](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-account-link-exception#class_firebase_1_1_auth_1_1_firebase_account_link_exception), with the given error code and message and the [AdditionalUserInfo](https://firebase.google.com/docs/reference/unity/class/firebase/auth/additional-user-info#class_firebase_1_1_auth_1_1_additional_user_info) returned from the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) auth service. ||

|                                                                                                                                                                                                                                               ### Properties                                                                                                                                                                                                                                               ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ErrorCode](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-account-link-exception#class_firebase_1_1_auth_1_1_firebase_account_link_exception_1ae45fa50ec5bc2b5a17122db7b9dbe844) | `int` Returns the [Auth](https://firebase.google.com/docs/reference/unity/namespace/firebase/auth#namespace_firebase_1_1_auth) defined non-zero error code.                                                                                                                              |
| [UserInfo](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-account-link-exception#class_firebase_1_1_auth_1_1_firebase_account_link_exception_1ab710c0bcd094e3c31925955c9d4a8c6e)  | [AdditionalUserInfo](https://firebase.google.com/docs/reference/unity/class/firebase/auth/additional-user-info#class_firebase_1_1_auth_1_1_additional_user_info) Returns a Firebase.Auth.UserInfo object that may include additional information about the account which failed to link. |

## Properties

### ErrorCode

```c#
int ErrorCode
```  
Returns the [Auth](https://firebase.google.com/docs/reference/unity/namespace/firebase/auth#namespace_firebase_1_1_auth) defined non-zero error code.

If the error code is 0, the error is with the Task itself, and not the API. See the exception message for more detail.  

### UserInfo

```c#
AdditionalUserInfo UserInfo
```  
Returns a Firebase.Auth.UserInfo object that may include additional information about the account which failed to link.

Additionally, if UserInfo.UpdatedCredential.IsValid() is true, the credential may be used to sign-in the user into [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) with Firebase.Auth.SignInWithCredentialAsync.

## Public functions

### FirebaseAccountLinkException

```c#
 FirebaseAccountLinkException(
  int errorCode,
  string message,
  AuthResult authResult
)
```  
Initializes a new [FirebaseAccountLinkException](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-account-link-exception#class_firebase_1_1_auth_1_1_firebase_account_link_exception), with the given error code and message and the [AdditionalUserInfo](https://firebase.google.com/docs/reference/unity/class/firebase/auth/additional-user-info#class_firebase_1_1_auth_1_1_additional_user_info) returned from the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) auth service.