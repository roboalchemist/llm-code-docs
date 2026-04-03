# Source: https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md.txt

# DocumentReference class

A `DocumentReference` refers to a document location in a Firestore database and can be used to write, read, or listen to the location. The document at the referenced location may or may not exist.

**Signature:**  

    export declare class DocumentReference<AppModelType = DocumentData, DbModelType extends DocumentData = DocumentData> 

## Properties

|                                                         Property                                                          | Modifiers |                                                                                          Type                                                                                          |                                                                                         Description                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [converter](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreferenceconverter) |           | [FirestoreDataConverter](https://firebase.google.com/docs/reference/js/firestore_lite.firestoredataconverter.md#firestoredataconverter_interface)\<AppModelType, DbModelType\> \| null | If provided, the `FirestoreDataConverter` associated with this instance.                                                                                                                     |
| [firestore](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreferencefirestore) |           | [Firestore](https://firebase.google.com/docs/reference/js/firestore_lite.firestore.md#firestore_class)                                                                                 | The [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance the document is in. This is useful for performing transactions, for example. |
| [id](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreferenceid)               |           | string                                                                                                                                                                                 | The document's identifier within its collection.                                                                                                                                             |
| [parent](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreferenceparent)       |           | [CollectionReference](https://firebase.google.com/docs/reference/js/firestore_lite.collectionreference.md#collectionreference_class)\<AppModelType, DbModelType\>                      | The collection this `DocumentReference` belongs to.                                                                                                                                          |
| [path](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreferencepath)           |           | string                                                                                                                                                                                 | A string representing the path of the referenced document (relative to the root of the database).                                                                                            |
| [type](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreferencetype)           |           | (not declared)                                                                                                                                                                         | The type of this Firestore reference.                                                                                                                                                        |

## Methods

|                                                                       Method                                                                        | Modifiers |                                                                                                                                                                                                                                                      Description                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [fromJSON(firestore, json)](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreferencefromjson)            | `static`  | Builds a `DocumentReference` instance from a JSON object created by [DocumentReference.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreferencetojson).                                                                                                                                                                                                                                                                                                              |
| [fromJSON(firestore, json, converter)](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreferencefromjson) | `static`  | Builds a `DocumentReference` instance from a JSON object created by [DocumentReference.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreferencetojson).                                                                                                                                                                                                                                                                                                              |
| [toJSON()](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreferencetojson)                               |           | Returns a JSON-serializable representation of this `DocumentReference` instance.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [withConverter(converter)](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreferencewithconverter)        |           | Applies a custom data converter to this `DocumentReference`, allowing you to use your own custom model objects with Firestore. When you call [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad), [getDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#getdoc_4569087), etc. with the returned `DocumentReference` instance, the provided converter will convert between Firestore data of type `NewDbModelType` and your custom type `NewAppModelType`. |
| [withConverter(converter)](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreferencewithconverter)        |           | Removes the current converter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## DocumentReference.converter

If provided, the `FirestoreDataConverter` associated with this instance.

**Signature:**  

    readonly converter: FirestoreDataConverter<AppModelType, DbModelType> | null;

## DocumentReference.firestore

The [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance the document is in. This is useful for performing transactions, for example.

**Signature:**  

    readonly firestore: Firestore;

## DocumentReference.id

The document's identifier within its collection.

**Signature:**  

    get id(): string;

## DocumentReference.parent

The collection this `DocumentReference` belongs to.

**Signature:**  

    get parent(): CollectionReference<AppModelType, DbModelType>;

## DocumentReference.path

A string representing the path of the referenced document (relative to the root of the database).

**Signature:**  

    get path(): string;

## DocumentReference.type

The type of this Firestore reference.

**Signature:**  

    readonly type = "document";

## DocumentReference.fromJSON()

Builds a `DocumentReference` instance from a JSON object created by [DocumentReference.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreferencetojson).

**Signature:**  

    static fromJSON(firestore: Firestore, json: object): DocumentReference;

#### Parameters

| Parameter |                                                  Type                                                  |                                                                    Description                                                                     |
|-----------|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| firestore | [Firestore](https://firebase.google.com/docs/reference/js/firestore_lite.firestore.md#firestore_class) | The [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance the snapshot should be loaded for. |
| json      | object                                                                                                 | a JSON object represention of a `DocumentReference` instance                                                                                       |

**Returns:**

[DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)

an instance of [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class) if the JSON object could be parsed. Throws a [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class) if an error occurs.

## DocumentReference.fromJSON()

Builds a `DocumentReference` instance from a JSON object created by [DocumentReference.toJSON()](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreferencetojson).

**Signature:**  

    static fromJSON<NewAppModelType = DocumentData, NewDbModelType extends DocumentData = DocumentData>(firestore: Firestore, json: object, converter: FirestoreDataConverter<NewAppModelType, NewDbModelType>): DocumentReference<NewAppModelType, NewDbModelType>;

#### Parameters

| Parameter |                                                                                         Type                                                                                         |                                                                    Description                                                                     |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| firestore | [Firestore](https://firebase.google.com/docs/reference/js/firestore_lite.firestore.md#firestore_class)                                                                               | The [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class) instance the snapshot should be loaded for. |
| json      | object                                                                                                                                                                               | a JSON object represention of a `DocumentReference` instance                                                                                       |
| converter | [FirestoreDataConverter](https://firebase.google.com/docs/reference/js/firestore_lite.firestoredataconverter.md#firestoredataconverter_interface)\<NewAppModelType, NewDbModelType\> | Converts objects to and from Firestore.                                                                                                            |

**Returns:**

[DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<NewAppModelType, NewDbModelType\>

an instance of [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class) if the JSON object could be parsed. Throws a [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class) if an error occurs.

## DocumentReference.toJSON()

Returns a JSON-serializable representation of this `DocumentReference` instance.

**Signature:**  

    toJSON(): object;

**Returns:**

object

a JSON representation of this object.

## DocumentReference.withConverter()

Applies a custom data converter to this `DocumentReference`, allowing you to use your own custom model objects with Firestore. When you call [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad), [getDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#getdoc_4569087), etc. with the returned `DocumentReference` instance, the provided converter will convert between Firestore data of type `NewDbModelType` and your custom type `NewAppModelType`.

**Signature:**  

    withConverter<NewAppModelType, NewDbModelType extends DocumentData = DocumentData>(converter: FirestoreDataConverter<NewAppModelType, NewDbModelType>): DocumentReference<NewAppModelType, NewDbModelType>;

#### Parameters

| Parameter |                                                                                         Type                                                                                         |               Description               |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| converter | [FirestoreDataConverter](https://firebase.google.com/docs/reference/js/firestore_lite.firestoredataconverter.md#firestoredataconverter_interface)\<NewAppModelType, NewDbModelType\> | Converts objects to and from Firestore. |

**Returns:**

[DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<NewAppModelType, NewDbModelType\>

A `DocumentReference` that uses the provided converter.

## DocumentReference.withConverter()

Removes the current converter.

**Signature:**  

    withConverter(converter: null): DocumentReference<DocumentData, DocumentData>;

#### Parameters

| Parameter | Type |              Description              |
|-----------|------|---------------------------------------|
| converter | null | `null` removes the current converter. |

**Returns:**

[DocumentReference](https://firebase.google.com/docs/reference/js/firestore_lite.documentreference.md#documentreference_class)\<[DocumentData](https://firebase.google.com/docs/reference/js/firestore_lite.documentdata.md#documentdata_interface), [DocumentData](https://firebase.google.com/docs/reference/js/firestore_lite.documentdata.md#documentdata_interface)\>

A `DocumentReference<DocumentData, DocumentData>` that does not use a converter.