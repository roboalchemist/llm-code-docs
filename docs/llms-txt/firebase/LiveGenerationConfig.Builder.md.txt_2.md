# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder.md.txt

# LiveGenerationConfig.Builder

# LiveGenerationConfig.Builder


```
public final class LiveGenerationConfig.Builder
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Builder for creating a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig`.

Mainly intended for Java interop. Kotlin consumers should use `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/package-summary#liveGenerationConfig(kotlin.Function1)` for a more idiomatic experience.

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#candidateCount()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig#candidateCount()`. |
| `final https://developer.android.com/reference/kotlin/java/lang/Float.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#frequencyPenalty()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig#frequencyPenalty()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#maxOutputTokens()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig#maxOutputTokens()`. |
| `final https://developer.android.com/reference/kotlin/java/lang/Float.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#presencePenalty()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig#presencePenalty()` |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ResponseModality` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#responseModality()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig#responseModality()` |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SpeechConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#speechConfig()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig#speechConfig()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Float.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#temperature()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig#temperature()`. |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#topK()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig#topK()`. |
| `final https://developer.android.com/reference/kotlin/java/lang/Float.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#topP()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig#topP()`. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#Builder()()` |

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#build()()` Create a new `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig` with the attached arguments. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setCandidateCount(kotlin.Int)(https://developer.android.com/reference/kotlin/java/lang/Integer.html candidateCount)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setFrequencyPenalty(kotlin.Float)(https://developer.android.com/reference/kotlin/java/lang/Float.html frequencyPenalty)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setMaxOutputTokens(kotlin.Int)(https://developer.android.com/reference/kotlin/java/lang/Integer.html maxOutputTokens)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setPresencePenalty(kotlin.Float)(https://developer.android.com/reference/kotlin/java/lang/Float.html presencePenalty)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setResponseModality(com.google.firebase.vertexai.type.ResponseModality)(https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ResponseModality responseModality)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setSpeechConfig(com.google.firebase.vertexai.type.SpeechConfig)(https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SpeechConfig speechConfig)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setTemperature(kotlin.Float)(https://developer.android.com/reference/kotlin/java/lang/Float.html temperature)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setTopK(kotlin.Int)(https://developer.android.com/reference/kotlin/java/lang/Integer.html topK)` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder#setTopP(kotlin.Float)(https://developer.android.com/reference/kotlin/java/lang/Float.html topP)` |

## Public fields

### candidateCount

```
public final Integer candidateCount
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig#candidateCount()`.

### frequencyPenalty

```
public final Float frequencyPenalty
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig#frequencyPenalty()`

### maxOutputTokens

```
public final Integer maxOutputTokens
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig#maxOutputTokens()`.

### presencePenalty

```
public final Float presencePenalty
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig#presencePenalty()`

### responseModality

```
public final ResponseModality responseModality
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig#responseModality()`

### speechConfig

```
public final SpeechConfig speechConfig
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig#speechConfig()`

### temperature

```
public final Float temperature
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig#temperature()`.

### topK

```
public final Integer topK
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig#topK()`.

### topP

```
public final Float topP
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig#topP()`.

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

Create a new `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig` with the attached arguments.

### setCandidateCount

```
public final @NonNull LiveGenerationConfig.Builder setCandidateCount(Integer candidateCount)
```

### setFrequencyPenalty

```
public final @NonNull LiveGenerationConfig.Builder setFrequencyPenalty(Float frequencyPenalty)
```

### setMaxOutputTokens

```
public final @NonNull LiveGenerationConfig.Builder setMaxOutputTokens(Integer maxOutputTokens)
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