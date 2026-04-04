# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig.Builder.md.txt

# ThinkingConfig.Builder

# ThinkingConfig.Builder


```
public final class ThinkingConfig.Builder
```

<br />

*** ** * ** ***

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/Boolean.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig.Builder#includeThoughts()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig.Builder#thinkingBudget()` |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingLevel` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig.Builder#thinkingLevel()` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig.Builder#Builder()()` |

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig.Builder#build()()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig.Builder#setIncludeThoughts(kotlin.Boolean)(boolean includeThoughts)` Indicates whether to request the model to include the thoughts parts in the response. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig.Builder#setThinkingBudget(kotlin.Int)(int thinkingBudget)` Sets the amount of thinking the model can do to generate a response, defined as a in tokens. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig.Builder#setThinkingLevel(com.google.firebase.ai.type.ThinkingLevel)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingLevel thinkingLevel)` Sets the amount of thinking the model can do to generate a response, defined as a . |

## Public fields

### includeThoughts

```
public final Boolean includeThoughts
```

### thinkingBudget

```
public final Integer thinkingBudget
```

### thinkingLevel

```
public final ThinkingLevel thinkingLevel
```

## Public constructors

### Builder

```
public Builder()
```

## Public methods

### build

```
public final @NonNull ThinkingConfig build()
```

### setIncludeThoughts

```
public final @NonNull ThinkingConfig.Builder setIncludeThoughts(boolean includeThoughts)
```

Indicates whether to request the model to include the thoughts parts in the response.

Keep in mind that once enabled, you should check for the `isThought` property when processing a `Part` instance to correctly handle both thoughts and the actual response.

The default value is `false`.

### setThinkingBudget

```
public final @NonNull ThinkingConfig.Builder setThinkingBudget(int thinkingBudget)
```

Sets the amount of thinking the model can do to generate a response, defined as a in tokens.

The range of [supported thinking budget values](https://firebase.google.com/docs/ai-logic/thinking#supported-thinking-budget-values) depends on the model.

- To disable thinking, when supported by the model, set this value to `0`.

- To use dynamic thinking, allowing the model to decide on the thinking budget based on the task, set this value to `-1`.

### setThinkingLevel

```
public final @NonNull ThinkingConfig.Builder setThinkingLevel(@NonNull ThinkingLevel thinkingLevel)
```

Sets the amount of thinking the model can do to generate a response, defined as a .

If you don't specify a thinking level, Gemini will use the model's default dynamic thinking level.
> Important: Gemini 2.5 series models do not support thinking levels; use `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig.Builder#setThinkingBudget(kotlin.Int)` to set a thinking budget instead.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingLevel thinkingLevel` | A preset that controls the model's "thinking" process. Use `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingLevel.Companion#LOW()` for faster responses on less complex tasks, and `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingLevel.Companion#HIGH()` for better reasoning on more complex tasks. |