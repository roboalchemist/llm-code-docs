# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/aggregate-query.md.txt

# Firebase.Firestore.AggregateQuery Class Reference

# Firebase.Firestore.AggregateQuery

A query that calculates aggregations over an underlying query.

## Summary

|                                                                                                                                                                                                 ### Public attributes                                                                                                                                                                                                 ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Query](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/aggregate-query#class_firebase_1_1_firestore_1_1_aggregate_query_1af02703a6994c78a0d2585aec079249c7)` => new Query(_proxy.query(), _firestore)` | [Query](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query) The query of aggregations that will be calculated. |

|                                                                                                                                                                                                                                                                                                   ### Public functions                                                                                                                                                                                                                                                                                                    ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Equals](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/aggregate-query#class_firebase_1_1_firestore_1_1_aggregate_query_1aadf02c69ccc2536b32e2f01424a4c21a)`(object obj)`                                                                                                                                                                              | `override bool`                                                                                                                                                                                                                       |
| [Equals](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/aggregate-query#class_firebase_1_1_firestore_1_1_aggregate_query_1a5f46c3a976e753aacf97c0e882cdef64)`(`[AggregateQuery](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/aggregate-query#class_firebase_1_1_firestore_1_1_aggregate_query)` other)`                    | `bool` Compares this aggregate query with another for equality.                                                                                                                                                                       |
| [GetHashCode](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/aggregate-query#class_firebase_1_1_firestore_1_1_aggregate_query_1afc85b700480e5983d656a468b3227507)`()`                                                                                                                                                                                   | `override int`                                                                                                                                                                                                                        |
| [GetSnapshotAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/aggregate-query#class_firebase_1_1_firestore_1_1_aggregate_query_1a997ce2841fd11585f1424fbde7884d05)`(`[AggregateSource](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore_1a026b0f28c2b3d36b66f1a3fbc6cb8646)` source)` | `Task< `[AggregateQuerySnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/aggregate-query-snapshot#class_firebase_1_1_firestore_1_1_aggregate_query_snapshot)` >` Asynchronously executes the query. |

## Public attributes

### Query

```c#
Query Query => new Query(_proxy.query(), _firestore)
```  
The query of aggregations that will be calculated.

## Public functions

### Equals

```c#
override bool Equals(
  object obj
)
```  

### Equals

```c#
bool Equals(
  AggregateQuery other
)
```  
Compares this aggregate query with another for equality.

<br />

|                                                               Details                                                                ||
|-------------|-------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|-----------------------------------------------| | `other` | The aggregate query to compare this one with. | |
| **Returns** | `true` if this aggregate query is equal to *other* ; `false` otherwise.                                                 |

### GetHashCode

```c#
override int GetHashCode()
```  

### GetSnapshotAsync

```c#
Task< AggregateQuerySnapshot > GetSnapshotAsync(
  AggregateSource source
)
```  
Asynchronously executes the query.

<br />

|                                                                          Details                                                                           ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |----------|---------------------------------------------------------| | `source` | The source from which to acquire the aggregate results. | |
| **Returns** | The results of the query.                                                                                                                     |