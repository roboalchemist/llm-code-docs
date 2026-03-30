# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures.md.txt

# LiveSessionFutures

# LiveSessionFutures


```
@PublicPreviewAPI
public abstract class LiveSessionFutures
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Wrapper class providing Java compatible methods for `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession` |   |

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures.Companion` |

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#close()()` Closes the client session. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures.Companion#from(com.google.firebase.vertexai.type.LiveSession)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession session)` |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/org/reactivestreams/Publisher<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveServerMessage>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#receive()()` Receives responses from the model for both streaming and standard requests. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#send(com.google.firebase.vertexai.type.Content)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content content)` Sends `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` to the model. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#send(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html text)` Sends text to the model. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#sendFunctionResponse(kotlin.collections.List)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart> functionList )` Sends function calling responses to the model. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#sendMediaStream(kotlin.collections.List)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/MediaData> mediaChunks)` Streams client data to the model. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#startAudioConversation()()` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#stopAudioConversation()`. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#startAudioConversation(kotlin.Function1)( Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart> functionCallHandler )` Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#stopAudioConversation()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#close()`. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html>` | `@https://developer.android.com/reference/kotlin/androidx/annotation/RequiresPermission.html(value = "android.permission.RECORD_AUDIO") https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#stopAudioConversation()()` Stops the audio conversation with the Gemini Server. |
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#stopReceiving()()` Stops receiving from the model. |

## Public methods

### close

```
public abstract @NonNull ListenableFuture<Unit> close()
```

Closes the client session.

Once a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession` is closed, it can not be reopened; you'll need to start a new `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#stopReceiving()` |   |

### from

```
public static final @NonNull LiveSessionFutures from(@NonNull LiveSession session)
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures` | a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures` created around the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveSession` |

### receive

```
public abstract @NonNull Publisher<@NonNull LiveServerMessage> receive()
```

Receives responses from the model for both streaming and standard requests.

Call `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#close()` to stop receiving responses from the model.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/org/reactivestreams/Publisher<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveServerMessage>` | A `https://firebase.google.com/docs/reference/android/org/reactivestreams/Publisher` which will emit `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveServerMessage` from the model. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SessionAlreadyReceivingException com.google.firebase.vertexai.type.SessionAlreadyReceivingException` | when the session is already receiving. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#stopReceiving()` |   |

### send

```
public abstract @NonNull ListenableFuture<Unit> send(@NonNull Content content)
```

Sends `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` to the model.

Calling this after `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#startAudioConversation(kotlin.Function1)` will play the response audio immediately.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content content` | Client `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` to be sent to the model. |

### send

```
public abstract @NonNull ListenableFuture<Unit> send(@NonNull String text)
```

Sends text to the model.

Calling this after `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#startAudioConversation(kotlin.Function1)` will play the response audio immediately.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html text` | Text to be sent to the model. |

### sendFunctionResponse

```
public abstract @NonNull ListenableFuture<Unit> sendFunctionResponse(
    @NonNull List<@NonNull FunctionResponsePart> functionList
)
```

Sends function calling responses to the model.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart> functionList` | The list of `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart` instances indicating the function response from the client. |

### sendMediaStream

```
public abstract @NonNull ListenableFuture<Unit> sendMediaStream(@NonNull List<@NonNull MediaData> mediaChunks)
```

Streams client data to the model.

Calling this after `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#startAudioConversation(kotlin.Function1)` will play the response audio immediately.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/MediaData> mediaChunks` | The list of `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/MediaData` instances representing the media data to be sent. |

### startAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
public abstract @NonNull ListenableFuture<Unit> startAudioConversation()
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#stopAudioConversation()`.

### startAudioConversation

```
public abstract @NonNull ListenableFuture<Unit> startAudioConversation(
    Function1<@NonNull FunctionCallPart, @NonNull FunctionResponsePart> functionCallHandler
)
```

Starts an audio conversation with the model, which can only be stopped using `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#stopAudioConversation()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#close()`.

| Parameters |
|---|---|
| `Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionResponsePart> functionCallHandler` | A callback function that is invoked whenever the model receives a function call. |

### stopAudioConversation

```
@RequiresPermission(value = "android.permission.RECORD_AUDIO")
public abstract @NonNull ListenableFuture<Unit> stopAudioConversation()
```

Stops the audio conversation with the Gemini Server.

This only needs to be called after a previous call to `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#startAudioConversation(kotlin.Function1)`.

If there is no audio conversation currently active, this function does nothing.

### stopReceiving

```
public abstract void stopReceiving()
```

Stops receiving from the model.

If this function is called during an ongoing audio conversation, the model's response will not be received, and no audio will be played; the live session object will no longer receive data from the server.

To resume receiving data, you must either handle it directly using `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#receive()`, or indirectly by using `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#startAudioConversation(kotlin.Function1)`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/LiveSessionFutures#close()` |   |