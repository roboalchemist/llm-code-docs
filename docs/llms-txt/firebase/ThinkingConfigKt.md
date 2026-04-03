# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfigKt.md.txt

# ThinkingConfigKt

# ThinkingConfigKt


```
public final class ThinkingConfigKt
```

<br />

*** ** * ** ***

## Summary

|                                                                                                      ### Public methods                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ThinkingConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig) | [thinkingConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfigKt#thinkingConfig(kotlin.Function1))`(` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ThinkingConfig.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig.Builder)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> init` `)` Helper method to construct a [ThinkingConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig) in a DSL-like manner. |

## Public methods

### thinkingConfig

```
publicÂ staticÂ finalÂ @NonNull ThinkingConfigÂ thinkingConfig(
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull ThinkingConfig.Builder,Â Unit>Â init
)
```

Helper method to construct a [ThinkingConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig) in a DSL-like manner.

Example Usage:  

```text
thinkingConfig {
  thinkingBudget = 0 // disable thinking
}
```