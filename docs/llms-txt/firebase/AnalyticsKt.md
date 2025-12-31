# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ktx/AnalyticsKt.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/AnalyticsKt.md.txt

# AnalyticsKt

# AnalyticsKt


```
public final class AnalyticsKt
```

<br />

*** ** * ** ***

## Summary

|                                                                                                      ### Public methods                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[FirebaseAnalytics](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics) | [getAnalytics](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/AnalyticsKt#(com.google.firebase.Firebase).getAnalytics())`(@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Firebase](https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase)` receiver)` Returns the [FirebaseAnalytics](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics) instance of the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `static final void`                                                                                                                                                                                                           | [logEvent](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/AnalyticsKt#(com.google.firebase.analytics.FirebaseAnalytics).logEvent(kotlin.String,kotlin.Function1))`(` ` @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[FirebaseAnalytics](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics)` receiver,` ` @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)` name,` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[ParametersBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> block` `)` Fluent version of [FirebaseAnalytics.logEvent](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#logEvent(kotlin.String,android.os.Bundle)). |
| `static final void`                                                                                                                                                                                                           | [setConsent](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/AnalyticsKt#(com.google.firebase.analytics.FirebaseAnalytics).setConsent(kotlin.Function1))`(` ` @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[FirebaseAnalytics](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics)` receiver,` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[ConsentBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ConsentBuilder)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> block` `)` Fluent version of [FirebaseAnalytics.setConsent](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setConsent(kotlin.collections.MutableMap)).                                                                                                                                                                                         |

## Public methods

### getAnalytics

```
publicÂ staticÂ finalÂ @NonNull FirebaseAnalyticsÂ getAnalytics(@NonNull FirebaseÂ receiver)
```

Returns the [FirebaseAnalytics](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics) instance of the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).  

### logEvent

```
publicÂ staticÂ finalÂ voidÂ logEvent(
Â Â Â Â @NonNull FirebaseAnalyticsÂ receiver,
Â Â Â Â @NonNull StringÂ name,
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull ParametersBuilder,Â Unit>Â block
)
```

Fluent version of [FirebaseAnalytics.logEvent](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#logEvent(kotlin.String,android.os.Bundle)).

Example use:  

```text
Firebase.analytics.logEvent("myEvent") {
  param(Params.VALUE, 3.99)
  param(Params.CURRENCY, "USD")
}
```  

### setConsent

```
publicÂ staticÂ finalÂ voidÂ setConsent(
Â Â Â Â @NonNull FirebaseAnalyticsÂ receiver,
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull ConsentBuilder,Â Unit>Â block
)
```

Fluent version of [FirebaseAnalytics.setConsent](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setConsent(kotlin.collections.MutableMap)).

Example use:  

```text
Firebase.analytics.setConsent {
  adStorage = ConsentStatus.GRANTED
  analyticsStorage = ConsentStatus.GRANTED
  adUserData = ConsentStatus.GRANTED
  adPersonalization = ConsentStatus.GRANTED
}
```