# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue.md.txt

# FieldValue

# FieldValue


```
public abstract class FieldValue
```

<br />

*** ** * ** ***

Sentinel values that can be used when writing document fields with `set()` or `
update()`.

## Summary

| ### Public methods |
|---|---|
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue#arrayRemove(java.lang.Object...)(Object[] elements)` Returns a special value that can be used with `set()` or `update()` that tells the server to remove the given elements from any array value that already exists on the server. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue#arrayUnion(java.lang.Object...)(Object[] elements)` Returns a special value that can be used with `set()` or `update()` that tells the server to union the given elements with any array value that already exists on the server. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue#delete()()` Returns a sentinel for use with `update()` to mark a field for deletion. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue#increment(long)(long l)` Returns a special value that can be used with `set()` or `update()` that tells the server to increment the field's current value by the given value. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue#increment(double)(double l)` Returns a special value that can be used with `set()` or `update()` that tells the server to increment the field's current value by the given value. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue#serverTimestamp()()` Returns a sentinel for use with `set()` or `update()` to include a server-generated timestamp in the written data. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue#vector(double[])(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html double[] values)` Creates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue` constructed with a copy of the given array of doubles. |

## Public methods

### arrayRemove

```
public static @NonNull FieldValue arrayRemove(Object[] elements)
```

Returns a special value that can be used with `set()` or `update()` that tells the server to remove the given elements from any array value that already exists on the server. All instances of each element specified will be removed from the array. If the field being modified is not already an array it will be overwritten with an empty array.

| Parameters |
|---|---|
| `Object[] elements` | The elements to remove from the array. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue` | The `FieldValue` sentinel for use in a call to `set()` or `update()`. |

### arrayUnion

```
public static @NonNull FieldValue arrayUnion(Object[] elements)
```

Returns a special value that can be used with `set()` or `update()` that tells the server to union the given elements with any array value that already exists on the server. Each specified element that doesn't already exist in the array will be added to the end. If the field being modified is not already an array it will be overwritten with an array containing exactly the specified elements.

| Parameters |
|---|---|
| `Object[] elements` | The elements to union into the array. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue` | The `FieldValue` sentinel for use in a call to `set()` or `update()`. |

### delete

```
public static @NonNull FieldValue delete()
```

Returns a sentinel for use with `update()` to mark a field for deletion.

### increment

```
public static @NonNull FieldValue increment(long l)
```

Returns a special value that can be used with `set()` or `update()` that tells the server to increment the field's current value by the given value.

If the current field value is an integer, possible integer overflows are resolved to Long.MAX_VALUE or Long.MIN_VALUE. If the current field value is a double, both values will be interpreted as doubles and the arithmetic will follow IEEE 754 semantics.

If the current field is not an integer or double, or if the field does not yet exist, the transformation will set the field to the given value.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue` | The `FieldValue` sentinel for use in a call to `set()` or `update()`. |

### increment

```
public static @NonNull FieldValue increment(double l)
```

Returns a special value that can be used with `set()` or `update()` that tells the server to increment the field's current value by the given value.

If the current value is an integer or a double, both the current and the given value will be interpreted as doubles and all arithmetic will follow IEEE 754 semantics. Otherwise, the transformation will set the field to the given value.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldValue` | The `FieldValue` sentinel for use in a call to `set()` or `update()`. |

### serverTimestamp

```
public static @NonNull FieldValue serverTimestamp()
```

Returns a sentinel for use with `set()` or `update()` to include a server-generated timestamp in the written data.

### vector

```
public static @NonNull VectorValue vector(@NonNull double[] values)
```

Creates a new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue` constructed with a copy of the given array of doubles.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html double[] values` | Array of doubles to be copied to create a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue`. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue` constructed with a copy of the given array of doubles. |