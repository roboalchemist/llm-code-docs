# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/GenerativeModelFutures.md.txt

# GenerativeModelFutures

# GenerativeModelFutures


```
public abstract class GenerativeModelFutures
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Wrapper class providing Java compatible methods for `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/GenerativeModel`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/GenerativeModel` |   |

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/GenerativeModelFutures.Companion` |

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/CountTokensResponse>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/GenerativeModelFutures#countTokens(kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content prompt)` Counts the number of tokens in a prompt using the model's tokenizer. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/GenerativeModelFutures` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/GenerativeModelFutures.Companion#from(com.google.firebase.vertexai.GenerativeModel)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/GenerativeModel model)` |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/GenerativeModelFutures#generateContent(kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content prompt)` Generates new content from the input `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` given to the model as a prompt. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/org/reactivestreams/Publisher<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/GenerativeModelFutures#generateContentStream(kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content prompt)` Generates new content as a stream from the input `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` given to the model as a prompt. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/GenerativeModel` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/GenerativeModelFutures#getGenerativeModel()()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/GenerativeModel` object wrapped by this object. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ChatFutures` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/GenerativeModelFutures#startChat()()` Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ChatFutures` instance which internally tracks the ongoing conversation with the model. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ChatFutures` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/GenerativeModelFutures#startChat(kotlin.collections.List)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content> history)` Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ChatFutures` instance, initialized using the optionally provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/GenerativeModelFutures#startChat(kotlin.collections.List)`. |

## Public methods

### countTokens

```
public abstract @NonNull ListenableFuture<@NonNull CountTokensResponse> countTokens(@NonNull Content prompt)
```

Counts the number of tokens in a prompt using the model's tokenizer.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content prompt` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/CountTokensResponse>` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/CountTokensResponse` of running the model's tokenizer on the input. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException com.google.firebase.vertexai.type.FirebaseVertexAIException` | if the request failed. |

### from

```
public static final @NonNull GenerativeModelFutures from(@NonNull GenerativeModel model)
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/GenerativeModelFutures` | a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/GenerativeModelFutures` created around the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/GenerativeModel` |

### generateContent

```
public abstract @NonNull ListenableFuture<@NonNull GenerateContentResponse> generateContent(@NonNull Content prompt)
```

Generates new content from the input `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` given to the model as a prompt.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content prompt` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerateContentResponse>` | The content generated by the model. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException com.google.firebase.vertexai.type.FirebaseVertexAIException` | if the request failed. |

### generateContentStream

```
public abstract @NonNull Publisher<@NonNull GenerateContentResponse> generateContentStream(@NonNull Content prompt)
```

Generates new content as a stream from the input `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` given to the model as a prompt.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content prompt` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/org/reactivestreams/Publisher<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerateContentResponse>` | A `https://firebase.google.com/docs/reference/android/org/reactivestreams/Publisher` which will emit responses as they are returned by the model. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException com.google.firebase.vertexai.type.FirebaseVertexAIException` | if the request failed. |

### getGenerativeModel

```
public abstract @NonNull GenerativeModel getGenerativeModel()
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/GenerativeModel` object wrapped by this object.

### startChat

```
public abstract @NonNull ChatFutures startChat()
```

Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ChatFutures` instance which internally tracks the ongoing conversation with the model.

### startChat

```
public abstract @NonNull ChatFutures startChat(@NonNull List<@NonNull Content> history)
```

Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/ChatFutures` instance, initialized using the optionally provided `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/java/GenerativeModelFutures#startChat(kotlin.collections.List)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content> history` | A list of previous interactions with the model to use as a starting point |