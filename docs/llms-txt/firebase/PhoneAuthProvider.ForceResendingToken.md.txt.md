# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken.md.txt

# PhoneAuthProvider.ForceResendingToken

# PhoneAuthProvider.ForceResendingToken


```
public class PhoneAuthProvider.ForceResendingToken implements Parcelable
```

<br />

*** ** * ** ***

A 'token' that can be used to force re-sending an SMS verification code. This token can be obtained in `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeSent(java.lang.String,com.google.firebase.auth.PhoneAuthProvider.ForceResendingToken)` callback.

## Summary

| ### Constants |
|---|---|
| `static final https://developer.android.com/reference/android/os/Parcelable.Creator.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken#CREATOR()` |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited methods |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `abstract int` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | |

## Constants

### CREATOR

```
public static final Parcelable.Creator<PhoneAuthProvider.ForceResendingToken> CREATOR
```