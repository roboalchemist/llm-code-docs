# Source: https://firebase.google.com/docs/reference/js/firestore_.collectionreference.md.txt

# CollectionReference class

A `CollectionReference` object can be used for adding documents, getting document references, and querying for documents (using [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4)).

**Signature:**  

    export declare class CollectionReference<AppModelType = DocumentData, DbModelType extends DocumentData = DocumentData> extends Query<AppModelType, DbModelType> 

**Extends:** [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class)\<AppModelType, DbModelType\>

## Properties

|                                                      Property                                                       | Modifiers |                                                                                                                                                                                  Type                                                                                                                                                                                  |                                                             Description                                                             |
|---------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [id](https://firebase.google.com/docs/reference/js/firestore_.collectionreference.md#collectionreferenceid)         |           | string                                                                                                                                                                                                                                                                                                                                                                 | The collection's identifier.                                                                                                        |
| [parent](https://firebase.google.com/docs/reference/js/firestore_.collectionreference.md#collectionreferenceparent) |           | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class)\<[DocumentData](https://firebase.google.com/docs/reference/js/firestore_.documentdata.md#documentdata_interface), [DocumentData](https://firebase.google.com/docs/reference/js/firestore_.documentdata.md#documentdata_interface)\> \| null | A reference to the containing `DocumentReference` if this is a subcollection. If this isn't a subcollection, the reference is null. |
| [path](https://firebase.google.com/docs/reference/js/firestore_.collectionreference.md#collectionreferencepath)     |           | string                                                                                                                                                                                                                                                                                                                                                                 | A string representing the path of the referenced collection (relative to the root of the database).                                 |
| [type](https://firebase.google.com/docs/reference/js/firestore_.collectionreference.md#collectionreferencetype)     |           | (not declared)                                                                                                                                                                                                                                                                                                                                                         | The type of this Firestore reference.                                                                                               |

## Methods

|                                                                    Method                                                                    | Modifiers |                                                                                                                                                                                                     Description                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [withConverter(converter)](https://firebase.google.com/docs/reference/js/firestore_.collectionreference.md#collectionreferencewithconverter) |           | Applies a custom data converter to this `CollectionReference`, allowing you to use your own custom model objects with Firestore. When you call [addDoc()](https://firebase.google.com/docs/reference/js/firestore_.md#adddoc_6e783ff) with the returned `CollectionReference` instance, the provided converter will convert between Firestore data of type `NewDbModelType` and your custom type `NewAppModelType`. |
| [withConverter(converter)](https://firebase.google.com/docs/reference/js/firestore_.collectionreference.md#collectionreferencewithconverter) |           | Removes the current converter.                                                                                                                                                                                                                                                                                                                                                                                      |

## CollectionReference.id

The collection's identifier.

**Signature:**  

    get id(): string;

## CollectionReference.parent

A reference to the containing `DocumentReference` if this is a subcollection. If this isn't a subcollection, the reference is null.

**Signature:**  

    get parent(): DocumentReference<DocumentData, DocumentData> | null;

## CollectionReference.path

A string representing the path of the referenced collection (relative to the root of the database).

**Signature:**  

    get path(): string;

## CollectionReference.type

The type of this Firestore reference.

**Signature:**  

    readonly type = "collection";

## CollectionReference.withConverter()

Applies a custom data converter to this `CollectionReference`, allowing you to use your own custom model objects with Firestore. When you call [addDoc()](https://firebase.google.com/docs/reference/js/firestore_.md#adddoc_6e783ff) with the returned `CollectionReference` instance, the provided converter will convert between Firestore data of type `NewDbModelType` and your custom type `NewAppModelType`.

**Signature:**  

    withConverter<NewAppModelType, NewDbModelType extends DocumentData = DocumentData>(converter: FirestoreDataConverter<NewAppModelType, NewDbModelType>): CollectionReference<NewAppModelType, NewDbModelType>;

#### Parameters

| Parameter |                                                                                       Type                                                                                       |               Description               |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| converter | [FirestoreDataConverter](https://firebase.google.com/docs/reference/js/firestore_.firestoredataconverter.md#firestoredataconverter_interface)\<NewAppModelType, NewDbModelType\> | Converts objects to and from Firestore. |

**Returns:**

[CollectionReference](https://firebase.google.com/docs/reference/js/firestore_.collectionreference.md#collectionreference_class)\<NewAppModelType, NewDbModelType\>

A `CollectionReference` that uses the provided converter.

## CollectionReference.withConverter()

Removes the current converter.

**Signature:**  

    withConverter(converter: null): CollectionReference<DocumentData, DocumentData>;

#### Parameters

| Parameter | Type |              Description              |
|-----------|------|---------------------------------------|
| converter | null | `null` removes the current converter. |

**Returns:**

[CollectionReference](https://firebase.google.com/docs/reference/js/firestore_.collectionreference.md#collectionreference_class)\<[DocumentData](https://firebase.google.com/docs/reference/js/firestore_.documentdata.md#documentdata_interface), [DocumentData](https://firebase.google.com/docs/reference/js/firestore_.documentdata.md#documentdata_interface)\>

A `CollectionReference<DocumentData, DocumentData>` that does not use a converter.