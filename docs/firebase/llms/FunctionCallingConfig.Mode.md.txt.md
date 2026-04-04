# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode.md.txt

# FunctionCallingConfig.Mode

# FunctionCallingConfig.Mode


```
public enum FunctionCallingConfig.Mode extends Enum
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [kotlin.Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html) ||
|   | ↳ | [com.google.firebase.vertexai.type.FunctionCallingConfig.Mode](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode) |

*** ** * ** ***

Configuration for dictating when the model should call the attached function.

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode#ANY` | The model always predicts a provided function call to answer every query. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode#AUTO` | The default behavior for function calling. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode#NONE` | The model will never predict a function call to answer a query. |

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode#valueOf(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html value)` Returns the enum constant of this type with the specified name. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html FunctionCallingConfig.Mode[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionCallingConfig.Mode#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### ANY

```
FunctionCallingConfig.Mode FunctionCallingConfig.Mode.ANY
```

The model always predicts a provided function call to answer every query.

### AUTO

```
FunctionCallingConfig.Mode FunctionCallingConfig.Mode.AUTO
```

The default behavior for function calling. The model calls functions to answer queries at its discretion

### NONE

```
FunctionCallingConfig.Mode FunctionCallingConfig.Mode.NONE
```

The model will never predict a function call to answer a query. This can also be achieved by not passing any tools to the model.

## Public methods

### valueOf

```
public final @NonNull FunctionCallingConfig.Mode valueOf(@NonNull String value)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Throws |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html kotlin.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
public final @NonNull FunctionCallingConfig.Mode[] values()
```

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.