# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder.md.txt

# DynamicLink.AndroidParameters.Builder

# DynamicLink.AndroidParameters.Builder


```
class DynamicLink.AndroidParameters.Builder
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Builder for Android parameters.

## Summary

| ### Public constructors |
|---|
| `[Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#Builder())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `[Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#Builder(java.lang.String))(packageName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters` | `[build](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#build())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://developer.android.com/reference/kotlin/android/net/Uri.html` | `[getFallbackUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#getFallbackUrl())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `[getMinimumVersion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#getMinimumVersion())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder` | `[setFallbackUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#setFallbackUrl(android.net.Uri))(fallbackUrl: https://developer.android.com/reference/kotlin/android/net/Uri.html)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder` | `[setMinimumVersion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#setMinimumVersion(int))(minimumVersion: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |

## Public constructors

### Builder

```
[Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#Builder())()
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Create Android parameters builder, using the package name of the calling app. The app must be connected to your project from the Overview page of the Firebase console.

| Throws |
|---|---|
| `java.lang.IllegalStateException: https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html` | if FirebaseApp has not been initialized correctly. |

### Builder

```
[Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#Builder(java.lang.String))(packageName: String)
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Create Android parameters builder.

| Parameters |
|---|---|
| `packageName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The package name of the Android app to use to open the link. The app must be connected to your project from the Overview page of the Firebase console. |

## Public functions

### build

```
fun [build](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#build())(): DynamicLink.AndroidParameters
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Build AndroidParameters for use with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setAndroidParameters(com.google.firebase.dynamiclinks.DynamicLink.AndroidParameters)`.

### getFallbackUrl

```
fun [getFallbackUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#getFallbackUrl())(): Uri
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Returns the link to open on Android if the app isn't installed.

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/android/net/Uri.html` | the link to open on Android if the app isn't installed. |

### getMinimumVersion

```
fun [getMinimumVersion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#getMinimumVersion())(): Int
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Returns the minimum version of your app that can open the link.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | the minimum version of your app that can open the link. |

### setFallbackUrl

```
fun [setFallbackUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#setFallbackUrl(android.net.Uri))(fallbackUrl: Uri): DynamicLink.AndroidParameters.Builder
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Sets the link to open when the app isn't installed. Specify this to do something other than install your app from the Play Store when the app isn't installed, such as open the mobile web version of the content, or display a promotional page for your app.

| Parameters |
|---|---|
| `fallbackUrl: https://developer.android.com/reference/kotlin/android/net/Uri.html` | The link to open on Android if the app is not installed. |

### setMinimumVersion

```
fun [setMinimumVersion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#setMinimumVersion(int))(minimumVersion: Int): DynamicLink.AndroidParameters.Builder
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Sets the versionCode of the minimum version of your app that can open the link.

| Parameters |
|---|---|
| `minimumVersion: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The minimum version. |