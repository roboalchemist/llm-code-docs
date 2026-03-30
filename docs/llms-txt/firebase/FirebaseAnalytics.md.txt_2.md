# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.md.txt

# FirebaseAnalytics

# FirebaseAnalytics


```
@DataCollectionPurpose(dataTypes = [SemanticType.ST_ANALYTICS_ID, SemanticType.ST_PAYMENTS_TRANSACTION_INFO, SemanticType.ST_HARDWARE_ID, SemanticType.ST_IDENTIFYING_ID, SemanticType.ST_COARSE_LOCATION], collectionPurposes = [CollectionPurpose.CP_ANALYTICS])
class FirebaseAnalytics
```

<br />

*** ** * ** ***

The top level Firebase Analytics singleton that provides methods for logging events and setting user properties. See [the developer guides](http://goo.gl/X2xCu3) for general information on using Firebase Analytics in your apps.

Applications can get an instance of this class by calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#getInstance(android.content.Context)`. `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#getInstance(android.content.Context)` is thread safe and can be called from any thread.

## Summary

| ### Nested types |
|---|
| `enum https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus` The status value of the consent type. |
| `enum https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType` The type of consent to set. |
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event` An Event is an important occurrence in your app that you want to measure. |
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param` Params supply information that contextualize Events. |
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.UserProperty` A UserProperty is an attribute that describes the app-user. |

| ### Public functions |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?>` | `@https://firebase.google.com/docs/reference/kotlin/com/google/android/gms/testing/lint/common/SuppressViolation(value = "catch_specific_exceptions") https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#getAppInstanceId()()` Retrieves the app instance id from the service, or `null` if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#ANALYTICS_STORAGE` has been set to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#DENIED`. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics` | `@https://developer.android.com/reference/androidx/annotation/RequiresPermission.html(allOf = [Manifest.permission.INTERNET, Manifest.permission.ACCESS_NETWORK_STATE, Manifest.permission.WAKE_LOCK]) @https://developer.android.com/reference/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#getInstance(android.content.Context)(context: https://developer.android.com/reference/android/content/Context.html)` Returns the singleton FirebaseAnalytics interface. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html?>` | `@https://firebase.google.com/docs/reference/kotlin/com/google/android/gms/testing/lint/common/SuppressViolation(value = "catch_specific_exceptions") https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#getSessionId()()` Retrieves the session id from the client. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#logEvent(java.lang.String,android.os.Bundle)(name: @https://developer.android.com/reference/androidx/annotation/Size.html(min = 1, max = 40) https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, params: https://developer.android.com/reference/android/os/Bundle.html?)` Logs an app event. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#resetAnalyticsData()()` Clears all analytics data for this app from the device and resets the app instance id. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setAnalyticsCollectionEnabled(boolean)(enabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Sets whether analytics collection is enabled for this app on this device. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setConsent(java.util.Map<com.google.firebase.analytics.FirebaseAnalytics.ConsentType,com.google.firebase.analytics.FirebaseAnalytics.ConsentStatus>)( consentSettings: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType!, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus!> )` Sets the applicable end user consent state (e.g., for device identifiers) for this app on this device. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `@https://developer.android.com/reference/androidx/annotation/MainThread.html @https://developer.android.com/reference/androidx/annotation/Keep.html [setCurrentScreen](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setCurrentScreen(android.app.Activity,java.lang.String,java.lang.String))( activity: https://developer.android.com/reference/android/app/Activity.html, screenName: @https://developer.android.com/reference/androidx/annotation/Size.html(min = 1, max = 36) https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, screenClassOverride: @https://developer.android.com/reference/androidx/annotation/Size.html(min = 1, max = 36) https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? )` **This function is deprecated.** To log screen view events, call mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.SCREEN_VIEW, params) instead. <br /> |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setDefaultEventParameters(android.os.Bundle)(parameters: https://developer.android.com/reference/android/os/Bundle.html?)` Adds parameters that will be set on every event logged from the SDK, including automatic ones. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setSessionTimeoutDuration(long)(milliseconds: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Sets the duration of inactivity that terminates the current session. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setUserId(java.lang.String)(id: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Sets the user ID property. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setUserProperty(java.lang.String,java.lang.String)( name: @https://developer.android.com/reference/androidx/annotation/Size.html(min = 1, max = 24) https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: @https://developer.android.com/reference/androidx/annotation/Size.html(max = 36) https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? )` Sets a user property to a given value. |

| ### Extension functions |
|---|---|
| `inline https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#(com.google.firebase.analytics.FirebaseAnalytics).logEvent(kotlin.String,kotlin.Function1)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, block: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Fluent version of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#logEvent(kotlin.String,android.os.Bundle)`. |
| `inline https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#(com.google.firebase.analytics.FirebaseAnalytics).setConsent(kotlin.Function1)(crossinline block: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ConsentBuilder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Fluent version of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setConsent(kotlin.collections.MutableMap)`. |

## Public functions

### getAppInstanceId

```
@SuppressViolation(value = "catch_specific_exceptions")
fun getAppInstanceId(): Task<String?>
```

Retrieves the app instance id from the service, or `null` if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#ANALYTICS_STORAGE` has been set to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#DENIED`.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` with the result of the retrieval |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setConsent(java.util.Map<com.google.firebase.analytics.FirebaseAnalytics.ConsentType,com.google.firebase.analytics.FirebaseAnalytics.ConsentStatus>)` |   |

### getInstance

```
@RequiresPermission(allOf = [Manifest.permission.INTERNET, Manifest.permission.ACCESS_NETWORK_STATE, Manifest.permission.WAKE_LOCK])
@Keep
java-static fun getInstance(context: Context): FirebaseAnalytics
```

Returns the singleton FirebaseAnalytics interface.

| Parameters |
|---|---|
| `context: https://developer.android.com/reference/android/content/Context.html` | the context used to initialize Firebase Analytics. Must not be `null`. |

### getSessionId

```
@SuppressViolation(value = "catch_specific_exceptions")
fun getSessionId(): Task<Long?>
```

Retrieves the session id from the client. Returns `null` if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#ANALYTICS_STORAGE` has been set to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#DENIED` or session is expired.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html?>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` with the result of the retrieval |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setConsent(java.util.Map<com.google.firebase.analytics.FirebaseAnalytics.ConsentType,com.google.firebase.analytics.FirebaseAnalytics.ConsentStatus>)` |   |

### logEvent

```
fun logEvent(name: @Size(min = 1, max = 40) String, params: Bundle?): Unit
```

Logs an app event. The event can have up to 25 parameters. Events with the same name must have the same parameters. Up to 500 event names are supported. Using predefined `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event` and/or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param` is recommended for optimal reporting.

| Parameters |
|---|---|
| `name: @https://developer.android.com/reference/androidx/annotation/Size.html(min = 1, max = 40) https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the event. Should contain 1 to 40 [alphanumeric](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetterOrDigit-int-)characters or underscores. The name must start with an [alphabetic](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetter-int-)character. Some event names are reserved. See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event` for the list of reserved event names. The "firebase_", "google_" and "ga_" prefixes are reserved and should not be used. Note that event names are case-sensitive and that logging two events whose names differ only in case will result in two distinct events. |
| `params: https://developer.android.com/reference/android/os/Bundle.html?` | The map of event parameters. Passing null indicates that the event has no parameters. Parameter names can be up to 40 characters long and must start with an [alphabetic](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetter-int-)character and contain only [alphanumeric](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetterOrDigit-int-)characters and underscores. String, long and double param types are supported. String parameter values can be up to 100 characters long. The "firebase_", "google_" and "ga_" prefixes are reserved and should not be used for parameter names. |

### resetAnalyticsData

```
fun resetAnalyticsData(): Unit
```

Clears all analytics data for this app from the device and resets the app instance id.

### setAnalyticsCollectionEnabled

```
fun setAnalyticsCollectionEnabled(enabled: Boolean): Unit
```

Sets whether analytics collection is enabled for this app on this device. This setting is persisted across app sessions. By default it is enabled.

| Parameters |
|---|---|
| `enabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | Whether analytics collection is enabled for this app on this device. |

### setConsent

```
fun setConsent(
    consentSettings: (Mutable)Map<FirebaseAnalytics.ConsentType!, FirebaseAnalytics.ConsentStatus!>
): Unit
```

Sets the applicable end user consent state (e.g., for device identifiers) for this app on this device. Use the consent map to specify individual consent type values. Settings are persisted across app sessions.

| Parameters |
|---|---|
| `consentSettings: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType!, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus!>` | The map of consent types. Supported consent type keys are `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#AD_STORAGE`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#ANALYTICS_STORAGE`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#AD_USER_DATA` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#AD_PERSONALIZATION`. Valid values are `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#GRANTED` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#DENIED`. |

### setCurrentScreen

```
@MainThread
@Keep
fun [setCurrentScreen](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setCurrentScreen(android.app.Activity,java.lang.String,java.lang.String))(
    activity: Activity,
    screenName: @Size(min = 1, max = 36) String?,
    screenClassOverride: @Size(min = 1, max = 36) String?
): Unit
```

> [!CAUTION]
> **This function is deprecated.**   
>
> To log screen view events, call mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.SCREEN_VIEW, params) instead.

