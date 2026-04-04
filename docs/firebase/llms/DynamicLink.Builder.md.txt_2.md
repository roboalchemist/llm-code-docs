# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder.md.txt

# DynamicLink.Builder

# DynamicLink.Builder


```
class DynamicLink.Builder
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Builder for creating Dynamic Links.

## Summary

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink` | `[buildDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#buildDynamicLink())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink!>` | `[buildShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#buildShortDynamicLink())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink!>` | `[buildShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#buildShortDynamicLink(int))(@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink.Suffix suffix: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `[getDomainUriPrefix](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#getDomainUriPrefix())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://developer.android.com/reference/kotlin/android/net/Uri.html` | `[getLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#getLink())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://developer.android.com/reference/kotlin/android/net/Uri.html` | `[getLongLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#getLongLink())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder` | `[setAndroidParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setAndroidParameters(com.google.firebase.dynamiclinks.DynamicLink.AndroidParameters))(androidParameters: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder` | `[setDomainUriPrefix](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setDomainUriPrefix(java.lang.String))(domainUriPrefix: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder` | `[setDynamicLinkDomain](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setDynamicLinkDomain(java.lang.String))(dynamicLinkDomain: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` **This function is deprecated.** Use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setDomainUriPrefix(java.lang.String)` instead <br /> |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder` | `[setGoogleAnalyticsParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setGoogleAnalyticsParameters(com.google.firebase.dynamiclinks.DynamicLink.GoogleAnalyticsParameters))( googleAnalyticsParameters: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.GoogleAnalyticsParameters )` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder` | `[setIosParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setIosParameters(com.google.firebase.dynamiclinks.DynamicLink.IosParameters))(iosParameters: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder` | `[setItunesConnectAnalyticsParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setItunesConnectAnalyticsParameters(com.google.firebase.dynamiclinks.DynamicLink.ItunesConnectAnalyticsParameters))( itunesConnectAnalyticsParameters: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.ItunesConnectAnalyticsParameters )` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder` | `[setLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setLink(android.net.Uri))(link: https://developer.android.com/reference/kotlin/android/net/Uri.html)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder` | `[setLongLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setLongLink(android.net.Uri))(longLink: https://developer.android.com/reference/kotlin/android/net/Uri.html)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder` | `[setNavigationInfoParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setNavigationInfoParameters(com.google.firebase.dynamiclinks.DynamicLink.NavigationInfoParameters))( navigationInfoParameters: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters )` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder` | `[setSocialMetaTagParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setSocialMetaTagParameters(com.google.firebase.dynamiclinks.DynamicLink.SocialMetaTagParameters))( socialMetaTagParameters: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.SocialMetaTagParameters )` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |

| ### Extension functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder.[androidParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).androidParameters(kotlin.Function1))(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).androidParameters(kotlin.Function1)` function and sets it to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder.[androidParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).androidParameters(kotlin.String,kotlin.Function1))( packageName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html )` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters` object initialized with the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).androidParameters(kotlin.String,kotlin.Function1)` and using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).androidParameters(kotlin.String,kotlin.Function1)` function and sets it to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder.[androidParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).androidParameters(kotlin.Function1))(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder.[androidParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).androidParameters(kotlin.String,kotlin.Function1))( packageName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html )` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder.[googleAnalyticsParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).googleAnalyticsParameters(kotlin.Function1))(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.GoogleAnalyticsParameters.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.GoogleAnalyticsParameters` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).googleAnalyticsParameters(kotlin.Function1)` function and sets it to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder.[googleAnalyticsParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).googleAnalyticsParameters(kotlin.String,kotlin.String,kotlin.String,kotlin.Function1))( source: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, medium: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, campaign: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.GoogleAnalyticsParameters.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html )` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.GoogleAnalyticsParameters` object initialized with the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).googleAnalyticsParameters(kotlin.String,kotlin.String,kotlin.String,kotlin.Function1)`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).googleAnalyticsParameters(kotlin.String,kotlin.String,kotlin.String,kotlin.Function1)`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).googleAnalyticsParameters(kotlin.String,kotlin.String,kotlin.String,kotlin.Function1)` and using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).googleAnalyticsParameters(kotlin.String,kotlin.String,kotlin.String,kotlin.Function1)` function and sets it to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder.[googleAnalyticsParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).googleAnalyticsParameters(kotlin.Function1))(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.GoogleAnalyticsParameters.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder.[googleAnalyticsParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).googleAnalyticsParameters(kotlin.String,kotlin.String,kotlin.String,kotlin.Function1))( source: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, medium: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, campaign: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.GoogleAnalyticsParameters.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html )` **This function is deprecated.** com.google.firebase.dynam |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder.[iosParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).iosParameters(kotlin.String,kotlin.Function1))(bundleId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters` object initialized with the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).iosParameters(kotlin.String,kotlin.Function1)` and using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).iosParameters(kotlin.String,kotlin.Function1)` function and sets it to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder.[iosParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).iosParameters(kotlin.String,kotlin.Function1))(bundleId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder.[itunesConnectAnalyticsParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).itunesConnectAnalyticsParameters(kotlin.Function1))(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.ItunesConnectAnalyticsParameters.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.ItunesConnectAnalyticsParameters` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).itunesConnectAnalyticsParameters(kotlin.Function1)` function and sets it to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder.[itunesConnectAnalyticsParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).itunesConnectAnalyticsParameters(kotlin.Function1))(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.ItunesConnectAnalyticsParameters.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder.[navigationInfoParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).navigationInfoParameters(kotlin.Function1))(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).navigationInfoParameters(kotlin.Function1)` function and sets it to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder.[navigationInfoParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).navigationInfoParameters(kotlin.Function1))(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder.[socialMetaTagParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).socialMetaTagParameters(kotlin.Function1))(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.SocialMetaTagParameters.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.SocialMetaTagParameters` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).socialMetaTagParameters(kotlin.Function1)` function and sets it to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder.[socialMetaTagParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).socialMetaTagParameters(kotlin.Function1))(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.SocialMetaTagParameters.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Public functions

### buildDynamicLink

```
fun [buildDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#buildDynamicLink())(): DynamicLink
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Creates a Dynamic Link from the parameters.

| Throws |
|---|---|
| `java.lang.IllegalArgumentException: https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html` | if the FDL domain is not set. Set with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setDynamicLinkDomain(java.lang.String)`. |

### buildShortDynamicLink

```
fun [buildShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#buildShortDynamicLink())(): Task<ShortDynamicLink!>
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Creates a shortened Dynamic Link from the parameters.

| Throws |
|---|---|
| `java.lang.IllegalArgumentException: https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html` | if the FDL domain and api key are not set. Set FDL domain with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setDynamicLinkDomain(java.lang.String)`. Ensure that google-services.json file is setup for the app if the api key is not set. |

### buildShortDynamicLink

```
fun [buildShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#buildShortDynamicLink(int))(@ShortDynamicLink.Suffix suffix: Int): Task<ShortDynamicLink!>
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Creates a shortened Dynamic Link from the parameters.

| Parameters |
|---|---|
| `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink.Suffix suffix: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The desired length of the Dynamic Link. One of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink.Suffix#UNGUESSABLE()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink.Suffix#SHORT()`. |

| Throws |
|---|---|
| `java.lang.IllegalArgumentException: https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html` | if the FDL domain and api key are not set. Set FDL domain with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setDynamicLinkDomain(java.lang.String)`. Ensure that google-services.json file is setup for the app if the api key is not set. |

### getDomainUriPrefix

```
fun [getDomainUriPrefix](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#getDomainUriPrefix())(): String
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Returns the deep link set to this DynamicLink.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the deep link set to this DynamicLink. |

### getLink

```
fun [getLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#getLink())(): Uri
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Return the deep link associated with this DynamicLink.

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/android/net/Uri.html` | the deep link associated with this DynamicLink. |

### getLongLink

```
fun [getLongLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#getLongLink())(): Uri
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Return the long Dynamic link associated with this DynamicLink.

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/android/net/Uri.html` | the long Dynamic link associated with this DynamicLink. |

### setAndroidParameters

```
fun [setAndroidParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setAndroidParameters(com.google.firebase.dynamiclinks.DynamicLink.AndroidParameters))(androidParameters: DynamicLink.AndroidParameters): DynamicLink.Builder
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Sets the Android parameters.

| Parameters |
|---|---|
| `androidParameters: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters` | The AndroidParameters from `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#build()`. |

### setDomainUriPrefix

```
fun [setDomainUriPrefix](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setDomainUriPrefix(java.lang.String))(domainUriPrefix: String): DynamicLink.Builder
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Sets the domain uri prefix (of the form "https://xyz.app.goo.gl", "https://custom.com/xyz") to use for this Dynamic Link.

| Parameters |
|---|---|
| `domainUriPrefix: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The target project's Domain Uri Prefix. You can find this value in the Dynamic Links section of the Firebase console. |

### setDynamicLinkDomain

```
fun [setDynamicLinkDomain](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setDynamicLinkDomain(java.lang.String))(dynamicLinkDomain: String): DynamicLink.Builder
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setDomainUriPrefix(java.lang.String)` instead

Sets the domain (of the form "xyz.app.goo.gl") to use for this Dynamic Link. Only applicable for \*.page.link and \*.app.goo.gl, use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setDomainUriPrefix(java.lang.String)` if domain is custom.

| Parameters |
|---|---|
| `dynamicLinkDomain: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The target project's Dynamic Links domain. You can find this value in the Dynamic Links section of the Firebase console. |

### setGoogleAnalyticsParameters

```
fun [setGoogleAnalyticsParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setGoogleAnalyticsParameters(com.google.firebase.dynamiclinks.DynamicLink.GoogleAnalyticsParameters))(
    googleAnalyticsParameters: DynamicLink.GoogleAnalyticsParameters
): DynamicLink.Builder
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Sets the Google Analytics parameters.

| Parameters |
|---|---|
| `googleAnalyticsParameters: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.GoogleAnalyticsParameters` | The GoogleAnalyticsParameters from `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.GoogleAnalyticsParameters.Builder#build()`. |

### setIosParameters

```
fun [setIosParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setIosParameters(com.google.firebase.dynamiclinks.DynamicLink.IosParameters))(iosParameters: DynamicLink.IosParameters): DynamicLink.Builder
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Sets the iOS parameters.

| Parameters |
|---|---|
| `iosParameters: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters` | The IosParameters from `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#build()`. |

### setItunesConnectAnalyticsParameters

```
fun [setItunesConnectAnalyticsParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setItunesConnectAnalyticsParameters(com.google.firebase.dynamiclinks.DynamicLink.ItunesConnectAnalyticsParameters))(
    itunesConnectAnalyticsParameters: DynamicLink.ItunesConnectAnalyticsParameters
): DynamicLink.Builder
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Sets the iTunes Connect App Analytics parameters.

| Parameters |
|---|---|
| `itunesConnectAnalyticsParameters: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.ItunesConnectAnalyticsParameters` | The ItunesConnectAnalyticsParameters from `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.ItunesConnectAnalyticsParameters.Builder#build()`. |

### setLink

```
fun [setLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setLink(android.net.Uri))(link: Uri): DynamicLink.Builder
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Set the deep link.

| Parameters |
|---|---|
| `link: https://developer.android.com/reference/kotlin/android/net/Uri.html` | The link your app will open. You can specify any URL your app can handle, such as a link to your app's content, or a URL that initiates some app-specific logic such as crediting the user with a coupon, or displaying a specific welcome screen. This link must be a well-formatted URL, be properly URL-encoded, and use the HTTP or HTTPS scheme. |

### setLongLink

```
fun [setLongLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setLongLink(android.net.Uri))(longLink: Uri): DynamicLink.Builder
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Set the long Dynamic Link. This can be used with buildShortDynamicLink to shorten an existing long FDL into a short FDL.

| Parameters |
|---|---|
| `longLink: https://developer.android.com/reference/kotlin/android/net/Uri.html` | The long FDL to shorten. |

### setNavigationInfoParameters

```
fun [setNavigationInfoParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setNavigationInfoParameters(com.google.firebase.dynamiclinks.DynamicLink.NavigationInfoParameters))(
    navigationInfoParameters: DynamicLink.NavigationInfoParameters
): DynamicLink.Builder
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Sets the navigation info parameters.

| Parameters |
|---|---|
| `navigationInfoParameters: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters` | The NavigationInfoParameters from `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters.Builder#build()`. |

### setSocialMetaTagParameters

```
fun [setSocialMetaTagParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setSocialMetaTagParameters(com.google.firebase.dynamiclinks.DynamicLink.SocialMetaTagParameters))(
    socialMetaTagParameters: DynamicLink.SocialMetaTagParameters
): DynamicLink.Builder
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Sets the social meta-tag parameters.

| Parameters |
|---|---|
| `socialMetaTagParameters: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.SocialMetaTagParameters` | The SocialMetaTagParameters from `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.SocialMetaTagParameters.Builder#build()`. |

## Extension functions

### androidParameters

```
fun DynamicLink.Builder.[androidParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).androidParameters(kotlin.Function1))(init: DynamicLink.AndroidParameters.Builder.() -> Unit): Unit
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).androidParameters(kotlin.Function1)` function and sets it to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder`

### androidParameters

```
fun DynamicLink.Builder.[androidParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).androidParameters(kotlin.String,kotlin.Function1))(
    packageName: String,
    init: DynamicLink.AndroidParameters.Builder.() -> Unit
): Unit
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters` object initialized with the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).androidParameters(kotlin.String,kotlin.Function1)` and using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).androidParameters(kotlin.String,kotlin.Function1)` function and sets it to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder`

