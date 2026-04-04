# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/CodeExecutionResultPart.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CodeExecutionResultPart.md.txt

# CodeExecutionResultPart


```
class CodeExecutionResultPart : Part
```

<br />

*** ** * ** ***

Represents the code execution result from the model.

## Summary

|                                                                                                                                                                                                              ### Public constructors                                                                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ~~[CodeExecutionResultPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CodeExecutionResultPart#CodeExecutionResultPart(kotlin.String,kotlin.String))~~`(outcome: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, output: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` **This function is deprecated.** Part of the model response. |

|                                ### Public functions                                |
|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | [executionSucceeded](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CodeExecutionResultPart#executionSucceeded())`()` Indicates if the code execution was successful |

|                                   ### Public properties                                   |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `open `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | [isThought](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CodeExecutionResultPart#isThought()) Indicates whether the response is a thought.                    |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)          | [outcome](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CodeExecutionResultPart#outcome()) The result of the execution.                                        |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)          | [output](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CodeExecutionResultPart#output()) The stdout from the code execution, or an error message if it failed. |

## Public constructors

### CodeExecutionResultPart

```
[CodeExecutionResultPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/CodeExecutionResultPart#CodeExecutionResultPart(kotlin.String,kotlin.String))(outcome:Â String,Â output:Â String)
```
| **This function is deprecated.**   
Part of the model response. Do not instantiate directly.  

## Public functions

### executionSucceeded

```
funÂ executionSucceeded():Â Boolean
```

Indicates if the code execution was successful  

## Public properties

### isThought

```
openÂ valÂ isThought:Â Boolean
```

Indicates whether the response is a thought.  

### outcome

```
valÂ outcome:Â String
```

The result of the execution.  

### output

```
valÂ output:Â String
```

The stdout from the code execution, or an error message if it failed.