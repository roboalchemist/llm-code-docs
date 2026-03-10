# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel.md.txt

# GenerativeModel

# GenerativeModel


```
class GenerativeModel
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents a multimodal model (like Gemini), capable of generating content based on various input types.

## Summary

| ### Public functions |
|---|---|
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel#countTokens(android.graphics.Bitmap)(prompt: https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html)` Counts the number of tokens in an image prompt using the model's tokenizer. |
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel#countTokens(kotlin.Array)(vararg prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content)` Counts the number of tokens in a prompt using the model's tokenizer. |
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel#countTokens(kotlin.String)(prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Counts the number of tokens in a text prompt using the model's tokenizer. |
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel#generateContent(android.graphics.Bitmap)(prompt: https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html)` Generates new content from the image input given to the model as a prompt. |
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel#generateContent(kotlin.Array)(vararg prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content)` Generates new content from the input `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` given to the model as a prompt. |
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel#generateContent(kotlin.String)(prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Generates new content from the text input given to the model as a prompt. |
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel#generateContentStream(android.graphics.Bitmap)(prompt: https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html)` Generates new content as a stream from the image input given to the model as a prompt. |
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel#generateContentStream(kotlin.Array)(vararg prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content)` Generates new content as a stream from the input `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` given to the model as a prompt. |
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel#generateContentStream(kotlin.String)(prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Generates new content as a stream from the text input given to the model as a prompt. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/GenerativeModel#startChat(kotlin.collections.List)(history: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content>)` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat` instance using this model with the optionally provided history. |

## Public functions

### countTokens

```
suspend fun countTokens(prompt: Bitmap): CountTokensResponse
```

Counts the number of tokens in an image prompt using the model's tokenizer.

| Parameters |
|---|---|
| `prompt: https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` | The image given to the model as a prompt. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse` of running the model's tokenizer on the input. |

| Throws |
|---|---|
| `com.google.firebase.vertexai.type.FirebaseVertexAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FirebaseVertexAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FirebaseVertexAIException` | for types of errors. |

### countTokens

```
suspend fun countTokens(vararg prompt: Content): CountTokensResponse
```

Counts the number of tokens in a prompt using the model's tokenizer.

| Parameters |
|---|---|
| `vararg prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse` of running the model's tokenizer on the input. |

| Throws |
|---|---|
| `com.google.firebase.vertexai.type.FirebaseVertexAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FirebaseVertexAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FirebaseVertexAIException` | for types of errors. |

### countTokens

```
suspend fun countTokens(prompt: String): CountTokensResponse
```

Counts the number of tokens in a text prompt using the model's tokenizer.

| Parameters |
|---|---|
| `prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The text given to the model as a prompt. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/CountTokensResponse` of running the model's tokenizer on the input. |

| Throws |
|---|---|
| `com.google.firebase.vertexai.type.FirebaseVertexAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FirebaseVertexAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FirebaseVertexAIException` | for types of errors. |

### generateContent

```
suspend fun generateContent(prompt: Bitmap): GenerateContentResponse
```

Generates new content from the image input given to the model as a prompt.

| Parameters |
|---|---|
| `prompt: https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` | The image to be converted into a single piece of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` to send to the model. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse` after some delay. |

| Throws |
|---|---|
| `com.google.firebase.vertexai.type.FirebaseVertexAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FirebaseVertexAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FirebaseVertexAIException` | for types of errors. |

### generateContent

```
suspend fun generateContent(vararg prompt: Content): GenerateContentResponse
```

Generates new content from the input `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` given to the model as a prompt.

| Parameters |
|---|---|
| `vararg prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse` | The content generated by the model. |

| Throws |
|---|---|
| `com.google.firebase.vertexai.type.FirebaseVertexAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FirebaseVertexAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FirebaseVertexAIException` | for types of errors. |

### generateContent

```
suspend fun generateContent(prompt: String): GenerateContentResponse
```

Generates new content from the text input given to the model as a prompt.

| Parameters |
|---|---|
| `prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The text to be send to the model as a prompt. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse` | The content generated by the model. |

| Throws |
|---|---|
| `com.google.firebase.vertexai.type.FirebaseVertexAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FirebaseVertexAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FirebaseVertexAIException` | for types of errors. |

### generateContentStream

```
fun generateContentStream(prompt: Bitmap): Flow<GenerateContentResponse>
```

Generates new content as a stream from the image input given to the model as a prompt.

| Parameters |
|---|---|
| `prompt: https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` | The image to be converted into a single piece of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` to send to the model. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse>` | A `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html` which will emit responses as they are returned by the model. |

| Throws |
|---|---|
| `com.google.firebase.vertexai.type.FirebaseVertexAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FirebaseVertexAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FirebaseVertexAIException` | for types of errors. |

### generateContentStream

```
fun generateContentStream(vararg prompt: Content): Flow<GenerateContentResponse>
```

Generates new content as a stream from the input `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` given to the model as a prompt.

| Parameters |
|---|---|
| `vararg prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Content` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse>` | A `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html` which will emit responses as they are returned by the model. |

| Throws |
|---|---|
| `com.google.firebase.vertexai.type.FirebaseVertexAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FirebaseVertexAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FirebaseVertexAIException` | for types of errors. |

### generateContentStream

```
fun generateContentStream(prompt: String): Flow<GenerateContentResponse>
```

Generates new content as a stream from the text input given to the model as a prompt.

| Parameters |
|---|---|
| `prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The text to be send to the model as a prompt. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerateContentResponse>` | A `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html` which will emit responses as they are returned by the model. |

| Throws |
|---|---|
| `com.google.firebase.vertexai.type.FirebaseVertexAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FirebaseVertexAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FirebaseVertexAIException` | for types of errors. |

### startChat

```
fun startChat(history: List<Content> = emptyList()): Chat
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/Chat` instance using this model with the optionally provided history.