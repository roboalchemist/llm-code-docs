# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockThreshold.md.txt

# BlockThreshold

# BlockThreshold


```
enum BlockThreshold : Enum
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [kotlin.Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html) ||
|   | ↳ | [com.google.firebase.vertexai.type.BlockThreshold](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockThreshold) |

*** ** * ** ***

Represents the threshold for some `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/HarmCategory` that is allowed and blocked by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/SafetySetting`.

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockThreshold#LOW_AND_ABOVE` | Content with negligible harm is allowed. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockThreshold#MEDIUM_AND_ABOVE` | Content with negligible to low harm is allowed. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockThreshold#NONE` | All content is allowed regardless of harm. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockThreshold#ONLY_HIGH` | Content with negligible to medium harm is allowed. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockThreshold#UNSPECIFIED` | The threshold was not specified. |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockThreshold` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockThreshold#valueOf(kotlin.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the enum constant of this type with the specified name. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockThreshold>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/BlockThreshold#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### LOW_AND_ABOVE

```
val BlockThreshold.LOW_AND_ABOVE: BlockThreshold
```

Content with negligible harm is allowed.

### MEDIUM_AND_ABOVE

```
val BlockThreshold.MEDIUM_AND_ABOVE: BlockThreshold
```

Content with negligible to low harm is allowed.

### NONE

```
val BlockThreshold.NONE: BlockThreshold
```

All content is allowed regardless of harm.

### ONLY_HIGH

```
val BlockThreshold.ONLY_HIGH: BlockThreshold
```

Content with negligible to medium harm is allowed.

### UNSPECIFIED

```
val BlockThreshold.UNSPECIFIED: BlockThreshold
```

The threshold was not specified.

## Public functions

### valueOf

```
fun valueOf(value: String): BlockThreshold
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Throws |
|---|---|
| `kotlin.IllegalArgumentException: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html` | if this enum type has no constant with the specified name |

### values

```
fun values(): Array<BlockThreshold>
```

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.