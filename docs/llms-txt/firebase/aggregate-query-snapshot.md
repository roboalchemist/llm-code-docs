# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/aggregate-query-snapshot.md.txt

# Firebase.Firestore.AggregateQuerySnapshot Class Reference

# Firebase.Firestore.AggregateQuerySnapshot

The results of executing an [AggregateQuerySnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/aggregate-query-snapshot#class_firebase_1_1_firestore_1_1_aggregate_query_snapshot).

## Summary

|                                                                                                                                                                                                           ### Properties                                                                                                                                                                                                           ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Count](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/aggregate-query-snapshot#class_firebase_1_1_firestore_1_1_aggregate_query_snapshot_1a936427886f8c133023ec7d6f5e80c4e4) | `long` Returns the number of documents in the result set of the underlying query.                                                                                                                                        |
| [Query](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/aggregate-query-snapshot#class_firebase_1_1_firestore_1_1_aggregate_query_snapshot_1a5cdaa0bbf44b1b1be4ab040c5e05898b) | [AggregateQuery](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/aggregate-query#class_firebase_1_1_firestore_1_1_aggregate_query) Returns the query that was executed to produce this result. |

|                                                                                                                                                                                                                              ### Public functions                                                                                                                                                                                                                               ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| [Equals](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/aggregate-query-snapshot#class_firebase_1_1_firestore_1_1_aggregate_query_snapshot_1aa036415bc531011246524c73d7473ef9)`(object obj)`                                                                                                                                                                                     | `override bool`                                                    |
| [Equals](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/aggregate-query-snapshot#class_firebase_1_1_firestore_1_1_aggregate_query_snapshot_1aaef7374042f21d1d73b911ce0f0d1320)`(`[AggregateQuerySnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/aggregate-query-snapshot#class_firebase_1_1_firestore_1_1_aggregate_query_snapshot)` other)` | `bool` Compares this aggregate snapshot with another for equality. |
| [GetHashCode](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/aggregate-query-snapshot#class_firebase_1_1_firestore_1_1_aggregate_query_snapshot_1a379cb946eaa1343ae825b8845b88c8e5)`()`                                                                                                                                                                                          | `override int`                                                     |

## Properties

### Count

```c#
long Count
```  
Returns the number of documents in the result set of the underlying query.  

### Query

```c#
AggregateQuery Query
```  
Returns the query that was executed to produce this result.

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
  AggregateQuerySnapshot other
)
```  
Compares this aggregate snapshot with another for equality.

<br />

|                                                                  Details                                                                   ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|--------------------------------------------------| | `other` | The aggregate snapshot to compare this one with. | |
| **Returns** | `true` if this aggregate snapshot is equal to *other* ; `false` otherwise.                                                    |

### GetHashCode

```c#
override int GetHashCode()
```