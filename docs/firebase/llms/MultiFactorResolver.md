# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorResolver.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorResolver.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorResolver.md.txt

# MultiFactorResolver

# MultiFactorResolver


```
abstract class MultiFactorResolver : Parcelable
```

<br />

*** ** * ** ***

Utility class that contains methods to resolve second factor requirements on users that have opted into two-factor authentication.

## Summary

|                                                             ### Public constructors                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [MultiFactorResolver](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorResolver#MultiFactorResolver())`()` |

|                                                                                                                                                      ### Public functions                                                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `abstract `[FirebaseAuth](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth)                                                                                                                                                                                                             | [getFirebaseAuth](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorResolver#getFirebaseAuth())`()` Returns the [FirebaseAuth](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth) reference for the current MultiFactorResolver.                                                                                                                                                                                                                                                                                   |
| `abstract (`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)`)`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[MultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo)`!>` | [getHints](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorResolver#getHints())`()` Returns a list of [MultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo) which represents the available second factors that can be used to complete the sign-in for the current session.                                                                                                                                                                                                                    |
| `abstract `[MultiFactorSession](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorSession)                                                                                                                                                                                                 | [getSession](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorResolver#getSession())`()` Returns a [MultiFactorSession](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorSession), an opaque session identifier for the current sign-in flow.                                                                                                                                                                                                                                                                      |
| `abstract `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[AuthResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthResult)`!>`                                                                                                            | [resolveSignIn](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorResolver#resolveSignIn(com.google.firebase.auth.MultiFactorAssertion))`(multiFactorAssertion: `[MultiFactorAssertion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorAssertion)`)` Completes sign in with a second factor using an [MultiFactorAssertion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorAssertion) which confirms that the user has successfully completed the second factor challenge. |

|                                                                                                                                                                                                                                                                                                                                                                                          ### Inherited Constants                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------| | `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [CONTENTS_FILE_DESCRIPTOR](https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR())` = 1`           | | `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [PARCELABLE_WRITE_RETURN_VALUE](https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE())` = 1` | |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ### Inherited functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `abstract `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)   | [describeContents](https://developer.android.com/reference/android/os/Parcelable.html#describeContents())`()`                                                                                                                                                                                 | | `abstract `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [writeToParcel](https://developer.android.com/reference/android/os/Parcelable.html#writeToParcel(android.os.Parcel, int))`(p: `[Parcel](https://developer.android.com/reference/android/os/Parcel.html)`!, p1: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`)` | |

## Public constructors

### MultiFactorResolver

```
MultiFactorResolver()
```  

## Public functions

### getFirebaseAuth

```
abstractÂ funÂ getFirebaseAuth():Â FirebaseAuth
```

Returns the [FirebaseAuth](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth) reference for the current MultiFactorResolver.  

### getHints

```
abstractÂ funÂ getHints():Â (Mutable)List<MultiFactorInfo!>
```

Returns a list of [MultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo) which represents the available second factors that can be used to complete the sign-in for the current session.  

### getSession

```
abstractÂ funÂ getSession():Â MultiFactorSession
```

Returns a [MultiFactorSession](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorSession), an opaque session identifier for the current sign-in flow.

This is needed to be provided with the second factor. It will provide context to the Auth backend on the first factor user to sign-in.  

### resolveSignIn

```
abstractÂ funÂ resolveSignIn(multiFactorAssertion:Â MultiFactorAssertion):Â Task<AuthResult!>
```

Completes sign in with a second factor using an [MultiFactorAssertion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorAssertion) which confirms that the user has successfully completed the second factor challenge.