# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession.md.txt

# LiveSession

# LiveSession


```
@PublicPreviewAPI
class LiveSession
```

<br />

*** ** * ** ***

Represents a live WebSocket session capable of streaming content to and from the server.

## Summary

| ### Public functions |
|---|---|
| `suspend https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#close()()` Closes the client session. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#isAudioConversationActive()()` Indicates whether an audio conversation is being used for this session object. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#isClosed()()` Indicates whether the underlying websocket connection is active. |
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveServerMessage>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#receive()()` Receives responses from the model for both streaming and standard requests. |
| `suspend https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#send(com.google.firebase.ai.type.Content)(content: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content)` Sends `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` to the model. |
| `suspend https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#send(kotlin.String)(text: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Sends text to the model. |
| `suspend https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#sendAudioRealtime(com.google.firebase.ai.type.InlineData)(audio: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineData)` Sends an audio input stream to the model, using the realtime API. |
| `suspend https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#sendFunctionResponse(kotlin.collections.List)(functionList: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart>)` Sends function calling responses to the model. |
| `suspend https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `[sendMediaStream](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#sendMediaStream(kotlin.collections.List))(mediaChunks: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/MediaData>)` **This function is deprecated.** Use sendAudioRealtime, sendVideoRealtime, or sendTextRealtime instead |
| `suspend https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#sendTextRealtime(kotlin.String)(text: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Sends a text input stream to the model, using the realtime API. |
| `suspend https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#sendVideoRealtime(com.google.firebase.ai.type.InlineData)(video: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineData)` Sends a video frame to the model, using the realtime API. |
| `suspend https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#startAudioConversation(kotlin.Function1)( functionCallHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart) -> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)? )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#stopAudioConversation()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#close()`. |
| `suspend https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#startAudioConversation(com.google.firebase.ai.type.LiveAudioConversationConfig)( liveAudioConversationConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#stopAudioConversation()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#close()`. |
| `suspend https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#startAudioConversation(kotlin.Function1,kotlin.Boolean)( functionCallHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart) -> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)?, enableInterruptions: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#stopAudioConversation()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#close()`. |
| `suspend https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#startAudioConversation(kotlin.Function1,kotlin.Function2,kotlin.Boolean)( functionCallHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart) -> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)?, transcriptHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription?, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription?) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)?, enableInterruptions: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#stopAudioConversation()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#close()`. |
| `suspend https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#startAudioConversation(kotlin.Function1,kotlin.Function2,kotlin.Function1,kotlin.Boolean)( functionCallHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart) -> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)?, transcriptHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription?, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription?) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)?, goAwayHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveServerGoAway) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)?, enableInterruptions: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#stopAudioConversation()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#close()`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#stopAudioConversation()()` Stops the audio conversation with the model. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#stopReceiving()()` Stops receiving from the model. |

## Public functions

### close

```
suspend fun close(): Unit
```

Closes the client session.

Once a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession` is closed, it can not be reopened; you'll need to start a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#stopReceiving()` |   |

### isAudioConversationActive

```
fun isAudioConversationActive(): Boolean
```

Indicates whether an audio conversation is being used for this session object.

### isClosed

```
fun isClosed(): Boolean
```

Indicates whether the underlying websocket connection is active.

### receive

```
fun receive(): Flow<LiveServerMessage>
```

Receives responses from the model for both streaming and standard requests.

Call `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#close()` to stop receiving responses from the model.

| Returns |
|---|---|
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveServerMessage>` | A `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html` which will emit `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveServerMessage` from the model. |

| Throws |
|---|---|
| `com.google.firebase.ai.type.SessionAlreadyReceivingException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SessionAlreadyReceivingException` | when the session is already receiving. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#stopReceiving()` |   |

### send

```
suspend fun send(content: Content): Unit
```

Sends `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` to the model.

Calling this after `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#startAudioConversation(kotlin.Function1)` will play the response audio immediately.

| Parameters |
|---|---|
| `content: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` | Client `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` to be sent to the model. |

### send

```
suspend fun send(text: String): Unit
```

Sends text to the model.

Calling this after `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#startAudioConversation(kotlin.Function1)` will play the response audio immediately.

| Parameters |
|---|---|
| `text: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Text to be sent to the model. |

### sendAudioRealtime

```
suspend fun sendAudioRealtime(audio: InlineData): Unit
```

Sends an audio input stream to the model, using the realtime API.

To learn more about audio formats, and the required state they should be provided in, see the docs on [Supported audio formats](https://cloud.google.com/vertex-ai/generative-ai/docs/live-api#supported-audio-formats)

| Parameters |
|---|---|
| `audio: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineData` | Raw audio data used to update the model on the client's conversation. For best results, send 16-bit PCM audio at 24kHz. |

### sendFunctionResponse

```
suspend fun sendFunctionResponse(functionList: List<FunctionResponsePart>): Unit
```

Sends function calling responses to the model.

**NOTE:** If you're using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#startAudioConversation(kotlin.Function1)`, the method will handle sending function responses to the model for you. You do *not* need to call this method in that case.

| Parameters |
|---|---|
| `functionList: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart>` | The list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart` instances indicating the function response from the client. |

### sendMediaStream

```
suspend fun [sendMediaStream](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#sendMediaStream(kotlin.collections.List))(mediaChunks: List<MediaData>): Unit
```

> [!CAUTION]
> **This function is deprecated.**   
> Use sendAudioRealtime, sendVideoRealtime, or sendTextRealtime instead

Streams client data to the model.

Calling this after `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#startAudioConversation(kotlin.Function1)` will play the response audio immediately.

| Parameters |
|---|---|
| `mediaChunks: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/MediaData>` | The list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/MediaData` instances representing the media data to be sent. |

### sendTextRealtime

```
suspend fun sendTextRealtime(text: String): Unit
```

Sends a text input stream to the model, using the realtime API.

| Parameters |
|---|---|
| `text: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Text content to append to the current client's conversation. |

### sendVideoRealtime

```
suspend fun sendVideoRealtime(video: InlineData): Unit
```

Sends a video frame to the model, using the realtime API.

Instead of raw video data, the model expects individual frames of the video, sent as images.

If your video has audio, send it separately through `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#sendAudioRealtime(com.google.firebase.ai.type.InlineData)`.

For better performance, frames can also be sent at a lower rate than the video; even as low as 1 frame per second.

| Parameters |
|---|---|
| `video: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineData` | Encoded image data extracted from a frame of the video, used to update the model on the client's conversation, with the corresponding IANA standard MIME type of the video frame data (for example, `image/png`, `image/jpeg`, etc.). |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
suspend fun startAudioConversation(
    functionCallHandler: ((FunctionCallPart) -> FunctionResponsePart)? = null
): Unit
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#stopAudioConversation()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#close()`.

| Parameters |
|---|---|
| `functionCallHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart) -> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)? = null` | A callback function that is invoked whenever the model receives a function call. The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart` that the callback function returns will be automatically sent to the model. |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
suspend fun startAudioConversation(
    liveAudioConversationConfig: LiveAudioConversationConfig
): Unit
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#stopAudioConversation()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#close()`.

| Parameters |
|---|---|
| `liveAudioConversationConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig` provided by the user to control the various aspects of the conversation. |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
suspend fun startAudioConversation(
    functionCallHandler: ((FunctionCallPart) -> FunctionResponsePart)? = null,
    enableInterruptions: Boolean = false
): Unit
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#stopAudioConversation()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#close()`.

| Parameters |
|---|---|
| `functionCallHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart) -> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)? = null` | A callback function that is invoked whenever the model receives a function call. The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart` that the callback function returns will be automatically sent to the model. |
| `enableInterruptions: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false` | If enabled, allows the user to speak over or interrupt the model's ongoing reply. **WARNING**: The user interruption feature relies on device-specific support, and may not be consistently available. |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
suspend fun startAudioConversation(
    functionCallHandler: ((FunctionCallPart) -> FunctionResponsePart)? = null,
    transcriptHandler: ((Transcription?, Transcription?) -> Unit)? = null,
    enableInterruptions: Boolean = false
): Unit
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#stopAudioConversation()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#close()`.

| Parameters |
|---|---|
| `functionCallHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart) -> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)? = null` | A callback function that is invoked whenever the model receives a function call. The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart` that the callback function returns will be automatically sent to the model. |
| `transcriptHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription?, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription?) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)? = null` | A callback function that is invoked whenever the model receives a transcript. The first `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription` object is the input transcription, and the second is the output transcription. |
| `enableInterruptions: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false` | If enabled, allows the user to speak over or interrupt the model's ongoing reply. **WARNING**: The user interruption feature relies on device-specific support, and may not be consistently available. |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
suspend fun startAudioConversation(
    functionCallHandler: ((FunctionCallPart) -> FunctionResponsePart)? = null,
    transcriptHandler: ((Transcription?, Transcription?) -> Unit)? = null,
    goAwayHandler: ((LiveServerGoAway) -> Unit)? = null,
    enableInterruptions: Boolean = false
): Unit
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#stopAudioConversation()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#close()`.

