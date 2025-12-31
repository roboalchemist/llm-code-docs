# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneAuthProvider.md.txt

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

|                                                                                                                                                        ### Nested types                                                                                                                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `class `[PhoneAuthProvider.ForceResendingToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken)` : `[Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) A 'token' that can be used to force re-sending an SMS verification code. |
| `abstract class `[PhoneAuthProvider.OnVerificationStateChangedCallbacks](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks) Registered callbacks for the different phone auth events.                                                            |

|                                        ### Constants                                        |
|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [PHONE_SIGN_IN_METHOD](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#PHONE_SIGN_IN_METHOD())` = "phone"` Unique string identifier for Phone sign-in method. |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [PROVIDER_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#PROVIDER_ID())` = "phone"` Unique string identifier for this provider type.                     |

|                                                        ### Public functions                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java-static `[PhoneAuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthCredential) | [getCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#getCredential(java.lang.String,java.lang.String))`(verificationId: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, smsCode: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns a new instance of [AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential) that is associated with a phone number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `java-static `[PhoneAuthProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider)     | ~~[getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#getInstance())~~`()` **This function is deprecated.** Instead, use [verifyPhoneNumber](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)) <br />                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `java-static `[PhoneAuthProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider)     | ~~[getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#getInstance(com.google.firebase.auth.FirebaseAuth))~~`(firebaseAuth: `[FirebaseAuth](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth)`)` **This function is deprecated.** Instead, use [verifyPhoneNumber](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)) <br />                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `java-static `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                          | [verifyPhoneNumber](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions))`(options: `[PhoneAuthOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions)`)` Starts the phone verification process with the settings defined in [PhoneAuthOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                        | ~~[verifyPhoneNumber](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(java.lang.String,long,java.util.concurrent.TimeUnit,android.app.Activity,com.google.firebase.auth.PhoneAuthProvider.OnVerificationStateChangedCallbacks))~~`(` ` phoneNumber: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`,` ` timeout: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)`,` ` unit: `[TimeUnit](https://developer.android.com/reference/java/util/concurrent/TimeUnit.html)`,` ` activity: `[Activity](https://developer.android.com/reference/android/app/Activity.html)`,` ` callbacks: `[PhoneAuthProvider.OnVerificationStateChangedCallbacks](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks) `)` **This function is deprecated.** Instead, use [verifyPhoneNumber](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)) <br />                                                                                                                                                                                                                                                        |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                        | ~~[verifyPhoneNumber](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(java.lang.String,long,java.util.concurrent.TimeUnit,android.app.Activity,com.google.firebase.auth.PhoneAuthProvider.OnVerificationStateChangedCallbacks,com.google.firebase.auth.PhoneAuthProvider.ForceResendingToken))~~`(` ` phoneNumber: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`,` ` timeout: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)`,` ` unit: `[TimeUnit](https://developer.android.com/reference/java/util/concurrent/TimeUnit.html)`,` ` activity: `[Activity](https://developer.android.com/reference/android/app/Activity.html)`,` ` callbacks: `[PhoneAuthProvider.OnVerificationStateChangedCallbacks](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks)`,` ` forceResendingToken: `[PhoneAuthProvider.ForceResendingToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken)`?` `)` **This function is deprecated.** Instead, use [verifyPhoneNumber](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)) <br /> |

## Constants

### PHONE_SIGN_IN_METHOD

```
constÂ valÂ PHONE_SIGN_IN_METHOD = "phone":Â String!
```

Unique string identifier for Phone sign-in method.  

### PROVIDER_ID

```
constÂ valÂ PROVIDER_ID = "phone":Â String!
```

Unique string identifier for this provider type.  

## Public functions

### getCredential

```
java-staticÂ funÂ getCredential(verificationId:Â String,Â smsCode:Â String):Â PhoneAuthCredential
```

Returns a new instance of [AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential) that is associated with a phone number. Used when calling [signInWithCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)) or [linkWithCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)).  

|                                             Parameters                                             |
|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `verificationId: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | a valid `verificationId` retrieved by calling [verifyPhoneNumber](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(java.lang.String,long,java.util.concurrent.TimeUnit,android.app.Activity,com.google.firebase.auth.PhoneAuthProvider.OnVerificationStateChangedCallbacks)) |
| `smsCode: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)        | the 6 digit SMS-code sent to the user                                                                                                                                                                                                                                                                                                      |

### getInstance

```
java-staticÂ funÂ [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#getInstance())():Â PhoneAuthProvider
```
| **This function is deprecated.**   
|
| Instead, use [verifyPhoneNumber](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions))

Initializes a new [PhoneAuthProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider) using the default FirebaseAuth instance.  

### getInstance

```
java-staticÂ funÂ [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#getInstance(com.google.firebase.auth.FirebaseAuth))(firebaseAuth:Â FirebaseAuth):Â PhoneAuthProvider
```
| **This function is deprecated.**   
|
| Instead, use [verifyPhoneNumber](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions))

Static method to initialize a new [PhoneAuthProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider) for the specified Auth instance.  

### verifyPhoneNumber

```
java-staticÂ funÂ verifyPhoneNumber(options:Â PhoneAuthOptions):Â Unit
```

Starts the phone verification process with the settings defined in [PhoneAuthOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions).  

### verifyPhoneNumber

```
funÂ [verifyPhoneNumber](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(java.lang.String,long,java.util.concurrent.TimeUnit,android.app.Activity,com.google.firebase.auth.PhoneAuthProvider.OnVerificationStateChangedCallbacks))(
Â Â Â Â phoneNumber:Â String,
Â Â Â Â timeout:Â Long,
Â Â Â Â unit:Â TimeUnit,
Â Â Â Â activity:Â Activity,
Â Â Â Â callbacks:Â PhoneAuthProvider.OnVerificationStateChangedCallbacks
):Â Unit
```
| **This function is deprecated.**   
|
| Instead, use [verifyPhoneNumber](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions))

