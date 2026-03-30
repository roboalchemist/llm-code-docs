# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat.md.txt

# Chat

# Chat


```
class Chat
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Representation of a multi-turn interaction with a model.

Captures and stores the history of communication in memory, and provides it as context with each new message.

**Note:** This object is not thread-safe, and calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#sendMessage(com.google.firebase.vertexai.type.Content)` multiple times without waiting for a response will throw an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InvalidStateException`.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#Chat(com.google.firebase.vertexai.GenerativeModel,kotlin.collections.MutableList)(model: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel, history: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content>)` |

| ### Public functions |
|---|---|
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#sendMessage(android.graphics.Bitmap)(prompt: https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html)` Sends a message using the existing history of this chat as context and the provided image prompt. |
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#sendMessage(com.google.firebase.vertexai.type.Content)(prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content)` Sends a message using the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#sendMessage(com.google.firebase.vertexai.type.Content)`; automatically providing the existing `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#history()` as context. |
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#sendMessage(kotlin.String)(prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Sends a message using the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#sendMessage(kotlin.String)`; automatically providing the existing `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#history()` as context. |
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#sendMessageStream(android.graphics.Bitmap)(prompt: https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html)` Sends a message using the existing history of this chat as context and the provided image prompt. |
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#sendMessageStream(com.google.firebase.vertexai.type.Content)(prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content)` Sends a message using the existing history of this chat as context and the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` prompt. |
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#sendMessageStream(kotlin.String)(prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Sends a message using the existing history of this chat as context and the provided text prompt. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#history()` The previous content from the chat that has been successfully sent and received from the model. |

## Public constructors

### Chat

```
Chat(model: GenerativeModel, history: MutableList<Content> = ArrayList())
```

| Parameters |
|---|---|
| `model: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel` | The model to use for the interaction. |

## Public functions

### sendMessage

```
suspend fun sendMessage(prompt: Bitmap): GenerateContentResponse
```

Sends a message using the existing history of this chat as context and the provided image prompt.

If successful, the message and response will be added to the history. If unsuccessful, history will remain unchanged.

| Parameters |
|---|---|
| `prompt: https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` | The input that, together with the history, will be given to the model as the prompt. |

| Throws |
|---|---|
| `com.google.firebase.vertexai.type.InvalidStateException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InvalidStateException` | if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#sendMessage(android.graphics.Bitmap)` is not coming from the 'user' role. |
| `com.google.firebase.vertexai.type.InvalidStateException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InvalidStateException` | if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat` instance has an active request. |

### sendMessage

```
suspend fun sendMessage(prompt: Content): GenerateContentResponse
```

Sends a message using the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#sendMessage(com.google.firebase.vertexai.type.Content)`; automatically providing the existing `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#history()` as context.

If successful, the message and response will be added to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#history()`. If unsuccessful, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#history()` will remain unchanged.

| Parameters |
|---|---|
| `prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` | The input that, together with the history, will be given to the model as the prompt. |

| Throws |
|---|---|
| `com.google.firebase.vertexai.type.InvalidStateException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InvalidStateException` | if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#sendMessage(com.google.firebase.vertexai.type.Content)` is not coming from the 'user' role. |
| `com.google.firebase.vertexai.type.InvalidStateException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InvalidStateException` | if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat` instance has an active request. |

### sendMessage

```
suspend fun sendMessage(prompt: String): GenerateContentResponse
```

Sends a message using the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#sendMessage(kotlin.String)`; automatically providing the existing `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#history()` as context.

If successful, the message and response will be added to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#history()`. If unsuccessful, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#history()` will remain unchanged.

| Parameters |
|---|---|
| `prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The input that, together with the history, will be given to the model as the prompt. |

| Throws |
|---|---|
| `com.google.firebase.vertexai.type.InvalidStateException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InvalidStateException` | if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#sendMessage(kotlin.String)` is not coming from the 'user' role. |
| `com.google.firebase.vertexai.type.InvalidStateException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InvalidStateException` | if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat` instance has an active request. |

### sendMessageStream

```
fun sendMessageStream(prompt: Bitmap): Flow<GenerateContentResponse>
```

Sends a message using the existing history of this chat as context and the provided image prompt.

The response from the model is returned as a stream.

If successful, the message and response will be added to the history. If unsuccessful, history will remain unchanged.

| Parameters |
|---|---|
| `prompt: https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` | The input that, together with the history, will be given to the model as the prompt. |

| Throws |
|---|---|
| `com.google.firebase.vertexai.type.InvalidStateException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InvalidStateException` | if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#sendMessageStream(android.graphics.Bitmap)` is not coming from the 'user' role. |
| `com.google.firebase.vertexai.type.InvalidStateException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InvalidStateException` | if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat` instance has an active request. |

### sendMessageStream

```
fun sendMessageStream(prompt: Content): Flow<GenerateContentResponse>
```

Sends a message using the existing history of this chat as context and the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` prompt.

The response from the model is returned as a stream.

If successful, the message and response will be added to the history. If unsuccessful, history will remain unchanged.

| Parameters |
|---|---|
| `prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` | The input that, together with the history, will be given to the model as the prompt. |

| Throws |
|---|---|
| `com.google.firebase.vertexai.type.InvalidStateException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InvalidStateException` | if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#sendMessageStream(com.google.firebase.vertexai.type.Content)` is not coming from the 'user' role. |
| `com.google.firebase.vertexai.type.InvalidStateException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InvalidStateException` | if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat` instance has an active request. |

### sendMessageStream

```
fun sendMessageStream(prompt: String): Flow<GenerateContentResponse>
```

Sends a message using the existing history of this chat as context and the provided text prompt.

The response from the model is returned as a stream.

If successful, the message and response will be added to the history. If unsuccessful, history will remain unchanged.

| Parameters |
|---|---|
| `prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The input(s) that, together with the history, will be given to the model as the prompt. |

| Throws |
|---|---|
| `com.google.firebase.vertexai.type.InvalidStateException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InvalidStateException` | if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat#sendMessageStream(kotlin.String)` is not coming from the 'user' role. |
| `com.google.firebase.vertexai.type.InvalidStateException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/InvalidStateException` | if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat` instance has an active request. |

## Public properties

### history

```
val history: MutableList<Content>
```

The previous content from the chat that has been successfully sent and received from the model. This will be provided to the model for each message sent (as context for the discussion).