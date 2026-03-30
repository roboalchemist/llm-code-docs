# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Tool.md.txt

# Tool

# Tool


```
class Tool
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Contains a set of function declarations that the model has access to. These can be used to gather information, or complete tasks

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Tool` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Tool.Companion#functionDeclarations(kotlin.collections.List)(functionDeclarations: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionDeclaration>)` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Tool` instance that provides the model with access to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Tool.Companion#functionDeclarations(kotlin.collections.List)`. |

## Public companion functions

### functionDeclarations

```
fun functionDeclarations(functionDeclarations: List<FunctionDeclaration>): Tool
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Tool` instance that provides the model with access to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Tool.Companion#functionDeclarations(kotlin.collections.List)`.

| Parameters |
|---|---|
| `functionDeclarations: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionDeclaration>` | The list of functions that this tool allows the model access to. |