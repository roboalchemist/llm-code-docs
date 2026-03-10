# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ServerValue.md.txt

# ServerValue

# ServerValue


```
class ServerValue
```

<br />

*** ** * ** ***

Contains placeholder values to use when writing data to the Firebase Database.

## Summary

| ### Constants |
|---|---|
| `const (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ServerValue#TIMESTAMP()` A placeholder value for auto-populating the current timestamp (time since the Unix epoch, in milliseconds) by the Firebase Database servers. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ServerValue#ServerValue()()` |

| ### Public functions |
|---|---|
| `java-static https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ServerValue#increment(long)(delta: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Returns a placeholder value that can be used to atomically increment the current database value by the provided delta. |
| `java-static https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/ServerValue#increment(double)(delta: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)` Returns a placeholder value that can be used to atomically increment the current database value by the provided delta. |

## Constants

### TIMESTAMP

```
const val TIMESTAMP: (Mutable)Map<String!, String!>
```

A placeholder value for auto-populating the current timestamp (time since the Unix epoch, in milliseconds) by the Firebase Database servers.

## Public constructors

### ServerValue

```
ServerValue()
```

## Public functions

### increment

```
java-static fun increment(delta: Long): Any
```

Returns a placeholder value that can be used to atomically increment the current database value by the provided delta.

The delta must be an long or a double value. If the current value is not a number, or if the database value does not yet exist, the transformation will set the database value to the delta value. If either the delta value or the existing value are doubles, both values will be interpreted as doubles. Double arithmetic and representation of double values follow IEEE 754 semantics. If there is positive/negative integer overflow, the sum is calculated as a double.

| Parameters |
|---|---|
| `delta: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the amount to modify the current value atomically. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | a placeholder value for modifying data atomically server-side. |

### increment

```
java-static fun increment(delta: Double): Any
```

Returns a placeholder value that can be used to atomically increment the current database value by the provided delta.

The delta must be an long or a double value. If the current value is not an integer or double, or if the data does not yet exist, the transformation will set the data to the delta value. If either of the delta value or the existing data are doubles, both values will be interpreted as doubles. Double arithmetic and representation of double values follow IEEE 754 semantics. If there is positive/negative integer overflow, the sum is calculated as a a double.

| Parameters |
|---|---|
| `delta: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` | the amount to modify the current value atomically. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | a placeholder value for modifying data atomically server-side. |