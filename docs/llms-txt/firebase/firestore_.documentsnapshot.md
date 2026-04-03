# Source: https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md.txt

# DocumentSnapshot class

A `DocumentSnapshot` contains data read from a document in your Firestore database. The data can be extracted with `.data()` or `.get(<field>)` to get a specific field.

For a `DocumentSnapshot` that points to a non-existing document, any data access will return 'undefined'. You can use the `exists()` method to explicitly verify a document's existence.

**Signature:**  

    export declare class DocumentSnapshot<AppModelType = DocumentData, DbModelType extends DocumentData = DocumentData> 

## Constructors

|                                                         Constructor                                                         | Modifiers |                        Description                        |
|-----------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------|
| [(constructor)()](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshotconstructor) |           | Constructs a new instance of the `DocumentSnapshot` class |

## Properties

|                                                     Property                                                      | Modifiers |                                                                          Type                                                                           |                                              Description                                               |
|-------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [id](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshotid)             |           | string                                                                                                                                                  | Property of the `DocumentSnapshot` that provides the document's ID.                                    |
| [metadata](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshotmetadata) |           | [SnapshotMetadata](https://firebase.google.com/docs/reference/js/firestore_.snapshotmetadata.md#snapshotmetadata_class)                                 | Metadata about the `DocumentSnapshot`, including information about its source and local modifications. |
| [ref](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshotref)           |           | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class)\<AppModelType, DbModelType\> | The `DocumentReference` for the document included in the `DocumentSnapshot`.                           |

## Methods

|                                                           Method                                                            | Modifiers |                                                                                                                                  Description                                                                                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [data(options)](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshotdata)          |           | Retrieves all fields in the document as an `Object`. Returns `undefined` if the document doesn't exist.By default, `serverTimestamp()` values that have not yet been set to their final value will be returned as `null`. You can override this by passing an options object. |
| [exists()](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshotexists)             |           | Returns whether or not the data exists. True if the document exists.                                                                                                                                                                                                          |
| [get(fieldPath, options)](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshotget) |           | Retrieves the field specified by `fieldPath`. Returns `undefined` if the document or field doesn't exist.By default, a `serverTimestamp()` that has not yet been set to its final value will be returned as `null`. You can override this by passing an options object.       |
| [toJSON()](https://firebase.google.com/docs/reference/js/firestore_.documentsnapshot.md#documentsnapshottojson)             |           | Returns a JSON-serializable representation of this `DocumentSnapshot` instance.                                                                                                                                                                                               |

## DocumentSnapshot.(constructor)

Constructs a new instance of the `DocumentSnapshot` class

**Signature:**  

    protected constructor();

## DocumentSnapshot.id

Property of the `DocumentSnapshot` that provides the document's ID.

**Signature:**  

    get id(): string;

## DocumentSnapshot.metadata

Metadata about the `DocumentSnapshot`, including information about its source and local modifications.

**Signature:**  

    readonly metadata: SnapshotMetadata;

## DocumentSnapshot.ref

The `DocumentReference` for the document included in the `DocumentSnapshot`.

**Signature:**  

    get ref(): DocumentReference<AppModelType, DbModelType>;

## DocumentSnapshot.data()

Retrieves all fields in the document as an `Object`. Returns `undefined` if the document doesn't exist.

By default, `serverTimestamp()` values that have not yet been set to their final value will be returned as `null`. You can override this by passing an options object.

**Signature:**  

    data(options?: SnapshotOptions): AppModelType | undefined;

#### Parameters

| Parameter |                                                           Type                                                           |                                                                                   Description                                                                                    |
|-----------|--------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| options   | [SnapshotOptions](https://firebase.google.com/docs/reference/js/firestore_.snapshotoptions.md#snapshotoptions_interface) | An options object to configure how data is retrieved from the snapshot (for example the desired behavior for server timestamps that have not yet been set to their final value). |

**Returns:**

AppModelType \| undefined

An `Object` containing all fields in the document or `undefined` if the document doesn't exist.

## DocumentSnapshot.exists()

Returns whether or not the data exists. True if the document exists.

**Signature:**  

    exists(): this is QueryDocumentSnapshot<AppModelType, DbModelType>;

**Returns:**

this is [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.querydocumentsnapshot.md#querydocumentsnapshot_class)\<AppModelType, DbModelType\>

## DocumentSnapshot.get()

Retrieves the field specified by `fieldPath`. Returns `undefined` if the document or field doesn't exist.

By default, a `serverTimestamp()` that has not yet been set to its final value will be returned as `null`. You can override this by passing an options object.

**Signature:**  

    get(fieldPath: string | FieldPath, options?: SnapshotOptions): any;

#### Parameters

| Parameter |                                                           Type                                                           |                                                                                      Description                                                                                      |
|-----------|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fieldPath | string \| [FieldPath](https://firebase.google.com/docs/reference/js/firestore_.fieldpath.md#fieldpath_class)             | The path (for example 'foo' or 'foo.bar') to a specific field.                                                                                                                        |
| options   | [SnapshotOptions](https://firebase.google.com/docs/reference/js/firestore_.snapshotoptions.md#snapshotoptions_interface) | An options object to configure how the field is retrieved from the snapshot (for example the desired behavior for server timestamps that have not yet been set to their final value). |

**Returns:**

any

The data at the specified field location or undefined if no such field exists in the document.

## DocumentSnapshot.toJSON()

Returns a JSON-serializable representation of this `DocumentSnapshot` instance.

**Signature:**  

    toJSON(): object;

**Returns:**

object

a JSON representation of this object. Throws a [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class) if this `DocumentSnapshot` has pending writes.