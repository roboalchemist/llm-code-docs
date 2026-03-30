# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/ktx/package-summary.md.txt

# com.google.firebase.functions.ktx

# com.google.firebase.functions.ktx

## Extension functions summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/ktx/package-summary#(com.google.firebase.ktx.Firebase).functions(com.google.firebase.FirebaseApp,kotlin.String)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp, regionOrCustomDomain: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/ktx/package-summary#(com.google.firebase.ktx.Firebase).functions(com.google.firebase.FirebaseApp)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/ktx/package-summary#(com.google.firebase.ktx.Firebase).functions(kotlin.String)(regionOrCustomDomain: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions.[getHttpsCallable](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/ktx/package-summary#(com.google.firebase.functions.FirebaseFunctions).getHttpsCallable(kotlin.String,kotlin.Function1))(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions.[getHttpsCallableFromUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/ktx/package-summary#(com.google.firebase.functions.FirebaseFunctions).getHttpsCallableFromUrl(java.net.URL,kotlin.Function1))(url: https://developer.android.com/reference/kotlin/java/net/URL.html, init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Extension properties summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/ktx/package-summary#(com.google.firebase.ktx.Firebase).functions()` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |

## Extension functions

### functions

```
fun Firebase.functions(app: FirebaseApp, regionOrCustomDomain: String): FirebaseFunctions
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/ktx/package-summary#(com.google.firebase.ktx.Firebase).functions(com.google.firebase.FirebaseApp,kotlin.String)`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### functions

```
fun Firebase.functions(app: FirebaseApp): FirebaseFunctions
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### functions

```
fun Firebase.functions(regionOrCustomDomain: String): FirebaseFunctions
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/ktx/package-summary#(com.google.firebase.ktx.Firebase).functions(kotlin.String)`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### getHttpsCallable

```
fun FirebaseFunctions.[getHttpsCallable](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/ktx/package-summary#(com.google.firebase.functions.FirebaseFunctions).getHttpsCallable(kotlin.String,kotlin.Function1))(name: String, init: HttpsCallableOptions.Builder.() -> Unit): HttpsCallableReference
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns a reference to the Callable HTTPS trigger with the given name and call options.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### getHttpsCallableFromUrl

```
fun FirebaseFunctions.[getHttpsCallableFromUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/ktx/package-summary#(com.google.firebase.functions.FirebaseFunctions).getHttpsCallableFromUrl(java.net.URL,kotlin.Function1))(url: URL, init: HttpsCallableOptions.Builder.() -> Unit): HttpsCallableReference
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns a reference to the Callable HTTPS trigger with the given URL and call options.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Extension properties

### functions

```
val Firebase.functions: FirebaseFunctions
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)