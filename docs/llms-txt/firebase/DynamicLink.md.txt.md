# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.md.txt

# DynamicLink

# DynamicLink


```
public final class DynamicLink
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Contains Builders for constructing Dynamic Links. Returned by `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.Builder#buildDynamicLink()` with the constructed Dynamic Link.

## Summary

| ### Nested types |
|---|
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters` **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder` **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.Builder` **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.GoogleAnalyticsParameters` **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.GoogleAnalyticsParameters.Builder` **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.IosParameters` **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder` **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.ItunesConnectAnalyticsParameters` **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.ItunesConnectAnalyticsParameters.Builder` **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters` **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters.Builder` **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.SocialMetaTagParameters` **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.SocialMetaTagParameters.Builder` **This class is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/net/Uri.html` | `[getUri](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink#getUri())()` **This method is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |

## Public methods

### getUri

```
public @NonNull Uri [getUri](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink#getUri())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Gets the Uri for this Dynamic Link.

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html java.lang.IllegalArgumentException` | if the FDL domain is not set. Set with `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.Builder#setDynamicLinkDomain(java.lang.String)`. |