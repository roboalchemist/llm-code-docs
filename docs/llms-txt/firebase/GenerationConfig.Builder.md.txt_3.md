# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder.md.txt

# GenerationConfig.Builder

# GenerationConfig.Builder


```
class GenerationConfig.Builder
```

<br />

*** ** * ** ***

Builder for creating a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig`.

Mainly intended for Java interop. Kotlin consumers should use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/package-summary#generationConfig(kotlin.Function1)` for a more idiomatic experience.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/package-summary#generationConfig(kotlin.Function1)` |   |

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#Builder()()` |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#build()()` Create a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig` with the attached arguments. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setCandidateCount(kotlin.Int)(candidateCount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setFrequencyPenalty(kotlin.Float)(frequencyPenalty: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setMaxOutputTokens(kotlin.Int)(maxOutputTokens: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setPresencePenalty(kotlin.Float)(presencePenalty: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setResponseMimeType(kotlin.String)(responseMimeType: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setResponseModalities(kotlin.collections.List)(responseModalities: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ResponseModality>?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setResponseSchema(com.google.firebase.ai.type.Schema)(responseSchema: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setResponseSchemaJson(com.google.firebase.ai.type.JsonSchema)(responseSchemaJson: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<*>?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setStopSequences(kotlin.collections.List)(stopSequences: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setTemperature(kotlin.Float)(temperature: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setThinkingConfig(com.google.firebase.ai.type.ThinkingConfig)(thinkingConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ThinkingConfig?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setTopK(kotlin.Int)(topK: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#setTopP(kotlin.Float)(topP: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#candidateCount()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#candidateCount()`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#frequencyPenalty()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#frequencyPenalty()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#maxOutputTokens()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#maxOutputTokens()`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#presencePenalty()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#presencePenalty()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<*>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#responseJsonSchema()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#responseJsonSchema()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#responseMimeType()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#responseMimeType()`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ResponseModality>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#responseModalities()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#responseModalities()`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#responseSchema()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#responseSchema()`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#stopSequences()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#stopSequences()`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#temperature()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#temperature()`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ThinkingConfig?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#thinkingConfig()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#topK()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#topK()`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig.Builder#topP()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#topP()`. |

## Public constructors

### Builder

```
Builder()
```

## Public functions

### build

```
fun build(): GenerationConfig
```

Create a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig` with the attached arguments.

### setCandidateCount

```
fun setCandidateCount(candidateCount: Int?): GenerationConfig.Builder
```

### setFrequencyPenalty

```
fun setFrequencyPenalty(frequencyPenalty: Float?): GenerationConfig.Builder
```

### setMaxOutputTokens

```
fun setMaxOutputTokens(maxOutputTokens: Int?): GenerationConfig.Builder
```

### setPresencePenalty

```
fun setPresencePenalty(presencePenalty: Float?): GenerationConfig.Builder
```

### setResponseMimeType

```
fun setResponseMimeType(responseMimeType: String?): GenerationConfig.Builder
```

### setResponseModalities

```
fun setResponseModalities(responseModalities: List<ResponseModality>?): GenerationConfig.Builder
```

### setResponseSchema

```
fun setResponseSchema(responseSchema: Schema?): GenerationConfig.Builder
```

### setResponseSchemaJson

```
fun setResponseSchemaJson(responseSchemaJson: JsonSchema<*>?): GenerationConfig.Builder
```

### setStopSequences

```
fun setStopSequences(stopSequences: List<String>?): GenerationConfig.Builder
```

### setTemperature

```
fun setTemperature(temperature: Float?): GenerationConfig.Builder
```

### setThinkingConfig

```
fun setThinkingConfig(thinkingConfig: ThinkingConfig?): GenerationConfig.Builder
```

### setTopK

```
fun setTopK(topK: Int?): GenerationConfig.Builder
```

### setTopP

```
fun setTopP(topP: Float?): GenerationConfig.Builder
```

## Public properties

### candidateCount

```
var candidateCount: Int?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#candidateCount()`.

### frequencyPenalty

```
var frequencyPenalty: Float?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#frequencyPenalty()`

### maxOutputTokens

```
var maxOutputTokens: Int?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#maxOutputTokens()`.

### presencePenalty

```
var presencePenalty: Float?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#presencePenalty()`

### responseJsonSchema

```
var responseJsonSchema: JsonSchema<*>?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#responseJsonSchema()`

### responseMimeType

```
var responseMimeType: String?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#responseMimeType()`.

### responseModalities

```
var responseModalities: List<ResponseModality>?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#responseModalities()`.

### responseSchema

```
var responseSchema: Schema?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#responseSchema()`.

### stopSequences

```
var stopSequences: List<String>?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#stopSequences()`.

### temperature

```
var temperature: Float?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#temperature()`.

### thinkingConfig

```
var thinkingConfig: ThinkingConfig?
```

### topK

```
var topK: Int?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#topK()`.

### topP

```
var topP: Float?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GenerationConfig#topP()`.