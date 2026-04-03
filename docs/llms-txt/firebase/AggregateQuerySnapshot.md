# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateQuerySnapshot.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuerySnapshot.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot.md.txt

# AggregateQuerySnapshot

# AggregateQuerySnapshot


```
public class AggregateQuerySnapshot
```

<br />

*** ** * ** ***

The results of executing an [AggregateQuery](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery).

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

|                                                                                                    ### Public fields                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[AggregateQuery](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery) | [query](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot#query()) |

|                                                                                                ### Public methods                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `boolean`                                                                                                                                                                                                         | [equals](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot#equals(java.lang.Object))`(`[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)` object)` Compares this object with the given object for equality.                                                                                                                                                                                                                                                   |
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)                                  | [get](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot#get(com.google.firebase.firestore.AggregateField))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[AggregateField](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField)` aggregateField)` Returns the result of the given aggregation from the server without coercion of data types.                                                 |
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Double](https://developer.android.com/reference/kotlin/java/lang/Double.html)                                  | [get](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot#get(com.google.firebase.firestore.AggregateField.AverageAggregateField))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[AggregateField.AverageAggregateField](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.AverageAggregateField)` averageAggregateField)` Returns the result of the given average aggregation.               |
| `long`                                                                                                                                                                                                            | [get](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot#get(com.google.firebase.firestore.AggregateField.CountAggregateField))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[AggregateField.CountAggregateField](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.CountAggregateField)` countAggregateField)` Returns the number of documents in the result set of the underlying query. |
| `long`                                                                                                                                                                                                            | [getCount](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot#getCount())`()` Returns the number of documents in the result set of the underlying query.                                                                                                                                                                                                                                                                                                                                    |
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Double](https://developer.android.com/reference/kotlin/java/lang/Double.html)                                  | [getDouble](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot#getDouble(com.google.firebase.firestore.AggregateField))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[AggregateField](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField)` aggregateField)` Returns the result of the given aggregation as a double.                                                                        |
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Long](https://developer.android.com/reference/kotlin/java/lang/Long.html)                                      | [getLong](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot#getLong(com.google.firebase.firestore.AggregateField))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[AggregateField](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField)` aggregateField)` Returns the result of the given aggregation as a long.                                                                              |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[AggregateQuery](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery) | [getQuery](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot#getQuery())`()` Returns the query that was executed to produce this result.                                                                                                                                                                                                                                                                                                                                                   |
| `int`                                                                                                                                                                                                             | [hashCode](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot#hashCode())`()` Calculates and returns the hash code for this object.                                                                                                                                                                                                                                                                                                                                                         |

## Public fields

### query

```
publicÂ finalÂ @NonNull AggregateQueryÂ query
```  

## Public methods

### equals

```
publicÂ booleanÂ equals(ObjectÂ object)
```

Compares this object with the given object for equality.

This object is considered "equal" to the other object if and only if all of the following conditions are satisfied:

1. `object` is a non-null instance of [AggregateQuerySnapshot](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot).
2. The [AggregateQuery](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery) of `object` compares equal to that of this object.
3. `object` has the same results as this object.

|                                       Parameters                                        |
|-----------------------------------------------------------------------------------------|----------------------------------------------------|
| [Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)` object` | The object to compare to this object for equality. |

|  Returns  |
|-----------|------------------------------------------------------------------------------------------------|
| `boolean` | `true` if this object is "equal" to the given object, as defined above, or ` false` otherwise. |

### get

```
publicÂ @Nullable ObjectÂ get(@NonNull AggregateFieldÂ aggregateField)
```

Returns the result of the given aggregation from the server without coercion of data types. Throws java.lang.RuntimeException if the \`aggregateField\` was not requested when calling \`query.aggregate(...)\`.  

|                                                                                                             Parameters                                                                                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[AggregateField](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField)` aggregateField` | The aggregation for which the value is requested. |

|                                                                                     Returns                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) | The result of the given aggregation. |

### get

```
publicÂ @Nullable DoubleÂ get(@NonNull AggregateField.AverageAggregateFieldÂ averageAggregateField)
```

Returns the result of the given average aggregation. Since the result of an average aggregation performed by the server is always a double, this convenience overload can be used in lieu of the above \`get\` method. Throws java.lang.RuntimeException if the \`aggregateField\` was not requested when calling \`query.aggregate(...)\`.  

|                                                                                                                                      Parameters                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[AggregateField.AverageAggregateField](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.AverageAggregateField)` averageAggregateField` | The average aggregation for which the value is requested. |

|                                                                                     Returns                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Double](https://developer.android.com/reference/kotlin/java/lang/Double.html) | The result of the given average aggregation. |

### get

```
publicÂ longÂ get(@NonNull AggregateField.CountAggregateFieldÂ countAggregateField)
```

Returns the number of documents in the result set of the underlying query.  

|                                                                                                                                   Parameters                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[AggregateField.CountAggregateField](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.CountAggregateField)` countAggregateField` | The count aggregation for which the value is requested. |

| Returns |
|---------|--------------------------------------------|
| `long`  | The result of the given count aggregation. |

### getCount

```
publicÂ longÂ getCount()
```

Returns the number of documents in the result set of the underlying query.  

### getDouble

```
publicÂ @Nullable DoubleÂ getDouble(@NonNull AggregateFieldÂ aggregateField)
```

Returns the result of the given aggregation as a double. Coerces all numeric values and throws a RuntimeException if the result of the aggregate is non-numeric. In the case of coercion of long to double, uses java.lang.Long.doubleValue to perform the conversion, and may result in a loss of precision.  

|                                                                                                             Parameters                                                                                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[AggregateField](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField)` aggregateField` | The aggregation for which the value is requested. |

|                                                                                     Returns                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Double](https://developer.android.com/reference/kotlin/java/lang/Double.html) | The result of the given average aggregation as a double. |

### getLong

```
publicÂ @Nullable LongÂ getLong(@NonNull AggregateFieldÂ aggregateField)
```

Returns the result of the given aggregation as a long. Coerces all numeric values and throws a RuntimeException if the result of the aggregate is non-numeric. In case of coercion of double to long, uses java.lang.Double.longValue to perform the conversion.  

|                                                                                                             Parameters                                                                                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[AggregateField](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField)` aggregateField` | The aggregation for which the value is requested. |

|                                                                                   Returns                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Long](https://developer.android.com/reference/kotlin/java/lang/Long.html) | The result of the given average aggregation as a long. |

### getQuery

```
publicÂ @NonNull AggregateQueryÂ getQuery()
```

Returns the query that was executed to produce this result.  

### hashCode

```
publicÂ intÂ hashCode()
```

Calculates and returns the hash code for this object.  

| Returns |
|---------|--------------------------------|
| `int`   | the hash code for this object. |