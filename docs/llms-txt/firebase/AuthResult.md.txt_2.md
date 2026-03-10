# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthResult.md.txt

# AuthResult

# AuthResult


```
interface AuthResult : Parcelable
```

<br />

*** ** * ** ***

Result object obtained from operations that can affect the authentication state. Contains a method that returns the currently signed-in user after the operation has completed.

## Summary

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AdditionalUserInfo?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthResult#getAdditionalUserInfo()()` Returns IDP-specific information for the user if the provider is one of Facebook, Github, Google, or Twitter. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthResult#getCredential()()` Returns an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` instance which may be used to obtain the IDP accessToken and/or IDToken pertaining to a recently signed-in user. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthResult#getUser()()` Returns the currently signed-in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser`, or `null` if there isn't any (i.e. the user is signed out). |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited functions |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#writeToParcel(android.os.Parcel, int)(p: https://developer.android.com/reference/android/os/Parcel.html!, p1: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | |

## Public functions

### getAdditionalUserInfo

```
fun getAdditionalUserInfo(): AdditionalUserInfo?
```

Returns IDP-specific information for the user if the provider is one of Facebook, Github, Google, or Twitter.

### getCredential

```
fun getCredential(): AuthCredential?
```

Returns an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` instance which may be used to obtain the IDP accessToken and/or IDToken pertaining to a recently signed-in user. May be `null`. For IDPs using OAuth, this will be an instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthCredential`.

### getUser

```
fun getUser(): FirebaseUser?
```

Returns the currently signed-in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser`, or `null` if there isn't any (i.e. the user is signed out).