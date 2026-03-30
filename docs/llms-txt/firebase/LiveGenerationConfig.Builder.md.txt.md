# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder.md.txt

# LiveGenerationConfig.Builder

# LiveGenerationConfig.Builder


```
public final class LiveGenerationConfig.Builder
```

<br />

*** ** * ** ***

Builder for creating a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig`.

Mainly intended for Java interop. Kotlin consumers should use `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/package-summary#liveGenerationConfig(kotlin.Function1)` for a more idiomatic experience.

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/Float.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder#frequencyPenalty()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig#frequencyPenalty()` |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/AudioTranscriptionConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder#inputAudioTranscription()` see `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig#inputAudioTranscription()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder#maxOutputTokens()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig#maxOutputTokens()`. |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/AudioTranscriptionConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder#outputAudioTranscription()` see `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig#outputAudioTranscription()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Float.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder#presencePenalty()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig#presencePenalty()` |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ResponseModality` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder#responseModality()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig#responseModality()` |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SpeechConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder#speechConfig()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig#speechConfig()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Float.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder#temperature()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig#temperature()`. |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder#topK()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig#topK()`. |
| `final https://developer.android.com/reference/kotlin/java/lang/Float.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder#topP()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig#topP()`. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder#Builder()()` |

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder#build()()` Create a new `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig` with the attached arguments. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder#setFrequencyPenalty(kotlin.Float)(https://developer.android.com/reference/kotlin/java/lang/Float.html frequencyPenalty)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder#setInputAudioTranscription(com.google.firebase.ai.type.AudioTranscriptionConfig)(https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/AudioTranscriptionConfig config)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder#setMaxOutputTokens(kotlin.Int)(https://developer.android.com/reference/kotlin/java/lang/Integer.html maxOutputTokens)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder#setOutputAudioTranscription(com.google.firebase.ai.type.AudioTranscriptionConfig)(https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/AudioTranscriptionConfig config)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder#setPresencePenalty(kotlin.Float)(https://developer.android.com/reference/kotlin/java/lang/Float.html presencePenalty)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder#setResponseModality(com.google.firebase.ai.type.ResponseModality)(https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ResponseModality responseModality)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder#setSpeechConfig(com.google.firebase.ai.type.SpeechConfig)(https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/SpeechConfig speechConfig)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder#setTemperature(kotlin.Float)(https://developer.android.com/reference/kotlin/java/lang/Float.html temperature)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder#setTopK(kotlin.Int)(https://developer.android.com/reference/kotlin/java/lang/Integer.html topK)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder#setTopP(kotlin.Float)(https://developer.android.com/reference/kotlin/java/lang/Float.html topP)` |

## Public fields

### frequencyPenalty

```
public final Float frequencyPenalty
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig#frequencyPenalty()`

### inputAudioTranscription

```
public final AudioTranscriptionConfig inputAudioTranscription
```

see `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig#inputAudioTranscription()`

### maxOutputTokens

```
public final Integer maxOutputTokens
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig#maxOutputTokens()`.

### outputAudioTranscription

```
public final AudioTranscriptionConfig outputAudioTranscription
```

see `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig#outputAudioTranscription()`

### presencePenalty

```
public final Float presencePenalty
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig#presencePenalty()`

### responseModality

```
public final ResponseModality responseModality
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig#responseModality()`

### speechConfig

```
public final SpeechConfig speechConfig
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig#speechConfig()`

### temperature

```
public final Float temperature
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig#temperature()`.

### topK

```
public final Integer topK
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig#topK()`.

### topP

```
public final Float topP
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig#topP()`.

## Public constructors

### Builder

```
public Builder()
```

## Public methods

### build

```
public final @NonNull LiveGenerationConfig build()
```

Create a new `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig` with the attached arguments.

### setFrequencyPenalty

```
public final @NonNull LiveGenerationConfig.Builder setFrequencyPenalty(Float frequencyPenalty)
```

### setInputAudioTranscription

```
public final @NonNull LiveGenerationConfig.Builder setInputAudioTranscription(AudioTranscriptionConfig config)
```

### setMaxOutputTokens

```
public final @NonNull LiveGenerationConfig.Builder setMaxOutputTokens(Integer maxOutputTokens)
```

### setOutputAudioTranscription

```
public final @NonNull LiveGenerationConfig.Builder setOutputAudioTranscription(AudioTranscriptionConfig config)
```

### setPresencePenalty

```
public final @NonNull LiveGenerationConfig.Builder setPresencePenalty(Float presencePenalty)
```

### setResponseModality

```
public final @NonNull LiveGenerationConfig.Builder setResponseModality(ResponseModality responseModality)
```

### setSpeechConfig

```
public final @NonNull LiveGenerationConfig.Builder setSpeechConfig(SpeechConfig speechConfig)
```

### setTemperature

```
public final @NonNull LiveGenerationConfig.Builder setTemperature(Float temperature)
```

### setTopK

```
public final @NonNull LiveGenerationConfig.Builder setTopK(Integer topK)
```

### setTopP

```
public final @NonNull LiveGenerationConfig.Builder setTopP(Float topP)
```