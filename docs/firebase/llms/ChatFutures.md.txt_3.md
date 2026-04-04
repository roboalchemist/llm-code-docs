# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ChatFutures.md.txt

# ChatFutures

# ChatFutures


```
abstract class ChatFutures
```

<br />

*** ** * ** ***

Wrapper class providing Java compatible methods for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/Chat`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/Chat` |   |

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ChatFutures` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ChatFutures.Companion#from(com.google.firebase.ai.Chat)(chat: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/Chat)` |

| ### Public functions |
|---|---|
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/Chat` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ChatFutures#getChat()()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/Chat` object wrapped by this object. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ChatFutures#sendMessage(com.google.firebase.ai.type.Content)(prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content)` Sends a message using the existing history of this chat as context and the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` prompt. |
| `abstract https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ChatFutures#sendMessageStream(com.google.firebase.ai.type.Content)(prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content)` Sends a message using the existing history of this chat as context and the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` prompt. |

## Public companion functions

### from

```
fun from(chat: Chat): ChatFutures
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ChatFutures` | a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ChatFutures` created around the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/Chat` |

## Public functions

### getChat

```
abstract fun getChat(): Chat
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/Chat` object wrapped by this object.

### sendMessage

```
abstract fun sendMessage(prompt: Content): ListenableFuture<GenerateContentResponse>
```

Sends a message using the existing history of this chat as context and the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` prompt.

If successful, the message and response will be added to the history. If unsuccessful, history will remain unchanged.

| Parameters |
|---|---|
| `prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` | The input(s) that, together with the history, will be given to the model as the prompt. |

| Throws |
|---|---|
| `com.google.firebase.ai.type.InvalidStateException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InvalidStateException` | if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ChatFutures#sendMessage(com.google.firebase.ai.type.Content)` is not coming from the 'user' role |
| `com.google.firebase.ai.type.InvalidStateException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InvalidStateException` | if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/Chat` instance has an active request |

### sendMessageStream

```
abstract fun sendMessageStream(prompt: Content): Publisher<GenerateContentResponse>
```

Sends a message using the existing history of this chat as context and the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` prompt.

The response from the model is returned as a stream.

If successful, the message and response will be added to the history. If unsuccessful, history will remain unchanged.

| Parameters |
|---|---|
| `prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` | The input(s) that, together with the history, will be given to the model as the prompt. |

| Throws |
|---|---|
| `com.google.firebase.ai.type.InvalidStateException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InvalidStateException` | if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ChatFutures#sendMessageStream(com.google.firebase.ai.type.Content)` is not coming from the 'user' role |
| `com.google.firebase.ai.type.InvalidStateException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InvalidStateException` | if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/Chat` instance has an active request |