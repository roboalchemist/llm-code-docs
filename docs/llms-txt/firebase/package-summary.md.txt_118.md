# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ktx/package-summary.md.txt

# com.google.firebase.analytics.ktx

# com.google.firebase.analytics.ktx

## Classes

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ktx/ConsentBuilder` | **This class is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ktx/ParametersBuilder` | **This class is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Extension functions summary

|---|---|
| `inline https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.[logEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ktx/package-summary#(com.google.firebase.analytics.FirebaseAnalytics).logEvent(kotlin.String,kotlin.Function1))(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, block: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ktx/ParametersBuilder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `inline https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.[setConsent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ktx/package-summary#(com.google.firebase.analytics.FirebaseAnalytics).setConsent(kotlin.Function1))(crossinline block: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ktx/ConsentBuilder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Extension properties summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ktx/package-summary#(com.google.firebase.ktx.Firebase).analytics()` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |

## Extension functions

### logEvent

```
inline fun FirebaseAnalytics.[logEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ktx/package-summary#(com.google.firebase.analytics.FirebaseAnalytics).logEvent(kotlin.String,kotlin.Function1))(name: String, block: ParametersBuilder.() -> Unit): Unit
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Fluent version of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#logEvent(kotlin.String,android.os.Bundle)`.

Example use:

```kotlin
Firebase.analytics.logEvent("myEvent") {
  param(Params.VALUE, 3.99)
  param(Params.CURRENCY, "USD")
}
```

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### setConsent

```
inline fun FirebaseAnalytics.[setConsent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ktx/package-summary#(com.google.firebase.analytics.FirebaseAnalytics).setConsent(kotlin.Function1))(crossinline block: ConsentBuilder.() -> Unit): Unit
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Fluent version of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setConsent(kotlin.collections.MutableMap)`.

Example use:

```kotlin
Firebase.analytics.setConsent {
  adStorage = ConsentStatus.GRANTED
  analyticsStorage = ConsentStatus.GRANTED
}
```

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Extension properties

### analytics

```
val Firebase.analytics: FirebaseAnalytics
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)