# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue.md.txt

# VectorValue

# VectorValue


```
public class VectorValue
```

<br />

*** ** * ** ***

Represent a vector type in Firestore documents. Create an instance with `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue#vector(double[])`.

## Summary

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue#equals(java.lang.Object)(https://developer.android.com/reference/kotlin/java/lang/Object.html obj)` Returns true if this VectorValue is equal to the provided object. |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue#hashCode()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html double[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue#toArray()()` Returns a representation of the vector as an array of doubles. |

## Public methods

### equals

```
public boolean equals(Object obj)
```

Returns true if this VectorValue is equal to the provided object.

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/Object.html obj` | The object to compare against. |

| Returns |
|---|---|
| `boolean` | Whether this VectorValue is equal to the provided object. |

### hashCode

```
public int hashCode()
```

### toArray

```
public @NonNull double[] toArray()
```

Returns a representation of the vector as an array of doubles.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html double[]` | A representation of the vector as an array of doubles |