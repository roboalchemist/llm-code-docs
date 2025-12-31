# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveSession.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveSession.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveSession.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession.md.txt

# LiveSession

# LiveSession


```
@PublicPreviewAPI
public final class LiveSession
```

<br />

*** ** * ** ***

| **This class is deprecated.**   
| The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents a live WebSocket session capable of streaming content to and from the server.

## Summary

|                                                                                                                                                                                                                     ### Public methods                                                                                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final void`                                                                                                                                                                                                                                                                                                                                                                                                                                                | [close](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#close())`()` Closes the client session.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[LiveServerMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveServerMessage)`>` | [receive](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#receive())`()` Receives responses from the model for both streaming and standard requests.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `final void`                                                                                                                                                                                                                                                                                                                                                                                                                                                | [send](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#send(com.google.firebase.vertexai.type.Content))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Content](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content)` content)` Sends [data](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content) to the model.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `final void`                                                                                                                                                                                                                                                                                                                                                                                                                                                | [send](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#send(kotlin.String))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` text)` Sends text to the model.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `final void`                                                                                                                                                                                                                                                                                                                                                                                                                                                | [sendFunctionResponse](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#sendFunctionResponse(kotlin.collections.List))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FunctionResponsePart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart)`> functionList` `)` Sends function calling responses to the model.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `final void`                                                                                                                                                                                                                                                                                                                                                                                                                                                | [sendMediaStream](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#sendMediaStream(kotlin.collections.List))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MediaData](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/MediaData)`> mediaChunks)` Streams client data to the model.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `final void`                                                                                                                                                                                                                                                                                                                                                                                                                                                | `@`[RequiresPermission](https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html)`(value = "android.permission.RECORD_AUDIO")` [startAudioConversation](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#startAudioConversation(kotlin.Function1))`(` ` Function1<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FunctionCallPart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart)`, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FunctionResponsePart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart)`> functionCallHandler` `)` Starts an audio conversation with the model, which can only be stopped using [stopAudioConversation](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#stopAudioConversation()) or [close](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#close()). |
| `final void`                                                                                                                                                                                                                                                                                                                                                                                                                                                | [stopAudioConversation](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#stopAudioConversation())`()` Stops the audio conversation with the model.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `final void`                                                                                                                                                                                                                                                                                                                                                                                                                                                | [stopReceiving](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#stopReceiving())`()` Stops receiving from the model.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## Public methods

### close

```
publicÂ finalÂ voidÂ close()
```

Closes the client session.

Once a [LiveSession](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession) is closed, it can not be reopened; you'll need to start a new [LiveSession](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession).  

|                                                             See also                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------|---|
| [stopReceiving](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#stopReceiving()) |   |

### receive

```
publicÂ finalÂ @NonNull Flow<@NonNull LiveServerMessage>Â receive()
```

Receives responses from the model for both streaming and standard requests.

Call [close](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#close()) to stop receiving responses from the model.  

|                                                                                                                                                                                                                        Returns                                                                                                                                                                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[LiveServerMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveServerMessage)`>` | A [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html) which will emit [LiveServerMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveServerMessage) from the model. |

|                                                                                                                              Throws                                                                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| [com.google.firebase.vertexai.type.SessionAlreadyReceivingException](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SessionAlreadyReceivingException)` com.google.firebase.vertexai.type.SessionAlreadyReceivingException` | when the session is already receiving. |

|                                                             See also                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------|---|
| [stopReceiving](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#stopReceiving()) |   |

### send

```
publicÂ finalÂ voidÂ send(@NonNull ContentÂ content)
```

Sends [data](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content) to the model.

Calling this after [startAudioConversation](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#startAudioConversation(kotlin.Function1)) will play the response audio immediately.  

|                                                                                                    Parameters                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Content](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content)` content` | Client [Content](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content) to be sent to the model. |

### send

```
publicÂ finalÂ voidÂ send(@NonNull StringÂ text)
```

Sends text to the model.

Calling this after [startAudioConversation](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#startAudioConversation(kotlin.Function1)) will play the response audio immediately.  

|                                                                                      Parameters                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` text` | Text to be sent to the model. |

### sendFunctionResponse

```
publicÂ finalÂ voidÂ sendFunctionResponse(
Â Â Â Â @NonNull List<@NonNull FunctionResponsePart>Â functionList
)
```

Sends function calling responses to the model.

**NOTE:** If you're using [startAudioConversation](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#startAudioConversation(kotlin.Function1)), the method will handle sending function responses to the model for you. You do *not* need to call this method in that case.  

|                                                                                                                                                                                                          Parameters                                                                                                                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FunctionResponsePart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart)`> functionList` | The list of [FunctionResponsePart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart) instances indicating the function response from the client. |

### sendMediaStream

```
publicÂ finalÂ voidÂ sendMediaStream(@NonNull List<@NonNull MediaData>Â mediaChunks)
```

Streams client data to the model.

Calling this after [startAudioConversation](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#startAudioConversation(kotlin.Function1)) will play the response audio immediately.  

|                                                                                                                                                                                              Parameters                                                                                                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MediaData](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/MediaData)`> mediaChunks` | The list of [MediaData](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/MediaData) instances representing the media data to be sent. |

### startAudioConversation

```
@RequiresPermission(valueÂ =Â "android.permission.RECORD_AUDIO")
publicÂ finalÂ voidÂ startAudioConversation(
Â Â Â Â Function1<@NonNull FunctionCallPart,Â @NonNull FunctionResponsePart>Â functionCallHandler
)
```

Starts an audio conversation with the model, which can only be stopped using [stopAudioConversation](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#stopAudioConversation()) or [close](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#close()).  

|                                                                                                                                                                                                                                          Parameters                                                                                                                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Function1<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FunctionCallPart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart)`, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FunctionResponsePart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart)`> functionCallHandler` | A callback function that is invoked whenever the model receives a function call. The [FunctionResponsePart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart) that the callback function returns will be automatically sent to the model. |

### stopAudioConversation

```
publicÂ finalÂ voidÂ stopAudioConversation()
```

Stops the audio conversation with the model.

This only needs to be called after a previous call to [startAudioConversation](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#startAudioConversation(kotlin.Function1)).

If there is no audio conversation currently active, this function does nothing.  

### stopReceiving

```
publicÂ finalÂ voidÂ stopReceiving()
```

Stops receiving from the model.

If this function is called during an ongoing audio conversation, the model's response will not be received, and no audio will be played; the live session object will no longer receive data from the server.

To resume receiving data, you must either handle it directly using [receive](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#receive()), or indirectly by using [startAudioConversation](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#startAudioConversation(kotlin.Function1)).  

|                                                     See also                                                      |
|-------------------------------------------------------------------------------------------------------------------|---|
| [close](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#close()) |   |