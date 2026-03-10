# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthSettings.md.txt

# FirebaseAuthSettings

# FirebaseAuthSettings


```
abstract class FirebaseAuthSettings
```

<br />

*** ** * ** ***

Enables the configuration of FirebaseAuth related settings.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthSettings#FirebaseAuthSettings()()` |

| ### Public functions |
|---|---|
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthSettings#forceRecaptchaFlowForTesting(boolean)(forceRecaptchaFlow: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Forces application verification to use the web reCAPTCHA flow for Phone Authentication. |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthSettings#setAppVerificationDisabledForTesting(boolean)(setVerificationDisabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Disables application verification flows for Phone Authentication and Phone Multi-Factor flows. |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthSettings#setAutoRetrievedSmsCodeForPhoneNumber(java.lang.String,java.lang.String)( phoneNumber: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, smsCode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? )` The phone number and SMS code here must have been configured in the Firebase Console (Authentication \>Sign In Method \>Phone). |

## Public constructors

### FirebaseAuthSettings

```
FirebaseAuthSettings()
```

## Public functions

### forceRecaptchaFlowForTesting

```
abstract fun forceRecaptchaFlowForTesting(forceRecaptchaFlow: Boolean): Unit
```

Forces application verification to use the web reCAPTCHA flow for Phone Authentication.

Once this has been called, every call to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)` will skip the Play Integrity API verification flow and use the reCAPTCHA flow instead.

Calling this method a second time will overwrite the previously passed parameter.

| Parameters |
|---|---|
| `forceRecaptchaFlow: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | whether to only use the reCAPTCHA-based verification flow. |

### setAppVerificationDisabledForTesting

```
abstract fun setAppVerificationDisabledForTesting(setVerificationDisabled: Boolean): Unit
```

Disables application verification flows for Phone Authentication and Phone Multi-Factor flows. Intended for use with the phone numbers configured in the Firebase Console for testing (Authentication \>Sign In Method \>Phone), or with the Firebase Auth emulator.

Once this has been called, every call to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)` will skip the Play Integrity API and reCAPTCHA verification flows.

Calling this method a second time will overwrite the previously passed parameter.

| Parameters |
|---|---|
| `setVerificationDisabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | whether to disable application verification for phone flows. |

### setAutoRetrievedSmsCodeForPhoneNumber

```
abstract fun setAutoRetrievedSmsCodeForPhoneNumber(
    phoneNumber: String?,
    smsCode: String?
): Unit
```

The phone number and SMS code here must have been configured in the Firebase Console (Authentication \>Sign In Method \>Phone).

Once this has been called, every call to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)` with the same phone number as the one that is configured here will have `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onVerificationCompleted(com.google.firebase.auth.PhoneAuthCredential)` triggered as the callback.

Calling this method a second time will overwrite the previously passed parameters. Only one number can be configured at a given time.

Calling this method with either parameter set to null removes this functionality until valid parameters are passed.

Verifying a phone number other than the one configured here will trigger normal behaviour. If the phone number is configured as a test phone number in the console, the regular testing flow occurs. Otherwise, normal phone number verification will take place.

When this is set and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)` is called with a matching phone number, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeAutoRetrievalTimeOut(java.lang.String)` will never be called.

| Parameters |
|---|---|
| `phoneNumber: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | A phone number that has been configured in the Firebase Console that conforms to the E.164 format. |
| `smsCode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | An SMS code that has been configured in the Firebase Console. |