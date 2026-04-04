# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PlayGamesAuthCredential.md.txt

# PlayGamesAuthCredential

# PlayGamesAuthCredential


```
class PlayGamesAuthCredential : AuthCredential
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.auth.AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential) ||
|   | ↳ | [com.google.firebase.auth.PlayGamesAuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PlayGamesAuthCredential) |

*** ** * ** ***

Wraps a Google Play Games Server Auth Code, for authentication purposes.

## Summary

| ### Constants |
|---|---|
| `const https://developer.android.com/reference/android/os/Parcelable.Creator.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PlayGamesAuthCredential!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PlayGamesAuthCredential#CREATOR()` |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PlayGamesAuthCredential#getProvider()()` Returns the unique string identifier for the provider type with which the credential is associated. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PlayGamesAuthCredential#getSignInMethod()()` Returns the unique string identifier for the sign in method with which the credential is associated. |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited functions |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | |

## Constants

### CREATOR

```
const val CREATOR: Parcelable.Creator<PlayGamesAuthCredential!>!
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