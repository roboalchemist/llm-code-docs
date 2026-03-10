# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession.md.txt

# LiveSession

# LiveSession


```
@PublicPreviewAPI
class LiveSession
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents a live WebSocket session capable of streaming content to and from the server.

## Summary

| ### Public functions |
|---|---|
| `suspend https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession#close()()` Closes the client session. |
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerMessage>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession#receive()()` Receives responses from the model for both streaming and standard requests. |
| `suspend https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession#send(com.google.firebase.vertexai.type.Content)(content: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content)` Sends `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` to the model. |
| `suspend https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession#send(kotlin.String)(text: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Sends text to the model. |
| `suspend https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession#sendFunctionResponse(kotlin.collections.List)(functionList: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionResponsePart>)` Sends function calling responses to the model. |
| `suspend https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession#sendMediaStream(kotlin.collections.List)(mediaChunks: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/MediaData>)` Streams client data to the model. |
| `suspend https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession#startAudioConversation(kotlin.Function1)( functionCallHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart) -> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionResponsePart)? )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession#stopAudioConversation()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession#close()`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession#stopAudioConversation()()` Stops the audio conversation with the model. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession#stopReceiving()()` Stops receiving from the model. |

## Public functions

### close

```
suspend fun close(): Unit
```

Closes the client session.

Once a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession` is closed, it can not be reopened; you'll need to start a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession#stopReceiving()` |   |

### receive

```
fun receive(): Flow<LiveServerMessage>
```

Receives responses from the model for both streaming and standard requests.

Call `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession#close()` to stop receiving responses from the model.

| Returns |
|---|---|
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerMessage>` | A `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html` which will emit `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerMessage` from the model. |

| Throws |
|---|---|
| `com.google.firebase.vertexai.type.SessionAlreadyReceivingException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SessionAlreadyReceivingException` | when the session is already receiving. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession#stopReceiving()` |   |

### send

```
suspend fun send(content: Content): Unit
```

Sends `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` to the model.

Calling this after `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession#startAudioConversation(kotlin.Function1)` will play the response audio immediately.

| Parameters |
|---|---|
| `content: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` | Client `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` to be sent to the model. |

### send

```
suspend fun send(text: String): Unit
```

Sends text to the model.

Calling this after `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession#startAudioConversation(kotlin.Function1)` will play the response audio immediately.

| Parameters |
|---|---|
| `text: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Text to be sent to the model. |

### sendFunctionResponse

```
suspend fun sendFunctionResponse(functionList: List<FunctionResponsePart>): Unit
```

Sends function calling responses to the model.

**NOTE:** If you're using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession#startAudioConversation(kotlin.Function1)`, the method will handle sending function responses to the model for you. You do *not* need to call this method in that case.

| Parameters |
|---|---|
| `functionList: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionResponsePart>` | The list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionResponsePart` instances indicating the function response from the client. |

### sendMediaStream

```
suspend fun sendMediaStream(mediaChunks: List<MediaData>): Unit
```

Streams client data to the model.

Calling this after `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession#startAudioConversation(kotlin.Function1)` will play the response audio immediately.

| Parameters |
|---|---|
| `mediaChunks: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/MediaData>` | The list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/MediaData` instances representing the media data to be sent. |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
suspend fun startAudioConversation(
    functionCallHandler: ((FunctionCallPart) -> FunctionResponsePart)? = null
): Unit
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession#stopAudioConversation()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession#close()`.

| Parameters |
|---|---|
| `functionCallHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart) -> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionResponsePart)? = null` | A callback function that is invoked whenever the model receives a function call. The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionResponsePart` that the callback function returns will be automatically sent to the model. |

### stopAudioConversation

```
fun stopAudioConversation(): Unit
```

Stops the audio conversation with the model.

This only needs to be called after a previous call to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession#startAudioConversation(kotlin.Function1)`.

If there is no audio conversation currently active, this function does nothing.

### stopReceiving

```
fun stopReceiving(): Unit
```

Stops receiving from the model.

If this function is called during an ongoing audio conversation, the model's response will not be received, and no audio will be played; the live session object will no longer receive data from the server.

To resume receiving data, you must either handle it directly using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession#receive()`, or indirectly by using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession#startAudioConversation(kotlin.Function1)`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession#close()` |   |