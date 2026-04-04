# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink.Warning.md.txt

# ShortDynamicLink.Warning

# ShortDynamicLink.Warning


```
public interface ShortDynamicLink.Warning
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This interface is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Information about potential warnings on short Dynamic Link creation.

## Summary

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `[getCode](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink.Warning#getCode())()` **This method is deprecated.** See `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink.Warning#getMessage()` for more information on this warning and how to correct it. <br /> |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `[getMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink.Warning#getMessage())()` **This method is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |

## Public methods

### getCode

```
abstract @Nullable String [getCode](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink.Warning#getCode())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> See `https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink.Warning#getMessage()` for more information on this warning and how to correct it.

Gets the warning code.

### getMessage

```
abstract @Nullable String [getMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/ShortDynamicLink.Warning#getMessage())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Gets the warning message to help developers improve their requests.