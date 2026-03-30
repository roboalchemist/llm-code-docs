# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot.md.txt

# firebase::firestore::DocumentSnapshot Class Reference

# firebase::firestore::DocumentSnapshot


`#include <document_snapshot.h>`

A [DocumentSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot) contains data read from a document in your [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) database.

## Summary

The data can be extracted with the [GetData()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a575b4e055541ecfb98f0621aa53c5f01) method, or by using [Get()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a75ca512289bd37032c0d30e222e07bcf) to access a specific field. For a [DocumentSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot) that points to a non-existing document, any data access will cause a failed assertion. You can use the [exists()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1ab146e7fc6be4d8e8811736e69fd56b1a) method to explicitly verify a document's existence.


> [!NOTE]
> **Note:** [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

<br />

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a67630ae23e5a868ddfe5ba7338127d9d()` Creates an invalid [DocumentSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot) that has to be reassigned before it can be used. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a6905edc91cac986a38efc35773c097e8(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot & other)` Copy constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1ae5d569f37c9722be9cf1f645970e5d48(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot && other)` Move constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a7daf47f116e0419236401fd0bda72dd4()` ||

| ### Public types ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a970e228d506154b17acb6e4de23b74a6{ https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a970e228d506154b17acb6e4de23b74a6a35c3ace1970663a16e5c65baa5941b13 = 0, https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a970e228d506154b17acb6e4de23b74a6a41d151799285ce4bb188edddd6bbec21, https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a970e228d506154b17acb6e4de23b74a6af8592f8ed8f28974b275c9c396700a85, https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a970e228d506154b17acb6e4de23b74a6a6867faeaa475fda467e48267db2bb8a8 = 0 }` | enumControls the return value for server timestamps that have not yet been set to their final value. |

| ### Friend classes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1aff4515b5dcce93944e98eb8cd45a4a88` | `friend std::ostream &` Outputs the string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot` to the given stream. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a75ca512289bd37032c0d30e222e07bcf(const char *field, https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a970e228d506154b17acb6e4de23b74a6 stb) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` Retrieves a specific field from the document. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a3362fe71941a50bb94affce0adbfadc2(const std::string & field, https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a970e228d506154b17acb6e4de23b74a6 stb) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` Retrieves a specific field from the document. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a84ce92407ec6ef9422f761d2e5c5942b(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path & field, https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a970e228d506154b17acb6e4de23b74a6 stb) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` Retrieves a specific field from the document. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a575b4e055541ecfb98f0621aa53c5f01(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a970e228d506154b17acb6e4de23b74a6 stb) const ` | `virtual https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1a8c836c76e7e87d8021bf3b33c8a71c7c` Retrieves all fields in the document as a map of FieldValues. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a666d61cdb298554dc9836e9b56d24b97() const ` | `std::string` Returns a string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot` for logging/debugging purposes. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1ab146e7fc6be4d8e8811736e69fd56b1a() const ` | `virtual bool` Explicitly verify a document's existence. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a69a344499885e6df9392d752e7fba87e() const ` | `virtual const std::string &` Returns the string ID of the document for which this [DocumentSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot) contains data. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1ac93e46d7e692b520f2a148a2153b8bb7() const ` | `bool` Returns true if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot` is valid, false if it is not valid. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a6e8881817cf1fdd48fe5603c74fe9aae() const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata` Returns the metadata about this snapshot concerning its source and if it has local modifications. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a15ae9030c82c5335e6422128f3ecd9c0(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot & other)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot &` Copy assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a936078e3a09837b7ec0a45d32733d4ef(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot && other)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot &` Move assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a81c9ae6c6fc28b9f3bd97f854aaf6a4c() const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` Returns the document location for which this [DocumentSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot) contains data. |

## Public types

### ServerTimestampBehavior

```c++
 ServerTimestampBehavior
```
Controls the return value for server timestamps that have not yet been set to their final value.

| Properties ||
|---|---|
| `kDefault` | The default behavior, which is equivalent to specifying kNone. |
| `kEstimate` | Return local estimates for server timestamps that have not yet been set to their final value. This estimate will likely differ from the final value and may cause these pending values to change once the server result becomes available. |
| `kNone` | Return Null for server timestamps that have not yet been set to their final value. |
| `kPrevious` | Return the previous value for server timestamps that have not yet been set to their final value. |

## Friend classes

### operator\<\<

```c++
friend std::ostream & operator<<(std::ostream &out, const DocumentSnapshot &document)
```
Outputs the string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot` to the given stream.

**See also:** `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a666d61cdb298554dc9836e9b56d24b97` for comments on the representation format.

## Public functions

### DocumentSnapshot

```c++
 DocumentSnapshot()
```
Creates an invalid [DocumentSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot) that has to be reassigned before it can be used.

Calling any member function on an invalid [DocumentSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot) will be a no-op. If the function returns a value, it will return a zero, empty, or invalid value, depending on the type of the value.

### DocumentSnapshot

```c++
 DocumentSnapshot(
  const DocumentSnapshot & other
)
```
Copy constructor.

`https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot` is immutable and can be efficiently copied (no deep copy is performed).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot` to copy from. | |

### DocumentSnapshot

```c++
 DocumentSnapshot(
  DocumentSnapshot && other
)
```
Move constructor.

Moving is more efficient than copying for a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot`. After being moved from, a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot` is equivalent to its default-constructed state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot` to move data from. | |

### Get

```c++
virtual FieldValue Get(
  const char *field,
  ServerTimestampBehavior stb
) const 
```
Retrieves a specific field from the document.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | String ID of the field to retrieve. The pointer only needs to be valid during this call. | | `stb` | Configures how server timestamps that have not yet been set to their final value are returned from the snapshot (optional). | |
| **Returns** | The value contained in the field. If the field does not exist in the document, then a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` instance with `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1ac93e46d7e692b520f2a148a2153b8bb7 == false` will be returned. |

### Get

```c++
virtual FieldValue Get(
  const std::string & field,
  ServerTimestampBehavior stb
) const 
```
Retrieves a specific field from the document.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | String ID of the field to retrieve. | | `stb` | Configures how server timestamps that have not yet been set to their final value are returned from the snapshot (optional). | |
| **Returns** | The value contained in the field. If the field does not exist in the document, then a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` instance with `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1ac93e46d7e692b520f2a148a2153b8bb7 == false` will be returned. |

### Get

```c++
virtual FieldValue Get(
  const FieldPath & field,
  ServerTimestampBehavior stb
) const 
```
Retrieves a specific field from the document.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | Path of the field to retrieve. | | `stb` | Configures how server timestamps that have not yet been set to their final value are returned from the snapshot (optional). | |
| **Returns** | The value contained in the field. If the field does not exist in the document, then a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value` instance with `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1ac93e46d7e692b520f2a148a2153b8bb7 == false` will be returned. |

### GetData

```c++
virtual MapFieldValue GetData(
  ServerTimestampBehavior stb
) const 
```
Retrieves all fields in the document as a map of FieldValues.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `stb` | Configures how server timestamps that have not yet been set to their final value are returned from the snapshot (optional). | |
| **Returns** | A map containing all fields in the document, or an empty map if the document doesn't exist. |

### ToString

```c++
std::string ToString() const 
```
Returns a string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot` for logging/debugging purposes.


> [!NOTE]
> **Note:** the exact string representation is unspecified and subject to change; don't rely on the format of the string.

<br />

### exists

```c++
virtual bool exists() const 
```
Explicitly verify a document's existence.

<br />

| Details ||
|---|---|
| **Returns** | True if the document exists in this snapshot. |

### id

```c++
virtual const std::string & id() const 
```
Returns the string ID of the document for which this [DocumentSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot) contains data.

<br />

| Details ||
|---|---|
| **Returns** | String ID of this document location. |

### is_valid

```c++
bool is_valid() const 
```
Returns true if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot` is valid, false if it is not valid.

An invalid `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot` could be the result of:

- Creating a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot` with the default constructor.
- Moving from the `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot`.
- Deleting your [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance, which will invalidate all the `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot` instances associated with it.

<br />

<br />

| Details ||
|---|---|
| **Returns** | true if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot` is valid, false if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot` is invalid. |

### metadata

```c++
virtual SnapshotMetadata metadata() const 
```
Returns the metadata about this snapshot concerning its source and if it has local modifications.

<br />

| Details ||
|---|---|
| **Returns** | [SnapshotMetadata](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/snapshot-metadata#classfirebase_1_1firestore_1_1_snapshot_metadata) about this snapshot. |

### operator=

```c++
DocumentSnapshot & operator=(
  const DocumentSnapshot & other
)
```
Copy assignment operator.

`https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot` is immutable and can be efficiently copied (no deep copy is performed).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot` to copy from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot`. |

### operator=

```c++
DocumentSnapshot & operator=(
  DocumentSnapshot && other
)
```
Move assignment operator.

Moving is more efficient than copying for a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot`. After being moved from, a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot` is equivalent to its default-constructed state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot` to move data from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot`. |

### reference

```c++
virtual DocumentReference reference() const 
```
Returns the document location for which this [DocumentSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot) contains data.

<br />

| Details ||
|---|---|
| **Returns** | [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) of this document location. |

### \~DocumentSnapshot

```c++
virtual  ~DocumentSnapshot()
```