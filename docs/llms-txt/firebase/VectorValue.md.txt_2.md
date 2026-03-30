# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue.md.txt

# VectorValue

# VectorValue


```
class VectorValue
```

<br />

*** ** * ** ***

Represent a vector type in Firestore documents. Create an instance with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue#vector(double[])`.

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue#equals(java.lang.Object)(obj: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!)` Returns true if this VectorValue is equal to the provided object. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue#hashCode()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue#toArray()()` Returns a representation of the vector as an array of doubles. |

## Public functions

### equals

```
fun equals(obj: Any!): Boolean
```

Returns true if this VectorValue is equal to the provided object.

| Parameters |
|---|---|
| `obj: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!` | The object to compare against. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | Whether this VectorValue is equal to the provided object. |

### hashCode

```
fun hashCode(): Int
```

### toArray

```
fun toArray(): DoubleArray<Double>
```

Returns a representation of the vector as an array of doubles.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html>` | A representation of the vector as an array of doubles |