# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerToolCall.md.txt

# LiveServerToolCall

# LiveServerToolCall


```
@PublicPreviewAPI
public final class LiveServerToolCall implements LiveServerMessage
```

<br />

*** ** * ** ***

Request for the client to execute the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerToolCall#functionCalls()`.

The client should return matching `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart`, where the `id` fields correspond to individual `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart`s.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerToolCall#functionCalls()` A list of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart` to run and return responses for. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerToolCall#LiveServerToolCall(kotlin.collections.List)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart> functionCalls)` |

## Public fields

### functionCalls

```
public final @NonNull List<@NonNull FunctionCallPart> functionCalls
```

A list of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart` to run and return responses for.

## Public constructors

### LiveServerToolCall

```
public LiveServerToolCall(@NonNull List<@NonNull FunctionCallPart> functionCalls)
```