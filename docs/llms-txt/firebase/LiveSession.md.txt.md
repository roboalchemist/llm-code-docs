# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession.md.txt

# LiveSession

# LiveSession


```
@PublicPreviewAPI
public final class LiveSession
```

<br />

*** ** * ** ***

Represents a live WebSocket session capable of streaming content to and from the server.

## Summary

| ### Public methods |
|---|---|
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#close()()` Closes the client session. |
| `final boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#isAudioConversationActive()()` Indicates whether an audio conversation is being used for this session object. |
| `final boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#isClosed()()` Indicates whether the underlying websocket connection is active. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerMessage>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#receive()()` Receives responses from the model for both streaming and standard requests. |
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#send(com.google.firebase.ai.type.Content)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content content)` Sends `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` to the model. |
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#send(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html text)` Sends text to the model. |
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#sendAudioRealtime(com.google.firebase.ai.type.InlineData)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineData audio)` Sends an audio input stream to the model, using the realtime API. |
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#sendFunctionResponse(kotlin.collections.List)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart> functionList )` Sends function calling responses to the model. |
| `final void` | `[sendMediaStream](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#sendMediaStream(kotlin.collections.List))(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/MediaData> mediaChunks)` **This method is deprecated.** Use sendAudioRealtime, sendVideoRealtime, or sendTextRealtime instead |
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#sendTextRealtime(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html text)` Sends a text input stream to the model, using the realtime API. |
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#sendVideoRealtime(com.google.firebase.ai.type.InlineData)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineData video)` Sends a video frame to the model, using the realtime API. |
| `final void` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#startAudioConversation(kotlin.Function1)( Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart> functionCallHandler )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#stopAudioConversation()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#close()`. |
| `final void` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#startAudioConversation(com.google.firebase.ai.type.LiveAudioConversationConfig)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig liveAudioConversationConfig )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#stopAudioConversation()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#close()`. |
| `final void` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#startAudioConversation(kotlin.Function1,kotlin.Boolean)( Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart> functionCallHandler, boolean enableInterruptions )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#stopAudioConversation()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#close()`. |
| `final void` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#startAudioConversation(kotlin.Function1,kotlin.Function2,kotlin.Boolean)( Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart> functionCallHandler, Function2<https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> transcriptHandler, boolean enableInterruptions )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#stopAudioConversation()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#close()`. |
| `final void` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#startAudioConversation(kotlin.Function1,kotlin.Function2,kotlin.Function1,kotlin.Boolean)( Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart> functionCallHandler, Function2<https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> transcriptHandler, Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerGoAway, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> goAwayHandler, boolean enableInterruptions )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#stopAudioConversation()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#close()`. |
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#stopAudioConversation()()` Stops the audio conversation with the model. |
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#stopReceiving()()` Stops receiving from the model. |

## Public methods

### close

```
public final void close()
```

Closes the client session.

Once a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession` is closed, it can not be reopened; you'll need to start a new `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#stopReceiving()` |   |

### isAudioConversationActive

```
public final boolean isAudioConversationActive()
```

Indicates whether an audio conversation is being used for this session object.

### isClosed

```
public final boolean isClosed()
```

Indicates whether the underlying websocket connection is active.

### receive

```
public final @NonNull Flow<@NonNull LiveServerMessage> receive()
```

Receives responses from the model for both streaming and standard requests.

Call `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#close()` to stop receiving responses from the model.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerMessage>` | A `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html` which will emit `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerMessage` from the model. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SessionAlreadyReceivingException com.google.firebase.ai.type.SessionAlreadyReceivingException` | when the session is already receiving. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#stopReceiving()` |   |

### send

```
public final void send(@NonNull Content content)
```

Sends `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` to the model.

Calling this after `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#startAudioConversation(kotlin.Function1)` will play the response audio immediately.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content content` | Client `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` to be sent to the model. |

### send

```
public final void send(@NonNull String text)
```

Sends text to the model.

Calling this after `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#startAudioConversation(kotlin.Function1)` will play the response audio immediately.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html text` | Text to be sent to the model. |

### sendAudioRealtime

```
public final void sendAudioRealtime(@NonNull InlineData audio)
```

Sends an audio input stream to the model, using the realtime API.

