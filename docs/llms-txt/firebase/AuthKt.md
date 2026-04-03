# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ktx/AuthKt.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthKt.md.txt

# AuthKt

# AuthKt


```
public final class AuthKt
```

<br />

*** ** * ** ***

## Summary

|                                                                                                           ### Public methods                                                                                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[ActionCodeSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings)             | [actionCodeSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthKt#actionCodeSettings(kotlin.Function1))`(` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[ActionCodeSettings.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> init` `)` Returns an [ActionCodeSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings) instance initialized using the [init](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/package-summary#actionCodeSettings(kotlin.Function1)) function.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `static final @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[FirebaseAuth](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth)                         | [auth](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthKt#(com.google.firebase.Firebase).auth(com.google.firebase.FirebaseApp))`(@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Firebase](https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase)` receiver, @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app)` Returns the [FirebaseAuth](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth) instance of a given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `static final @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[FirebaseAuth](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth)                         | [getAuth](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthKt#(com.google.firebase.Firebase).getAuth())`(@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Firebase](https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase)` receiver)` Returns the [FirebaseAuth](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth) instance of the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `static final @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential)                     | [oAuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthKt#oAuthCredential(kotlin.String,kotlin.Function1))`(` ` @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)` providerId,` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[OAuthProvider.CredentialBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.CredentialBuilder)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> init` `)` Returns an OAuth [AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential) instance initialized using the [init](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/package-summary#oAuthCredential(kotlin.String,kotlin.Function1)) function.                                                                                                                                                                                                                                                              |
| `static final @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[OAuthProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider)                       | [oAuthProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthKt#oAuthProvider(kotlin.String,kotlin.Function1))`(` ` @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)` providerId,` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[OAuthProvider.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> init` `)` Returns an [OAuthProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider) instance initialized using the [init](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/package-summary#oAuthProvider(kotlin.String,kotlin.Function1)) function.                                                                                                                                                                                                                                                                                                |
| `static final @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[OAuthProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider)                       | [oAuthProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthKt#oAuthProvider(kotlin.String,com.google.firebase.auth.FirebaseAuth,kotlin.Function1))`(` ` @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)` providerId,` ` @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[FirebaseAuth](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth)` firebaseAuth,` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[OAuthProvider.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> init` `)` Returns an [OAuthProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider) instance initialized using the [init](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/package-summary#oAuthProvider(kotlin.String,com.google.firebase.auth.FirebaseAuth,kotlin.Function1)) function. |
| `static final @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[UserProfileChangeRequest](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest) | [userProfileChangeRequest](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthKt#userProfileChangeRequest(kotlin.Function1))`(` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[UserProfileChangeRequest.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest.Builder)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> init` `)` Returns an [UserProfileChangeRequest](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest) instance initialized using the [init](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/package-summary#userProfileChangeRequest(kotlin.Function1)) function.                                                                                                                                                                                                                                                                                                                                                                                                                               |

## Public methods

### actionCodeSettings

```
publicÂ staticÂ finalÂ @NonNull ActionCodeSettingsÂ actionCodeSettings(
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull ActionCodeSettings.Builder,Â Unit>Â init
)
```

Returns an [ActionCodeSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings) instance initialized using the [init](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/package-summary#actionCodeSettings(kotlin.Function1)) function.  

### auth

```
publicÂ staticÂ finalÂ @NonNull FirebaseAuthÂ auth(@NonNull FirebaseÂ receiver,Â @NonNull FirebaseAppÂ app)
```

Returns the [FirebaseAuth](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth) instance of a given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).  

### getAuth

```
publicÂ staticÂ finalÂ @NonNull FirebaseAuthÂ getAuth(@NonNull FirebaseÂ receiver)
```

Returns the [FirebaseAuth](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth) instance of the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).  

### oAuthCredential

```
publicÂ staticÂ finalÂ @NonNull AuthCredentialÂ oAuthCredential(
Â Â Â Â @NonNull StringÂ providerId,
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull OAuthProvider.CredentialBuilder,Â Unit>Â init
)
```

Returns an OAuth [AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential) instance initialized using the [init](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/package-summary#oAuthCredential(kotlin.String,kotlin.Function1)) function.  

### oAuthProvider

```
publicÂ staticÂ finalÂ @NonNull OAuthProviderÂ oAuthProvider(
Â Â Â Â @NonNull StringÂ providerId,
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull OAuthProvider.Builder,Â Unit>Â init
)
```

Returns an [OAuthProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider) instance initialized using the [init](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/package-summary#oAuthProvider(kotlin.String,kotlin.Function1)) function.  

### oAuthProvider

```
publicÂ staticÂ finalÂ @NonNull OAuthProviderÂ oAuthProvider(
Â Â Â Â @NonNull StringÂ providerId,
Â Â Â Â @NonNull FirebaseAuthÂ firebaseAuth,
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull OAuthProvider.Builder,Â Unit>Â init
)
```

Returns an [OAuthProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider) instance initialized using the [init](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/package-summary#oAuthProvider(kotlin.String,com.google.firebase.auth.FirebaseAuth,kotlin.Function1)) function.  

### userProfileChangeRequest

```
publicÂ staticÂ finalÂ @NonNull UserProfileChangeRequestÂ userProfileChangeRequest(
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull UserProfileChangeRequest.Builder,Â Unit>Â init
)
```

Returns an [UserProfileChangeRequest](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest) instance initialized using the [init](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/package-summary#userProfileChangeRequest(kotlin.Function1)) function.