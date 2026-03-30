# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures.md.txt

# GenerativeModelFutures

# GenerativeModelFutures


```
abstract class GenerativeModelFutures
```

<br />

*** ** * ** ***

Wrapper class providing Java compatible methods for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel` |   |

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures.Companion#from(com.google.firebase.ai.GenerativeModel)(model: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel)` |

| ### Public functions |
|---|---|
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures#countTokens(com.google.firebase.ai.type.Content,kotlin.Array)(prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content, vararg prompts: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content)` Counts the number of tokens in a prompt using the model's tokenizer. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures#generateContent(com.google.firebase.ai.type.Content,kotlin.Array)(prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content, vararg prompts: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content)` Generates new content from the input `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` given to the model as a prompt. |
| `abstract https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures#generateContentStream(com.google.firebase.ai.type.Content,kotlin.Array)(prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content, vararg prompts: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content)` Generates new content as a stream from the input `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` given to the model as a prompt. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures#getGenerativeModel()()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel` object wrapped by this object. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ChatFutures` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures#startChat()()` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ChatFutures` instance which internally tracks the ongoing conversation with the model. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ChatFutures` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures#startChat(kotlin.collections.List)(history: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content>)` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ChatFutures` instance, initialized using the optionally provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures#startChat(kotlin.collections.List)`. |

## Public companion functions

### from

```
fun from(model: GenerativeModel): GenerativeModelFutures
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures` | a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures` created around the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel` |

## Public functions

### countTokens

```
abstract fun countTokens(prompt: Content, vararg prompts: Content): ListenableFuture<CountTokensResponse>
```

Counts the number of tokens in a prompt using the model's tokenizer.

| Parameters |
|---|---|
| `prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse>` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse` of running the model's tokenizer on the input. |

| Throws |
|---|---|
| `com.google.firebase.ai.type.FirebaseAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | if the request failed. |

### generateContent

```
abstract fun generateContent(prompt: Content, vararg prompts: Content): ListenableFuture<GenerateContentResponse>
```

Generates new content from the input `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` given to the model as a prompt.

| Parameters |
|---|---|
| `prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse>` | The content generated by the model. |

| Throws |
|---|---|
| `com.google.firebase.ai.type.FirebaseAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | if the request failed. |

### generateContentStream

```
abstract fun generateContentStream(prompt: Content, vararg prompts: Content): Publisher<GenerateContentResponse>
```

Generates new content as a stream from the input `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` given to the model as a prompt.

| Parameters |
|---|---|
| `prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse>` | A `https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher` which will emit responses as they are returned by the model. |

| Throws |
|---|---|
| `com.google.firebase.ai.type.FirebaseAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | if the request failed. |

### getGenerativeModel

```
abstract fun getGenerativeModel(): GenerativeModel
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel` object wrapped by this object.

### startChat

```
abstract fun startChat(): ChatFutures
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ChatFutures` instance which internally tracks the ongoing conversation with the model.

### startChat

```
abstract fun startChat(history: List<Content>): ChatFutures
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/ChatFutures` instance, initialized using the optionally provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/java/GenerativeModelFutures#startChat(kotlin.collections.List)`.

| Parameters |
|---|---|
| `history: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content>` | A list of previous interactions with the model to use as a starting point |