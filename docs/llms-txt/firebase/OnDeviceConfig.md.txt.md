# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/OnDeviceConfig.md.txt

# OnDeviceConfig

# OnDeviceConfig


```
@PublicPreviewAPI
public final class OnDeviceConfig
```

<br />

*** ** * ** ***

Configuration for on-device AI model inference.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/OnDeviceConfig.Companion` |

| ### Public fields |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/OnDeviceConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/OnDeviceConfig.Companion#IN_CLOUD()` A default configuration that only uses in-cloud inference. |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/OnDeviceConfig#candidateCount()` The number of generated responses to return. |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/OnDeviceConfig#maxOutputTokens()` The maximum number of tokens to generate in the response. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/InferenceMode` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/OnDeviceConfig#mode()` The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/InferenceMode` to use for the model. |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/OnDeviceConfig#seed()` The seed to use for generation to ensure reproducibility. |
| `final https://developer.android.com/reference/kotlin/java/lang/Float.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/OnDeviceConfig#temperature()` A parameter controlling the degree of randomness in token selection. |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/OnDeviceConfig#topK()` The `topK` parameter changes how the model selects tokens for output. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/OnDeviceConfig#OnDeviceConfig(com.google.firebase.ai.InferenceMode,kotlin.Int,kotlin.Float,kotlin.Int,kotlin.Int,kotlin.Int)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/InferenceMode mode, https://developer.android.com/reference/kotlin/java/lang/Integer.html maxOutputTokens, https://developer.android.com/reference/kotlin/java/lang/Float.html temperature, https://developer.android.com/reference/kotlin/java/lang/Integer.html topK, https://developer.android.com/reference/kotlin/java/lang/Integer.html seed, int candidateCount )` |

## Public fields

### IN_CLOUD

```
public static final @NonNull OnDeviceConfig IN_CLOUD
```

A default configuration that only uses in-cloud inference.

### candidateCount

```
public final int candidateCount
```

The number of generated responses to return. See GenerationConfig for more detail. By default it's set to 1.

### maxOutputTokens

```
public final Integer maxOutputTokens
```

The maximum number of tokens to generate in the response. See GenerationConfig for more detail.

### mode

```
public final @NonNull InferenceMode mode
```

The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/InferenceMode` to use for the model.

### seed

```
public final Integer seed
```

The seed to use for generation to ensure reproducibility. See GenerationConfig for more detail.

### temperature

```
public final Float temperature
```

A parameter controlling the degree of randomness in token selection. See GenerationConfig for more detail.

### topK

```
public final Integer topK
```

The `topK` parameter changes how the model selects tokens for output. See GenerationConfig for more detail.

## Public constructors

### OnDeviceConfig

```
public OnDeviceConfig(
    @NonNull InferenceMode mode,
    Integer maxOutputTokens,
    Float temperature,
    Integer topK,
    Integer seed,
    int candidateCount
)
```