Sets the current screen name, which specifies the current visual context in your app. This helps identify the areas in your app where users spend their time and how they interact with your app.

Note that screen reporting is enabled automatically and records the class name of the current Activity for you without requiring you to call this function. The class name can optionally be overridden by calling this function in the onResume callback of your Activity and specifying the screenClassOverride parameter.

If your app does not use a distinct Activity for each screen, you should call this function and specify a distinct screenName each time a new screen is presented to the user.

The name and classOverride remain in effect until the current Activity changes or a new call to setCurrentScreen is made.

This method must be called from the app's main thread.

| Parameters |
|---|---|
| `activity: https://developer.android.com/reference/android/app/Activity.html` | The activity to which the screen name and class name apply. |
| `screenName: @https://developer.android.com/reference/androidx/annotation/Size.html(min = 1, max = 36) https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | The name of the current screen. Set to null to clear the current screen name. |
| `screenClassOverride: @https://developer.android.com/reference/androidx/annotation/Size.html(min = 1, max = 36) https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | The name of the screen class. By default this is the class name of the current Activity. Set to null to revert to the default class name. |

### setDefaultEventParameters

```
fun setDefaultEventParameters(parameters: Bundle?): Unit
```

Adds parameters that will be set on every event logged from the SDK, including automatic ones. The values passed in the parameters bundle will be added to the map of default event parameters. These parameters persist across app runs. They are of lower precedence than event parameters, so if an event parameter and a parameter set using this API have the same name, the value of the event parameter will be used. The same limitations on event parameters apply to default event parameters.

