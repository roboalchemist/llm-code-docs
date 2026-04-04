# Source: https://firebase.google.com/docs/reference/js/firestore_.query.md.txt

# Query class

A `Query` refers to a query which you can read or listen to. You can also construct refined `Query` objects by adding filters and ordering.

**Signature:**  

    export declare class Query<AppModelType = DocumentData, DbModelType extends DocumentData = DocumentData> 

## Constructors

|                                              Constructor                                              | Modifiers |                  Description                   |
|-------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------|
| [(constructor)()](https://firebase.google.com/docs/reference/js/firestore_.query.md#queryconstructor) |           | Constructs a new instance of the `Query` class |

## Properties

|                                           Property                                            | Modifiers |                                                                                        Type                                                                                        |                                           Description                                           |
|-----------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [converter](https://firebase.google.com/docs/reference/js/firestore_.query.md#queryconverter) |           | [FirestoreDataConverter](https://firebase.google.com/docs/reference/js/firestore_.firestoredataconverter.md#firestoredataconverter_interface)\<AppModelType, DbModelType\> \| null | If provided, the `FirestoreDataConverter` associated with this instance.                        |
| [firestore](https://firebase.google.com/docs/reference/js/firestore_.query.md#queryfirestore) |           | [Firestore](https://firebase.google.com/docs/reference/js/firestore_.firestore.md#firestore_class)                                                                                 | The `Firestore` instance for the Firestore database (useful for performing transactions, etc.). |
| [type](https://firebase.google.com/docs/reference/js/firestore_.query.md#querytype)           |           | 'query' \| 'collection'                                                                                                                                                            | The type of this Firestore reference.                                                           |

## Methods

|                                                      Method                                                      | Modifiers |                                                                                                                                                                                 Description                                                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [withConverter(converter)](https://firebase.google.com/docs/reference/js/firestore_.query.md#querywithconverter) |           | Removes the current converter.                                                                                                                                                                                                                                                                                                                                               |
| [withConverter(converter)](https://firebase.google.com/docs/reference/js/firestore_.query.md#querywithconverter) |           | Applies a custom data converter to this query, allowing you to use your own custom model objects with Firestore. When you call [getDocs()](https://firebase.google.com/docs/reference/js/firestore_.md#getdocs_4e56953) with the returned query, the provided converter will convert between Firestore data of type `NewDbModelType` and your custom type `NewAppModelType`. |

## Query.(constructor)

Constructs a new instance of the `Query` class

**Signature:**  

    protected constructor();

## Query.converter

If provided, the `FirestoreDataConverter` associated with this instance.

**Signature:**  

    readonly converter: FirestoreDataConverter<AppModelType, DbModelType> | null;

## Query.firestore

The `Firestore` instance for the Firestore database (useful for performing transactions, etc.).

**Signature:**  

    readonly firestore: Firestore;

## Query.type

The type of this Firestore reference.

**Signature:**  

    readonly type: 'query' | 'collection';

## Query.withConverter()

Removes the current converter.

**Signature:**  

    withConverter(converter: null): Query<DocumentData, DocumentData>;

#### Parameters

| Parameter | Type |              Description              |
|-----------|------|---------------------------------------|
| converter | null | `null` removes the current converter. |

**Returns:**

[Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class)\<[DocumentData](https://firebase.google.com/docs/reference/js/firestore_.documentdata.md#documentdata_interface), [DocumentData](https://firebase.google.com/docs/reference/js/firestore_.documentdata.md#documentdata_interface)\>

A `Query<DocumentData, DocumentData>` that does not use a converter.

## Query.withConverter()

Applies a custom data converter to this query, allowing you to use your own custom model objects with Firestore. When you call [getDocs()](https://firebase.google.com/docs/reference/js/firestore_.md#getdocs_4e56953) with the returned query, the provided converter will convert between Firestore data of type `NewDbModelType` and your custom type `NewAppModelType`.

**Signature:**  

    withConverter<NewAppModelType, NewDbModelType extends DocumentData = DocumentData>(converter: FirestoreDataConverter<NewAppModelType, NewDbModelType>): Query<NewAppModelType, NewDbModelType>;

#### Parameters

| Parameter |                                                                                       Type                                                                                       |               Description               |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| converter | [FirestoreDataConverter](https://firebase.google.com/docs/reference/js/firestore_.firestoredataconverter.md#firestoredataconverter_interface)\<NewAppModelType, NewDbModelType\> | Converts objects to and from Firestore. |

**Returns:**

[Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class)\<NewAppModelType, NewDbModelType\>

A `Query` that uses the provided converter.