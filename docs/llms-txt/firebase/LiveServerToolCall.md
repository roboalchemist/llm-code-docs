# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveServerToolCall.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerToolCall.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveServerToolCall.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerToolCall.md.txt

# LiveServerToolCall

# LiveServerToolCall


```
@PublicPreviewAPI
class LiveServerToolCall : LiveServerMessage
```

<br />

*** ** * ** ***

| **This class is deprecated.**   
| The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Request for the client to execute the provided [functionCalls](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerToolCall#functionCalls()).

The client should return matching [FunctionResponsePart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionResponsePart), where the `id` fields correspond to individual [FunctionCallPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart)s.

## Summary

|                                                                                                                                                                                              ### Public constructors                                                                                                                                                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [LiveServerToolCall](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerToolCall#LiveServerToolCall(kotlin.collections.List))`(functionCalls: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[FunctionCallPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart)`>)` |

|                                                                                                 ### Public properties                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[FunctionCallPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart)`>` | [functionCalls](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerToolCall#functionCalls()) A list of [FunctionCallPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart) to run and return responses for. |

## Public constructors

### LiveServerToolCall

```
LiveServerToolCall(functionCalls:Â List<FunctionCallPart>)
```  

## Public properties

### functionCalls

```
valÂ functionCalls:Â List<FunctionCallPart>
```

A list of [FunctionCallPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart) to run and return responses for.