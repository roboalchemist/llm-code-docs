# Source: https://firebase.google.com/docs/reference/js/firestore_lite.querydocumentsnapshot.md.txt

# QueryDocumentSnapshot class

A `QueryDocumentSnapshot` contains data read from a document in your Firestore database as part of a query. The document is guaranteed to exist and its data can be extracted with `.data()` or `.get(<field>)` to get a specific field.

A `QueryDocumentSnapshot` offers the same API surface as a `DocumentSnapshot`. Since query results contain only existing documents, the `exists` property will always be true and `data()` will never return 'undefined'.

**Signature:**  

    export declare class QueryDocumentSnapshot<AppModelType = DocumentData, DbModelType extends DocumentData = DocumentData> extends DocumentSnapshot<AppModelType, DbModelType> 

**Extends:** [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_lite.documentsnapshot.md#documentsnapshot_class)\<AppModelType, DbModelType\>

## Methods

|                                                          Method                                                           | Modifiers |                     Description                      |
|---------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------|
| [data()](https://firebase.google.com/docs/reference/js/firestore_lite.querydocumentsnapshot.md#querydocumentsnapshotdata) |           | Retrieves all fields in the document as an `Object`. |

## QueryDocumentSnapshot.data()

Retrieves all fields in the document as an `Object`.

**Signature:**  

    /** @override */
    data(): AppModelType;

**Returns:**

AppModelType

An `Object` containing all fields in the document.