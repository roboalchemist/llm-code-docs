# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures.md.txt

# LiveSessionFutures

# LiveSessionFutures


```
@PublicPreviewAPI
abstract class LiveSessionFutures
```

<br />

*** ** * ** ***

Wrapper class providing Java compatible methods for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession` |   |

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures.Companion#from(com.google.firebase.ai.type.LiveSession)(session: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession)` |

| ### Public functions |
|---|---|
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close()()` Closes the client session. |
| `abstract https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveServerMessage>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#receive()()` Receives responses from the model for both streaming and standard requests. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#send(com.google.firebase.ai.type.Content)(content: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content)` Sends `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` to the model. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#send(kotlin.String)(text: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Sends text to the model. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#sendAudioRealtime(com.google.firebase.ai.type.InlineData)(audio: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineData)` Sends an audio input stream to the model, using the realtime API. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#sendFunctionResponse(kotlin.collections.List)(functionList: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart>)` Sends function calling responses to the model. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `[sendMediaStream](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#sendMediaStream(kotlin.collections.List))(mediaChunks: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/MediaData>)` **This function is deprecated.** Use \`sendAudioRealtime\`, \`sendVideoRealtime\`, or \`sendTextRealtime\` instead |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#sendTextRealtime(kotlin.String)(text: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` For details about the realtime input usage, see the `BidiGenerateContentRealtimeInput` documentation ( [Gemini Developer API](https://ai.google.dev/api/live#bidigeneratecontentrealtimeinput) or [Vertex AI Gemini API](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/multimodal-live#bidigeneratecontentrealtimeinput) ). |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#sendVideoRealtime(com.google.firebase.ai.type.InlineData)(video: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineData)` Sends a video input stream to the model, using the realtime API. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation()()` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()`. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation(kotlin.Boolean)(enableInterruptions: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close()`. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation(kotlin.Function1)( functionCallHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart) -> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)? )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close()`. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation(com.google.firebase.ai.type.LiveAudioConversationConfig)( liveAudioConversationConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()`. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation(kotlin.Function2)( transcriptHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription?, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription?) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)? )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()`. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation(kotlin.Function1,kotlin.Boolean)( functionCallHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart) -> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)?, enableInterruptions: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close()`. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation(kotlin.Function2,kotlin.Boolean)( transcriptHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription?, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription?) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)?, enableInterruptions: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close()`. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation(kotlin.Function1,kotlin.Function2,kotlin.Boolean)( functionCallHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart) -> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)?, transcriptHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription?, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription?) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)?, enableInterruptions: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close()`. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()()` Stops the audio conversation with the Gemini Server. |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopReceiving()()` Stops receiving from the model. |

## Public companion functions

### from

```
fun from(session: LiveSession): LiveSessionFutures
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures` | a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures` created around the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession` |

## Public functions

### close

```
abstract fun close(): ListenableFuture<Unit>
```

Closes the client session.

Once a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession` is closed, it can not be reopened; you'll need to start a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopReceiving()` |   |

### receive

```
abstract fun receive(): Publisher<LiveServerMessage>
```

Receives responses from the model for both streaming and standard requests.

Call `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close()` to stop receiving responses from the model.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveServerMessage>` | A `https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher` which will emit `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveServerMessage` from the model. |

| Throws |
|---|---|
| `com.google.firebase.ai.type.SessionAlreadyReceivingException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SessionAlreadyReceivingException` | when the session is already receiving. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopReceiving()` |   |

### send

```
abstract fun send(content: Content): ListenableFuture<Unit>
```

Sends `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` to the model.

Calling this after `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation()` will play the response audio immediately.

| Parameters |
|---|---|
| `content: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` | Client `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` to be sent to the model. |

### send

```
abstract fun send(text: String): ListenableFuture<Unit>
```

Sends text to the model.

Calling this after `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation()` will play the response audio immediately.

| Parameters |
|---|---|
| `text: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Text to be sent to the model. |

### sendAudioRealtime

```
abstract fun sendAudioRealtime(audio: InlineData): ListenableFuture<Unit>
```

Sends an audio input stream to the model, using the realtime API.

| Parameters |
|---|---|
| `audio: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineData` | The audio data to send. |

### sendFunctionResponse

```
abstract fun sendFunctionResponse(functionList: List<FunctionResponsePart>): ListenableFuture<Unit>
```

Sends function calling responses to the model.

| Parameters |
|---|---|
| `functionList: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart>` | The list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart` instances indicating the function response from the client. |

### sendMediaStream

```
abstract fun [sendMediaStream](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#sendMediaStream(kotlin.collections.List))(mediaChunks: List<MediaData>): ListenableFuture<Unit>
```

