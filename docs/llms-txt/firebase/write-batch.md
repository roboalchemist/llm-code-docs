# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/write-batch.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch.md.txt

# firebase::firestore::WriteBatch Class Reference

# firebase::firestore::WriteBatch


`#include <write_batch.h>`

A write batch is used to perform multiple writes as a single atomic unit.

## Summary

A [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch) object provides methods for adding writes to the write batch. None of the writes will be committed (or visible locally) until [Commit()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch_1a0bfbd1f4e9149d873a17ade0540b0512) is called.

Unlike transactions, write batches are persisted offline and therefore are preferable when you don't need to condition your writes on read data.


| **Note:** [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

<br />

| ### Constructors and Destructors ||
|---|---|
| [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch_1a1ef2385a4c63e72629050f5189f05a81)`()` Creates an invalid [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch) that has to be reassigned before it can be used. ||
| [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch_1a70ef96e2013e32353e7c38e3acf90a63)`(const `[WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch)` & other)` Copy constructor. ||
| [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch_1a6265f025cb1da1b53fa761a3080528a4)`(`[WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch)` && other)` Move constructor. ||
| [~WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch_1ae5c74ee1ec3e7fe13469e0898f913e30)`()` ||

|                                                                                                                                                                                                                                                                                                                                                                                                                                                               ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Commit](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch_1a0bfbd1f4e9149d873a17ade0540b0512)`()`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `virtual `[Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Commits all of the writes in this write batch as a single atomic unit.                               |
| [Delete](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch_1a382c0bbd7418383444d54a856e5779a6)`(const `[DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference)` & document)`                                                                                                                                                                                                                                                                                                                                             | `virtual `[WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch)` &` Deletes the document referred to by the provided reference.           |
| [Set](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch_1a11e09b5de4b493973e290cf3fd9784e9)`(const `[DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference)` & document, const `[MapFieldValue](https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1a8c836c76e7e87d8021bf3b33c8a71c7c)` & data, const `[SetOptions](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options)` & options)` | `virtual `[WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch)` &` Writes to the document referred to by the provided reference.         |
| [Update](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch_1af21e3ca91e338fe1137e6a9e80dc40ce)`(const `[DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference)` & document, const `[MapFieldValue](https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1a8c836c76e7e87d8021bf3b33c8a71c7c)` & data)`                                                                                                                                                              | `virtual `[WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch)` &` Updates fields in the document referred to by the provided reference. |
| [Update](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch_1a8b3da20650ee36cdfc768be4afe677b6)`(const `[DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference)` & document, const `[MapFieldPathValue](https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1a8e8e5e69a7a198ffd86426e741b04187)` & data)`                                                                                                                                                          | `virtual `[WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch)` &` Updates fields in the document referred to by the provided reference. |
| [is_valid](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch_1a33b9f972dfae8c83621028bdc2f719fe)`() const `                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `bool` Returns true if this [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch) is valid, false if it is not valid.                     |
| [operator=](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch_1a4d08844d41aa10034583a1df51729035)`(const `[WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch)` & other)`                                                                                                                                                                                                                                                                                                                                                                  | [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch)` &` Copy assignment operator.                                                       |
| [operator=](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch_1a11f41953a8aabd164b670e02cc324e56)`(`[WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch)` && other)`                                                                                                                                                                                                                                                                                                                                                                       | [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch)` &` Move assignment operator.                                                       |

## Public functions

### Commit

```c++
virtual Future< void > Commit()
```  
Commits all of the writes in this write batch as a single atomic unit.

<br />

|                                                                                Details                                                                                ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) that will be resolved when the write finishes. |

### Delete

```c++
virtual WriteBatch & Delete(
  const DocumentReference & document
)
```  
Deletes the document referred to by the provided reference.

<br />

|                                                                                                                                                                                                     Details                                                                                                                                                                                                      ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `document` | The [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) to delete. | |
| **Returns** | This [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch) instance. Used for chaining method calls.                                                                                                                                                                                                         |

