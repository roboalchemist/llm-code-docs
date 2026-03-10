# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/package-summary.md.txt

# com.google.firebase.ktx

# com.google.firebase.ktx

## Objects

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase` | All fields in this object are deprecated; Use `com.google.firebase.Firebase` instead. |

## Extension functions summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/package-summary#(com.google.firebase.ktx.Firebase).app(kotlin.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Accessing this object for Kotlin apps has changed; see the migration guide: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.[initialize](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/package-summary#(com.google.firebase.ktx.Firebase).initialize(android.content.Context,com.google.firebase.FirebaseOptions,kotlin.String))( context: https://developer.android.com/reference/kotlin/android/content/Context.html, options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions, name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html )` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.[initialize](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/package-summary#(com.google.firebase.ktx.Firebase).initialize(android.content.Context,com.google.firebase.FirebaseOptions))(context: https://developer.android.com/reference/kotlin/android/content/Context.html, options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.[initialize](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/package-summary#(com.google.firebase.ktx.Firebase).initialize(android.content.Context))(context: https://developer.android.com/reference/kotlin/android/content/Context.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Extension properties summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/package-summary#(com.google.firebase.ktx.Firebase).app()` Accessing this object for Kotlin apps has changed; see the migration guide: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/package-summary#(com.google.firebase.ktx.Firebase).options()` Accessing this object for Kotlin apps has changed; see the migration guide: https://firebase.google.com/docs/android/kotlin-migration. |

## Extension functions

### app

```
fun Firebase.app(name: String): FirebaseApp
```

Accessing this object for Kotlin apps has changed; see the migration guide: https://firebase.google.com/docs/android/kotlin-migration.

Returns a named firebase app instance.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### initialize

```
fun Firebase.[initialize](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/package-summary#(com.google.firebase.ktx.Firebase).initialize(android.content.Context,com.google.firebase.FirebaseOptions,kotlin.String))(
    context: Context,
    options: FirebaseOptions,
    name: String
): FirebaseApp
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Initializes and returns a FirebaseApp.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### initialize

```
fun Firebase.[initialize](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/package-summary#(com.google.firebase.ktx.Firebase).initialize(android.content.Context,com.google.firebase.FirebaseOptions))(context: Context, options: FirebaseOptions): FirebaseApp
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Initializes and returns a FirebaseApp.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### initialize

```
fun Firebase.[initialize](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/package-summary#(com.google.firebase.ktx.Firebase).initialize(android.content.Context))(context: Context): FirebaseApp?
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Initializes and returns a FirebaseApp.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Extension properties

### app

```
val Firebase.app: FirebaseApp
```

Accessing this object for Kotlin apps has changed; see the migration guide: https://firebase.google.com/docs/android/kotlin-migration.

Returns the default firebase app instance.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### options

```
val Firebase.options: FirebaseOptions
```

Accessing this object for Kotlin apps has changed; see the migration guide: https://firebase.google.com/docs/android/kotlin-migration.

Returns options of default FirebaseApp

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)