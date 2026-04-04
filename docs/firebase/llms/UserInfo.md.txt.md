# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserInfo.md.txt

# UserInfo

# UserInfo


```
public interface UserInfo
```

<br />

Known direct subclasses [FirebaseUser](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser)

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser` | Represents a user's profile information in your Firebase project's user database. |

*** ** * ** ***

Represents a collection of standard profile information for a user. Can be used to expose profile information returned by an identity provider, such as Google Sign-In or Facebook Login.

## Summary

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserInfo#getDisplayName()()` Returns the user's display name, if available. |
| `abstract @https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserInfo#getEmail()()` Returns the email address corresponding to the user's account in the specified provider, if available. |
| `abstract @https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserInfo#getPhoneNumber()()` Returns the phone number corresponding to the user's account, if available, or `null` if none exists. |
| `abstract @https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/android/net/Uri.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserInfo#getPhotoUrl()()` Returns a `https://developer.android.com/reference/android/net/Uri.html` to the user's profile picture, if available. |
| `abstract @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserInfo#getProviderId()()` Returns the unique identifier of the provider type that this instance corresponds to. |
| `abstract @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserInfo#getUid()()` Returns a user identifier as specified by the authentication provider. |
| `abstract boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserInfo#isEmailVerified()()` Returns `true` if the user's email is verified. |

## Public methods

### getDisplayName

```
abstract @Nullable String getDisplayName()
```

Returns the user's display name, if available.

### getEmail

```
abstract @Nullable String getEmail()
```

Returns the email address corresponding to the user's account in the specified provider, if available. Some authentication providers, like Twitter, do not contain an email address. Others, like Facebook Login, contain it optionally.

### getPhoneNumber

```
abstract @Nullable String getPhoneNumber()
```

Returns the phone number corresponding to the user's account, if available, or `null` if none exists.

### getPhotoUrl

```
abstract @Nullable Uri getPhotoUrl()
```

Returns a `https://developer.android.com/reference/android/net/Uri.html` to the user's profile picture, if available.

### getProviderId

```
abstract @NonNull String getProviderId()
```

Returns the unique identifier of the provider type that this instance corresponds to. For example, `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FacebookAuthProvider#PROVIDER_ID()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GoogleAuthProvider#PROVIDER_ID()`.

### getUid

```
abstract @NonNull String getUid()
```

Returns a user identifier as specified by the authentication provider. For example, if this object corresponds to a Google user, returns a Google user ID. For phone number accounts, the UID will be the normalized phone number in E.164 format.

### isEmailVerified

```
abstract boolean isEmailVerified()
```

Returns `true` if the user's email is verified.