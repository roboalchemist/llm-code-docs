# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.CredentialBuilder.md.txt

# OAuthProvider.CredentialBuilder

# OAuthProvider.CredentialBuilder


```
public class OAuthProvider.CredentialBuilder
```

<br />

*** ** * ** ***

Builder class to initialize `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential`'s.

## Summary

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.CredentialBuilder#build()()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` that this `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.CredentialBuilder` has constructed. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.CredentialBuilder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.CredentialBuilder#setIdTokenWithRawNonce(java.lang.String,java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html idToken, @https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html rawNonce)` Adds an ID token and raw nonce to the credential being built. |

## Public methods

### build

```
public @NonNull AuthCredential build()
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` that this `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.CredentialBuilder` has constructed.

| Throws |
|---|---|
| `https://developer.android.com/reference/java/lang/IllegalArgumentException.html` | if an ID token and access token were not provided. |

### setIdTokenWithRawNonce

```
public @NonNull OAuthProvider.CredentialBuilder setIdTokenWithRawNonce(@NonNull String idToken, @Nullable String rawNonce)
```

Adds an ID token and raw nonce to the credential being built.

The raw nonce is required when an OIDC ID token with a nonce field is provided. The SHA-256 hash of the raw nonce must match the nonce field in the OIDC ID token.