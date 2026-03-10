# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification.md.txt

# FirebasePhoneNumberVerification

# FirebasePhoneNumberVerification


```
public interface FirebasePhoneNumberVerification
```

<br />

*** ** * ** ***

Entry point for Firebase Phone Number Verification.

## Summary

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification#exchangeCredentialResponseForPhoneNumber(kotlin.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html dcApiResponse)` Completes the phone number verification process by exchanging a response from Credential Manager for a verified phone number token. |
| `abstract @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification#getDigitalCredentialPayload(kotlin.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html nonce)` Prepares for a phone number verification flow by performing preflight checks and returning a digital credential payload for use with Android's Credential Manager. |
| `default static final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification#getInstance()()` Returns an instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification` using the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and its application context. |
| `default static final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification#getInstance(android.content.Context)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/android/content/Context.html context)` Returns an instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification` for the given `https://developer.android.com/reference/android/content/Context.html` and the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `default static final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification#getInstance(com.google.firebase.FirebaseApp)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp firebaseApp)` Returns an instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification` for the given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `default static final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification#getInstance(com.google.firebase.FirebaseApp,android.content.Context)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp firebaseApp, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/android/content/Context.html context)` Returns an instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification` for the given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and a `https://developer.android.com/reference/android/content/Context.html`. |
| `abstract @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/util/List.html<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerificationSupportResult>>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification#getVerificationSupportInfo()()` Checks if phone number verification is supported for all SIMs. |
| `abstract @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/util/List.html<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerificationSupportResult>>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification#getVerificationSupportInfo(kotlin.Int)(int simSlot)` Checks if phone number verification is supported for a specific `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification#getVerificationSupportInfo(kotlin.Int)`. |
| `abstract @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerifiedPhoneNumberTokenResult>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification#getVerifiedPhoneNumber()()` Initiates the phone number verification process by getting a signed request, interacting with Credential Manager, and exchanging the response for a verified phone number token. |

## Public methods

### exchangeCredentialResponseForPhoneNumber

```
abstract @NonNull Task<@NonNull VerifiedPhoneNumberTokenResult> exchangeCredentialResponseForPhoneNumber(@NonNull String dcApiResponse)
```

Completes the phone number verification process by exchanging a response from Credential Manager for a verified phone number token.

### getDigitalCredentialPayload

```
abstract @NonNull Task<@NonNull String> getDigitalCredentialPayload(@NonNull String nonce)
```

Prepares for a phone number verification flow by performing preflight checks and returning a digital credential payload for use with Android's Credential Manager.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html nonce` | A unique string used to prevent replay attacks. screen. |

### getInstance

```
default static final @NonNull FirebasePhoneNumberVerification getInstance()
```

Returns an instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification` using the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and its application context.

Note that for methods that require an Activity context, using the result of this method will result in an `https://developer.android.com/reference/java/lang/IllegalArgumentException.html`.

### getInstance

```
default static final @NonNull FirebasePhoneNumberVerification getInstance(@NonNull Context context)
```

Returns an instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification` for the given `https://developer.android.com/reference/android/content/Context.html` and the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. Note that for methods that require an Activity context, providing a non-Activity context will result in an `https://developer.android.com/reference/java/lang/IllegalArgumentException.html`.

### getInstance

```
default static final @NonNull FirebasePhoneNumberVerification getInstance(@NonNull FirebaseApp firebaseApp)
```

Returns an instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification` for the given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. It will be initialized with the application context.

Note that for methods that require an Activity context, using the result of this method will result in an `https://developer.android.com/reference/java/lang/IllegalArgumentException.html`.

### getInstance

```
default static final @NonNull FirebasePhoneNumberVerification getInstance(@NonNull FirebaseApp firebaseApp, @NonNull Context context)
```

Returns an instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification` for the given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and a `https://developer.android.com/reference/android/content/Context.html`. The instance will be initialized with the provided `https://developer.android.com/reference/android/content/Context.html`. Note that for methods that require an Activity context, providing a non-Activity context will result in an `https://developer.android.com/reference/java/lang/IllegalArgumentException.html`.

### getVerificationSupportInfo

```
abstract @NonNull Task<@NonNull List<@NonNull VerificationSupportResult>> getVerificationSupportInfo()
```

Checks if phone number verification is supported for all SIMs.

This is a pre-check to determine if the verification flow is likely to succeed and does not require user consent.

The returned `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` completes with a list of `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerificationSupportResult` objects containing information about verification support for all SIM slots.

### getVerificationSupportInfo

```
abstract @NonNull Task<@NonNull List<@NonNull VerificationSupportResult>> getVerificationSupportInfo(int simSlot)
```

Checks if phone number verification is supported for a specific `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification#getVerificationSupportInfo(kotlin.Int)`.

This is a pre-check to determine if the verification flow is likely to succeed and does not require user consent.

The returned `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` completes with a `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerificationSupportResult` object containing information about verification support for the specified `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification#getVerificationSupportInfo(kotlin.Int)`.

Throws `https://developer.android.com/reference/java/lang/IllegalArgumentException.html` if the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/FirebasePhoneNumberVerification#getVerificationSupportInfo(kotlin.Int)` is not 0 or 1.

### getVerifiedPhoneNumber

```
abstract @NonNull Task<@NonNull VerifiedPhoneNumberTokenResult> getVerifiedPhoneNumber()
```

Initiates the phone number verification process by getting a signed request, interacting with Credential Manager, and exchanging the response for a verified phone number token. This function handles the entire end-to-end flow.