### androidParameters

```
fun DynamicLink.Builder.[androidParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).androidParameters(kotlin.Function1))(init: DynamicLink.AndroidParameters.Builder.() -> Unit): Unit
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ktx/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).androidParameters(kotlin.Function1)` function and sets it to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder`

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### androidParameters

```
fun DynamicLink.Builder.[androidParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).androidParameters(kotlin.String,kotlin.Function1))(
    packageName: String,
    init: DynamicLink.AndroidParameters.Builder.() -> Unit
): Unit
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters` object initialized with the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ktx/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).androidParameters(kotlin.String,kotlin.Function1)` and using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ktx/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).androidParameters(kotlin.String,kotlin.Function1)` function and sets it to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder`

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### googleAnalyticsParameters

```
fun DynamicLink.Builder.[googleAnalyticsParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).googleAnalyticsParameters(kotlin.Function1))(init: DynamicLink.GoogleAnalyticsParameters.Builder.() -> Unit): Unit
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.GoogleAnalyticsParameters` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).googleAnalyticsParameters(kotlin.Function1)` function and sets it to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder`

### googleAnalyticsParameters

```
fun DynamicLink.Builder.[googleAnalyticsParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).googleAnalyticsParameters(kotlin.String,kotlin.String,kotlin.String,kotlin.Function1))(
    source: String,
    medium: String,
    campaign: String,
    init: DynamicLink.GoogleAnalyticsParameters.Builder.() -> Unit
): Unit
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.GoogleAnalyticsParameters` object initialized with the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).googleAnalyticsParameters(kotlin.String,kotlin.String,kotlin.String,kotlin.Function1)`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).googleAnalyticsParameters(kotlin.String,kotlin.String,kotlin.String,kotlin.Function1)`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).googleAnalyticsParameters(kotlin.String,kotlin.String,kotlin.String,kotlin.Function1)` and using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).googleAnalyticsParameters(kotlin.String,kotlin.String,kotlin.String,kotlin.Function1)` function and sets it to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder`.

### googleAnalyticsParameters

```
fun DynamicLink.Builder.[googleAnalyticsParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).googleAnalyticsParameters(kotlin.Function1))(init: DynamicLink.GoogleAnalyticsParameters.Builder.() -> Unit): Unit
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.GoogleAnalyticsParameters` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ktx/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).googleAnalyticsParameters(kotlin.Function1)` function and sets it to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder`

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### googleAnalyticsParameters

```
fun DynamicLink.Builder.[googleAnalyticsParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).googleAnalyticsParameters(kotlin.String,kotlin.String,kotlin.String,kotlin.Function1))(
    source: String,
    medium: String,
    campaign: String,
    init: DynamicLink.GoogleAnalyticsParameters.Builder.() -> Unit
): Unit
```

> [!CAUTION]
> **This function is deprecated.**   
> com.google.firebase.dynam

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.GoogleAnalyticsParameters` object initialized with the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ktx/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).googleAnalyticsParameters(kotlin.String,kotlin.String,kotlin.String,kotlin.Function1)`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ktx/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).googleAnalyticsParameters(kotlin.String,kotlin.String,kotlin.String,kotlin.Function1)`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ktx/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).googleAnalyticsParameters(kotlin.String,kotlin.String,kotlin.String,kotlin.Function1)` and using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ktx/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).googleAnalyticsParameters(kotlin.String,kotlin.String,kotlin.String,kotlin.Function1)` function and sets it to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder`.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### iosParameters

```
fun DynamicLink.Builder.[iosParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).iosParameters(kotlin.String,kotlin.Function1))(bundleId: String, init: DynamicLink.IosParameters.Builder.() -> Unit): Unit
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters` object initialized with the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).iosParameters(kotlin.String,kotlin.Function1)` and using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).iosParameters(kotlin.String,kotlin.Function1)` function and sets it to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder`

