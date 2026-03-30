# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig.Companion.md.txt

# FunctionCallingConfig.Companion

# FunctionCallingConfig.Companion


```
public static class FunctionCallingConfig.Companion
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig.Companion#any(kotlin.collections.List)(https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html> allowedFunctionNames)` The model always predicts a provided function call to answer every query. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig.Companion#auto()()` The default behavior for function calling. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig.Companion#none()()` The model will never predict a function call to answer a query. |

## Public methods

### any

```
public static final @NonNull FunctionCallingConfig any(List<@NonNull String> allowedFunctionNames)
```

The model always predicts a provided function call to answer every query.

### auto

```
public static final @NonNull FunctionCallingConfig auto()
```

The default behavior for function calling. The model calls functions to answer queries at its discretion.

### none

```
public static final @NonNull FunctionCallingConfig none()
```

The model will never predict a function call to answer a query. This can also be achieved by not passing any tools to the model.