# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthCredential.md.txt

# PhoneAuthCredential

# PhoneAuthCredential


```
public class PhoneAuthCredential extends AuthCredential implements Cloneable
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/java/lang/Object.html) |||
| ↳ | [com.google.firebase.auth.AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential) ||
|   | ↳ | [com.google.firebase.auth.PhoneAuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthCredential) |

*** ** * ** ***

Wraps phone number and verification information for authentication purposes.

## Summary

| ### Constants |
|---|---|
| `static final https://developer.android.com/reference/android/os/Parcelable.Creator.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthCredential>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthCredential#CREATOR()` |

| ### Public fields |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthCredential#smsCode()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthCredential#getProvider()()` Returns the unique string identifier for the provider type with which the credential is associated. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthCredential#getSignInMethod()()` Returns the unique string identifier for the sign in method with which the credential is associated. |
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthCredential#getSmsCode()()` Gets the auto-retrieved SMS verification code if applicable. |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited methods |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `abstract int` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | |

## Constants

### CREATOR

```
public static final Parcelable.Creator<PhoneAuthCredential> CREATOR
```

## Public fields

### smsCode

```
public @Nullable String smsCode
```

## Public methods

### getProvider

```
public @NonNull String getProvider()
```

Returns the unique string identifier for the provider type with which the credential is associated.

### getSignInMethod

```
public @NonNull String getSignInMethod()
```

Returns the unique string identifier for the sign in method with which the credential is associated. Should match that returned by `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#fetchSignInMethodsForEmail(java.lang.String)` after this user has signed in with this type of credential.

### getSmsCode

```
public @Nullable String getSmsCode()
```

Gets the auto-retrieved SMS verification code if applicable. When SMS verification is used, you will be called back first via `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeSent(java.lang.String,com.google.firebase.auth.PhoneAuthProvider.ForceResendingToken)`, and later `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onVerificationCompleted(com.google.firebase.auth.PhoneAuthCredential)` with a containing a non-null SMS code if auto-retrieval succeeded. If Firebase used another approach to verify the phone number and triggers a callback via `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onVerificationCompleted(com.google.firebase.auth.PhoneAuthCredential)`, then SMS code can be `null`.