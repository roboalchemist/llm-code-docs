# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/AnalyticsKt.md.txt

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
| `static final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/AnalyticsKt#(com.google.firebase.Firebase).getAnalytics()(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase receiver)` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `static final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/AnalyticsKt#(com.google.firebase.analytics.FirebaseAnalytics).logEvent(kotlin.String,kotlin.Function1)( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics receiver, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html name, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> block )` Fluent version of `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#logEvent(kotlin.String,android.os.Bundle)`. |
| `static final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/AnalyticsKt#(com.google.firebase.analytics.FirebaseAnalytics).setConsent(kotlin.Function1)( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics receiver, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ConsentBuilder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> block )` Fluent version of `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setConsent(kotlin.collections.MutableMap)`. |

## Public methods

### getAnalytics

```
public static final @NonNull FirebaseAnalytics getAnalytics(@NonNull Firebase receiver)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

### logEvent

```
public static final void logEvent(
    @NonNull FirebaseAnalytics receiver,
    @NonNull String name,
    @ExtensionFunctionType @NonNull Function1<@NonNull ParametersBuilder, Unit> block
)
```

Fluent version of `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#logEvent(kotlin.String,android.os.Bundle)`.

Example use:

```
Firebase.analytics.logEvent("myEvent") {
  param(Params.VALUE, 3.99)
  param(Params.CURRENCY, "USD")
}
```

### setConsent

```
public static final void setConsent(
    @NonNull FirebaseAnalytics receiver,
    @ExtensionFunctionType @NonNull Function1<@NonNull ConsentBuilder, Unit> block
)
```

Fluent version of `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setConsent(kotlin.collections.MutableMap)`.

Example use:

```
Firebase.analytics.setConsent {
  adStorage = ConsentStatus.GRANTED
  analyticsStorage = ConsentStatus.GRANTED
  adUserData = ConsentStatus.GRANTED
  adPersonalization = ConsentStatus.GRANTED
}
```