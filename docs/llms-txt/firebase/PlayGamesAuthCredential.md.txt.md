# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PlayGamesAuthCredential.md.txt

# PlayGamesAuthCredential

# PlayGamesAuthCredential


```
public class PlayGamesAuthCredential extends AuthCredential
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/java/lang/Object.html) |||
| ↳ | [com.google.firebase.auth.AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential) ||
|   | ↳ | [com.google.firebase.auth.PlayGamesAuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PlayGamesAuthCredential) |

*** ** * ** ***

Wraps a Google Play Games Server Auth Code, for authentication purposes.

## Summary

| ### Constants |
|---|---|
| `static final https://developer.android.com/reference/android/os/Parcelable.Creator.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PlayGamesAuthCredential>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PlayGamesAuthCredential#CREATOR()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PlayGamesAuthCredential#getProvider()()` Returns the unique string identifier for the provider type with which the credential is associated. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PlayGamesAuthCredential#getSignInMethod()()` Returns the unique string identifier for the sign in method with which the credential is associated. |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited methods |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `abstract int` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | |

## Constants

### CREATOR

```
public static final Parcelable.Creator<PlayGamesAuthCredential> CREATOR
```

## Public methods

### getProvider

```
public @NonNull String getProvider()
```

Returns the unique string identifier for the provider type with which the credential is associated.

### getSignInMethod

```
public @NonNull String getSignInMethod()
```

Returns the unique string identifier for the sign in method with which the credential is associated. Should match that returned by `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#fetchSignInMethodsForEmail(java.lang.String)` after this user has signed in with this type of credential.