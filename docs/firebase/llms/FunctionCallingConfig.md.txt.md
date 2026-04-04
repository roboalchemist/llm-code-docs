# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig.md.txt

# FunctionCallingConfig

# FunctionCallingConfig


```
public final class FunctionCallingConfig
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

The configuration that specifies the function calling behavior.

See the static methods in the `companion object` for the list of available behaviors.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig.Companion` |

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