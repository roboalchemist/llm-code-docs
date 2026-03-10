# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks.md.txt

# PhoneAuthProvider.OnVerificationStateChangedCallbacks

# PhoneAuthProvider.OnVerificationStateChangedCallbacks


```
public abstract class PhoneAuthProvider.OnVerificationStateChangedCallbacks
```

<br />

*** ** * ** ***

Registered callbacks for the different phone auth events. Requires implementing two mandatory callbacks and provides default no-op implementations for optional callbacks.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#OnVerificationStateChangedCallbacks()()` |

| ### Public methods |
|---|---|
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeAutoRetrievalTimeOut(java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html verificationId)` Optional callback. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeSent(java.lang.String,com.google.firebase.auth.PhoneAuthProvider.ForceResendingToken)( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html verificationId, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken forceResendingToken )` Optional callback. |
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onVerificationCompleted(com.google.firebase.auth.PhoneAuthCredential)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthCredential credential)` This callback must be implemented. |
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onVerificationFailed(com.google.firebase.FirebaseException)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseException exception)` This callback must be implemented. |

## Public constructors

### OnVerificationStateChangedCallbacks

```
public OnVerificationStateChangedCallbacks()
```

## Public methods

### onCodeAutoRetrievalTimeOut

```
public void onCodeAutoRetrievalTimeOut(@NonNull String verificationId)
```

Optional callback. It will trigger when SMS auto-retrieval times out and provide a `
verificationId`.

### onCodeSent

```
public void onCodeSent(
    @NonNull String verificationId,
    @NonNull PhoneAuthProvider.ForceResendingToken forceResendingToken
)
```

Optional callback. It will trigger when an SMS has been sent to the users phone, and will include a `verificationId` and `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken`.

### onVerificationCompleted

```
public abstract void onVerificationCompleted(@NonNull PhoneAuthCredential credential)
```

This callback must be implemented. It will trigger when an SMS is auto-retrieved or the phone number has been instantly verified. The callback will provide a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential`.

### onVerificationFailed

```
public abstract void onVerificationFailed(@NonNull FirebaseException exception)
```

This callback must be implemented.

Triggered when an error occurred during phone number verification.
Exceptions

- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException` thrown if the request is in some way malformed (such as an invalid phone number). Check the error message for details.
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException` thrown if the app is not authorized to use Firebase Authentication. Verify the app's package name and SHA-1 in the Firebase Console.
- `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseTooManyRequestsException` thrown if the sms quota for the project has been exceeded.
- `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApiNotAvailableException` thrown if this api is called on a device the does not have Google Play Services
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthMissingActivityForRecaptchaException` thrown if the activity is not set and a reCAPTCHA verification is attempted