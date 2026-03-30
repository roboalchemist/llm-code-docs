# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FacebookAuthProvider.md.txt

# FacebookAuthProvider

# FacebookAuthProvider


```
class FacebookAuthProvider
```

<br />

*** ** * ** ***

Represents the Facebook Login authentication provider. Use this class to obtain s.

## Summary

| ### Constants |
|---|---|
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FacebookAuthProvider#FACEBOOK_SIGN_IN_METHOD() = "facebook.com"` Unique string identifier for Facebook sign-in method. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FacebookAuthProvider#PROVIDER_ID() = "facebook.com"` Unique string identifier for this provider type. |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FacebookAuthProvider#getCredential(java.lang.String)(accessToken: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` that wraps a Facebook Login token. |

## Constants

### FACEBOOK_SIGN_IN_METHOD

```
const val FACEBOOK_SIGN_IN_METHOD = "facebook.com": String!
```

Unique string identifier for Facebook sign-in method.

### PROVIDER_ID

```
const val PROVIDER_ID = "facebook.com": String!
```

Unique string identifier for this provider type.

## Public functions

### getCredential

```
java-static fun getCredential(accessToken: String): AuthCredential
```

Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` that wraps a Facebook Login token. Used when calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)`.

| Parameters |
|---|---|
| `accessToken: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | a valid Facebook Login access token, obtained from the Facebook Login SDK |