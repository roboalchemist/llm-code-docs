# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockThreshold.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockThreshold.md.txt

# BlockThreshold

# BlockThreshold


```
enum BlockThreshold : Enum
```

<br />

|---|---|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                            |||
| â³ | [kotlin.Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)                                                                       ||
|   | â³ | [com.google.firebase.vertexai.type.BlockThreshold](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockThreshold) |

*** ** * ** ***

Represents the threshold for some [HarmCategory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmCategory) that is allowed and blocked by [SafetySetting](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetySetting).

## Summary

|                                                             ### Enum Values                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| [LOW_AND_ABOVE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockThreshold#LOW_AND_ABOVE)       | Content with negligible harm is allowed.           |
| [MEDIUM_AND_ABOVE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockThreshold#MEDIUM_AND_ABOVE) | Content with negligible to low harm is allowed.    |
| [NONE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockThreshold#NONE)                         | All content is allowed regardless of harm.         |
| [ONLY_HIGH](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockThreshold#ONLY_HIGH)               | Content with negligible to medium harm is allowed. |
| [UNSPECIFIED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockThreshold#UNSPECIFIED)           | The threshold was not specified.                   |

|                                                                                           ### Public functions                                                                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [BlockThreshold](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockThreshold)                                                                                     | [valueOf](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockThreshold#valueOf(kotlin.String))`(value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns the enum constant of this type with the specified name. |
| [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[BlockThreshold](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockThreshold)`>` | [values](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockThreshold#values())`()` Returns an array containing the constants of this enum type, in the order they're declared.                                                                             |

## Enum Values

### LOW_AND_ABOVE

```
valÂ BlockThreshold.LOW_AND_ABOVE:Â BlockThreshold
```

Content with negligible harm is allowed.  

### MEDIUM_AND_ABOVE

```
valÂ BlockThreshold.MEDIUM_AND_ABOVE:Â BlockThreshold
```

Content with negligible to low harm is allowed.  

### NONE

```
valÂ BlockThreshold.NONE:Â BlockThreshold
```

All content is allowed regardless of harm.  

### ONLY_HIGH

```
valÂ BlockThreshold.ONLY_HIGH:Â BlockThreshold
```

Content with negligible to medium harm is allowed.  

### UNSPECIFIED

```
valÂ BlockThreshold.UNSPECIFIED:Â BlockThreshold
```

The threshold was not specified.  

## Public functions

### valueOf

```
funÂ valueOf(value:Â String):Â BlockThreshold
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)  

|                                                                              Throws                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| `kotlin.IllegalArgumentException: `[kotlin.IllegalArgumentException](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html) | if this enum type has no constant with the specified name |

### values

```
funÂ values():Â Array<BlockThreshold>
```

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.