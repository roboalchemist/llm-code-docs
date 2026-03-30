# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CodeExecutionResultPart.md.txt

# CodeExecutionResultPart

# CodeExecutionResultPart


```
class CodeExecutionResultPart : Part
```

<br />

*** ** * ** ***

Represents the code execution result from the model.

## Summary

| ### Public constructors |
|---|
| `[CodeExecutionResultPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CodeExecutionResultPart#CodeExecutionResultPart(kotlin.String,kotlin.String))(outcome: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, output: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` **This function is deprecated.** Part of the model response. |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CodeExecutionResultPart#executionSucceeded()()` Indicates if the code execution was successful |

| ### Public properties |
|---|---|
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CodeExecutionResultPart#isThought()` Indicates whether the response is a thought. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CodeExecutionResultPart#outcome()` The result of the execution. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CodeExecutionResultPart#output()` The stdout from the code execution, or an error message if it failed. |

## Public constructors

### CodeExecutionResultPart

```
[CodeExecutionResultPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CodeExecutionResultPart#CodeExecutionResultPart(kotlin.String,kotlin.String))(outcome: String, output: String)
```

> [!CAUTION]
> **This function is deprecated.**   
> Part of the model response. Do not instantiate directly.

## Public functions

### executionSucceeded

```
fun executionSucceeded(): Boolean
```

Indicates if the code execution was successful

## Public properties

### isThought

```
open val isThought: Boolean
```

Indicates whether the response is a thought.

### outcome

```
val outcome: String
```

The result of the execution.

### output

```
val output: String
```

The stdout from the code execution, or an error message if it failed.