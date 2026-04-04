# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.md.txt

# FirebaseAnalytics

# FirebaseAnalytics


```
@DataCollectionPurpose(dataTypes = [SemanticType.ST_ANALYTICS_ID, SemanticType.ST_PAYMENTS_TRANSACTION_INFO, SemanticType.ST_HARDWARE_ID, SemanticType.ST_IDENTIFYING_ID, SemanticType.ST_COARSE_LOCATION], collectionPurposes = [CollectionPurpose.CP_ANALYTICS])
public final class FirebaseAnalytics
```

<br />

*** ** * ** ***

The top level Firebase Analytics singleton that provides methods for logging events and setting user properties. See [the developer guides](http://goo.gl/X2xCu3) for general information on using Firebase Analytics in your apps.

Applications can get an instance of this class by calling `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#getInstance(android.content.Context)`. `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#getInstance(android.content.Context)` is thread safe and can be called from any thread.

## Summary

| ### Nested types |
|---|
| `public enum https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus` The status value of the consent type. |
| `public enum https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType` The type of consent to set. |
| `public class https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event` An Event is an important occurrence in your app that you want to measure. |
| `public class https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param` Params supply information that contextualize Events. |
| `public class https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.UserProperty` A UserProperty is an attribute that describes the app-user. |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<@https://checkerframework.org/api/org/checkerframework/checker/nullness/qual/Nullable.html https://developer.android.com/reference/java/lang/String.html>` | `@https://firebase.google.com/docs/reference/android/com/google/android/gms/testing/lint/common/SuppressViolation(value = "catch_specific_exceptions") https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#getAppInstanceId()()` Retrieves the app instance id from the service, or `null` if `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#ANALYTICS_STORAGE` has been set to `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#DENIED`. |
| `static @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics` | `@https://developer.android.com/reference/androidx/annotation/RequiresPermission.html(allOf = [Manifest.permission.INTERNET, Manifest.permission.ACCESS_NETWORK_STATE, Manifest.permission.WAKE_LOCK]) @https://developer.android.com/reference/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#getInstance(android.content.Context)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/android/content/Context.html context)` Returns the singleton FirebaseAnalytics interface. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<@https://checkerframework.org/api/org/checkerframework/checker/nullness/qual/Nullable.html https://developer.android.com/reference/java/lang/Long.html>` | `@https://firebase.google.com/docs/reference/android/com/google/android/gms/testing/lint/common/SuppressViolation(value = "catch_specific_exceptions") https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#getSessionId()()` Retrieves the session id from the client. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#logEvent(java.lang.String,android.os.Bundle)(@https://developer.android.com/reference/androidx/annotation/NonNull.html @https://developer.android.com/reference/androidx/annotation/Size.html(min = 1, max = 40) https://developer.android.com/reference/java/lang/String.html name, @https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/android/os/Bundle.html params)` Logs an app event. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#resetAnalyticsData()()` Clears all analytics data for this app from the device and resets the app instance id. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setAnalyticsCollectionEnabled(boolean)(boolean enabled)` Sets whether analytics collection is enabled for this app on this device. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setConsent(java.util.Map<com.google.firebase.analytics.FirebaseAnalytics.ConsentType,com.google.firebase.analytics.FirebaseAnalytics.ConsentStatus>)( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/util/Map.html<https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType, https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus> consentSettings )` Sets the applicable end user consent state (e.g., for device identifiers) for this app on this device. |
| `void` | `@https://developer.android.com/reference/androidx/annotation/MainThread.html @https://developer.android.com/reference/androidx/annotation/Keep.html [setCurrentScreen](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setCurrentScreen(android.app.Activity,java.lang.String,java.lang.String))( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/android/app/Activity.html activity, @https://developer.android.com/reference/androidx/annotation/Nullable.html @https://developer.android.com/reference/androidx/annotation/Size.html(min = 1, max = 36) https://developer.android.com/reference/java/lang/String.html screenName, @https://developer.android.com/reference/androidx/annotation/Nullable.html @https://developer.android.com/reference/androidx/annotation/Size.html(min = 1, max = 36) https://developer.android.com/reference/java/lang/String.html screenClassOverride )` **This method is deprecated.** To log screen view events, call mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.SCREEN_VIEW, params) instead. <br /> |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setDefaultEventParameters(android.os.Bundle)(@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/android/os/Bundle.html parameters)` Adds parameters that will be set on every event logged from the SDK, including automatic ones. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setSessionTimeoutDuration(long)(long milliseconds)` Sets the duration of inactivity that terminates the current session. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setUserId(java.lang.String)(@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html id)` Sets the user ID property. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setUserProperty(java.lang.String,java.lang.String)( @https://developer.android.com/reference/androidx/annotation/NonNull.html @https://developer.android.com/reference/androidx/annotation/Size.html(min = 1, max = 24) https://developer.android.com/reference/java/lang/String.html name, @https://developer.android.com/reference/androidx/annotation/Nullable.html @https://developer.android.com/reference/androidx/annotation/Size.html(max = 36) https://developer.android.com/reference/java/lang/String.html value )` Sets a user property to a given value. |

