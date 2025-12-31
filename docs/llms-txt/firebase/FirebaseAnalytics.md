# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.md.txt

# FirebaseAnalytics

# FirebaseAnalytics


```
@DataCollectionPurpose(dataTypesÂ =Â [SemanticType.ST_ANALYTICS_ID,Â SemanticType.ST_PAYMENTS_TRANSACTION_INFO,Â SemanticType.ST_HARDWARE_ID,Â SemanticType.ST_IDENTIFYING_ID,Â SemanticType.ST_COARSE_LOCATION],Â collectionPurposesÂ =Â [CollectionPurpose.CP_ANALYTICS])
class FirebaseAnalytics
```

<br />

*** ** * ** ***

The top level Firebase Analytics singleton that provides methods for logging events and setting user properties. See [the developer guides](http://goo.gl/X2xCu3) for general information on using Firebase Analytics in your apps.

Applications can get an instance of this class by calling [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#getInstance(android.content.Context)). [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#getInstance(android.content.Context)) is thread safe and can be called from any thread.

## Summary

|                                                                                                   ### Nested types                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `enum `[FirebaseAnalytics.ConsentStatus](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus) The status value of the consent type.                      |
| `enum `[FirebaseAnalytics.ConsentType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType) The type of consent to set.                                    |
| `class `[FirebaseAnalytics.Event](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event) An Event is an important occurrence in your app that you want to measure. |
| `class `[FirebaseAnalytics.Param](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param) Params supply information that contextualize Events.                      |
| `class `[FirebaseAnalytics.UserProperty](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.UserProperty) A UserProperty is an attribute that describes the app-user. |

|                                                                                 ### Public functions                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?>` | `@`[SuppressViolation](https://firebase.google.com/docs/reference/kotlin/com/google/android/gms/testing/lint/common/SuppressViolation)`(value = "catch_specific_exceptions")` [getAppInstanceId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#getAppInstanceId())`()` Retrieves the app instance id from the service, or `null` if [ANALYTICS_STORAGE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#ANALYTICS_STORAGE) has been set to [DENIED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#DENIED).                                                                                                                                                                                                                                                                                                                                                                          |
| `java-static `[FirebaseAnalytics](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics)                                                  | `@`[RequiresPermission](https://developer.android.com/reference/androidx/annotation/RequiresPermission.html)`(allOf = [Manifest.permission.INTERNET, Manifest.permission.ACCESS_NETWORK_STATE, Manifest.permission.WAKE_LOCK])` `@`[Keep](https://developer.android.com/reference/androidx/annotation/Keep.html) [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#getInstance(android.content.Context))`(context: `[Context](https://developer.android.com/reference/android/content/Context.html)`)` Returns the singleton FirebaseAnalytics interface.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)`?>`     | `@`[SuppressViolation](https://firebase.google.com/docs/reference/kotlin/com/google/android/gms/testing/lint/common/SuppressViolation)`(value = "catch_specific_exceptions")` [getSessionId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#getSessionId())`()` Retrieves the session id from the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                          | [logEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#logEvent(java.lang.String,android.os.Bundle))`(name: @`[Size](https://developer.android.com/reference/androidx/annotation/Size.html)`(min = 1, max = 40) `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, params: `[Bundle](https://developer.android.com/reference/android/os/Bundle.html)`?)` Logs an app event.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                          | [resetAnalyticsData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#resetAnalyticsData())`()` Clears all analytics data for this app from the device and resets the app instance id.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                          | [setAnalyticsCollectionEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setAnalyticsCollectionEnabled(boolean))`(enabled: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`)` Sets whether analytics collection is enabled for this app on this device.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                          | [setConsent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setConsent(java.util.Map<com.google.firebase.analytics.FirebaseAnalytics.ConsentType,com.google.firebase.analytics.FirebaseAnalytics.ConsentStatus>))`(` ` consentSettings: (`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[FirebaseAnalytics.ConsentType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType)`!, `[FirebaseAnalytics.ConsentStatus](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus)`!>` `)` Sets the applicable end user consent state (e.g., for device identifiers) for this app on this device.                                                                                                                                                         |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                          | `@`[MainThread](https://developer.android.com/reference/androidx/annotation/MainThread.html) `@`[Keep](https://developer.android.com/reference/androidx/annotation/Keep.html) ~~[setCurrentScreen](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setCurrentScreen(android.app.Activity,java.lang.String,java.lang.String))~~`(` ` activity: `[Activity](https://developer.android.com/reference/android/app/Activity.html)`,` ` screenName: @`[Size](https://developer.android.com/reference/androidx/annotation/Size.html)`(min = 1, max = 36) `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?,` ` screenClassOverride: @`[Size](https://developer.android.com/reference/androidx/annotation/Size.html)`(min = 1, max = 36) `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` `)` **This function is deprecated.** To log screen view events, call mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.SCREEN_VIEW, params) instead. <br /> |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                          | [setDefaultEventParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setDefaultEventParameters(android.os.Bundle))`(parameters: `[Bundle](https://developer.android.com/reference/android/os/Bundle.html)`?)` Adds parameters that will be set on every event logged from the SDK, including automatic ones.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                          | [setSessionTimeoutDuration](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setSessionTimeoutDuration(long))`(milliseconds: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)`)` Sets the duration of inactivity that terminates the current session.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                          | [setUserId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setUserId(java.lang.String))`(id: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Sets the user ID property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                          | [setUserProperty](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setUserProperty(java.lang.String,java.lang.String))`(` ` name: @`[Size](https://developer.android.com/reference/androidx/annotation/Size.html)`(min = 1, max = 24) `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`,` ` value: @`[Size](https://developer.android.com/reference/androidx/annotation/Size.html)`(max = 36) `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` `)` Sets a user property to a given value.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

|                                ### Extension functions                                |
|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `inline `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [FirebaseAnalytics](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics)`.`[logEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#(com.google.firebase.analytics.FirebaseAnalytics).logEvent(kotlin.String,kotlin.Function1))`(name: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, block: `[ParametersBuilder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ParametersBuilder)`.() `->` `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`)` Fluent version of [FirebaseAnalytics.logEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#logEvent(kotlin.String,android.os.Bundle)). |
| `inline `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [FirebaseAnalytics](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics)`.`[setConsent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#(com.google.firebase.analytics.FirebaseAnalytics).setConsent(kotlin.Function1))`(crossinline block: `[ConsentBuilder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ConsentBuilder)`.() `->` `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`)` Fluent version of [FirebaseAnalytics.setConsent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setConsent(kotlin.collections.MutableMap)).                                                                                             |

## Public functions

### getAppInstanceId

```
@SuppressViolation(valueÂ =Â "catch_specific_exceptions")
funÂ getAppInstanceId():Â Task<String?>
```

Retrieves the app instance id from the service, or `null` if [ANALYTICS_STORAGE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#ANALYTICS_STORAGE) has been set to [DENIED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#DENIED).  

|                                                                                        Returns                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?>` | [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) with the result of the retrieval |

|                                                                                                                               See also                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| [setConsent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setConsent(java.util.Map<com.google.firebase.analytics.FirebaseAnalytics.ConsentType,com.google.firebase.analytics.FirebaseAnalytics.ConsentStatus>)) |   |

### getInstance

```
@RequiresPermission(allOfÂ =Â [Manifest.permission.INTERNET,Â Manifest.permission.ACCESS_NETWORK_STATE,Â Manifest.permission.WAKE_LOCK])
@Keep
java-staticÂ funÂ getInstance(context:Â Context):Â FirebaseAnalytics
```

Returns the singleton FirebaseAnalytics interface.  

|                                         Parameters                                         |
|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| `context: `[Context](https://developer.android.com/reference/android/content/Context.html) | the context used to initialize Firebase Analytics. Must not be `null`. |

### getSessionId

```
@SuppressViolation(valueÂ =Â "catch_specific_exceptions")
funÂ getSessionId():Â Task<Long?>
```

Retrieves the session id from the client. Returns `null` if [ANALYTICS_STORAGE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#ANALYTICS_STORAGE) has been set to [DENIED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#DENIED) or session is expired.  

|                                                                                      Returns                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)`?>` | [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) with the result of the retrieval |

|                                                                                                                               See also                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| [setConsent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setConsent(java.util.Map<com.google.firebase.analytics.FirebaseAnalytics.ConsentType,com.google.firebase.analytics.FirebaseAnalytics.ConsentStatus>)) |   |

### logEvent

```
funÂ logEvent(name:Â @Size(minÂ =Â 1,Â maxÂ =Â 40) String,Â params:Â Bundle?):Â Unit
```

Logs an app event. The event can have up to 25 parameters. Events with the same name must have the same parameters. Up to 500 event names are supported. Using predefined [Event](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event) and/or [Param](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param) is recommended for optimal reporting.  

|                                                                                          Parameters                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name: @`[Size](https://developer.android.com/reference/androidx/annotation/Size.html)`(min = 1, max = 40) `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The name of the event. Should contain 1 to 40 [alphanumeric](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetterOrDigit-int-)characters or underscores. The name must start with an [alphabetic](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetter-int-)character. Some event names are reserved. See [Event](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event) for the list of reserved event names. The "firebase_", "google_" and "ga_" prefixes are reserved and should not be used. Note that event names are case-sensitive and that logging two events whose names differ only in case will result in two distinct events. |
| `params: `[Bundle](https://developer.android.com/reference/android/os/Bundle.html)`?`                                                                                                        | The map of event parameters. Passing null indicates that the event has no parameters. Parameter names can be up to 40 characters long and must start with an [alphabetic](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetter-int-)character and contain only [alphanumeric](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetterOrDigit-int-)characters and underscores. String, long and double param types are supported. String parameter values can be up to 100 characters long. The "firebase_", "google_" and "ga_" prefixes are reserved and should not be used for parameter names.                                                                                               |

### resetAnalyticsData

```
funÂ resetAnalyticsData():Â Unit
```

Clears all analytics data for this app from the device and resets the app instance id.  

### setAnalyticsCollectionEnabled

```
funÂ setAnalyticsCollectionEnabled(enabled:Â Boolean):Â Unit
```

Sets whether analytics collection is enabled for this app on this device. This setting is persisted across app sessions. By default it is enabled.  

|                                          Parameters                                           |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| `enabled: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | Whether analytics collection is enabled for this app on this device. |

### setConsent

```
funÂ setConsent(
Â Â Â Â consentSettings:Â (Mutable)Map<FirebaseAnalytics.ConsentType!,Â FirebaseAnalytics.ConsentStatus!>
):Â Unit
```

Sets the applicable end user consent state (e.g., for device identifiers) for this app on this device. Use the consent map to specify individual consent type values. Settings are persisted across app sessions.  

|                                                                                                                                                                                                                                                         Parameters                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `consentSettings: (`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[FirebaseAnalytics.ConsentType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType)`!, `[FirebaseAnalytics.ConsentStatus](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus)`!>` | The map of consent types. Supported consent type keys are [AD_STORAGE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#AD_STORAGE), [ANALYTICS_STORAGE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#ANALYTICS_STORAGE), [AD_USER_DATA](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#AD_USER_DATA) and [AD_PERSONALIZATION](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#AD_PERSONALIZATION). Valid values are [GRANTED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#GRANTED) and [DENIED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#DENIED). |

### setCurrentScreen

```
@MainThread
@Keep
funÂ [setCurrentScreen](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setCurrentScreen(android.app.Activity,java.lang.String,java.lang.String))(
Â Â Â Â activity:Â Activity,
Â Â Â Â screenName:Â @Size(minÂ =Â 1,Â maxÂ =Â 36) String?,
Â Â Â Â screenClassOverride:Â @Size(minÂ =Â 1,Â maxÂ =Â 36) String?
):Â Unit
```
| **This function is deprecated.**   
|
| To log screen view events, call mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.SCREEN_VIEW, params) instead.

Sets the current screen name, which specifies the current visual context in your app. This helps identify the areas in your app where users spend their time and how they interact with your app.

Note that screen reporting is enabled automatically and records the class name of the current Activity for you without requiring you to call this function. The class name can optionally be overridden by calling this function in the onResume callback of your Activity and specifying the screenClassOverride parameter.

If your app does not use a distinct Activity for each screen, you should call this function and specify a distinct screenName each time a new screen is presented to the user.

The name and classOverride remain in effect until the current Activity changes or a new call to setCurrentScreen is made.

This method must be called from the app's main thread.  

|                                                                                                   Parameters                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| `activity: `[Activity](https://developer.android.com/reference/android/app/Activity.html)                                                                                                                      | The activity to which the screen name and class name apply.                                                                               |
| `screenName: @`[Size](https://developer.android.com/reference/androidx/annotation/Size.html)`(min = 1, max = 36) `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`          | The name of the current screen. Set to null to clear the current screen name.                                                             |
| `screenClassOverride: @`[Size](https://developer.android.com/reference/androidx/annotation/Size.html)`(min = 1, max = 36) `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The name of the screen class. By default this is the class name of the current Activity. Set to null to revert to the default class name. |

### setDefaultEventParameters

```
funÂ setDefaultEventParameters(parameters:Â Bundle?):Â Unit
```

Adds parameters that will be set on every event logged from the SDK, including automatic ones. The values passed in the parameters bundle will be added to the map of default event parameters. These parameters persist across app runs. They are of lower precedence than event parameters, so if an event parameter and a parameter set using this API have the same name, the value of the event parameter will be used. The same limitations on event parameters apply to default event parameters.  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `parameters: `[Bundle](https://developer.android.com/reference/android/os/Bundle.html)`?` | Parameters to be added to the map of parameters added to every event. They will be added to the map of default event parameters, replacing any existing parameter with the same name. Valid parameter values are `String`, `long`, and `double`. Setting a key's value to `null` will clear that parameter. Passing in a `null` bundle will clear all parameters. |

### setSessionTimeoutDuration

```
funÂ setSessionTimeoutDuration(milliseconds:Â Long):Â Unit
```

Sets the duration of inactivity that terminates the current session. The default value is 1800000 (30 minutes).  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|------------------------------------------|
| `milliseconds: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | Session timeout duration in milliseconds |

### setUserId

```
funÂ setUserId(id:Â String?):Â Unit
```

Sets the user ID property. This feature must be used in accordance with [Google's Privacy Policy](https://www.google.com/policies/privacy).  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The user ID to ascribe to the user of this app on this device, which must be non-empty and no more than 256 characters long. Setting the ID to null removes the user ID. |

### setUserProperty

```
funÂ setUserProperty(
Â Â Â Â name:Â @Size(minÂ =Â 1,Â maxÂ =Â 24) String,
Â Â Â Â value:Â @Size(maxÂ =Â 36) String?
):Â Unit
```

Sets a user property to a given value. Up to 25 user property names are supported. Once set, user property values persist throughout the app lifecycle and across sessions.  

|                                                                                          Parameters                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name: @`[Size](https://developer.android.com/reference/androidx/annotation/Size.html)`(min = 1, max = 24) `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The name of the user property to set. Should contain 1 to 24 [alphanumeric](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetterOrDigit-int-)characters or underscores and must start with an [alphabetic](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetter-int-)character. The "firebase_", "google_" and "ga_" prefixes are reserved and should not be used for user property names. |
| `value: @`[Size](https://developer.android.com/reference/androidx/annotation/Size.html)`(max = 36) `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`      | The value of the user property. Values can be up to 36 characters long. Setting the value to null removes the user property.                                                                                                                                                                                                                                                                                                             |

## Extension functions

### logEvent

```
inlineÂ funÂ FirebaseAnalytics.logEvent(name:Â String,Â block:Â ParametersBuilder.() -> Unit):Â Unit
```

Fluent version of [FirebaseAnalytics.logEvent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#logEvent(kotlin.String,android.os.Bundle)).

Example use:  

```kotlin
Firebase.analytics.logEvent("myEvent") {
  param(Params.VALUE, 3.99)
  param(Params.CURRENCY, "USD")
}
```  

### setConsent

```
inlineÂ funÂ FirebaseAnalytics.setConsent(crossinlineÂ block:Â ConsentBuilder.() -> Unit):Â Unit
```

Fluent version of [FirebaseAnalytics.setConsent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics#setConsent(kotlin.collections.MutableMap)).

Example use:  

```kotlin
Firebase.analytics.setConsent {
  adStorage = ConsentStatus.GRANTED
  analyticsStorage = ConsentStatus.GRANTED
  adUserData = ConsentStatus.GRANTED
  adPersonalization = ConsentStatus.GRANTED
}
```