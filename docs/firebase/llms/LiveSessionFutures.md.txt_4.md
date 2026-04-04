# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures.md.txt

# LiveSessionFutures

# LiveSessionFutures


```
@PublicPreviewAPI
abstract class LiveSessionFutures
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Wrapper class providing Java compatible methods for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession` |   |

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures.Companion#from(com.google.firebase.vertexai.type.LiveSession)(session: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession)` |

| ### Public functions |
|---|---|
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#close()()` Closes the client session. |
| `abstract https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerMessage>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#receive()()` Receives responses from the model for both streaming and standard requests. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#send(com.google.firebase.vertexai.type.Content)(content: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content)` Sends `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` to the model. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#send(kotlin.String)(text: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Sends text to the model. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#sendFunctionResponse(kotlin.collections.List)(functionList: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionResponsePart>)` Sends function calling responses to the model. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#sendMediaStream(kotlin.collections.List)(mediaChunks: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/MediaData>)` Streams client data to the model. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#startAudioConversation()()` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#stopAudioConversation()`. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#startAudioConversation(kotlin.Function1)( functionCallHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart) -> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionResponsePart)? )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#stopAudioConversation()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#close()`. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#stopAudioConversation()()` Stops the audio conversation with the Gemini Server. |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#stopReceiving()()` Stops receiving from the model. |

## Public companion functions

### from

```
fun from(session: LiveSession): LiveSessionFutures
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures` | a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures` created around the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession` |

## Public functions

### close

```
abstract fun close(): ListenableFuture<Unit>
```

Closes the client session.

Once a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession` is closed, it can not be reopened; you'll need to start a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#stopReceiving()` |   |

### receive

```
abstract fun receive(): Publisher<LiveServerMessage>
```

Receives responses from the model for both streaming and standard requests.

Call `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#close()` to stop receiving responses from the model.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerMessage>` | A `https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher` which will emit `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveServerMessage` from the model. |

| Throws |
|---|---|
| `com.google.firebase.vertexai.type.SessionAlreadyReceivingException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SessionAlreadyReceivingException` | when the session is already receiving. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#stopReceiving()` |   |

### send

```
abstract fun send(content: Content): ListenableFuture<Unit>
```

Sends `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` to the model.

Calling this after `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#startAudioConversation(kotlin.Function1)` will play the response audio immediately.

| Parameters |
|---|---|
| `content: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` | Client `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` to be sent to the model. |

### send

```
abstract fun send(text: String): ListenableFuture<Unit>
```

Sends text to the model.

Calling this after `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#startAudioConversation(kotlin.Function1)` will play the response audio immediately.

| Parameters |
|---|---|
| `text: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Text to be sent to the model. |

### sendFunctionResponse

```
abstract fun sendFunctionResponse(functionList: List<FunctionResponsePart>): ListenableFuture<Unit>
```

Sends function calling responses to the model.

| Parameters |
|---|---|
| `functionList: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionResponsePart>` | The list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionResponsePart` instances indicating the function response from the client. |

### sendMediaStream

```
abstract fun sendMediaStream(mediaChunks: List<MediaData>): ListenableFuture<Unit>
```

Streams client data to the model.

Calling this after `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#startAudioConversation(kotlin.Function1)` will play the response audio immediately.

| Parameters |
|---|---|
| `mediaChunks: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/MediaData>` | The list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/MediaData` instances representing the media data to be sent. |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
abstract fun startAudioConversation(): ListenableFuture<Unit>
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#stopAudioConversation()`.

### startAudioConversation

```
abstract fun startAudioConversation(
    functionCallHandler: ((FunctionCallPart) -> FunctionResponsePart)?
): ListenableFuture<Unit>
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#stopAudioConversation()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#close()`.

| Parameters |
|---|---|
| `functionCallHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart) -> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionResponsePart)?` | A callback function that is invoked whenever the model receives a function call. |

### stopAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
abstract fun stopAudioConversation(): ListenableFuture<Unit>
```

Stops the audio conversation with the Gemini Server.

This only needs to be called after a previous call to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#startAudioConversation(kotlin.Function1)`.

If there is no audio conversation currently active, this function does nothing.

### stopReceiving

```
abstract fun stopReceiving(): Unit
```

Stops receiving from the model.

If this function is called during an ongoing audio conversation, the model's response will not be received, and no audio will be played; the live session object will no longer receive data from the server.

To resume receiving data, you must either handle it directly using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#receive()`, or indirectly by using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#startAudioConversation(kotlin.Function1)`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures#close()` |   |