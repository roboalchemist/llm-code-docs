# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.SumAggregateField.md.txt

# AggregateField.SumAggregateField

# AggregateField.SumAggregateField


```
public class AggregateField.SumAggregateField extends AggregateField
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.firestore.AggregateField](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField) ||
|   | ↳ | [com.google.firebase.firestore.AggregateField.SumAggregateField](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.SumAggregateField) |

*** ** * ** ***

Represents a "sum" aggregation that can be performed by Firestore.

## Summary

| ### Inherited fields |
|---|
| From [com.google.firebase.firestore.AggregateField](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField) |---|---| | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField#alias()` | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField#operator()` | |

| ### Inherited methods |
|---|
| From [com.google.firebase.firestore.AggregateField](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField) |---|---| | `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.AverageAggregateField` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField#average(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Create an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.AverageAggregateField` object that can be used to compute the average of a specified field over a range of documents in the result set of a query. | | `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.AverageAggregateField` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField#average(com.google.firebase.firestore.FieldPath)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath)` Create an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.AverageAggregateField` object that can be used to compute the average of a specified field over a range of documents in the result set of a query. | | `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.CountAggregateField` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField#count()()` Create a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.CountAggregateField` object that can be used to compute the count of documents in the result set of a query. | | `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField#equals(java.lang.Object)(https://developer.android.com/reference/kotlin/java/lang/Object.html other)` Returns true if the given object is equal to this object. | | `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField#hashCode()()` Calculates and returns the hash code for this object. | | `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.SumAggregateField` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField#sum(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html field)` Create a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.SumAggregateField` object that can be used to compute the sum of a specified field over a range of documents in the result set of a query. | | `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.SumAggregateField` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField#sum(com.google.firebase.firestore.FieldPath)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath)` Create a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.SumAggregateField` object that can be used to compute the sum of a specified field over a range of documents in the result set of a query. | |