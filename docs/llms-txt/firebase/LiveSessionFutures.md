# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/LiveSessionFutures.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/LiveSessionFutures.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures.md.txt

# LiveSessionFutures

<br />

```
@PublicPreviewAPI
abstract class LiveSessionFutures
```

<br />

*** ** * ** ***

Wrapper class providing Java compatible methods for[LiveSession](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession).  

|                                                 See also                                                 |
|----------------------------------------------------------------------------------------------------------|---|
| [LiveSession](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession) |   |

## Summary

|                                             ### Public companion functions                                             |
|------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [LiveSessionFutures](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures) | [from](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures.Companion#from(com.google.firebase.ai.type.LiveSession))`(session: `[LiveSession](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession)`)` |

|                                                                                                       ### Public functions                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`>`             | [close](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close())`()` Closes the client session.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `abstract `[Publisher](https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher)`<`[LiveServerMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveServerMessage)`>` | [receive](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#receive())`()` Receives responses from the model for both streaming and standard requests.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`>`             | [send](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#send(com.google.firebase.ai.type.Content))`(content: `[Content](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content)`)` Sends[data](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content)to the model.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`>`             | [send](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#send(kotlin.String))`(text: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Sends text to the model.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`>`             | [sendAudioRealtime](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#sendAudioRealtime(com.google.firebase.ai.type.InlineData))`(audio: `[InlineData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineData)`)` Sends an audio input stream to the model, using the realtime API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`>`             | [sendFunctionResponse](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#sendFunctionResponse(kotlin.collections.List))`(functionList: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[FunctionResponsePart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)`>)` Sends function calling responses to the model.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`>`             | ~~[sendMediaStream](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#sendMediaStream(kotlin.collections.List))~~`(mediaChunks: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[MediaData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/MediaData)`>)` **This function is deprecated.**Use \`sendAudioRealtime\`, \`sendVideoRealtime\`, or \`sendTextRealtime\` instead                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`>`             | [sendTextRealtime](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#sendTextRealtime(kotlin.String))`(text: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` For details about the realtime input usage, see the`BidiGenerateContentRealtimeInput`documentation ([Gemini Developer API](https://ai.google.dev/api/live#bidigeneratecontentrealtimeinput)or[Vertex AI Gemini API](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/multimodal-live#bidigeneratecontentrealtimeinput)).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`>`             | [sendVideoRealtime](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#sendVideoRealtime(com.google.firebase.ai.type.InlineData))`(video: `[InlineData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineData)`)` Sends a video input stream to the model, using the realtime API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`>`             | `@`[RequiresPermission](https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html)`(value = "android.permission.RECORD_AUDIO")` [startAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation())`()` Starts an audio conversation with the model, which can only be stopped using[stopAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`>`             | `@`[RequiresPermission](https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html)`(value = "android.permission.RECORD_AUDIO")` [startAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation(kotlin.Boolean))`(enableInterruptions: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`)` Starts an audio conversation with the model, which can only be stopped using[stopAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation())or[close](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close()).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`>`             | `@`[RequiresPermission](https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html)`(value = "android.permission.RECORD_AUDIO")` [startAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation(kotlin.Function1))`(` ` functionCallHandler: ((`[FunctionCallPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart)`) `->` `[FunctionResponsePart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)`)?` `)` Starts an audio conversation with the model, which can only be stopped using[stopAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation())or[close](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close()).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`>`             | `@`[RequiresPermission](https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html)`(value = "android.permission.RECORD_AUDIO")` [startAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation(com.google.firebase.ai.type.LiveAudioConversationConfig))`(` ` liveAudioConversationConfig: `[LiveAudioConversationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig) `)` Starts an audio conversation with the model, which can only be stopped using[stopAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`>`             | `@`[RequiresPermission](https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html)`(value = "android.permission.RECORD_AUDIO")` [startAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation(kotlin.Function2))`(` ` transcriptHandler: ((`[Transcription](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription)`?, `[Transcription](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription)`?) `->` `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`)?` `)` Starts an audio conversation with the model, which can only be stopped using[stopAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`>`             | `@`[RequiresPermission](https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html)`(value = "android.permission.RECORD_AUDIO")` [startAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation(kotlin.Function1,kotlin.Boolean))`(` ` functionCallHandler: ((`[FunctionCallPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart)`) `->` `[FunctionResponsePart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)`)?,` ` enableInterruptions: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) `)` Starts an audio conversation with the model, which can only be stopped using[stopAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation())or[close](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close()).                                                                                                                                                                                                                                                                                                                                                                   |
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`>`             | `@`[RequiresPermission](https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html)`(value = "android.permission.RECORD_AUDIO")` [startAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation(kotlin.Function2,kotlin.Boolean))`(` ` transcriptHandler: ((`[Transcription](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription)`?, `[Transcription](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription)`?) `->` `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`)?,` ` enableInterruptions: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) `)` Starts an audio conversation with the model, which can only be stopped using[stopAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation())or[close](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close()).                                                                                                                                                                                                                                                                                                       |
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`>`             | `@`[RequiresPermission](https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html)`(value = "android.permission.RECORD_AUDIO")` [startAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation(kotlin.Function1,kotlin.Function2,kotlin.Boolean))`(` ` functionCallHandler: ((`[FunctionCallPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart)`) `->` `[FunctionResponsePart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)`)?,` ` transcriptHandler: ((`[Transcription](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription)`?, `[Transcription](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription)`?) `->` `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`)?,` ` enableInterruptions: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) `)` Starts an audio conversation with the model, which can only be stopped using[stopAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation())or[close](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close()). |
| `abstract `[ListenableFuture](https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture)`<`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`>`             | `@`[RequiresPermission](https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html)`(value = "android.permission.RECORD_AUDIO")` [stopAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation())`()` Stops the audio conversation with the Gemini Server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `abstract `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                                           | [stopReceiving](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopReceiving())`()` Stops receiving from the model.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## Public companion functions

