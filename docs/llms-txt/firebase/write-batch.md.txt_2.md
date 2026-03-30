# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/write-batch.md.txt

# Firebase.Firestore.WriteBatch Class Reference

# Firebase.Firestore.WriteBatch

A batch of write operations, used to perform multiple writes as a single atomic unit.

## Summary

A `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/write-batch#class_firebase_1_1_firestore_1_1_write_batch` object can be acquired by calling [FirebaseFirestore.StartBatch](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore_1ab2d183efdb86e5f3f52f42877b51ae4f). It provides methods for adding writes to the write batch. None of the writes will be committed (or visible locally) until [CommitAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/write-batch#class_firebase_1_1_firestore_1_1_write_batch_1a16242eb3b0ee576c58534b2006519fc7) is called.

Unlike transactions, write batches are persisted offline and therefore are preferable when you don't need to condition your writes on read data.

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/write-batch#class_firebase_1_1_firestore_1_1_write_batch_1a16242eb3b0ee576c58534b2006519fc7()` | `Task` Commits all of the writes in this write batch as a single atomic unit. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/write-batch#class_firebase_1_1_firestore_1_1_write_batch_1a1fb1d127404f457d91386b66971febf1(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference documentReference)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/write-batch#class_firebase_1_1_firestore_1_1_write_batch` Deletes the document referenced by the provided `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference`. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/write-batch#class_firebase_1_1_firestore_1_1_write_batch_1af70ca7652b2b54720a8aec568fd66d05(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference documentReference, object documentData, https://firebase.google.com/docs/reference/unity/class/firebase/firestore/set-options#class_firebase_1_1_firestore_1_1_set_options options)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/write-batch#class_firebase_1_1_firestore_1_1_write_batch` Writes to the document referred to by the provided `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference`. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/write-batch#class_firebase_1_1_firestore_1_1_write_batch_1a694907eafc24d107489f6e6cc9a654f1(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference documentReference, IDictionary< string, object > updates)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/write-batch#class_firebase_1_1_firestore_1_1_write_batch` Updates fields in the document referred to by the provided `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference`. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/write-batch#class_firebase_1_1_firestore_1_1_write_batch_1abe9db6b5411c0dc7d94b38c12c1dfd8a(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference documentReference, string field, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/write-batch#class_firebase_1_1_firestore_1_1_write_batch` Updates the field in the document referred to by the provided `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference`. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/write-batch#class_firebase_1_1_firestore_1_1_write_batch_1a08c5515ee5794eb0a244ee94412e12ba(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference documentReference, IDictionary< https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path, object > updates)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/write-batch#class_firebase_1_1_firestore_1_1_write_batch` Updates fields in the document referred to by the provided `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference`. |

## Public functions

### CommitAsync

```c#
Task CommitAsync()
```
Commits all of the writes in this write batch as a single atomic unit.

<br />

| Details ||
|---|---|
| **Returns** | The write result of the server operation. The task will not complete while the client is offline, though local changes will be visible immediately. |

### Delete

```c#
WriteBatch Delete(
  DocumentReference documentReference
)
```
Deletes the document referenced by the provided `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `documentReference` | The document to delete. Must not be `null`. | |
| **Returns** | This batch, for the purposes of method chaining. |

### Set

```c#
WriteBatch Set(
  DocumentReference documentReference,
  object documentData,
  SetOptions options
)
```
Writes to the document referred to by the provided `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference`.

If the document does not yet exist, it will be created. If you pass *options* , the provided data can be merged into an existing document.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `documentReference` | The document in which to set the data. Must not be `null`. | | `documentData` | The data for the document. Must not be `null`. | | `options` | The options to use when updating the document. May be `null`, which is equivalent to [SetOptions.Overwrite](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/set-options#class_firebase_1_1_firestore_1_1_set_options_1ad6276e4792d4c87d0313af76f2f6905a). | |
| **Returns** | This batch, for the purposes of method chaining. |

### Update

```c#
WriteBatch Update(
  DocumentReference documentReference,
  IDictionary< string, object > updates
)
```
Updates fields in the document referred to by the provided `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference`.

If no document exists yet, the update will fail.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `documentReference` | The document to update. Must not be `null`. | | `updates` | A dictionary of field / value pairs to update. Fields can contain dots to reference nested fields in the document. Fields not present in this dictionary are not updated. Must not be `null`. | |
| **Returns** | This batch, for the purposes of method chaining. |

### Update

```c#
WriteBatch Update(
  DocumentReference documentReference,
  string field,
  object value
)
```
Updates the field in the document referred to by the provided `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference`.

If no document exists yet, the update will fail.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `documentReference` | The document to update. Must not be `null`. | | `field` | The dot-separated name of the field to update. Must not be `null`. | | `value` | The new value for the field. May be `null`. | |
| **Returns** | This batch, for the purposes of method chaining. |

### Update

```c#
WriteBatch Update(
  DocumentReference documentReference,
  IDictionary< FieldPath, object > updates
)
```
Updates fields in the document referred to by the provided `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-reference#class_firebase_1_1_firestore_1_1_document_reference`.

If no document exists yet, the update will fail.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `documentReference` | The document to update. Must not be `null`. | | `updates` | A dictionary of field / value pairs to update. Fields not present in this dictionary are not updated. Must not be `null`. | |
| **Returns** | This batch, for the purposes of method chaining. |