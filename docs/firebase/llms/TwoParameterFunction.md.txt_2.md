# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/TwoParameterFunction.md.txt

# TwoParameterFunction

# TwoParameterFunction


```
class TwoParameterFunction<T : Any?, U : Any?> : FunctionDeclaration
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.vertexai.type.FunctionDeclaration](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionDeclaration) ||
|   | ↳ | [com.google.firebase.vertexai.type.TwoParameterFunction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/TwoParameterFunction) |

*** ** * ** ***

A declared two param function, including implementation, that a model can be given access to in order to gain info or complete tasks.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/package-summary#defineFunction(kotlin.String,kotlin.String,kotlin.coroutines.SuspendFunction0)` | for how to create an instance of this class. |

## Summary

| ### Public functions |
|---|---|
| `open suspend https://developer.android.com/reference/kotlin/org/json/JSONObject.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/TwoParameterFunction#execute(com.google.firebase.vertexai.type.FunctionCallPart)(part: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart)` Run the attached function with the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/TwoParameterFunction#execute(com.google.firebase.vertexai.type.FunctionCallPart)`. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/TwoParameterFunction#getParameters()()` The parameters of the attached function as a list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema`. |

| ### Public properties |
|---|---|
| `suspend (T, U) -> https://developer.android.com/reference/kotlin/org/json/JSONObject.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/TwoParameterFunction#function()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema<T>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/TwoParameterFunction#param1()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema<U>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/TwoParameterFunction#param2()` |

| ### Inherited properties |
|---|
| From [com.google.firebase.vertexai.type.FunctionDeclaration](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionDeclaration) |---|---| | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionDeclaration#description()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionDeclaration#name()` | |

## Public functions

### execute

```
open suspend fun execute(part: FunctionCallPart): JSONObject
```

Run the attached function with the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/TwoParameterFunction#execute(com.google.firebase.vertexai.type.FunctionCallPart)`.

### getParameters

```
open fun getParameters(): List<Schema<Any?>>
```

The parameters of the attached function as a list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema`.

## Public properties

### function

```
val function: suspend (T, U) -> JSONObject
```

### param1

```
val param1: Schema<T>
```

### param2

```
val param2: Schema<U>
```