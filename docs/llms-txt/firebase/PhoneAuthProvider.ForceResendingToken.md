# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken.md.txt

# PhoneAuthProvider.ForceResendingToken

# PhoneAuthProvider.ForceResendingToken


```
class PhoneAuthProvider.ForceResendingToken : Parcelable
```

<br />

*** ** * ** ***

A 'token' that can be used to force re-sending an SMS verification code. This token can be obtained in [onCodeSent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.OnVerificationStateChangedCallbacks#onCodeSent(java.lang.String,com.google.firebase.auth.PhoneAuthProvider.ForceResendingToken)) callback.

## Summary

|                                                                                                                               ### Constants                                                                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| `const `[Parcelable.Creator](https://developer.android.com/reference/android/os/Parcelable.Creator.html)`<`[PhoneAuthProvider.ForceResendingToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken)`!>!` | [CREATOR](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider.ForceResendingToken#CREATOR()) |

|                                                                                                                                                                                                                                                                                                                                                                                          ### Inherited Constants                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------| | `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [CONTENTS_FILE_DESCRIPTOR](https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR())` = 1`           | | `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [PARCELABLE_WRITE_RETURN_VALUE](https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE())` = 1` | |

|                                                                                                                                                                                                                                               ### Inherited functions                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------| | `abstract `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [describeContents](https://developer.android.com/reference/android/os/Parcelable.html#describeContents())`()` | |

## Constants

### CREATOR

```
constÂ valÂ CREATOR:Â Parcelable.Creator<PhoneAuthProvider.ForceResendingToken!>!
```