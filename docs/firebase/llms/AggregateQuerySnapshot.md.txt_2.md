# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuerySnapshot.md.txt

# AggregateQuerySnapshot

# AggregateQuerySnapshot


```
class AggregateQuerySnapshot
```

<br />

*** ** * ** ***

The results of executing an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery`.

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuerySnapshot#equals(java.lang.Object)(object: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!)` Compares this object with the given object for equality. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuerySnapshot#get(com.google.firebase.firestore.AggregateField)(aggregateField: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField)` Returns the result of the given aggregation from the server without coercion of data types. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuerySnapshot#get(com.google.firebase.firestore.AggregateField.AverageAggregateField)(averageAggregateField: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField)` Returns the result of the given average aggregation. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuerySnapshot#get(com.google.firebase.firestore.AggregateField.CountAggregateField)(countAggregateField: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.CountAggregateField)` Returns the number of documents in the result set of the underlying query. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuerySnapshot#getCount()()` Returns the number of documents in the result set of the underlying query. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuerySnapshot#getDouble(com.google.firebase.firestore.AggregateField)(aggregateField: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField)` Returns the result of the given aggregation as a double. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuerySnapshot#getLong(com.google.firebase.firestore.AggregateField)(aggregateField: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField)` Returns the result of the given aggregation as a long. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuerySnapshot#hashCode()()` Calculates and returns the hash code for this object. |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuerySnapshot#query()` |

## Public functions

### equals

```
fun equals(object: Any!): Boolean
```

Compares this object with the given object for equality.

This object is considered "equal" to the other object if and only if all of the following conditions are satisfied:

1. `object` is a non-null instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuerySnapshot`.
2. The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery` of `object` compares equal to that of this object.
3. `object` has the same results as this object.

| Parameters |
|---|---|
| `object: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!` | The object to compare to this object for equality. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `true` if this object is "equal" to the given object, as defined above, or ` false` otherwise. |

### get

```
fun get(aggregateField: AggregateField): Any?
```

Returns the result of the given aggregation from the server without coercion of data types. Throws java.lang.RuntimeException if the \`aggregateField\` was not requested when calling \`query.aggregate(...)\`.

| Parameters |
|---|---|
| `aggregateField: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField` | The aggregation for which the value is requested. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The result of the given aggregation. |

### get

```
fun get(averageAggregateField: AggregateField.AverageAggregateField): Double?
```

Returns the result of the given average aggregation. Since the result of an average aggregation performed by the server is always a double, this convenience overload can be used in lieu of the above \`get\` method. Throws java.lang.RuntimeException if the \`aggregateField\` was not requested when calling \`query.aggregate(...)\`.

| Parameters |
|---|---|
| `averageAggregateField: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField` | The average aggregation for which the value is requested. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html?` | The result of the given average aggregation. |

### get

```
fun get(countAggregateField: AggregateField.CountAggregateField): Long
```

Returns the number of documents in the result set of the underlying query.

| Parameters |
|---|---|
| `countAggregateField: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.CountAggregateField` | The count aggregation for which the value is requested. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The result of the given count aggregation. |

### getCount

```
fun getCount(): Long
```

Returns the number of documents in the result set of the underlying query.

### getDouble

```
fun getDouble(aggregateField: AggregateField): Double?
```

Returns the result of the given aggregation as a double. Coerces all numeric values and throws a RuntimeException if the result of the aggregate is non-numeric. In the case of coercion of long to double, uses java.lang.Long.doubleValue to perform the conversion, and may result in a loss of precision.

| Parameters |
|---|---|
| `aggregateField: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField` | The aggregation for which the value is requested. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html?` | The result of the given average aggregation as a double. |

### getLong

```
fun getLong(aggregateField: AggregateField): Long?
```

Returns the result of the given aggregation as a long. Coerces all numeric values and throws a RuntimeException if the result of the aggregate is non-numeric. In case of coercion of double to long, uses java.lang.Double.longValue to perform the conversion.

| Parameters |
|---|---|
| `aggregateField: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField` | The aggregation for which the value is requested. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html?` | The result of the given average aggregation as a long. |

### hashCode

```
fun hashCode(): Int
```

Calculates and returns the hash code for this object.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | the hash code for this object. |

## Public properties

### query

```
val query: AggregateQuery
```