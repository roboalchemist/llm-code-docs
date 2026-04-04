# Source: https://firebase.google.com/docs/reference/cpp/group/user-property-names.md.txt

# Analytics User Properties

# Analytics User Properties

Predefined user property names.

## Summary

A UserProperty is an attribute that describes the app-user. By supplying UserProperties, you can later analyze different behaviors of various segments of your userbase. You may supply up to 25 unique UserProperties per app, and you can use the name and value of your choosing for each one. UserProperty names can be up to 24 characters long, may only contain alphanumeric characters and underscores ("_"), and must start with an alphabetic character. UserProperty values can be up to 36 characters long. The "firebase_", "google_", and "ga_" prefixes are reserved and should not be used.

| ### Variables ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/group/user-property-names#group__user__property__names_1gaa576972ee95a7acee21444556870b95c = "allow_personalized_ads"` | `const char *const` Indicates whether events logged by Google Analytics can be used to personalize ads for the user. |
| `https://firebase.google.com/docs/reference/cpp/group/user-property-names#group__user__property__names_1ga2c3ee5a8891ee5ef3cd68156cca94e81 = "sign_up_method"` | `const char *const` The method used to sign in. |

## Variables

### kUserPropertyAllowAdPersonalizationSignals

```c++
const char *const kUserPropertyAllowAdPersonalizationSignals = "allow_personalized_ads"
```
Indicates whether events logged by Google Analytics can be used to personalize ads for the user.

Set to "YES" to enable, or "NO" to disable. Default is enabled. See the [documentation](https://firebase.google.com/support/guides/disable-analytics) for more details and information about related settings.


```c++
Analytics.setUserProperty("NO", forName: AnalyticsUserPropertyAllowAdPersonalizationSignals)
```

<br />

### kUserPropertySignUpMethod

```c++
const char *const kUserPropertySignUpMethod = "sign_up_method"
```
The method used to sign in.

For example, "google", "facebook" or "twitter".