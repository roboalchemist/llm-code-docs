# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorResolver.md.txt

# MultiFactorResolver

# MultiFactorResolver


```
public abstract class MultiFactorResolver implements Parcelable
```

<br />

*** ** * ** ***

Utility class that contains methods to resolve second factor requirements on users that have opted into two-factor authentication.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorResolver#MultiFactorResolver()()` |

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorResolver#getFirebaseAuth()()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` reference for the current MultiFactorResolver. |
| `abstract @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/util/List.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorResolver#getHints()()` Returns a list of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo` which represents the available second factors that can be used to complete the sign-in for the current session. |
| `abstract @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorSession` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorResolver#getSession()()` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorSession`, an opaque session identifier for the current sign-in flow. |
| `abstract @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorResolver#resolveSignIn(com.google.firebase.auth.MultiFactorAssertion)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorAssertion multiFactorAssertion)` Completes sign in with a second factor using an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorAssertion` which confirms that the user has successfully completed the second factor challenge. |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited methods |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `abstract int` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | | `abstract void` | `https://developer.android.com/reference/android/os/Parcelable.html#writeToParcel(android.os.Parcel, int)(https://developer.android.com/reference/android/os/Parcel.html p, int p1)` | |

## Public constructors

### MultiFactorResolver

```
public MultiFactorResolver()
```

## Public methods

### getFirebaseAuth

```
public abstract @NonNull FirebaseAuth getFirebaseAuth()
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` reference for the current MultiFactorResolver.

### getHints

```
public abstract @NonNull List<MultiFactorInfo> getHints()
```

Returns a list of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo` which represents the available second factors that can be used to complete the sign-in for the current session.

### getSession

```
public abstract @NonNull MultiFactorSession getSession()
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorSession`, an opaque session identifier for the current sign-in flow.

This is needed to be provided with the second factor. It will provide context to the Auth backend on the first factor user to sign-in.

### resolveSignIn

```
public abstract @NonNull Task<AuthResult> resolveSignIn(@NonNull MultiFactorAssertion multiFactorAssertion)
```

Completes sign in with a second factor using an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorAssertion` which confirms that the user has successfully completed the second factor challenge.