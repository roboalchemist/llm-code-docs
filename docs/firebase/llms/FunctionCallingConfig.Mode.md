# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode.md.txt

# FunctionCallingConfig.Mode

# FunctionCallingConfig.Mode


```
public enum FunctionCallingConfig.Mode extends Enum
```

<br />

|---|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)                                                                                              |||
| â³ | [kotlin.Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)                                                                                                ||
|   | â³ | [com.google.firebase.vertexai.type.FunctionCallingConfig.Mode](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode) |

*** ** * ** ***

Configuration for dictating when the model should call the attached function.

## Summary

|                                                       ### Enum Values                                                        |
|------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| [ANY](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode#ANY)   | The model always predicts a provided function call to answer every query. |
| [AUTO](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode#AUTO) | The default behavior for function calling.                                |
| [NONE](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode#NONE) | The model will never predict a function call to answer a query.           |

|                                                                                                                 ### Public methods                                                                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FunctionCallingConfig.Mode](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode) | [valueOf](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode#valueOf(kotlin.String))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` value)` Returns the enum constant of this type with the specified name. |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` FunctionCallingConfig.Mode[]`                                                                                                                  | [values](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode#values())`()` Returns an array containing the constants of this enum type, in the order they're declared.                                                                                                                                                                        |

## Enum Values

### ANY

```
FunctionCallingConfig.ModeÂ FunctionCallingConfig.Mode.ANY
```

The model always predicts a provided function call to answer every query.  

### AUTO

```
FunctionCallingConfig.ModeÂ FunctionCallingConfig.Mode.AUTO
```

The default behavior for function calling. The model calls functions to answer queries at its discretion  

### NONE

```
FunctionCallingConfig.ModeÂ FunctionCallingConfig.Mode.NONE
```

The model will never predict a function call to answer a query. This can also be achieved by not passing any tools to the model.  

## Public methods

### valueOf

```
publicÂ finalÂ @NonNull FunctionCallingConfig.ModeÂ valueOf(@NonNull StringÂ value)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)  

|                                                                             Throws                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| [kotlin.IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html)` kotlin.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
publicÂ finalÂ @NonNull FunctionCallingConfig.Mode[]Â values()
```

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.