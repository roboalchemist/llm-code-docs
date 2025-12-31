# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider.md.txt

# Firebase.Auth.PhoneAuthProvider Class Reference

# Firebase.Auth.PhoneAuthProvider

Use phone number text messages to authenticate.

## Summary

Allows developers to use the phone number and SMS verification codes to authenticate a user.

This class is not supported on tvOS and Desktop platforms.

The verification flow results in a [PhoneAuthCredential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-credential#class_firebase_1_1_auth_1_1_phone_auth_credential) that can be used to,

- Sign in to an existing phone number account/sign up with a new phone number
- Link a phone number to a current user. This provider will be added to the user.
- Update a phone number on an existing user.
- Re-authenticate an existing user. This may be needed when a sensitive operation requires the user to be recently logged in.

<br />

Possible verification flows: (1) User manually enters verification code.

- App calls [VerifyPhoneNumber](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider_1a9428bdf467d2213b96e3b7f279dc8562).
- Web verification page is displayed to user where they may need to solve a CAPTCHA. \[iOS only\].
- [Auth](https://firebase.google.com/docs/reference/unity/namespace/firebase/auth#namespace_firebase_1_1_auth) server sends the verification code via SMS to the provided phone number. App receives verification id via [CodeSent](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider_1a96f9a8f73784ca4c9ebe01e571ab218f).
- User receives SMS and enters verification code in app's GUI.
- App uses user's verification code to call [PhoneAuthProvider.GetCredential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider_1ad450508b8b6fef8fdb532be6ebce9b20).

<br />

(2) SMS is automatically retrieved (Android only).

- App calls [VerifyPhoneNumber](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider_1a9428bdf467d2213b96e3b7f279dc8562) with `autoVerifyTimeOutMs` \> 0.
- [Auth](https://firebase.google.com/docs/reference/unity/namespace/firebase/auth#namespace_firebase_1_1_auth) server sends the verification code via SMS to the provided phone number.
- SMS arrives and is automatically retrieved by the operating system. [PhoneAuthCredential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-credential#class_firebase_1_1_auth_1_1_phone_auth_credential) is automatically created and passed to the app via [VerificationCompleted](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider_1a64e9a7b72b2cf3f5e6da45b08b8ee66d).

<br />

(3) Phone number is instantly verified (Android only).

- App calls [VerifyPhoneNumber](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider_1a9428bdf467d2213b96e3b7f279dc8562).
- The operating system validates the phone number without having to send an SMS. [PhoneAuthCredential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-credential#class_firebase_1_1_auth_1_1_phone_auth_credential) is automatically created and passed to the app via [VerificationCompleted](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider_1a64e9a7b72b2cf3f5e6da45b08b8ee66d).

<br />

### Inheritance

Inherits from: SystemIDisposable

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CodeAutoRetrievalTimeOut](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider_1a38054ec4c44ed8916095ccbf64153d77)`(string verificationId)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `delegate void` Callback used when a timeout occurs.                                                                                                                                                                  |
| [CodeSent](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider_1a96f9a8f73784ca4c9ebe01e571ab218f)`(string verificationId, `[ForceResendingToken](https://firebase.google.com/docs/reference/unity/class/firebase/auth/force-resending-token#class_firebase_1_1_auth_1_1_force_resending_token)` forceResendingToken)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `delegate void` Callback used when a verification code is sent to the given number.                                                                                                                                   |
| [Dispose](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider_1a36eb4fc5e75f8d11241821b42e65c6dc)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `void`                                                                                                                                                                                                                |
| [GetCredential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider_1ad450508b8b6fef8fdb532be6ebce9b20)`(string verificationId, string verificationCode)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [PhoneAuthCredential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-credential#class_firebase_1_1_auth_1_1_phone_auth_credential) Generate a credential for the given phone number. |
| [VerificationCompleted](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider_1a64e9a7b72b2cf3f5e6da45b08b8ee66d)`(`[PhoneAuthCredential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-credential#class_firebase_1_1_auth_1_1_phone_auth_credential)` credential)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `delegate void` Callback used when phone number auto-verification succeeded.                                                                                                                                          |
| [VerificationFailed](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider_1ace5f16ad0441eb20e12a24a7b53e314b)`(string error)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `delegate void` Callback used when phone number verification fails.                                                                                                                                                   |
| [VerifyPhoneNumber](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider_1a9428bdf467d2213b96e3b7f279dc8562)`(`[PhoneAuthOptions](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-options#class_firebase_1_1_auth_1_1_phone_auth_options)` options, `[VerificationCompleted](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider_1a64e9a7b72b2cf3f5e6da45b08b8ee66d)` verificationCompleted, `[VerificationFailed](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider_1ace5f16ad0441eb20e12a24a7b53e314b)` verificationFailed, `[CodeSent](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider_1a96f9a8f73784ca4c9ebe01e571ab218f)` codeSent, `[CodeAutoRetrievalTimeOut](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider_1a38054ec4c44ed8916095ccbf64153d77)` codeAutoRetrievalTimeOut)` | `void` Start the phone number authentication operation.                                                                                                                                                               |

|                                                                                                                                                                                                                                                                                                                                             ### Public static functions                                                                                                                                                                                                                                                                                                                                             ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GetInstance](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider_1abe93cf449ba3c813e37e83bf2e36a565)`(`[FirebaseAuth](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-auth#class_firebase_1_1_auth_1_1_firebase_auth)` auth)` | [PhoneAuthProvider](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider) Return the [PhoneAuthProvider](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider) for the specified `auth`. |

## Public functions

### CodeAutoRetrievalTimeOut

```c#
delegate void CodeAutoRetrievalTimeOut(
  string verificationId
)
```  
Callback used when a timeout occurs.  

### CodeSent

```c#
delegate void CodeSent(
  string verificationId,
  ForceResendingToken forceResendingToken
)
```  
Callback used when a verification code is sent to the given number.  

### Dispose

```c#
void Dispose()
```  

### GetCredential

```c#
PhoneAuthCredential GetCredential(
  string verificationId,
  string verificationCode
)
```  
Generate a credential for the given phone number.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `verification_id`   | The id returned when sending the verification code. Sent to the caller via Listener::OnCodeSent.                                                                                                                                                                                                                                       | | `verification_code` | The verification code supplied by the user, most likely by a GUI where the user manually enters the code received in the SMS sent by [VerifyPhoneNumber](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider_1a9428bdf467d2213b96e3b7f279dc8562). | |
| **Returns** | New [PhoneAuthCredential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-credential#class_firebase_1_1_auth_1_1_phone_auth_credential).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

### VerificationCompleted

```c#
delegate void VerificationCompleted(
  PhoneAuthCredential credential
)
```  
Callback used when phone number auto-verification succeeded.  

### VerificationFailed

```c#
delegate void VerificationFailed(
  string error
)
```  
Callback used when phone number verification fails.  

### VerifyPhoneNumber

```c#
void VerifyPhoneNumber(
  PhoneAuthOptions options,
  VerificationCompleted verificationCompleted,
  VerificationFailed verificationFailed,
  CodeSent codeSent,
  CodeAutoRetrievalTimeOut codeAutoRetrievalTimeOut
)
```  
Start the phone number authentication operation.


| **Note:** On iOS the verificationCompleted callback is never invoked and the codeAutoRetrievalTimeOut callback is invoked immediately since auto-validation is not supported on that platform.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `options`                  | The [PhoneAuthOptions](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-options#class_firebase_1_1_auth_1_1_phone_auth_options) struct with a verification configuration.                   | | `verificationCompleted`    | Phone number auto-verification succeeded. Called when auto-sms-retrieval or instant validation succeeds. Provided with the completed credential.                                                                           | | `verificationFailed`       | Phone number verification failed with an error. For example, quota exceeded or unknown phone number format. Provided with a description of the error.                                                                      | | `codeSent`                 | SMS message with verification code sent to phone number. Provided with the verification id to pass along to `GetCredential` along with the sent code, and a token to use if the user requests another SMS message be sent. | | `codeAutoRetrievalTimeOut` | The timeout specified has expired. Provided with the verification id for the transaction that timed out.                                                                                                                   | |

## Public static functions

### GetInstance

```c#
PhoneAuthProvider GetInstance(
  FirebaseAuth auth
)
```  
Return the [PhoneAuthProvider](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider) for the specified `auth`.

<br />

|                                                                                                                                                                                                                                                                                                                                   Details                                                                                                                                                                                                                                                                                                                                    ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `auth` | The [Auth](https://firebase.google.com/docs/reference/unity/namespace/firebase/auth#namespace_firebase_1_1_auth) session for which we want to get a [PhoneAuthProvider](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider). | |
| **Returns** | a [PhoneAuthProvider](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider) for the given auth object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |