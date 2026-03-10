# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/package-summary.md.txt

# com.google.firebase.analytics

# com.google.firebase.analytics

Contains public API classes for Firebase Analytics.

## Classes

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ConsentBuilder` | Helper class used to enable fluent syntax in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/package-summary#(com.google.firebase.analytics.FirebaseAnalytics).setConsent(kotlin.Function1)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics` | The top level Firebase Analytics singleton that provides methods for logging events and setting user properties. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event` | An Event is an important occurrence in your app that you want to measure. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param` | Params supply information that contextualize Events. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.UserProperty` | A UserProperty is an attribute that describes the app-user. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/GoogleAnalyticsServerPreviewActivity` | An `https://developer.android.com/reference/android/app/Activity.html` to preview or stop previewing a server-side Google Tag Manager container. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder` | Helper class used to enable fluent syntax in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/package-summary#(com.google.firebase.analytics.FirebaseAnalytics).logEvent(kotlin.String,kotlin.Function1)`. |

## Enums

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus` | The status value of the consent type. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType` | The type of consent to set. |

## Extension functions summary

|---|---|
| `inline https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/package-summary#(com.google.firebase.analytics.FirebaseAnalytics).logEvent(kotlin.String,kotlin.Function1)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, block: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Fluent version of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#logEvent(kotlin.String,android.os.Bundle)`. |
| `inline https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/package-summary#(com.google.firebase.analytics.FirebaseAnalytics).setConsent(kotlin.Function1)(crossinline block: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ConsentBuilder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Fluent version of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setConsent(kotlin.collections.MutableMap)`. |

## Extension properties summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/package-summary#(com.google.firebase.Firebase).analytics()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |

## Extension functions

### logEvent

```
inline fun FirebaseAnalytics.logEvent(name: String, block: ParametersBuilder.() -> Unit): Unit
```

Fluent version of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#logEvent(kotlin.String,android.os.Bundle)`.

Example use:

```kotlin
Firebase.analytics.logEvent("myEvent") {
  param(Params.VALUE, 3.99)
  param(Params.CURRENCY, "USD")
}
```

### setConsent

```
inline fun FirebaseAnalytics.setConsent(crossinline block: ConsentBuilder.() -> Unit): Unit
```

Fluent version of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setConsent(kotlin.collections.MutableMap)`.

Example use:

```kotlin
Firebase.analytics.setConsent {
  adStorage = ConsentStatus.GRANTED
  analyticsStorage = ConsentStatus.GRANTED
  adUserData = ConsentStatus.GRANTED
  adPersonalization = ConsentStatus.GRANTED
}
```

## Extension properties

### analytics

```
val Firebase.analytics: FirebaseAnalytics
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.