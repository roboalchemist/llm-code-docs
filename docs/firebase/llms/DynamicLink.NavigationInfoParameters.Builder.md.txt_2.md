# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters.Builder.md.txt

# DynamicLink.NavigationInfoParameters.Builder

# DynamicLink.NavigationInfoParameters.Builder


```
class DynamicLink.NavigationInfoParameters.Builder
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
| `[Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters.Builder#Builder())()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters` | `[build](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters.Builder#build())()` **This function is deprecated.** |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters.Builder#getForcedRedirectEnabled()()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters.Builder` | `[setForcedRedirectEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters.Builder#setForcedRedirectEnabled(boolean))(forcedRedirectEnabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |

## Public constructors

### Builder

```
[Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters.Builder#Builder())()
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Create navigation info parameter builder.

## Public functions

### build

```
fun [build](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters.Builder#build())(): DynamicLink.NavigationInfoParameters
```

> [!CAUTION]
> **This function is deprecated.**   

Build NavigationInfoParameters for use with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setNavigationInfoParameters(com.google.firebase.dynamiclinks.DynamicLink.NavigationInfoParameters)`.

### getForcedRedirectEnabled

```
fun getForcedRedirectEnabled(): Boolean
```

### setForcedRedirectEnabled

```
fun [setForcedRedirectEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.NavigationInfoParameters.Builder#setForcedRedirectEnabled(boolean))(forcedRedirectEnabled: Boolean): DynamicLink.NavigationInfoParameters.Builder
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Sets whether to enable force redirecting or going to the app preview page. Defaults to false.

| Parameters |
|---|---|
| `forcedRedirectEnabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | If true, app preview page will be disabled and there will be a redirect to the FDL. If false, go to the app preview page. |