Starts the phone number verification process for the given phone number. Either sends an SMS with a 6 digit code to the phone number specified or triggers the callback with a complete [AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential) that can be used to log in the user.

The specified callback will be Activity-scoped, i.e. it will be automatically removed during [onStop](https://developer.android.com/reference/android/app/Activity.html#onStop()). This function is reentrant and can be called again in [onStart](https://developer.android.com/reference/android/app/Activity.html#onStart()). No duplicated SMS will be sent out upon re-entry (before timeout).

Make sure to test all scenarios below:

- You directly get back an [AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential) if Google Play services verified the phone number instantly or helped you auto-retrieve the verification code.
- auto-retrieve verification code timed out.
- error cases when you receive [onVerificationFailed](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onVerificationFailed(com.google.firebase.FirebaseException)).

|                                                                                               Parameters                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `phoneNumber: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                                        | the phone number for the account the user is signing up for or signing into. Make sure to pass in a phone number with country code prefixed with plus sign ('+').                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `timeout: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)                                                                                                                | the maximum amount of time you are willing to wait for SMS auto-retrieval to be completed by the library. Maximum allowed value is 2 minutes. Use 0 to disable SMS-auto-retrieval. Setting this to 0 will also cause [onCodeAutoRetrievalTimeOut](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeAutoRetrievalTimeOut(java.lang.String)) to be called immediately. If you specified a positive value less than 30 seconds, library will default to 30 seconds.                                                                                                                                       |
| `unit: `[TimeUnit](https://developer.android.com/reference/java/util/concurrent/TimeUnit.html)                                                                                                         | the [TimeUnit](https://developer.android.com/reference/java/util/concurrent/TimeUnit.html) for the timeout                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `activity: `[Activity](https://developer.android.com/reference/android/app/Activity.html)                                                                                                              | the Activity to which the callbacks are scoped.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `callbacks: `[PhoneAuthProvider.OnVerificationStateChangedCallbacks](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks) | the callbacks to get the status of phone number verification. The callbacks will be automatically removed when the specified activity has stopped. When a test phone number and sms code pair is set via [setAutoRetrievedSmsCodeForPhoneNumber](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthSettings#setAutoRetrievedSmsCodeForPhoneNumber(java.lang.String,java.lang.String)) and in the Firebase console, [onCodeAutoRetrievalTimeOut](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeAutoRetrievalTimeOut(java.lang.String)) will never be triggered. |

### verifyPhoneNumber

```
funÂ [verifyPhoneNumber](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(java.lang.String,long,java.util.concurrent.TimeUnit,android.app.Activity,com.google.firebase.auth.PhoneAuthProvider.OnVerificationStateChangedCallbacks,com.google.firebase.auth.PhoneAuthProvider.ForceResendingToken))(
Â Â Â Â phoneNumber:Â String,
Â Â Â Â timeout:Â Long,
Â Â Â Â unit:Â TimeUnit,
Â Â Â Â activity:Â Activity,
Â Â Â Â callbacks:Â PhoneAuthProvider.OnVerificationStateChangedCallbacks,
Â Â Â Â forceResendingToken:Â PhoneAuthProvider.ForceResendingToken?
):Â Unit
```
| **This function is deprecated.**   
|
| Instead, use [verifyPhoneNumber](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions))

See [verifyPhoneNumber](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(java.lang.String,long,java.util.concurrent.TimeUnit,android.app.Activity,com.google.firebase.auth.PhoneAuthProvider.OnVerificationStateChangedCallbacks)) for details. This overload allows specifying a .  

|                                                                                               Parameters                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `phoneNumber: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                                        | the phone number for the account the user is signing up for or signing into. Make sure to pass in a phone number with country code prefixed with plus sign ('+').                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `timeout: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)                                                                                                                | the maximum amount of time you are willing to wait for SMS auto-retrieval to be completed by the library. Maximum allowed value is 2 minutes. Use 0 to disable SMS-auto-retrieval. Setting this to 0 will also cause [onCodeAutoRetrievalTimeOut](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeAutoRetrievalTimeOut(java.lang.String)) to be called immediately. If you specified a positive value less than 30 seconds, library will default to 30 seconds.                                                                                                                                       |
| `unit: `[TimeUnit](https://developer.android.com/reference/java/util/concurrent/TimeUnit.html)                                                                                                         | the [TimeUnit](https://developer.android.com/reference/java/util/concurrent/TimeUnit.html) for the timeout                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `activity: `[Activity](https://developer.android.com/reference/android/app/Activity.html)                                                                                                              | the Activity to which the callbacks are scoped.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `callbacks: `[PhoneAuthProvider.OnVerificationStateChangedCallbacks](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks) | the callbacks to get the status of phone number verification. The callbacks will be automatically removed when the specified activity has stopped. When a test phone number and sms code pair is set via [setAutoRetrievedSmsCodeForPhoneNumber](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthSettings#setAutoRetrievedSmsCodeForPhoneNumber(java.lang.String,java.lang.String)) and in the Firebase console, [onCodeAutoRetrievalTimeOut](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeAutoRetrievalTimeOut(java.lang.String)) will never be triggered. |
| `forceResendingToken: `[PhoneAuthProvider.ForceResendingToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken)`?`                    | the ForceResendingToken obtained from [onCodeSent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeSent(java.lang.String,com.google.firebase.auth.PhoneAuthProvider.ForceResendingToken)) callback to force re-sending another verification SMS before the auto-retrieval timeout.                                                                                                                                                                                                                                                                                                                    |