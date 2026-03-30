# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference.md.txt

# firebase::firestore::DocumentReference Class Reference

# firebase::firestore::DocumentReference


`#include <document_reference.h>`

A [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) refers to a document location in a [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) database and can be used to write, read, or listen to the location.

## Summary

There may or may not exist a document at the referenced location. A [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) can also be used to create a [CollectionReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference) to a subcollection.

Create a [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) via `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1a0b6c26a1ca9f4d56e741083f21c24162(const std::string& path)`.


> [!NOTE]
> **Note:** [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

<br />

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1afe92a224cd813909d20e7290917cc8f4()` Creates an invalid [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) that has to be reassigned before it can be used. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1a2db2c2b9f3d21c3711864ad7d08cdd2d(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference & other)` Copy constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1a7cf74014f365e98409a7e6b004242f49(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference && other)` Move constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1aeee319887878deab13ab5075b70f1a65()` ||

| ### Friend classes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1a353c19045ca053d28887ee58b7ea317f` | `friend std::ostream &` Outputs the string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` to the given stream. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1a3e145c34e25474ff912aba9b18d6517e(std::function< void(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot &, https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1acbed0dcd73b55ce5a9d9c3d07bb9cac5, const std::string &)> callback)` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration` Starts listening to the document referenced by this [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1ac8317928a827cac59f7c51e66f8a517b(https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1a9f0a586c44417cd24932561719c97f54 metadata_changes, std::function< void(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot &, https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1acbed0dcd73b55ce5a9d9c3d07bb9cac5, const std::string &)> callback)` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration` Starts listening to the document referenced by this [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1ad04ee32464ec295fd71fd1409866d7c6(const char *collection_path) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference` Returns a [CollectionReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference) instance that refers to the subcollection at the specified path relative to this document. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1a8139cb66ae7c1df589c7e4e1c1a745f3(const std::string & collection_path) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference` Returns a [CollectionReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference) instance that refers to the subcollection at the specified path relative to this document. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1a71dd14d26309c0dbd55a4ecf376de88d()` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Removes the document referred to by this [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1a7c1711d91dd8e025642bb1bc793dc6c8(https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1a706b13a274f8586c90167ba6073e5c66 source) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot >` Reads the document referenced by this [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1aff18b0d9daec23d0070704ea780d6baa() const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference` Returns a [CollectionReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference) to the collection that contains this document. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1ace49a9db5c4c1f68ab85a36b1738eebc(const https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1a8c836c76e7e87d8021bf3b33c8a71c7c & data, const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options & options)` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Writes to the document referred to by this [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1a685340cad727bee31464b81ebf558cef() const ` | `std::string` Returns a string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` for logging/debugging purposes. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1a3aa6aef66a13b5601737a2cea610b179(const https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1a8c836c76e7e87d8021bf3b33c8a71c7c & data)` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Updates fields in the document referred to by this [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1afd3da01667281624f1dd1923de6b4121(const https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1a8e8e5e69a7a198ffd86426e741b04187 & data)` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Updates fields in the document referred to by this [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1aef23952bfd8cb315c73a9a09597f65b5() const ` | `virtual const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore *` Returns the [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance associated with this document reference. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1a06c4a89b90d779ad13579415d7349182()` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore *` Returns the [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance associated with this document reference. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1abf8fc04a98d248141548d6f82bdab1ac() const ` | `virtual const std::string &` Returns the string ID of this document location. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1af3a05d84cd5045af0601f0949ea3da81() const ` | `bool` Returns true if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` is valid, false if it is not valid. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1a943541423d78b15ef11b218bdbfa9d19(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference & other)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference &` Copy assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1a302fb2829d82d1897990b75295c9d718(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference && other)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference &` Move assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1a9c18dbad511ade2fb12077eae26dbad0() const ` | `virtual std::string` Returns the path of this document (relative to the root of the database) as a slash-separated string. |

## Friend classes

### operator\<\<

```c++
friend std::ostream & operator<<(std::ostream &out, const DocumentReference &reference)
```
Outputs the string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` to the given stream.

**See also:** `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1a685340cad727bee31464b81ebf558cef` for comments on the representation format.

## Public functions

### AddSnapshotListener

```c++
virtual ListenerRegistration AddSnapshotListener(
  std::function< void(const DocumentSnapshot &, Error, const std::string &)> callback
)
```
Starts listening to the document referenced by this [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `callback` | The std::function to call. When this function is called, snapshot value is valid if and only if error is Error::kErrorOk. The std::string is an error message; the value may be empty if an error message is not available. | |
| **Returns** | A registration object that can be used to remove the listener. |

### AddSnapshotListener

```c++
virtual ListenerRegistration AddSnapshotListener(
  MetadataChanges metadata_changes,
  std::function< void(const DocumentSnapshot &, Error, const std::string &)> callback
)
```
Starts listening to the document referenced by this [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `metadata_changes` | Indicates whether metadata-only changes (that is, only [DocumentSnapshot::metadata()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a6e8881817cf1fdd48fe5603c74fe9aae) changed) should trigger snapshot events. | | `callback` | The std::function to call. When this function is called, snapshot value is valid if and only if error is Error::kErrorOk. The std::string is an error message; the value may be empty if an error message is not available. | |
| **Returns** | A registration object that can be used to remove the listener. |

### Collection

```c++
virtual CollectionReference Collection(
  const char *collection_path
) const 
```
Returns a [CollectionReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference) instance that refers to the subcollection at the specified path relative to this document.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `collection_path` | A slash-separated relative path to a subcollection. The pointer only needs to be valid during this call. | |
| **Returns** | The [CollectionReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference) instance. |

### Collection

```c++
virtual CollectionReference Collection(
  const std::string & collection_path
) const 
```
Returns a [CollectionReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference) instance that refers to the subcollection at the specified path relative to this document.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `collection_path` | A slash-separated relative path to a subcollection. | |
| **Returns** | The [CollectionReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference) instance. |

### Delete

```c++
virtual Future< void > Delete()
```
Removes the document referred to by this [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference).

<br />

| Details ||
|---|---|
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) that will be resolved when the delete completes. |

### DocumentReference

```c++
 DocumentReference()
```
Creates an invalid [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) that has to be reassigned before it can be used.

Calling any member function on an invalid [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) will be a no-op. If the function returns a value, it will return a zero, empty, or invalid value, depending on the type of the value.

### DocumentReference

```c++
 DocumentReference(
  const DocumentReference & other
)
```
Copy constructor.

`https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` can be efficiently copied because it simply refers to a location in the database.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` to copy from. | |

### DocumentReference

```c++
 DocumentReference(
  DocumentReference && other
)
```
Move constructor.

Moving is more efficient than copying for a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference`. After being moved from, a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` is equivalent to its default-constructed state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` to move data from. | |

### Get

```c++
virtual Future< DocumentSnapshot > Get(
  Source source
) const 
```
Reads the document referenced by this [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference).

By default, [Get()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1a7c1711d91dd8e025642bb1bc793dc6c8) attempts to provide up-to-date data when possible by waiting for data from the server, but it may return cached data or fail if you are offline and the server cannot be reached. This behavior can be altered via the Source parameter.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `source` | A value to configure the get behavior (optional). | |
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) that will be resolved with the contents of the Document at this [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference). |

### Parent

```c++
virtual CollectionReference Parent() const 
```
Returns a [CollectionReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference) to the collection that contains this document.

### Set

```c++
virtual Future< void > Set(
  const MapFieldValue & data,
  const SetOptions & options
)
```
Writes to the document referred to by this [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference).

If the document does not yet exist, it will be created. If you pass [SetOptions](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options), the provided data can be merged into an existing document.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `data` | A map of the fields and values to write to the document. | | `options` | An object to configure the [Set()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1ace49a9db5c4c1f68ab85a36b1738eebc) behavior (optional). | |
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) that will be resolved when the write finishes. |

### ToString

```c++
std::string ToString() const 
```
Returns a string representation of this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` for logging/debugging purposes.


> [!NOTE]
> **Note:** the exact string representation is unspecified and subject to change; don't rely on the format of the string.

<br />

### Update

```c++
virtual Future< void > Update(
  const MapFieldValue & data
)
```
Updates fields in the document referred to by this [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference).

If no document exists yet, the update will fail.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `data` | A map of field / value pairs to update. Fields can contain dots to reference nested fields within the document. | |
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) that will be resolved when the client is online and the commit has completed against the server. The future will not resolve when the device is offline, though local changes will be visible immediately. |

