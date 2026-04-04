# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/GithubAuthProvider.md.txt

# GithubAuthProvider

# GithubAuthProvider


```
class GithubAuthProvider
```

<br />

*** ** * ** ***

Represents the Github authentication provider. Use this class to obtain s.

## Summary

| ### Constants |
|---|---|
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/GithubAuthProvider#GITHUB_SIGN_IN_METHOD() = "github.com"` Unique string identifier for Github sign-in method. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/GithubAuthProvider#PROVIDER_ID() = "github.com"` Unique string identifier for this provider type. |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/GithubAuthProvider#getCredential(java.lang.String)(token: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` that wraps a Github OAuth token. |

## Constants

### GITHUB_SIGN_IN_METHOD

```
const val GITHUB_SIGN_IN_METHOD = "github.com": String!
```

Unique string identifier for Github sign-in method.

### PROVIDER_ID

```
const val PROVIDER_ID = "github.com": String!
```

Unique string identifier for this provider type.

## Public functions

### getCredential

```
java-static fun getCredential(token: String): AuthCredential
```

Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` that wraps a Github OAuth token. Used when calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)`.

| Parameters |
|---|---|
| `token: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A valid Github OAuth access token, obtained from the Github OAuth flow |