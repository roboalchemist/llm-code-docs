# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/ktx/package-summary.md.txt

# com.google.firebase.crashlytics.ktx

# com.google.firebase.crashlytics.ktx

## Classes

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/ktx/KeyValueBuilder` | **This class is deprecated.** Use \`com.google.firebase.crashlytics.KeyValueBuilder\` from the main module. |

## Extension functions summary

|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics.[setCustomKeys](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/ktx/package-summary#(com.google.firebase.crashlytics.FirebaseCrashlytics).setCustomKeys(kotlin.Function1))(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/ktx/KeyValueBuilder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Extension properties summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/ktx/package-summary#(com.google.firebase.ktx.Firebase).crashlytics()` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |

## Extension functions

### setCustomKeys

```
fun FirebaseCrashlytics.[setCustomKeys](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/ktx/package-summary#(com.google.firebase.crashlytics.FirebaseCrashlytics).setCustomKeys(kotlin.Function1))(init: KeyValueBuilder.() -> Unit): Unit
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Associates all key-value parameters with the reports

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Extension properties

### crashlytics

```
val Firebase.crashlytics: FirebaseCrashlytics
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)