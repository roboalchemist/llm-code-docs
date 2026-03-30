# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel.md.txt

# GenerativeModel

# GenerativeModel


```
public final class GenerativeModel
```

<br />

*** ** * ** ***

Represents a multimodal model (like Gemini), capable of generating content based on various input types.

## Summary

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CountTokensResponse` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel#countTokens(android.graphics.Bitmap)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html prompt)` Counts the number of tokens in an image prompt using the model's tokenizer. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CountTokensResponse` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel#countTokens(kotlin.collections.List)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content> prompt)` Counts the number of tokens in a prompt using the model's tokenizer. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CountTokensResponse` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel#countTokens(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt)` Counts the number of tokens in a text prompt using the model's tokenizer. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CountTokensResponse` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel#countTokens(com.google.firebase.ai.type.Content,kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompt, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompts)` Counts the number of tokens in a prompt using the model's tokenizer. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel#generateContent(android.graphics.Bitmap)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html prompt)` Generates new content from the image input given to the model as a prompt. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel#generateContent(kotlin.collections.List)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content> prompt)` Generates new content from the input `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` given to the model as a prompt. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel#generateContent(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt)` Generates new content from the text input given to the model as a prompt. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel#generateContent(com.google.firebase.ai.type.Content,kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompt, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompts)` Generates new content from the input `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` given to the model as a prompt. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel#generateContentStream(android.graphics.Bitmap)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html prompt)` Generates new content as a stream from the image input given to the model as a prompt. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel#generateContentStream(kotlin.collections.List)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content> prompt)` Generates new content as a stream from the input `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` given to the model as a prompt. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel#generateContentStream(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt)` Generates new content as a stream from the text input given to the model as a prompt. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel#generateContentStream(com.google.firebase.ai.type.Content,kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompt, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompts)` Generates new content as a stream from the input `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` given to the model as a prompt. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateObjectResponse<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T>` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel#generateObject(com.google.firebase.ai.type.JsonSchema,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> jsonSchema, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt )` Generates an object from the text input given to the model as a prompt. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateObjectResponse<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T>` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel#generateObject(com.google.firebase.ai.type.JsonSchema,com.google.firebase.ai.type.Content,kotlin.Array)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> jsonSchema, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompt, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompts )` Generates an object from the input `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` given to the model as a prompt. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/Chat` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel#startChat(kotlin.collections.List)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content> history)` Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/Chat` instance using this model with the optionally provided history. |
| `final void` | `@https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PublicPreviewAPI https://firebase.google.com/docs/reference/android/com/google/firebase/ai/GenerativeModel#warmUp()()` Warms up the model to reduce latency for the first request. |

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
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CountTokensResponse` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CountTokensResponse` of running the model's tokenizer on the input. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException com.google.firebase.ai.type.FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

### countTokens

```
public final @NonNull CountTokensResponse countTokens(@NonNull List<@NonNull Content> prompt)
```

Counts the number of tokens in a prompt using the model's tokenizer.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content> prompt` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CountTokensResponse` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CountTokensResponse` of running the model's tokenizer on the input. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException com.google.firebase.ai.type.FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

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
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CountTokensResponse` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CountTokensResponse` of running the model's tokenizer on the input. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException com.google.firebase.ai.type.FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

### countTokens

```
public final @NonNull CountTokensResponse countTokens(@NonNull Content prompt, @NonNull Content prompts)
```

Counts the number of tokens in a prompt using the model's tokenizer.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompt` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CountTokensResponse` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CountTokensResponse` of running the model's tokenizer on the input. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException com.google.firebase.ai.type.FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

### generateContent

```
public final @NonNull GenerateContentResponse generateContent(@NonNull Bitmap prompt)
```

Generates new content from the image input given to the model as a prompt.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html prompt` | The image to be converted into a single piece of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` to send to the model. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse` after some delay. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException com.google.firebase.ai.type.FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

### generateContent

```
public final @NonNull GenerateContentResponse generateContent(@NonNull List<@NonNull Content> prompt)
```

Generates new content from the input `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` given to the model as a prompt.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content> prompt` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse` | The content generated by the model. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException com.google.firebase.ai.type.FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

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
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse` | The content generated by the model. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException com.google.firebase.ai.type.FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

### generateContent

```
public final @NonNull GenerateContentResponse generateContent(@NonNull Content prompt, @NonNull Content prompts)
```

Generates new content from the input `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` given to the model as a prompt.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompt` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse` | The content generated by the model. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException com.google.firebase.ai.type.FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

### generateContentStream

```
public final @NonNull Flow<@NonNull GenerateContentResponse> generateContentStream(@NonNull Bitmap prompt)
```

Generates new content as a stream from the image input given to the model as a prompt.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html prompt` | The image to be converted into a single piece of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` to send to the model. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse>` | A `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html` which will emit responses as they are returned by the model. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException com.google.firebase.ai.type.FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

### generateContentStream

```
public final @NonNull Flow<@NonNull GenerateContentResponse> generateContentStream(@NonNull List<@NonNull Content> prompt)
```

Generates new content as a stream from the input `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` given to the model as a prompt.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content> prompt` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse>` | A `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html` which will emit responses as they are returned by the model. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException com.google.firebase.ai.type.FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

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
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse>` | A `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html` which will emit responses as they are returned by the model. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException com.google.firebase.ai.type.FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

### generateContentStream

```
public final @NonNull Flow<@NonNull GenerateContentResponse> generateContentStream(@NonNull Content prompt, @NonNull Content prompts)
```

Generates new content as a stream from the input `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` given to the model as a prompt.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompt` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateContentResponse>` | A `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html` which will emit responses as they are returned by the model. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException com.google.firebase.ai.type.FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

### generateObject

```
public final @NonNull GenerateObjectResponse<@NonNull T> <T extends Object> generateObject(
    @NonNull JsonSchema<@NonNull T> jsonSchema,
    @NonNull String prompt
)
```

Generates an object from the text input given to the model as a prompt.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> jsonSchema` | A schema for the output |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prompt` | The text to be send to the model as a prompt. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateObjectResponse<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T>` | The content generated by the model. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException com.google.firebase.ai.type.FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

### generateObject

```
public final @NonNull GenerateObjectResponse<@NonNull T> <T extends Object> generateObject(
    @NonNull JsonSchema<@NonNull T> jsonSchema,
    @NonNull Content prompt,
    @NonNull Content prompts
)
```

Generates an object from the input `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` given to the model as a prompt.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> jsonSchema` | A schema for the output |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content prompt` | The input(s) given to the model as a prompt. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerateObjectResponse<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T>` | The content generated by the model. |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException com.google.firebase.ai.type.FirebaseAIException` | if the request failed. |

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException` | for types of errors. |

### startChat

```
public final @NonNull Chat startChat(@NonNull List<@NonNull Content> history)
```

Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/Chat` instance using this model with the optionally provided history.

### warmUp

```
@PublicPreviewAPI
public final void warmUp()
```

Warms up the model to reduce latency for the first request.

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FirebaseAIException com.google.firebase.ai.type.FirebaseAIException` | if the warmup failed. |