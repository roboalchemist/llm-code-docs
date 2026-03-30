# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig.Builder.md.txt

# GenerationConfig.Builder

# GenerationConfig.Builder


```
public final class GenerationConfig.Builder
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Builder for creating a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig`.

Mainly intended for Java interop. Kotlin consumers should use `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/package-summary#generationConfig(kotlin.Function1)` for a more idiomatic experience.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/package-summary#generationConfig(kotlin.Function1)` |   |

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig.Builder#candidateCount()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig#candidateCount()`. |
| `final https://developer.android.com/reference/kotlin/java/lang/Float.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig.Builder#frequencyPenalty()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig#frequencyPenalty()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig.Builder#maxOutputTokens()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig#maxOutputTokens()`. |
| `final https://developer.android.com/reference/kotlin/java/lang/Float.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig.Builder#presencePenalty()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig#presencePenalty()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig.Builder#responseMimeType()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig#responseMimeType()`. |
| `final https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ResponseModality>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig.Builder#responseModalities()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig#responseModalities()`. |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig.Builder#responseSchema()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig#responseSchema()`. |
| `final https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig.Builder#stopSequences()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig#stopSequences()`. |
| `final https://developer.android.com/reference/kotlin/java/lang/Float.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig.Builder#temperature()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig#temperature()`. |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig.Builder#topK()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig#topK()`. |
| `final https://developer.android.com/reference/kotlin/java/lang/Float.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig.Builder#topP()` See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig#topP()`. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig.Builder#Builder()()` |

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig.Builder#build()()` Create a new `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig` with the attached arguments. |

## Public fields

### candidateCount

```
public final Integer candidateCount
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig#candidateCount()`.

### frequencyPenalty

```
public final Float frequencyPenalty
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig#frequencyPenalty()`

### maxOutputTokens

```
public final Integer maxOutputTokens
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig#maxOutputTokens()`.

### presencePenalty

```
public final Float presencePenalty
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig#presencePenalty()`

### responseMimeType

```
public final String responseMimeType
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig#responseMimeType()`.

### responseModalities

```
public final List<@NonNull ResponseModality> responseModalities
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig#responseModalities()`.

### responseSchema

```
public final Schema responseSchema
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig#responseSchema()`.

### stopSequences

```
public final List<@NonNull String> stopSequences
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig#stopSequences()`.

### temperature

```
public final Float temperature
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig#temperature()`.

### topK

```
public final Integer topK
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig#topK()`.

### topP

```
public final Float topP
```

See `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig#topP()`.

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

Create a new `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfig` with the attached arguments.