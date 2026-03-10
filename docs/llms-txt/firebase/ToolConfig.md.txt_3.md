# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ToolConfig.md.txt

# ToolConfig

# ToolConfig


```
class ToolConfig
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Contains configuration for the function calling tools of the model. This can be used to change when the model can predict function calls.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ToolConfig#ToolConfig(com.google.firebase.vertexai.type.FunctionCallingConfig)(functionCallingConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallingConfig?)` |

## Public constructors

### ToolConfig

```
ToolConfig(functionCallingConfig: FunctionCallingConfig?)
```

| Parameters |
|---|---|
| `functionCallingConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallingConfig?` | The config for function calling |