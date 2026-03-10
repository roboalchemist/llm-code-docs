# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CodeExecutionResultPart.md.txt

# CodeExecutionResultPart

# CodeExecutionResultPart


```
public final class CodeExecutionResultPart implements Part
```

<br />

*** ** * ** ***

Represents the code execution result from the model.

## Summary

| ### Public fields |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CodeExecutionResultPart#isThought()` Indicates whether the response is a thought. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CodeExecutionResultPart#outcome()` The result of the execution. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CodeExecutionResultPart#output()` The stdout from the code execution, or an error message if it failed. |

| ### Public constructors |
|---|
| `[CodeExecutionResultPart](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CodeExecutionResultPart#CodeExecutionResultPart(kotlin.String,kotlin.String))(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html outcome, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html output)` **This method is deprecated.** Part of the model response. |

| ### Public methods |
|---|---|
| `final boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CodeExecutionResultPart#executionSucceeded()()` Indicates if the code execution was successful |

## Public fields

### isThought

```
public boolean isThought
```

Indicates whether the response is a thought.

### outcome

```
public final @NonNull String outcome
```

The result of the execution.

### output

```
public final @NonNull String output
```

The stdout from the code execution, or an error message if it failed.

## Public constructors

### CodeExecutionResultPart

```
public [CodeExecutionResultPart](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CodeExecutionResultPart#CodeExecutionResultPart(kotlin.String,kotlin.String))(@NonNull String outcome, @NonNull String output)
```

> [!CAUTION]
> **This method is deprecated.**   
> Part of the model response. Do not instantiate directly.

## Public methods

### executionSucceeded

```
public final boolean executionSucceeded()
```

Indicates if the code execution was successful