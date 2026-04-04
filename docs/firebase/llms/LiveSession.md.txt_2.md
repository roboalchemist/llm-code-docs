# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession.md.txt

# LiveSession

# LiveSession


```
@PublicPreviewAPI
public final class LiveSession
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents a live WebSocket session capable of streaming content to and from the server.

## Summary

| ### Public methods |
|---|---|
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#close()()` Closes the client session. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveServerMessage>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#receive()()` Receives responses from the model for both streaming and standard requests. |
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#send(com.google.firebase.vertexai.type.Content)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content content)` Sends `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` to the model. |
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#send(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html text)` Sends text to the model. |
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#sendFunctionResponse(kotlin.collections.List)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart> functionList )` Sends function calling responses to the model. |
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#sendMediaStream(kotlin.collections.List)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/MediaData> mediaChunks)` Streams client data to the model. |
| `final void` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#startAudioConversation(kotlin.Function1)( Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart> functionCallHandler )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#stopAudioConversation()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#close()`. |
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#stopAudioConversation()()` Stops the audio conversation with the model. |
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#stopReceiving()()` Stops receiving from the model. |

## Public methods

### close

```
public final void close()
```

Closes the client session.

Once a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession` is closed, it can not be reopened; you'll need to start a new `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#stopReceiving()` |   |

### receive

```
public final @NonNull Flow<@NonNull LiveServerMessage> receive()
```

Receives responses from the model for both streaming and standard requests.

Call `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#close()` to stop receiving responses from the model.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveServerMessage>` | A `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html` which will emit `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveServerMessage` from the model. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SessionAlreadyReceivingException com.google.firebase.vertexai.type.SessionAlreadyReceivingException` | when the session is already receiving. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#stopReceiving()` |   |

### send

```
public final void send(@NonNull Content content)
```

Sends `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` to the model.

Calling this after `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#startAudioConversation(kotlin.Function1)` will play the response audio immediately.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content content` | Client `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` to be sent to the model. |

### send

```
public final void send(@NonNull String text)
```

Sends text to the model.

Calling this after `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#startAudioConversation(kotlin.Function1)` will play the response audio immediately.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html text` | Text to be sent to the model. |

### sendFunctionResponse

```
public final void sendFunctionResponse(
    @NonNull List<@NonNull FunctionResponsePart> functionList
)
```

Sends function calling responses to the model.

**NOTE:** If you're using `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#startAudioConversation(kotlin.Function1)`, the method will handle sending function responses to the model for you. You do *not* need to call this method in that case.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart> functionList` | The list of `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart` instances indicating the function response from the client. |

### sendMediaStream

```
public final void sendMediaStream(@NonNull List<@NonNull MediaData> mediaChunks)
```

Streams client data to the model.

Calling this after `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#startAudioConversation(kotlin.Function1)` will play the response audio immediately.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/MediaData> mediaChunks` | The list of `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/MediaData` instances representing the media data to be sent. |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
public final void startAudioConversation(
    Function1<@NonNull FunctionCallPart, @NonNull FunctionResponsePart> functionCallHandler
)
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#stopAudioConversation()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#close()`.

| Parameters |
|---|---|
| `Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart> functionCallHandler` | A callback function that is invoked whenever the model receives a function call. The `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart` that the callback function returns will be automatically sent to the model. |

### stopAudioConversation

```
public final void stopAudioConversation()
```

Stops the audio conversation with the model.

This only needs to be called after a previous call to `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#startAudioConversation(kotlin.Function1)`.

If there is no audio conversation currently active, this function does nothing.

### stopReceiving

```
public final void stopReceiving()
```

Stops receiving from the model.

If this function is called during an ongoing audio conversation, the model's response will not be received, and no audio will be played; the live session object will no longer receive data from the server.

To resume receiving data, you must either handle it directly using `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#receive()`, or indirectly by using `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#startAudioConversation(kotlin.Function1)`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession#close()` |   |