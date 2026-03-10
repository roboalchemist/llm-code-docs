# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change.md.txt

# firebase::firestore::DocumentChange Class Reference

# firebase::firestore::DocumentChange


`#include <document_change.h>`

A [DocumentChange](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change) represents a change to the documents matching a query.

## Summary

[DocumentChange](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change) contains the document affected and the type of change that occurred (added, modified, or removed).


> [!NOTE]
> **Note:** [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

<br />

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change_1a6d3683a5aee3ede7a5dc09e7e65f86b5()` Creates an invalid [DocumentChange](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change) that has to be reassigned before it can be used. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change_1aeeffacb865746b754ca6da8450bff1e4(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change & other)` Copy constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change_1a3decd36de27096650b60b8eaae37367a(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change && other)` Move constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change_1a2f386dd3d68a9c3a0ebc5588eb2e16b7()` ||

| ### Public types ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change_1ac97ee985130fa84cbf305fb4d7555454{ https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change_1ac97ee985130fa84cbf305fb4d7555454a300b0905bab3778110ad4f255e268e64, https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change_1ac97ee985130fa84cbf305fb4d7555454aea9bda5c5f60cbfacdd0e1427c1a8dfb, https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change_1ac97ee985130fa84cbf305fb4d7555454a4f44be333b6269b33c50c45819e5dc82 }` | enumAn enumeration of snapshot diff types. |

| ### Public static attributes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change_1aa28f7435efe5d3b0ce79b4c532ee9568 = static_cast(-1)` | `constexpr std::size_t` The sentinel index used as a return value to indicate no matches. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change_1a89482f39c01f69d055a3ae6ca18a1fa9() const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot` The document affected by this change. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change_1aa47e0cf9dc948982b3f264ddc286f143() const ` | `bool` Returns true if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change` is valid, false if it is not valid. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change_1a6c3596a03dec8eea4adc4c17cb2fb3c1() const ` | `virtual std::size_t` The index of the changed document in the result set immediately after this [DocumentChange](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change) (that is, supposing that all prior [DocumentChange](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change) objects and the current [DocumentChange](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change) object have been applied). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change_1a56c71905f58a61f97e8d596c7e616cee() const ` | `virtual std::size_t` The index of the changed document in the result set immediately prior to this [DocumentChange](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change) (that is, supposing that all prior [DocumentChange](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change) objects have been applied). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change_1aa7fe87aa8d567c4f2d3b1689b32994af(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change & other)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change &` Copy assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change_1a50598413ac09837d7f2256065377298d(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change && other)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change &` Move assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change_1a717db7e56debe51a1bff562493d9f308() const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change_1ac97ee985130fa84cbf305fb4d7555454` Returns the type of change that occurred (added, modified, or removed). |

## Public types

### Type

```c++
 Type
```
An enumeration of snapshot diff types.

| Properties ||
|---|---|
| `kAdded` | Indicates a new document was added to the set of documents matching the query. |
| `kModified` | Indicates a document within the query was modified. |
| `kRemoved` | Indicates a document within the query was removed (either deleted or no longer matches the query). |

## Public static attributes

### npos

```c++
constexpr std::size_t npos = static_cast<std::size_t>(-1)
```
The sentinel index used as a return value to indicate no matches.

## Public functions

### DocumentChange

```c++
 DocumentChange()
```
Creates an invalid [DocumentChange](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change) that has to be reassigned before it can be used.

Calling any member function on an invalid [DocumentChange](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change) will be a no-op. If the function returns a value, it will return a zero, empty, or invalid value, depending on the type of the value.

### DocumentChange

```c++
 DocumentChange(
  const DocumentChange & other
)
```
Copy constructor.

`https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change` is immutable and can be efficiently copied (no deep copy is performed).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change` to copy from. | |

### DocumentChange

```c++
 DocumentChange(
  DocumentChange && other
)
```
Move constructor.

Moving is more efficient than copying for a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change`. After being moved from, a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change` is equivalent to its default-constructed state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change` to move data from. | |

### document

```c++
virtual DocumentSnapshot document() const 
```
The document affected by this change.

Returns the newly added or modified document if this [DocumentChange](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change) is for an updated document. Returns the deleted document if this document change represents a removal.

### is_valid

```c++
bool is_valid() const 
```
Returns true if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change` is valid, false if it is not valid.

An invalid `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change` could be the result of:

- Creating a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change` using the default constructor.
- Moving from the `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change`.
- Deleting your [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance, which will invalidate all the `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change` instances associated with it.

<br />

<br />

| Details ||
|---|---|
| **Returns** | true if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change` is valid, false if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change` is invalid. |

### new_index

```c++
virtual std::size_t new_index() const 
```
The index of the changed document in the result set immediately after this [DocumentChange](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change) (that is, supposing that all prior [DocumentChange](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change) objects and the current [DocumentChange](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change) object have been applied).

Returns [DocumentChange::npos](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change_1aa28f7435efe5d3b0ce79b4c532ee9568) for 'removed' events.

### old_index

```c++
virtual std::size_t old_index() const 
```
The index of the changed document in the result set immediately prior to this [DocumentChange](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change) (that is, supposing that all prior [DocumentChange](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change) objects have been applied).

Returns [DocumentChange::npos](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change_1aa28f7435efe5d3b0ce79b4c532ee9568) for 'added' events.

### operator=

```c++
DocumentChange & operator=(
  const DocumentChange & other
)
```
Copy assignment operator.

`https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change` is immutable and can be efficiently copied (no deep copy is performed).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change` to copy from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change`. |

### operator=

```c++
DocumentChange & operator=(
  DocumentChange && other
)
```
Move assignment operator.

Moving is more efficient than copying for a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change`. After being moved from, a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change` is equivalent to its default-constructed state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change` to move data from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change#classfirebase_1_1firestore_1_1_document_change`. |

### type

```c++
virtual Type type() const 
```
Returns the type of change that occurred (added, modified, or removed).

### \~DocumentChange

```c++
virtual  ~DocumentChange()
```