# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Extensions/VectorValue.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue.md.txt

# VectorValue

# VectorValue


```
public class VectorValue
```

<br />

*** ** * ** ***

Represent a vector type in Firestore documents. Create an instance with [vector](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue#vector(double[])).

## Summary

|                                            ### Public methods                                            |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `boolean`                                                                                                | [equals](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue#equals(java.lang.Object))`(`[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)` obj)` Returns true if this VectorValue is equal to the provided object. |
| `int`                                                                                                    | [hashCode](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue#hashCode())`()`                                                                                                                                                                   |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` double[]` | [toArray](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue#toArray())`()` Returns a representation of the vector as an array of doubles.                                                                                                      |

## Public methods

### equals

```
publicÂ booleanÂ equals(ObjectÂ obj)
```

Returns true if this VectorValue is equal to the provided object.  

|                                      Parameters                                      |
|--------------------------------------------------------------------------------------|--------------------------------|
| [Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)` obj` | The object to compare against. |

|  Returns  |
|-----------|-----------------------------------------------------------|
| `boolean` | Whether this VectorValue is equal to the provided object. |

### hashCode

```
publicÂ intÂ hashCode()
```  

### toArray

```
publicÂ @NonNull double[]Â toArray()
```

Returns a representation of the vector as an array of doubles.  

|                                                 Returns                                                  |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` double[]` | A representation of the vector as an array of doubles |