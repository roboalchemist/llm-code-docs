# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel.md.txt

# GenerativeModel

# GenerativeModel


```
class GenerativeModel
```

<br />

*** ** * ** ***

Represents a multimodal model (like Gemini), capable of generating content based on various input types.

## Summary

| ### Public functions |
|---|---|
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#countTokens(android.graphics.Bitmap)(prompt: https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html)` Counts the number of tokens in an image prompt using the model's tokenizer. |
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#countTokens(kotlin.collections.List)(prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content>)` Counts the number of tokens in a prompt using the model's tokenizer. |
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#countTokens(kotlin.String)(prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Counts the number of tokens in a text prompt using the model's tokenizer. |
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#countTokens(com.google.firebase.ai.type.Content,kotlin.Array)(prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content, vararg prompts: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content)` Counts the number of tokens in a prompt using the model's tokenizer. |
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#generateContent(android.graphics.Bitmap)(prompt: https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html)` Generates new content from the image input given to the model as a prompt. |
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#generateContent(kotlin.collections.List)(prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content>)` Generates new content from the input `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` given to the model as a prompt. |
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#generateContent(kotlin.String)(prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Generates new content from the text input given to the model as a prompt. |
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#generateContent(com.google.firebase.ai.type.Content,kotlin.Array)(prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content, vararg prompts: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content)` Generates new content from the input `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` given to the model as a prompt. |
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#generateContentStream(android.graphics.Bitmap)(prompt: https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html)` Generates new content as a stream from the image input given to the model as a prompt. |
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#generateContentStream(kotlin.collections.List)(prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content>)` Generates new content as a stream from the input `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` given to the model as a prompt. |
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#generateContentStream(kotlin.String)(prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Generates new content as a stream from the text input given to the model as a prompt. |
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#generateContentStream(com.google.firebase.ai.type.Content,kotlin.Array)(prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content, vararg prompts: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content)` Generates new content as a stream from the input `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` given to the model as a prompt. |
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateObjectResponse<T>` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#generateObject(com.google.firebase.ai.type.JsonSchema,kotlin.String)(jsonSchema: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<T>, prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Generates an object from the text input given to the model as a prompt. |
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateObjectResponse<T>` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#generateObject(com.google.firebase.ai.type.JsonSchema,com.google.firebase.ai.type.Content,kotlin.Array)( jsonSchema: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<T>, prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content, vararg prompts: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content )` Generates an object from the input `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` given to the model as a prompt. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/Chat` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#startChat(kotlin.collections.List)(history: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content>)` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/Chat` instance using this model with the optionally provided history. |
| `suspend https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/PublicPreviewAPI https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/GenerativeModel#warmUp()()` Warms up the model to reduce latency for the first request. |

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
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse` of running the model's tokenizer on the input. |

| Throws |
|---|---|
| `com.google.firebase.ai.type.FirebaseAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

### countTokens

```
suspend fun countTokens(prompt: List<Content>): CountTokensResponse
```

Counts the number of tokens in a prompt using the model's tokenizer.

| Parameters |
|---|---|
| `prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content>` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse` of running the model's tokenizer on the input. |

| Throws |
|---|---|
| `com.google.firebase.ai.type.FirebaseAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

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
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse` of running the model's tokenizer on the input. |

| Throws |
|---|---|
| `com.google.firebase.ai.type.FirebaseAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

### countTokens

```
suspend fun countTokens(prompt: Content, vararg prompts: Content): CountTokensResponse
```

Counts the number of tokens in a prompt using the model's tokenizer.

| Parameters |
|---|---|
| `prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CountTokensResponse` of running the model's tokenizer on the input. |

| Throws |
|---|---|
| `com.google.firebase.ai.type.FirebaseAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

### generateContent

```
suspend fun generateContent(prompt: Bitmap): GenerateContentResponse
```

Generates new content from the image input given to the model as a prompt.

| Parameters |
|---|---|
| `prompt: https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` | The image to be converted into a single piece of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` to send to the model. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse` after some delay. |

| Throws |
|---|---|
| `com.google.firebase.ai.type.FirebaseAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

### generateContent

```
suspend fun generateContent(prompt: List<Content>): GenerateContentResponse
```

Generates new content from the input `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` given to the model as a prompt.

| Parameters |
|---|---|
| `prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content>` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse` | The content generated by the model. |

| Throws |
|---|---|
| `com.google.firebase.ai.type.FirebaseAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

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
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse` | The content generated by the model. |

| Throws |
|---|---|
| `com.google.firebase.ai.type.FirebaseAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

### generateContent

```
suspend fun generateContent(prompt: Content, vararg prompts: Content): GenerateContentResponse
```

Generates new content from the input `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` given to the model as a prompt.

| Parameters |
|---|---|
| `prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse` | The content generated by the model. |

| Throws |
|---|---|
| `com.google.firebase.ai.type.FirebaseAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

### generateContentStream

```
fun generateContentStream(prompt: Bitmap): Flow<GenerateContentResponse>
```

Generates new content as a stream from the image input given to the model as a prompt.

| Parameters |
|---|---|
| `prompt: https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` | The image to be converted into a single piece of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` to send to the model. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse>` | A `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html` which will emit responses as they are returned by the model. |

| Throws |
|---|---|
| `com.google.firebase.ai.type.FirebaseAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

### generateContentStream

```
fun generateContentStream(prompt: List<Content>): Flow<GenerateContentResponse>
```

Generates new content as a stream from the input `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` given to the model as a prompt.

| Parameters |
|---|---|
| `prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content>` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse>` | A `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html` which will emit responses as they are returned by the model. |

| Throws |
|---|---|
| `com.google.firebase.ai.type.FirebaseAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

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
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse>` | A `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html` which will emit responses as they are returned by the model. |

| Throws |
|---|---|
| `com.google.firebase.ai.type.FirebaseAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

### generateContentStream

```
fun generateContentStream(prompt: Content, vararg prompts: Content): Flow<GenerateContentResponse>
```

Generates new content as a stream from the input `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` given to the model as a prompt.

| Parameters |
|---|---|
| `prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateContentResponse>` | A `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html` which will emit responses as they are returned by the model. |

| Throws |
|---|---|
| `com.google.firebase.ai.type.FirebaseAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

### generateObject

```
suspend fun <T : Any> generateObject(jsonSchema: JsonSchema<T>, prompt: String): GenerateObjectResponse<T>
```

Generates an object from the text input given to the model as a prompt.

| Parameters |
|---|---|
| `jsonSchema: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<T>` | A schema for the output |
| `prompt: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The text to be send to the model as a prompt. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateObjectResponse<T>` | The content generated by the model. |

| Throws |
|---|---|
| `com.google.firebase.ai.type.FirebaseAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

### generateObject

```
suspend fun <T : Any> generateObject(
    jsonSchema: JsonSchema<T>,
    prompt: Content,
    vararg prompts: Content
): GenerateObjectResponse<T>
```

Generates an object from the input `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` given to the model as a prompt.

| Parameters |
|---|---|
| `jsonSchema: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<T>` | A schema for the output |
| `prompt: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerateObjectResponse<T>` | The content generated by the model. |

| Throws |
|---|---|
| `com.google.firebase.ai.type.FirebaseAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

### startChat

```
fun startChat(history: List<Content> = emptyList()): Chat
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/Chat` instance using this model with the optionally provided history.

### warmUp

```
@PublicPreviewAPI
suspend fun warmUp(): Unit
```

Warms up the model to reduce latency for the first request.

| Throws |
|---|---|
| `com.google.firebase.ai.type.FirebaseAIException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/FirebaseAIException` | if the warmup failed. |