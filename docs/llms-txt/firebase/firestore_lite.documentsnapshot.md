# Source: https://firebase.google.com/docs/reference/js/firestore_lite.documentsnapshot.md.txt

# DocumentSnapshot class

A `DocumentSnapshot` contains data read from a document in your Firestore database. The data can be extracted with `.data()` or `.get(<field>)` to get a specific field.

For a `DocumentSnapshot` that points to a non-existing document, any data access will return 'undefined'. You can use the `exists()` method to explicitly verify a document's existence.

**Signature:**  

    export declare class DocumentSnapshot<AppModelType = DocumentData, DbModelType extends DocumentData = DocumentData> 

## Constructors

|                                                           Constructor                                                           | Modifiers |                        Description                        |
|---------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------|
| [(constructor)()](https://firebase.google.com/docs/reference/js/firestore_lite.documentsnapshot.md#documentsnapshotconstructor) |           | Constructs a new instance of the `DocumentSnapshot` class |

## Properties

|                                                  Property                                                   | Modifiers |                                                                            Type                                                                             |                                 Description                                  |
|-------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| [id](https://firebase.google.com/docs/reference/js/firestore_lite.documentsnapshot.md#documentsnapshotid)   |           | string                                                                                                                                                      | Property of the `DocumentSnapshot` that provides the document's ID.          |
| [ref](https://firebase.google.com/docs/reference/js/firestore_lite.documentsnapshot.md#documentsnapshotref) |           | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | The `DocumentReference` for the document included in the `DocumentSnapshot`. |

## Methods

|                                                         Method                                                         | Modifiers |                                                Description                                                |
|------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------|
| [data()](https://firebase.google.com/docs/reference/js/firestore_lite.documentsnapshot.md#documentsnapshotdata)        |           | Retrieves all fields in the document as an `Object`. Returns `undefined` if the document doesn't exist.   |
| [exists()](https://firebase.google.com/docs/reference/js/firestore_lite.documentsnapshot.md#documentsnapshotexists)    |           | Signals whether or not the document at the snapshot's location exists.                                    |
| [get(fieldPath)](https://firebase.google.com/docs/reference/js/firestore_lite.documentsnapshot.md#documentsnapshotget) |           | Retrieves the field specified by `fieldPath`. Returns `undefined` if the document or field doesn't exist. |

## DocumentSnapshot.(constructor)

Constructs a new instance of the `DocumentSnapshot` class

**Signature:**  

    protected constructor();

## DocumentSnapshot.id

Property of the `DocumentSnapshot` that provides the document's ID.

**Signature:**  

    get id(): string;

## DocumentSnapshot.ref

The `DocumentReference` for the document included in the `DocumentSnapshot`.

**Signature:**  

    get ref(): DocumentReference<AppModelType, DbModelType>;

## DocumentSnapshot.data()

Retrieves all fields in the document as an `Object`. Returns `undefined` if the document doesn't exist.

**Signature:**  

    data(): AppModelType | undefined;

**Returns:**

AppModelType \| undefined

An `Object` containing all fields in the document or `undefined` if the document doesn't exist.

## DocumentSnapshot.exists()

Signals whether or not the document at the snapshot's location exists.

**Signature:**  

    exists(): this is QueryDocumentSnapshot<AppModelType, DbModelType>;

**Returns:**

this is [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_lite.querydocumentsnapshot.md#querydocumentsnapshot_class)\<AppModelType, DbModelType\>

true if the document exists.

## DocumentSnapshot.get()

Retrieves the field specified by `fieldPath`. Returns `undefined` if the document or field doesn't exist.

**Signature:**  

    get(fieldPath: string | FieldPath): any;

#### Parameters

| Parameter |                                                       Type                                                       |                          Description                           |
|-----------|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| fieldPath | string \| [FieldPath](https://firebase.google.com/docs/reference/js/firestore_lite.fieldpath.md#fieldpath_class) | The path (for example 'foo' or 'foo.bar') to a specific field. |

**Returns:**

any

The data at the specified field location or undefined if no such field exists in the document.