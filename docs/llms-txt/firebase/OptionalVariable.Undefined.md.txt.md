# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Undefined.md.txt

# OptionalVariable.Undefined

# OptionalVariable.Undefined


```
object OptionalVariable.Undefined : OptionalVariable
```

<br />

*** ** * ** ***

An implementation of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable` representing an "undefined" value.

This value will be excluded entirely from the serial form.

## Summary

| ### Public functions |
|---|---|
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Undefined#toString()()` Returns a string representation of this object, useful for debugging. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-nothing/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Undefined#valueOrNull()()` Unconditionally returns `null`. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-nothing/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Undefined#valueOrThrow()()` Unconditionally throws an exception. |

## Public functions

### toString

```
open fun toString(): String
```

Returns a string representation of this object, useful for debugging.

The string representation is *not* guaranteed to be stable and may change without notice at any time. Therefore, the only recommended usage of the returned string is debugging and/or logging. Namely, parsing the returned string or storing the returned string in non-volatile storage should generally be avoided in order to be robust in case that the string representation changes.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | a string representation of this object. |

### valueOrNull

```
open fun valueOrNull(): Nothing?
```

Unconditionally returns `null`.

### valueOrThrow

```
open fun valueOrThrow(): Nothing
```

Unconditionally throws an exception.