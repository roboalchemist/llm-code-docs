# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot.md.txt

# AggregateQuerySnapshot

# AggregateQuerySnapshot


```
public class AggregateQuerySnapshot
```

<br />

*** ** * ** ***

The results of executing an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery`.

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot#query()` |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot#equals(java.lang.Object)(https://developer.android.com/reference/kotlin/java/lang/Object.html object)` Compares this object with the given object for equality. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot#get(com.google.firebase.firestore.AggregateField)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField aggregateField)` Returns the result of the given aggregation from the server without coercion of data types. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Double.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot#get(com.google.firebase.firestore.AggregateField.AverageAggregateField)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.AverageAggregateField averageAggregateField)` Returns the result of the given average aggregation. |
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot#get(com.google.firebase.firestore.AggregateField.CountAggregateField)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.CountAggregateField countAggregateField)` Returns the number of documents in the result set of the underlying query. |
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot#getCount()()` Returns the number of documents in the result set of the underlying query. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Double.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot#getDouble(com.google.firebase.firestore.AggregateField)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField aggregateField)` Returns the result of the given aggregation as a double. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Long.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot#getLong(com.google.firebase.firestore.AggregateField)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField aggregateField)` Returns the result of the given aggregation as a long. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot#getQuery()()` Returns the query that was executed to produce this result. |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot#hashCode()()` Calculates and returns the hash code for this object. |

## Public fields

### query

```
public final @NonNull AggregateQuery query
```

## Public methods

### equals

```
public boolean equals(Object object)
```

Compares this object with the given object for equality.

This object is considered "equal" to the other object if and only if all of the following conditions are satisfied:

1. `object` is a non-null instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot`.
2. The `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery` of `object` compares equal to that of this object.
3. `object` has the same results as this object.

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/Object.html object` | The object to compare to this object for equality. |

| Returns |
|---|---|
| `boolean` | `true` if this object is "equal" to the given object, as defined above, or ` false` otherwise. |

### get

```
public @Nullable Object get(@NonNull AggregateField aggregateField)
```

Returns the result of the given aggregation from the server without coercion of data types. Throws java.lang.RuntimeException if the \`aggregateField\` was not requested when calling \`query.aggregate(...)\`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField aggregateField` | The aggregation for which the value is requested. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | The result of the given aggregation. |

### get

```
public @Nullable Double get(@NonNull AggregateField.AverageAggregateField averageAggregateField)
```

Returns the result of the given average aggregation. Since the result of an average aggregation performed by the server is always a double, this convenience overload can be used in lieu of the above \`get\` method. Throws java.lang.RuntimeException if the \`aggregateField\` was not requested when calling \`query.aggregate(...)\`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.AverageAggregateField averageAggregateField` | The average aggregation for which the value is requested. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Double.html` | The result of the given average aggregation. |

### get

```
public long get(@NonNull AggregateField.CountAggregateField countAggregateField)
```

Returns the number of documents in the result set of the underlying query.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.CountAggregateField countAggregateField` | The count aggregation for which the value is requested. |

| Returns |
|---|---|
| `long` | The result of the given count aggregation. |

### getCount

```
public long getCount()
```

Returns the number of documents in the result set of the underlying query.

### getDouble

```
public @Nullable Double getDouble(@NonNull AggregateField aggregateField)
```

Returns the result of the given aggregation as a double. Coerces all numeric values and throws a RuntimeException if the result of the aggregate is non-numeric. In the case of coercion of long to double, uses java.lang.Long.doubleValue to perform the conversion, and may result in a loss of precision.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField aggregateField` | The aggregation for which the value is requested. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Double.html` | The result of the given average aggregation as a double. |

### getLong

```
public @Nullable Long getLong(@NonNull AggregateField aggregateField)
```

Returns the result of the given aggregation as a long. Coerces all numeric values and throws a RuntimeException if the result of the aggregate is non-numeric. In case of coercion of double to long, uses java.lang.Double.longValue to perform the conversion.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField aggregateField` | The aggregation for which the value is requested. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Long.html` | The result of the given average aggregation as a long. |

### getQuery

```
public @NonNull AggregateQuery getQuery()
```

Returns the query that was executed to produce this result.

### hashCode

```
public int hashCode()
```

Calculates and returns the hash code for this object.

| Returns |
|---|---|
| `int` | the hash code for this object. |