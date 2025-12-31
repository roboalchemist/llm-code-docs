# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Extensions/FieldValue.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Extensions/FirebaseFirestore/FieldValue.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldValue.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Extensions/FirebaseFirestore/FieldValue.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldValue.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue.md.txt

# FieldValue

# FieldValue


```
abstract class FieldValue
```

<br />

*** ** * ** ***

Sentinel values that can be used when writing document fields with `set()` or `
update()`.

## Summary

|                                                   ### Public functions                                                   |
|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java-static `[FieldValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue)   | [arrayRemove](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue#arrayRemove(java.lang.Object...))`(elements: `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>!)` Returns a special value that can be used with `set()` or `update()` that tells the server to remove the given elements from any array value that already exists on the server. |
| `java-static `[FieldValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue)   | [arrayUnion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue#arrayUnion(java.lang.Object...))`(elements: `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>!)` Returns a special value that can be used with `set()` or `update()` that tells the server to union the given elements with any array value that already exists on the server.    |
| `java-static `[FieldValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue)   | [delete](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue#delete())`()` Returns a sentinel for use with `update()` to mark a field for deletion.                                                                                                                                                                                                                                                                                                              |
| `java-static `[FieldValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue)   | [increment](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue#increment(long))`(l: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)`)` Returns a special value that can be used with `set()` or `update()` that tells the server to increment the field's current value by the given value.                                                                                                                                       |
| `java-static `[FieldValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue)   | [increment](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue#increment(double))`(l: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`)` Returns a special value that can be used with `set()` or `update()` that tells the server to increment the field's current value by the given value.                                                                                                                                 |
| `java-static `[FieldValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue)   | [serverTimestamp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue#serverTimestamp())`()` Returns a sentinel for use with `set()` or `update()` to include a server-generated timestamp in the written data.                                                                                                                                                                                                                                                  |
| `java-static `[VectorValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue) | [vector](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue#vector(double[]))`(values: `[DoubleArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html)`)` Creates a new [VectorValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue) constructed with a copy of the given array of doubles.                                                                                          |

## Public functions

### arrayRemove

```
java-staticÂ funÂ arrayRemove(elements:Â Array<Any!>!):Â FieldValue
```

Returns a special value that can be used with `set()` or `update()` that tells the server to remove the given elements from any array value that already exists on the server. All instances of each element specified will be removed from the array. If the field being modified is not already an array it will be overwritten with an empty array.  

|                                                                                  Parameters                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| `elements: `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>!` | The elements to remove from the array. |

|                                                 Returns                                                  |
|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [FieldValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue) | The `FieldValue` sentinel for use in a call to `set()` or `update()`. |

### arrayUnion

```
java-staticÂ funÂ arrayUnion(elements:Â Array<Any!>!):Â FieldValue
```

Returns a special value that can be used with `set()` or `update()` that tells the server to union the given elements with any array value that already exists on the server. Each specified element that doesn't already exist in the array will be added to the end. If the field being modified is not already an array it will be overwritten with an array containing exactly the specified elements.  

|                                                                                  Parameters                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| `elements: `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>!` | The elements to union into the array. |

|                                                 Returns                                                  |
|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [FieldValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue) | The `FieldValue` sentinel for use in a call to `set()` or `update()`. |

### delete

```
java-staticÂ funÂ delete():Â FieldValue
```

Returns a sentinel for use with `update()` to mark a field for deletion.  

### increment

```
java-staticÂ funÂ increment(l:Â Long):Â FieldValue
```

Returns a special value that can be used with `set()` or `update()` that tells the server to increment the field's current value by the given value.

If the current field value is an integer, possible integer overflows are resolved to Long.MAX_VALUE or Long.MIN_VALUE. If the current field value is a double, both values will be interpreted as doubles and the arithmetic will follow IEEE 754 semantics.

If the current field is not an integer or double, or if the field does not yet exist, the transformation will set the field to the given value.  

|                                                 Returns                                                  |
|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [FieldValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue) | The `FieldValue` sentinel for use in a call to `set()` or `update()`. |

### increment

```
java-staticÂ funÂ increment(l:Â Double):Â FieldValue
```

Returns a special value that can be used with `set()` or `update()` that tells the server to increment the field's current value by the given value.

If the current value is an integer or a double, both the current and the given value will be interpreted as doubles and all arithmetic will follow IEEE 754 semantics. Otherwise, the transformation will set the field to the given value.  

|                                                 Returns                                                  |
|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [FieldValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldValue) | The `FieldValue` sentinel for use in a call to `set()` or `update()`. |

### serverTimestamp

```
java-staticÂ funÂ serverTimestamp():Â FieldValue
```

Returns a sentinel for use with `set()` or `update()` to include a server-generated timestamp in the written data.  

### vector

```
java-staticÂ funÂ vector(values:Â DoubleArray):Â VectorValue
```

Creates a new [VectorValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue) constructed with a copy of the given array of doubles.  

|                                              Parameters                                               |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| `values: `[DoubleArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html) | Array of doubles to be copied to create a [VectorValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue). |

|                                                  Returns                                                   |
|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [VectorValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue) | A new [VectorValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue) constructed with a copy of the given array of doubles. |