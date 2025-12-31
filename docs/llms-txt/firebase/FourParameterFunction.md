# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FourParameterFunction.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FourParameterFunction.md.txt

# FourParameterFunction

# FourParameterFunction


```
public final class FourParameterFunction<TÂ extendsÂ Object,Â UÂ extendsÂ Object,Â VÂ extendsÂ Object,Â WÂ extendsÂ Object> extends FunctionDeclaration
```

<br />

|---|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)                                                                                    |||
| â³ | [com.google.firebase.vertexai.type.FunctionDeclaration](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionDeclaration)        ||
|   | â³ | [com.google.firebase.vertexai.type.FourParameterFunction](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FourParameterFunction) |

*** ** * ** ***

A declared four param function, including implementation, that a model can be given access to in order to gain info or complete tasks.  

|                                                                                               See also                                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| [defineFunction](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/package-summary#defineFunction(kotlin.String,kotlin.String,kotlin.coroutines.SuspendFunction0)) | for how to create an instance of this class. |

## Summary

|                                                                                                                                                                                                                                                                                                                                                                                                  ### Public fields                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[SuspendFunction4](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.coroutines/-suspend-function4/index.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` T, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` U, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` V, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` W, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[JSONObject](https://developer.android.com/reference/kotlin/org/json/JSONObject.html)`>` | [function](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FourParameterFunction#function()) |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` T>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [param1](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FourParameterFunction#param1())     |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` U>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [param2](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FourParameterFunction#param2())     |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` V>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [param3](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FourParameterFunction#param3())     |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` W>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [param4](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FourParameterFunction#param4())     |

|                                                                                                                                                                                                                          ### Public methods                                                                                                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[JSONObject](https://developer.android.com/reference/kotlin/org/json/JSONObject.html)                                                                                                                                                                                                                                                                                 | [execute](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FourParameterFunction#execute(com.google.firebase.vertexai.type.FunctionCallPart))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FunctionCallPart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallPart)` part)` Run the attached function with the provided [arguments](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FourParameterFunction#execute(com.google.firebase.vertexai.type.FunctionCallPart)). |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema)`<`[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`>>` | [getParameters](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FourParameterFunction#getParameters())`()` The parameters of the attached function as a list of [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema).                                                                                                                                                                                                                                                                                                                                          |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ### Inherited fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [com.google.firebase.vertexai.type.FunctionDeclaration](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionDeclaration) |--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------| | `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html) | [description](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionDeclaration#description()) | | `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html) | [name](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionDeclaration#name())               | |

## Public fields

### function

```
publicÂ finalÂ @NonNull SuspendFunction4<@NonNull T,Â @NonNull U,Â @NonNull V,Â @NonNull W,Â @NonNull JSONObject>Â function
```  

### param1

```
publicÂ finalÂ @NonNull Schema<@NonNull T>Â param1
```  

### param2

```
publicÂ finalÂ @NonNull Schema<@NonNull U>Â param2
```  

### param3

```
publicÂ finalÂ @NonNull Schema<@NonNull V>Â param3
```  

### param4

```
publicÂ finalÂ @NonNull Schema<@NonNull W>Â param4
```  

## Public methods

### execute

```
publicÂ @NonNull JSONObjectÂ execute(@NonNull FunctionCallPartÂ part)
```

Run the attached function with the provided [arguments](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FourParameterFunction#execute(com.google.firebase.vertexai.type.FunctionCallPart)).  

### getParameters

```
publicÂ @NonNull List<@NonNull Schema<Object>>Â getParameters()
```

The parameters of the attached function as a list of [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema).