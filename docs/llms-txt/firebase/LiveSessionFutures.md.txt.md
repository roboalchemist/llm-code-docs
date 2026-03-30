# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures.md.txt

# LiveSessionFutures

# LiveSessionFutures


```
@PublicPreviewAPI
public abstract class LiveSessionFutures
```

<br />

*** ** * ** ***

Wrapper class providing Java compatible methods for `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession` |   |

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures.Companion` |

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#close()()` Closes the client session. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures.Companion#from(com.google.firebase.ai.type.LiveSession)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession session)` |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/org/reactivestreams/Publisher<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerMessage>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#receive()()` Receives responses from the model for both streaming and standard requests. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#send(com.google.firebase.ai.type.Content)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content content)` Sends `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` to the model. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#send(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html text)` Sends text to the model. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#sendAudioRealtime(com.google.firebase.ai.type.InlineData)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineData audio)` Sends an audio input stream to the model, using the realtime API. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#sendFunctionResponse(kotlin.collections.List)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart> functionList )` Sends function calling responses to the model. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `[sendMediaStream](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#sendMediaStream(kotlin.collections.List))(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/MediaData> mediaChunks)` **This method is deprecated.** Use \`sendAudioRealtime\`, \`sendVideoRealtime\`, or \`sendTextRealtime\` instead |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#sendTextRealtime(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html text)` For details about the realtime input usage, see the `BidiGenerateContentRealtimeInput` documentation ( [Gemini Developer API](https://ai.google.dev/api/live#bidigeneratecontentrealtimeinput) or [Vertex AI Gemini API](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/multimodal-live#bidigeneratecontentrealtimeinput) ). |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#sendVideoRealtime(com.google.firebase.ai.type.InlineData)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineData video)` Sends a video input stream to the model, using the realtime API. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation()()` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()`. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation(kotlin.Boolean)(boolean enableInterruptions)` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#close()`. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation(kotlin.Function1)( Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart> functionCallHandler )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#close()`. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation(com.google.firebase.ai.type.LiveAudioConversationConfig)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig liveAudioConversationConfig )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()`. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation(kotlin.Function2)( Function2<https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> transcriptHandler )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()`. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation(kotlin.Function1,kotlin.Boolean)( Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart> functionCallHandler, boolean enableInterruptions )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#close()`. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation(kotlin.Function2,kotlin.Boolean)( Function2<https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> transcriptHandler, boolean enableInterruptions )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#close()`. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation(kotlin.Function1,kotlin.Function2,kotlin.Boolean)( Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart> functionCallHandler, Function2<https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> transcriptHandler, boolean enableInterruptions )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#close()`. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()()` Stops the audio conversation with the Gemini Server. |
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#stopReceiving()()` Stops receiving from the model. |

## Public methods

### close

```
public abstract @NonNull ListenableFuture<Unit> close()
```

Closes the client session.

Once a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession` is closed, it can not be reopened; you'll need to start a new `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#stopReceiving()` |   |

### from

```
public static final @NonNull LiveSessionFutures from(@NonNull LiveSession session)
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures` | a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures` created around the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession` |

### receive

```
public abstract @NonNull Publisher<@NonNull LiveServerMessage> receive()
```

Receives responses from the model for both streaming and standard requests.

Call `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#close()` to stop receiving responses from the model.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/org/reactivestreams/Publisher<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerMessage>` | A `https://firebase.google.com/docs/reference/android/org/reactivestreams/Publisher` which will emit `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveServerMessage` from the model. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SessionAlreadyReceivingException com.google.firebase.ai.type.SessionAlreadyReceivingException` | when the session is already receiving. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#stopReceiving()` |   |

### send

```
public abstract @NonNull ListenableFuture<Unit> send(@NonNull Content content)
```

Sends `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` to the model.

Calling this after `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation()` will play the response audio immediately.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content content` | Client `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` to be sent to the model. |

### send

```
public abstract @NonNull ListenableFuture<Unit> send(@NonNull String text)
```

Sends text to the model.

Calling this after `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation()` will play the response audio immediately.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html text` | Text to be sent to the model. |

### sendAudioRealtime

```
public abstract @NonNull ListenableFuture<Unit> sendAudioRealtime(@NonNull InlineData audio)
```

