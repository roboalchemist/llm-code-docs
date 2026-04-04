# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Logger.Level.md.txt

# Logger.Level

# Logger.Level


```
enum Logger.Level
```

<br />

*** ** * ** ***

The log levels used by the Realtime Database library

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Logger.Level#DEBUG` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Logger.Level#ERROR` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Logger.Level#INFO` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Logger.Level#NONE` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Logger.Level#WARN` |   |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Logger.Level!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Logger.Level#valueOf(java.lang.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!)` Returns the enum constant of this type with the specified name. |
| `java-static https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Logger.Level!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Logger.Level#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### DEBUG

```
val Logger.Level.DEBUG: Logger.Level
```

### ERROR

```
val Logger.Level.ERROR: Logger.Level
```

### INFO

```
val Logger.Level.INFO: Logger.Level
```

### NONE

```
val Logger.Level.NONE: Logger.Level
```

### WARN

```
val Logger.Level.WARN: Logger.Level
```

## Public functions

### valueOf

```
java-static fun valueOf(name: String!): Logger.Level!
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Logger.Level!` | the enum constant with the specified name |

| Throws |
|---|---|
| `java.lang.IllegalArgumentException: https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html` | if this enum type has no constant with the specified name |

### values

```
java-static fun values(): Array<Logger.Level!>!
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Logger.Level!>!` | an array containing the constants of this enum type, in the order they're declared |