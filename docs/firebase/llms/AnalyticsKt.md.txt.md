# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ktx/AnalyticsKt.md.txt

# AnalyticsKt

# AnalyticsKt


```
public final class AnalyticsKt
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ktx/AnalyticsKt#(com.google.firebase.ktx.Firebase).getAnalytics()(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/Firebase receiver)` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |
| `static final void` | `[logEvent](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ktx/AnalyticsKt#(com.google.firebase.analytics.FirebaseAnalytics).logEvent(kotlin.String,kotlin.Function1))( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics receiver, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html name, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ktx/ParametersBuilder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> block )` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `static final void` | `[setConsent](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ktx/AnalyticsKt#(com.google.firebase.analytics.FirebaseAnalytics).setConsent(kotlin.Function1))( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics receiver, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ktx/ConsentBuilder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> block )` **This method is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Public methods

### getAnalytics

```
public static final @NonNull FirebaseAnalytics getAnalytics(@NonNull Firebase receiver)
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### logEvent

```
public static final void [logEvent](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ktx/AnalyticsKt#(com.google.firebase.analytics.FirebaseAnalytics).logEvent(kotlin.String,kotlin.Function1))(
    @NonNull FirebaseAnalytics receiver,
    @NonNull String name,
    @ExtensionFunctionType @NonNull Function1<@NonNull ParametersBuilder, Unit> block
)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Fluent version of `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#logEvent(kotlin.String,android.os.Bundle)`.

Example use:

```
Firebase.analytics.logEvent("myEvent") {
  param(Params.VALUE, 3.99)
  param(Params.CURRENCY, "USD")
}
```

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### setConsent

```
public static final void [setConsent](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ktx/AnalyticsKt#(com.google.firebase.analytics.FirebaseAnalytics).setConsent(kotlin.Function1))(
    @NonNull FirebaseAnalytics receiver,
    @ExtensionFunctionType @NonNull Function1<@NonNull ConsentBuilder, Unit> block
)
```

> [!CAUTION]
> **This method is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Fluent version of `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setConsent(kotlin.collections.MutableMap)`.

Example use:

```
Firebase.analytics.setConsent {
  adStorage = ConsentStatus.GRANTED
  analyticsStorage = ConsentStatus.GRANTED
}
```

**Important:** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)