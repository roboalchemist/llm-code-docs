# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery.md.txt

# AggregateQuery

# AggregateQuery


```
class AggregateQuery
```

<br />

*** ** * ** ***

A query that calculates aggregations over an underlying query.

**Subclassing Note**: Cloud Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery#equals(java.lang.Object)(object: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!)` Compares this object with the given object for equality. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuerySnapshot!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery#get(com.google.firebase.firestore.AggregateSource)(source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateSource)` Executes this query. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery#hashCode()()` Calculates and returns the hash code for this object. |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery#query()` |

## Public functions

### equals

```
fun equals(object: Any!): Boolean
```

Compares this object with the given object for equality.

This object is considered "equal" to the other object if and only if all of the following conditions are satisfied:

1. `object` is a non-null instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery`.
2. `object` performs the same aggregations as this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery`.
3. The underlying `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` of `object` compares equal to that of this object.

| Parameters |
|---|---|
| `object: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!` | The object to compare to this object for equality. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `true` if this object is "equal" to the given object, as defined above, or ` false` otherwise. |

### get

```
fun get(source: AggregateSource): Task<AggregateQuerySnapshot!>
```

Executes this query.

| Parameters |
|---|---|
| `source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateSource` | The source from which to acquire the aggregate results. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuerySnapshot!>` | A `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` that will be resolved with the results of the query. |

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
val query: Query
```