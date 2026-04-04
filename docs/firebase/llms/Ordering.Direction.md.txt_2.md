# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering.Direction.md.txt

# Ordering.Direction

# Ordering.Direction


```
enum Ordering.Direction : Enum
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [kotlin.Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html) ||
|   | ↳ | [com.google.firebase.firestore.pipeline.Ordering.Direction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering.Direction) |

*** ** * ** ***

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering.Direction#ASCENDING` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering.Direction#DESCENDING` |   |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering.Direction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering.Direction#valueOf(kotlin.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the enum constant of this type with the specified name. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering.Direction>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering.Direction#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/[JVM root]/<Error class: unknown class>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering.Direction#proto()` |

## Enum Values

### ASCENDING

```
val Ordering.Direction.ASCENDING: Ordering.Direction
```

### DESCENDING

```
val Ordering.Direction.DESCENDING: Ordering.Direction
```

## Public functions

### valueOf

```
fun valueOf(value: String): Ordering.Direction
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Throws |
|---|---|
| `kotlin.IllegalArgumentException: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html` | if this enum type has no constant with the specified name |

### values

```
fun values(): Array<Ordering.Direction>
```

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.

## Public properties

### proto

```
val proto: <Error class: unknown class>
```