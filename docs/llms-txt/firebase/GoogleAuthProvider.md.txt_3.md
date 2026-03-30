# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/GoogleAuthProvider.md.txt

# GoogleAuthProvider

# GoogleAuthProvider


```
class GoogleAuthProvider
```

<br />

*** ** * ** ***

Represents the Google Sign-In authentication provider. Use this class to obtain s.

## Summary

| ### Constants |
|---|---|
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/GoogleAuthProvider#GOOGLE_SIGN_IN_METHOD() = "google.com"` Unique string identifier for Google sign-in method. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/GoogleAuthProvider#PROVIDER_ID() = "google.com"` Unique string identifier for this provider type. |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/GoogleAuthProvider#getCredential(java.lang.String,java.lang.String)(idToken: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, accessToken: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` that wraps Google Sign-In ID or access tokens. |

## Constants

### GOOGLE_SIGN_IN_METHOD

```
const val GOOGLE_SIGN_IN_METHOD = "google.com": String!
```

Unique string identifier for Google sign-in method.

### PROVIDER_ID

```
const val PROVIDER_ID = "google.com": String!
```

Unique string identifier for this provider type.

## Public functions

### getCredential

```
java-static fun getCredential(idToken: String?, accessToken: String?): AuthCredential
```

Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` that wraps Google Sign-In ID or access tokens. Used when calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)`.

Both parameters are optional but at least one must be present.

| Parameters |
|---|---|
| `idToken: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | a valid Google Sign-In id token, obtained from the Google Sign-In SDK |
| `accessToken: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | a valid Google Sign-In access token, obtained from the Google Sign-In SDK |