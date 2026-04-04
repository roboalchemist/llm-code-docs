# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode.md.txt

# FunctionCallingConfig.Mode

# FunctionCallingConfig.Mode


```
enum FunctionCallingConfig.Mode : Enum
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [kotlin.Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html) ||
|   | ↳ | [com.google.firebase.vertexai.type.FunctionCallingConfig.Mode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode) |

*** ** * ** ***

Configuration for dictating when the model should call the attached function.

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode#ANY` | The model always predicts a provided function call to answer every query. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode#AUTO` | The default behavior for function calling. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode#NONE` | The model will never predict a function call to answer a query. |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode#valueOf(kotlin.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the enum constant of this type with the specified name. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### ANY

```
val FunctionCallingConfig.Mode.ANY: FunctionCallingConfig.Mode
```

The model always predicts a provided function call to answer every query.

### AUTO

```
val FunctionCallingConfig.Mode.AUTO: FunctionCallingConfig.Mode
```

The default behavior for function calling. The model calls functions to answer queries at its discretion

### NONE

```
val FunctionCallingConfig.Mode.NONE: FunctionCallingConfig.Mode
```

The model will never predict a function call to answer a query. This can also be achieved by not passing any tools to the model.

## Public functions

### valueOf

```
fun valueOf(value: String): FunctionCallingConfig.Mode
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Throws |
|---|---|
| `kotlin.IllegalArgumentException: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html` | if this enum type has no constant with the specified name |

### values

```
fun values(): Array<FunctionCallingConfig.Mode>
```

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.