# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder.md.txt

# PhoneAuthOptions.Builder

# PhoneAuthOptions.Builder


```
class PhoneAuthOptions.Builder
```

<br />

*** ** * ** ***

A Builder class for [PhoneAuthOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions). Get an instance of this Builder using [newBuilder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions#newBuilder()) or [newBuilder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions#newBuilder(com.google.firebase.auth.FirebaseAuth)).

## Summary

|                                                                                                                                        ### Public constructors                                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder#Builder(com.google.firebase.auth.FirebaseAuth))`(auth: `[FirebaseAuth](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth)`)` Creates a new Builder |

|                                                      ### Public functions                                                       |
|---------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PhoneAuthOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions)                 | [build](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder#build())`()` Returns the [PhoneAuthOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions) that this [Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder) has constructed.                                                                                                                                                                                                                                                 |
| [PhoneAuthOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder) | [requireSmsValidation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder#requireSmsValidation(boolean))`(requireSmsValidation: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`)` Specifies whether to force an SMS to be sent for second factor validation.                                                                                                                                                                                                                                                                                             |
| [PhoneAuthOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder) | [setActivity](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder#setActivity(android.app.Activity))`(activity: `[Activity](https://developer.android.com/reference/android/app/Activity.html)`)` Sets the [Activity](https://developer.android.com/reference/android/app/Activity.html) to which the callbacks are scoped, and with which app verification will be completed.                                                                                                                                                                                                                 |
| [PhoneAuthOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder) | [setCallbacks](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder#setCallbacks(com.google.firebase.auth.PhoneAuthProvider.OnVerificationStateChangedCallbacks))`(` ` callbacks: `[PhoneAuthProvider.OnVerificationStateChangedCallbacks](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks) `)` Sets the callbacks to get the status of phone number verification.                                                                                                                                             |
| [PhoneAuthOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder) | [setForceResendingToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder#setForceResendingToken(com.google.firebase.auth.PhoneAuthProvider.ForceResendingToken))`(` ` forceResendingToken: `[PhoneAuthProvider.ForceResendingToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken) `)` Sets the [ForceResendingToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken) to force another verification SMS to be sent before the auto-retrieval timeout. |
| [PhoneAuthOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder) | [setMultiFactorHint](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder#setMultiFactorHint(com.google.firebase.auth.PhoneMultiFactorInfo))`(phoneMultiFactorInfo: `[PhoneMultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo)`)` Sets the [PhoneMultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo) to use for second factor sign-in.                                                                                                                              |
| [PhoneAuthOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder) | [setMultiFactorSession](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder#setMultiFactorSession(com.google.firebase.auth.MultiFactorSession))`(multiFactorSession: `[MultiFactorSession](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorSession)`)` Sets the [MultiFactorSession](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorSession) that holds the necessary data to start an SMS verification for multi-factor authentication enrollment or sign in.                                                    |
| [PhoneAuthOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder) | [setPhoneNumber](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder#setPhoneNumber(java.lang.String))`(phoneNumber: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Sets the phone number for sign-in, sign-up, or second factor enrollment.                                                                                                                                                                                                                                                                                                             |
| [PhoneAuthOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder) | [setTimeout](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder#setTimeout(java.lang.Long,java.util.concurrent.TimeUnit))`(timeout: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)`, unit: `[TimeUnit](https://developer.android.com/reference/java/util/concurrent/TimeUnit.html)`)` Sets the maximum amount of time you are willing to wait for SMS auto-retrieval to be completed by the library.                                                                                                                                                           |

## Public constructors

### Builder

```
Builder(auth:Â FirebaseAuth)
```

Creates a new Builder  

|                                                   Parameters                                                    |
|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `auth: `[FirebaseAuth](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth) | the [FirebaseAuth](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth) with which this Builder is associated. |

## Public functions

### build

```
funÂ build():Â PhoneAuthOptions
```

Returns the [PhoneAuthOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions) that this [Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder) has constructed.  

### requireSmsValidation

```
funÂ requireSmsValidation(requireSmsValidation:Â Boolean):Â PhoneAuthOptions.Builder
```

Specifies whether to force an SMS to be sent for second factor validation.

In some cases the phone number can be instantly verified without needing to send or enter a verification code. This feature can be disabled here, and it is enabled by default.

This is only applicable to Multi-Factor Authentication.  

### setActivity

```
funÂ setActivity(activity:Â Activity):Â PhoneAuthOptions.Builder
```

Sets the [Activity](https://developer.android.com/reference/android/app/Activity.html) to which the callbacks are scoped, and with which app verification will be completed. This is an optional parameter of the builder, but is required to perform a reCAPTCHA fallback for client verification. If the activity is not set and a reCAPTCHA verification is attempted, a [FirebaseAuthMissingActivityForRecaptchaException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthMissingActivityForRecaptchaException) error is thrown, which can be handled in the [onVerificationFailed](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onVerificationFailed(com.google.firebase.FirebaseException)) callback.  

### setCallbacks

```
funÂ setCallbacks(
Â Â Â Â callbacks:Â PhoneAuthProvider.OnVerificationStateChangedCallbacks
):Â PhoneAuthOptions.Builder
```

Sets the callbacks to get the status of phone number verification. The callbacks will be automatically removed when the specified activity has stopped.

When a test phone number and SMS code pair is set via [setAutoRetrievedSmsCodeForPhoneNumber](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthSettings#setAutoRetrievedSmsCodeForPhoneNumber(java.lang.String,java.lang.String)) and in the Firebase console, [onCodeAutoRetrievalTimeOut](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeAutoRetrievalTimeOut(java.lang.String)) will never be triggered.  

### setForceResendingToken

```
funÂ setForceResendingToken(
Â Â Â Â forceResendingToken:Â PhoneAuthProvider.ForceResendingToken
):Â PhoneAuthOptions.Builder
```

Sets the [ForceResendingToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken) to force another verification SMS to be sent before the auto-retrieval timeout.  

### setMultiFactorHint

```
funÂ setMultiFactorHint(phoneMultiFactorInfo:Â PhoneMultiFactorInfo):Â PhoneAuthOptions.Builder
```

Sets the [PhoneMultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo) to use for second factor sign-in.  

### setMultiFactorSession

```
funÂ setMultiFactorSession(multiFactorSession:Â MultiFactorSession):Â PhoneAuthOptions.Builder
```

Sets the [MultiFactorSession](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorSession) that holds the necessary data to start an SMS verification for multi-factor authentication enrollment or sign in.

When this is set, the verification will be for validating ownership of a phone SMS second factor, not for phone authentication.  

### setPhoneNumber

```
funÂ setPhoneNumber(phoneNumber:Â String):Â PhoneAuthOptions.Builder
```

Sets the phone number for sign-in, sign-up, or second factor enrollment.  

|                                           Parameters                                            |
|-------------------------------------------------------------------------------------------------|---------------------------------------------------|
| `phoneNumber: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | a phone number that conforms to the E.164 format. |

### setTimeout

```
funÂ setTimeout(timeout:Â Long,Â unit:Â TimeUnit):Â PhoneAuthOptions.Builder
```

Sets the maximum amount of time you are willing to wait for SMS auto-retrieval to be completed by the library.

The minimum timeout is 30 seconds, and the maximum timeout is 2 minutes. If you specified a positive value less than 30 seconds, library will default to 30 seconds. Specifying a negative timeout or a timeout that is greater than 120 seconds will result in an being thrown.

Use 0 to disable SMS-auto-retrieval. This will also cause [onCodeAutoRetrievalTimeOut](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeAutoRetrievalTimeOut(java.lang.String)) to be called immediately.  

|                                           Parameters                                           |
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| `timeout: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)        | the length of the timeout in the units specified by `unit`.                                                   |
| `unit: `[TimeUnit](https://developer.android.com/reference/java/util/concurrent/TimeUnit.html) | the [TimeUnit](https://developer.android.com/reference/java/util/concurrent/TimeUnit.html) for the `timeout`. |