# Source: https://firebase.google.com/docs/reference/cpp/group/user-property-names.md.txt

# Source: https://firebase.google.com/docs/reference/unity/group/user-property-names.md.txt

# Analytics User Properties

# Analytics User Properties

Predefined user property names.

## Summary

A UserProperty is an attribute that describes the app-user. By supplying UserProperties, you can later analyze different behaviors of various segments of your userbase. You may supply up to 25 unique UserProperties per app, and you can use the name and value of your choosing for each one. UserProperty names can be up to 24 characters long, may only contain alphanumeric characters and underscores ("_"), and must start with an alphabetic character. UserProperty values can be up to 36 characters long. The "firebase_", "google_", and "ga_" prefixes are reserved and should not be used.

|                                                                                                                                                                                                                   ### Variables                                                                                                                                                                                                                    ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [UserPropertyAllowAdPersonalizationSignals](https://firebase.google.com/docs/reference/unity/group/user-property-names#group__user__property__names_1gae84a687de309c83dabf27ca65dd18b0e)` = "allow_personalized_ads"` | `string` Indicates whether events logged by Google [Analytics](https://firebase.google.com/docs/reference/unity/namespace/firebase/analytics#namespace_firebase_1_1_analytics) can be used to personalize ads for the user. |
| [UserPropertySignUpMethod](https://firebase.google.com/docs/reference/unity/group/user-property-names#group__user__property__names_1ga58850cee496acc02fbf1cc788b45df32)` = "sign_up_method"`                          | `string` The method used to sign in.                                                                                                                                                                                        |

## Variables

### UserPropertyAllowAdPersonalizationSignals

```c#
string UserPropertyAllowAdPersonalizationSignals = "allow_personalized_ads"
```  
Indicates whether events logged by Google [Analytics](https://firebase.google.com/docs/reference/unity/namespace/firebase/analytics#namespace_firebase_1_1_analytics) can be used to personalize ads for the user.

Set to "YES" to enable, or "NO" to disable. Default is enabled. See the [documentation](https://firebase.google.com/support/guides/disable-analytics) for more details and information about related settings.


```c#
Analytics.setUserProperty("NO", forName: AnalyticsUserPropertyAllowAdPersonalizationSignals)
```

<br />

### UserPropertySignUpMethod

```c#
string UserPropertySignUpMethod = "sign_up_method"
```  
The method used to sign in.

For example, "google", "facebook" or "twitter".