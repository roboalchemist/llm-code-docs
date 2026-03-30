# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ktx/package-summary.md.txt

# com.google.firebase.auth.ktx

# com.google.firebase.auth.ktx

## Top-level functions summary

|---|---|
| `inline https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings` | `[actionCodeSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ktx/package-summary#actionCodeSettings(kotlin.Function1))(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `inline https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` | `[oAuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ktx/package-summary#oAuthCredential(kotlin.String,kotlin.Function1))(providerId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.CredentialBuilder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `inline https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider` | `[oAuthProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ktx/package-summary#oAuthProvider(kotlin.String,kotlin.Function1))(providerId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `inline https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider` | `[oAuthProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ktx/package-summary#oAuthProvider(kotlin.String,com.google.firebase.auth.FirebaseAuth,kotlin.Function1))( providerId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, firebaseAuth: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth, init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html )` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `inline https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserProfileChangeRequest` | `[userProfileChangeRequest](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ktx/package-summary#userProfileChangeRequest(kotlin.Function1))(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserProfileChangeRequest.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Extension functions summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ktx/package-summary#(com.google.firebase.ktx.Firebase).auth(com.google.firebase.FirebaseApp)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |

## Extension properties summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ktx/package-summary#(com.google.firebase.ktx.Firebase).auth()` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |

## Top-level functions

### actionCodeSettings

```
inline fun [actionCodeSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ktx/package-summary#actionCodeSettings(kotlin.Function1))(init: ActionCodeSettings.Builder.() -> Unit): ActionCodeSettings
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings` instance initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ktx/package-summary#actionCodeSettings(kotlin.Function1)` function.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### oAuthCredential

```
inline fun [oAuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ktx/package-summary#oAuthCredential(kotlin.String,kotlin.Function1))(providerId: String, init: OAuthProvider.CredentialBuilder.() -> Unit): AuthCredential
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns an OAuth `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` instance initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ktx/package-summary#oAuthCredential(kotlin.String,kotlin.Function1)` function.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### oAuthProvider

```
inline fun [oAuthProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ktx/package-summary#oAuthProvider(kotlin.String,kotlin.Function1))(providerId: String, init: OAuthProvider.Builder.() -> Unit): OAuthProvider
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider` instance initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ktx/package-summary#oAuthProvider(kotlin.String,kotlin.Function1)` function.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### oAuthProvider

```
inline fun [oAuthProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ktx/package-summary#oAuthProvider(kotlin.String,com.google.firebase.auth.FirebaseAuth,kotlin.Function1))(
    providerId: String,
    firebaseAuth: FirebaseAuth,
    init: OAuthProvider.Builder.() -> Unit
): OAuthProvider
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider` instance initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ktx/package-summary#oAuthProvider(kotlin.String,com.google.firebase.auth.FirebaseAuth,kotlin.Function1)` function.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### userProfileChangeRequest

```
inline fun [userProfileChangeRequest](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ktx/package-summary#userProfileChangeRequest(kotlin.Function1))(init: UserProfileChangeRequest.Builder.() -> Unit): UserProfileChangeRequest
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserProfileChangeRequest` instance initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ktx/package-summary#userProfileChangeRequest(kotlin.Function1)` function.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Extension functions

### auth

```
fun Firebase.auth(app: FirebaseApp): FirebaseAuth
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Extension properties

### auth

```
val Firebase.auth: FirebaseAuth
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)