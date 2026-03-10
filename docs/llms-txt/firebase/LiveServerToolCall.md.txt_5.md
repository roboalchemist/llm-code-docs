# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerToolCall.md.txt

# LiveServerToolCall

# LiveServerToolCall


```
@PublicPreviewAPI
class LiveServerToolCall : LiveServerMessage
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Request for the client to execute the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerToolCall#functionCalls()`.

The client should return matching `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionResponsePart`, where the `id` fields correspond to individual `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart`s.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerToolCall#LiveServerToolCall(kotlin.collections.List)(functionCalls: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart>)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerToolCall#functionCalls()` A list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart` to run and return responses for. |

## Public constructors

### LiveServerToolCall

```
LiveServerToolCall(functionCalls: List<FunctionCallPart>)
```

## Public properties

### functionCalls

```
val functionCalls: List<FunctionCallPart>
```

A list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart` to run and return responses for.