# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures.md.txt

# ChatFutures

# ChatFutures


```
public abstract class ChatFutures
```

<br />

*** ** * ** ***

Wrapper class providing Java compatible methods for `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/Chat`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/Chat` |   |

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures.Companion` |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures.Companion#from(com.google.firebase.ai.Chat)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/Chat chat)` |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/Chat` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures#getChat()()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/Chat` object wrapped by this object. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures#sendMessage(com.google.firebase.ai.type.Content)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompt)` Sends a message using the existing history of this chat as context and the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` prompt. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/org/reactivestreams/Publisher<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures#sendMessageStream(com.google.firebase.ai.type.Content)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompt)` Sends a message using the existing history of this chat as context and the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` prompt. |

## Public methods

### from

```
public static final @NonNull ChatFutures from(@NonNull Chat chat)
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures` | a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures` created around the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/Chat` |

### getChat

```
public abstract @NonNull Chat getChat()
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/Chat` object wrapped by this object.

### sendMessage

```
public abstract @NonNull ListenableFuture<@NonNull GenerateContentResponse> sendMessage(@NonNull Content prompt)
```

Sends a message using the existing history of this chat as context and the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` prompt.

If successful, the message and response will be added to the history. If unsuccessful, history will remain unchanged.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompt` | The input(s) that, together with the history, will be given to the model as the prompt. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InvalidStateException com.google.firebase.ai.type.InvalidStateException` | if `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures#sendMessage(com.google.firebase.ai.type.Content)` is not coming from the 'user' role |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InvalidStateException com.google.firebase.ai.type.InvalidStateException` | if the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/Chat` instance has an active request |

### sendMessageStream

```
public abstract @NonNull Publisher<@NonNull GenerateContentResponse> sendMessageStream(@NonNull Content prompt)
```

Sends a message using the existing history of this chat as context and the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` prompt.

The response from the model is returned as a stream.

If successful, the message and response will be added to the history. If unsuccessful, history will remain unchanged.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompt` | The input(s) that, together with the history, will be given to the model as the prompt. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InvalidStateException com.google.firebase.ai.type.InvalidStateException` | if `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures#sendMessageStream(com.google.firebase.ai.type.Content)` is not coming from the 'user' role |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InvalidStateException com.google.firebase.ai.type.InvalidStateException` | if the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/Chat` instance has an active request |