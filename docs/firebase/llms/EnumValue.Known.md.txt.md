# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known.md.txt

# EnumValue.Known

# EnumValue.Known


```
class EnumValue.Known<T : Enum<T>> : EnumValue
```

<br />

*** ** * ** ***

Represents a known enum value.

## Summary

| ### Public constructors |
|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html<T>> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known#Known(kotlin.Enum)(value: T)` |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known<T>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known#copy(kotlin.Enum)(value: T)` Creates and returns a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known` instance with the given property values. |
| `open operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known#equals(kotlin.Any)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Compares this object with another object for equality. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known#hashCode()()` Calculates and returns the hash code for this object. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known#toString()()` Returns a string representation of this object, useful for debugging. |

| ### Public properties |
|---|---|
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known#stringValue()` `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/name.html` of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known#value()`. |
| `open T` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known#value()` The enum value wrapped by this object. |

## Public constructors

### Known

```
<T : Enum<T>> Known(value: T)
```

| Parameters |
|---|---|
| `value: T` | The enum value. |

## Public functions

### copy

```
fun copy(value: T = this.value): EnumValue.Known<T>
```

Creates and returns a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known` instance with the given property values.

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
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | true if, and only if, the other object is an instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known` whose `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known#value()` compares equal to this object's `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known#value()` using the `==` operator. |

### hashCode

```
open fun hashCode(): Int
```

Calculates and returns the hash code for this object.

The hash code is *not* guaranteed to be stable across application restarts.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | the hash code for this object, that incorporates the values of this object's public properties. |

### toString

```
open fun toString(): String
```

Returns a string representation of this object, useful for debugging.

The string representation is *not* guaranteed to be stable and may change without notice at any time. Therefore, the only recommended usage of the returned string is debugging and/or logging. Namely, parsing the returned string or storing the returned string in non-volatile storage should generally be avoided in order to be robust in case that the string representation changes.

## Public properties

### stringValue

```
open val stringValue: String
```

`https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/name.html` of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known#value()`.

### value

```
open val value: T
```

The enum value wrapped by this object.