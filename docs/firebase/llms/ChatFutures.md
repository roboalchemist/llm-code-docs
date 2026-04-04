# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ChatFutures.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ChatFutures.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures.md.txt

# ChatFutures

# ChatFutures


```
public abstract class ChatFutures
```

<br />

*** ** * ** ***

Wrapper class providing Java compatible methods for [Chat](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/Chat).  

|                                        See also                                        |
|----------------------------------------------------------------------------------------|---|
| [Chat](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/Chat) |   |

## Summary

|                                                                  ### Nested types                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `public static class `[ChatFutures.Companion](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures.Companion) |

|                                                                                                                                                                                                                           ### Public methods                                                                                                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ChatFutures](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures)                                                                                                                                                                                                                                                  | [from](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures.Companion#from(com.google.firebase.ai.Chat))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Chat](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/Chat)` chat)`                                                                                                                                                                                                                                    |
| `abstract @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Chat](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/Chat)                                                                                                                                                                                                                                                                         | [getChat](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures#getChat())`()` Returns the [Chat](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/Chat) object wrapped by this object.                                                                                                                                                                                                                                                                                                                            |
| `abstract @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ListenableFuture](https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[GenerateContentResponse](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse)`>` | [sendMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures#sendMessage(com.google.firebase.ai.type.Content))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Content](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content)` prompt)` Sends a message using the existing history of this chat as context and the provided [Content](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content) prompt.             |
| `abstract @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Publisher](https://firebase.google.com/docs/reference/android/org/reactivestreams/Publisher)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[GenerateContentResponse](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse)`>`                             | [sendMessageStream](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures#sendMessageStream(com.google.firebase.ai.type.Content))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Content](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content)` prompt)` Sends a message using the existing history of this chat as context and the provided [Content](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content) prompt. |

## Public methods

### from

```
publicÂ staticÂ finalÂ @NonNull ChatFuturesÂ from(@NonNull ChatÂ chat)
```  

|                                                                                                  Returns                                                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ChatFutures](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures) | a [ChatFutures](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures) created around the provided [Chat](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/Chat) |

### getChat

```
publicÂ abstractÂ @NonNull ChatÂ getChat()
```

Returns the [Chat](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/Chat) object wrapped by this object.  

### sendMessage

```
publicÂ abstractÂ @NonNull ListenableFuture<@NonNull GenerateContentResponse>Â sendMessage(@NonNull ContentÂ prompt)
```

Sends a message using the existing history of this chat as context and the provided [Content](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content) prompt.

If successful, the message and response will be added to the history. If unsuccessful, history will remain unchanged.  

|                                                                                                 Parameters                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Content](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content)` prompt` | The input(s) that, together with the history, will be given to the model as the prompt. |

|                                                                                                    Throws                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [com.google.firebase.ai.type.InvalidStateException](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InvalidStateException)` com.google.firebase.ai.type.InvalidStateException` | if [prompt](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures#sendMessage(com.google.firebase.ai.type.Content)) is not coming from the 'user' role |
| [com.google.firebase.ai.type.InvalidStateException](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InvalidStateException)` com.google.firebase.ai.type.InvalidStateException` | if the [Chat](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/Chat) instance has an active request                                                                |

### sendMessageStream

```
publicÂ abstractÂ @NonNull Publisher<@NonNull GenerateContentResponse>Â sendMessageStream(@NonNull ContentÂ prompt)
```

Sends a message using the existing history of this chat as context and the provided [Content](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content) prompt.

The response from the model is returned as a stream.

If successful, the message and response will be added to the history. If unsuccessful, history will remain unchanged.  

|                                                                                                 Parameters                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Content](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content)` prompt` | The input(s) that, together with the history, will be given to the model as the prompt. |

|                                                                                                    Throws                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [com.google.firebase.ai.type.InvalidStateException](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InvalidStateException)` com.google.firebase.ai.type.InvalidStateException` | if [prompt](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures#sendMessageStream(com.google.firebase.ai.type.Content)) is not coming from the 'user' role |
| [com.google.firebase.ai.type.InvalidStateException](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InvalidStateException)` com.google.firebase.ai.type.InvalidStateException` | if the [Chat](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/Chat) instance has an active request                                                                      |