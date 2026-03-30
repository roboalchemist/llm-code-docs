# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification.md.txt

# FirebasePhoneNumberVerification

# FirebasePhoneNumberVerification


```
interface FirebasePhoneNumberVerification
```

<br />

*** ** * ** ***

Entry point for Firebase Phone Number Verification.

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification#getInstance()()` Returns an instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification` using the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and its application context. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification#getInstance(android.content.Context)(context: https://developer.android.com/reference/android/content/Context.html)` Returns an instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification` for the given `https://developer.android.com/reference/android/content/Context.html` and the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification#getInstance(com.google.firebase.FirebaseApp)(firebaseApp: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` Returns an instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification` for the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification#getInstance(com.google.firebase.FirebaseApp,android.content.Context)(firebaseApp: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp, context: https://developer.android.com/reference/android/content/Context.html)` Returns an instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification` for the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and a `https://developer.android.com/reference/android/content/Context.html`. |

| ### Public functions |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification#exchangeCredentialResponseForPhoneNumber(kotlin.String)(dcApiResponse: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Completes the phone number verification process by exchanging a response from Credential Manager for a verified phone number token. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification#getDigitalCredentialPayload(kotlin.String)(nonce: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Prepares for a phone number verification flow by performing preflight checks and returning a digital credential payload for use with Android's Credential Manager. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportResult>>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification#getVerificationSupportInfo()()` Checks if phone number verification is supported for all SIMs. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportResult>>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification#getVerificationSupportInfo(kotlin.Int)(simSlot: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Checks if phone number verification is supported for a specific `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification#getVerificationSupportInfo(kotlin.Int)`. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification#getVerifiedPhoneNumber()()` Initiates the phone number verification process by getting a signed request, interacting with Credential Manager, and exchanging the response for a verified phone number token. |

## Public companion functions

### getInstance

```
fun getInstance(): FirebasePhoneNumberVerification
```

Returns an instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification` using the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and its application context.

Note that for methods that require an Activity context, using the result of this method will result in an `https://developer.android.com/reference/java/lang/IllegalArgumentException.html`.

### getInstance

```
fun getInstance(context: Context): FirebasePhoneNumberVerification
```

Returns an instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification` for the given `https://developer.android.com/reference/android/content/Context.html` and the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. Note that for methods that require an Activity context, providing a non-Activity context will result in an `https://developer.android.com/reference/java/lang/IllegalArgumentException.html`.

### getInstance

```
fun getInstance(firebaseApp: FirebaseApp): FirebasePhoneNumberVerification
```

Returns an instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification` for the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. It will be initialized with the application context.

Note that for methods that require an Activity context, using the result of this method will result in an `https://developer.android.com/reference/java/lang/IllegalArgumentException.html`.

### getInstance

```
fun getInstance(firebaseApp: FirebaseApp, context: Context): FirebasePhoneNumberVerification
```

Returns an instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification` for the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and a `https://developer.android.com/reference/android/content/Context.html`. The instance will be initialized with the provided `https://developer.android.com/reference/android/content/Context.html`. Note that for methods that require an Activity context, providing a non-Activity context will result in an `https://developer.android.com/reference/java/lang/IllegalArgumentException.html`.

## Public functions

### exchangeCredentialResponseForPhoneNumber

```
fun exchangeCredentialResponseForPhoneNumber(dcApiResponse: String): Task<VerifiedPhoneNumberTokenResult>
```

Completes the phone number verification process by exchanging a response from Credential Manager for a verified phone number token.

### getDigitalCredentialPayload

```
fun getDigitalCredentialPayload(nonce: String): Task<String>
```

Prepares for a phone number verification flow by performing preflight checks and returning a digital credential payload for use with Android's Credential Manager.

| Parameters |
|---|---|
| `nonce: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A unique string used to prevent replay attacks. screen. |

### getVerificationSupportInfo

```
fun getVerificationSupportInfo(): Task<List<VerificationSupportResult>>
```

Checks if phone number verification is supported for all SIMs.

This is a pre-check to determine if the verification flow is likely to succeed and does not require user consent.

The returned `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` completes with a list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportResult` objects containing information about verification support for all SIM slots.

### getVerificationSupportInfo

```
fun getVerificationSupportInfo(simSlot: Int): Task<List<VerificationSupportResult>>
```

Checks if phone number verification is supported for a specific `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification#getVerificationSupportInfo(kotlin.Int)`.

This is a pre-check to determine if the verification flow is likely to succeed and does not require user consent.

The returned `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` completes with a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportResult` object containing information about verification support for the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification#getVerificationSupportInfo(kotlin.Int)`.

Throws `https://developer.android.com/reference/java/lang/IllegalArgumentException.html` if the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/FirebasePhoneNumberVerification#getVerificationSupportInfo(kotlin.Int)` is not 0 or 1.

### getVerifiedPhoneNumber

```
fun getVerifiedPhoneNumber(): Task<VerifiedPhoneNumberTokenResult>
```

Initiates the phone number verification process by getting a signed request, interacting with Credential Manager, and exchanging the response for a verified phone number token. This function handles the entire end-to-end flow.