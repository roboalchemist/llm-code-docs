# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder.md.txt

# PhoneAuthOptions.Builder

# PhoneAuthOptions.Builder


```
class PhoneAuthOptions.Builder
```

<br />

*** ** * ** ***

A Builder class for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions`. Get an instance of this Builder using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions#newBuilder()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions#newBuilder(com.google.firebase.auth.FirebaseAuth)`.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder#Builder(com.google.firebase.auth.FirebaseAuth)(auth: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth)` Creates a new Builder |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder#build()()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions` that this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder` has constructed. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder#requireSmsValidation(boolean)(requireSmsValidation: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Specifies whether to force an SMS to be sent for second factor validation. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder#setActivity(android.app.Activity)(activity: https://developer.android.com/reference/android/app/Activity.html)` Sets the `https://developer.android.com/reference/android/app/Activity.html` to which the callbacks are scoped, and with which app verification will be completed. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder#setCallbacks(com.google.firebase.auth.PhoneAuthProvider.OnVerificationStateChangedCallbacks)( callbacks: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks )` Sets the callbacks to get the status of phone number verification. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder#setForceResendingToken(com.google.firebase.auth.PhoneAuthProvider.ForceResendingToken)( forceResendingToken: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken )` Sets the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken` to force another verification SMS to be sent before the auto-retrieval timeout. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder#setMultiFactorHint(com.google.firebase.auth.PhoneMultiFactorInfo)(phoneMultiFactorInfo: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo)` Sets the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo` to use for second factor sign-in. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder#setMultiFactorSession(com.google.firebase.auth.MultiFactorSession)(multiFactorSession: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorSession)` Sets the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorSession` that holds the necessary data to start an SMS verification for multi-factor authentication enrollment or sign in. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder#setPhoneNumber(java.lang.String)(phoneNumber: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Sets the phone number for sign-in, sign-up, or second factor enrollment. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder#setTimeout(java.lang.Long,java.util.concurrent.TimeUnit)(timeout: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, unit: https://developer.android.com/reference/java/util/concurrent/TimeUnit.html)` Sets the maximum amount of time you are willing to wait for SMS auto-retrieval to be completed by the library. |

## Public constructors

### Builder

```
Builder(auth: FirebaseAuth)
```

Creates a new Builder

| Parameters |
|---|---|
| `auth: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth` | the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth` with which this Builder is associated. |

## Public functions

### build

```
fun build(): PhoneAuthOptions
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions` that this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder` has constructed.

### requireSmsValidation

```
fun requireSmsValidation(requireSmsValidation: Boolean): PhoneAuthOptions.Builder
```

Specifies whether to force an SMS to be sent for second factor validation.

In some cases the phone number can be instantly verified without needing to send or enter a verification code. This feature can be disabled here, and it is enabled by default.

This is only applicable to Multi-Factor Authentication.

### setActivity

```
fun setActivity(activity: Activity): PhoneAuthOptions.Builder
```

Sets the `https://developer.android.com/reference/android/app/Activity.html` to which the callbacks are scoped, and with which app verification will be completed. This is an optional parameter of the builder, but is required to perform a reCAPTCHA fallback for client verification. If the activity is not set and a reCAPTCHA verification is attempted, a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthMissingActivityForRecaptchaException` error is thrown, which can be handled in the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onVerificationFailed(com.google.firebase.FirebaseException)` callback.

### setCallbacks

```
fun setCallbacks(
    callbacks: PhoneAuthProvider.OnVerificationStateChangedCallbacks
): PhoneAuthOptions.Builder
```

Sets the callbacks to get the status of phone number verification. The callbacks will be automatically removed when the specified activity has stopped.

When a test phone number and SMS code pair is set via `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthSettings#setAutoRetrievedSmsCodeForPhoneNumber(java.lang.String,java.lang.String)` and in the Firebase console, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeAutoRetrievalTimeOut(java.lang.String)` will never be triggered.

### setForceResendingToken

```
fun setForceResendingToken(
    forceResendingToken: PhoneAuthProvider.ForceResendingToken
): PhoneAuthOptions.Builder
```

Sets the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken` to force another verification SMS to be sent before the auto-retrieval timeout.

### setMultiFactorHint

```
fun setMultiFactorHint(phoneMultiFactorInfo: PhoneMultiFactorInfo): PhoneAuthOptions.Builder
```

Sets the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo` to use for second factor sign-in.

### setMultiFactorSession

```
fun setMultiFactorSession(multiFactorSession: MultiFactorSession): PhoneAuthOptions.Builder
```

Sets the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorSession` that holds the necessary data to start an SMS verification for multi-factor authentication enrollment or sign in.

When this is set, the verification will be for validating ownership of a phone SMS second factor, not for phone authentication.

### setPhoneNumber

```
fun setPhoneNumber(phoneNumber: String): PhoneAuthOptions.Builder
```

Sets the phone number for sign-in, sign-up, or second factor enrollment.

| Parameters |
|---|---|
| `phoneNumber: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | a phone number that conforms to the E.164 format. |

### setTimeout

```
fun setTimeout(timeout: Long, unit: TimeUnit): PhoneAuthOptions.Builder
```

Sets the maximum amount of time you are willing to wait for SMS auto-retrieval to be completed by the library.

The minimum timeout is 30 seconds, and the maximum timeout is 2 minutes. If you specified a positive value less than 30 seconds, library will default to 30 seconds. Specifying a negative timeout or a timeout that is greater than 120 seconds will result in an being thrown.

Use 0 to disable SMS-auto-retrieval. This will also cause `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeAutoRetrievalTimeOut(java.lang.String)` to be called immediately.

| Parameters |
|---|---|
| `timeout: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the length of the timeout in the units specified by `unit`. |
| `unit: https://developer.android.com/reference/java/util/concurrent/TimeUnit.html` | the `https://developer.android.com/reference/java/util/concurrent/TimeUnit.html` for the `timeout`. |