### iosParameters

```
fun DynamicLink.Builder.[iosParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).iosParameters(kotlin.String,kotlin.Function1))(bundleId: String, init: DynamicLink.IosParameters.Builder.() -> Unit): Unit
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters` object initialized with the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ktx/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).iosParameters(kotlin.String,kotlin.Function1)` and using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ktx/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).iosParameters(kotlin.String,kotlin.Function1)` function and sets it to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder`

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### itunesConnectAnalyticsParameters

```
fun DynamicLink.Builder.[itunesConnectAnalyticsParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).itunesConnectAnalyticsParameters(kotlin.Function1))(init: DynamicLink.ItunesConnectAnalyticsParameters.Builder.() -> Unit): Unit
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.ItunesConnectAnalyticsParameters` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).itunesConnectAnalyticsParameters(kotlin.Function1)` function and sets it to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder`

### itunesConnectAnalyticsParameters

```
fun DynamicLink.Builder.[itunesConnectAnalyticsParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).itunesConnectAnalyticsParameters(kotlin.Function1))(init: DynamicLink.ItunesConnectAnalyticsParameters.Builder.() -> Unit): Unit
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.ItunesConnectAnalyticsParameters` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ktx/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).itunesConnectAnalyticsParameters(kotlin.Function1)` function and sets it to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder`

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### navigationInfoParameters

```
fun DynamicLink.Builder.[navigationInfoParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).navigationInfoParameters(kotlin.Function1))(init: DynamicLink.NavigationInfoParameters.Builder.() -> Unit): Unit
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).navigationInfoParameters(kotlin.Function1)` function and sets it to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder`

### navigationInfoParameters

```
fun DynamicLink.Builder.[navigationInfoParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).navigationInfoParameters(kotlin.Function1))(init: DynamicLink.NavigationInfoParameters.Builder.() -> Unit): Unit
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ktx/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).navigationInfoParameters(kotlin.Function1)` function and sets it to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder`

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

### socialMetaTagParameters

```
fun DynamicLink.Builder.[socialMetaTagParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).socialMetaTagParameters(kotlin.Function1))(init: DynamicLink.SocialMetaTagParameters.Builder.() -> Unit): Unit
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.SocialMetaTagParameters` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).socialMetaTagParameters(kotlin.Function1)` function and sets it to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder`

### socialMetaTagParameters

```
fun DynamicLink.Builder.[socialMetaTagParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#(com.google.firebase.dynamiclinks.DynamicLink.Builder).socialMetaTagParameters(kotlin.Function1))(init: DynamicLink.SocialMetaTagParameters.Builder.() -> Unit): Unit
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.SocialMetaTagParameters` object initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ktx/package-summary#(com.google.firebase.dynamiclinks.DynamicLink.Builder).socialMetaTagParameters(kotlin.Function1)` function and sets it to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder`

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)