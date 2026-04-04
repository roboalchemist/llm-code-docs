# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference.md.txt

# Firebase.Firestore.DocumentReference Class Reference

# Firebase.Firestore.DocumentReference

A [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference) refers to a document location in a Cloud [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) database and can be used to write, read, or listen to the location.

## Summary

There may or may not exist a document at the referenced location. A [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference) can also be used to create a [CollectionReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/collection-reference#class_firebase_1_1_firestore_1_1_collection_reference) to a subcollection.

### Inheritance

Inherits from: IEquatable\< DocumentReference \>

|                                                                                                                                                                                                  ### Properties                                                                                                                                                                                                   ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Firestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference_1a0f5e74f6fca00b141012c7345b186ed8) | [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) The database which contains the document. |

|                                                                                                                                                                                                                   ### Public attributes                                                                                                                                                                                                                    ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Id](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference_1aa0ff8412f721169f5bfc7c402dee18ac)` => _proxy.id()`                                             | `string` The final part of the complete document path; this is the identity of the document relative to its parent collection.                                                                     |
| [Parent](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference_1af19fac9f643cd3cae2a83f0f3f6c7eb6)` => new CollectionReference(_proxy.Parent(), Firestore)` | [CollectionReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/collection-reference#class_firebase_1_1_firestore_1_1_collection_reference) The parent collection. |
| [Path](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference_1a0a1908487c69bf2d5447c3fd6143eb5d)` => _proxy.path()`                                         | `string` The complete document path, not including project and database ID.                                                                                                                        |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Collection](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference_1ae1ac765bb5388826d7c8c6121b3be147)`(string path)`                                                                                                                                                                                                                                                                                                                                                                 | [CollectionReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/collection-reference#class_firebase_1_1_firestore_1_1_collection_reference) Creates a [CollectionReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/collection-reference#class_firebase_1_1_firestore_1_1_collection_reference) for a child collection of this document.           |
| [DeleteAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference_1ab79a376bcbf0d63ba02ac31be60e7227)`()`                                                                                                                                                                                                                                                                                                                                                                           | `Task` Asynchronously deletes the document referred to by this [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference).                                                                                                                                                                                |
| [Equals](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference_1a5d3a19a21b44c3b1cf69400b1d576b82)`(object obj)`                                                                                                                                                                                                                                                                                                                                                                      | `override bool`                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Equals](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference_1a140452685ec7922794d99719e4685f4a)`(`[DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference)` other)`                                                                                                                                                                                                   | `bool`                                                                                                                                                                                                                                                                                                                                                                                                               |
| [GetHashCode](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference_1ab590ffa99fd6780edd87fd6dd603c86f)`()`                                                                                                                                                                                                                                                                                                                                                                           | `override int`                                                                                                                                                                                                                                                                                                                                                                                                       |
| [GetSnapshotAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference_1a6f618848d083200f4882a43506342bf4)`(`[Source](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore_1a1e8014969fa0e13d46c8e0684fe0db80)` source)`                                                                                                                                                                                                  | `Task< `[DocumentSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot)` >` Asynchronously fetches a snapshot of the document.                                                                                                                                                                                    |
| [Listen](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference_1a4c2c1f4fa2e961126524d5b5a70309b7)`(Action< `[DocumentSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot)` > callback)`                                                                                                                                                                                         | [ListenerRegistration](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/listener-registration#class_firebase_1_1_firestore_1_1_listener_registration) Starts listening to changes to the document referenced by this [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference). |
| [Listen](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference_1aa9cd027ccf95897425f2a52264a5a0fc)`(`[MetadataChanges](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore_1a43cdca9284c02096b03c5ae05de2e288)` metadataChanges, Action< `[DocumentSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot)` > callback)` | [ListenerRegistration](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/listener-registration#class_firebase_1_1_firestore_1_1_listener_registration) Starts listening to changes to the document referenced by this [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference). |
| [SetAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference_1a10d789ea301586c4d65e51a7214ed681)`(object documentData, `[SetOptions](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/set-options#class_firebase_1_1_firestore_1_1_set_options)` options)`                                                                                                                                                                                               | `Task` Asynchronously sets data in the document, either replacing it completely or merging fields.                                                                                                                                                                                                                                                                                                                   |
| [ToString](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference_1aecde0e990917170e47ff93b4fd3109c3)`()`                                                                                                                                                                                                                                                                                                                                                                              | `override string`                                                                                                                                                                                                                                                                                                                                                                                                    |
| [UpdateAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference_1a54c77be071e3fbe12b56cbc2d9d33e04)`(IDictionary< string, object > updates)`                                                                                                                                                                                                                                                                                                                                      | `Task` Asynchronously performs a set of updates on the document referred to by this [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference).                                                                                                                                                           |
| [UpdateAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference_1a7004a1073f7b63c9ff35e7912662e19d)`(string field, object value)`                                                                                                                                                                                                                                                                                                                                                 | `Task` Asynchronously performs a single field update on the document referred to by this [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference).                                                                                                                                                      |
| [UpdateAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference_1a2360bcdec27c075329a057bea7e469fd)`(IDictionary< `[FieldPath](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path)`, object > updates)`                                                                                                                                                                                             | `Task` Asynchronously performs a set of updates on the document referred to by this [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference).                                                                                                                                                           |

## Properties

### Firestore

```c#
FirebaseFirestore Firestore
```  
The database which contains the document.

## Public attributes

### Id

```c#
string Id => _proxy.id()
```  
The final part of the complete document path; this is the identity of the document relative to its parent collection.  

### Parent

```c#
CollectionReference Parent => new CollectionReference(_proxy.Parent(), Firestore)
```  
The parent collection.

Never `null`.  

### Path

```c#
string Path => _proxy.path()
```  
The complete document path, not including project and database ID.

## Public functions

### Collection

```c#
CollectionReference Collection(
  string path
)
```  
Creates a [CollectionReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/collection-reference#class_firebase_1_1_firestore_1_1_collection_reference) for a child collection of this document.

<br />

|                                                                                                                                                            Details                                                                                                                                                             ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------|---------------------------------------------------------------------------------------------------------------------------------------------| | `path` | The path to the collection, relative to this document. Must not be `null`, and must contain an odd number of slash-separated path elements. | |
| **Returns** | A [CollectionReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/collection-reference#class_firebase_1_1_firestore_1_1_collection_reference) for the specified collection.                                                                                                       |

### DeleteAsync

```c#
Task DeleteAsync()
```  
Asynchronously deletes the document referred to by this [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference).

<br />

|                                                                             Details                                                                              ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The write result of the server operation. The task will not complete while the client is offline, though local changes will be visible immediately. |

### Equals

```c#
override bool Equals(
  object obj
)
```  

### Equals

```c#
bool Equals(
  DocumentReference other
)
```  

### GetHashCode

```c#
override int GetHashCode()
```  

### GetSnapshotAsync

```c#
Task< DocumentSnapshot > GetSnapshotAsync(
  Source source
)
```  
Asynchronously fetches a snapshot of the document.

By default, `GetSnapshotAsync` attempts to provide up-to-date data when possible by waiting for data from the server, but it may return cached data or fail if you are offline and the server cannot be reached. This behavior can be altered via the `source` parameter.

<br />

|                                                                                                                                                                                                                   Details                                                                                                                                                                                                                    ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `source` | indicates whether the results should be fetched from the cache only (`Source.Cache`), the server only (`Source.Server`), or to attempt the server and fall back to the cache (`Source.Default`). | |
| **Returns** | A snapshot of the document. The snapshot may represent a missing document.                                                                                                                                                                                                                                                                                                                                                      |

### Listen

```c#
ListenerRegistration Listen(
  Action< DocumentSnapshot > callback
)
```  
Starts listening to changes to the document referenced by this [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference).

<br />

|                                                                                                                                                    Details                                                                                                                                                     ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|---------------------------------------------------------------------------------------------------------------------------------| | `callback` | The callback to invoke each time the query results change. Must not be `null`. The callback will be invoked on the main thread. | |
| **Returns** | A [ListenerRegistration](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/listener-registration#class_firebase_1_1_firestore_1_1_listener_registration) which may be used to stop listening gracefully.                                                                  |

### Listen

```c#
ListenerRegistration Listen(
  MetadataChanges metadataChanges,
  Action< DocumentSnapshot > callback
)
```  
Starts listening to changes to the document referenced by this [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference).

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `metadataChanges` | Indicates whether metadata-only changes (i.e. only [DocumentSnapshot.Metadata](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot_1a734cee9c3d88d7c80d425aaca41b3230) changed) should trigger snapshot events. | | `callback`        | The callback to invoke each time the query results change. Must not be `null`. The callback will be invoked on the main thread.                                                                                                                                                                            | |
| **Returns** | A [ListenerRegistration](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/listener-registration#class_firebase_1_1_firestore_1_1_listener_registration) which may be used to stop listening gracefully.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

### SetAsync

```c#
Task SetAsync(
  object documentData,
  SetOptions options
)
```  
Asynchronously sets data in the document, either replacing it completely or merging fields.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `documentData` | The data to store in the document. Must not be `null`.                                                                                                                                                                                                                              | | `options`      | The options to use when updating the document. May be `null`, which is equivalent to [SetOptions.Overwrite](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/set-options#class_firebase_1_1_firestore_1_1_set_options_1ad6276e4792d4c87d0313af76f2f6905a). | |
| **Returns** | The write result of the server operation. The task will not complete while the client is offline, though local changes will be visible immediately.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

### ToString

```c#
override string ToString()
```  

### UpdateAsync

```c#
Task UpdateAsync(
  IDictionary< string, object > updates
)
```  
Asynchronously performs a set of updates on the document referred to by this [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference).

<br />

|                                                                                                                                                                         Details                                                                                                                                                                          ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------| | `updates` | The updates to perform on the document, keyed by the field path to update. Fields not present in this dictionary are not updated. Must not be `null`. | |
| **Returns** | The write result of the server operation. The task will not complete while the client is offline, though local changes will be visible immediately.                                                                                                                                                                                         |

### UpdateAsync

```c#
Task UpdateAsync(
  string field,
  object value
)
```  
Asynchronously performs a single field update on the document referred to by this [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference).

<br />

|                                                                                                                             Details                                                                                                                             ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|--------------------------------------------------------------------| | `field` | The dot-separated name of the field to update. Must not be `null`. | | `value` | The new value for the field. May be `null`.                        | |
| **Returns** | The write result of the server operation. The task will not complete while the client is offline, though local changes will be visible immediately.                                                                                                |

### UpdateAsync

```c#
Task UpdateAsync(
  IDictionary< FieldPath, object > updates
)
```  
Asynchronously performs a set of updates on the document referred to by this [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference).

<br />

|                                                                                                                                                                         Details                                                                                                                                                                          ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------| | `updates` | The updates to perform on the document, keyed by the field path to update. Fields not present in this dictionary are not updated. Must not be `null`. | |
| **Returns** | The write result of the server operation. The task will not complete while the client is offline, though local changes will be visible immediately.                                                                                                                                                                                         |