# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/transaction.md.txt

# Firebase.Firestore.Transaction Class Reference

# Firebase.Firestore.Transaction

A transaction, as created by FirebaseFirestore.RunTransactionAsync{T}(System.Func{Transaction, Task{T}}) (and overloads) and passed to user code.

## Summary

|                                                                                                                                                                                        ### Properties                                                                                                                                                                                        ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Firestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/transaction#class_firebase_1_1_firestore_1_1_transaction_1a7500ee1aef427bbf1c3624f7fe01c1c1) | [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) The database for this transaction. |

|                                                                                                                                                                                                                                                                                                                                                                                                               ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Delete](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/transaction#class_firebase_1_1_firestore_1_1_transaction_1a5159edf07e9d65e5280b81321d9b975b)`(`[DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference)` documentReference)`                                                                                                                                                                                 | `void` Deletes the document referenced by the provided [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference).                                                       |
| [GetSnapshotAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/transaction#class_firebase_1_1_firestore_1_1_transaction_1a718e1628152ea6833d7ecde717ee5a07)`(`[DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference)` documentReference)`                                                                                                                                                                       | `Task< `[DocumentSnapshot](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot)` >` Read a snapshot of the document specified by *documentReference* , with respect to this transaction. |
| [Set](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/transaction#class_firebase_1_1_firestore_1_1_transaction_1a973184c2acd6c08c9f89e233f3f6f4d9)`(`[DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference)` documentReference, object documentData, `[SetOptions](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/set-options#class_firebase_1_1_firestore_1_1_set_options)` options)`   | `void` Writes to the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference).                                                    |
| [Update](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/transaction#class_firebase_1_1_firestore_1_1_transaction_1a5b315edaef3b486343eefc46aac22715)`(`[DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference)` documentReference, IDictionary< string, object > updates)`                                                                                                                                          | `void` Updates fields in the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference).                                            |
| [Update](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/transaction#class_firebase_1_1_firestore_1_1_transaction_1a9f896750e362dddbce46949a29a5928d)`(`[DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference)` documentReference, string field, object value)`                                                                                                                                                     | `void` Updates the field in the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference).                                         |
| [Update](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/transaction#class_firebase_1_1_firestore_1_1_transaction_1af30e15e07e83ae08a281255d235ecf0e)`(`[DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference)` documentReference, IDictionary< `[FieldPath](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path)`, object > updates)` | `void` Updates fields in the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference).                                            |

## Properties

### Firestore

```c#
FirebaseFirestore Firestore
```  
The database for this transaction.

## Public functions

### Delete

```c#
void Delete(
  DocumentReference documentReference
)
```  
Deletes the document referenced by the provided [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference).

<br />

|                                                                         Details                                                                         ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------|---------------------------------------------| | `documentReference` | The document to delete. Must not be `null`. | |

### GetSnapshotAsync

```c#
Task< DocumentSnapshot > GetSnapshotAsync(
  DocumentReference documentReference
)
```  
Read a snapshot of the document specified by *documentReference* , with respect to this transaction.

This method cannot be called after any write operations have been created.

<br />

|                                                                                 Details                                                                                  ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|-----------------------------------------------------| | `documentReference` | The document reference to read. Must not be `null`. | |
| **Returns** | A snapshot of the given document with respect to this transaction.                                                                                          |

### Set

```c#
void Set(
  DocumentReference documentReference,
  object documentData,
  SetOptions options
)
```  
Writes to the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference).

If the document does not yet exist, it will be created. If you pass *options* , the provided data can be merged into an existing document.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `documentReference` | The document in which to set the data. Must not be `null`.                                                                                                                                                                                                                          | | `documentData`      | The data for the document. Must not be `null`.                                                                                                                                                                                                                                      | | `options`           | The options to use when updating the document. May be `null`, which is equivalent to [SetOptions.Overwrite](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/set-options#class_firebase_1_1_firestore_1_1_set_options_1ad6276e4792d4c87d0313af76f2f6905a). | |

### Update

```c#
void Update(
  DocumentReference documentReference,
  IDictionary< string, object > updates
)
```  
Updates fields in the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference).

If no document exists yet, the update will fail.

<br />

|                                                                                                                                                                                                                                                                                                                                       Details                                                                                                                                                                                                                                                                                                                                       ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `documentReference` | The document to update. Must not be `null`.                                                                                                                                                   | | `updates`           | A dictionary of field / value pairs to update. Fields can contain dots to reference nested fields in the document. Fields not present in this dictionary are not updated. Must not be `null`. | |

### Update

```c#
void Update(
  DocumentReference documentReference,
  string field,
  object value
)
```  
Updates the field in the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference).

If no document exists yet, the update will fail.

<br />

|                                                                                                                                                                                             Details                                                                                                                                                                                             ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------|--------------------------------------------------------------------| | `documentReference` | The document to update. Must not be `null`.                        | | `field`             | The dot-separated name of the field to update. Must not be `null`. | | `value`             | The new value for the field. May be `null`.                        | |

### Update

```c#
void Update(
  DocumentReference documentReference,
  IDictionary< FieldPath, object > updates
)
```  
Updates fields in the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference).

If no document exists yet, the update will fail.

<br />

|                                                                                                                                                                                                                                 Details                                                                                                                                                                                                                                 ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------|---------------------------------------------------------------------------------------------------------------------------| | `documentReference` | The document to update. Must not be `null`.                                                                               | | `updates`           | A dictionary of field / value pairs to update. Fields not present in this dictionary are not updated. Must not be `null`. | |