### from

```
funÂ from(session:Â LiveSession):Â LiveSessionFutures
```  

|                                                        Returns                                                         |
|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [LiveSessionFutures](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures) | a[LiveSessionFutures](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures)created around the provided[LiveSession](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession) |

## Public functions

### close

```
abstractÂ funÂ close():Â ListenableFuture<Unit>
```

Closes the client session.

Once a[LiveSession](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession)is closed, it can not be reopened; you'll need to start a new[LiveSession](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession).  

|                                                             See also                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------|---|
| [stopReceiving](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopReceiving()) |   |

### receive

```
abstractÂ funÂ receive():Â Publisher<LiveServerMessage>
```

Receives responses from the model for both streaming and standard requests.

Call[close](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close())to stop receiving responses from the model.  

|                                                                                                        Returns                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Publisher](https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher)`<`[LiveServerMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveServerMessage)`>` | A[Publisher](https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher)which will emit[LiveServerMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveServerMessage)from the model. |

|                                                                                                                     Throws                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| `com.google.firebase.ai.type.SessionAlreadyReceivingException: `[com.google.firebase.ai.type.SessionAlreadyReceivingException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SessionAlreadyReceivingException) | when the session is already receiving. |

|                                                             See also                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------|---|
| [stopReceiving](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopReceiving()) |   |

### send

```
abstractÂ funÂ send(content:Â Content):Â ListenableFuture<Unit>
```

Sends[data](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content)to the model.

Calling this after[startAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation())will play the response audio immediately.  

|                                                 Parameters                                                  |
|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| `content: `[Content](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content) | Client[Content](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content)to be sent to the model. |

### send

```
abstractÂ funÂ send(text:Â String):Â ListenableFuture<Unit>
```

Sends text to the model.

Calling this after[startAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation())will play the response audio immediately.  

|                                        Parameters                                        |
|------------------------------------------------------------------------------------------|-------------------------------|
| `text: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | Text to be sent to the model. |

### sendAudioRealtime

```
abstractÂ funÂ sendAudioRealtime(audio:Â InlineData):Â ListenableFuture<Unit>
```

Sends an audio input stream to the model, using the realtime API.  

|                                                   Parameters                                                    |
|-----------------------------------------------------------------------------------------------------------------|-------------------------|
| `audio: `[InlineData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineData) | The audio data to send. |

### sendFunctionResponse

```
abstractÂ funÂ sendFunctionResponse(functionList:Â List<FunctionResponsePart>):Â ListenableFuture<Unit>
```

Sends function calling responses to the model.  

|                                                                                                                Parameters                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `functionList: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[FunctionResponsePart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)`>` | The list of[FunctionResponsePart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)instances indicating the function response from the client. |

