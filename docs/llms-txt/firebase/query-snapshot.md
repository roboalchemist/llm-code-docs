# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query-snapshot.md.txt

# Firebase.Firestore.QuerySnapshot Class Reference

# Firebase.Firestore.QuerySnapshot

A [QuerySnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query-snapshot#class_firebase_1_1_firestore_1_1_query_snapshot) contains the results of a query.

## Summary

It can contain zero or more [DocumentSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot) objects.

### Inheritance

Inherits from: global::SystemCollections::Generic::IEnumerable\< DocumentSnapshot \>

|                                                                                                                                                                                        ### Public attributes                                                                                                                                                                                        ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Query](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query-snapshot#class_firebase_1_1_firestore_1_1_query_snapshot_1aad830588df5ab6b7b35a126e91556a5c)` => new Query(_proxy.query(), _firestore)` | [Query](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query) The query producing this snapshot. |

|                                                                                                                                                                                                                                                                   ### Properties                                                                                                                                                                                                                                                                    ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Count](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query-snapshot#class_firebase_1_1_firestore_1_1_query_snapshot_1a41fc0913989b441ef90513bafe542982)           | `int` Returns the number of documents in this query snapshot.                                                                                                                                                                                                                                                                                       |
| [Documents](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query-snapshot#class_firebase_1_1_firestore_1_1_query_snapshot_1a53b20efb05e52b9944e415fe3c6493c0)       | `IEnumerable< `[DocumentSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot)` >` The documents in the snapshot.                                                                                                                                |
| [Metadata](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query-snapshot#class_firebase_1_1_firestore_1_1_query_snapshot_1ae3483481c5513bf32acf9a7728850ad2)        | [SnapshotMetadata](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/snapshot-metadata#class_firebase_1_1_firestore_1_1_snapshot_metadata) The metadata for this [QuerySnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query-snapshot#class_firebase_1_1_firestore_1_1_query_snapshot). |
| [this[int index]](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query-snapshot#class_firebase_1_1_firestore_1_1_query_snapshot_1a82c73082eb2576be66fa72ade88f5366) | [DocumentSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot) Returns the document snapshot with the specified index within this query snapshot.                                                                                               |

|                                                                                                                                                                                                                                                                                                       ### Public functions                                                                                                                                                                                                                                                                                                       ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Equals](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query-snapshot#class_firebase_1_1_firestore_1_1_query_snapshot_1a721e21fca621c2bf80c55411e51c0399)`(object obj)`                                                                                                                                                                                 | `override bool`                                                                                                                                                                                                                             |
| [Equals](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query-snapshot#class_firebase_1_1_firestore_1_1_query_snapshot_1a13f866c0771bf07e610810aac90f5b7a)`(`[QuerySnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query-snapshot#class_firebase_1_1_firestore_1_1_query_snapshot)` other)`                          | `bool`                                                                                                                                                                                                                                      |
| [GetChanges](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query-snapshot#class_firebase_1_1_firestore_1_1_query_snapshot_1a41bd85c872c528f8d6839334a7898f40)`()`                                                                                                                                                                                       | `IEnumerable< `[DocumentChange](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change)` >` The list of documents that changed since the last snapshot. |
| [GetChanges](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query-snapshot#class_firebase_1_1_firestore_1_1_query_snapshot_1a2c6c523627bf961c85360037dfb87cd0)`(`[MetadataChanges](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore_1a43cdca9284c02096b03c5ae05de2e288)` metadataChanges)` | `IEnumerable< `[DocumentChange](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change)` >` The list of documents that changed since the last snapshot. |
| [GetHashCode](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query-snapshot#class_firebase_1_1_firestore_1_1_query_snapshot_1aa8dd257ab5db26fa31a021731d5fa81a)`()`                                                                                                                                                                                      | `override int`                                                                                                                                                                                                                              |

## Public attributes

### Query

```c#
Query Query => new Query(_proxy.query(), _firestore)
```  
The query producing this snapshot.

## Properties

### Count

```c#
int Count
```  
Returns the number of documents in this query snapshot.

The number of documents in this query snapshot.  

### Documents

```c#
IEnumerable< DocumentSnapshot > Documents
```  
The documents in the snapshot.  

### Metadata

```c#
SnapshotMetadata Metadata
```  
The metadata for this [QuerySnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query-snapshot#class_firebase_1_1_firestore_1_1_query_snapshot).  

### this\[int index\]

```c#
DocumentSnapshot this[int index]
```  
Returns the document snapshot with the specified index within this query snapshot.

<br />

|                                                                                                                                                                                                                                                                                 Details                                                                                                                                                                                                                                                                                  ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|--------------------------------------| | `index` | The index of the document to return. |                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Exceptions  | |-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `ArgumentOutOfRangeException` | *index* is less than 0, or greater than or equal to [Count](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query-snapshot#class_firebase_1_1_firestore_1_1_query_snapshot_1a41fc0913989b441ef90513bafe542982). | |
| **Returns** | The document snapshot with the specified index within this query snapshot.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

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
  QuerySnapshot other
)
```  

### GetChanges

```c#
IEnumerable< DocumentChange > GetChanges()
```  
The list of documents that changed since the last snapshot.

If it's the first snapshot all documents will be in the list as added changes.

Documents with changes only to their metadata will not be included.

<br />

|                              Details                               ||
|-------------|-------------------------------------------------------|
| **Returns** | The list of document changes since the last snapshot. |

### GetChanges

```c#
IEnumerable< DocumentChange > GetChanges(
  MetadataChanges metadataChanges
)
```  
The list of documents that changed since the last snapshot.

If it's the first snapshot all documents will be in the list as added changes.

<br />

|                                                                                                                                                                                                                                                                                                                                             Details                                                                                                                                                                                                                                                                                                                                              ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `metadataChanges` | Indicates whether metadata-only changes (i.e. only [Firebase.Firestore.DocumentSnapshot.Metadata](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot_1a734cee9c3d88d7c80d425aaca41b3230) changed) should be included. | |
| **Returns** | The list of document changes since the last snapshot.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

### GetHashCode

```c#
override int GetHashCode()
```