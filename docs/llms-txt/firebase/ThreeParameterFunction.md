# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/ThreeParameterFunction.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ThreeParameterFunction.md.txt

# ThreeParameterFunction

# ThreeParameterFunction


```
class ThreeParameterFunction<TÂ :Â Any?,Â UÂ :Â Any?,Â VÂ :Â Any?> : FunctionDeclaration
```

<br />

|---|---|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                                            |||
| â³ | [com.google.firebase.vertexai.type.FunctionDeclaration](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionDeclaration)          ||
|   | â³ | [com.google.firebase.vertexai.type.ThreeParameterFunction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ThreeParameterFunction) |

*** ** * ** ***

A declared three param function, including implementation, that a model can be given access to in order to gain info or complete tasks.  

|                                                                                               See also                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| [defineFunction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/package-summary#defineFunction(kotlin.String,kotlin.String,kotlin.coroutines.SuspendFunction0)) | for how to create an instance of this class. |

## Summary

|                                                                                                                                   ### Public functions                                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `open suspend `[JSONObject](https://developer.android.com/reference/kotlin/org/json/JSONObject.html)                                                                                                                                                                                     | [execute](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ThreeParameterFunction#execute(com.google.firebase.vertexai.type.FunctionCallPart))`(part: `[FunctionCallPart](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallPart)`)` Run the attached function with the provided [arguments](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ThreeParameterFunction#execute(com.google.firebase.vertexai.type.FunctionCallPart)). |
| `open `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?>>` | [getParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ThreeParameterFunction#getParameters())`()` The parameters of the attached function as a list of [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema).                                                                                                                                                                                                                                             |

|                                             ### Public properties                                              |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| `suspend (T, U, V) `->` `[JSONObject](https://developer.android.com/reference/kotlin/org/json/JSONObject.html) | [function](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ThreeParameterFunction#function()) |
| [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema)`<T>`      | [param1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ThreeParameterFunction#param1())     |
| [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema)`<U>`      | [param2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ThreeParameterFunction#param2())     |
| [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema)`<V>`      | [param3](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ThreeParameterFunction#param3())     |

|                                                                                                                                                                                                                                                                                                                                                                                                                 ### Inherited properties                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [com.google.firebase.vertexai.type.FunctionDeclaration](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionDeclaration) |----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------| | [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [description](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionDeclaration#description()) | | [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [name](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionDeclaration#name())               | |

## Public functions

### execute

```
openÂ suspendÂ funÂ execute(part:Â FunctionCallPart):Â JSONObject
```

Run the attached function with the provided [arguments](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/ThreeParameterFunction#execute(com.google.firebase.vertexai.type.FunctionCallPart)).  

### getParameters

```
openÂ funÂ getParameters():Â List<Schema<Any?>>
```

The parameters of the attached function as a list of [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema).  

## Public properties

### function

```
valÂ function:Â suspendÂ (T, U, V) -> JSONObject
```  

### param1

```
valÂ param1:Â Schema<T>
```  

### param2

```
valÂ param2:Â Schema<U>
```  

### param3

```
valÂ param3:Â Schema<V>
```