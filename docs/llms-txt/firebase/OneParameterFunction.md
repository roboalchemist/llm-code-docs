# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/OneParameterFunction.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/OneParameterFunction.md.txt

# OneParameterFunction

# OneParameterFunction


```
class OneParameterFunction<TÂ :Â Any?> : FunctionDeclaration
```

<br />

|---|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                                        |||
| â³ | [com.google.firebase.vertexai.type.FunctionDeclaration](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionDeclaration)      ||
|   | â³ | [com.google.firebase.vertexai.type.OneParameterFunction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/OneParameterFunction) |

*** ** * ** ***

A declared one param function, including implementation, that a model can be given access to in order to gain info or complete tasks.  

|                                                                                               See also                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| [defineFunction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/package-summary#defineFunction(kotlin.String,kotlin.String,kotlin.coroutines.SuspendFunction0)) | for how to create an instance of this class. |

## Summary

|                                                                                             ### Public functions                                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `open suspend `[JSONObject](https://developer.android.com/reference/kotlin/org/json/JSONObject.html)                                                                                                         | [execute](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/OneParameterFunction#execute(com.google.firebase.vertexai.type.FunctionCallPart))`(part: `[FunctionCallPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart)`)` Run the attached function with the provided [arguments](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/OneParameterFunction#execute(com.google.firebase.vertexai.type.FunctionCallPart)). |
| `open `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema)`<T>>` | [getParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/OneParameterFunction#getParameters())`()` The parameters of the attached function as a list of [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema).                                                                                                                                                                                                                                           |

|                                           ### Public properties                                           |
|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| `suspend (T) `->` `[JSONObject](https://developer.android.com/reference/kotlin/org/json/JSONObject.html)  | [function](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/OneParameterFunction#function()) |
| [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema)`<T>` | [param](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/OneParameterFunction#param())       |

|                                                                                                                                                                                                                                                                                                                                                                                                                 ### Inherited properties                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [com.google.firebase.vertexai.type.FunctionDeclaration](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionDeclaration) |----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------| | [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [description](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionDeclaration#description()) | | [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [name](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionDeclaration#name())               | |

## Public functions

### execute

```
openÂ suspendÂ funÂ execute(part:Â FunctionCallPart):Â JSONObject
```

Run the attached function with the provided [arguments](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/OneParameterFunction#execute(com.google.firebase.vertexai.type.FunctionCallPart)).  

### getParameters

```
openÂ funÂ getParameters():Â List<Schema<T>>
```

The parameters of the attached function as a list of [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema).  

## Public properties

### function

```
valÂ function:Â suspendÂ (T) -> JSONObject
```  

### param

```
valÂ param:Â Schema<T>
```