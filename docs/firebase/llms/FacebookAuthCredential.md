# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FacebookAuthCredential.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FacebookAuthCredential.md.txt

# FacebookAuthCredential

# FacebookAuthCredential


```
public class FacebookAuthCredential extends AuthCredential
```

<br />

|---|---|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [java.lang.Object](https://developer.android.com/reference/java/lang/Object.html)                                                                           |||
| â³ | [com.google.firebase.auth.AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential)                    ||
|   | â³ | [com.google.firebase.auth.FacebookAuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FacebookAuthCredential) |

*** ** * ** ***

Wraps a Facebook Login access token for authentication purposes.

## Summary

|                                                                                                                   ### Constants                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| `static final `[Parcelable.Creator](https://developer.android.com/reference/android/os/Parcelable.Creator.html)`<`[FacebookAuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FacebookAuthCredential)`>` | [CREATOR](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FacebookAuthCredential#CREATOR()) |

|                                                                        ### Public methods                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html) | [getProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FacebookAuthCredential#getProvider())`()` Returns the unique string identifier for the provider type with which the credential is associated.          |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html) | [getSignInMethod](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FacebookAuthCredential#getSignInMethod())`()` Returns the unique string identifier for the sign in method with which the credential is associated. |

|                                                                                                                                                                                                                                                                                          ### Inherited Constants                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |--------------------|-------------------------------------------------------------------------------------------------------------------------------------------| | `static final int` | [CONTENTS_FILE_DESCRIPTOR](https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR())` = 1`           | | `static final int` | [PARCELABLE_WRITE_RETURN_VALUE](https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE())` = 1` | |

|                                                                                                                                                                         ### Inherited methods                                                                                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |----------------|---------------------------------------------------------------------------------------------------------------| | `abstract int` | [describeContents](https://developer.android.com/reference/android/os/Parcelable.html#describeContents())`()` | |

## Constants

### CREATOR

```
publicÂ staticÂ finalÂ Parcelable.Creator<FacebookAuthCredential>Â CREATOR
```  

## Public methods

### getProvider

```
publicÂ @NonNull StringÂ getProvider()
```

Returns the unique string identifier for the provider type with which the credential is associated.  

### getSignInMethod

```
publicÂ @NonNull StringÂ getSignInMethod()
```

Returns the unique string identifier for the sign in method with which the credential is associated. Should match that returned by [fetchSignInMethodsForEmail](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#fetchSignInMethodsForEmail(java.lang.String)) after this user has signed in with this type of credential.