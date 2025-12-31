# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/collection-reference.md.txt

# Firebase.Firestore.CollectionReference Class Reference

# Firebase.Firestore.CollectionReference

A reference to a collection in a [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) database.

## Summary

The existence of this object does not imply that the collection currently exists in storage.

A [CollectionReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/collection-reference#class_firebase_1_1_firestore_1_1_collection_reference) can be used for adding documents, getting document references, and querying for documents (using the methods inherited from [Query](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query)).

### Inheritance

Inherits from: [Firebase.Firestore.Query](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query), IEquatable\< CollectionReference \>

|                                                                                                                                                                                                           ### Properties                                                                                                                                                                                                            ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Parent](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/collection-reference#class_firebase_1_1_firestore_1_1_collection_reference_1adf1b07958231b05f82ac646c1e96c244) | [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference) The parent document, or null if this is a root collection. |

|                                                                                                                                                                ### Public attributes                                                                                                                                                                ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [Id](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/collection-reference#class_firebase_1_1_firestore_1_1_collection_reference_1a657bc2e62604de09d202523d84e63191)` => Proxy.id()`     | `string` The final part of the complete collection path; this is the identity of the collection relative to its parent document. |
| [Path](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/collection-reference#class_firebase_1_1_firestore_1_1_collection_reference_1ab9d1d5cd90ec7282d7abf31e5d47799b)` => Proxy.path()` | `string` The complete collection path, including project and database ID.                                                        |

|                                                                                                                                                                                                                                                                                                                                                                                               ### Public functions                                                                                                                                                                                                                                                                                                                                                                                               ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AddAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/collection-reference#class_firebase_1_1_firestore_1_1_collection_reference_1ae33ae3826cb5eb47587377670dbb6c81)`(object documentData)`                                                                                                                                                               | `Task< `[DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference)` >` Asynchronously creates a document with the given data in this collection.                                                                                                                                                            |
| [Document](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/collection-reference#class_firebase_1_1_firestore_1_1_collection_reference_1ab94632fa586f8f8149c501639d5acbb7)`()`                                                                                                                                                                                  | [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference) Creates a [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference) for a direct child document of this collection with a random ID. |
| [Document](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/collection-reference#class_firebase_1_1_firestore_1_1_collection_reference_1a2a23ea2730e067634ae4e16293814a77)`(string path)`                                                                                                                                                                       | [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference) Creates a [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference) for a child document of this reference.                          |
| [Equals](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/collection-reference#class_firebase_1_1_firestore_1_1_collection_reference_1aa719626247e1f0d71d652da477754808)`(object obj)`                                                                                                                                                                          | `override bool`                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Equals](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/collection-reference#class_firebase_1_1_firestore_1_1_collection_reference_1a388da5ad3074b0f65d4b3365b52f659c)`(`[CollectionReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/collection-reference#class_firebase_1_1_firestore_1_1_collection_reference)` other)` | `bool`                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [GetHashCode](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/collection-reference#class_firebase_1_1_firestore_1_1_collection_reference_1a703e1b06f6739148d9dd81e73684c2b0)`()`                                                                                                                                                                               | `override int`                                                                                                                                                                                                                                                                                                                                                                                                         |
| [ToString](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/collection-reference#class_firebase_1_1_firestore_1_1_collection_reference_1a70b58c951805f1ebdcbf2345e4e4a618)`()`                                                                                                                                                                                  | `override string`                                                                                                                                                                                                                                                                                                                                                                                                      |

## Properties

### Parent

```c#
DocumentReference Parent
```  
The parent document, or null if this is a root collection.

## Public attributes

### Id

```c#
string Id => Proxy.id()
```  
The final part of the complete collection path; this is the identity of the collection relative to its parent document.  

### Path

```c#
string Path => Proxy.path()
```  
The complete collection path, including project and database ID.

## Public functions

### AddAsync

```c#
Task< DocumentReference > AddAsync(
  object documentData
)
```  
Asynchronously creates a document with the given data in this collection.

The document has a randomly generated ID.

<br />

|                                                                     Details                                                                      ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |----------------|----------------------------------------------| | `documentData` | The data for the document. Must not be null. | |
| **Returns** | The reference for the newly-created document.                                                                                       |

### Document

```c#
DocumentReference Document()
```  
Creates a [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference) for a direct child document of this collection with a random ID.

This performs no server-side operations; it only generates the appropriate [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference).

<br />

|                                                                                                                    Details                                                                                                                    ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference) to a child document of this collection with a random ID. |

### Document

```c#
DocumentReference Document(
  string path
)
```  
Creates a [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference) for a child document of this reference.

<br />

|                                                                                                                                                          Details                                                                                                                                                           ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------|-------------------------------------------------------------------------------------------------------------------------------------------| | `path` | The path to the document, relative to this collection. Must not be null, and must contain an odd number of slash-separated path elements. | |
| **Returns** | A [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference) for the specified document.                                                                                                           |

### Equals

```c#
override bool Equals(
  object obj
)
```  

### Equals

```c#
bool Equals(
  CollectionReference other
)
```  

### GetHashCode

```c#
override int GetHashCode()
```  

### ToString

```c#
override string ToString()
```