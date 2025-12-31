# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthCredential.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthCredential.md.txt

# EmailAuthCredential

# EmailAuthCredential


```
class EmailAuthCredential : AuthCredential
```

<br />

|---|---|------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                    |||
| â³ | [com.google.firebase.auth.AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential)              ||
|   | â³ | [com.google.firebase.auth.EmailAuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthCredential) |

*** ** * ** ***

Wraps an email and password tuple for authentication purposes.

## Summary

|                                                                                                             ### Constants                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| `const `[Parcelable.Creator](https://developer.android.com/reference/android/os/Parcelable.Creator.html)`<`[EmailAuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthCredential)`!>!` | [CREATOR](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthCredential#CREATOR()) |

|                               ### Public functions                               |
|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [getProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthCredential#getProvider())`()` Returns the unique string identifier for the provider type with which the credential is associated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [getSignInMethod](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthCredential#getSignInMethod())`()` Returns either [EMAIL_LINK_SIGN_IN_METHOD](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthProvider#EMAIL_LINK_SIGN_IN_METHOD()) for a credential generated with [getCredentialWithLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthProvider#getCredentialWithLink(java.lang.String,java.lang.String)) or [EMAIL_PASSWORD_SIGN_IN_METHOD](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthProvider#EMAIL_PASSWORD_SIGN_IN_METHOD()) for a credential generated with [getCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthProvider#getCredential(java.lang.String,java.lang.String)). |

|                                                                                                                                                                                                                                                                                                                                                                                          ### Inherited Constants                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------| | `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [CONTENTS_FILE_DESCRIPTOR](https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR())` = 1`           | | `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [PARCELABLE_WRITE_RETURN_VALUE](https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE())` = 1` | |

|                                                                                                                                                                                                                                               ### Inherited functions                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------| | `abstract `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [describeContents](https://developer.android.com/reference/android/os/Parcelable.html#describeContents())`()` | |

## Constants

### CREATOR

```
constÂ valÂ CREATOR:Â Parcelable.Creator<EmailAuthCredential!>!
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

Returns either [EMAIL_LINK_SIGN_IN_METHOD](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthProvider#EMAIL_LINK_SIGN_IN_METHOD()) for a credential generated with [getCredentialWithLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthProvider#getCredentialWithLink(java.lang.String,java.lang.String)) or [EMAIL_PASSWORD_SIGN_IN_METHOD](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthProvider#EMAIL_PASSWORD_SIGN_IN_METHOD()) for a credential generated with [getCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/EmailAuthProvider#getCredential(java.lang.String,java.lang.String)).