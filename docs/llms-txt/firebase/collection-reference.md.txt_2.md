# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference.md.txt

# firebase::firestore::CollectionReference Class Reference

# firebase::firestore::CollectionReference


`#include <collection_reference.h>`

A [CollectionReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference) can be used for adding documents, getting document references, and querying for documents (using the methods inherited from `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query`).

## Summary


> [!NOTE]
> **Note:** [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

<br />

### Inheritance

Inherits from: [firebase::firestore::Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query)

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference_1a9e2f0db88d238d786e0dbbf604531c73()` Creates an invalid [CollectionReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference) that has to be reassigned before it can be used. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference_1a0cf3a420bbfc2afa7c6da72fc4a7a4d5(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference & other)` Copy constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference_1a11f173e91d21387fdc73c5888084ef7c(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference && other)` Move constructor. ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference_1a7c2d173c29e6264ef9e0cba8cc367505(const https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1a8c836c76e7e87d8021bf3b33c8a71c7c & data)` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference >` Adds a new document to this collection with the specified data, assigning it a document ID automatically. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference_1a3cb1646fef0f9f4b89ea7c8e5a3608fc() const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` Returns a [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) that points to a new document with an auto-generated ID within this collection. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference_1a51afdd755ccaa4895f2994814a34dc70(const char *document_path) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` Gets a [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) instance that refers to the document at the specified path within this collection. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference_1a197e94377d92f1899dbcf56df698dd42(const std::string & document_path) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` Gets a [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) instance that refers to the document at the specified path within this collection. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference_1a6423c6f0e6147fd16ffc42111a75e5d2() const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference` Gets a [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) to the document that contains this collection. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference_1add40660e18384902cbc85372ba445e6f() const ` | `virtual const std::string &` Gets the ID of the referenced collection. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference_1a5cba253e29546f2a45b7826f97968595(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference & other)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference &` Copy assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference_1aba0b2f03b322a37f03ab1956d0821b60(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference && other)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference &` Move assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference_1aa4c0ec70304e5ad9a0d64c26214e7878() const ` | `virtual std::string` Returns the path of this collection (relative to the root of the database) as a slash-separated string. |

## Public functions

### Add

```c++
virtual Future< DocumentReference > Add(
  const MapFieldValue & data
)
```
Adds a new document to this collection with the specified data, assigning it a document ID automatically.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `data` | A map containing the data for the new document. | |
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) that will be resolved with the [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) of the newly created document. |

### CollectionReference

```c++
 CollectionReference()
```
Creates an invalid [CollectionReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference) that has to be reassigned before it can be used.

Calling any member function on an invalid [CollectionReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference) will be a no-op. If the function returns a value, it will return a zero, empty, or invalid value, depending on the type of the value.

### CollectionReference

```c++
 CollectionReference(
  const CollectionReference & other
)
```
Copy constructor.

`https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference` can be efficiently copied because it simply refers to a location in the database.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference` to copy from. | |

### CollectionReference

```c++
 CollectionReference(
  CollectionReference && other
)
```
Move constructor.

Moving is more efficient than copying for a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference`. After being moved from, a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference` is equivalent to its default-constructed state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference` to move data from. | |

### Document

```c++
virtual DocumentReference Document() const 
```
Returns a [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) that points to a new document with an auto-generated ID within this collection.

<br />

| Details ||
|---|---|
| **Returns** | A [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) pointing to the new document. |

### Document

```c++
virtual DocumentReference Document(
  const char *document_path
) const 
```
Gets a [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) instance that refers to the document at the specified path within this collection.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `document_path` | A slash-separated relative path to a document. The pointer only needs to be valid during this call. | |
| **Returns** | The [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) instance. |

### Document

```c++
virtual DocumentReference Document(
  const std::string & document_path
) const 
```
Gets a [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) instance that refers to the document at the specified path within this collection.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `document_path` | A slash-separated relative path to a document. | |
| **Returns** | The [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) instance. |

### Parent

```c++
virtual DocumentReference Parent() const 
```
Gets a [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) to the document that contains this collection.

<br />

| Details ||
|---|---|
| **Returns** | The [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) that contains this collection if this is a subcollection. If this is a root collection, returns an invalid [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) (`https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference_1af3a05d84cd5045af0601f0949ea3da81` will return false). |

### id

```c++
virtual const std::string & id() const 
```
Gets the ID of the referenced collection.

<br />

| Details ||
|---|---|
| **Returns** | The ID as a std::string. |

### operator=

```c++
CollectionReference & operator=(
  const CollectionReference & other
)
```
Copy assignment operator.

`https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference` can be efficiently copied because it simply refers to a location in the database.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference` to copy from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference`. |

### operator=

```c++
CollectionReference & operator=(
  CollectionReference && other
)
```
Move assignment operator.

Moving is more efficient than copying for a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference`. After being moved from, a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference` is equivalent to its default-constructed state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference` to move data from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference`. |

### path

```c++
virtual std::string path() const 
```
Returns the path of this collection (relative to the root of the database) as a slash-separated string.

<br />

| Details ||
|---|---|
| **Returns** | The path as a std::string. |