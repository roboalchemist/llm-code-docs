# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/GenerativeModelFutures.md.txt

# GenerativeModelFutures

# GenerativeModelFutures


```
public abstract class GenerativeModelFutures
```

<br />

*** ** * ** ***

Wrapper class providing Java compatible methods for `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel` |   |

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/GenerativeModelFutures.Companion` |

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CountTokensResponse>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/GenerativeModelFutures#countTokens(com.google.firebase.ai.type.Content,kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompt, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompts)` Counts the number of tokens in a prompt using the model's tokenizer. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/GenerativeModelFutures` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/GenerativeModelFutures.Companion#from(com.google.firebase.ai.GenerativeModel)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel model)` |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/GenerativeModelFutures#generateContent(com.google.firebase.ai.type.Content,kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompt, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompts)` Generates new content from the input `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` given to the model as a prompt. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/org/reactivestreams/Publisher<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/GenerativeModelFutures#generateContentStream(com.google.firebase.ai.type.Content,kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompt, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompts)` Generates new content as a stream from the input `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` given to the model as a prompt. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/GenerativeModelFutures#getGenerativeModel()()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel` object wrapped by this object. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/GenerativeModelFutures#startChat()()` Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures` instance which internally tracks the ongoing conversation with the model. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/GenerativeModelFutures#startChat(kotlin.collections.List)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content> history)` Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures` instance, initialized using the optionally provided `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/GenerativeModelFutures#startChat(kotlin.collections.List)`. |

## Public methods

### countTokens

```
public abstract @NonNull ListenableFuture<@NonNull CountTokensResponse> countTokens(@NonNull Content prompt, @NonNull Content prompts)
```

Counts the number of tokens in a prompt using the model's tokenizer.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompt` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CountTokensResponse>` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CountTokensResponse` of running the model's tokenizer on the input. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException com.google.firebase.ai.type.FirebaseAIException` | if the request failed. |

### from

```
public static final @NonNull GenerativeModelFutures from(@NonNull GenerativeModel model)
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/GenerativeModelFutures` | a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/GenerativeModelFutures` created around the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel` |

### generateContent

```
public abstract @NonNull ListenableFuture<@NonNull GenerateContentResponse> generateContent(@NonNull Content prompt, @NonNull Content prompts)
```

Generates new content from the input `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` given to the model as a prompt.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompt` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/common/util/concurrent/ListenableFuture<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse>` | The content generated by the model. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException com.google.firebase.ai.type.FirebaseAIException` | if the request failed. |

### generateContentStream

```
public abstract @NonNull Publisher<@NonNull GenerateContentResponse> generateContentStream(@NonNull Content prompt, @NonNull Content prompts)
```

Generates new content as a stream from the input `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` given to the model as a prompt.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompt` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/org/reactivestreams/Publisher<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse>` | A `https://firebase.google.com/docs/reference/android/org/reactivestreams/Publisher` which will emit responses as they are returned by the model. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException com.google.firebase.ai.type.FirebaseAIException` | if the request failed. |

### getGenerativeModel

```
public abstract @NonNull GenerativeModel getGenerativeModel()
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel` object wrapped by this object.

### startChat

```
public abstract @NonNull ChatFutures startChat()
```

Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures` instance which internally tracks the ongoing conversation with the model.

### startChat

```
public abstract @NonNull ChatFutures startChat(@NonNull List<@NonNull Content> history)
```

Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/ChatFutures` instance, initialized using the optionally provided `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/java/GenerativeModelFutures#startChat(kotlin.collections.List)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content> history` | A list of previous interactions with the model to use as a starting point |