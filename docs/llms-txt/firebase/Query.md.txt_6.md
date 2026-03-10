# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.md.txt

# Query

# Query


```
class Query
```

<br />

Known direct subclasses [CollectionReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/CollectionReference)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/CollectionReference` | A `CollectionReference` can be used for adding documents, getting document references, and querying for documents (using the methods inherited from `Query`). |

*** ** * ** ***

A `Query` which you can read or listen to. You can also construct refined `Query` objects by adding filters and ordering.

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

| ### Nested types |
|---|
| `enum https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.Direction` An enum for the direction of a sort. |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#addSnapshotListener(com.google.firebase.firestore.EventListener<com.google.firebase.firestore.QuerySnapshot>)(listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot!>)` Starts listening to this query. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#addSnapshotListener(android.app.Activity,com.google.firebase.firestore.EventListener<com.google.firebase.firestore.QuerySnapshot>)( activity: https://developer.android.com/reference/kotlin/android/app/Activity.html, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot!> )` Starts listening to this query using an Activity-scoped listener. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#addSnapshotListener(java.util.concurrent.Executor,com.google.firebase.firestore.EventListener<com.google.firebase.firestore.QuerySnapshot>)( executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot!> )` Starts listening to this query. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#addSnapshotListener(com.google.firebase.firestore.MetadataChanges,com.google.firebase.firestore.EventListener<com.google.firebase.firestore.QuerySnapshot>)( metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot!> )` Starts listening to this query with the given options. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#addSnapshotListener(com.google.firebase.firestore.SnapshotListenOptions,com.google.firebase.firestore.EventListener<com.google.firebase.firestore.QuerySnapshot>)( options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot!> )` Starts listening to this query with the given options. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#addSnapshotListener(android.app.Activity,com.google.firebase.firestore.MetadataChanges,com.google.firebase.firestore.EventListener<com.google.firebase.firestore.QuerySnapshot>)( activity: https://developer.android.com/reference/kotlin/android/app/Activity.html, metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot!> )` Starts listening to this query with the given options, using an Activity-scoped listener. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#addSnapshotListener(java.util.concurrent.Executor,com.google.firebase.firestore.MetadataChanges,com.google.firebase.firestore.EventListener<com.google.firebase.firestore.QuerySnapshot>)( executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html, metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges, listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot!> )` Starts listening to this query with the given options. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#aggregate(com.google.firebase.firestore.AggregateField,com.google.firebase.firestore.AggregateField...)( aggregateField: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField, aggregateFields: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField!> )` Calculates the specified aggregations over the documents in the result set of the given query without actually downloading the documents. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#count()()` Returns a query that counts the documents in the result set of this query. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#endAt(java.lang.Object...)(fieldValues: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>!)` Creates and returns a new `Query` that ends at the provided fields relative to the order of the query. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#endAt(com.google.firebase.firestore.DocumentSnapshot)(snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot)` Creates and returns a new `Query` that ends at the provided document (inclusive). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#endBefore(java.lang.Object...)(fieldValues: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>!)` Creates and returns a new `Query` that ends before the provided fields relative to the order of the query. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#endBefore(com.google.firebase.firestore.DocumentSnapshot)(snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot)` Creates and returns a new `Query` that ends before the provided document (exclusive). |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#equals(java.lang.Object)(o: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!)` |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#get()()` Executes the query and returns the results as a `QuerySnapshot`. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#get(com.google.firebase.firestore.Source)(source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Source)` Executes the query and returns the results as a `QuerySnapshot`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#hashCode()()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#limit(long)(limit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Creates and returns a new `Query` that only returns the first matching documents up to the specified number. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#limitToLast(long)(limit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Creates and returns a new `Query` that only returns the last matching documents up to the specified number. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#orderBy(java.lang.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates and returns a new `Query` that's additionally sorted by the specified field. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#orderBy(com.google.firebase.firestore.FieldPath)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)` Creates and returns a new `Query` that's additionally sorted by the specified field. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#orderBy(java.lang.String,com.google.firebase.firestore.Query.Direction)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, direction: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.Direction)` Creates and returns a new `Query` that's additionally sorted by the specified field, optionally in descending order instead of ascending. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#orderBy(com.google.firebase.firestore.FieldPath,com.google.firebase.firestore.Query.Direction)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath, direction: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.Direction)` Creates and returns a new `Query` that's additionally sorted by the specified field, optionally in descending order instead of ascending. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#startAfter(java.lang.Object...)(fieldValues: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>!)` Creates and returns a new `Query` that starts after the provided fields relative to the order of the query. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#startAfter(com.google.firebase.firestore.DocumentSnapshot)(snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot)` Creates and returns a new `Query` that starts after the provided document (exclusive). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#startAt(java.lang.Object...)(fieldValues: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>!)` Creates and returns a new `Query` that starts at the provided fields relative to the order of the query. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#startAt(com.google.firebase.firestore.DocumentSnapshot)(snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot)` Creates and returns a new `Query` that starts at the provided document (inclusive). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#where(com.google.firebase.firestore.Filter)(filter: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Filter)` Creates and returns a new `Query` with the additional filter. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#whereArrayContains(java.lang.String,java.lang.Object)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates and returns a new `Query` with the additional filter that documents must contain the specified field, the value must be an array, and that the array must contain the provided value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#whereArrayContains(com.google.firebase.firestore.FieldPath,java.lang.Object)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates and returns a new `Query` with the additional filter that documents must contain the specified field, the value must be an array, and that the array must contain the provided value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#whereArrayContainsAny(java.lang.String,java.util.List<? extends java.lang.Object>)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, values: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Creates and returns a new `Query` with the additional filter that documents must contain the specified field, the value must be an array, and that the array must contain at least one value from the provided list. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#whereArrayContainsAny(com.google.firebase.firestore.FieldPath,java.util.List<? extends java.lang.Object>)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath, values: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Creates and returns a new `Query` with the additional filter that documents must contain the specified field, the value must be an array, and that the array must contain at least one value from the provided list. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#whereEqualTo(java.lang.String,java.lang.Object)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value should be equal to the specified value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#whereEqualTo(com.google.firebase.firestore.FieldPath,java.lang.Object)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value should be equal to the specified value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#whereGreaterThan(java.lang.String,java.lang.Object)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value should be greater than the specified value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#whereGreaterThan(com.google.firebase.firestore.FieldPath,java.lang.Object)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value should be greater than the specified value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#whereGreaterThanOrEqualTo(java.lang.String,java.lang.Object)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value should be greater than or equal to the specified value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#whereGreaterThanOrEqualTo(com.google.firebase.firestore.FieldPath,java.lang.Object)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value should be greater than or equal to the specified value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#whereIn(java.lang.String,java.util.List<? extends java.lang.Object>)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, values: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value must equal one of the values from the provided list. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#whereIn(com.google.firebase.firestore.FieldPath,java.util.List<? extends java.lang.Object>)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath, values: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value must equal one of the values from the provided list. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#whereLessThan(java.lang.String,java.lang.Object)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value should be less than the specified value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#whereLessThan(com.google.firebase.firestore.FieldPath,java.lang.Object)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value should be less than the specified value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#whereLessThanOrEqualTo(java.lang.String,java.lang.Object)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value should be less than or equal to the specified value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#whereLessThanOrEqualTo(com.google.firebase.firestore.FieldPath,java.lang.Object)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value should be less than or equal to the specified value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#whereNotEqualTo(java.lang.String,java.lang.Object)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value does not equal the specified value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#whereNotEqualTo(com.google.firebase.firestore.FieldPath,java.lang.Object)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value does not equal the specified value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#whereNotIn(java.lang.String,java.util.List<? extends java.lang.Object>)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, values: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value does not equal any of the values from the provided list. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#whereNotIn(com.google.firebase.firestore.FieldPath,java.util.List<? extends java.lang.Object>)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath, values: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value does not equal any of the values from the provided list. |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#firestore()` |

