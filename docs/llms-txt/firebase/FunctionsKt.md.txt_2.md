# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/functions/ktx/FunctionsKt.md.txt

# FunctionsKt

# FunctionsKt


```
public final class FunctionsKt
```

<br />

*** ** * ** ***

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/ktx/package-summary#(com.google.firebase.ktx.Firebase).functions()` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/ktx/FunctionsKt.https://firebase.google.com/docs/reference/android/com/google/firebase/functions/ktx/FunctionsKt#(com.google.firebase.ktx.Firebase).functions(com.google.firebase.FirebaseApp)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app )` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/ktx/FunctionsKt.https://firebase.google.com/docs/reference/android/com/google/firebase/functions/ktx/FunctionsKt#(com.google.firebase.ktx.Firebase).functions(kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html regionOrCustomDomain )` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/ktx/FunctionsKt.https://firebase.google.com/docs/reference/android/com/google/firebase/functions/ktx/FunctionsKt#(com.google.firebase.ktx.Firebase).functions(com.google.firebase.FirebaseApp,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html regionOrCustomDomain )` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/ktx/FunctionsKt.[getHttpsCallable](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/ktx/FunctionsKt#(com.google.firebase.functions.FirebaseFunctions).getHttpsCallable(kotlin.String,kotlin.Function1))( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/ktx/FunctionsKt.[getHttpsCallableFromUrl](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/ktx/FunctionsKt#(com.google.firebase.functions.FirebaseFunctions).getHttpsCallableFromUrl(java.net.URL,kotlin.Function1))( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/net/URL.html url, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Public fields

### functions

```
public final @NonNull FirebaseFunctions functions
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Public methods

### FunctionsKt.functions

```
public static final @NonNull FirebaseFunctions FunctionsKt.functions(
    @NonNull Firebase receiver,
    @NonNull FirebaseApp app
)
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### FunctionsKt.functions

```
public static final @NonNull FirebaseFunctions FunctionsKt.functions(
    @NonNull Firebase receiver,
    @NonNull String regionOrCustomDomain
)
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/ktx/package-summary#(com.google.firebase.ktx.Firebase).functions(kotlin.String)`.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### FunctionsKt.functions

```
public static final @NonNull FirebaseFunctions FunctionsKt.functions(
    @NonNull Firebase receiver,
    @NonNull FirebaseApp app,
    @NonNull String regionOrCustomDomain
)
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/ktx/package-summary#(com.google.firebase.ktx.Firebase).functions(com.google.firebase.FirebaseApp,kotlin.String)`.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### FunctionsKt.getHttpsCallable

```
public static final @NonNull HttpsCallableReference FunctionsKt.[getHttpsCallable](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/ktx/FunctionsKt#(com.google.firebase.functions.FirebaseFunctions).getHttpsCallable(kotlin.String,kotlin.Function1))(
    @NonNull FirebaseFunctions receiver,
    @NonNull String name,
    @ExtensionFunctionType @NonNull Function1<@NonNull HttpsCallableOptions.Builder, Unit> init
)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns a reference to the Callable HTTPS trigger with the given name and call options.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### FunctionsKt.getHttpsCallableFromUrl

```
public static final @NonNull HttpsCallableReference FunctionsKt.[getHttpsCallableFromUrl](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/ktx/FunctionsKt#(com.google.firebase.functions.FirebaseFunctions).getHttpsCallableFromUrl(java.net.URL,kotlin.Function1))(
    @NonNull FirebaseFunctions receiver,
    @NonNull URL url,
    @ExtensionFunctionType @NonNull Function1<@NonNull HttpsCallableOptions.Builder, Unit> init
)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns a reference to the Callable HTTPS trigger with the given URL and call options.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)