# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLink.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLink.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.md.txt

# DynamicLink

# DynamicLink


```
class DynamicLink
```

<br />

*** ** * ** ***

| **This class is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Contains Builders for constructing Dynamic Links. Returned by [buildDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#buildDynamicLink()) with the constructed Dynamic Link.

## Summary

|                                                                                                                                                     ### Nested types                                                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `class `[DynamicLink.AndroidParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters) **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />                                               |
| `class `[DynamicLink.AndroidParameters.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder) **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />                               |
| `class `[DynamicLink.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder) **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />                                                                   |
| `class `[DynamicLink.GoogleAnalyticsParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.GoogleAnalyticsParameters) **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />                               |
| `class `[DynamicLink.GoogleAnalyticsParameters.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.GoogleAnalyticsParameters.Builder) **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />               |
| `class `[DynamicLink.IosParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters) **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />                                                       |
| `class `[DynamicLink.IosParameters.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder) **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />                                       |
| `class `[DynamicLink.ItunesConnectAnalyticsParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.ItunesConnectAnalyticsParameters) **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />                 |
| `class `[DynamicLink.ItunesConnectAnalyticsParameters.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.ItunesConnectAnalyticsParameters.Builder) **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `class `[DynamicLink.NavigationInfoParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters) **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />                                 |
| `class `[DynamicLink.NavigationInfoParameters.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters.Builder) **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />                 |
| `class `[DynamicLink.SocialMetaTagParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.SocialMetaTagParameters) **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />                                   |
| `class `[DynamicLink.SocialMetaTagParameters.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.SocialMetaTagParameters.Builder) **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />                   |

|                            ### Public functions                            |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html) | ~~[getUri](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink#getUri())~~`()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |

## Public functions

### getUri

```
funÂ [getUri](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink#getUri())():Â Uri
```
| **This function is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Gets the Uri for this Dynamic Link.  

|                                                                               Throws                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java.lang.IllegalArgumentException: `[java.lang.IllegalArgumentException](https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html) | if the FDL domain is not set. Set with [setDynamicLinkDomain](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setDynamicLinkDomain(java.lang.String)). |