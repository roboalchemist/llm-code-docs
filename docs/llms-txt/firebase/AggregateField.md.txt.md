# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.md.txt

# AggregateField

# AggregateField


```
public abstract class AggregateField
```

<br />

Known direct subclasses [AggregateField.AverageAggregateField](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.AverageAggregateField), [AggregateField.CountAggregateField](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.CountAggregateField), [AggregateField.SumAggregateField](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.SumAggregateField)

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.AverageAggregateField` | Represents an "average" aggregation that can be performed by Firestore. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.CountAggregateField` | Represents a "count" aggregation that can be performed by Firestore. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.SumAggregateField` | Represents a "sum" aggregation that can be performed by Firestore. |

*** ** * ** ***

Represents an aggregation that can be performed by Firestore.

## Summary

| ### Nested types |
|---|
| `public class https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.AverageAggregateField extends https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField` Represents an "average" aggregation that can be performed by Firestore. |
| `public class https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.CountAggregateField extends https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField` Represents a "count" aggregation that can be performed by Firestore. |
| `public class https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.SumAggregateField extends https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField` Represents a "sum" aggregation that can be performed by Firestore. |

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField#alias()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField#operator()` |

| ### Public methods |
|---|---|
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.AverageAggregateField` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField#average(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Create an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.AverageAggregateField` object that can be used to compute the average of a specified field over a range of documents in the result set of a query. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.AverageAggregateField` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField#average(com.google.firebase.firestore.FieldPath)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath)` Create an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.AverageAggregateField` object that can be used to compute the average of a specified field over a range of documents in the result set of a query. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.CountAggregateField` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField#count()()` Create a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.CountAggregateField` object that can be used to compute the count of documents in the result set of a query. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField#equals(java.lang.Object)(https://developer.android.com/reference/kotlin/java/lang/Object.html other)` Returns true if the given object is equal to this object. |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField#hashCode()()` Calculates and returns the hash code for this object. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.SumAggregateField` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField#sum(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Create a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.SumAggregateField` object that can be used to compute the sum of a specified field over a range of documents in the result set of a query. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.SumAggregateField` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField#sum(com.google.firebase.firestore.FieldPath)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath)` Create a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.SumAggregateField` object that can be used to compute the sum of a specified field over a range of documents in the result set of a query. |

## Public fields

### alias

```
public final @NonNull String alias
```

### operator

```
public final @NonNull String operator
```

## Public methods

### average

```
public static @NonNull AggregateField.AverageAggregateField average(@NonNull String field)
```

Create an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.AverageAggregateField` object that can be used to compute the average of a specified field over a range of documents in the result set of a query.

The result of an average operation will always be a double or NaN.

- Averaging over zero documents or fields will result in a double value representing NaN.
- Averaging over NaN will result in a double value representing NaN.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field` | Specifies the field to average across the result set. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.AverageAggregateField` | The \`AverageAggregateField\` object that can be used to compute the average of a specified field over a range of documents in the result set of a query. |

### average

```
public static @NonNull AggregateField.AverageAggregateField average(@NonNull FieldPath fieldPath)
```

Create an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.AverageAggregateField` object that can be used to compute the average of a specified field over a range of documents in the result set of a query.

The result of an average operation will always be a double or NaN.

- Averaging over zero documents or fields will result in a double value representing NaN.
- Averaging over NaN will result in a double value representing NaN.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath` | Specifies the field to average across the result set. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.AverageAggregateField` | The \`AverageAggregateField\` object that can be used to compute the average of a specified field over a range of documents in the result set of a query. |

### count

```
public static @NonNull AggregateField.CountAggregateField count()
```

Create a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.CountAggregateField` object that can be used to compute the count of documents in the result set of a query.

The result of a count operation will always be a 64-bit integer value.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.CountAggregateField` | The \`CountAggregateField\` object that can be used to compute the count of documents in the result set of a query. |

### equals

```
public boolean equals(Object other)
```

Returns true if the given object is equal to this object. Two \`AggregateField\` objects are considered equal if they have the same operator and operate on the same field.

### hashCode

```
public int hashCode()
```

Calculates and returns the hash code for this object.

### sum

```
public static @NonNull AggregateField.SumAggregateField sum(@NonNull String field)
```

Create a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.SumAggregateField` object that can be used to compute the sum of a specified field over a range of documents in the result set of a query.

The result of a sum operation will always be a 64-bit integer value, a double, or NaN.

- Summing over zero documents or fields will result in 0L.
- Summing over NaN will result in a double value representing NaN.
- A sum that overflows the maximum representable 64-bit integer value will result in a double return value. This may result in lost precision of the result.
- A sum that overflows the maximum representable double value will result in a double return value representing infinity.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field` | Specifies the field to sum across the result set. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.SumAggregateField` | The \`SumAggregateField\` object that can be used to compute the sum of a specified field over a range of documents in the result set of a query. |

### sum

```
public static @NonNull AggregateField.SumAggregateField sum(@NonNull FieldPath fieldPath)
```

Create a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.SumAggregateField` object that can be used to compute the sum of a specified field over a range of documents in the result set of a query.

The result of a sum operation will always be a 64-bit integer value, a double, or NaN.

- Summing over zero documents or fields will result in 0L.
- Summing over NaN will result in a double value representing NaN.
- A sum that overflows the maximum representable 64-bit integer value will result in a double return value. This may result in lost precision of the result.
- A sum that overflows the maximum representable double value will result in a double return value representing infinity.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath` | Specifies the field to sum across the result set. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.SumAggregateField` | The \`SumAggregateField\` object that can be used to compute the sum of a specified field over a range of documents in the result set of a query. |