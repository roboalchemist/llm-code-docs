# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder.md.txt

# LiveGenerationConfig.Builder

# LiveGenerationConfig.Builder


```
class LiveGenerationConfig.Builder
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Builder for creating a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig`.

Mainly intended for Java interop. Kotlin consumers should use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/package-summary#liveGenerationConfig(kotlin.Function1)` for a more idiomatic experience.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#Builder()()` |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#build()()` Create a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig` with the attached arguments. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setCandidateCount(kotlin.Int)(candidateCount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setFrequencyPenalty(kotlin.Float)(frequencyPenalty: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setMaxOutputTokens(kotlin.Int)(maxOutputTokens: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setPresencePenalty(kotlin.Float)(presencePenalty: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setResponseModality(com.google.firebase.vertexai.type.ResponseModality)(responseModality: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ResponseModality?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setSpeechConfig(com.google.firebase.vertexai.type.SpeechConfig)(speechConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SpeechConfig?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setTemperature(kotlin.Float)(temperature: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setTopK(kotlin.Int)(topK: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setTopP(kotlin.Float)(topP: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#candidateCount()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#candidateCount()`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#frequencyPenalty()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#frequencyPenalty()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#maxOutputTokens()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#maxOutputTokens()`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#presencePenalty()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#presencePenalty()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ResponseModality?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#responseModality()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#responseModality()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SpeechConfig?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#speechConfig()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#speechConfig()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#temperature()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#temperature()`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#topK()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#topK()`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#topP()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#topP()`. |

## Public constructors

### Builder

```
Builder()
```

## Public functions

### build

```
fun build(): LiveGenerationConfig
```

Create a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig` with the attached arguments.

### setCandidateCount

```
fun setCandidateCount(candidateCount: Int?): LiveGenerationConfig.Builder
```

### setFrequencyPenalty

```
fun setFrequencyPenalty(frequencyPenalty: Float?): LiveGenerationConfig.Builder
```

### setMaxOutputTokens

```
fun setMaxOutputTokens(maxOutputTokens: Int?): LiveGenerationConfig.Builder
```

### setPresencePenalty

```
fun setPresencePenalty(presencePenalty: Float?): LiveGenerationConfig.Builder
```

### setResponseModality

```
fun setResponseModality(responseModality: ResponseModality?): LiveGenerationConfig.Builder
```

### setSpeechConfig

```
fun setSpeechConfig(speechConfig: SpeechConfig?): LiveGenerationConfig.Builder
```

### setTemperature

```
fun setTemperature(temperature: Float?): LiveGenerationConfig.Builder
```

### setTopK

```
fun setTopK(topK: Int?): LiveGenerationConfig.Builder
```

### setTopP

```
fun setTopP(topP: Float?): LiveGenerationConfig.Builder
```

## Public properties

### candidateCount

```
var candidateCount: Int?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#candidateCount()`.

### frequencyPenalty

```
var frequencyPenalty: Float?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#frequencyPenalty()`

### maxOutputTokens

```
var maxOutputTokens: Int?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#maxOutputTokens()`.

### presencePenalty

```
var presencePenalty: Float?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#presencePenalty()`

### responseModality

```
var responseModality: ResponseModality?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#responseModality()`

### speechConfig

```
var speechConfig: SpeechConfig?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#speechConfig()`

### temperature

```
var temperature: Float?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#temperature()`.

### topK

```
var topK: Int?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#topK()`.

### topP

```
var topP: Float?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/LiveGenerationConfig#topP()`.