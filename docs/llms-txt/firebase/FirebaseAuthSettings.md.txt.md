# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthSettings.md.txt

# FirebaseAuthSettings

# FirebaseAuthSettings


```
public abstract class FirebaseAuthSettings
```

<br />

*** ** * ** ***

Enables the configuration of FirebaseAuth related settings.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthSettings#FirebaseAuthSettings()()` |

| ### Public methods |
|---|---|
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthSettings#forceRecaptchaFlowForTesting(boolean)(boolean forceRecaptchaFlow)` Forces application verification to use the web reCAPTCHA flow for Phone Authentication. |
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthSettings#setAppVerificationDisabledForTesting(boolean)(boolean setVerificationDisabled)` Disables application verification flows for Phone Authentication and Phone Multi-Factor flows. |
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthSettings#setAutoRetrievedSmsCodeForPhoneNumber(java.lang.String,java.lang.String)( @https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html phoneNumber, @https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html smsCode )` The phone number and SMS code here must have been configured in the Firebase Console (Authentication \>Sign In Method \>Phone). |

## Public constructors

### FirebaseAuthSettings

```
public FirebaseAuthSettings()
```

## Public methods

### forceRecaptchaFlowForTesting

```
public abstract void forceRecaptchaFlowForTesting(boolean forceRecaptchaFlow)
```

Forces application verification to use the web reCAPTCHA flow for Phone Authentication.

Once this has been called, every call to `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)` will skip the Play Integrity API verification flow and use the reCAPTCHA flow instead.

Calling this method a second time will overwrite the previously passed parameter.

| Parameters |
|---|---|
| `boolean forceRecaptchaFlow` | whether to only use the reCAPTCHA-based verification flow. |

### setAppVerificationDisabledForTesting

```
public abstract void setAppVerificationDisabledForTesting(boolean setVerificationDisabled)
```

Disables application verification flows for Phone Authentication and Phone Multi-Factor flows. Intended for use with the phone numbers configured in the Firebase Console for testing (Authentication \>Sign In Method \>Phone), or with the Firebase Auth emulator.

Once this has been called, every call to `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)` will skip the Play Integrity API and reCAPTCHA verification flows.

Calling this method a second time will overwrite the previously passed parameter.

| Parameters |
|---|---|
| `boolean setVerificationDisabled` | whether to disable application verification for phone flows. |

### setAutoRetrievedSmsCodeForPhoneNumber

```
public abstract void setAutoRetrievedSmsCodeForPhoneNumber(
    @Nullable String phoneNumber,
    @Nullable String smsCode
)
```

The phone number and SMS code here must have been configured in the Firebase Console (Authentication \>Sign In Method \>Phone).

Once this has been called, every call to `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)` with the same phone number as the one that is configured here will have `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onVerificationCompleted(com.google.firebase.auth.PhoneAuthCredential)` triggered as the callback.

Calling this method a second time will overwrite the previously passed parameters. Only one number can be configured at a given time.

Calling this method with either parameter set to null removes this functionality until valid parameters are passed.

Verifying a phone number other than the one configured here will trigger normal behaviour. If the phone number is configured as a test phone number in the console, the regular testing flow occurs. Otherwise, normal phone number verification will take place.

When this is set and `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)` is called with a matching phone number, `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeAutoRetrievalTimeOut(java.lang.String)` will never be called.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html phoneNumber` | A phone number that has been configured in the Firebase Console that conforms to the E.164 format. |
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html smsCode` | An SMS code that has been configured in the Firebase Console. |