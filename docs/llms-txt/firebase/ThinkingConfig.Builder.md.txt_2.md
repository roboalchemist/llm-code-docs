# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ThinkingConfig.Builder.md.txt

# ThinkingConfig.Builder

# ThinkingConfig.Builder


```
class ThinkingConfig.Builder
```

<br />

*** ** * ** ***

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ThinkingConfig.Builder#Builder()()` |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ThinkingConfig` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ThinkingConfig.Builder#build()()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ThinkingConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ThinkingConfig.Builder#setIncludeThoughts(kotlin.Boolean)(includeThoughts: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Indicates whether to request the model to include the thoughts parts in the response. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ThinkingConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ThinkingConfig.Builder#setThinkingBudget(kotlin.Int)(thinkingBudget: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Sets the amount of thinking the model can do to generate a response, defined as a in tokens. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ThinkingConfig.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ThinkingConfig.Builder#setThinkingLevel(com.google.firebase.ai.type.ThinkingLevel)(thinkingLevel: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ThinkingLevel)` Sets the amount of thinking the model can do to generate a response, defined as a . |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ThinkingConfig.Builder#includeThoughts()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ThinkingConfig.Builder#thinkingBudget()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ThinkingLevel?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ThinkingConfig.Builder#thinkingLevel()` |

## Public constructors

### Builder

```
Builder()
```

## Public functions

### build

```
fun build(): ThinkingConfig
```

### setIncludeThoughts

```
fun setIncludeThoughts(includeThoughts: Boolean): ThinkingConfig.Builder
```

Indicates whether to request the model to include the thoughts parts in the response.

Keep in mind that once enabled, you should check for the `isThought` property when processing a `Part` instance to correctly handle both thoughts and the actual response.

The default value is `false`.

### setThinkingBudget

```
fun setThinkingBudget(thinkingBudget: Int): ThinkingConfig.Builder
```

Sets the amount of thinking the model can do to generate a response, defined as a in tokens.

The range of [supported thinking budget values](https://firebase.google.com/docs/ai-logic/thinking#supported-thinking-budget-values) depends on the model.

- To disable thinking, when supported by the model, set this value to `0`.

- To use dynamic thinking, allowing the model to decide on the thinking budget based on the task, set this value to `-1`.

### setThinkingLevel

```
fun setThinkingLevel(thinkingLevel: ThinkingLevel): ThinkingConfig.Builder
```

Sets the amount of thinking the model can do to generate a response, defined as a .

If you don't specify a thinking level, Gemini will use the model's default dynamic thinking level.
> Important: Gemini 2.5 series models do not support thinking levels; use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ThinkingConfig.Builder#setThinkingBudget(kotlin.Int)` to set a thinking budget instead.

| Parameters |
|---|---|
| `thinkingLevel: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ThinkingLevel` | A preset that controls the model's "thinking" process. Use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ThinkingLevel.Companion#LOW()` for faster responses on less complex tasks, and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ThinkingLevel.Companion#HIGH()` for better reasoning on more complex tasks. |

## Public properties

### includeThoughts

```
var includeThoughts: Boolean?
```

### thinkingBudget

```
var thinkingBudget: Int?
```

### thinkingLevel

```
var thinkingLevel: ThinkingLevel?
```