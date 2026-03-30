# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery.md.txt

# AggregateQuery

# AggregateQuery


```
public class AggregateQuery
```

<br />

*** ** * ** ***

A query that calculates aggregations over an underlying query.

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery#query()` |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery#equals(java.lang.Object)(https://developer.android.com/reference/kotlin/java/lang/Object.html object)` Compares this object with the given object for equality. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery#get(com.google.firebase.firestore.AggregateSource)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateSource source)` Executes this query. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery#getQuery()()` Returns the query whose aggregations will be calculated by this object. |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery#hashCode()()` Calculates and returns the hash code for this object. |

## Public fields

### query

```
public final @NonNull Query query
```

## Public methods

### equals

```
public boolean equals(Object object)
```

Compares this object with the given object for equality.

This object is considered "equal" to the other object if and only if all of the following conditions are satisfied:

1. `object` is a non-null instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery`.
2. `object` performs the same aggregations as this `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery`.
3. The underlying `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query` of `object` compares equal to that of this object.

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/Object.html object` | The object to compare to this object for equality. |

| Returns |
|---|---|
| `boolean` | `true` if this object is "equal" to the given object, as defined above, or ` false` otherwise. |

### get

```
public @NonNull Task<AggregateQuerySnapshot> get(@NonNull AggregateSource source)
```

Executes this query.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateSource source` | The source from which to acquire the aggregate results. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuerySnapshot>` | A `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` that will be resolved with the results of the query. |

### getQuery

```
public @NonNull Query getQuery()
```

Returns the query whose aggregations will be calculated by this object.

### hashCode

```
public int hashCode()
```

Calculates and returns the hash code for this object.

| Returns |
|---|---|
| `int` | the hash code for this object. |