### sendMediaStream

```
abstractÂ funÂ [sendMediaStream](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#sendMediaStream(kotlin.collections.List))(mediaChunks:Â List<MediaData>):Â ListenableFuture<Unit>
```
| **This function is deprecated.**   
| Use \`sendAudioRealtime\`, \`sendVideoRealtime\`, or \`sendTextRealtime\` instead

Streams client data to the model.

Calling this after[startAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation())will play the response audio immediately.  

|                                                                                                    Parameters                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `mediaChunks: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[MediaData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/MediaData)`>` | The list of[MediaData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/MediaData)instances representing the media data to be sent. |

### sendTextRealtime

```
abstractÂ funÂ sendTextRealtime(text:Â String):Â ListenableFuture<Unit>
```

For details about the realtime input usage, see the`BidiGenerateContentRealtimeInput`documentation ([Gemini Developer API](https://ai.google.dev/api/live#bidigeneratecontentrealtimeinput)or[Vertex AI Gemini API](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/multimodal-live#bidigeneratecontentrealtimeinput)).  

|                                        Parameters                                        |
|------------------------------------------------------------------------------------------|------------------------|
| `text: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The text data to send. |

### sendVideoRealtime

```
abstractÂ funÂ sendVideoRealtime(video:Â InlineData):Â ListenableFuture<Unit>
```

Sends a video input stream to the model, using the realtime API.  

|                                                   Parameters                                                    |
|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `video: `[InlineData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/InlineData) | The video data to send. Video MIME type could be either video or image. |

### startAudioConversation

```
@RequiresPermission(valueÂ =Â "android.permission.RECORD_AUDIO")
abstractÂ funÂ startAudioConversation():Â ListenableFuture<Unit>
```

Starts an audio conversation with the model, which can only be stopped using[stopAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()).  

### startAudioConversation

```
@RequiresPermission(valueÂ =Â "android.permission.RECORD_AUDIO")
abstractÂ funÂ startAudioConversation(enableInterruptions:Â Boolean):Â ListenableFuture<Unit>
```

Starts an audio conversation with the model, which can only be stopped using[stopAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation())or[close](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close()).  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `enableInterruptions: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | If enabled, allows the user to speak over or interrupt the model's ongoing reply. **WARNING**: The user interruption feature relies on device-specific support, and may not be consistently available. |

### startAudioConversation

```
@RequiresPermission(valueÂ =Â "android.permission.RECORD_AUDIO")
abstractÂ funÂ startAudioConversation(
Â Â Â Â functionCallHandler:Â ((FunctionCallPart) -> FunctionResponsePart)?
):Â ListenableFuture<Unit>
```

Starts an audio conversation with the model, which can only be stopped using[stopAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation())or[close](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close()).  

|                                                                                                                                     Parameters                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| `functionCallHandler: ((`[FunctionCallPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart)`) `->` `[FunctionResponsePart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)`)?` | A callback function that is invoked whenever the model receives a function call. |

### startAudioConversation

```
@RequiresPermission(valueÂ =Â "android.permission.RECORD_AUDIO")
abstractÂ funÂ startAudioConversation(
Â Â Â Â liveAudioConversationConfig:Â LiveAudioConversationConfig
):Â ListenableFuture<Unit>
```

Starts an audio conversation with the model, which can only be stopped using[stopAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()).  

|                                                                               Parameters                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `liveAudioConversationConfig: `[LiveAudioConversationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig) | A[LiveAudioConversationConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveAudioConversationConfig)provided by the user to control the various aspects of the conversation. |

### startAudioConversation

```
@RequiresPermission(valueÂ =Â "android.permission.RECORD_AUDIO")
abstractÂ funÂ startAudioConversation(
Â Â Â Â transcriptHandler:Â ((Transcription?, Transcription?) -> Unit)?
):Â ListenableFuture<Unit>
```

Starts an audio conversation with the model, which can only be stopped using[stopAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation()).  

|                                                                                                                                                                   Parameters                                                                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `transcriptHandler: ((`[Transcription](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription)`?, `[Transcription](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription)`?) `->` `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`)?` | A callback function that is invoked whenever the model receives a transcript. The first[Transcription](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription)object is the input transcription, and the second is the output transcription |

### startAudioConversation

```
@RequiresPermission(valueÂ =Â "android.permission.RECORD_AUDIO")
abstractÂ funÂ startAudioConversation(
Â Â Â Â functionCallHandler:Â ((FunctionCallPart) -> FunctionResponsePart)?,
Â Â Â Â enableInterruptions:Â Boolean
):Â ListenableFuture<Unit>
```

Starts an audio conversation with the model, which can only be stopped using[stopAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation())or[close](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close()).  

|                                                                                                                                     Parameters                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `functionCallHandler: ((`[FunctionCallPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart)`) `->` `[FunctionResponsePart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)`)?` | A callback function that is invoked whenever the model receives a function call.                                                                                                                       |
| `enableInterruptions: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                                                                                                          | If enabled, allows the user to speak over or interrupt the model's ongoing reply. **WARNING**: The user interruption feature relies on device-specific support, and may not be consistently available. |

### startAudioConversation

```
@RequiresPermission(valueÂ =Â "android.permission.RECORD_AUDIO")
abstractÂ funÂ startAudioConversation(
Â Â Â Â transcriptHandler:Â ((Transcription?, Transcription?) -> Unit)?,
Â Â Â Â enableInterruptions:Â Boolean
):Â ListenableFuture<Unit>
```

Starts an audio conversation with the model, which can only be stopped using[stopAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation())or[close](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close()).  

|                                                                                                                                                                   Parameters                                                                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `transcriptHandler: ((`[Transcription](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription)`?, `[Transcription](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription)`?) `->` `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`)?` | A callback function that is invoked whenever the model receives a transcript. The first[Transcription](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription)object is the input transcription, and the second is the output transcription |
| `enableInterruptions: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                                                                                                                                                                      | If enabled, allows the user to speak over or interrupt the model's ongoing reply. **WARNING**: The user interruption feature relies on device-specific support, and may not be consistently available.                                                                           |

### startAudioConversation

```
@RequiresPermission(valueÂ =Â "android.permission.RECORD_AUDIO")
abstractÂ funÂ startAudioConversation(
Â Â Â Â functionCallHandler:Â ((FunctionCallPart) -> FunctionResponsePart)?,
Â Â Â Â transcriptHandler:Â ((Transcription?, Transcription?) -> Unit)?,
Â Â Â Â enableInterruptions:Â Boolean
):Â ListenableFuture<Unit>
```

Starts an audio conversation with the model, which can only be stopped using[stopAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#stopAudioConversation())or[close](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close()).  

|                                                                                                                                                                   Parameters                                                                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `functionCallHandler: ((`[FunctionCallPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionCallPart)`) `->` `[FunctionResponsePart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FunctionResponsePart)`)?`                                                             | A callback function that is invoked whenever the model receives a function call.                                                                                                                                                                                                 |
| `transcriptHandler: ((`[Transcription](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription)`?, `[Transcription](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription)`?) `->` `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`)?` | A callback function that is invoked whenever the model receives a transcript. The first[Transcription](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Transcription)object is the input transcription, and the second is the output transcription |
| `enableInterruptions: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                                                                                                                                                                      | If enabled, allows the user to speak over or interrupt the model's ongoing reply. **WARNING**: The user interruption feature relies on device-specific support, and may not be consistently available.                                                                           |

### stopAudioConversation

```
@RequiresPermission(valueÂ =Â "android.permission.RECORD_AUDIO")
abstractÂ funÂ stopAudioConversation():Â ListenableFuture<Unit>
```

Stops the audio conversation with the Gemini Server.

This only needs to be called after a previous call to[startAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation()).

If there is no audio conversation currently active, this function does nothing.  

### stopReceiving

```
abstractÂ funÂ stopReceiving():Â Unit
```

Stops receiving from the model.

If this function is called during an ongoing audio conversation, the model's response will not be received, and no audio will be played; the live session object will no longer receive data from the server.

To resume receiving data, you must either handle it directly using[receive](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#receive()), or indirectly by using[startAudioConversation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#startAudioConversation()).  

|                                                     See also                                                      |
|-------------------------------------------------------------------------------------------------------------------|---|
| [close](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/LiveSessionFutures#close()) |   |