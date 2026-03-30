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

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#OnVerificationStateChangedCallbacks()()` |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeAutoRetrievalTimeOut(java.lang.String)(verificationId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Optional callback. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeSent(java.lang.String,com.google.firebase.auth.PhoneAuthProvider.ForceResendingToken)( verificationId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, forceResendingToken: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken )` Optional callback. |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onVerificationCompleted(com.google.firebase.auth.PhoneAuthCredential)(credential: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthCredential)` This callback must be implemented. |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onVerificationFailed(com.google.firebase.FirebaseException)(exception: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseException)` This callback must be implemented. |

## Public constructors

### OnVerificationStateChangedCallbacks

```
OnVerificationStateChangedCallbacks()
```

## Public functions

### onCodeAutoRetrievalTimeOut

```
fun onCodeAutoRetrievalTimeOut(verificationId: String): Unit
```

Optional callback. It will trigger when SMS auto-retrieval times out and provide a `
verificationId`.

### onCodeSent

```
fun onCodeSent(
    verificationId: String,
    forceResendingToken: PhoneAuthProvider.ForceResendingToken
): Unit
```

Optional callback. It will trigger when an SMS has been sent to the users phone, and will include a `verificationId` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken`.

### onVerificationCompleted

```
abstract fun onVerificationCompleted(credential: PhoneAuthCredential): Unit
```

This callback must be implemented. It will trigger when an SMS is auto-retrieved or the phone number has been instantly verified. The callback will provide a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential`.

### onVerificationFailed

```
abstract fun onVerificationFailed(exception: FirebaseException): Unit
```

This callback must be implemented.

Triggered when an error occurred during phone number verification.
Exceptions

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException` thrown if the request is in some way malformed (such as an invalid phone number). Check the error message for details.
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthException` thrown if the app is not authorized to use Firebase Authentication. Verify the app's package name and SHA-1 in the Firebase Console.
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseTooManyRequestsException` thrown if the sms quota for the project has been exceeded.
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApiNotAvailableException` thrown if this api is called on a device the does not have Google Play Services
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthMissingActivityForRecaptchaException` thrown if the activity is not set and a reCAPTCHA verification is attempted