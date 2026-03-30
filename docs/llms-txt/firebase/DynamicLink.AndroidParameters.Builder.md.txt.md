# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder.md.txt

# DynamicLink.AndroidParameters.Builder

# DynamicLink.AndroidParameters.Builder


```
public final class DynamicLink.AndroidParameters.Builder
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
| `[Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#Builder())()` **This method is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `[Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#Builder(java.lang.String))(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html packageName)` **This method is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters` | `[build](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#build())()` **This method is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/net/Uri.html` | `[getFallbackUrl](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#getFallbackUrl())()` **This method is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `int` | `[getMinimumVersion](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#getMinimumVersion())()` **This method is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder` | `[setFallbackUrl](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#setFallbackUrl(android.net.Uri))(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/net/Uri.html fallbackUrl)` **This method is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder` | `[setMinimumVersion](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#setMinimumVersion(int))(int minimumVersion)` **This method is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |

## Public constructors

### Builder

```
public [Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#Builder())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Create Android parameters builder, using the package name of the calling app. The app must be connected to your project from the Overview page of the Firebase console.

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html java.lang.IllegalStateException` | if FirebaseApp has not been initialized correctly. |

### Builder

```
public [Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#Builder(java.lang.String))(@NonNull String packageName)
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Create Android parameters builder.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html packageName` | The package name of the Android app to use to open the link. The app must be connected to your project from the Overview page of the Firebase console. |

## Public methods

### build

```
public @NonNull DynamicLink.AndroidParameters [build](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#build())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Build AndroidParameters for use with `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.Builder#setAndroidParameters(com.google.firebase.dynamiclinks.DynamicLink.AndroidParameters)`.

### getFallbackUrl

```
public @NonNull Uri [getFallbackUrl](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#getFallbackUrl())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Returns the link to open on Android if the app isn't installed.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/net/Uri.html` | the link to open on Android if the app isn't installed. |

### getMinimumVersion

```
public int [getMinimumVersion](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#getMinimumVersion())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Returns the minimum version of your app that can open the link.

| Returns |
|---|---|
| `int` | the minimum version of your app that can open the link. |

### setFallbackUrl

```
public @NonNull DynamicLink.AndroidParameters.Builder [setFallbackUrl](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#setFallbackUrl(android.net.Uri))(@NonNull Uri fallbackUrl)
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Sets the link to open when the app isn't installed. Specify this to do something other than install your app from the Play Store when the app isn't installed, such as open the mobile web version of the content, or display a promotional page for your app.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/net/Uri.html fallbackUrl` | The link to open on Android if the app is not installed. |

### setMinimumVersion

```
public @NonNull DynamicLink.AndroidParameters.Builder [setMinimumVersion](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#setMinimumVersion(int))(int minimumVersion)
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Sets the versionCode of the minimum version of your app that can open the link.

| Parameters |
|---|---|
| `int minimumVersion` | The minimum version. |