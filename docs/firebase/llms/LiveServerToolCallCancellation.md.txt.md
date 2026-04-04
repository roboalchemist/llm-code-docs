# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerToolCallCancellation.md.txt

# LiveServerToolCallCancellation

# LiveServerToolCallCancellation


```
@PublicPreviewAPI
public final class LiveServerToolCallCancellation implements LiveServerMessage
```

<br />

*** ** * ** ***

Notification for the client to cancel a previous function call from `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerToolCall`.

You do not need to send `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart`s for the cancelled `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart`s.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerToolCallCancellation#functionIds()` A list of `id`s matching the `id` provided in a previous `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerToolCall`, where only the provided `id`s should be cancelled. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerToolCallCancellation#LiveServerToolCallCancellation(kotlin.collections.List)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html> functionIds)` |

## Public fields

### functionIds

```
public final @NonNull List<@NonNull String> functionIds
```

A list of `id`s matching the `id` provided in a previous `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerToolCall`, where only the provided `id`s should be cancelled.

## Public constructors

### LiveServerToolCallCancellation

```
public LiveServerToolCallCancellation(@NonNull List<@NonNull String> functionIds)
```