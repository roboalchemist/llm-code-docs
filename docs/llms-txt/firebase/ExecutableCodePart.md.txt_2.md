# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ExecutableCodePart.md.txt

# ExecutableCodePart

# ExecutableCodePart


```
class ExecutableCodePart : Part
```

<br />

*** ** * ** ***

Represents the code that was executed by the model.

## Summary

| ### Public constructors |
|---|
| `[ExecutableCodePart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ExecutableCodePart#ExecutableCodePart(kotlin.String,kotlin.String))(language: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, code: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` **This function is deprecated.** Part of the model response. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ExecutableCodePart#code()` The source code to be executed. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ExecutableCodePart#isThought()` Indicates whether the response is a thought. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ExecutableCodePart#language()` The programming language of the code. |

## Public constructors

### ExecutableCodePart

```
[ExecutableCodePart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ExecutableCodePart#ExecutableCodePart(kotlin.String,kotlin.String))(language: String, code: String)
```

> [!CAUTION]
> **This function is deprecated.**   
> Part of the model response. Do not instantiate directly.

## Public properties

### code

```
val code: String
```

The source code to be executed.

### isThought

```
open val isThought: Boolean
```

Indicates whether the response is a thought.

### language

```
val language: String
```

The programming language of the code.