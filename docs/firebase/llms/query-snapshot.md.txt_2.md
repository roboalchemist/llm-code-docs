# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot.md.txt

# firebase::firestore::QuerySnapshot Class Reference

# firebase::firestore::QuerySnapshot


`#include <query_snapshot.h>`

A [QuerySnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot) contains zero or more [DocumentSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot) objects.

## Summary

[QuerySnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot) can be iterated using a range-based for loop, and its size can be inspected with [empty()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot_1a5f523037391d146fdac5bdf39ba47f1e) and [size()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot_1a826f774294c18369d6bbd7b4c790e16f).


> [!NOTE]
> **Note:** [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

<br />

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot_1aadb1451783edc6a6585ba255fe8d70af()` Creates an invalid [QuerySnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot) that has to be reassigned before it can be used. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot_1a5fcec63cda426898ed071b0669dbe3b0(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot & other)` Copy constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot_1a092feef2ecf7942404beaf56fe7b7b00(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot && other)` Move constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot_1a8bd4017019c0344dad9c4f8b065a1b0a()` ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot_1af1f23e166e2676e4748e3097aeb843d3(https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1a9f0a586c44417cd24932561719c97f54 metadata_changes) const ` | `virtual std::vector< https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change >` The list of documents that changed since the last snapshot. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot_1af9f302e8517bb4f449723227a46b1f1d() const ` | `virtual std::vector< https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot >` The list of documents in this [QuerySnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot) in order of the query. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot_1a5f523037391d146fdac5bdf39ba47f1e() const ` | `bool` Checks the emptiness of the [QuerySnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot_1a0a75fd5f39dd304ac8333ac9b4c8ea86() const ` | `bool` Returns true if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot` is valid, false if it is not valid. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot_1a5dd7c1215e4f11ef4a560190843786cc() const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata` Metadata about this snapshot, concerning its source and if it has local modifications. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot_1a03dc3bdfb55799e5c2f24a9f1501f78f(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot & other)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot &` Copy assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot_1ae6881c93f3643948bebce22ba2c0d1c8(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot && other)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot &` Move assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot_1a397e527ab65eae9b56ab22ea3706dad3() const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` The query from which you got this [QuerySnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot_1a826f774294c18369d6bbd7b4c790e16f() const ` | `virtual std::size_t` Checks the size of the [QuerySnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot). |

## Public functions

### DocumentChanges

```c++
virtual std::vector< DocumentChange > DocumentChanges(
  MetadataChanges metadata_changes
) const 
```
The list of documents that changed since the last snapshot.

If it's the first snapshot, all documents will be in the list as added changes. Documents with changes only to their metadata will not be included.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `metadata_changes` | Indicates whether metadata-only changes (that is, only [QuerySnapshot::metadata()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot_1a5dd7c1215e4f11ef4a560190843786cc) changed) should be included. | |
| **Returns** | The list of document changes since the last snapshot. |

### QuerySnapshot

```c++
 QuerySnapshot()
```
Creates an invalid [QuerySnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot) that has to be reassigned before it can be used.

Calling any member function on an invalid [QuerySnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot) will be a no-op. If the function returns a value, it will return a zero, empty, or invalid value, depending on the type of the value.

### QuerySnapshot

```c++
 QuerySnapshot(
  const QuerySnapshot & other
)
```
Copy constructor.

`https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot` is immutable and can be efficiently copied (no deep copy is performed).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot` to copy from. | |

### QuerySnapshot

```c++
 QuerySnapshot(
  QuerySnapshot && other
)
```
Move constructor.

Moving is more efficient than copying for a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot`. After being moved from, a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot` is equivalent to its default-constructed state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot` to move data from. | |

### documents

```c++
virtual std::vector< DocumentSnapshot > documents() const 
```
The list of documents in this [QuerySnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot) in order of the query.

<br />

| Details ||
|---|---|
| **Returns** | The list of documents. |

### empty

```c++
bool empty() const 
```
Checks the emptiness of the [QuerySnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot).

<br />

| Details ||
|---|---|
| **Returns** | True if there are no documents in the [QuerySnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot). |

### is_valid

```c++
bool is_valid() const 
```
Returns true if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot` is valid, false if it is not valid.

An invalid `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot` could be the result of:

- Creating a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot` using the default constructor.
- Moving from the `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot`.
- Deleting your [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance, which will invalidate all the `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot` instances associated with it.

<br />

<br />

| Details ||
|---|---|
| **Returns** | true if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot` is valid, false if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot` is invalid. |

### metadata

```c++
virtual SnapshotMetadata metadata() const 
```
Metadata about this snapshot, concerning its source and if it has local modifications.

<br />

| Details ||
|---|---|
| **Returns** | The metadata for this document snapshot. |

### operator=

```c++
QuerySnapshot & operator=(
  const QuerySnapshot & other
)
```
Copy assignment operator.

`https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot` is immutable and can be efficiently copied (no deep copy is performed).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot` to copy from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot`. |

### operator=

```c++
QuerySnapshot & operator=(
  QuerySnapshot && other
)
```
Move assignment operator.

Moving is more efficient than copying for a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot`. After being moved from, a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot` is equivalent to its default-constructed state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot` to move data from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot`. |

### query

```c++
virtual Query query() const 
```
The query from which you got this [QuerySnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot).

### size

```c++
virtual std::size_t size() const 
```
Checks the size of the [QuerySnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot).

<br />

| Details ||
|---|---|
| **Returns** | The number of documents in the [QuerySnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot). |

### \~QuerySnapshot

```c++
virtual  ~QuerySnapshot()
```