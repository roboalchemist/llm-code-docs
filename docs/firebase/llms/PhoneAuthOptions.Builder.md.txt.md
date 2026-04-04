# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder.md.txt

# PhoneAuthOptions.Builder

# PhoneAuthOptions.Builder


```
public final class PhoneAuthOptions.Builder
```

<br />

*** ** * ** ***

A Builder class for `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions`. Get an instance of this Builder using `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions#newBuilder()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions#newBuilder(com.google.firebase.auth.FirebaseAuth)`.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder#Builder(com.google.firebase.auth.FirebaseAuth)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth auth)` Creates a new Builder |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder#build()()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions` that this `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder` has constructed. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder#requireSmsValidation(boolean)(boolean requireSmsValidation)` Specifies whether to force an SMS to be sent for second factor validation. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder#setActivity(android.app.Activity)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/android/app/Activity.html activity)` Sets the `https://developer.android.com/reference/android/app/Activity.html` to which the callbacks are scoped, and with which app verification will be completed. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder#setCallbacks(com.google.firebase.auth.PhoneAuthProvider.OnVerificationStateChangedCallbacks)( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks callbacks )` Sets the callbacks to get the status of phone number verification. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder#setForceResendingToken(com.google.firebase.auth.PhoneAuthProvider.ForceResendingToken)( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken forceResendingToken )` Sets the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken` to force another verification SMS to be sent before the auto-retrieval timeout. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder#setMultiFactorHint(com.google.firebase.auth.PhoneMultiFactorInfo)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorInfo phoneMultiFactorInfo)` Sets the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorInfo` to use for second factor sign-in. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder#setMultiFactorSession(com.google.firebase.auth.MultiFactorSession)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorSession multiFactorSession)` Sets the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorSession` that holds the necessary data to start an SMS verification for multi-factor authentication enrollment or sign in. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder#setPhoneNumber(java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html phoneNumber)` Sets the phone number for sign-in, sign-up, or second factor enrollment. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder#setTimeout(java.lang.Long,java.util.concurrent.TimeUnit)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/Long.html timeout, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/util/concurrent/TimeUnit.html unit)` Sets the maximum amount of time you are willing to wait for SMS auto-retrieval to be completed by the library. |

## Public constructors

### Builder

```
public Builder(@NonNull FirebaseAuth auth)
```

Creates a new Builder

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth auth` | the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` with which this Builder is associated. |

## Public methods

### build

```
public @NonNull PhoneAuthOptions build()
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions` that this `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder` has constructed.

### requireSmsValidation

```
public @NonNull PhoneAuthOptions.Builder requireSmsValidation(boolean requireSmsValidation)
```

Specifies whether to force an SMS to be sent for second factor validation.

In some cases the phone number can be instantly verified without needing to send or enter a verification code. This feature can be disabled here, and it is enabled by default.

This is only applicable to Multi-Factor Authentication.

### setActivity

```
public @NonNull PhoneAuthOptions.Builder setActivity(@NonNull Activity activity)
```

Sets the `https://developer.android.com/reference/android/app/Activity.html` to which the callbacks are scoped, and with which app verification will be completed. This is an optional parameter of the builder, but is required to perform a reCAPTCHA fallback for client verification. If the activity is not set and a reCAPTCHA verification is attempted, a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthMissingActivityForRecaptchaException` error is thrown, which can be handled in the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onVerificationFailed(com.google.firebase.FirebaseException)` callback.

### setCallbacks

```
public @NonNull PhoneAuthOptions.Builder setCallbacks(
    @NonNull PhoneAuthProvider.OnVerificationStateChangedCallbacks callbacks
)
```

Sets the callbacks to get the status of phone number verification. The callbacks will be automatically removed when the specified activity has stopped.

When a test phone number and SMS code pair is set via `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthSettings#setAutoRetrievedSmsCodeForPhoneNumber(java.lang.String,java.lang.String)` and in the Firebase console, `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeAutoRetrievalTimeOut(java.lang.String)` will never be triggered.

### setForceResendingToken

```
public @NonNull PhoneAuthOptions.Builder setForceResendingToken(
    @NonNull PhoneAuthProvider.ForceResendingToken forceResendingToken
)
```

Sets the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken` to force another verification SMS to be sent before the auto-retrieval timeout.

### setMultiFactorHint

```
public @NonNull PhoneAuthOptions.Builder setMultiFactorHint(@NonNull PhoneMultiFactorInfo phoneMultiFactorInfo)
```

Sets the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorInfo` to use for second factor sign-in.

### setMultiFactorSession

```
public @NonNull PhoneAuthOptions.Builder setMultiFactorSession(@NonNull MultiFactorSession multiFactorSession)
```

Sets the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorSession` that holds the necessary data to start an SMS verification for multi-factor authentication enrollment or sign in.

When this is set, the verification will be for validating ownership of a phone SMS second factor, not for phone authentication.

### setPhoneNumber

```
public @NonNull PhoneAuthOptions.Builder setPhoneNumber(@NonNull String phoneNumber)
```

Sets the phone number for sign-in, sign-up, or second factor enrollment.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html phoneNumber` | a phone number that conforms to the E.164 format. |

### setTimeout

```
public @NonNull PhoneAuthOptions.Builder setTimeout(@NonNull Long timeout, @NonNull TimeUnit unit)
```

Sets the maximum amount of time you are willing to wait for SMS auto-retrieval to be completed by the library.

The minimum timeout is 30 seconds, and the maximum timeout is 2 minutes. If you specified a positive value less than 30 seconds, library will default to 30 seconds. Specifying a negative timeout or a timeout that is greater than 120 seconds will result in an being thrown.

Use 0 to disable SMS-auto-retrieval. This will also cause `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeAutoRetrievalTimeOut(java.lang.String)` to be called immediately.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/Long.html timeout` | the length of the timeout in the units specified by `unit`. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/util/concurrent/TimeUnit.html unit` | the `https://developer.android.com/reference/java/util/concurrent/TimeUnit.html` for the `timeout`. |