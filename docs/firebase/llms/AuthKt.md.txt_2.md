# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthKt.md.txt

# AuthKt

# AuthKt


```
public final class AuthKt
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthKt#actionCodeSettings(kotlin.Function1)( @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` Returns an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings` instance initialized using the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/package-summary#actionCodeSettings(kotlin.Function1)` function. |
| `static final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthKt#(com.google.firebase.Firebase).auth(com.google.firebase.FirebaseApp)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase receiver, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app)` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `static final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthKt#(com.google.firebase.Firebase).getAuth()(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase receiver)` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `static final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthKt#oAuthCredential(kotlin.String,kotlin.Function1)( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html providerId, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.CredentialBuilder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` Returns an OAuth `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` instance initialized using the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/package-summary#oAuthCredential(kotlin.String,kotlin.Function1)` function. |
| `static final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthKt#oAuthProvider(kotlin.String,kotlin.Function1)( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html providerId, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` Returns an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider` instance initialized using the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/package-summary#oAuthProvider(kotlin.String,kotlin.Function1)` function. |
| `static final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthKt#oAuthProvider(kotlin.String,com.google.firebase.auth.FirebaseAuth,kotlin.Function1)( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html providerId, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth firebaseAuth, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` Returns an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider` instance initialized using the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/package-summary#oAuthProvider(kotlin.String,com.google.firebase.auth.FirebaseAuth,kotlin.Function1)` function. |
| `static final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthKt#userProfileChangeRequest(kotlin.Function1)( @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` Returns an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest` instance initialized using the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/package-summary#userProfileChangeRequest(kotlin.Function1)` function. |

## Public methods

### actionCodeSettings

```
public static final @NonNull ActionCodeSettings actionCodeSettings(
    @ExtensionFunctionType @NonNull Function1<@NonNull ActionCodeSettings.Builder, Unit> init
)
```

Returns an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings` instance initialized using the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/package-summary#actionCodeSettings(kotlin.Function1)` function.

### auth

```
public static final @NonNull FirebaseAuth auth(@NonNull Firebase receiver, @NonNull FirebaseApp app)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

### getAuth

```
public static final @NonNull FirebaseAuth getAuth(@NonNull Firebase receiver)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

### oAuthCredential

```
public static final @NonNull AuthCredential oAuthCredential(
    @NonNull String providerId,
    @ExtensionFunctionType @NonNull Function1<@NonNull OAuthProvider.CredentialBuilder, Unit> init
)
```

Returns an OAuth `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` instance initialized using the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/package-summary#oAuthCredential(kotlin.String,kotlin.Function1)` function.

### oAuthProvider

```
public static final @NonNull OAuthProvider oAuthProvider(
    @NonNull String providerId,
    @ExtensionFunctionType @NonNull Function1<@NonNull OAuthProvider.Builder, Unit> init
)
```

Returns an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider` instance initialized using the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/package-summary#oAuthProvider(kotlin.String,kotlin.Function1)` function.

### oAuthProvider

```
public static final @NonNull OAuthProvider oAuthProvider(
    @NonNull String providerId,
    @NonNull FirebaseAuth firebaseAuth,
    @ExtensionFunctionType @NonNull Function1<@NonNull OAuthProvider.Builder, Unit> init
)
```

Returns an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider` instance initialized using the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/package-summary#oAuthProvider(kotlin.String,com.google.firebase.auth.FirebaseAuth,kotlin.Function1)` function.

### userProfileChangeRequest

```
public static final @NonNull UserProfileChangeRequest userProfileChangeRequest(
    @ExtensionFunctionType @NonNull Function1<@NonNull UserProfileChangeRequest.Builder, Unit> init
)
```

Returns an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest` instance initialized using the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/package-summary#userProfileChangeRequest(kotlin.Function1)` function.