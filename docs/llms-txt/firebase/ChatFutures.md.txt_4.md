# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ChatFutures.md.txt

# ChatFutures

# ChatFutures


```
abstract class ChatFutures
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Wrapper class providing Java compatible methods for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat` |   |

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ChatFutures` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ChatFutures.Companion#from(com.google.firebase.vertexai.Chat)(chat: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat)` |

| ### Public functions |
|---|---|
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ChatFutures#getChat()()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat` object wrapped by this object. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ChatFutures#sendMessage(com.google.firebase.vertexai.type.Content)(prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content)` Sends a message using the existing history of this chat as context and the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` prompt. |
| `abstract https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ChatFutures#sendMessageStream(com.google.firebase.vertexai.type.Content)(prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content)` Sends a message using the existing history of this chat as context and the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` prompt. |

## Public companion functions

### from

```
fun from(chat: Chat): ChatFutures
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ChatFutures` | a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ChatFutures` created around the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat` |

## Public functions

### getChat

```
abstract fun getChat(): Chat
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat` object wrapped by this object.

### sendMessage

```
abstract fun sendMessage(prompt: Content): ListenableFuture<GenerateContentResponse>
```

Sends a message using the existing history of this chat as context and the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` prompt.

If successful, the message and response will be added to the history. If unsuccessful, history will remain unchanged.

| Parameters |
|---|---|
| `prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` | The input(s) that, together with the history, will be given to the model as the prompt. |

| Throws |
|---|---|
| `com.google.firebase.vertexai.type.InvalidStateException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InvalidStateException` | if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ChatFutures#sendMessage(com.google.firebase.vertexai.type.Content)` is not coming from the 'user' role |
| `com.google.firebase.vertexai.type.InvalidStateException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InvalidStateException` | if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat` instance has an active request |

### sendMessageStream

```
abstract fun sendMessageStream(prompt: Content): Publisher<GenerateContentResponse>
```

Sends a message using the existing history of this chat as context and the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` prompt.

The response from the model is returned as a stream.

If successful, the message and response will be added to the history. If unsuccessful, history will remain unchanged.

| Parameters |
|---|---|
| `prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` | The input(s) that, together with the history, will be given to the model as the prompt. |

| Throws |
|---|---|
| `com.google.firebase.vertexai.type.InvalidStateException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InvalidStateException` | if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ChatFutures#sendMessageStream(com.google.firebase.vertexai.type.Content)` is not coming from the 'user' role |
| `com.google.firebase.vertexai.type.InvalidStateException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InvalidStateException` | if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat` instance has an active request |