| Parameters |
|---|---|
| `functionCallHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart) -> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)? = null` | A callback function that is invoked whenever the model receives a function call. The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart` that the callback function returns will be automatically sent to the model. |
| `transcriptHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription?, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription?) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)? = null` | A callback function that is invoked whenever the model receives a transcript. The first `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription` object is the input transcription, and the second is the output transcription. |
| `goAwayHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveServerGoAway) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)? = null` | A callback function that is invoked when the server initiates a disconnect via a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveServerGoAway` message. This allows the application to handle server-initiated session termination gracefully. |
| `enableInterruptions: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false` | If enabled, allows the user to speak over or interrupt the model's ongoing reply. **WARNING**: The user interruption feature relies on device-specific support, and may not be consistently available. |

### stopAudioConversation

```
fun stopAudioConversation(): Unit
```

Stops the audio conversation with the model.

This only needs to be called after a previous call to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#startAudioConversation(kotlin.Function1)`.

If there is no audio conversation currently active, this function does nothing.

### stopReceiving

```
fun stopReceiving(): Unit
```

Stops receiving from the model.

If this function is called during an ongoing audio conversation, the model's response will not be received, and no audio will be played; the live session object will no longer receive data from the server.

To resume receiving data, you must either handle it directly using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#receive()`, or indirectly by using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#startAudioConversation(kotlin.Function1)`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession#close()` |   |