| ### Extension functions |
|---|---|
| `inline https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<T>>` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#(com.google.firebase.firestore.Query).dataObjects(com.google.firebase.firestore.MetadataChanges)(metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges)` Starts listening to this query with the given options and emits its values converted to a POJO via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. |
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query#(com.google.firebase.firestore.Query).snapshots(com.google.firebase.firestore.MetadataChanges)(metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges)` Starts listening to this query with the given options and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. |

## Public functions

### addSnapshotListener

```
fun addSnapshotListener(listener: EventListener<QuerySnapshot!>): ListenerRegistration
```

Starts listening to this query.

| Parameters |
|---|---|
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot!>` | The event listener that will be called with the snapshots. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### addSnapshotListener

```
fun addSnapshotListener(
    activity: Activity,
    listener: EventListener<QuerySnapshot!>
): ListenerRegistration
```

Starts listening to this query using an Activity-scoped listener.

The listener will be automatically removed during `https://developer.android.com/reference/kotlin/android/app/Activity.html#onStop--`.

| Parameters |
|---|---|
| `activity: https://developer.android.com/reference/kotlin/android/app/Activity.html` | The activity to scope the listener to. |
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot!>` | The event listener that will be called with the snapshots. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### addSnapshotListener

```
fun addSnapshotListener(
    executor: Executor,
    listener: EventListener<QuerySnapshot!>
): ListenerRegistration
```

Starts listening to this query.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | The executor to use to call the listener. |
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot!>` | The event listener that will be called with the snapshots. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### addSnapshotListener

