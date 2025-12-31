# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ThinkingConfig.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig.Builder.md.txt

# ThinkingConfig.Builder

# ThinkingConfig.Builder


```
public final class ThinkingConfig.Builder
```

<br />

*** ** * ** ***

## Summary

|                                    ### Public fields                                     |
|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `final `[Boolean](https://developer.android.com/reference/kotlin/java/lang/Boolean.html) | [includeThoughts](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig.Builder#includeThoughts()) |
| `final `[Integer](https://developer.android.com/reference/kotlin/java/lang/Integer.html) | [thinkingBudget](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig.Builder#thinkingBudget())   |

|                                                    ### Public constructors                                                     |
|--------------------------------------------------------------------------------------------------------------------------------|
| [Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig.Builder#Builder())`()` |

|                                                                                                          ### Public methods                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ThinkingConfig](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig.Builder#build())`()`                                                                                                                                                      |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ThinkingConfig.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig.Builder) | [setIncludeThoughts](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig.Builder#setIncludeThoughts(kotlin.Boolean))`(boolean includeThoughts)` Indicates whether to request the model to include the thoughts parts in the response. |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[ThinkingConfig.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig.Builder) | [setThinkingBudget](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ThinkingConfig.Builder#setThinkingBudget(kotlin.Int))`(int thinkingBudget)` Indicates the thinking budget in tokens.                                                         |

## Public fields

### includeThoughts

```
publicÂ finalÂ BooleanÂ includeThoughts
```  

### thinkingBudget

```
publicÂ finalÂ IntegerÂ thinkingBudget
```  

## Public constructors

### Builder

```
publicÂ Builder()
```  

## Public methods

### build

```
publicÂ finalÂ @NonNull ThinkingConfigÂ build()
```  

### setIncludeThoughts

```
publicÂ finalÂ @NonNull ThinkingConfig.BuilderÂ setIncludeThoughts(booleanÂ includeThoughts)
```

Indicates whether to request the model to include the thoughts parts in the response.

Keep in mind that once enabled, you should check for the `isThought` property when processing a `Part` instance to correctly handle both thoughts and the actual response.

The default value is `false`.  

### setThinkingBudget

```
publicÂ finalÂ @NonNull ThinkingConfig.BuilderÂ setThinkingBudget(intÂ thinkingBudget)
```

Indicates the thinking budget in tokens. `0` is disabled. `-1` is dynamic. The default values and allowed ranges are model dependent.