> [!CAUTION]
> **This function is deprecated.**   
> Use \`sendAudioRealtime\`, \`sendVideoRealtime\`, or \`sendTextRealtime\` instead

Streams client data to the model.

Calling this after `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation()` will play the response audio immediately.

| Parameters |
|---|---|
| `mediaChunks: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/MediaData>` | The list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/MediaData` instances representing the media data to be sent. |

### sendTextRealtime

```
abstract fun sendTextRealtime(text: String): ListenableFuture<Unit>
```

For details about the realtime input usage, see the `BidiGenerateContentRealtimeInput` documentation ( [Gemini Developer API](https://ai.google.dev/api/live#bidigeneratecontentrealtimeinput) or [Vertex AI Gemini API](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/multimodal-live#bidigeneratecontentrealtimeinput) ).

| Parameters |
|---|---|
| `text: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The text data to send. |

### sendVideoRealtime

```
abstract fun sendVideoRealtime(video: InlineData): ListenableFuture<Unit>
```

Sends a video input stream to the model, using the realtime API.

| Parameters |
|---|---|
| `video: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineData` | The video data to send. Video MIME type could be either video or image. |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
abstract fun startAudioConversation(): ListenableFuture<Unit>
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()`.

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
abstract fun startAudioConversation(enableInterruptions: Boolean): ListenableFuture<Unit>
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close()`.

| Parameters |
|---|---|
| `enableInterruptions: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | If enabled, allows the user to speak over or interrupt the model's ongoing reply. **WARNING**: The user interruption feature relies on device-specific support, and may not be consistently available. |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
abstract fun startAudioConversation(
    functionCallHandler: ((FunctionCallPart) -> FunctionResponsePart)?
): ListenableFuture<Unit>
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close()`.

| Parameters |
|---|---|
| `functionCallHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart) -> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)?` | A callback function that is invoked whenever the model receives a function call. |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
abstract fun startAudioConversation(
    liveAudioConversationConfig: LiveAudioConversationConfig
): ListenableFuture<Unit>
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()`.

| Parameters |
|---|---|
| `liveAudioConversationConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig` provided by the user to control the various aspects of the conversation. |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
abstract fun startAudioConversation(
    transcriptHandler: ((Transcription?, Transcription?) -> Unit)?
): ListenableFuture<Unit>
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()`.

| Parameters |
|---|---|
| `transcriptHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription?, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription?) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)?` | A callback function that is invoked whenever the model receives a transcript. The first `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription` object is the input transcription, and the second is the output transcription |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
abstract fun startAudioConversation(
    functionCallHandler: ((FunctionCallPart) -> FunctionResponsePart)?,
    enableInterruptions: Boolean
): ListenableFuture<Unit>
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close()`.

| Parameters |
|---|---|
| `functionCallHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart) -> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)?` | A callback function that is invoked whenever the model receives a function call. |
| `enableInterruptions: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | If enabled, allows the user to speak over or interrupt the model's ongoing reply. **WARNING**: The user interruption feature relies on device-specific support, and may not be consistently available. |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
abstract fun startAudioConversation(
    transcriptHandler: ((Transcription?, Transcription?) -> Unit)?,
    enableInterruptions: Boolean
): ListenableFuture<Unit>
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close()`.

| Parameters |
|---|---|
| `transcriptHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription?, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription?) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)?` | A callback function that is invoked whenever the model receives a transcript. The first `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription` object is the input transcription, and the second is the output transcription |
| `enableInterruptions: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | If enabled, allows the user to speak over or interrupt the model's ongoing reply. **WARNING**: The user interruption feature relies on device-specific support, and may not be consistently available. |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
abstract fun startAudioConversation(
    functionCallHandler: ((FunctionCallPart) -> FunctionResponsePart)?,
    transcriptHandler: ((Transcription?, Transcription?) -> Unit)?,
    enableInterruptions: Boolean
): ListenableFuture<Unit>
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close()`.

| Parameters |
|---|---|
| `functionCallHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart) -> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)?` | A callback function that is invoked whenever the model receives a function call. |
| `transcriptHandler: ((https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription?, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription?) -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)?` | A callback function that is invoked whenever the model receives a transcript. The first `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription` object is the input transcription, and the second is the output transcription |
| `enableInterruptions: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | If enabled, allows the user to speak over or interrupt the model's ongoing reply. **WARNING**: The user interruption feature relies on device-specific support, and may not be consistently available. |

### stopAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
abstract fun stopAudioConversation(): ListenableFuture<Unit>
```

Stops the audio conversation with the Gemini Server.

This only needs to be called after a previous call to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation()`.

If there is no audio conversation currently active, this function does nothing.

### stopReceiving

```
abstract fun stopReceiving(): Unit
```

Stops receiving from the model.

If this function is called during an ongoing audio conversation, the model's response will not be received, and no audio will be played; the live session object will no longer receive data from the server.

To resume receiving data, you must either handle it directly using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#receive()`, or indirectly by using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation()`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close()` |   |