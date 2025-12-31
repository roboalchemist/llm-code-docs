# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig.Companion.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallingConfig.Companion.md.txt

# FunctionCallingConfig.Companion

# FunctionCallingConfig.Companion


```
public static class FunctionCallingConfig.Companion
```

<br />

*** ** * ** ***

## Summary

|                                                                                                             ### Public methods                                                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FunctionCallingConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallingConfig) | [any](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallingConfig.Companion#any(kotlin.collections.List))`(`[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)`> allowedFunctionNames)` The model always predicts a provided function call to answer every query. |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FunctionCallingConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallingConfig) | [auto](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallingConfig.Companion#auto())`()` The default behavior for function calling.                                                                                                                                                                                                                                                                                                                                      |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FunctionCallingConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallingConfig) | [none](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallingConfig.Companion#none())`()` The model will never predict a function call to answer a query.                                                                                                                                                                                                                                                                                                                 |

## Public methods

### any

```
publicÂ staticÂ finalÂ @NonNull FunctionCallingConfigÂ any(List<@NonNull String>Â allowedFunctionNames)
```

The model always predicts a provided function call to answer every query.  

### auto

```
publicÂ staticÂ finalÂ @NonNull FunctionCallingConfigÂ auto()
```

The default behavior for function calling. The model calls functions to answer queries at its discretion.  

### none

```
publicÂ staticÂ finalÂ @NonNull FunctionCallingConfigÂ none()
```

The model will never predict a function call to answer a query. This can also be achieved by not passing any tools to the model.