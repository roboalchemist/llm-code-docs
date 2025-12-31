# Source: https://firebase.google.com/docs/reference/js/firestore_lite.writebatch.md.txt

# WriteBatch class

A write batch, used to perform multiple writes as a single atomic unit.

A `WriteBatch` object can be acquired by calling [writeBatch()](https://firebase.google.com/docs/reference/js/firestore_.md#writebatch_231a8e0). It provides methods for adding writes to the write batch. None of the writes will be committed (or visible locally) until [WriteBatch.commit()](https://firebase.google.com/docs/reference/js/firestore_.writebatch.md#writebatchcommit) is called.

**Signature:**  

    export declare class WriteBatch 

## Methods

|                                                                        Method                                                                         | Modifiers |                                                                                                                                                                           Description                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [commit()](https://firebase.google.com/docs/reference/js/firestore_lite.writebatch.md#writebatchcommit)                                               |           | Commits all of the writes in this write batch as a single atomic unit.The result of these writes will only be reflected in document reads that occur after the returned promise resolves. If the client is offline, the write fails. If you would like to see local modifications or buffer writes until the client is online, use the full Firestore SDK.      |
| [delete(documentRef)](https://firebase.google.com/docs/reference/js/firestore_lite.writebatch.md#writebatchdelete)                                    |           | Deletes the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class).                                                                                                                                                                                    |
| [set(documentRef, data)](https://firebase.google.com/docs/reference/js/firestore_lite.writebatch.md#writebatchset)                                    |           | Writes to the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class). If the document does not exist yet, it will be created.                                                                                                                          |
| [set(documentRef, data, options)](https://firebase.google.com/docs/reference/js/firestore_lite.writebatch.md#writebatchset)                           |           | Writes to the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class). If the document does not exist yet, it will be created. If you provide `merge` or `mergeFields`, the provided data can be merged into an existing document.                      |
| [update(documentRef, data)](https://firebase.google.com/docs/reference/js/firestore_lite.writebatch.md#writebatchupdate)                              |           | Updates fields in the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class). The update will fail if applied to a document that does not exist.                                                                                                       |
| [update(documentRef, field, value, moreFieldsAndValues)](https://firebase.google.com/docs/reference/js/firestore_lite.writebatch.md#writebatchupdate) |           | Updates fields in the document referred to by this [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class). The update will fail if applied to a document that does not exist.Nested fields can be update by providing dot-separated field path strings or by providing `FieldPath` objects. |

## WriteBatch.commit()

Commits all of the writes in this write batch as a single atomic unit.

The result of these writes will only be reflected in document reads that occur after the returned promise resolves. If the client is offline, the write fails. If you would like to see local modifications or buffer writes until the client is online, use the full Firestore SDK.

**Signature:**  

    commit(): Promise<void>;

**Returns:**

Promise\<void\>

A `Promise` resolved once all of the writes in the batch have been successfully written to the backend as an atomic unit (note that it won't resolve while you're offline).

## WriteBatch.delete()

Deletes the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class).

**Signature:**  

    delete<AppModelType, DbModelType extends DocumentData>(documentRef: DocumentReference<AppModelType, DbModelType>): WriteBatch;

#### Parameters

|  Parameter  |                                                                            Type                                                                             |                Description                 |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| documentRef | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to the document to be deleted. |

**Returns:**

[WriteBatch](https://firebase.google.com/docs/reference/js/firestore_lite.writebatch.md#writebatch_class)

This `WriteBatch` instance. Used for chaining method calls.

## WriteBatch.set()

Writes to the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class). If the document does not exist yet, it will be created.

**Signature:**  

    set<AppModelType, DbModelType extends DocumentData>(documentRef: DocumentReference<AppModelType, DbModelType>, data: WithFieldValue<AppModelType>): WriteBatch;

#### Parameters

|  Parameter  |                                                                            Type                                                                             |                     Description                      |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| documentRef | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to the document to be set.               |
| data        | [WithFieldValue](https://firebase.google.com/docs/reference/js/firestore_lite.md#withfieldvalue)\<AppModelType\>                                            | An object of the fields and values for the document. |

**Returns:**

[WriteBatch](https://firebase.google.com/docs/reference/js/firestore_lite.writebatch.md#writebatch_class)

This `WriteBatch` instance. Used for chaining method calls.

## WriteBatch.set()

Writes to the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class). If the document does not exist yet, it will be created. If you provide `merge` or `mergeFields`, the provided data can be merged into an existing document.

**Signature:**  

    set<AppModelType, DbModelType extends DocumentData>(documentRef: DocumentReference<AppModelType, DbModelType>, data: PartialWithFieldValue<AppModelType>, options: SetOptions): WriteBatch;

#### Parameters

|  Parameter  |                                                                            Type                                                                             |                     Description                      |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| documentRef | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to the document to be set.               |
| data        | [PartialWithFieldValue](https://firebase.google.com/docs/reference/js/firestore_lite.md#partialwithfieldvalue)\<AppModelType\>                              | An object of the fields and values for the document. |
| options     | [SetOptions](https://firebase.google.com/docs/reference/js/firestore_lite.md#setoptions)                                                                    | An object to configure the set behavior.             |

**Returns:**

[WriteBatch](https://firebase.google.com/docs/reference/js/firestore_lite.writebatch.md#writebatch_class)

This `WriteBatch` instance. Used for chaining method calls.

#### Exceptions

Error - If the provided input is not a valid Firestore document.

## WriteBatch.update()

Updates fields in the document referred to by the provided [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class). The update will fail if applied to a document that does not exist.

**Signature:**  

    update<AppModelType, DbModelType extends DocumentData>(documentRef: DocumentReference<AppModelType, DbModelType>, data: UpdateData<DbModelType>): WriteBatch;

#### Parameters

|  Parameter  |                                                                            Type                                                                             |                                                                      Description                                                                      |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| documentRef | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to the document to be updated.                                                                                                            |
| data        | [UpdateData](https://firebase.google.com/docs/reference/js/firestore_lite.md#updatedata)\<DbModelType\>                                                     | An object containing the fields and values with which to update the document. Fields can contain dots to reference nested fields within the document. |

**Returns:**

[WriteBatch](https://firebase.google.com/docs/reference/js/firestore_lite.writebatch.md#writebatch_class)

This `WriteBatch` instance. Used for chaining method calls.

#### Exceptions

Error - If the provided input is not valid Firestore data.

## WriteBatch.update()

Updates fields in the document referred to by this [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class). The update will fail if applied to a document that does not exist.

Nested fields can be update by providing dot-separated field path strings or by providing `FieldPath` objects.

**Signature:**  

    update<AppModelType, DbModelType extends DocumentData>(documentRef: DocumentReference<AppModelType, DbModelType>, field: string | FieldPath, value: unknown, ...moreFieldsAndValues: unknown[]): WriteBatch;

#### Parameters

|      Parameter      |                                                                            Type                                                                             |                Description                 |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| documentRef         | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | A reference to the document to be updated. |
| field               | string \| [FieldPath](https://firebase.google.com/docs/reference/js/firestore_lite.fieldpath.md#fieldpath_class)                                            | The first field to update.                 |
| value               | unknown                                                                                                                                                     | The first value.                           |
| moreFieldsAndValues | unknown\[\]                                                                                                                                                 | Additional key value pairs.                |

**Returns:**

[WriteBatch](https://firebase.google.com/docs/reference/js/firestore_lite.writebatch.md#writebatch_class)

This `WriteBatch` instance. Used for chaining method calls.

#### Exceptions

Error - If the provided input is not valid Firestore data.