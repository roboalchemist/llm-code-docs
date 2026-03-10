# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/ktx/package-summary.md.txt

# com.google.firebase.appcheck.ktx

# com.google.firebase.appcheck.ktx

## Extension functions summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/ktx/package-summary#(com.google.firebase.ktx.Firebase).appCheck(com.google.firebase.FirebaseApp)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken.[component1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/ktx/package-summary#(com.google.firebase.appcheck.AppCheckToken).component1())()` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken.[component2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/ktx/package-summary#(com.google.firebase.appcheck.AppCheckToken).component2())()` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Extension properties summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/ktx/package-summary#(com.google.firebase.ktx.Firebase).appCheck()` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |

## Extension functions

### appCheck

```
fun Firebase.appCheck(app: FirebaseApp): FirebaseAppCheck
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### component1

```
operator fun AppCheckToken.[component1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/ktx/package-summary#(com.google.firebase.appcheck.AppCheckToken).component1())(): String
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken` to provide token.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the token of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken` |

### component2

```
operator fun AppCheckToken.[component2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/ktx/package-summary#(com.google.firebase.appcheck.AppCheckToken).component2())(): Long
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken` to provide expireTimeMillis.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the expireTimeMillis of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken` |

## Extension properties

### appCheck

```
val Firebase.appCheck: FirebaseAppCheck
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)