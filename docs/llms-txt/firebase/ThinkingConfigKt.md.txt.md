# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfigKt.md.txt

# ThinkingConfigKt

# ThinkingConfigKt


```
public final class ThinkingConfigKt
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfigKt#thinkingConfig(kotlin.Function1)( @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` Helper method to construct a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig` in a DSL-like manner. |

## Public methods

### thinkingConfig

```
public static final @NonNull ThinkingConfig thinkingConfig(
    @ExtensionFunctionType @NonNull Function1<@NonNull ThinkingConfig.Builder, Unit> init
)
```

Helper method to construct a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig` in a DSL-like manner.

Example Usage:

```
thinkingConfig {
  thinkingBudget = 0 // disable thinking
}
```