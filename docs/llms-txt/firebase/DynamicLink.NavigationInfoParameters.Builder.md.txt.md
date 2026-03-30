# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters.Builder.md.txt

# DynamicLink.NavigationInfoParameters.Builder

# DynamicLink.NavigationInfoParameters.Builder


```
public final class DynamicLink.NavigationInfoParameters.Builder
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Builder for navigation info parameters.

## Summary

| ### Public constructors |
|---|
| `[Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters.Builder#Builder())()` **This method is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters` | `[build](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters.Builder#build())()` **This method is deprecated.** |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters.Builder#getForcedRedirectEnabled()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters.Builder` | `[setForcedRedirectEnabled](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters.Builder#setForcedRedirectEnabled(boolean))(boolean forcedRedirectEnabled)` **This method is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |

## Public constructors

### Builder

```
public [Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters.Builder#Builder())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Create navigation info parameter builder.

## Public methods

### build

```
public @NonNull DynamicLink.NavigationInfoParameters [build](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters.Builder#build())()
```

> [!CAUTION]
> **This method is deprecated.**   

Build NavigationInfoParameters for use with `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.Builder#setNavigationInfoParameters(com.google.firebase.dynamiclinks.DynamicLink.NavigationInfoParameters)`.

### getForcedRedirectEnabled

```
public boolean getForcedRedirectEnabled()
```

### setForcedRedirectEnabled

```
public @NonNull DynamicLink.NavigationInfoParameters.Builder [setForcedRedirectEnabled](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters.Builder#setForcedRedirectEnabled(boolean))(boolean forcedRedirectEnabled)
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Sets whether to enable force redirecting or going to the app preview page. Defaults to false.

| Parameters |
|---|---|
| `boolean forcedRedirectEnabled` | If true, app preview page will be disabled and there will be a redirect to the FDL. If false, go to the app preview page. |