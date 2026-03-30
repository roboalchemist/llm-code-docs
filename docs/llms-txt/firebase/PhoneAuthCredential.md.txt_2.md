# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthCredential.md.txt

# PhoneAuthCredential

# PhoneAuthCredential


```
class PhoneAuthCredential : AuthCredential, Cloneable
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.auth.AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential) ||
|   | ↳ | [com.google.firebase.auth.PhoneAuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthCredential) |

*** ** * ** ***

Wraps phone number and verification information for authentication purposes.

## Summary

| ### Constants |
|---|---|
| `const https://developer.android.com/reference/android/os/Parcelable.Creator.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthCredential!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthCredential#CREATOR()` |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthCredential#getProvider()()` Returns the unique string identifier for the provider type with which the credential is associated. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthCredential#getSignInMethod()()` Returns the unique string identifier for the sign in method with which the credential is associated. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthCredential#smsCode()` |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited functions |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | |

## Constants

### CREATOR

```
const val CREATOR: Parcelable.Creator<PhoneAuthCredential!>!
```

## Public functions

### getProvider

```
fun getProvider(): String
```

Returns the unique string identifier for the provider type with which the credential is associated.

### getSignInMethod

```
fun getSignInMethod(): String
```

Returns the unique string identifier for the sign in method with which the credential is associated. Should match that returned by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#fetchSignInMethodsForEmail(java.lang.String)` after this user has signed in with this type of credential.

## Public properties

### smsCode

```
val smsCode: String?
```