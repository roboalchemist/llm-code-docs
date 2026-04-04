# Source: https://firebase.google.com/docs/reference/js/firestore_.querydocumentsnapshot.md.txt

# QueryDocumentSnapshot class

A `QueryDocumentSnapshot` contains data read from a document in your Firestore database as part of a query. The document is guaranteed to exist and its data can be extracted with `.data()` or `.get(<field>)` to get a specific field.

A `QueryDocumentSnapshot` offers the same API surface as a `DocumentSnapshot`. Since query results contain only existing documents, the `exists` property will always be true and `data()` will never return 'undefined'.

**Signature:**  

    export declare class QueryDocumentSnapshot<AppModelType = DocumentData, DbModelType extends DocumentData = DocumentData> extends DocumentSnapshot<AppModelType, DbModelType> 

**Extends:** [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\>

## Methods

|                                                            Method                                                            | Modifiers |                                                                                                        Description                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [data(options)](https://firebase.google.com/docs/reference/js/firestore_.querydocumentsnapshot.md#querydocumentsnapshotdata) |           | Retrieves all fields in the document as an `Object`.By default, `serverTimestamp()` values that have not yet been set to their final value will be returned as `null`. You can override this by passing an options object. |

## QueryDocumentSnapshot.data()

Retrieves all fields in the document as an `Object`.

By default, `serverTimestamp()` values that have not yet been set to their final value will be returned as `null`. You can override this by passing an options object.

**Signature:**  

    /** @override */
    data(options?: SnapshotOptions): AppModelType;

#### Parameters

| Parameter |                                                           Type                                                           |                                                                                   Description                                                                                    |
|-----------|--------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| options   | [SnapshotOptions](https://firebase.google.com/docs/reference/js/firestore_.snapshotoptions.md#snapshotoptions_interface) | An options object to configure how data is retrieved from the snapshot (for example the desired behavior for server timestamps that have not yet been set to their final value). |

**Returns:**

AppModelType

An `Object` containing all fields in the document.