### Update

```c++
virtual Future< void > Update(
  const MapFieldPathValue & data
)
```
Updates fields in the document referred to by this [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference).

If no document exists yet, the update will fail.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `data` | A map from [FieldPath](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path) to [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) to update. | |
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) that will be resolved when the client is online and the commit has completed against the server. The future will not resolve when the device is offline, though local changes will be visible immediately. |

### firestore

```c++
virtual const Firestore * firestore() const 
```
Returns the [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance associated with this document reference.

The pointer will remain valid indefinitely.

<br />

| Details ||
|---|---|
| **Returns** | Firebase [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance that this [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) refers to. |

### firestore

```c++
virtual Firestore * firestore()
```
Returns the [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance associated with this document reference.

The pointer will remain valid indefinitely.

<br />

| Details ||
|---|---|
| **Returns** | Firebase [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance that this [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) refers to. |

### id

```c++
virtual const std::string & id() const 
```
Returns the string ID of this document location.

<br />

| Details ||
|---|---|
| **Returns** | String ID of this document location. |

### is_valid

```c++
bool is_valid() const 
```
Returns true if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` is valid, false if it is not valid.

An invalid `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` could be the result of:

- Creating a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` using the default constructor.
- Moving from the `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference`.
- Calling `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference_1a6423c6f0e6147fd16ffc42111a75e5d2` on a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference` that is not a subcollection.
- Deleting your [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance, which will invalidate all the `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` instances associated with it.

<br />

<br />

| Details ||
|---|---|
| **Returns** | true if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` is valid, false if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` is invalid. |

### operator=

```c++
DocumentReference & operator=(
  const DocumentReference & other
)
```
Copy assignment operator.

`https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` can be efficiently copied because it simply refers to a location in the database.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` to copy from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference`. |

### operator=

```c++
DocumentReference & operator=(
  DocumentReference && other
)
```
Move assignment operator.

Moving is more efficient than copying for a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference`. After being moved from, a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` is equivalent to its default-constructed state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` to move data from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference`. |

### path

```c++
virtual std::string path() const 
```
Returns the path of this document (relative to the root of the database) as a slash-separated string.

<br />

| Details ||
|---|---|
| **Returns** | String path of this document location. |

### \~DocumentReference

```c++
virtual  ~DocumentReference()
```