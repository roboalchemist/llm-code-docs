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

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorResolver#MultiFactorResolver()()` |

| ### Public functions |
|---|---|
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorResolver#getFirebaseAuth()()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth` reference for the current MultiFactorResolver. |
| `abstract (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorResolver#getHints()()` Returns a list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo` which represents the available second factors that can be used to complete the sign-in for the current session. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorSession` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorResolver#getSession()()` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorSession`, an opaque session identifier for the current sign-in flow. |
| `abstract https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthResult!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorResolver#resolveSignIn(com.google.firebase.auth.MultiFactorAssertion)(multiFactorAssertion: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorAssertion)` Completes sign in with a second factor using an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorAssertion` which confirms that the user has successfully completed the second factor challenge. |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited functions |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#writeToParcel(android.os.Parcel, int)(p: https://developer.android.com/reference/android/os/Parcel.html!, p1: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | |

## Public constructors

### MultiFactorResolver

```
MultiFactorResolver()
```

## Public functions

### getFirebaseAuth

```
abstract fun getFirebaseAuth(): FirebaseAuth
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth` reference for the current MultiFactorResolver.

### getHints

```
abstract fun getHints(): (Mutable)List<MultiFactorInfo!>
```

Returns a list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo` which represents the available second factors that can be used to complete the sign-in for the current session.

### getSession

```
abstract fun getSession(): MultiFactorSession
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorSession`, an opaque session identifier for the current sign-in flow.

This is needed to be provided with the second factor. It will provide context to the Auth backend on the first factor user to sign-in.

### resolveSignIn

```
abstract fun resolveSignIn(multiFactorAssertion: MultiFactorAssertion): Task<AuthResult!>
```

Completes sign in with a second factor using an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorAssertion` which confirms that the user has successfully completed the second factor challenge.