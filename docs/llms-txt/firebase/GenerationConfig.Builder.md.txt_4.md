# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig.Builder.md.txt

# GenerationConfig.Builder

# GenerationConfig.Builder


```
class GenerationConfig.Builder
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Builder for creating a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig`.

Mainly intended for Java interop. Kotlin consumers should use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/package-summary#generationConfig(kotlin.Function1)` for a more idiomatic experience.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/package-summary#generationConfig(kotlin.Function1)` |   |

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig.Builder#Builder()()` |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig.Builder#build()()` Create a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig` with the attached arguments. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig.Builder#candidateCount()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig#candidateCount()`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig.Builder#frequencyPenalty()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig#frequencyPenalty()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig.Builder#maxOutputTokens()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig#maxOutputTokens()`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig.Builder#presencePenalty()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig#presencePenalty()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig.Builder#responseMimeType()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig#responseMimeType()`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ResponseModality>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig.Builder#responseModalities()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig#responseModalities()`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig.Builder#responseSchema()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig#responseSchema()`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig.Builder#stopSequences()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig#stopSequences()`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig.Builder#temperature()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig#temperature()`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig.Builder#topK()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig#topK()`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig.Builder#topP()` See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig#topP()`. |

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

Create a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig` with the attached arguments.

## Public properties

### candidateCount

```
var candidateCount: Int?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig#candidateCount()`.

### frequencyPenalty

```
var frequencyPenalty: Float?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig#frequencyPenalty()`

### maxOutputTokens

```
var maxOutputTokens: Int?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig#maxOutputTokens()`.

### presencePenalty

```
var presencePenalty: Float?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig#presencePenalty()`

### responseMimeType

```
var responseMimeType: String?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig#responseMimeType()`.

### responseModalities

```
var responseModalities: List<ResponseModality>?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig#responseModalities()`.

### responseSchema

```
var responseSchema: Schema?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig#responseSchema()`.

### stopSequences

```
var stopSequences: List<String>?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig#stopSequences()`.

### temperature

```
var temperature: Float?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig#temperature()`.

### topK

```
var topK: Int?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig#topK()`.

### topP

```
var topP: Float?
```

See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/GenerationConfig#topP()`.