| ### Extension functions |
|---|---|
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/AnalyticsKt.https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#(com.google.firebase.analytics.FirebaseAnalytics).logEvent(kotlin.String,kotlin.Function1)( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics receiver, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html name, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ParametersBuilder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> block )` Fluent version of `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#logEvent(kotlin.String,android.os.Bundle)`. |
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/AnalyticsKt.https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#(com.google.firebase.analytics.FirebaseAnalytics).setConsent(kotlin.Function1)( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics receiver, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/ConsentBuilder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> block )` Fluent version of `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setConsent(kotlin.collections.MutableMap)`. |

## Public methods

### getAppInstanceId

```
@SuppressViolation(value = "catch_specific_exceptions")
public @NonNull Task<@Nullable String> getAppInstanceId()
```

Retrieves the app instance id from the service, or `null` if `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#ANALYTICS_STORAGE` has been set to `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#DENIED`.

| Returns |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<@https://checkerframework.org/api/org/checkerframework/checker/nullness/qual/Nullable.html https://developer.android.com/reference/java/lang/String.html>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` with the result of the retrieval |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setConsent(java.util.Map<com.google.firebase.analytics.FirebaseAnalytics.ConsentType,com.google.firebase.analytics.FirebaseAnalytics.ConsentStatus>)` |   |

### getInstance

```
@RequiresPermission(allOf = [Manifest.permission.INTERNET, Manifest.permission.ACCESS_NETWORK_STATE, Manifest.permission.WAKE_LOCK])
@Keep
public static @NonNull FirebaseAnalytics getInstance(@NonNull Context context)
```

Returns the singleton FirebaseAnalytics interface.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/android/content/Context.html context` | the context used to initialize Firebase Analytics. Must not be `null`. |

### getSessionId

```
@SuppressViolation(value = "catch_specific_exceptions")
public @NonNull Task<@Nullable Long> getSessionId()
```

Retrieves the session id from the client. Returns `null` if `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#ANALYTICS_STORAGE` has been set to `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#DENIED` or session is expired.

| Returns |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<@https://checkerframework.org/api/org/checkerframework/checker/nullness/qual/Nullable.html https://developer.android.com/reference/java/lang/Long.html>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` with the result of the retrieval |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setConsent(java.util.Map<com.google.firebase.analytics.FirebaseAnalytics.ConsentType,com.google.firebase.analytics.FirebaseAnalytics.ConsentStatus>)` |   |

### logEvent

```
public void logEvent(@NonNull @Size(min = 1, max = 40) String name, @Nullable Bundle params)
```

Logs an app event. The event can have up to 25 parameters. Events with the same name must have the same parameters. Up to 500 event names are supported. Using predefined `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event` and/or `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param` is recommended for optimal reporting.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html @https://developer.android.com/reference/androidx/annotation/Size.html(min = 1, max = 40) https://developer.android.com/reference/java/lang/String.html name` | The name of the event. Should contain 1 to 40 [alphanumeric](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetterOrDigit-int-)characters or underscores. The name must start with an [alphabetic](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetter-int-)character. Some event names are reserved. See `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event` for the list of reserved event names. The "firebase_", "google_" and "ga_" prefixes are reserved and should not be used. Note that event names are case-sensitive and that logging two events whose names differ only in case will result in two distinct events. |
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/android/os/Bundle.html params` | The map of event parameters. Passing null indicates that the event has no parameters. Parameter names can be up to 40 characters long and must start with an [alphabetic](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetter-int-)character and contain only [alphanumeric](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetterOrDigit-int-)characters and underscores. String, long and double param types are supported. String parameter values can be up to 100 characters long. The "firebase_", "google_" and "ga_" prefixes are reserved and should not be used for parameter names. |

### resetAnalyticsData

```
public void resetAnalyticsData()
```

Clears all analytics data for this app from the device and resets the app instance id.

### setAnalyticsCollectionEnabled

```
public void setAnalyticsCollectionEnabled(boolean enabled)
```

Sets whether analytics collection is enabled for this app on this device. This setting is persisted across app sessions. By default it is enabled.

| Parameters |
|---|---|
| `boolean enabled` | Whether analytics collection is enabled for this app on this device. |

### setConsent

```
public void setConsent(
    @NonNull Map<FirebaseAnalytics.ConsentType, FirebaseAnalytics.ConsentStatus> consentSettings
)
```

Sets the applicable end user consent state (e.g., for device identifiers) for this app on this device. Use the consent map to specify individual consent type values. Settings are persisted across app sessions.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/util/Map.html<https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType, https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus> consentSettings` | The map of consent types. Supported consent type keys are `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#AD_STORAGE`, `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#ANALYTICS_STORAGE`, `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#AD_USER_DATA` and `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#AD_PERSONALIZATION`. Valid values are `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#GRANTED` and `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#DENIED`. |

