# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.md.txt

# EnumValue

# EnumValue


```
interface EnumValue<T : Enum<T>>
```

<br />

Known direct subclasses [EnumValue.Known](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known), [EnumValue.Unknown](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Unknown)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known` | Represents a known enum value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Unknown` | Represents an unknown enum value. |

*** ** * ** ***

Stores the value of an `enum` or a string if the string does not correspond to one of the enum's values.

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html<T>> : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue` Represents a known enum value. |
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Unknown : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue` Represents an unknown enum value. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue#stringValue()` The string value of the enum, either the `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/name.html` of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known#value()` in the case of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known` or the `stringValue` given to the constructor in the case of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Unknown`. |
| `T?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue#value()` `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known#value()` in the case of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known`, or `null` in the case of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Unknown`. |

## Public properties

### stringValue

```
val stringValue: String
```

The string value of the enum, either the `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/name.html` of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known#value()` in the case of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known` or the `stringValue` given to the constructor in the case of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Unknown`.

### value

```
val value: T?
```

`https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known#value()` in the case of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known`, or `null` in the case of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Unknown`.