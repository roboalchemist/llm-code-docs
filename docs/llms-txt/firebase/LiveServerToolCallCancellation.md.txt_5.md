# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerToolCallCancellation.md.txt

# LiveServerToolCallCancellation

# LiveServerToolCallCancellation


```
@PublicPreviewAPI
class LiveServerToolCallCancellation : LiveServerMessage
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Notification for the client to cancel a previous function call from `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerToolCall`.

You do not need to send `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionResponsePart`s for the cancelled `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart`s.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerToolCallCancellation#LiveServerToolCallCancellation(kotlin.collections.List)(functionIds: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerToolCallCancellation#functionIds()` A list of `id`s matching the `id` provided in a previous `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerToolCall`, where only the provided `id`s should be cancelled. |

## Public constructors

### LiveServerToolCallCancellation

```
LiveServerToolCallCancellation(functionIds: List<String>)
```

## Public properties

### functionIds

```
val functionIds: List<String>
```

A list of `id`s matching the `id` provided in a previous `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerToolCall`, where only the provided `id`s should be cancelled.