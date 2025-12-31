# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-change.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change.md.txt

# Firebase.Firestore.DocumentChange Class Reference

# Firebase.Firestore.DocumentChange

A [DocumentChange](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change) represents a change to the documents matching a query.

## Summary

It contains the document affected and the type of change that occurred (added, modified, or removed).

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ### Public types                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Type](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change_1a12ef3c2f358e84614666f07720032aa5)`{` ` `[Added](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change_1a12ef3c2f358e84614666f07720032aa5af29ddbfb905eb2593fdcdfb243f9af85)` = 0,` ` `[Modified](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change_1a12ef3c2f358e84614666f07720032aa5a35e0c8c0b180c95d4e122e55ed62cc64)` = 1,` ` `[Removed](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change_1a12ef3c2f358e84614666f07720032aa5a93f07b720ebf7d1246512569761a5804)` = 2` `}` | enum An enumeration of [DocumentChange](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change) types. |

|                                                                                                                                                                                                                                                                              ### Properties                                                                                                                                                                                                                                                                              ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ChangeType](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change_1a8ca24282013ffb255cb3b96815794d3e) | [Type](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change_1a12ef3c2f358e84614666f07720032aa5) Returns the type of the [DocumentChange](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change). |
| [NewIndex](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change_1add496005f87d1168025431b3367058c9)   | `int` The index of the changed document in the result set immediately after this [DocumentChange](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change) (i.e.                                                                                                                         |
| [OldIndex](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change_1a979847e42a6856a98e96d9938d16510c)   | `int` The index of the changed document in the result set immediately prior to this [DocumentChange](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change) (i.e.                                                                                                                      |

|                                                                                                                                                                                                                                                                                                                        ### Public attributes                                                                                                                                                                                                                                                                                                                         ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Document](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change_1afebed1223033f06aa549fcd9a4fce817)` => new DocumentSnapshot(_proxy.document(), _firestore)` | [DocumentSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot) Returns the newly added or modified document if this [DocumentChange](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change) is for an updated document. |

|                                                                                                                                                                               ### Public functions                                                                                                                                                                               ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| [Equals](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change_1a4f7c356822007766c8763115fcba6a52)`(object obj)`                                                                                                                                                           | `override bool` |
| [Equals](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change_1abd8a8fce58c2d8e38de2a0d86244b686)`(`[DocumentChange](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change)` other)` | `bool`          |
| [GetHashCode](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change_1a3ef2a2150a85e316e2d7a7f02715bde7)`()`                                                                                                                                                                | `override int`  |

## Public types

### Type

```c#
 Type
```  
An enumeration of [DocumentChange](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change) types.

|                                                   Properties                                                   ||
|------------|----------------------------------------------------------------------------------------------------|
| `Added`    | Indicates a new document was added to the set of documents matching the query.                     |
| `Modified` | Indicates document within the query was modified.                                                  |
| `Removed`  | Indicates a document within the query was removed (either deleted or no longer matches the query). |

## Properties

### ChangeType

```c#
Type ChangeType
```  
Returns the type of the [DocumentChange](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change).  

### NewIndex

```c#
int NewIndex
```  
The index of the changed document in the result set immediately after this [DocumentChange](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change) (i.e.

supposing that all prior [DocumentChange](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change) objects and the current [DocumentChange](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change) object have been applied). Returns -1 for 'removed' events.  

### OldIndex

```c#
int OldIndex
```  
The index of the changed document in the result set immediately prior to this [DocumentChange](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change) (i.e.

supposing that all prior [DocumentChange](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change) objects have been applied). Returns -1 for 'added' events.

## Public attributes

### Document

```c#
DocumentSnapshot Document => new DocumentSnapshot(_proxy.document(), _firestore)
```  
Returns the newly added or modified document if this [DocumentChange](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-change#class_firebase_1_1_firestore_1_1_document_change) is for an updated document.

Returns the deleted document if this document change represents a removal.

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
  DocumentChange other
)
```  

### GetHashCode

```c#
override int GetHashCode()
```