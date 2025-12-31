# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks.md.txt

# PhoneAuthProvider.OnVerificationStateChangedCallbacks

# PhoneAuthProvider.OnVerificationStateChangedCallbacks


```
abstract class PhoneAuthProvider.OnVerificationStateChangedCallbacks
```

<br />

*** ** * ** ***

Registered callbacks for the different phone auth events. Requires implementing two mandatory callbacks and provides default no-op implementations for optional callbacks.

## Summary

|                                                                                              ### Public constructors                                                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [OnVerificationStateChangedCallbacks](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#OnVerificationStateChangedCallbacks())`()` |

|                                  ### Public functions                                   |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)            | [onCodeAutoRetrievalTimeOut](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeAutoRetrievalTimeOut(java.lang.String))`(verificationId: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Optional callback.                                                                                                                                                                                                                          |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)            | [onCodeSent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeSent(java.lang.String,com.google.firebase.auth.PhoneAuthProvider.ForceResendingToken))`(` ` verificationId: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`,` ` forceResendingToken: `[PhoneAuthProvider.ForceResendingToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken) `)` Optional callback. |
| `abstract `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [onVerificationCompleted](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onVerificationCompleted(com.google.firebase.auth.PhoneAuthCredential))`(credential: `[PhoneAuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthCredential)`)` This callback must be implemented.                                                                                                                                                   |
| `abstract `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [onVerificationFailed](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onVerificationFailed(com.google.firebase.FirebaseException))`(exception: `[FirebaseException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseException)`)` This callback must be implemented.                                                                                                                                                                          |

## Public constructors

### OnVerificationStateChangedCallbacks

```
OnVerificationStateChangedCallbacks()
```  

## Public functions

### onCodeAutoRetrievalTimeOut

```
funÂ onCodeAutoRetrievalTimeOut(verificationId:Â String):Â Unit
```

Optional callback. It will trigger when SMS auto-retrieval times out and provide a `
verificationId`.  

### onCodeSent

```
funÂ onCodeSent(
Â Â Â Â verificationId:Â String,
Â Â Â Â forceResendingToken:Â PhoneAuthProvider.ForceResendingToken
):Â Unit
```

Optional callback. It will trigger when an SMS has been sent to the users phone, and will include a `verificationId` and [ForceResendingToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken).  

### onVerificationCompleted

```
abstractÂ funÂ onVerificationCompleted(credential:Â PhoneAuthCredential):Â Unit
```

This callback must be implemented. It will trigger when an SMS is auto-retrieved or the phone number has been instantly verified. The callback will provide a [AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential).  

### onVerificationFailed

```
abstractÂ funÂ onVerificationFailed(exception:Â FirebaseException):Â Unit
```

This callback must be implemented.

Triggered when an error occurred during phone number verification.
Exceptions

- [FirebaseAuthInvalidCredentialsException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException) thrown if the request is in some way malformed (such as an invalid phone number). Check the error message for details.
- [com.google.firebase.auth.FirebaseAuthException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthException) thrown if the app is not authorized to use Firebase Authentication. Verify the app's package name and SHA-1 in the Firebase Console.
- [com.google.firebase.FirebaseTooManyRequestsException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseTooManyRequestsException) thrown if the sms quota for the project has been exceeded.
- [com.google.firebase.FirebaseApiNotAvailableException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApiNotAvailableException) thrown if this api is called on a device the does not have Google Play Services
- [FirebaseAuthMissingActivityForRecaptchaException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthMissingActivityForRecaptchaException) thrown if the activity is not set and a reCAPTCHA verification is attempted