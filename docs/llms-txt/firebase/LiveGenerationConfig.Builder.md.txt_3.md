# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder.md.txt

# LiveGenerationConfig.Builder

# LiveGenerationConfig.Builder


```
class LiveGenerationConfig.Builder
```

<br />

*** ** * ** ***

Builder for creating a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig`.

Mainly intended for Java interop. Kotlin consumers should use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/package-summary#liveGenerationConfig(kotlin.Function1)` for a more idiomatic experience.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder#Builder()()` |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder#build()()` Create a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig` with the attached arguments. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder#setFrequencyPenalty(kotlin.Float)(frequencyPenalty: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder#setInputAudioTranscription(com.google.firebase.ai.type.AudioTranscriptionConfig)(config: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/AudioTranscriptionConfig?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder#setMaxOutputTokens(kotlin.Int)(maxOutputTokens: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder#setOutputAudioTranscription(com.google.firebase.ai.type.AudioTranscriptionConfig)(config: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/AudioTranscriptionConfig?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder#setPresencePenalty(kotlin.Float)(presencePenalty: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder#setResponseModality(com.google.firebase.ai.type.ResponseModality)(responseModality: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ResponseModality?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder#setSpeechConfig(com.google.firebase.ai.type.SpeechConfig)(speechConfig: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SpeechConfig?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder#setTemperature(kotlin.Float)(temperature: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder#setTopK(kotlin.Int)(topK: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder#setTopP(kotlin.Float)(topP: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder#frequencyPenalty()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig#frequencyPenalty()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/AudioTranscriptionConfig?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder#inputAudioTranscription()` see `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig#inputAudioTranscription()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder#maxOutputTokens()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig#maxOutputTokens()`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/AudioTranscriptionConfig?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder#outputAudioTranscription()` see `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig#outputAudioTranscription()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder#presencePenalty()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig#presencePenalty()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ResponseModality?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder#responseModality()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig#responseModality()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/SpeechConfig?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder#speechConfig()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig#speechConfig()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder#temperature()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig#temperature()`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder#topK()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig#topK()`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig.Builder#topP()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig#topP()`. |

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

Create a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig` with the attached arguments.

### setFrequencyPenalty

```
fun setFrequencyPenalty(frequencyPenalty: Float?): LiveGenerationConfig.Builder
```

### setInputAudioTranscription

```
fun setInputAudioTranscription(config: AudioTranscriptionConfig?): LiveGenerationConfig.Builder
```

### setMaxOutputTokens

```
fun setMaxOutputTokens(maxOutputTokens: Int?): LiveGenerationConfig.Builder
```

### setOutputAudioTranscription

```
fun setOutputAudioTranscription(config: AudioTranscriptionConfig?): LiveGenerationConfig.Builder
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

### frequencyPenalty

```
var frequencyPenalty: Float?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig#frequencyPenalty()`

### inputAudioTranscription

```
var inputAudioTranscription: AudioTranscriptionConfig?
```

see `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig#inputAudioTranscription()`

### maxOutputTokens

```
var maxOutputTokens: Int?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig#maxOutputTokens()`.

### outputAudioTranscription

```
var outputAudioTranscription: AudioTranscriptionConfig?
```

see `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig#outputAudioTranscription()`

### presencePenalty

```
var presencePenalty: Float?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig#presencePenalty()`

### responseModality

```
var responseModality: ResponseModality?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig#responseModality()`

### speechConfig

```
var speechConfig: SpeechConfig?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig#speechConfig()`

### temperature

```
var temperature: Float?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig#temperature()`.

### topK

```
var topK: Int?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig#topK()`.

### topP

```
var topP: Float?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/LiveGenerationConfig#topP()`.