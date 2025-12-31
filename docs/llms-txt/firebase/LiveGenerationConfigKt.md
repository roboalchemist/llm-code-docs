# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfigKt.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfigKt.md.txt

# LiveGenerationConfigKt


```
public final class LiveGenerationConfigKt
```

<br />

*** ** * ** ***

## Summary

|                                                                                                            ### Public methods                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[LiveGenerationConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig) | [liveGenerationConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfigKt#liveGenerationConfig(kotlin.Function1))`(` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[LiveGenerationConfig.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig.Builder)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> init` `)` Helper method to construct a [LiveGenerationConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig) in a DSL-like manner. |

## Public methods

### liveGenerationConfig

```
publicÂ staticÂ finalÂ @NonNull LiveGenerationConfigÂ liveGenerationConfig(
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull LiveGenerationConfig.Builder,Â Unit>Â init
)
```

Helper method to construct a [LiveGenerationConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/LiveGenerationConfig) in a DSL-like manner.

Example Usage:  

```text
liveGenerationConfig {
  temperature = 0.75f
  topP = 0.5f
  topK = 30
  maxOutputTokens = 300
  ...
}
```