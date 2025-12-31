# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult.md.txt

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

|                                                  ### Public functions                                                  |
|------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AdditionalUserInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AdditionalUserInfo)`?` | [getAdditionalUserInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthResult#getAdditionalUserInfo())`()` Returns IDP-specific information for the user if the provider is one of Facebook, Github, Google, or Twitter.                                                                                                           |
| [AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential)`?`         | [getCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthResult#getCredential())`()` Returns an [AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential) instance which may be used to obtain the IDP accessToken and/or IDToken pertaining to a recently signed-in user. |
| [FirebaseUser](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser)`?`             | [getUser](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthResult#getUser())`()` Returns the currently signed-in [FirebaseUser](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser), or `null` if there isn't any (i.e. the user is signed out).                                                |

|                                                                                                                                                                                                                                                                                                                                                                                          ### Inherited Constants                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------| | `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [CONTENTS_FILE_DESCRIPTOR](https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR())` = 1`           | | `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [PARCELABLE_WRITE_RETURN_VALUE](https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE())` = 1` | |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ### Inherited functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)   | [describeContents](https://developer.android.com/reference/android/os/Parcelable.html#describeContents())`()`                                                                                                                                                                                 | | [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [writeToParcel](https://developer.android.com/reference/android/os/Parcelable.html#writeToParcel(android.os.Parcel, int))`(p: `[Parcel](https://developer.android.com/reference/android/os/Parcel.html)`!, p1: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`)` | |

## Public functions

### getAdditionalUserInfo

```
funÂ getAdditionalUserInfo():Â AdditionalUserInfo?
```

Returns IDP-specific information for the user if the provider is one of Facebook, Github, Google, or Twitter.  

### getCredential

```
funÂ getCredential():Â AuthCredential?
```

Returns an [AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential) instance which may be used to obtain the IDP accessToken and/or IDToken pertaining to a recently signed-in user. May be `null`. For IDPs using OAuth, this will be an instance of [OAuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthCredential).  

### getUser

```
funÂ getUser():Â FirebaseUser?
```

Returns the currently signed-in [FirebaseUser](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser), or `null` if there isn't any (i.e. the user is signed out).