# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ktx/AuthKt.md.txt

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
| `static final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings` | `[actionCodeSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ktx/AuthKt#actionCodeSettings(kotlin.Function1))( @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `static final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ktx/AuthKt#(com.google.firebase.ktx.Firebase).auth(com.google.firebase.FirebaseApp)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/Firebase receiver, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app)` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |
| `static final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ktx/AuthKt#(com.google.firebase.ktx.Firebase).getAuth()(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/Firebase receiver)` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |
| `static final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` | `[oAuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ktx/AuthKt#oAuthCredential(kotlin.String,kotlin.Function1))( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html providerId, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.CredentialBuilder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `static final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider` | `[oAuthProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ktx/AuthKt#oAuthProvider(kotlin.String,kotlin.Function1))( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html providerId, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `static final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider` | `[oAuthProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ktx/AuthKt#oAuthProvider(kotlin.String,com.google.firebase.auth.FirebaseAuth,kotlin.Function1))( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html providerId, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth firebaseAuth, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `static final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest` | `[userProfileChangeRequest](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ktx/AuthKt#userProfileChangeRequest(kotlin.Function1))( @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Public methods

### actionCodeSettings

```
public static final @NonNull ActionCodeSettings [actionCodeSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ktx/AuthKt#actionCodeSettings(kotlin.Function1))(
    @ExtensionFunctionType @NonNull Function1<@NonNull ActionCodeSettings.Builder, Unit> init
)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings` instance initialized using the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ktx/package-summary#actionCodeSettings(kotlin.Function1)` function.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### auth

```
public static final @NonNull FirebaseAuth auth(@NonNull Firebase receiver, @NonNull FirebaseApp app)
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### getAuth

```
public static final @NonNull FirebaseAuth getAuth(@NonNull Firebase receiver)
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### oAuthCredential

```
public static final @NonNull AuthCredential [oAuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ktx/AuthKt#oAuthCredential(kotlin.String,kotlin.Function1))(
    @NonNull String providerId,
    @ExtensionFunctionType @NonNull Function1<@NonNull OAuthProvider.CredentialBuilder, Unit> init
)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns an OAuth `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` instance initialized using the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ktx/package-summary#oAuthCredential(kotlin.String,kotlin.Function1)` function.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### oAuthProvider

```
public static final @NonNull OAuthProvider [oAuthProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ktx/AuthKt#oAuthProvider(kotlin.String,kotlin.Function1))(
    @NonNull String providerId,
    @ExtensionFunctionType @NonNull Function1<@NonNull OAuthProvider.Builder, Unit> init
)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider` instance initialized using the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ktx/package-summary#oAuthProvider(kotlin.String,kotlin.Function1)` function.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### oAuthProvider

```
public static final @NonNull OAuthProvider [oAuthProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ktx/AuthKt#oAuthProvider(kotlin.String,com.google.firebase.auth.FirebaseAuth,kotlin.Function1))(
    @NonNull String providerId,
    @NonNull FirebaseAuth firebaseAuth,
    @ExtensionFunctionType @NonNull Function1<@NonNull OAuthProvider.Builder, Unit> init
)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider` instance initialized using the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ktx/package-summary#oAuthProvider(kotlin.String,com.google.firebase.auth.FirebaseAuth,kotlin.Function1)` function.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### userProfileChangeRequest

```
public static final @NonNull UserProfileChangeRequest [userProfileChangeRequest](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ktx/AuthKt#userProfileChangeRequest(kotlin.Function1))(
    @ExtensionFunctionType @NonNull Function1<@NonNull UserProfileChangeRequest.Builder, Unit> init
)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest` instance initialized using the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ktx/package-summary#userProfileChangeRequest(kotlin.Function1)` function.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)