# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallingConfig.md.txt

# FunctionCallingConfig

# FunctionCallingConfig


```
class FunctionCallingConfig
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

The configuration that specifies the function calling behavior.

See the static methods in the `companion object` for the list of available behaviors.

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallingConfig` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallingConfig.Companion#any(kotlin.collections.List)(allowedFunctionNames: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>?)` The model always predicts a provided function call to answer every query. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallingConfig` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallingConfig.Companion#auto()()` The default behavior for function calling. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallingConfig` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallingConfig.Companion#none()()` The model will never predict a function call to answer a query. |

## Public companion functions

### any

```
fun any(allowedFunctionNames: List<String>? = null): FunctionCallingConfig
```

The model always predicts a provided function call to answer every query.

### auto

```
fun auto(): FunctionCallingConfig
```

The default behavior for function calling. The model calls functions to answer queries at its discretion.

### none

```
fun none(): FunctionCallingConfig
```

The model will never predict a function call to answer a query. This can also be achieved by not passing any tools to the model.