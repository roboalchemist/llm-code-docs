# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField.md.txt

# AggregateField.AverageAggregateField

# AggregateField.AverageAggregateField


```
class AggregateField.AverageAggregateField : AggregateField
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.firestore.AggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField) ||
|   | ↳ | [com.google.firebase.firestore.AggregateField.AverageAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField) |

*** ** * ** ***

Represents an "average" aggregation that can be performed by Firestore.

## Summary

| ### Inherited functions |
|---|
| From [com.google.firebase.firestore.AggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField) |---|---| | `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#average(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Create an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField` object that can be used to compute the average of a specified field over a range of documents in the result set of a query. | | `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#average(com.google.firebase.firestore.FieldPath)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)` Create an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField` object that can be used to compute the average of a specified field over a range of documents in the result set of a query. | | `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.CountAggregateField` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#count()()` Create a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.CountAggregateField` object that can be used to compute the count of documents in the result set of a query. | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#equals(java.lang.Object)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!)` Returns true if the given object is equal to this object. | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#hashCode()()` Calculates and returns the hash code for this object. | | `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#sum(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Create a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField` object that can be used to compute the sum of a specified field over a range of documents in the result set of a query. | | `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#sum(com.google.firebase.firestore.FieldPath)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)` Create a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField` object that can be used to compute the sum of a specified field over a range of documents in the result set of a query. | |

| ### Inherited properties |
|---|
| From [com.google.firebase.firestore.AggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField) |---|---| | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#alias()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#operator()` | |