To learn more about audio formats, and the required state they should be provided in, see the docs on [Supported audio formats](https://cloud.google.com/vertex-ai/generative-ai/docs/live-api#supported-audio-formats)

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineData audio` | Raw audio data used to update the model on the client's conversation. For best results, send 16-bit PCM audio at 24kHz. |

### sendFunctionResponse

```
public final void sendFunctionResponse(
    @NonNull List<@NonNull FunctionResponsePart> functionList
)
```

Sends function calling responses to the model.

**NOTE:** If you're using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#startAudioConversation(kotlin.Function1)`, the method will handle sending function responses to the model for you. You do *not* need to call this method in that case.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart> functionList` | The list of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart` instances indicating the function response from the client. |

### sendMediaStream

```
public final void [sendMediaStream](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#sendMediaStream(kotlin.collections.List))(@NonNull List<@NonNull MediaData> mediaChunks)
```

> [!CAUTION]
> **This method is deprecated.**   
> Use sendAudioRealtime, sendVideoRealtime, or sendTextRealtime instead

Streams client data to the model.

Calling this after `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#startAudioConversation(kotlin.Function1)` will play the response audio immediately.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/MediaData> mediaChunks` | The list of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/MediaData` instances representing the media data to be sent. |

### sendTextRealtime

```
public final void sendTextRealtime(@NonNull String text)
```

Sends a text input stream to the model, using the realtime API.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html text` | Text content to append to the current client's conversation. |

### sendVideoRealtime

```
public final void sendVideoRealtime(@NonNull InlineData video)
```

Sends a video frame to the model, using the realtime API.

Instead of raw video data, the model expects individual frames of the video, sent as images.

If your video has audio, send it separately through `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#sendAudioRealtime(com.google.firebase.ai.type.InlineData)`.

For better performance, frames can also be sent at a lower rate than the video; even as low as 1 frame per second.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineData video` | Encoded image data extracted from a frame of the video, used to update the model on the client's conversation, with the corresponding IANA standard MIME type of the video frame data (for example, `image/png`, `image/jpeg`, etc.). |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
public final void startAudioConversation(
    Function1<@NonNull FunctionCallPart, @NonNull FunctionResponsePart> functionCallHandler
)
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#stopAudioConversation()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#close()`.

| Parameters |
|---|---|
| `Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart> functionCallHandler` | A callback function that is invoked whenever the model receives a function call. The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart` that the callback function returns will be automatically sent to the model. |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
public final void startAudioConversation(
    @NonNull LiveAudioConversationConfig liveAudioConversationConfig
)
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#stopAudioConversation()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#close()`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig liveAudioConversationConfig` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig` provided by the user to control the various aspects of the conversation. |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
public final void startAudioConversation(
    Function1<@NonNull FunctionCallPart, @NonNull FunctionResponsePart> functionCallHandler,
    boolean enableInterruptions
)
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#stopAudioConversation()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#close()`.

| Parameters |
|---|---|
| `Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart> functionCallHandler` | A callback function that is invoked whenever the model receives a function call. The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart` that the callback function returns will be automatically sent to the model. |
| `boolean enableInterruptions` | If enabled, allows the user to speak over or interrupt the model's ongoing reply. **WARNING**: The user interruption feature relies on device-specific support, and may not be consistently available. |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
public final void startAudioConversation(
    Function1<@NonNull FunctionCallPart, @NonNull FunctionResponsePart> functionCallHandler,
    Function2<Transcription, Transcription, Unit> transcriptHandler,
    boolean enableInterruptions
)
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#stopAudioConversation()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#close()`.

| Parameters |
|---|---|
| `Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart> functionCallHandler` | A callback function that is invoked whenever the model receives a function call. The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart` that the callback function returns will be automatically sent to the model. |
| `Function2<https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> transcriptHandler` | A callback function that is invoked whenever the model receives a transcript. The first `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription` object is the input transcription, and the second is the output transcription. |
| `boolean enableInterruptions` | If enabled, allows the user to speak over or interrupt the model's ongoing reply. **WARNING**: The user interruption feature relies on device-specific support, and may not be consistently available. |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
public final void startAudioConversation(
    Function1<@NonNull FunctionCallPart, @NonNull FunctionResponsePart> functionCallHandler,
    Function2<Transcription, Transcription, Unit> transcriptHandler,
    Function1<@NonNull LiveServerGoAway, Unit> goAwayHandler,
    boolean enableInterruptions
)
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#stopAudioConversation()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#close()`.

| Parameters |
|---|---|
| `Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart> functionCallHandler` | A callback function that is invoked whenever the model receives a function call. The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart` that the callback function returns will be automatically sent to the model. |
| `Function2<https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> transcriptHandler` | A callback function that is invoked whenever the model receives a transcript. The first `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription` object is the input transcription, and the second is the output transcription. |
| `Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerGoAway, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> goAwayHandler` | A callback function that is invoked when the server initiates a disconnect via a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerGoAway` message. This allows the application to handle server-initiated session termination gracefully. |
| `boolean enableInterruptions` | If enabled, allows the user to speak over or interrupt the model's ongoing reply. **WARNING**: The user interruption feature relies on device-specific support, and may not be consistently available. |

### stopAudioConversation

```
public final void stopAudioConversation()
```

Stops the audio conversation with the model.

This only needs to be called after a previous call to `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#startAudioConversation(kotlin.Function1)`.

If there is no audio conversation currently active, this function does nothing.

### stopReceiving

```
public final void stopReceiving()
```

Stops receiving from the model.

If this function is called during an ongoing audio conversation, the model's response will not be received, and no audio will be played; the live session object will no longer receive data from the server.

To resume receiving data, you must either handle it directly using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#receive()`, or indirectly by using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#startAudioConversation(kotlin.Function1)`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession#close()` |   |