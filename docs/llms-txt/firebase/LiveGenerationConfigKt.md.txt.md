# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfigKt.md.txt

# LiveGenerationConfigKt

# LiveGenerationConfigKt


```
public final class LiveGenerationConfigKt
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfigKt#liveGenerationConfig(kotlin.Function1)( @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` Helper method to construct a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig` in a DSL-like manner. |

## Public methods

### liveGenerationConfig

```
public static final @NonNull LiveGenerationConfig liveGenerationConfig(
    @ExtensionFunctionType @NonNull Function1<@NonNull LiveGenerationConfig.Builder, Unit> init
)
```

Helper method to construct a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/LiveGenerationConfig` in a DSL-like manner.

Example Usage:

```
liveGenerationConfig {
  temperature = 0.75f
  topP = 0.5f
  topK = 30
  candidateCount = 4
  maxOutputTokens = 300
  ...
}
```