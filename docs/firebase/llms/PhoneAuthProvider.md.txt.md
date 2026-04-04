# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.md.txt

# PhoneAuthProvider

# PhoneAuthProvider


```
public class PhoneAuthProvider
```

<br />

*** ** * ** ***

Represents the phone number authentication mechanism. Use this class to obtain s.

## Summary

| ### Nested types |
|---|
| `public class https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken implements https://developer.android.com/reference/android/os/Parcelable.html` A 'token' that can be used to force re-sending an SMS verification code. |
| `public abstract class https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks` Registered callbacks for the different phone auth events. |

| ### Constants |
|---|---|
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#PHONE_SIGN_IN_METHOD() = "phone"` Unique string identifier for Phone sign-in method. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#PROVIDER_ID() = "phone"` Unique string identifier for this provider type. |

| ### Public methods |
|---|---|
| `static @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthCredential` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#getCredential(java.lang.String,java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html verificationId, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html smsCode)` Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` that is associated with a phone number. |
| `static @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider` | `[getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#getInstance())()` **This method is deprecated.** Instead, use `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)` <br /> |
| `static @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider` | `[getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#getInstance(com.google.firebase.auth.FirebaseAuth))(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth firebaseAuth)` **This method is deprecated.** Instead, use `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)` <br /> |
| `static void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions options)` Starts the phone verification process with the settings defined in `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions`. |
| `void` | `[verifyPhoneNumber](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(java.lang.String,long,java.util.concurrent.TimeUnit,android.app.Activity,com.google.firebase.auth.PhoneAuthProvider.OnVerificationStateChangedCallbacks))( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html phoneNumber, long timeout, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/util/concurrent/TimeUnit.html unit, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/android/app/Activity.html activity, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks callbacks )` **This method is deprecated.** Instead, use `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)` <br /> |
| `void` | `[verifyPhoneNumber](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(java.lang.String,long,java.util.concurrent.TimeUnit,android.app.Activity,com.google.firebase.auth.PhoneAuthProvider.OnVerificationStateChangedCallbacks,com.google.firebase.auth.PhoneAuthProvider.ForceResendingToken))( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html phoneNumber, long timeout, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/util/concurrent/TimeUnit.html unit, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/android/app/Activity.html activity, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks callbacks, @https://developer.android.com/reference/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken forceResendingToken )` **This method is deprecated.** Instead, use `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)` <br /> |

## Constants

### PHONE_SIGN_IN_METHOD

```
public static final String PHONE_SIGN_IN_METHOD = "phone"
```

Unique string identifier for Phone sign-in method.

### PROVIDER_ID

```
public static final String PROVIDER_ID = "phone"
```

Unique string identifier for this provider type.

## Public methods

### getCredential

```
public static @NonNull PhoneAuthCredential getCredential(@NonNull String verificationId, @NonNull String smsCode)
```

Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` that is associated with a phone number. Used when calling `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)` or `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html verificationId` | a valid `verificationId` retrieved by calling `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(java.lang.String,long,java.util.concurrent.TimeUnit,android.app.Activity,com.google.firebase.auth.PhoneAuthProvider.OnVerificationStateChangedCallbacks)` |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html smsCode` | the 6 digit SMS-code sent to the user |

### getInstance

```
public static @NonNull PhoneAuthProvider [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#getInstance())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Instead, use `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)`

Initializes a new `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider` using the default FirebaseAuth instance.

### getInstance

```
public static @NonNull PhoneAuthProvider [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#getInstance(com.google.firebase.auth.FirebaseAuth))(@NonNull FirebaseAuth firebaseAuth)
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Instead, use `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)`

Static method to initialize a new `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider` for the specified Auth instance.

### verifyPhoneNumber

```
public static void verifyPhoneNumber(@NonNull PhoneAuthOptions options)
```

Starts the phone verification process with the settings defined in `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions`.

### verifyPhoneNumber

```
public void [verifyPhoneNumber](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(java.lang.String,long,java.util.concurrent.TimeUnit,android.app.Activity,com.google.firebase.auth.PhoneAuthProvider.OnVerificationStateChangedCallbacks))(
    @NonNull String phoneNumber,
    long timeout,
    @NonNull TimeUnit unit,
    @NonNull Activity activity,
    @NonNull PhoneAuthProvider.OnVerificationStateChangedCallbacks callbacks
)
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Instead, use `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)`

Starts the phone number verification process for the given phone number. Either sends an SMS with a 6 digit code to the phone number specified or triggers the callback with a complete `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` that can be used to log in the user.

The specified callback will be Activity-scoped, i.e. it will be automatically removed during `https://developer.android.com/reference/android/app/Activity.html#onStop()`. This function is reentrant and can be called again in `https://developer.android.com/reference/android/app/Activity.html#onStart()`. No duplicated SMS will be sent out upon re-entry (before timeout).