```
fun addSnapshotListener(
    metadataChanges: MetadataChanges,
    listener: EventListener<QuerySnapshot!>
): ListenerRegistration
```

Starts listening to this query with the given options.

| Parameters |
|---|---|
| `metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges` | Indicates whether metadata-only changes (specifically, only ` QuerySnapshot.getMetadata()` changed) should trigger snapshot events. |
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot!>` | The event listener that will be called with the snapshots. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### addSnapshotListener

```
fun addSnapshotListener(
    options: SnapshotListenOptions,
    listener: EventListener<QuerySnapshot!>
): ListenerRegistration
```

Starts listening to this query with the given options.

| Parameters |
|---|---|
| `options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/SnapshotListenOptions` | Sets snapshot listener options, including whether metadata-only changes should trigger snapshot events, the source to listen to, the executor to use to call the listener, or the activity to scope the listener to. |
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot!>` | The event listener that will be called with the snapshots. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### addSnapshotListener

```
fun addSnapshotListener(
    activity: Activity,
    metadataChanges: MetadataChanges,
    listener: EventListener<QuerySnapshot!>
): ListenerRegistration
```

Starts listening to this query with the given options, using an Activity-scoped listener.

The listener will be automatically removed during `https://developer.android.com/reference/kotlin/android/app/Activity.html#onStop--`.

| Parameters |
|---|---|
| `activity: https://developer.android.com/reference/kotlin/android/app/Activity.html` | The activity to scope the listener to. |
| `metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges` | Indicates whether metadata-only changes (specifically, only ` QuerySnapshot.getMetadata()` changed) should trigger snapshot events. |
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot!>` | The event listener that will be called with the snapshots. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### addSnapshotListener

```
fun addSnapshotListener(
    executor: Executor,
    metadataChanges: MetadataChanges,
    listener: EventListener<QuerySnapshot!>
): ListenerRegistration
```

Starts listening to this query with the given options.

| Parameters |
|---|---|
| `executor: https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html` | The executor to use to call the listener. |
| `metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges` | Indicates whether metadata-only changes (specifically, only ` QuerySnapshot.getMetadata()` changed) should trigger snapshot events. |
| `listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot!>` | The event listener that will be called with the snapshots. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenerRegistration` | A registration object that can be used to remove the listener. |

### aggregate

```
fun aggregate(
    aggregateField: AggregateField,
    aggregateFields: Array<AggregateField!>
): AggregateQuery
```

Calculates the specified aggregations over the documents in the result set of the given query without actually downloading the documents.

Using the returned query to perform aggregations is efficient because only the final aggregation values, not the documents' data, is downloaded. The returned query can perform aggregations of the documents in cases where the result set is prohibitively large to download entirely (thousands of documents).

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery` | The `AggregateQuery` that performs aggregations on the documents in the result set of this query. |

### count

```
fun count(): AggregateQuery
```

Returns a query that counts the documents in the result set of this query.

The returned query, when executed, counts the documents in the result set of this query *without actually downloading the documents*.

Using the returned query to count the documents is efficient because only the final count, not the documents' data, is downloaded. The returned query can count the documents in cases where the result set is prohibitively large to download entirely (thousands of documents).

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery` | The `AggregateQuery` that counts the documents in the result set of this query. |