| Parameters |
|---|---|
| `parameters: https://developer.android.com/reference/android/os/Bundle.html?` | Parameters to be added to the map of parameters added to every event. They will be added to the map of default event parameters, replacing any existing parameter with the same name. Valid parameter values are `String`, `long`, and `double`. Setting a key's value to `null` will clear that parameter. Passing in a `null` bundle will clear all parameters. |

### setSessionTimeoutDuration

```
fun setSessionTimeoutDuration(milliseconds: Long): Unit
```

Sets the duration of inactivity that terminates the current session. The default value is 1800000 (30 minutes).

| Parameters |
|---|---|
| `milliseconds: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | Session timeout duration in milliseconds |

### setUserId

```
fun setUserId(id: String?): Unit
```

Sets the user ID property. This feature must be used in accordance with [Google's Privacy Policy](https://www.google.com/policies/privacy).

| Parameters |
|---|---|
| `id: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | The user ID to ascribe to the user of this app on this device, which must be non-empty and no more than 256 characters long. Setting the ID to null removes the user ID. |

### setUserProperty

```
fun setUserProperty(
    name: @Size(min = 1, max = 24) String,
    value: @Size(max = 36) String?
): Unit
```

Sets a user property to a given value. Up to 25 user property names are supported. Once set, user property values persist throughout the app lifecycle and across sessions.

| Parameters |
|---|---|
| `name: @https://developer.android.com/reference/androidx/annotation/Size.html(min = 1, max = 24) https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the user property to set. Should contain 1 to 24 [alphanumeric](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetterOrDigit-int-)characters or underscores and must start with an [alphabetic](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetter-int-)character. The "firebase_", "google_" and "ga_" prefixes are reserved and should not be used for user property names. |
| `value: @https://developer.android.com/reference/androidx/annotation/Size.html(max = 36) https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | The value of the user property. Values can be up to 36 characters long. Setting the value to null removes the user property. |

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