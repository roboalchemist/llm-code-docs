# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction.md.txt

# firebase::firestore::Transaction Class Reference

# firebase::firestore::Transaction


`#include <transaction.h>`

[Transaction](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction#classfirebase_1_1firestore_1_1_transaction) provides methods to read and write data within a transaction.

## Summary

You cannot create a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction#classfirebase_1_1firestore_1_1_transaction` directly; use `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1ad82d5378fb9807f472d3d2bdaa12e696` function instead.


> [!NOTE]
> **Note:** [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

<br />

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction#classfirebase_1_1firestore_1_1_transaction_1a96b7e6eb05ab4b0dfd2c408c1bfb8362(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction#classfirebase_1_1firestore_1_1_transaction & other)` Deleted copy constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction#classfirebase_1_1firestore_1_1_transaction_1ac85e529c46aa2ba95fc3421dd04d6c27()` Destructor. ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction#classfirebase_1_1firestore_1_1_transaction_1aab3a01d16c0816fede8b937e133a36c4(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference & document)` | `virtual void` Deletes the document referred to by the provided reference. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction#classfirebase_1_1firestore_1_1_transaction_1ae6783063d3e48296c947fbf1909de697(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference & document, https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1acbed0dcd73b55ce5a9d9c3d07bb9cac5 *error_code, std::string *error_message)` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot` Reads the document referred by the provided reference. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction#classfirebase_1_1firestore_1_1_transaction_1a9465dc81d986b6f066fdf4f41ce978e1(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference & document, const https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1a8c836c76e7e87d8021bf3b33c8a71c7c & data, const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options & options)` | `virtual void` Writes to the document referred to by the provided reference. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction#classfirebase_1_1firestore_1_1_transaction_1ac6153b94bc12a6627f835bbdb632553e(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference & document, const https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1a8c836c76e7e87d8021bf3b33c8a71c7c & data)` | `virtual void` Updates fields in the document referred to by the provided reference. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction#classfirebase_1_1firestore_1_1_transaction_1a8a4d510257cfa3265da50106c5eda01e(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference & document, const https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1a8e8e5e69a7a198ffd86426e741b04187 & data)` | `virtual void` Updates fields in the document referred to by the provided reference. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction#classfirebase_1_1firestore_1_1_transaction_1af871793de14429e1f9c63bdd2246116d(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction#classfirebase_1_1firestore_1_1_transaction & other)=delete` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction#classfirebase_1_1firestore_1_1_transaction &` Deleted copy assignment operator. |

| ### Protected functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction#classfirebase_1_1firestore_1_1_transaction_1ad676b6a4e7b7ad58cc813e7f1c9b86f5()=default` | ` ``` Default constructor, to be used only for mocking a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction#classfirebase_1_1firestore_1_1_transaction`. `` |

## Public functions

### Delete

```c++
virtual void Delete(
  const DocumentReference & document
)
```
Deletes the document referred to by the provided reference.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `document` | The [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) to delete. | |

### Get

```c++
virtual DocumentSnapshot Get(
  const DocumentReference & document,
  Error *error_code,
  std::string *error_message
)
```
Reads the document referred by the provided reference.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `document` | The [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) to read. | | `error_code` | An out parameter to capture an error, if one occurred. | | `error_message` | An out parameter to capture error message, if any. | |
| **Returns** | The contents of the document at this [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) or invalid [DocumentSnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot) if there is any error. |

### Set

```c++
virtual void Set(
  const DocumentReference & document,
  const MapFieldValue & data,
  const SetOptions & options
)
```
Writes to the document referred to by the provided reference.

If the document does not yet exist, it will be created. If you pass [SetOptions](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/set-options#classfirebase_1_1firestore_1_1_set_options), the provided data can be merged into an existing document.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `document` | The [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) to overwrite. | | `data` | A map of the fields and values to write to the document. | | `options` | An object to configure the [Set()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction#classfirebase_1_1firestore_1_1_transaction_1a9465dc81d986b6f066fdf4f41ce978e1) behavior (optional). | |

### Transaction

```c++
 Transaction(
  const Transaction & other
)=delete
```
Deleted copy constructor.

A `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction#classfirebase_1_1firestore_1_1_transaction` object is only valid for the duration of the callback you pass to `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1ad82d5378fb9807f472d3d2bdaa12e696` and cannot be copied.

### Update

```c++
virtual void Update(
  const DocumentReference & document,
  const MapFieldValue & data
)
```
Updates fields in the document referred to by the provided reference.

If no document exists yet, the update will fail.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `document` | The [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) to update. | | `data` | A map of field / value pairs to update. Fields can contain dots to reference nested fields within the document. | |

### Update

```c++
virtual void Update(
  const DocumentReference & document,
  const MapFieldPathValue & data
)
```
Updates fields in the document referred to by the provided reference.

If no document exists yet, the update will fail.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `document` | The [DocumentReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-reference#classfirebase_1_1firestore_1_1_document_reference) to update. | | `data` | A map from [FieldPath](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path) to [FieldValue](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value) to update. | |

### operator=

```c++
Transaction & operator=(
  const Transaction & other
)=delete
```
Deleted copy assignment operator.

A `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction#classfirebase_1_1firestore_1_1_transaction` object is only valid for the duration of the callback you pass to `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore_1ad82d5378fb9807f472d3d2bdaa12e696` and cannot be copied.

### \~Transaction

```c++
virtual  ~Transaction()
```
Destructor.

## Protected functions

### Transaction

```c++
 Transaction()=default
```
Default constructor, to be used only for mocking a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/transaction#classfirebase_1_1firestore_1_1_transaction`.