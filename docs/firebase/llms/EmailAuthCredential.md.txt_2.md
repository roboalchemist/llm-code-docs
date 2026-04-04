# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthCredential.md.txt

# EmailAuthCredential

# EmailAuthCredential


```
class EmailAuthCredential : AuthCredential
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.auth.AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential) ||
|   | ↳ | [com.google.firebase.auth.EmailAuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthCredential) |

*** ** * ** ***

Wraps an email and password tuple for authentication purposes.

## Summary

| ### Constants |
|---|---|
| `const https://developer.android.com/reference/android/os/Parcelable.Creator.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthCredential!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthCredential#CREATOR()` |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthCredential#getProvider()()` Returns the unique string identifier for the provider type with which the credential is associated. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthCredential#getSignInMethod()()` Returns either `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthProvider#EMAIL_LINK_SIGN_IN_METHOD()` for a credential generated with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthProvider#getCredentialWithLink(java.lang.String,java.lang.String)` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthProvider#EMAIL_PASSWORD_SIGN_IN_METHOD()` for a credential generated with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthProvider#getCredential(java.lang.String,java.lang.String)`. |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited functions |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | |

## Constants

### CREATOR

```
const val CREATOR: Parcelable.Creator<EmailAuthCredential!>!
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

Returns either `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthProvider#EMAIL_LINK_SIGN_IN_METHOD()` for a credential generated with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthProvider#getCredentialWithLink(java.lang.String,java.lang.String)` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthProvider#EMAIL_PASSWORD_SIGN_IN_METHOD()` for a credential generated with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthProvider#getCredential(java.lang.String,java.lang.String)`.