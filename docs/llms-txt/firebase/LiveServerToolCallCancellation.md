# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveServerToolCallCancellation.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveServerToolCallCancellation.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerToolCallCancellation.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerToolCallCancellation.md.txt

# LiveServerToolCallCancellation

# LiveServerToolCallCancellation


```
@PublicPreviewAPI
class LiveServerToolCallCancellation : LiveServerMessage
```

<br />

*** ** * ** ***

| **This class is deprecated.**   
| The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Notification for the client to cancel a previous function call from [LiveServerToolCall](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerToolCall).

You do not need to send [FunctionResponsePart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionResponsePart)s for the cancelled [FunctionCallPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart)s.

## Summary

|                                                                                                                                                                                           ### Public constructors                                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [LiveServerToolCallCancellation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerToolCallCancellation#LiveServerToolCallCancellation(kotlin.collections.List))`(functionIds: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`>)` |

|                                                                             ### Public properties                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`>` | [functionIds](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerToolCallCancellation#functionIds()) A list of `id`s matching the `id` provided in a previous [LiveServerToolCall](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerToolCall), where only the provided `id`s should be cancelled. |

## Public constructors

### LiveServerToolCallCancellation

```
LiveServerToolCallCancellation(functionIds:Â List<String>)
```  

## Public properties

### functionIds

```
valÂ functionIds:Â List<String>
```

A list of `id`s matching the `id` provided in a previous [LiveServerToolCall](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerToolCall), where only the provided `id`s should be cancelled.