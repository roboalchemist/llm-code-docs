# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/OneParameterFunction.md.txt

# OneParameterFunction

# OneParameterFunction


```
class OneParameterFunction<T : Any?> : FunctionDeclaration
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.vertexai.type.FunctionDeclaration](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionDeclaration) ||
|   | ↳ | [com.google.firebase.vertexai.type.OneParameterFunction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/OneParameterFunction) |

*** ** * ** ***

A declared one param function, including implementation, that a model can be given access to in order to gain info or complete tasks.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/package-summary#defineFunction(kotlin.String,kotlin.String,kotlin.coroutines.SuspendFunction0)` | for how to create an instance of this class. |

## Summary

| ### Public functions |
|---|---|
| `open suspend https://developer.android.com/reference/kotlin/org/json/JSONObject.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/OneParameterFunction#execute(com.google.firebase.vertexai.type.FunctionCallPart)(part: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart)` Run the attached function with the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/OneParameterFunction#execute(com.google.firebase.vertexai.type.FunctionCallPart)`. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema<T>>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/OneParameterFunction#getParameters()()` The parameters of the attached function as a list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema`. |

| ### Public properties |
|---|---|
| `suspend (T) -> https://developer.android.com/reference/kotlin/org/json/JSONObject.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/OneParameterFunction#function()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema<T>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/OneParameterFunction#param()` |

| ### Inherited properties |
|---|
| From [com.google.firebase.vertexai.type.FunctionDeclaration](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionDeclaration) |---|---| | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionDeclaration#description()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionDeclaration#name()` | |

## Public functions

### execute

```
open suspend fun execute(part: FunctionCallPart): JSONObject
```

Run the attached function with the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/OneParameterFunction#execute(com.google.firebase.vertexai.type.FunctionCallPart)`.

### getParameters

```
open fun getParameters(): List<Schema<T>>
```

The parameters of the attached function as a list of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema`.

## Public properties

### function

```
val function: suspend (T) -> JSONObject
```

### param

```
val param: Schema<T>
```