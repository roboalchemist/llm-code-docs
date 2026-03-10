# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthCredential.md.txt

# EmailAuthCredential

# EmailAuthCredential


```
public class EmailAuthCredential extends AuthCredential
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/java/lang/Object.html) |||
| ↳ | [com.google.firebase.auth.AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential) ||
|   | ↳ | [com.google.firebase.auth.EmailAuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthCredential) |

*** ** * ** ***

Wraps an email and password tuple for authentication purposes.

## Summary

| ### Constants |
|---|---|
| `static final https://developer.android.com/reference/android/os/Parcelable.Creator.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthCredential>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthCredential#CREATOR()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthCredential#getProvider()()` Returns the unique string identifier for the provider type with which the credential is associated. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthCredential#getSignInMethod()()` Returns either `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthProvider#EMAIL_LINK_SIGN_IN_METHOD()` for a credential generated with `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthProvider#getCredentialWithLink(java.lang.String,java.lang.String)` or `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthProvider#EMAIL_PASSWORD_SIGN_IN_METHOD()` for a credential generated with `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthProvider#getCredential(java.lang.String,java.lang.String)`. |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited methods |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `abstract int` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | |

## Constants

### CREATOR

```
public static final Parcelable.Creator<EmailAuthCredential> CREATOR
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

Returns either `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthProvider#EMAIL_LINK_SIGN_IN_METHOD()` for a credential generated with `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthProvider#getCredentialWithLink(java.lang.String,java.lang.String)` or `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthProvider#EMAIL_PASSWORD_SIGN_IN_METHOD()` for a credential generated with `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthProvider#getCredential(java.lang.String,java.lang.String)`.