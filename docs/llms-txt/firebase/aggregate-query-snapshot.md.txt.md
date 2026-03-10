# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot.md.txt

# firebase::firestore::AggregateQuerySnapshot Class Reference

# firebase::firestore::AggregateQuerySnapshot


`#include <aggregate_query_snapshot.h>`

The results of executing an [AggregateQuery](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query).

## Summary


> [!NOTE]
> **Note:** [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

<br />

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot_1ace0982a8cdbdf64b54e11cd5da6c9af1()` Creates an invalid [AggregateQuerySnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot) that has to be reassigned before it can be used. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot_1a0a51fc47f8d6ad220ca965acf6fe1f08(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot & other)` Copy constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot_1a2664e0e60f29c04c8222525cf153dea9(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot && other)` Move constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot_1ad305243bcb46bc59fe68e8a384016446()` ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot_1aa7448e493a0dd39759df8bec6d5c33d7() const ` | `virtual int64_t` Returns the number of documents in the result set of the underlying query. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot_1a80b385c9b1d762593cd5210d7c866478() const ` | `bool` Returns true if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot` is valid, false if it is not valid. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot_1ac2655ff4523032203161543788bd472b(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot & other)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot &` Copy assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot_1a939fc713e64e180806f613e71ca7a41a(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot && other)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot &` Move assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot_1ae2ee60a143c3535702b658702d6ebd1f() const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query` Returns the query that was executed to produce this result. |

## Public functions

### AggregateQuerySnapshot

```c++
 AggregateQuerySnapshot()
```
Creates an invalid [AggregateQuerySnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot) that has to be reassigned before it can be used.

Calling any member function on an invalid [AggregateQuerySnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot) will be a no-op. If the function returns a value, it will return a zero, empty, or invalid value, depending on the type of the value.

### AggregateQuerySnapshot

```c++
 AggregateQuerySnapshot(
  const AggregateQuerySnapshot & other
)
```
Copy constructor.

`https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot` is immutable and can be efficiently copied (no deep copy is performed).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot` to copy from. | |

### AggregateQuerySnapshot

```c++
 AggregateQuerySnapshot(
  AggregateQuerySnapshot && other
)
```
Move constructor.

Moving is more efficient than copying for a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot`. After being moved from, a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot` is equivalent to its default-constructed state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot` to move data from. | |

### count

```c++
virtual int64_t count() const 
```
Returns the number of documents in the result set of the underlying query.

<br />

| Details ||
|---|---|
| **Returns** | The number of documents in the result set of the underlying query. |

### is_valid

```c++
bool is_valid() const 
```
Returns true if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot` is valid, false if it is not valid.

An invalid `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot` could be the result of:

- Creating a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot` using the default constructor.
- Moving from the `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot`.
- Deleting your [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance, which will invalidate all the `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot` instances associated with it.

<br />

<br />

| Details ||
|---|---|
| **Returns** | true if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot` is valid, false if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot` is invalid. |

### operator=

```c++
AggregateQuerySnapshot & operator=(
  const AggregateQuerySnapshot & other
)
```
Copy assignment operator.

`https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot` is immutable and can be efficiently copied (no deep copy is performed).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot` to copy from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot`. |

### operator=

```c++
AggregateQuerySnapshot & operator=(
  AggregateQuerySnapshot && other
)
```
Move assignment operator.

Moving is more efficient than copying for a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot`. After being moved from, a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot` is equivalent to its default-constructed state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot` to move data from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query-snapshot#classfirebase_1_1firestore_1_1_aggregate_query_snapshot`. |

### query

```c++
virtual AggregateQuery query() const 
```
Returns the query that was executed to produce this result.

<br />

| Details ||
|---|---|
| **Returns** | The `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query` instance. |

### \~AggregateQuerySnapshot

```c++
virtual  ~AggregateQuerySnapshot()
```