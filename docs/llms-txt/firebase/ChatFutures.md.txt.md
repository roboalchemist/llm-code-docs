# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ChatFutures.md.txt

# ChatFutures

# ChatFutures


```
public abstract class ChatFutures
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Wrapper class providing Java compatible methods for `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/Chat`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/Chat` |   |

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ChatFutures.Companion` |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ChatFutures` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ChatFutures.Companion#from(com.google.firebase.vertexai.Chat)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/Chat chat)` |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/Chat` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ChatFutures#getChat()()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/Chat` object wrapped by this object. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ChatFutures#sendMessage(com.google.firebase.vertexai.type.Content)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content prompt)` Sends a message using the existing history of this chat as context and the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` prompt. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/org/reactivestreams/Publisher<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ChatFutures#sendMessageStream(com.google.firebase.vertexai.type.Content)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content prompt)` Sends a message using the existing history of this chat as context and the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` prompt. |

## Public methods

### from

```
public static final @NonNull ChatFutures from(@NonNull Chat chat)
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ChatFutures` | a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ChatFutures` created around the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/Chat` |

### getChat

```
public abstract @NonNull Chat getChat()
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/Chat` object wrapped by this object.

### sendMessage

```
public abstract @NonNull ListenableFuture<@NonNull GenerateContentResponse> sendMessage(@NonNull Content prompt)
```

Sends a message using the existing history of this chat as context and the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` prompt.

If successful, the message and response will be added to the history. If unsuccessful, history will remain unchanged.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content prompt` | The input(s) that, together with the history, will be given to the model as the prompt. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/InvalidStateException com.google.firebase.vertexai.type.InvalidStateException` | if `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ChatFutures#sendMessage(com.google.firebase.vertexai.type.Content)` is not coming from the 'user' role |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/InvalidStateException com.google.firebase.vertexai.type.InvalidStateException` | if the `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/Chat` instance has an active request |

### sendMessageStream

```
public abstract @NonNull Publisher<@NonNull GenerateContentResponse> sendMessageStream(@NonNull Content prompt)
```

Sends a message using the existing history of this chat as context and the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` prompt.

The response from the model is returned as a stream.

If successful, the message and response will be added to the history. If unsuccessful, history will remain unchanged.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content prompt` | The input(s) that, together with the history, will be given to the model as the prompt. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/InvalidStateException com.google.firebase.vertexai.type.InvalidStateException` | if `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ChatFutures#sendMessageStream(com.google.firebase.vertexai.type.Content)` is not coming from the 'user' role |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/InvalidStateException com.google.firebase.vertexai.type.InvalidStateException` | if the `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/Chat` instance has an active request |