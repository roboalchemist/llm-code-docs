# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Unknown.md.txt

# EnumValue.Unknown

# EnumValue.Unknown


```
class EnumValue.Unknown : EnumValue
```

<br />

*** ** * ** ***

Represents an unknown enum value.

This could happen, for example, if an enum gained a new value but this code was compiled for the older version that lacked the new enum value. Instead of failing, the unknown enum value will be gracefully mapped to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Unknown`.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Unknown#Unknown(kotlin.String)(stringValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Unknown` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Unknown#copy(kotlin.String)(stringValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates and returns a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Unknown` instance with the given property values. |
| `open operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Unknown#equals(kotlin.Any)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Compares this object with another object for equality. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Unknown#hashCode()()` Calculates and returns the hash code for this object. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Unknown#toString()()` Returns a string representation of this object, useful for debugging. |

| ### Public properties |
|---|---|
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Unknown#stringValue()` The unknown string value. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-nothing/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Unknown#value()` Always `null`. |

## Public constructors

### Unknown

```
Unknown(stringValue: String)
```

## Public functions

### copy

```
fun copy(stringValue: String = this.stringValue): EnumValue.Unknown
```

Creates and returns a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Unknown` instance with the given property values.

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
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | true if, and only if, the other object is an instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Unknown` whose `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Unknown#stringValue()` compares equal to this object's `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Unknown#stringValue()` using the `==` operator. |

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

The unknown string value.

### value

```
open val value: Nothing?
```

Always `null`.