Sends an audio input stream to the model, using the realtime API.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineData audio` | The audio data to send. |

### sendFunctionResponse

```
public abstract @NonNull ListenableFuture<Unit> sendFunctionResponse(
    @NonNull List<@NonNull FunctionResponsePart> functionList
)
```

Sends function calling responses to the model.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart> functionList` | The list of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart` instances indicating the function response from the client. |

### sendMediaStream

```
public abstract @NonNull ListenableFuture<Unit> [sendMediaStream](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#sendMediaStream(kotlin.collections.List))(@NonNull List<@NonNull MediaData> mediaChunks)
```

> [!CAUTION]
> **This method is deprecated.**   
> Use \`sendAudioRealtime\`, \`sendVideoRealtime\`, or \`sendTextRealtime\` instead

Streams client data to the model.

Calling this after `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation()` will play the response audio immediately.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/MediaData> mediaChunks` | The list of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/MediaData` instances representing the media data to be sent. |

### sendTextRealtime

```
public abstract @NonNull ListenableFuture<Unit> sendTextRealtime(@NonNull String text)
```

For details about the realtime input usage, see the `BidiGenerateContentRealtimeInput` documentation ( [Gemini Developer API](https://ai.google.dev/api/live#bidigeneratecontentrealtimeinput) or [Vertex AI Gemini API](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/multimodal-live#bidigeneratecontentrealtimeinput) ).

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html text` | The text data to send. |

### sendVideoRealtime

```
public abstract @NonNull ListenableFuture<Unit> sendVideoRealtime(@NonNull InlineData video)
```

Sends a video input stream to the model, using the realtime API.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineData video` | The video data to send. Video MIME type could be either video or image. |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
public abstract @NonNull ListenableFuture<Unit> startAudioConversation()
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()`.

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
public abstract @NonNull ListenableFuture<Unit> startAudioConversation(boolean enableInterruptions)
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#close()`.

| Parameters |
|---|---|
| `boolean enableInterruptions` | If enabled, allows the user to speak over or interrupt the model's ongoing reply. **WARNING**: The user interruption feature relies on device-specific support, and may not be consistently available. |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
public abstract @NonNull ListenableFuture<Unit> startAudioConversation(
    Function1<@NonNull FunctionCallPart, @NonNull FunctionResponsePart> functionCallHandler
)
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#close()`.

| Parameters |
|---|---|
| `Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart> functionCallHandler` | A callback function that is invoked whenever the model receives a function call. |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
public abstract @NonNull ListenableFuture<Unit> startAudioConversation(
    @NonNull LiveAudioConversationConfig liveAudioConversationConfig
)
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig liveAudioConversationConfig` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveAudioConversationConfig` provided by the user to control the various aspects of the conversation. |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
public abstract @NonNull ListenableFuture<Unit> startAudioConversation(
    Function2<Transcription, Transcription, Unit> transcriptHandler
)
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()`.

| Parameters |
|---|---|
| `Function2<https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> transcriptHandler` | A callback function that is invoked whenever the model receives a transcript. The first `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription` object is the input transcription, and the second is the output transcription |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
public abstract @NonNull ListenableFuture<Unit> startAudioConversation(
    Function1<@NonNull FunctionCallPart, @NonNull FunctionResponsePart> functionCallHandler,
    boolean enableInterruptions
)
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#close()`.

| Parameters |
|---|---|
| `Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart> functionCallHandler` | A callback function that is invoked whenever the model receives a function call. |
| `boolean enableInterruptions` | If enabled, allows the user to speak over or interrupt the model's ongoing reply. **WARNING**: The user interruption feature relies on device-specific support, and may not be consistently available. |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
public abstract @NonNull ListenableFuture<Unit> startAudioConversation(
    Function2<Transcription, Transcription, Unit> transcriptHandler,
    boolean enableInterruptions
)
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#close()`.

| Parameters |
|---|---|
| `Function2<https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> transcriptHandler` | A callback function that is invoked whenever the model receives a transcript. The first `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription` object is the input transcription, and the second is the output transcription |
| `boolean enableInterruptions` | If enabled, allows the user to speak over or interrupt the model's ongoing reply. **WARNING**: The user interruption feature relies on device-specific support, and may not be consistently available. |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
public abstract @NonNull ListenableFuture<Unit> startAudioConversation(
    Function1<@NonNull FunctionCallPart, @NonNull FunctionResponsePart> functionCallHandler,
    Function2<Transcription, Transcription, Unit> transcriptHandler,
    boolean enableInterruptions
)
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#close()`.

| Parameters |
|---|---|
| `Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionCallPart, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FunctionResponsePart> functionCallHandler` | A callback function that is invoked whenever the model receives a function call. |
| `Function2<https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> transcriptHandler` | A callback function that is invoked whenever the model receives a transcript. The first `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Transcription` object is the input transcription, and the second is the output transcription |
| `boolean enableInterruptions` | If enabled, allows the user to speak over or interrupt the model's ongoing reply. **WARNING**: The user interruption feature relies on device-specific support, and may not be consistently available. |

### stopAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
public abstract @NonNull ListenableFuture<Unit> stopAudioConversation()
```

Stops the audio conversation with the Gemini Server.

This only needs to be called after a previous call to `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation()`.

If there is no audio conversation currently active, this function does nothing.

### stopReceiving

```
public abstract void stopReceiving()
```

Stops receiving from the model.

If this function is called during an ongoing audio conversation, the model's response will not be received, and no audio will be played; the live session object will no longer receive data from the server.

To resume receiving data, you must either handle it directly using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#receive()`, or indirectly by using `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation()`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures#close()` |   |