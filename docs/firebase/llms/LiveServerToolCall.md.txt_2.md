# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveServerToolCall.md.txt

# LiveServerToolCall

# LiveServerToolCall


```
@PublicPreviewAPI
public final class LiveServerToolCall implements LiveServerMessage
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Request for the client to execute the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveServerToolCall#functionCalls()`.

The client should return matching `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart`, where the `id` fields correspond to individual `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart`s.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveServerToolCall#functionCalls()` A list of `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart` to run and return responses for. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveServerToolCall#LiveServerToolCall(kotlin.collections.List)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart> functionCalls)` |

## Public fields

### functionCalls

```
public final @NonNull List<@NonNull FunctionCallPart> functionCalls
```

A list of `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart` to run and return responses for.

## Public constructors

### LiveServerToolCall

```
public LiveServerToolCall(@NonNull List<@NonNull FunctionCallPart> functionCalls)
```