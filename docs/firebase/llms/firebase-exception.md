# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firebase-exception.md.txt

# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-exception.md.txt

# FirebaseAdmin.FirebaseException Class Reference

# FirebaseAdmin.FirebaseException

Common error type for all exceptions raised by Firebase APIs.

## Summary

### Inheritance

Inherits from: Exception  
Direct Known Subclasses:[FirebaseAdmin.Auth.FirebaseAuthException](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/firebase-auth-exception), [FirebaseAdmin.Messaging.FirebaseMessagingException](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/messaging/firebase-messaging-exception)

|                                                                                                                                                                                                       ### Properties                                                                                                                                                                                                        ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ErrorCode](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-exception#class_firebase_admin_1_1_firebase_exception_1a441ac0cb487c6ab8a5e8c61ab147777a)    | [ErrorCode](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin#namespace_firebase_admin_1a949005b83e5a3d5fbfe31fec6ab5d806) Gets the platform-wide error code associated with this exception. |
| [HttpResponse](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-exception#class_firebase_admin_1_1_firebase_exception_1a498930ac32a46c7d6a1b23d3d3bc2403) | `HttpResponseMessage` Gets the HTTP response that resulted in this exception.                                                                                                                                               |

## Properties

### ErrorCode

```text
ErrorCode ErrorCode
```  
Gets the platform-wide error code associated with this exception.  

### HttpResponse

```text
HttpResponseMessage HttpResponse
```  
Gets the HTTP response that resulted in this exception.

Null, if the exception was not caused by an HTTP error response.