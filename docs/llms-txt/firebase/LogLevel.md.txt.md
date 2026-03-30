# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LogLevel.md.txt

# LogLevel

# LogLevel


```
enum LogLevel : Enum
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [kotlin.Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html) ||
|   | ↳ | [com.google.firebase.dataconnect.LogLevel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LogLevel) |

*** ** * ** ***

The log levels supported by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.FirebaseDataConnect.Companion).logLevel()` |   |

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LogLevel#DEBUG` | Log all messages, including detailed debug logs. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LogLevel#NONE` | Do not log anything. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LogLevel#WARN` | Only log warnings and errors; this is the default log level. |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LogLevel` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LogLevel#valueOf(kotlin.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the enum constant of this type with the specified name. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LogLevel>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LogLevel#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### DEBUG

```
val LogLevel.DEBUG: LogLevel
```

Log all messages, including detailed debug logs.

### NONE

```
val LogLevel.NONE: LogLevel
```

Do not log anything.

### WARN

```
val LogLevel.WARN: LogLevel
```

Only log warnings and errors; this is the default log level.

## Public functions

### valueOf

```
fun valueOf(value: String): LogLevel
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Throws |
|---|---|
| `kotlin.IllegalArgumentException: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html` | if this enum type has no constant with the specified name |

### values

```
fun values(): Array<LogLevel>
```

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.