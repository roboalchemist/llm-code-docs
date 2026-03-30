# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult.md.txt

# AuthResult

# AuthResult


```
public interface AuthResult extends Parcelable
```

<br />

*** ** * ** ***

Result object obtained from operations that can affect the authentication state. Contains a method that returns the currently signed-in user after the operation has completed.

## Summary

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AdditionalUserInfo` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult#getAdditionalUserInfo()()` Returns IDP-specific information for the user if the provider is one of Facebook, Github, Google, or Twitter. |
| `abstract @https://developer.android.com/reference/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult#getCredential()()` Returns an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` instance which may be used to obtain the IDP accessToken and/or IDToken pertaining to a recently signed-in user. |
| `abstract @https://developer.android.com/reference/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult#getUser()()` Returns the currently signed-in `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser`, or `null` if there isn't any (i.e. the user is signed out). |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `default static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `default static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited methods |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `abstract int` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | | `abstract void` | `https://developer.android.com/reference/android/os/Parcelable.html#writeToParcel(android.os.Parcel, int)(https://developer.android.com/reference/android/os/Parcel.html p, int p1)` | |

## Public methods

### getAdditionalUserInfo

```
abstract @Nullable AdditionalUserInfo getAdditionalUserInfo()
```

Returns IDP-specific information for the user if the provider is one of Facebook, Github, Google, or Twitter.

### getCredential

```
abstract @Nullable AuthCredential getCredential()
```

Returns an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` instance which may be used to obtain the IDP accessToken and/or IDToken pertaining to a recently signed-in user. May be `null`. For IDPs using OAuth, this will be an instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthCredential`.

### getUser

```
abstract @Nullable FirebaseUser getUser()
```

Returns the currently signed-in `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser`, or `null` if there isn't any (i.e. the user is signed out).