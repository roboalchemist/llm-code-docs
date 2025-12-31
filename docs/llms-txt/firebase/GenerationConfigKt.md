# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/GenerationConfigKt.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfigKt.md.txt

# GenerationConfigKt

# GenerationConfigKt


```
public final class GenerationConfigKt
```

<br />

*** ** * ** ***

## Summary

|                                                                                                        ### Public methods                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[GenerationConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig) | [generationConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfigKt#generationConfig(kotlin.Function1))`(` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[GenerationConfig.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> init` `)` Helper method to construct a [GenerationConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig) in a DSL-like manner. |

## Public methods

### generationConfig

```
publicÂ staticÂ finalÂ @NonNull GenerationConfigÂ generationConfig(
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull GenerationConfig.Builder,Â Unit>Â init
)
```

Helper method to construct a [GenerationConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig) in a DSL-like manner.

Example Usage:  

```text
generationConfig {
  temperature = 0.75f
  topP = 0.5f
  topK = 30
  candidateCount = 4
  maxOutputTokens = 300
  stopSequences = listOf("in conclusion", "-----", "do you need")
}
```