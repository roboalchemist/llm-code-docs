# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.CredentialBuilder.md.txt

# OAuthProvider.CredentialBuilder

# OAuthProvider.CredentialBuilder


```
class OAuthProvider.CredentialBuilder
```

<br />

*** ** * ** ***

Builder class to initialize `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential`'s.

## Summary

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.CredentialBuilder#build()()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` that this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.CredentialBuilder` has constructed. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.CredentialBuilder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.CredentialBuilder#setIdTokenWithRawNonce(java.lang.String,java.lang.String)(idToken: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, rawNonce: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Adds an ID token and raw nonce to the credential being built. |

## Public functions

### build

```
fun build(): AuthCredential
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` that this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.CredentialBuilder` has constructed.

| Throws |
|---|---|
| `https://developer.android.com/reference/java/lang/IllegalArgumentException.html` | if an ID token and access token were not provided. |

### setIdTokenWithRawNonce

```
fun setIdTokenWithRawNonce(idToken: String, rawNonce: String?): OAuthProvider.CredentialBuilder
```

Adds an ID token and raw nonce to the credential being built.

The raw nonce is required when an OIDC ID token with a nonce field is provided. The SHA-256 hash of the raw nonce must match the nonce field in the OIDC ID token.