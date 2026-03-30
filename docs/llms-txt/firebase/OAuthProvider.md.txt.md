# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.md.txt

# OAuthProvider

# OAuthProvider


```
public class OAuthProvider extends FederatedAuthProvider
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/java/lang/Object.html) |||
| ↳ | [com.google.firebase.auth.FederatedAuthProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FederatedAuthProvider) ||
|   | ↳ | [com.google.firebase.auth.OAuthProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider) |

*** ** * ** ***

Represents the login authentication provider for a generic OAuth2 provider. Use this class to obtain `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential`.

## Summary

| ### Nested types |
|---|
| `public class https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder` Class used to create instances of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider`. |
| `public class https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.CredentialBuilder` Builder class to initialize `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential`'s. |

| ### Public methods |
|---|---|
| `static @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` | `@https://errorprone.info/api/latest/com/google/errorprone/annotations/InlineMe.html(replacement = "DefaultOAuthCredential.createDefaultOAuthCredential(providerId, idToken, accessToken)", imports = "com.google.firebase.auth.DefaultOAuthCredential") [getCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider#getCredential(java.lang.String,java.lang.String,java.lang.String))( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html providerId, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html idToken, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html accessToken )` **This method is deprecated.** use `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider#newCredentialBuilder(java.lang.String)` instead <br /> |
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider#getProviderId()()` Returns the provider ID with which this OAuthProvider is associated. |
| `static @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider#newBuilder(java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html providerId)` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder` used to construct a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider` instantiated with the given `providerId`. |
| `static @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider#newBuilder(java.lang.String,com.google.firebase.auth.FirebaseAuth)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html providerId, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth firebaseAuth)` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder` used to construct a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider` instantiated with the given `providerId`. |
| `static @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.CredentialBuilder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider#newCredentialBuilder(java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html providerId)` Creates an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.CredentialBuilder` for the specified provider ID. |

## Public methods

### getCredential

```
@InlineMe(replacement = "DefaultOAuthCredential.createDefaultOAuthCredential(providerId, idToken, accessToken)", imports = "com.google.firebase.auth.DefaultOAuthCredential")
public static @NonNull AuthCredential [getCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider#getCredential(java.lang.String,java.lang.String,java.lang.String))(
    @NonNull String providerId,
    @NonNull String idToken,
    @NonNull String accessToken
)
```

> [!CAUTION]
> **This method is deprecated.**   
>
> use `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider#newCredentialBuilder(java.lang.String)` instead

Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` that wraps a login token. Used when calling `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)` or `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html accessToken` | a valid Facebook Login access token, obtained from the Facebook Login SDK |

### getProviderId

```
public @Nullable String getProviderId()
```

Returns the provider ID with which this OAuthProvider is associated.

### newBuilder

```
public static @NonNull OAuthProvider.Builder newBuilder(@NonNull String providerId)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder` used to construct a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider` instantiated with the given `providerId`.

### newBuilder

```
public static @NonNull OAuthProvider.Builder newBuilder(@NonNull String providerId, @NonNull FirebaseAuth firebaseAuth)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder` used to construct a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider` instantiated with the given `providerId`. Uses the specified `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` instance.

### newCredentialBuilder

```
public static @NonNull OAuthProvider.CredentialBuilder newCredentialBuilder(@NonNull String providerId)
```

Creates an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.CredentialBuilder` for the specified provider ID.

| Throws |
|---|---|
| `https://developer.android.com/reference/java/lang/IllegalArgumentException.html` | if `providerId` is null or empty |