### Set

```c++
virtual WriteBatch & Set(
  const DocumentReference & document,
  const MapFieldValue & data,
  const SetOptions & options
)
```  
Writes to the document referred to by the provided reference.

If the document does not yet exist, it will be created. If you pass [SetOptions](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options), the provided data can be merged into an existing document.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `document` | The [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) to write to.                                         | | `data`     | A map of the fields and values to write to the document.                                                                                                                                                                   | | `options`  | An object to configure the [Set()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch_1a11e09b5de4b493973e290cf3fd9784e9) behavior (optional). | |
| **Returns** | This [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch) instance. Used for chaining method calls.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

### Update

```c++
virtual WriteBatch & Update(
  const DocumentReference & document,
  const MapFieldValue & data
)
```  
Updates fields in the document referred to by the provided reference.

If no document exists yet, the update will fail.

<br />

|                                                                                                                                                                                                                                                                                                      Details                                                                                                                                                                                                                                                                                                       ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `document` | The [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) to update. | | `data`     | A map of field / value pairs to update. Fields can contain dots to reference nested fields within the document.                                                                  | |
| **Returns** | This [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch) instance. Used for chaining method calls.                                                                                                                                                                                                                                                                                                                                                                                                           |

### Update

```c++
virtual WriteBatch & Update(
  const DocumentReference & document,
  const MapFieldPathValue & data
)
```  
Updates fields in the document referred to by the provided reference.

If no document exists yet, the update will fail.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `document` | The [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) to update.                                                                                                                                | | `data`     | A map from [FieldPath](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path) to [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) to update. | |
| **Returns** | This [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch) instance. Used for chaining method calls.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

### WriteBatch

```c++
 WriteBatch()
```  
Creates an invalid [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch) that has to be reassigned before it can be used.

Calling any member function on an invalid [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch) will be a no-op. If the function returns a value, it will return a zero, empty, or invalid value, depending on the type of the value.  

### WriteBatch

```c++
 WriteBatch(
  const WriteBatch & other
)
```  
Copy constructor.

This performs a deep copy, creating an independent instance.

<br />

|                                                                                                                                                                            Details                                                                                                                                                                            ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|------------------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch) to copy from. | |

### WriteBatch

```c++
 WriteBatch(
  WriteBatch && other
)
```  
Move constructor.

Moving is more efficient than copying for a [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch). After being moved from, a [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch) is equivalent to its default-constructed state.

<br />

|                                                                                                                                                                                 Details                                                                                                                                                                                 ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch) to move data from. | |

### is_valid

```c++
bool is_valid() const 
```  
Returns true if this [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch) is valid, false if it is not valid.

An invalid [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch) could be the result of:

- Creating a [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch) using the default constructor.
- Moving from the [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch).
- Deleting your [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance, which will invalidate all the [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch) instances associated with it.

<br />

<br />

|                                                                                                                                                                         Details                                                                                                                                                                         ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | true if this [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch) is valid, false if this [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch) is invalid. |

### operator=

```c++
WriteBatch & operator=(
  const WriteBatch & other
)
```  
Copy assignment operator.

This performs a deep copy, creating an independent instance.

<br />

|                                                                                                                                                                            Details                                                                                                                                                                             ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|------------------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch) to copy from. | |
| **Returns** | Reference to the destination [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch).                                                                                                                                                                        |

### operator=

```c++
WriteBatch & operator=(
  WriteBatch && other
)
```  
Move assignment operator.

Moving is more efficient than copying for a [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch). After being moved from, a [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch) is equivalent to its default-constructed state.

<br />

|                                                                                                                                                                                 Details                                                                                                                                                                                  ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------| | `other` | [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch) to move data from. | |
| **Returns** | Reference to the destination [WriteBatch](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/write-batch#classfirebase_1_1firestore_1_1_write_batch).                                                                                                                                                                                  |

### \~WriteBatch

```c++
virtual  ~WriteBatch()
```