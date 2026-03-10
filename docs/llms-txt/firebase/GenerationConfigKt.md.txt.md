# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfigKt.md.txt

# GenerationConfigKt

# GenerationConfigKt


```
public final class GenerationConfigKt
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfigKt#generationConfig(kotlin.Function1)( @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` Helper method to construct a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig` in a DSL-like manner. |

## Public methods

### generationConfig

```
public static final @NonNull GenerationConfig generationConfig(
    @ExtensionFunctionType @NonNull Function1<@NonNull GenerationConfig.Builder, Unit> init
)
```

Helper method to construct a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GenerationConfig` in a DSL-like manner.

Example Usage:

```
generationConfig {
  temperature = 0.75f
  topP = 0.5f
  topK = 30
  candidateCount = 4
  maxOutputTokens = 300
  stopSequences = listOf("in conclusion", "---", "do you need")
}
```