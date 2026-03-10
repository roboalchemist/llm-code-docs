# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/Logger.Level.md.txt

# Logger.Level

# Logger.Level


```
public enum Logger.Level
```

<br />

*** ** * ** ***

The log levels used by the Realtime Database library

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Logger.Level#DEBUG` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Logger.Level#ERROR` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Logger.Level#INFO` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Logger.Level#NONE` |   |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Logger.Level#WARN` |   |

| ### Public methods |
|---|---|
| `static https://firebase.google.com/docs/reference/android/com/google/firebase/database/Logger.Level` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Logger.Level#valueOf(java.lang.String)(https://developer.android.com/reference/kotlin/java/lang/String.html name)` Returns the enum constant of this type with the specified name. |
| `static Logger.Level[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Logger.Level#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### DEBUG

```
Logger.Level Logger.Level.DEBUG
```

### ERROR

```
Logger.Level Logger.Level.ERROR
```

### INFO

```
Logger.Level Logger.Level.INFO
```

### NONE

```
Logger.Level Logger.Level.NONE
```

### WARN

```
Logger.Level Logger.Level.WARN
```

## Public methods

### valueOf

```
public static Logger.Level valueOf(String name)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Logger.Level` | the enum constant with the specified name |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html java.lang.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
public static Logger.Level[] values()
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `Logger.Level[]` | an array containing the constants of this enum type, in the order they're declared |