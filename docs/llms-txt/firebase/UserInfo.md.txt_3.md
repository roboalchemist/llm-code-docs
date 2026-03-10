# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserInfo.md.txt

# UserInfo

# UserInfo


```
interface UserInfo
```

<br />

Known direct subclasses [FirebaseUser](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser` | Represents a user's profile information in your Firebase project's user database. |

*** ** * ** ***

Represents a collection of standard profile information for a user. Can be used to expose profile information returned by an identity provider, such as Google Sign-In or Facebook Login.

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserInfo#getDisplayName()()` Returns the user's display name, if available. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserInfo#getEmail()()` Returns the email address corresponding to the user's account in the specified provider, if available. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserInfo#getPhoneNumber()()` Returns the phone number corresponding to the user's account, if available, or `null` if none exists. |
| `https://developer.android.com/reference/android/net/Uri.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserInfo#getPhotoUrl()()` Returns a `https://developer.android.com/reference/android/net/Uri.html` to the user's profile picture, if available. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserInfo#getProviderId()()` Returns the unique identifier of the provider type that this instance corresponds to. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserInfo#getUid()()` Returns a user identifier as specified by the authentication provider. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserInfo#isEmailVerified()()` Returns `true` if the user's email is verified. |

## Public functions

### getDisplayName

```
fun getDisplayName(): String?
```

Returns the user's display name, if available.

### getEmail

```
fun getEmail(): String?
```

Returns the email address corresponding to the user's account in the specified provider, if available. Some authentication providers, like Twitter, do not contain an email address. Others, like Facebook Login, contain it optionally.

### getPhoneNumber

```
fun getPhoneNumber(): String?
```

Returns the phone number corresponding to the user's account, if available, or `null` if none exists.

### getPhotoUrl

```
fun getPhotoUrl(): Uri?
```

Returns a `https://developer.android.com/reference/android/net/Uri.html` to the user's profile picture, if available.

### getProviderId

```
fun getProviderId(): String
```

Returns the unique identifier of the provider type that this instance corresponds to. For example, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FacebookAuthProvider#PROVIDER_ID()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/GoogleAuthProvider#PROVIDER_ID()`.

### getUid

```
fun getUid(): String
```

Returns a user identifier as specified by the authentication provider. For example, if this object corresponds to a Google user, returns a Google user ID. For phone number accounts, the UID will be the normalized phone number in E.164 format.

### isEmailVerified

```
fun isEmailVerified(): Boolean
```

Returns `true` if the user's email is verified.