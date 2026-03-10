# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/GenerativeModel.md.txt

# GenerativeModel

# GenerativeModel


```
public final class GenerativeModel
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Represents a multimodal model (like Gemini), capable of generating content based on various input types.

## Summary

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/CountTokensResponse` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/GenerativeModel#countTokens(android.graphics.Bitmap)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html prompt)` Counts the number of tokens in an image prompt using the model's tokenizer. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/CountTokensResponse` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/GenerativeModel#countTokens(kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content prompt)` Counts the number of tokens in a prompt using the model's tokenizer. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/CountTokensResponse` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/GenerativeModel#countTokens(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt)` Counts the number of tokens in a text prompt using the model's tokenizer. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerateContentResponse` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/GenerativeModel#generateContent(android.graphics.Bitmap)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html prompt)` Generates new content from the image input given to the model as a prompt. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerateContentResponse` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/GenerativeModel#generateContent(kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content prompt)` Generates new content from the input `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` given to the model as a prompt. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerateContentResponse` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/GenerativeModel#generateContent(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt)` Generates new content from the text input given to the model as a prompt. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/GenerativeModel#generateContentStream(android.graphics.Bitmap)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html prompt)` Generates new content as a stream from the image input given to the model as a prompt. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/GenerativeModel#generateContentStream(kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content prompt)` Generates new content as a stream from the input `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` given to the model as a prompt. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/GenerativeModel#generateContentStream(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt)` Generates new content as a stream from the text input given to the model as a prompt. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/Chat` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/GenerativeModel#startChat(kotlin.collections.List)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content> history)` Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/Chat` instance using this model with the optionally provided history. |

## Public methods

### countTokens

```
public final @NonNull CountTokensResponse countTokens(@NonNull Bitmap prompt)
```

Counts the number of tokens in an image prompt using the model's tokenizer.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html prompt` | The image given to the model as a prompt. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/CountTokensResponse` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/CountTokensResponse` of running the model's tokenizer on the input. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException com.google.firebase.vertexai.type.FirebaseVertexAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException` | for types of errors. |

### countTokens

```
public final @NonNull CountTokensResponse countTokens(@NonNull Content prompt)
```

Counts the number of tokens in a prompt using the model's tokenizer.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content prompt` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/CountTokensResponse` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/CountTokensResponse` of running the model's tokenizer on the input. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException com.google.firebase.vertexai.type.FirebaseVertexAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException` | for types of errors. |

### countTokens

```
public final @NonNull CountTokensResponse countTokens(@NonNull String prompt)
```

Counts the number of tokens in a text prompt using the model's tokenizer.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt` | The text given to the model as a prompt. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/CountTokensResponse` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/CountTokensResponse` of running the model's tokenizer on the input. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException com.google.firebase.vertexai.type.FirebaseVertexAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException` | for types of errors. |

### generateContent

```
public final @NonNull GenerateContentResponse generateContent(@NonNull Bitmap prompt)
```

Generates new content from the image input given to the model as a prompt.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html prompt` | The image to be converted into a single piece of `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` to send to the model. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerateContentResponse` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerateContentResponse` after some delay. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException com.google.firebase.vertexai.type.FirebaseVertexAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException` | for types of errors. |

### generateContent

```
public final @NonNull GenerateContentResponse generateContent(@NonNull Content prompt)
```

Generates new content from the input `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` given to the model as a prompt.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content prompt` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerateContentResponse` | The content generated by the model. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException com.google.firebase.vertexai.type.FirebaseVertexAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException` | for types of errors. |

### generateContent

```
public final @NonNull GenerateContentResponse generateContent(@NonNull String prompt)
```

Generates new content from the text input given to the model as a prompt.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt` | The text to be send to the model as a prompt. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerateContentResponse` | The content generated by the model. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException com.google.firebase.vertexai.type.FirebaseVertexAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException` | for types of errors. |

### generateContentStream

```
public final @NonNull Flow<@NonNull GenerateContentResponse> generateContentStream(@NonNull Bitmap prompt)
```

Generates new content as a stream from the image input given to the model as a prompt.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html prompt` | The image to be converted into a single piece of `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` to send to the model. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerateContentResponse>` | A `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html` which will emit responses as they are returned by the model. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException com.google.firebase.vertexai.type.FirebaseVertexAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException` | for types of errors. |

### generateContentStream

```
public final @NonNull Flow<@NonNull GenerateContentResponse> generateContentStream(@NonNull Content prompt)
```

Generates new content as a stream from the input `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content` given to the model as a prompt.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Content prompt` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerateContentResponse>` | A `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html` which will emit responses as they are returned by the model. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException com.google.firebase.vertexai.type.FirebaseVertexAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException` | for types of errors. |

### generateContentStream

```
public final @NonNull Flow<@NonNull GenerateContentResponse> generateContentStream(@NonNull String prompt)
```

Generates new content as a stream from the text input given to the model as a prompt.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt` | The text to be send to the model as a prompt. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerateContentResponse>` | A `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html` which will emit responses as they are returned by the model. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException com.google.firebase.vertexai.type.FirebaseVertexAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FirebaseVertexAIException` | for types of errors. |

### startChat

```
public final @NonNull Chat startChat(@NonNull List<@NonNull Content> history)
```

Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/Chat` instance using this model with the optionally provided history.