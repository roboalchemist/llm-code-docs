# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GithubAuthCredential.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/GithubAuthCredential.md.txt

# GithubAuthCredential

# GithubAuthCredential


```
class GithubAuthCredential : AuthCredential
```

<br />

|---|---|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                      |||
| â³ | [com.google.firebase.auth.AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential)                ||
|   | â³ | [com.google.firebase.auth.GithubAuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/GithubAuthCredential) |

*** ** * ** ***

Wraps a Github OAuth access token for authentication purposes.

## Summary

|                                                                                                              ### Constants                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| `const `[Parcelable.Creator](https://developer.android.com/reference/android/os/Parcelable.Creator.html)`<`[GithubAuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/GithubAuthCredential)`!>!` | [CREATOR](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/GithubAuthCredential#CREATOR()) |

|                               ### Public functions                               |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [getProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/GithubAuthCredential#getProvider())`()` Returns the unique string identifier for the provider type with which the credential is associated.          |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [getSignInMethod](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/GithubAuthCredential#getSignInMethod())`()` Returns the unique string identifier for the sign in method with which the credential is associated. |

|                                                                                                                                                                                                                                                                                                                                                                                          ### Inherited Constants                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------| | `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [CONTENTS_FILE_DESCRIPTOR](https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR())` = 1`           | | `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [PARCELABLE_WRITE_RETURN_VALUE](https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE())` = 1` | |

|                                                                                                                                                                                                                                               ### Inherited functions                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------| | `abstract `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [describeContents](https://developer.android.com/reference/android/os/Parcelable.html#describeContents())`()` | |

## Constants

### CREATOR

```
constÂ valÂ CREATOR:Â Parcelable.Creator<GithubAuthCredential!>!
```  

## Public functions

### getProvider

```
funÂ getProvider():Â String
```

Returns the unique string identifier for the provider type with which the credential is associated.  

### getSignInMethod

```
funÂ getSignInMethod():Â String
```

Returns the unique string identifier for the sign in method with which the credential is associated. Should match that returned by [fetchSignInMethodsForEmail](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#fetchSignInMethodsForEmail(java.lang.String)) after this user has signed in with this type of credential.