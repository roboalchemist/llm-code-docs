# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.md.txt

# PhoneAuthProvider

# PhoneAuthProvider


```
class PhoneAuthProvider
```

<br />

*** ** * ** ***

Represents the phone number authentication mechanism. Use this class to obtain s.

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken : https://developer.android.com/reference/android/os/Parcelable.html` A 'token' that can be used to force re-sending an SMS verification code. |
| `abstract class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks` Registered callbacks for the different phone auth events. |

| ### Constants |
|---|---|
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#PHONE_SIGN_IN_METHOD() = "phone"` Unique string identifier for Phone sign-in method. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#PROVIDER_ID() = "phone"` Unique string identifier for this provider type. |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthCredential` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#getCredential(java.lang.String,java.lang.String)(verificationId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, smsCode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` that is associated with a phone number. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider` | `[getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#getInstance())()` **This function is deprecated.** Instead, use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)` <br /> |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider` | `[getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#getInstance(com.google.firebase.auth.FirebaseAuth))(firebaseAuth: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth)` **This function is deprecated.** Instead, use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)` <br /> |
| `java-static https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)(options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions)` Starts the phone verification process with the settings defined in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `[verifyPhoneNumber](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(java.lang.String,long,java.util.concurrent.TimeUnit,android.app.Activity,com.google.firebase.auth.PhoneAuthProvider.OnVerificationStateChangedCallbacks))( phoneNumber: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, timeout: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, unit: https://developer.android.com/reference/java/util/concurrent/TimeUnit.html, activity: https://developer.android.com/reference/android/app/Activity.html, callbacks: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks )` **This function is deprecated.** Instead, use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)` <br /> |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `[verifyPhoneNumber](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(java.lang.String,long,java.util.concurrent.TimeUnit,android.app.Activity,com.google.firebase.auth.PhoneAuthProvider.OnVerificationStateChangedCallbacks,com.google.firebase.auth.PhoneAuthProvider.ForceResendingToken))( phoneNumber: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, timeout: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html, unit: https://developer.android.com/reference/java/util/concurrent/TimeUnit.html, activity: https://developer.android.com/reference/android/app/Activity.html, callbacks: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks, forceResendingToken: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken? )` **This function is deprecated.** Instead, use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)` <br /> |

## Constants

### PHONE_SIGN_IN_METHOD

```
const val PHONE_SIGN_IN_METHOD = "phone": String!
```

Unique string identifier for Phone sign-in method.

### PROVIDER_ID

```
const val PROVIDER_ID = "phone": String!
```

Unique string identifier for this provider type.

## Public functions

### getCredential

```
java-static fun getCredential(verificationId: String, smsCode: String): PhoneAuthCredential
```

Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` that is associated with a phone number. Used when calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)`.

| Parameters |
|---|---|
| `verificationId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | a valid `verificationId` retrieved by calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(java.lang.String,long,java.util.concurrent.TimeUnit,android.app.Activity,com.google.firebase.auth.PhoneAuthProvider.OnVerificationStateChangedCallbacks)` |
| `smsCode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the 6 digit SMS-code sent to the user |

### getInstance

```
java-static fun [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#getInstance())(): PhoneAuthProvider
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Instead, use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)`

Initializes a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider` using the default FirebaseAuth instance.

### getInstance

```
java-static fun [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#getInstance(com.google.firebase.auth.FirebaseAuth))(firebaseAuth: FirebaseAuth): PhoneAuthProvider
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Instead, use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)`

Static method to initialize a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider` for the specified Auth instance.

### verifyPhoneNumber

```
java-static fun verifyPhoneNumber(options: PhoneAuthOptions): Unit
```

Starts the phone verification process with the settings defined in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions`.

### verifyPhoneNumber

```
fun [verifyPhoneNumber](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(java.lang.String,long,java.util.concurrent.TimeUnit,android.app.Activity,com.google.firebase.auth.PhoneAuthProvider.OnVerificationStateChangedCallbacks))(
    phoneNumber: String,
    timeout: Long,
    unit: TimeUnit,
    activity: Activity,
    callbacks: PhoneAuthProvider.OnVerificationStateChangedCallbacks
): Unit
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Instead, use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)`

Starts the phone number verification process for the given phone number. Either sends an SMS with a 6 digit code to the phone number specified or triggers the callback with a complete `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` that can be used to log in the user.

The specified callback will be Activity-scoped, i.e. it will be automatically removed during `https://developer.android.com/reference/android/app/Activity.html#onStop()`. This function is reentrant and can be called again in `https://developer.android.com/reference/android/app/Activity.html#onStart()`. No duplicated SMS will be sent out upon re-entry (before timeout).

Make sure to test all scenarios below:

- You directly get back an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` if Google Play services verified the phone number instantly or helped you auto-retrieve the verification code.
- auto-retrieve verification code timed out.
- error cases when you receive `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onVerificationFailed(com.google.firebase.FirebaseException)`.

| Parameters |
|---|---|
| `phoneNumber: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the phone number for the account the user is signing up for or signing into. Make sure to pass in a phone number with country code prefixed with plus sign ('+'). |
| `timeout: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the maximum amount of time you are willing to wait for SMS auto-retrieval to be completed by the library. Maximum allowed value is 2 minutes. Use 0 to disable SMS-auto-retrieval. Setting this to 0 will also cause `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeAutoRetrievalTimeOut(java.lang.String)` to be called immediately. If you specified a positive value less than 30 seconds, library will default to 30 seconds. |
| `unit: https://developer.android.com/reference/java/util/concurrent/TimeUnit.html` | the `https://developer.android.com/reference/java/util/concurrent/TimeUnit.html` for the timeout |
| `activity: https://developer.android.com/reference/android/app/Activity.html` | the Activity to which the callbacks are scoped. |
| `callbacks: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks` | the callbacks to get the status of phone number verification. The callbacks will be automatically removed when the specified activity has stopped. When a test phone number and sms code pair is set via `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthSettings#setAutoRetrievedSmsCodeForPhoneNumber(java.lang.String,java.lang.String)` and in the Firebase console, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeAutoRetrievalTimeOut(java.lang.String)` will never be triggered. |

### verifyPhoneNumber

```
fun [verifyPhoneNumber](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(java.lang.String,long,java.util.concurrent.TimeUnit,android.app.Activity,com.google.firebase.auth.PhoneAuthProvider.OnVerificationStateChangedCallbacks,com.google.firebase.auth.PhoneAuthProvider.ForceResendingToken))(
    phoneNumber: String,
    timeout: Long,
    unit: TimeUnit,
    activity: Activity,
    callbacks: PhoneAuthProvider.OnVerificationStateChangedCallbacks,
    forceResendingToken: PhoneAuthProvider.ForceResendingToken?
): Unit
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Instead, use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)`

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(java.lang.String,long,java.util.concurrent.TimeUnit,android.app.Activity,com.google.firebase.auth.PhoneAuthProvider.OnVerificationStateChangedCallbacks)` for details. This overload allows specifying a .