### setCurrentScreen

```
@MainThread
@Keep
public void [setCurrentScreen](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setCurrentScreen(android.app.Activity,java.lang.String,java.lang.String))(
    @NonNull Activity activity,
    @Nullable @Size(min = 1, max = 36) String screenName,
    @Nullable @Size(min = 1, max = 36) String screenClassOverride
)
```

> [!CAUTION]
> **This method is deprecated.**   
>
> To log screen view events, call mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.SCREEN_VIEW, params) instead.

Sets the current screen name, which specifies the current visual context in your app. This helps identify the areas in your app where users spend their time and how they interact with your app.

Note that screen reporting is enabled automatically and records the class name of the current Activity for you without requiring you to call this function. The class name can optionally be overridden by calling this function in the onResume callback of your Activity and specifying the screenClassOverride parameter.

If your app does not use a distinct Activity for each screen, you should call this function and specify a distinct screenName each time a new screen is presented to the user.

The name and classOverride remain in effect until the current Activity changes or a new call to setCurrentScreen is made.

This method must be called from the app's main thread.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/android/app/Activity.html activity` | The activity to which the screen name and class name apply. |
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html @https://developer.android.com/reference/androidx/annotation/Size.html(min = 1, max = 36) https://developer.android.com/reference/java/lang/String.html screenName` | The name of the current screen. Set to null to clear the current screen name. |
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html @https://developer.android.com/reference/androidx/annotation/Size.html(min = 1, max = 36) https://developer.android.com/reference/java/lang/String.html screenClassOverride` | The name of the screen class. By default this is the class name of the current Activity. Set to null to revert to the default class name. |

### setDefaultEventParameters

```
public void setDefaultEventParameters(@Nullable Bundle parameters)
```

Adds parameters that will be set on every event logged from the SDK, including automatic ones. The values passed in the parameters bundle will be added to the map of default event parameters. These parameters persist across app runs. They are of lower precedence than event parameters, so if an event parameter and a parameter set using this API have the same name, the value of the event parameter will be used. The same limitations on event parameters apply to default event parameters.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/android/os/Bundle.html parameters` | Parameters to be added to the map of parameters added to every event. They will be added to the map of default event parameters, replacing any existing parameter with the same name. Valid parameter values are `String`, `long`, and `double`. Setting a key's value to `null` will clear that parameter. Passing in a `null` bundle will clear all parameters. |

### setSessionTimeoutDuration

```
public void setSessionTimeoutDuration(long milliseconds)
```

Sets the duration of inactivity that terminates the current session. The default value is 1800000 (30 minutes).

| Parameters |
|---|---|
| `long milliseconds` | Session timeout duration in milliseconds |

### setUserId

```
public void setUserId(@Nullable String id)
```

Sets the user ID property. This feature must be used in accordance with [Google's Privacy Policy](https://www.google.com/policies/privacy).

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html id` | The user ID to ascribe to the user of this app on this device, which must be non-empty and no more than 256 characters long. Setting the ID to null removes the user ID. |

### setUserProperty

```
public void setUserProperty(
    @NonNull @Size(min = 1, max = 24) String name,
    @Nullable @Size(max = 36) String value
)
```

Sets a user property to a given value. Up to 25 user property names are supported. Once set, user property values persist throughout the app lifecycle and across sessions.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html @https://developer.android.com/reference/androidx/annotation/Size.html(min = 1, max = 24) https://developer.android.com/reference/java/lang/String.html name` | The name of the user property to set. Should contain 1 to 24 [alphanumeric](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetterOrDigit-int-)characters or underscores and must start with an [alphabetic](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetter-int-)character. The "firebase_", "google_" and "ga_" prefixes are reserved and should not be used for user property names. |
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html @https://developer.android.com/reference/androidx/annotation/Size.html(max = 36) https://developer.android.com/reference/java/lang/String.html value` | The value of the user property. Values can be up to 36 characters long. Setting the value to null removes the user property. |

## Extension functions

### AnalyticsKt.logEvent

```
public final void AnalyticsKt.logEvent(
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

### AnalyticsKt.setConsent

```
public final void AnalyticsKt.setConsent(
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