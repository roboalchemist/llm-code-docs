# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TwitterAuthProvider.md.txt

# TwitterAuthProvider

# TwitterAuthProvider


```
class TwitterAuthProvider
```

<br />

*** ** * ** ***

Represents the Twitter authentication provider. Use this class to obtain s.

## Summary

| ### Constants |
|---|---|
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TwitterAuthProvider#PROVIDER_ID() = "twitter.com"` Unique string identifier for this provider type. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TwitterAuthProvider#TWITTER_SIGN_IN_METHOD() = "twitter.com"` Unique string identifier for Twitter sign-in method. |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TwitterAuthProvider#getCredential(java.lang.String,java.lang.String)(token: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, secret: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` that wraps a Log in with Twitter token. |

## Constants

### PROVIDER_ID

```
const val PROVIDER_ID = "twitter.com": String!
```

Unique string identifier for this provider type.

### TWITTER_SIGN_IN_METHOD

```
const val TWITTER_SIGN_IN_METHOD = "twitter.com": String!
```

Unique string identifier for Twitter sign-in method.

## Public functions

### getCredential

```
java-static fun getCredential(token: String, secret: String): AuthCredential
```

Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` that wraps a Log in with Twitter token. Used when calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)`.

| Parameters |
|---|---|
| `token: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | a valid Log in with Twitter token (`TwitterAuthToken.token`), obtained from the Twitter Fabric SDK |
| `secret: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | a valid Log in with Twitter secret (`TwitterAuthToken.secret`), obtained from the Twitter Fabric SDK |