Make sure to test all scenarios below:

- You directly get back an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` if Google Play services verified the phone number instantly or helped you auto-retrieve the verification code.
- auto-retrieve verification code timed out.
- error cases when you receive `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onVerificationFailed(com.google.firebase.FirebaseException)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html phoneNumber` | the phone number for the account the user is signing up for or signing into. Make sure to pass in a phone number with country code prefixed with plus sign ('+'). |
| `long timeout` | the maximum amount of time you are willing to wait for SMS auto-retrieval to be completed by the library. Maximum allowed value is 2 minutes. Use 0 to disable SMS-auto-retrieval. Setting this to 0 will also cause `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeAutoRetrievalTimeOut(java.lang.String)` to be called immediately. If you specified a positive value less than 30 seconds, library will default to 30 seconds. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/util/concurrent/TimeUnit.html unit` | the `https://developer.android.com/reference/java/util/concurrent/TimeUnit.html` for the timeout |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/android/app/Activity.html activity` | the Activity to which the callbacks are scoped. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks callbacks` | the callbacks to get the status of phone number verification. The callbacks will be automatically removed when the specified activity has stopped. When a test phone number and sms code pair is set via `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthSettings#setAutoRetrievedSmsCodeForPhoneNumber(java.lang.String,java.lang.String)` and in the Firebase console, `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeAutoRetrievalTimeOut(java.lang.String)` will never be triggered. |

### verifyPhoneNumber

```
public void [verifyPhoneNumber](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(java.lang.String,long,java.util.concurrent.TimeUnit,android.app.Activity,com.google.firebase.auth.PhoneAuthProvider.OnVerificationStateChangedCallbacks,com.google.firebase.auth.PhoneAuthProvider.ForceResendingToken))(
    @NonNull String phoneNumber,
    long timeout,
    @NonNull TimeUnit unit,
    @NonNull Activity activity,
    @NonNull PhoneAuthProvider.OnVerificationStateChangedCallbacks callbacks,
    @Nullable PhoneAuthProvider.ForceResendingToken forceResendingToken
)
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Instead, use `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)`

See `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(java.lang.String,long,java.util.concurrent.TimeUnit,android.app.Activity,com.google.firebase.auth.PhoneAuthProvider.OnVerificationStateChangedCallbacks)` for details. This overload allows specifying a .

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html phoneNumber` | the phone number for the account the user is signing up for or signing into. Make sure to pass in a phone number with country code prefixed with plus sign ('+'). |
| `long timeout` | the maximum amount of time you are willing to wait for SMS auto-retrieval to be completed by the library. Maximum allowed value is 2 minutes. Use 0 to disable SMS-auto-retrieval. Setting this to 0 will also cause `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeAutoRetrievalTimeOut(java.lang.String)` to be called immediately. If you specified a positive value less than 30 seconds, library will default to 30 seconds. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/util/concurrent/TimeUnit.html unit` | the `https://developer.android.com/reference/java/util/concurrent/TimeUnit.html` for the timeout |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/android/app/Activity.html activity` | the Activity to which the callbacks are scoped. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks callbacks` | the callbacks to get the status of phone number verification. The callbacks will be automatically removed when the specified activity has stopped. When a test phone number and sms code pair is set via `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthSettings#setAutoRetrievedSmsCodeForPhoneNumber(java.lang.String,java.lang.String)` and in the Firebase console, `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeAutoRetrievalTimeOut(java.lang.String)` will never be triggered. |
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken forceResendingToken` | the ForceResendingToken obtained from `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeSent(java.lang.String,com.google.firebase.auth.PhoneAuthProvider.ForceResendingToken)` callback to force re-sending another verification SMS before the auto-retrieval timeout. |