# Source: https://firebase.google.com/docs/reference/js/firestore_lite.transaction.md.txt

# Transaction class

A reference to a transaction.

The `Transaction` object passed to a transaction's `updateFunction` provides the methods to read and write data within the transaction context. See [runTransaction()](https://firebase.google.com/docs/reference/js/firestore_.md#runtransaction_6f03ec4).

**Signature:**  

    export declare class Transaction 

## Methods

|                                                                         Method                                                                          | Modifiers |                                                                                                                                                                               Description                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [delete(documentRef)](https://firebase.google.com/docs/reference/js/firestore_lite.transaction.md#transactiondelete)                                    |           | Deletes the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class).                                                                                                                                                                                             |
| [get(documentRef)](https://firebase.google.com/docs/reference/js/firestore_lite.transaction.md#transactionget)                                          |           | Reads the document referenced by the provided [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class).                                                                                                                                                                                                |
| [set(documentRef, data)](https://firebase.google.com/docs/reference/js/firestore_lite.transaction.md#transactionset)                                    |           | Writes to the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class). If the document does not exist yet, it will be created.                                                                                                                                   |
| [set(documentRef, data, options)](https://firebase.google.com/docs/reference/js/firestore_lite.transaction.md#transactionset)                           |           | Writes to the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class). If the document does not exist yet, it will be created. If you provide `merge` or `mergeFields`, the provided data can be merged into an existing document.                               |
| [update(documentRef, data)](https://firebase.google.com/docs/reference/js/firestore_lite.transaction.md#transactionupdate)                              |           | Updates fields in the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class). The update will fail if applied to a document that does not exist.                                                                                                                |
| [update(documentRef, field, value, moreFieldsAndValues)](https://firebase.google.com/docs/reference/js/firestore_lite.transaction.md#transactionupdate) |           | Updates fields in the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class). The update will fail if applied to a document that does not exist.Nested fields can be updated by providing dot-separated field path strings or by providing `FieldPath` objects. |

## Transaction.delete()

Deletes the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class).

**Signature:**  

    delete<AppModelType, DbModelType extends DocumentData>(documentRef: DocumentReference<AppModelType, DbModelType>): this;

#### Parameters

|  Parameter  |                                                                            Type                                                                             |                Description                 |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| documentRef | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to the document to be deleted. |

**Returns:**

this

This `Transaction` instance. Used for chaining method calls.

## Transaction.get()

Reads the document referenced by the provided [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class).

**Signature:**  

    get<AppModelType, DbModelType extends DocumentData>(documentRef: DocumentReference<AppModelType, DbModelType>): Promise<DocumentSnapshot<AppModelType, DbModelType>>;

#### Parameters

|  Parameter  |                                                                            Type                                                                             |               Description               |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| documentRef | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to the document to be read. |

**Returns:**

Promise\<[DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_lite.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\>\>

A `DocumentSnapshot` with the read data.

## Transaction.set()

Writes to the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class). If the document does not exist yet, it will be created.

**Signature:**  

    set<AppModelType, DbModelType extends DocumentData>(documentRef: DocumentReference<AppModelType, DbModelType>, data: WithFieldValue<AppModelType>): this;

#### Parameters

|  Parameter  |                                                                            Type                                                                             |                     Description                      |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| documentRef | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to the document to be set.               |
| data        | [WithFieldValue](https://firebase.google.com/docs/reference/js/firestore_lite.md#withfieldvalue)\<AppModelType\>                                            | An object of the fields and values for the document. |

**Returns:**

this

This `Transaction` instance. Used for chaining method calls.

#### Exceptions

Error - If the provided input is not a valid Firestore document.

## Transaction.set()

Writes to the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class). If the document does not exist yet, it will be created. If you provide `merge` or `mergeFields`, the provided data can be merged into an existing document.

**Signature:**  

    set<AppModelType, DbModelType extends DocumentData>(documentRef: DocumentReference<AppModelType, DbModelType>, data: PartialWithFieldValue<AppModelType>, options: SetOptions): this;

#### Parameters

|  Parameter  |                                                                            Type                                                                             |                     Description                      |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| documentRef | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to the document to be set.               |
| data        | [PartialWithFieldValue](https://firebase.google.com/docs/reference/js/firestore_lite.md#partialwithfieldvalue)\<AppModelType\>                              | An object of the fields and values for the document. |
| options     | [SetOptions](https://firebase.google.com/docs/reference/js/firestore_lite.md#setoptions)                                                                    | An object to configure the set behavior.             |

**Returns:**

this

This `Transaction` instance. Used for chaining method calls.

#### Exceptions

Error - If the provided input is not a valid Firestore document.

## Transaction.update()

Updates fields in the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class). The update will fail if applied to a document that does not exist.

**Signature:**  

    update<AppModelType, DbModelType extends DocumentData>(documentRef: DocumentReference<AppModelType, DbModelType>, data: UpdateData<DbModelType>): this;

#### Parameters

|  Parameter  |                                                                            Type                                                                             |                                                                      Description                                                                      |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| documentRef | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to the document to be updated.                                                                                                            |
| data        | [UpdateData](https://firebase.google.com/docs/reference/js/firestore_lite.md#updatedata)\<DbModelType\>                                                     | An object containing the fields and values with which to update the document. Fields can contain dots to reference nested fields within the document. |

**Returns:**

this

This `Transaction` instance. Used for chaining method calls.

#### Exceptions

Error - If the provided input is not valid Firestore data.

## Transaction.update()

Updates fields in the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class). The update will fail if applied to a document that does not exist.

Nested fields can be updated by providing dot-separated field path strings or by providing `FieldPath` objects.

**Signature:**  

    update<AppModelType, DbModelType extends DocumentData>(documentRef: DocumentReference<AppModelType, DbModelType>, field: string | FieldPath, value: unknown, ...moreFieldsAndValues: unknown[]): this;

#### Parameters

|      Parameter      |                                                                            Type                                                                             |                Description                 |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| documentRef         | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to the document to be updated. |
| field               | string \| [FieldPath](https://firebase.google.com/docs/reference/js/firestore_lite.fieldpath.md#fieldpath_class)                                            | The first field to update.                 |
| value               | unknown                                                                                                                                                     | The first value.                           |
| moreFieldsAndValues | unknown\[\]                                                                                                                                                 | Additional key/value pairs.                |

**Returns:**

this

This `Transaction` instance. Used for chaining method calls.

#### Exceptions

Error - If the provided input is not valid Firestore data.