### endAt

```
fun endAt(fieldValues: Array<Any!>!): Query
```

Creates and returns a new `Query` that ends at the provided fields relative to the order of the query. The order of the field values must match the order of the order by clauses of the query.

| Parameters |
|---|---|
| `fieldValues: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>!` | The field values to end this query at, in order of the query's order by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### endAt

```
fun endAt(snapshot: DocumentSnapshot): Query
```

Creates and returns a new `Query` that ends at the provided document (inclusive). The end position is relative to the order of the query. The document must contain all of the fields provided in the orderBy of this query.

| Parameters |
|---|---|
| `snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot` | The snapshot of the document to end at. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### endBefore

```
fun endBefore(fieldValues: Array<Any!>!): Query
```

Creates and returns a new `Query` that ends before the provided fields relative to the order of the query. The order of the field values must match the order of the order by clauses of the query.

| Parameters |
|---|---|
| `fieldValues: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>!` | The field values to end this query before, in order of the query's order by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### endBefore

```
fun endBefore(snapshot: DocumentSnapshot): Query
```

Creates and returns a new `Query` that ends before the provided document (exclusive). The end position is relative to the order of the query. The document must contain all of the fields provided in the orderBy of this query.

| Parameters |
|---|---|
| `snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot` | The snapshot of the document to end before. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### equals

```
fun equals(o: Any!): Boolean
```

### get

```
fun get(): Task<QuerySnapshot!>
```

Executes the query and returns the results as a `QuerySnapshot`.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot!>` | A Task that will be resolved with the results of the `Query`. |

### get

```
fun get(source: Source): Task<QuerySnapshot!>
```

Executes the query and returns the results as a `QuerySnapshot`.

By default, `get()` attempts to provide up-to-date data when possible by waiting for data from the server, but it may return cached data or fail if you are offline and the server cannot be reached. This behavior can be altered via the `Source` parameter.

| Parameters |
|---|---|
| `source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Source` | A value to configure the get behavior. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/QuerySnapshot!>` | A Task that will be resolved with the results of the `Query`. |

### hashCode

```
fun hashCode(): Int
```

### limit

```
fun limit(limit: Long): Query
```

Creates and returns a new `Query` that only returns the first matching documents up to the specified number.

| Parameters |
|---|---|
| `limit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The maximum number of items to return. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### limitToLast

```
fun limitToLast(limit: Long): Query
```

Creates and returns a new `Query` that only returns the last matching documents up to the specified number.

You must specify at least one `orderBy` clause for `limitToLast` queries, otherwise an exception will be thrown during execution.

| Parameters |
|---|---|
| `limit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The maximum number of items to return. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### orderBy

```
fun orderBy(field: String): Query
```

Creates and returns a new `Query` that's additionally sorted by the specified field.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field to sort by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### orderBy

```
fun orderBy(fieldPath: FieldPath): Query
```

Creates and returns a new `Query` that's additionally sorted by the specified field.

| Parameters |
|---|---|
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The field to sort by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### orderBy

```
fun orderBy(field: String, direction: Query.Direction): Query
```

Creates and returns a new `Query` that's additionally sorted by the specified field, optionally in descending order instead of ascending.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field to sort by. |
| `direction: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.Direction` | The direction to sort. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### orderBy

```
fun orderBy(fieldPath: FieldPath, direction: Query.Direction): Query
```

Creates and returns a new `Query` that's additionally sorted by the specified field, optionally in descending order instead of ascending.

| Parameters |
|---|---|
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The field to sort by. |
| `direction: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query.Direction` | The direction to sort. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### startAfter

```
fun startAfter(fieldValues: Array<Any!>!): Query
```

Creates and returns a new `Query` that starts after the provided fields relative to the order of the query. The order of the field values must match the order of the order by clauses of the query.

| Parameters |
|---|---|
| `fieldValues: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>!` | The field values to start this query after, in order of the query's order by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### startAfter

```
fun startAfter(snapshot: DocumentSnapshot): Query
```

Creates and returns a new `Query` that starts after the provided document (exclusive). The starting position is relative to the order of the query. The document must contain all of the fields provided in the orderBy of this query.