| Parameters |
|---|---|
| `phoneNumber: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the phone number for the account the user is signing up for or signing into. Make sure to pass in a phone number with country code prefixed with plus sign ('+'). |
| `timeout: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the maximum amount of time you are willing to wait for SMS auto-retrieval to be completed by the library. Maximum allowed value is 2 minutes. Use 0 to disable SMS-auto-retrieval. Setting this to 0 will also cause `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeAutoRetrievalTimeOut(java.lang.String)` to be called immediately. If you specified a positive value less than 30 seconds, library will default to 30 seconds. |
| `unit: https://developer.android.com/reference/java/util/concurrent/TimeUnit.html` | the `https://developer.android.com/reference/java/util/concurrent/TimeUnit.html` for the timeout |
| `activity: https://developer.android.com/reference/android/app/Activity.html` | the Activity to which the callbacks are scoped. |
| `callbacks: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks` | the callbacks to get the status of phone number verification. The callbacks will be automatically removed when the specified activity has stopped. When a test phone number and sms code pair is set via `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthSettings#setAutoRetrievedSmsCodeForPhoneNumber(java.lang.String,java.lang.String)` and in the Firebase console, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeAutoRetrievalTimeOut(java.lang.String)` will never be triggered. |
| `forceResendingToken: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken?` | the ForceResendingToken obtained from `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeSent(java.lang.String,com.google.firebase.auth.PhoneAuthProvider.ForceResendingToken)` callback to force re-sending another verification SMS before the auto-retrieval timeout. |