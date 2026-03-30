# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder.md.txt

# DynamicLink.IosParameters.Builder

# DynamicLink.IosParameters.Builder


```
class DynamicLink.IosParameters.Builder
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Builder for iOS parameters.

## Summary

| ### Public constructors |
|---|
| `[Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#Builder(java.lang.String))(bundleId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters` | `[build](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#build())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `[getAppStoreId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#getAppStoreId())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `[getCustomScheme](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#getCustomScheme())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `[getIpadBundleId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#getIpadBundleId())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://developer.android.com/reference/kotlin/android/net/Uri.html` | `[getIpadFallbackUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#getIpadFallbackUrl())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `[getMinimumVersion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#getMinimumVersion())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder` | `[setAppStoreId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#setAppStoreId(java.lang.String))(appStoreId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder` | `[setCustomScheme](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#setCustomScheme(java.lang.String))(customScheme: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder` | `[setFallbackUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#setFallbackUrl(android.net.Uri))(fallbackUrl: https://developer.android.com/reference/kotlin/android/net/Uri.html)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder` | `[setIpadBundleId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#setIpadBundleId(java.lang.String))(bundleId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder` | `[setIpadFallbackUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#setIpadFallbackUrl(android.net.Uri))(fallbackUrl: https://developer.android.com/reference/kotlin/android/net/Uri.html)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder` | `[setMinimumVersion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#setMinimumVersion(java.lang.String))(minimumVersion: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |

## Public constructors

### Builder

```
[Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#Builder(java.lang.String))(bundleId: String)
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Create iOS parameters builder.

| Parameters |
|---|---|
| `bundleId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The bundle ID of the iOS app to use to open the link. The app must be connected to your project from the Overview page of the Firebase console. |

## Public functions

### build

```
fun [build](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#build())(): DynamicLink.IosParameters
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Build IosParameters for use with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setIosParameters(com.google.firebase.dynamiclinks.DynamicLink.IosParameters)`.

### getAppStoreId

```
fun [getAppStoreId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#getAppStoreId())(): String
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).d.

Returns the App Store ID, used to send users to the App Store when the app isn't installed

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the App Store ID, used to send users to the App Store when the app isn't installed. |

### getCustomScheme

```
fun [getCustomScheme](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#getCustomScheme())(): String
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Returns the app's custom URL scheme.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the app's custom URL scheme. |

### getIpadBundleId

```
fun [getIpadBundleId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#getIpadBundleId())(): String
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Returns the iPad bundle ID of the app.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the iPad bundle ID of the app. |

### getIpadFallbackUrl

```
fun [getIpadFallbackUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#getIpadFallbackUrl())(): Uri
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Returns the link to open on iPad if the app is not installed.

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/android/net/Uri.html` | the link to open on iPad if the app is not installed. |

### getMinimumVersion

```
fun [getMinimumVersion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#getMinimumVersion())(): String
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Returns the minimum version of your app that can open the link.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the minimum version of your app that can open the link. |

### setAppStoreId

```
fun [setAppStoreId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#setAppStoreId(java.lang.String))(appStoreId: String): DynamicLink.IosParameters.Builder
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Sets the App Store ID, used to send users to the App Store when the app isn't installed.

| Parameters |
|---|---|
| `appStoreId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The App Store ID. |

### setCustomScheme

```
fun [setCustomScheme](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#setCustomScheme(java.lang.String))(customScheme: String): DynamicLink.IosParameters.Builder
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Sets the app's custom URL scheme, if defined to be something other than your app's bundle ID.

| Parameters |
|---|---|
| `customScheme: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The app's custom URL scheme. |

### setFallbackUrl

```
fun [setFallbackUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#setFallbackUrl(android.net.Uri))(fallbackUrl: Uri): DynamicLink.IosParameters.Builder
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Sets the link to open when the app isn't installed. Specify this to do something other than install your app from the App Store when the app isn't installed, such as open the mobile web version of the content, or display a promotional page for your app.

| Parameters |
|---|---|
| `fallbackUrl: https://developer.android.com/reference/kotlin/android/net/Uri.html` | The link to open on iOS if the app is not installed. |

### setIpadBundleId

```
fun [setIpadBundleId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#setIpadBundleId(java.lang.String))(bundleId: String): DynamicLink.IosParameters.Builder
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Sets the bundle ID of the iOS app to use on iPads to open the link. The app must be connected to your project from the Overview page of the Firebase console.

| Parameters |
|---|---|
| `bundleId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The iPad bundle ID of the app. |

### setIpadFallbackUrl

```
fun [setIpadFallbackUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#setIpadFallbackUrl(android.net.Uri))(fallbackUrl: Uri): DynamicLink.IosParameters.Builder
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Sets the link to open on iPads when the app isn't installed. Specify this to do something other than install your app from the App Store when the app isn't installed, such as open the web version of the content, or display a promotional page for your app. Overrides the fallback link set by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#setFallbackUrl(android.net.Uri)` on iPad.

| Parameters |
|---|---|
| `fallbackUrl: https://developer.android.com/reference/kotlin/android/net/Uri.html` | The link to open on iPad if the app is not installed. |

### setMinimumVersion

```
fun [setMinimumVersion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.IosParameters.Builder#setMinimumVersion(java.lang.String))(minimumVersion: String): DynamicLink.IosParameters.Builder
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Sets the minimum version of your app that can open the link.

| Parameters |
|---|---|
| `minimumVersion: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The minimum version. |