| Parameters |
|---|---|
| `snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot` | The snapshot of the document to start after. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### startAt

```
fun startAt(fieldValues: Array<Any!>!): Query
```

Creates and returns a new `Query` that starts at the provided fields relative to the order of the query. The order of the field values must match the order of the order by clauses of the query.

| Parameters |
|---|---|
| `fieldValues: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>!` | The field values to start this query at, in order of the query's order by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### startAt

```
fun startAt(snapshot: DocumentSnapshot): Query
```

Creates and returns a new `Query` that starts at the provided document (inclusive). The starting position is relative to the order of the query. The document must contain all of the fields provided in the orderBy of this query.

| Parameters |
|---|---|
| `snapshot: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot` | The snapshot of the document to start at. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### where

```
fun where(filter: Filter): Query
```

Creates and returns a new `Query` with the additional filter.

| Parameters |
|---|---|
| `filter: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Filter` | The new filter to apply to the existing query. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The newly created `Query`. |

### whereArrayContains

```
fun whereArrayContains(field: String, value: Any): Query
```

Creates and returns a new `Query` with the additional filter that documents must contain the specified field, the value must be an array, and that the array must contain the provided value.

A `Query` can have only one `whereArrayContains()` filter and it cannot be combined with `whereArrayContainsAny()`.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing an array to search. |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value that must be contained in the array |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### whereArrayContains

```
fun whereArrayContains(fieldPath: FieldPath, value: Any): Query
```

Creates and returns a new `Query` with the additional filter that documents must contain the specified field, the value must be an array, and that the array must contain the provided value.

A `Query` can have only one `whereArrayContains()` filter and it cannot be combined with `whereArrayContainsAny()`.

| Parameters |
|---|---|
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The path of the field containing an array to search. |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value that must be contained in the array |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### whereArrayContainsAny

```
fun whereArrayContainsAny(field: String, values: (Mutable)List<Any!>): Query
```

Creates and returns a new `Query` with the additional filter that documents must contain the specified field, the value must be an array, and that the array must contain at least one value from the provided list.

A `Query` can have only one `whereArrayContainsAny()` filter and it cannot be combined with `whereArrayContains()` or `whereIn()`.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing an array to search. |
| `values: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>` | The list that contains the values to match. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### whereArrayContainsAny

```
fun whereArrayContainsAny(fieldPath: FieldPath, values: (Mutable)List<Any!>): Query
```

Creates and returns a new `Query` with the additional filter that documents must contain the specified field, the value must be an array, and that the array must contain at least one value from the provided list.

A `Query` can have only one `whereArrayContainsAny()` filter and it cannot be combined with `whereArrayContains()` or `whereIn()`.

| Parameters |
|---|---|
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The path of the field containing an array to search. |
| `values: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>` | The list that contains the values to match. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### whereEqualTo

```
fun whereEqualTo(field: String, value: Any?): Query
```

Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value should be equal to the specified value.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field to compare |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The value for comparison |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### whereEqualTo

```
fun whereEqualTo(fieldPath: FieldPath, value: Any?): Query
```

Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value should be equal to the specified value.

| Parameters |
|---|---|
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The path of the field to compare |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The value for comparison |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### whereGreaterThan

```
fun whereGreaterThan(field: String, value: Any): Query
```

Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value should be greater than the specified value.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field to compare |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value for comparison |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### whereGreaterThan

```
fun whereGreaterThan(fieldPath: FieldPath, value: Any): Query
```

Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value should be greater than the specified value.

| Parameters |
|---|---|
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The path of the field to compare |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value for comparison |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### whereGreaterThanOrEqualTo

```
fun whereGreaterThanOrEqualTo(field: String, value: Any): Query
```

Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value should be greater than or equal to the specified value.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field to compare |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value for comparison |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### whereGreaterThanOrEqualTo

```
fun whereGreaterThanOrEqualTo(fieldPath: FieldPath, value: Any): Query
```

Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value should be greater than or equal to the specified value.

| Parameters |
|---|---|
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The path of the field to compare |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value for comparison |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### whereIn

```
fun whereIn(field: String, values: (Mutable)List<Any!>): Query
```

Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value must equal one of the values from the provided list.

A `Query` can have only one `whereIn()` filter, and it cannot be combined with `whereArrayContainsAny()`.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field to search. |
| `values: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>` | The list that contains the values to match. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### whereIn

