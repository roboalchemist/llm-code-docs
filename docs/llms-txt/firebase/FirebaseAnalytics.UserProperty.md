# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.UserProperty.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.UserProperty.md.txt

# FirebaseAnalytics.UserProperty

# FirebaseAnalytics.UserProperty


```
class FirebaseAnalytics.UserProperty
```

<br />

*** ** * ** ***

A UserProperty is an attribute that describes the app-user. By supplying UserProperties, you can later analyze different behaviors of various segments of your user base. You may supply up to 25 unique UserProperties per app, and you can use the name and value of your choosing for each one. UserProperty names can be up to 24 characters long, may only contain [alphanumeric](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetterOrDigit-int-) characters and underscores ("_"), and must start with an [alphabetic](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetter-int-) character. UserProperty values can be up to 36 characters long. The "firebase_", "google_" and "ga_" prefixes are reserved and should not be used.

The following user property names are reserved and cannot be used:

- first_open_time
- first_visit_time
- last_deep_link_referrer
- user_id
- first_open_after_install

## Summary

|                                        ### Constants                                        |
|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [ALLOW_AD_PERSONALIZATION_SIGNALS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.UserProperty#ALLOW_AD_PERSONALIZATION_SIGNALS())` = "allow_personalized_ads"` Indicates whether events logged by Google Analytics can be used to personalize ads for the user. |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [SIGN_UP_METHOD](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.UserProperty#SIGN_UP_METHOD())` = "sign_up_method"` The method used to sign in.                                                                                                                  |

|                                                            ### Protected constructors                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------|
| [UserProperty](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.UserProperty#UserProperty())`()` |

## Constants

### ALLOW_AD_PERSONALIZATION_SIGNALS

```
constÂ valÂ ALLOW_AD_PERSONALIZATION_SIGNALS = "allow_personalized_ads":Â String!
```

Indicates whether events logged by Google Analytics can be used to personalize ads for the user. Set to "true" to enable, or "false" to disable. Default is enabled. See the [documentation](https://firebase.google.com/support/guides/disable-analytics) for more details and information about related settings.  

### SIGN_UP_METHOD

```
constÂ valÂ SIGN_UP_METHOD = "sign_up_method":Â String!
```

The method used to sign in. For example, "google", "facebook" or "twitter".  

## Protected constructors

### UserProperty

```
protectedÂ UserProperty()
```