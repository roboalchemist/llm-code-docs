# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder.md.txt

# GenerationConfig.Builder

# GenerationConfig.Builder


```
public final class GenerationConfig.Builder
```

<br />

*** ** * ** ***

Builder for creating a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig`.

Mainly intended for Java interop. Kotlin consumers should use `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/package-summary#generationConfig(kotlin.Function1)` for a more idiomatic experience.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/package-summary#generationConfig(kotlin.Function1)` |   |

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#candidateCount()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig#candidateCount()`. |
| `final https://developer.android.com/reference/kotlin/java/lang/Float.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#frequencyPenalty()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig#frequencyPenalty()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#maxOutputTokens()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig#maxOutputTokens()`. |
| `final https://developer.android.com/reference/kotlin/java/lang/Float.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#presencePenalty()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig#presencePenalty()` |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html ?>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#responseJsonSchema()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig#responseJsonSchema()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#responseMimeType()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig#responseMimeType()`. |
| `final https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ResponseModality>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#responseModalities()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig#responseModalities()`. |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#responseSchema()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig#responseSchema()`. |
| `final https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#stopSequences()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig#stopSequences()`. |
| `final https://developer.android.com/reference/kotlin/java/lang/Float.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#temperature()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig#temperature()`. |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#thinkingConfig()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#topK()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig#topK()`. |
| `final https://developer.android.com/reference/kotlin/java/lang/Float.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#topP()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig#topP()`. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#Builder()()` |

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#build()()` Create a new `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig` with the attached arguments. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#setCandidateCount(kotlin.Int)(https://developer.android.com/reference/kotlin/java/lang/Integer.html candidateCount)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#setFrequencyPenalty(kotlin.Float)(https://developer.android.com/reference/kotlin/java/lang/Float.html frequencyPenalty)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#setMaxOutputTokens(kotlin.Int)(https://developer.android.com/reference/kotlin/java/lang/Integer.html maxOutputTokens)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#setPresencePenalty(kotlin.Float)(https://developer.android.com/reference/kotlin/java/lang/Float.html presencePenalty)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#setResponseMimeType(kotlin.String)(https://developer.android.com/reference/kotlin/java/lang/String.html responseMimeType)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#setResponseModalities(kotlin.collections.List)( https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ResponseModality> responseModalities )` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#setResponseSchema(com.google.firebase.ai.type.Schema)(https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema responseSchema)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#setResponseSchemaJson(com.google.firebase.ai.type.JsonSchema)(https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html ?> responseSchemaJson)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#setStopSequences(kotlin.collections.List)(https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html> stopSequences)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#setTemperature(kotlin.Float)(https://developer.android.com/reference/kotlin/java/lang/Float.html temperature)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#setThinkingConfig(com.google.firebase.ai.type.ThinkingConfig)(https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig thinkingConfig)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#setTopK(kotlin.Int)(https://developer.android.com/reference/kotlin/java/lang/Integer.html topK)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder#setTopP(kotlin.Float)(https://developer.android.com/reference/kotlin/java/lang/Float.html topP)` |

## Public fields

### candidateCount

```
public final Integer candidateCount
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig#candidateCount()`.

### frequencyPenalty

```
public final Float frequencyPenalty
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig#frequencyPenalty()`

### maxOutputTokens

```
public final Integer maxOutputTokens
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig#maxOutputTokens()`.

### presencePenalty

```
public final Float presencePenalty
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig#presencePenalty()`

### responseJsonSchema

```
public final JsonSchema<@NonNull ?> responseJsonSchema
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig#responseJsonSchema()`

### responseMimeType

```
public final String responseMimeType
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig#responseMimeType()`.

### responseModalities

```
public final List<@NonNull ResponseModality> responseModalities
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig#responseModalities()`.

### responseSchema

```
public final Schema responseSchema
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig#responseSchema()`.

### stopSequences

```
public final List<@NonNull String> stopSequences
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig#stopSequences()`.

### temperature

```
public final Float temperature
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig#temperature()`.

### thinkingConfig

```
public final ThinkingConfig thinkingConfig
```

### topK

```
public final Integer topK
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig#topK()`.

### topP

```
public final Float topP
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig#topP()`.

## Public constructors

### Builder

```
public Builder()
```

## Public methods

### build

```
public final @NonNull GenerationConfig build()
```

Create a new `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig` with the attached arguments.

### setCandidateCount

```
public final @NonNull GenerationConfig.Builder setCandidateCount(Integer candidateCount)
```

### setFrequencyPenalty

```
public final @NonNull GenerationConfig.Builder setFrequencyPenalty(Float frequencyPenalty)
```

### setMaxOutputTokens

```
public final @NonNull GenerationConfig.Builder setMaxOutputTokens(Integer maxOutputTokens)
```

### setPresencePenalty

```
public final @NonNull GenerationConfig.Builder setPresencePenalty(Float presencePenalty)
```

### setResponseMimeType

```
public final @NonNull GenerationConfig.Builder setResponseMimeType(String responseMimeType)
```

### setResponseModalities

```
public final @NonNull GenerationConfig.Builder setResponseModalities(
    List<@NonNull ResponseModality> responseModalities
)
```

### setResponseSchema

```
public final @NonNull GenerationConfig.Builder setResponseSchema(Schema responseSchema)
```

### setResponseSchemaJson

```
public final @NonNull GenerationConfig.Builder setResponseSchemaJson(JsonSchema<@NonNull ?> responseSchemaJson)
```

### setStopSequences

```
public final @NonNull GenerationConfig.Builder setStopSequences(List<@NonNull String> stopSequences)
```

### setTemperature

```
public final @NonNull GenerationConfig.Builder setTemperature(Float temperature)
```

### setThinkingConfig

```
public final @NonNull GenerationConfig.Builder setThinkingConfig(ThinkingConfig thinkingConfig)
```

### setTopK

```
public final @NonNull GenerationConfig.Builder setTopK(Integer topK)
```

### setTopP

```
public final @NonNull GenerationConfig.Builder setTopP(Float topP)
```