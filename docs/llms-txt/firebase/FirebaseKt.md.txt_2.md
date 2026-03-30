# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/FirebaseKt.md.txt

# FirebaseKt

# FirebaseKt


```
public final class FirebaseKt
```

<br />

*** ** * ** ***

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/package-summary#(com.google.firebase.ktx.Firebase).app()` Accessing this object for Kotlin apps has changed; see the migration guide: https://firebase.google.com/docs/android/kotlin-migration. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/package-summary#(com.google.firebase.ktx.Firebase).options()` Accessing this object for Kotlin apps has changed; see the migration guide: https://firebase.google.com/docs/android/kotlin-migration. |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/FirebaseKt.https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/FirebaseKt#(com.google.firebase.ktx.Firebase).app(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name)` Accessing this object for Kotlin apps has changed; see the migration guide: https://firebase.google.com/docs/android/kotlin-migration. |
| `static final https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/FirebaseKt.[initialize](https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/FirebaseKt#(com.google.firebase.ktx.Firebase).initialize(android.content.Context))( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/content/Context.html context )` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/FirebaseKt.[initialize](https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/FirebaseKt#(com.google.firebase.ktx.Firebase).initialize(android.content.Context,com.google.firebase.FirebaseOptions))( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/content/Context.html context, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions options )` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/FirebaseKt.[initialize](https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/FirebaseKt#(com.google.firebase.ktx.Firebase).initialize(android.content.Context,com.google.firebase.FirebaseOptions,kotlin.String))( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/content/Context.html context, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions options, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name )` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Public fields

### app

```
public final @NonNull FirebaseApp app
```

Accessing this object for Kotlin apps has changed; see the migration guide: https://firebase.google.com/docs/android/kotlin-migration.

Returns the default firebase app instance.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### options

```
public final @NonNull FirebaseOptions options
```

Accessing this object for Kotlin apps has changed; see the migration guide: https://firebase.google.com/docs/android/kotlin-migration.

Returns options of default FirebaseApp

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Public methods

### FirebaseKt.app

```
public static final @NonNull FirebaseApp FirebaseKt.app(@NonNull Firebase receiver, @NonNull String name)
```

Accessing this object for Kotlin apps has changed; see the migration guide: https://firebase.google.com/docs/android/kotlin-migration.

Returns a named firebase app instance.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### FirebaseKt.initialize

```
public static final FirebaseApp FirebaseKt.[initialize](https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/FirebaseKt#(com.google.firebase.ktx.Firebase).initialize(android.content.Context))(
    @NonNull Firebase receiver,
    @NonNull Context context
)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Initializes and returns a FirebaseApp.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### FirebaseKt.initialize

```
public static final @NonNull FirebaseApp FirebaseKt.[initialize](https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/FirebaseKt#(com.google.firebase.ktx.Firebase).initialize(android.content.Context,com.google.firebase.FirebaseOptions))(
    @NonNull Firebase receiver,
    @NonNull Context context,
    @NonNull FirebaseOptions options
)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Initializes and returns a FirebaseApp.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### FirebaseKt.initialize

```
public static final @NonNull FirebaseApp FirebaseKt.[initialize](https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/FirebaseKt#(com.google.firebase.ktx.Firebase).initialize(android.content.Context,com.google.firebase.FirebaseOptions,kotlin.String))(
    @NonNull Firebase receiver,
    @NonNull Context context,
    @NonNull FirebaseOptions options,
    @NonNull String name
)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Initializes and returns a FirebaseApp.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)