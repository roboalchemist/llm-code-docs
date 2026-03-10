# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveServerToolCall.md.txt

# LiveServerToolCall

# LiveServerToolCall


```
@PublicPreviewAPI
class LiveServerToolCall : LiveServerMessage
```

<br />

*** ** * ** ***

Request for the client to execute the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveServerToolCall#functionCalls()`.

The client should return matching `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart`, where the `id` fields correspond to individual `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart`s.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveServerToolCall#LiveServerToolCall(kotlin.collections.List)(functionCalls: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart>)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveServerToolCall#functionCalls()` A list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart` to run and return responses for. |

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

A list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart` to run and return responses for.