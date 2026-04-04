# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/GenerativeModelFutures.md.txt

# GenerativeModelFutures

# GenerativeModelFutures


```
abstract class GenerativeModelFutures
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Wrapper class providing Java compatible methods for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel` |   |

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/GenerativeModelFutures` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/GenerativeModelFutures.Companion#from(com.google.firebase.vertexai.GenerativeModel)(model: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel)` |

| ### Public functions |
|---|---|
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/GenerativeModelFutures#countTokens(kotlin.Array)(vararg prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content)` Counts the number of tokens in a prompt using the model's tokenizer. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/GenerativeModelFutures#generateContent(kotlin.Array)(vararg prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content)` Generates new content from the input `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` given to the model as a prompt. |
| `abstract https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/GenerativeModelFutures#generateContentStream(kotlin.Array)(vararg prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content)` Generates new content as a stream from the input `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` given to the model as a prompt. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/GenerativeModelFutures#getGenerativeModel()()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel` object wrapped by this object. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ChatFutures` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/GenerativeModelFutures#startChat()()` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ChatFutures` instance which internally tracks the ongoing conversation with the model. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ChatFutures` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/GenerativeModelFutures#startChat(kotlin.collections.List)(history: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content>)` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ChatFutures` instance, initialized using the optionally provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/GenerativeModelFutures#startChat(kotlin.collections.List)`. |

## Public companion functions

### from

```
fun from(model: GenerativeModel): GenerativeModelFutures
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/GenerativeModelFutures` | a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/GenerativeModelFutures` created around the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel` |

## Public functions

### countTokens

```
abstract fun countTokens(vararg prompt: Content): ListenableFuture<CountTokensResponse>
```

Counts the number of tokens in a prompt using the model's tokenizer.

| Parameters |
|---|---|
| `vararg prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse>` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse` of running the model's tokenizer on the input. |

| Throws |
|---|---|
| `com.google.firebase.vertexai.type.FirebaseVertexAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FirebaseVertexAIException` | if the request failed. |

### generateContent

```
abstract fun generateContent(vararg prompt: Content): ListenableFuture<GenerateContentResponse>
```

Generates new content from the input `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` given to the model as a prompt.

| Parameters |
|---|---|
| `vararg prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/common/util/concurrent/ListenableFuture<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse>` | The content generated by the model. |

| Throws |
|---|---|
| `com.google.firebase.vertexai.type.FirebaseVertexAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FirebaseVertexAIException` | if the request failed. |

### generateContentStream

```
abstract fun generateContentStream(vararg prompt: Content): Publisher<GenerateContentResponse>
```

Generates new content as a stream from the input `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` given to the model as a prompt.

| Parameters |
|---|---|
| `vararg prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse>` | A `https://firebase.google.com/docs/reference/kotlin/org/reactivestreams/Publisher` which will emit responses as they are returned by the model. |

| Throws |
|---|---|
| `com.google.firebase.vertexai.type.FirebaseVertexAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FirebaseVertexAIException` | if the request failed. |

### getGenerativeModel

```
abstract fun getGenerativeModel(): GenerativeModel
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel` object wrapped by this object.

### startChat

```
abstract fun startChat(): ChatFutures
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ChatFutures` instance which internally tracks the ongoing conversation with the model.

### startChat

```
abstract fun startChat(history: List<Content>): ChatFutures
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/ChatFutures` instance, initialized using the optionally provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/java/GenerativeModelFutures#startChat(kotlin.collections.List)`.

| Parameters |
|---|---|
| `history: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content>` | A list of previous interactions with the model to use as a starting point |