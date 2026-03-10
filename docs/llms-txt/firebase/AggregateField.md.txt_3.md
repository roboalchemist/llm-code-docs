# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.md.txt

# AggregateField

# AggregateField


```
abstract class AggregateField
```

<br />

Known direct subclasses [AggregateField.AverageAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField), [AggregateField.CountAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.CountAggregateField), [AggregateField.SumAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField` | Represents an "average" aggregation that can be performed by Firestore. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.CountAggregateField` | Represents a "count" aggregation that can be performed by Firestore. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField` | Represents a "sum" aggregation that can be performed by Firestore. |

*** ** * ** ***

Represents an aggregation that can be performed by Firestore.

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField` Represents an "average" aggregation that can be performed by Firestore. |
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.CountAggregateField : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField` Represents a "count" aggregation that can be performed by Firestore. |
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField` Represents a "sum" aggregation that can be performed by Firestore. |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#average(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Create an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField` object that can be used to compute the average of a specified field over a range of documents in the result set of a query. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#average(com.google.firebase.firestore.FieldPath)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)` Create an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField` object that can be used to compute the average of a specified field over a range of documents in the result set of a query. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.CountAggregateField` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#count()()` Create a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.CountAggregateField` object that can be used to compute the count of documents in the result set of a query. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#equals(java.lang.Object)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!)` Returns true if the given object is equal to this object. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#hashCode()()` Calculates and returns the hash code for this object. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#sum(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Create a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField` object that can be used to compute the sum of a specified field over a range of documents in the result set of a query. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#sum(com.google.firebase.firestore.FieldPath)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)` Create a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField` object that can be used to compute the sum of a specified field over a range of documents in the result set of a query. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#alias()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#operator()` |

## Public functions

### average

```
java-static fun average(field: String): AggregateField.AverageAggregateField
```

Create an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField` object that can be used to compute the average of a specified field over a range of documents in the result set of a query.

The result of an average operation will always be a double or NaN.

- Averaging over zero documents or fields will result in a double value representing NaN.
- Averaging over NaN will result in a double value representing NaN.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Specifies the field to average across the result set. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField` | The \`AverageAggregateField\` object that can be used to compute the average of a specified field over a range of documents in the result set of a query. |

### average

```
java-static fun average(fieldPath: FieldPath): AggregateField.AverageAggregateField
```

Create an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField` object that can be used to compute the average of a specified field over a range of documents in the result set of a query.

The result of an average operation will always be a double or NaN.

- Averaging over zero documents or fields will result in a double value representing NaN.
- Averaging over NaN will result in a double value representing NaN.

| Parameters |
|---|---|
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | Specifies the field to average across the result set. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField` | The \`AverageAggregateField\` object that can be used to compute the average of a specified field over a range of documents in the result set of a query. |

### count

```
java-static fun count(): AggregateField.CountAggregateField
```

Create a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.CountAggregateField` object that can be used to compute the count of documents in the result set of a query.

The result of a count operation will always be a 64-bit integer value.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.CountAggregateField` | The \`CountAggregateField\` object that can be used to compute the count of documents in the result set of a query. |

### equals

```
fun equals(other: Any!): Boolean
```

Returns true if the given object is equal to this object. Two \`AggregateField\` objects are considered equal if they have the same operator and operate on the same field.

### hashCode

```
fun hashCode(): Int
```

Calculates and returns the hash code for this object.

### sum

```
java-static fun sum(field: String): AggregateField.SumAggregateField
```

Create a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField` object that can be used to compute the sum of a specified field over a range of documents in the result set of a query.

The result of a sum operation will always be a 64-bit integer value, a double, or NaN.

- Summing over zero documents or fields will result in 0L.
- Summing over NaN will result in a double value representing NaN.
- A sum that overflows the maximum representable 64-bit integer value will result in a double return value. This may result in lost precision of the result.
- A sum that overflows the maximum representable double value will result in a double return value representing infinity.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Specifies the field to sum across the result set. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField` | The \`SumAggregateField\` object that can be used to compute the sum of a specified field over a range of documents in the result set of a query. |

### sum

```
java-static fun sum(fieldPath: FieldPath): AggregateField.SumAggregateField
```

Create a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField` object that can be used to compute the sum of a specified field over a range of documents in the result set of a query.

The result of a sum operation will always be a 64-bit integer value, a double, or NaN.

- Summing over zero documents or fields will result in 0L.
- Summing over NaN will result in a double value representing NaN.
- A sum that overflows the maximum representable 64-bit integer value will result in a double return value. This may result in lost precision of the result.
- A sum that overflows the maximum representable double value will result in a double return value representing infinity.

| Parameters |
|---|---|
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | Specifies the field to sum across the result set. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField` | The \`SumAggregateField\` object that can be used to compute the sum of a specified field over a range of documents in the result set of a query. |

## Public properties

### alias

```
val alias: String
```

### operator

```
val operator: String
```