```
fun whereIn(fieldPath: FieldPath, values: (Mutable)List<Any!>): Query
```

Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value must equal one of the values from the provided list.

A `Query` can have only one `whereIn()` filter, and it cannot be combined with `whereArrayContainsAny()`.

| Parameters |
|---|---|
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The path of the field to search. |
| `values: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>` | The list that contains the values to match. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### whereLessThan

```
fun whereLessThan(field: String, value: Any): Query
```

Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value should be less than the specified value.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field to compare |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value for comparison |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### whereLessThan

```
fun whereLessThan(fieldPath: FieldPath, value: Any): Query
```

Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value should be less than the specified value.

| Parameters |
|---|---|
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The path of the field to compare |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value for comparison |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### whereLessThanOrEqualTo

```
fun whereLessThanOrEqualTo(field: String, value: Any): Query
```

Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value should be less than or equal to the specified value.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field to compare |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value for comparison |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### whereLessThanOrEqualTo

```
fun whereLessThanOrEqualTo(fieldPath: FieldPath, value: Any): Query
```

Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value should be less than or equal to the specified value.

| Parameters |
|---|---|
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The path of the field to compare |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value for comparison |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### whereNotEqualTo

```
fun whereNotEqualTo(field: String, value: Any?): Query
```

Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value does not equal the specified value.

A `Query` can have only one `whereNotEqualTo()` filter, and it cannot be combined with `whereNotIn()`.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field to compare |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The value for comparison |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### whereNotEqualTo

```
fun whereNotEqualTo(fieldPath: FieldPath, value: Any?): Query
```

Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value does not equal the specified value.

A `Query` can have only one `whereNotEqualTo()` filter, and it cannot be combined with `whereNotIn()`.

| Parameters |
|---|---|
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The path of the field to compare |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The value for comparison |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### whereNotIn

```
fun whereNotIn(field: String, values: (Mutable)List<Any!>): Query
```

Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value does not equal any of the values from the provided list.

One special case is that `whereNotIn` cannot match `null` values. To query for documents where a field exists and is `null`, use `whereNotEqualTo`, which can handle this special case.

A `Query` can have only one `whereNotIn()` filter, and it cannot be combined with `whereArrayContains()`, `whereArrayContainsAny()`, `whereIn()`, or `whereNotEqualTo()`.

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field to search. |
| `values: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>` | The list that contains the values to match. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

### whereNotIn

```
fun whereNotIn(fieldPath: FieldPath, values: (Mutable)List<Any!>): Query
```

Creates and returns a new `Query` with the additional filter that documents must contain the specified field and the value does not equal any of the values from the provided list.

One special case is that `whereNotIn` cannot match `null` values. To query for documents where a field exists and is `null`, use `whereNotEqualTo`, which can handle this special case.

A `Query` can have only one `whereNotIn()` filter, and it cannot be combined with `whereArrayContains()`, `whereArrayContainsAny()`, `whereIn()`, or `whereNotEqualTo()`.

| Parameters |
|---|---|
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The path of the field to search. |
| `values: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>` | The list that contains the values to match. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | The created `Query`. |

## Public properties

### firestore

```
val firestore: FirebaseFirestore!
```

## Extension functions

### dataObjects

```
inline fun <T : Any> Query.dataObjects(
    metadataChanges: MetadataChanges = MetadataChanges.EXCLUDE
): Flow<List<T>>
```

Starts listening to this query with the given options and emits its values converted to a POJO via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener` will be attached.

- When the flow completes, the listener will be removed.

| Parameters |
|---|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The type of the object to convert to. |
| `metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges = MetadataChanges.EXCLUDE` | controls metadata-only changes. Default: `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges#EXCLUDE` |

### snapshots

```
fun Query.snapshots(
    metadataChanges: MetadataChanges = MetadataChanges.EXCLUDE
): Flow<QuerySnapshot>
```

Starts listening to this query with the given options and emits its values via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`.

- When the returned flow starts being collected, an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/EventListener` will be attached.

- When the flow completes, the listener will be removed.

| Parameters |
|---|---|
| `metadataChanges: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges = MetadataChanges.EXCLUDE` | controls metadata-only changes. Default: `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MetadataChanges#EXCLUDE` |