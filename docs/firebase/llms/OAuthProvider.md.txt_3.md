# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.md.txt

# OAuthProvider

# OAuthProvider


```
class OAuthProvider : FederatedAuthProvider
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.auth.FederatedAuthProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FederatedAuthProvider) ||
|   | ↳ | [com.google.firebase.auth.OAuthProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider) |

*** ** * ** ***

Represents the login authentication provider for a generic OAuth2 provider. Use this class to obtain `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential`.

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder` Class used to create instances of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider`. |
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.CredentialBuilder` Builder class to initialize `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential`'s. |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` | `@https://errorprone.info/api/latest/com/google/errorprone/annotations/InlineMe.html(replacement = "DefaultOAuthCredential.createDefaultOAuthCredential(providerId, idToken, accessToken)", imports = "com.google.firebase.auth.DefaultOAuthCredential") [getCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider#getCredential(java.lang.String,java.lang.String,java.lang.String))(providerId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, idToken: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, accessToken: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` **This function is deprecated.** use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider#newCredentialBuilder(java.lang.String)` instead <br /> |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider#getProviderId()()` Returns the provider ID with which this OAuthProvider is associated. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider#newBuilder(java.lang.String)(providerId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder` used to construct a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider` instantiated with the given `providerId`. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider#newBuilder(java.lang.String,com.google.firebase.auth.FirebaseAuth)(providerId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, firebaseAuth: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth)` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder` used to construct a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider` instantiated with the given `providerId`. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.CredentialBuilder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider#newCredentialBuilder(java.lang.String)(providerId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.CredentialBuilder` for the specified provider ID. |

## Public functions

### getCredential

```
@InlineMe(replacement = "DefaultOAuthCredential.createDefaultOAuthCredential(providerId, idToken, accessToken)", imports = "com.google.firebase.auth.DefaultOAuthCredential")
java-static fun [getCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider#getCredential(java.lang.String,java.lang.String,java.lang.String))(providerId: String, idToken: String, accessToken: String): AuthCredential
```

> [!CAUTION]
> **This function is deprecated.**   
>
> use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider#newCredentialBuilder(java.lang.String)` instead

Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` that wraps a login token. Used when calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)`.

| Parameters |
|---|---|
| `accessToken: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | a valid Facebook Login access token, obtained from the Facebook Login SDK |

### getProviderId

```
fun getProviderId(): String?
```

Returns the provider ID with which this OAuthProvider is associated.

### newBuilder

```
java-static fun newBuilder(providerId: String): OAuthProvider.Builder
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder` used to construct a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider` instantiated with the given `providerId`.

### newBuilder

```
java-static fun newBuilder(providerId: String, firebaseAuth: FirebaseAuth): OAuthProvider.Builder
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder` used to construct a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider` instantiated with the given `providerId`. Uses the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth` instance.

### newCredentialBuilder

```
java-static fun newCredentialBuilder(providerId: String): OAuthProvider.CredentialBuilder
```

Creates an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.CredentialBuilder` for the specified provider ID.

| Throws |
|---|---|
| `https://developer.android.com/reference/java/lang/IllegalArgumentException.html` | if `providerId` is null or empty |