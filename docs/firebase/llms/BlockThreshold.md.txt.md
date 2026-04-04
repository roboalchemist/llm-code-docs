# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockThreshold.md.txt

# BlockThreshold

# BlockThreshold


```
public enum BlockThreshold extends Enum
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [kotlin.Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html) ||
|   | ↳ | [com.google.firebase.vertexai.type.BlockThreshold](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockThreshold) |

*** ** * ** ***

Represents the threshold for some `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/HarmCategory` that is allowed and blocked by `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/SafetySetting`.

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockThreshold#LOW_AND_ABOVE` | Content with negligible harm is allowed. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockThreshold#MEDIUM_AND_ABOVE` | Content with negligible to low harm is allowed. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockThreshold#NONE` | All content is allowed regardless of harm. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockThreshold#ONLY_HIGH` | Content with negligible to medium harm is allowed. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockThreshold#UNSPECIFIED` | The threshold was not specified. |

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockThreshold` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockThreshold#valueOf(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html value)` Returns the enum constant of this type with the specified name. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html BlockThreshold[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/BlockThreshold#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### LOW_AND_ABOVE

```
BlockThreshold BlockThreshold.LOW_AND_ABOVE
```

Content with negligible harm is allowed.

### MEDIUM_AND_ABOVE

```
BlockThreshold BlockThreshold.MEDIUM_AND_ABOVE
```

Content with negligible to low harm is allowed.

### NONE

```
BlockThreshold BlockThreshold.NONE
```

All content is allowed regardless of harm.

### ONLY_HIGH

```
BlockThreshold BlockThreshold.ONLY_HIGH
```

Content with negligible to medium harm is allowed.

### UNSPECIFIED

```
BlockThreshold BlockThreshold.UNSPECIFIED
```

The threshold was not specified.

## Public methods

### valueOf

```
public final @NonNull BlockThreshold valueOf(@NonNull String value)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Throws |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html kotlin.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
public final @NonNull BlockThreshold[] values()
```

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.