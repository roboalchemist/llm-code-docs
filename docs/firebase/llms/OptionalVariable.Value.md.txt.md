# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Value.md.txt

# OptionalVariable.Value

# OptionalVariable.Value


```
class OptionalVariable.Value<T : Any?> : OptionalVariable
```

<br />

*** ** * ** ***

An implementation of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable` representing a "defined" value.

This value will be *included* in the serial form, even if the value is `null`.

## Summary

| ### Public constructors |
|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Value#Value(kotlin.Any)(value: T)` |

| ### Public functions |
|---|---|
| `open operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Value#equals(kotlin.Any)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Compares this object with another object for equality. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Value#hashCode()()` Returns the hash code of the encapsulated value, or `0` if the encapsulated value is `null`. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Value#toString()()` Returns the `https://developer.android.com/reference/kotlin/java/lang/Object.html` result of the encapsulated value, or `"null"` if the encapsulated value is `null`. |
| `open T` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Value#valueOrNull()()` Returns the value encapsulated by this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable`, which *may* be `null`. |
| `open T` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Value#valueOrThrow()()` Returns the value encapsulated by this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable`, which *may* be `null`, but never throws an exception. |

| ### Public properties |
|---|---|
| `T` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Value#value()` the value encapsulated by this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable`. |

## Public constructors

### Value

```
<T : Any?> Value(value: T)
```

## Public functions

### equals

```
open operator fun equals(other: Any?): Boolean
```

Compares this object with another object for equality.

| Parameters |
|---|---|
| `other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The object to compare to this for equality. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | true if, and only if, the other object is an instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Value` whose encapsulated value compares equal to this object's encapsulated value using the `==` operator. |

### hashCode

```
open fun hashCode(): Int
```

Returns the hash code of the encapsulated value, or `0` if the encapsulated value is `null`.

### toString

```
open fun toString(): String
```

Returns the `https://developer.android.com/reference/kotlin/java/lang/Object.html` result of the encapsulated value, or `"null"` if the encapsulated value is `null`.

The string representation is *not* guaranteed to be stable and may change without notice at any time. Therefore, the only recommended usage of the returned string is debugging and/or logging. Namely, parsing the returned string or storing the returned string in non-volatile storage should generally be avoided in order to be robust in case that the string representation changes.

### valueOrNull

```
open fun valueOrNull(): T
```

Returns the value encapsulated by this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable`, which *may* be `null`.

### valueOrThrow

```
open fun valueOrThrow(): T
```

Returns the value encapsulated by this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable`, which *may* be `null`, but never throws an exception.

## Public properties

### value

```
val value: T
```

the value encapsulated by this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable`.