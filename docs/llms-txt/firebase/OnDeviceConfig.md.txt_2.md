# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/OnDeviceConfig.md.txt

# OnDeviceConfig

# OnDeviceConfig


```
@PublicPreviewAPI
class OnDeviceConfig
```

<br />

*** ** * ** ***

Configuration for on-device AI model inference.

## Summary

| ### Public companion properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/OnDeviceConfig` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/OnDeviceConfig.Companion#IN_CLOUD()` A default configuration that only uses in-cloud inference. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/OnDeviceConfig#OnDeviceConfig(com.google.firebase.ai.InferenceMode,kotlin.Int,kotlin.Float,kotlin.Int,kotlin.Int,kotlin.Int)( mode: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/InferenceMode, maxOutputTokens: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?, temperature: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?, topK: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?, seed: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?, candidateCount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html )` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/OnDeviceConfig#candidateCount()` The number of generated responses to return. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/OnDeviceConfig#maxOutputTokens()` The maximum number of tokens to generate in the response. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/InferenceMode` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/OnDeviceConfig#mode()` The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/InferenceMode` to use for the model. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/OnDeviceConfig#seed()` The seed to use for generation to ensure reproducibility. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/OnDeviceConfig#temperature()` A parameter controlling the degree of randomness in token selection. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/OnDeviceConfig#topK()` The `topK` parameter changes how the model selects tokens for output. |

## Public companion properties

### IN_CLOUD

```
val IN_CLOUD: OnDeviceConfig
```

A default configuration that only uses in-cloud inference.

## Public constructors

### OnDeviceConfig

```
OnDeviceConfig(
    mode: InferenceMode,
    maxOutputTokens: Int? = null,
    temperature: Float? = null,
    topK: Int? = null,
    seed: Int? = null,
    candidateCount: Int = 1
)
```

## Public properties

### candidateCount

```
val candidateCount: Int
```

The number of generated responses to return. See GenerationConfig for more detail. By default it's set to 1.

### maxOutputTokens

```
val maxOutputTokens: Int?
```

The maximum number of tokens to generate in the response. See GenerationConfig for more detail.

### mode

```
val mode: InferenceMode
```

The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/InferenceMode` to use for the model.

### seed

```
val seed: Int?
```

The seed to use for generation to ensure reproducibility. See GenerationConfig for more detail.

### temperature

```
val temperature: Float?
```

A parameter controlling the degree of randomness in token selection. See GenerationConfig for more detail.

### topK

```
val topK: Int?
```

The `topK` parameter changes how the model selects tokens for output. See GenerationConfig for more detail.