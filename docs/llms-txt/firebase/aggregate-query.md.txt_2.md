# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query.md.txt

# firebase::firestore::AggregateQuery Class Reference

# firebase::firestore::AggregateQuery


`#include <aggregate_query.h>`

A query that calculates aggregations over an underlying query.

## Summary

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query_1aee5c8871825f7c886c66fb6cfada4597()` Creates an invalid [AggregateQuery](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query) that has to be reassigned before it can be used. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query_1a856e7973d4057f51bb6bc98a256a5903(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query & other)` Copy constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query_1a28b9b5955f14afb8c826298d2e6a71ee(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query && other)` Move constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query_1aa2becbf746eea94429cdf5425d79342c()` ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query_1a27c07d290606716096491dd95eb40bb5(https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1a1d6797da13a16683507ee70cf1702178 aggregate_source) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot >` Executes this query. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query_1a68dda2f917c7f3f2a7a8d2d0c6adc3ff() const ` | `bool` Returns true if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query` is valid, false if it is not valid. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query_1ae26b6774b98cc9d1fcc7d4808ecc4830(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query & other)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query &` Copy assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query_1a9475861d77b27867b6f039f43acd0d10(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query && other)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query &` Move assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query_1a0a9c10f5922478c121c3e9cc4e5befab() const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Returns the query whose aggregations will be calculated by this object. |

## Public functions

### AggregateQuery

```c++
 AggregateQuery()
```
Creates an invalid [AggregateQuery](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query) that has to be reassigned before it can be used.

Calling any member function on an invalid [AggregateQuery](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query) will be a no-op. If the function returns a value, it will return a zero, empty, or invalid value, depending on the type of the value.

### AggregateQuery

```c++
 AggregateQuery(
  const AggregateQuery & other
)
```
Copy constructor.

`https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query` is immutable and can be efficiently copied (no deep copy is performed).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query` to copy from. | |

### AggregateQuery

```c++
 AggregateQuery(
  AggregateQuery && other
)
```
Move constructor.

Moving is more efficient than copying for a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query`. After being moved from, a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query` is equivalent to its default-constructed state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query` to move data from. | |

### Get

```c++
virtual Future< AggregateQuerySnapshot > Get(
  AggregateSource aggregate_source
) const 
```
Executes this query.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `aggregate_source` | The source from which to acquire the aggregate results. | |
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) that will be resolved with the results of the [AggregateQuery](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query). |

### is_valid

```c++
bool is_valid() const 
```
Returns true if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query` is valid, false if it is not valid.

An invalid `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query` could be the result of:

- Creating a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query` using the default constructor.
- Moving from the `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query`.
- Deleting your [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance, which will invalidate all the `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query` instances associated with it.

<br />

<br />

| Details ||
|---|---|
| **Returns** | true if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query` is valid, false if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query` is invalid. |

### operator=

```c++
AggregateQuery & operator=(
  const AggregateQuery & other
)
```
Copy assignment operator.

`https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query` is immutable and can be efficiently copied (no deep copy is performed).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query` to copy from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query`. |

### operator=

```c++
AggregateQuery & operator=(
  AggregateQuery && other
)
```
Move assignment operator.

Moving is more efficient than copying for a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query`. After being moved from, a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query` is equivalent to its default-constructed state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query` to move data from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query`. |

### query

```c++
virtual Query query() const 
```
Returns the query whose aggregations will be calculated by this object.

### \~AggregateQuery

```c++
virtual  ~AggregateQuery()
```