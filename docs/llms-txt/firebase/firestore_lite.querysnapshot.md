# Source: https://firebase.google.com/docs/reference/js/firestore_lite.querysnapshot.md.txt

# QuerySnapshot class

A `QuerySnapshot` contains zero or more `DocumentSnapshot` objects representing the results of a query. The documents can be accessed as an array via the `docs` property or enumerated using the `forEach` method. The number of documents can be determined via the `empty` and `size` properties.

**Signature:**  

    export declare class QuerySnapshot<AppModelType = DocumentData, DbModelType extends DocumentData = DocumentData> 

## Properties

|                                                 Property                                                  | Modifiers |                                                                                       Type                                                                                       |                                                                         Description                                                                          |
|-----------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [docs](https://firebase.google.com/docs/reference/js/firestore_lite.querysnapshot.md#querysnapshotdocs)   |           | Array\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_lite.querydocumentsnapshot.md#querydocumentsnapshot_class)\<AppModelType, DbModelType\>\> | An array of all the documents in the `QuerySnapshot`.                                                                                                        |
| [empty](https://firebase.google.com/docs/reference/js/firestore_lite.querysnapshot.md#querysnapshotempty) |           | boolean                                                                                                                                                                          | True if there are no documents in the `QuerySnapshot`.                                                                                                       |
| [query](https://firebase.google.com/docs/reference/js/firestore_lite.querysnapshot.md#querysnapshotquery) |           | [Query](https://firebase.google.com/docs/reference/js/firestore_lite.query.md#query_class)\<AppModelType, DbModelType\>                                                          | The query on which you called [getDocs()](https://firebase.google.com/docs/reference/js/firestore_.md#getdocs_4e56953) in order to get this `QuerySnapshot`. |
| [size](https://firebase.google.com/docs/reference/js/firestore_lite.querysnapshot.md#querysnapshotsize)   |           | number                                                                                                                                                                           | The number of documents in the `QuerySnapshot`.                                                                                                              |

## Methods

|                                                              Method                                                              | Modifiers |                       Description                       |
|----------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------|
| [forEach(callback, thisArg)](https://firebase.google.com/docs/reference/js/firestore_lite.querysnapshot.md#querysnapshotforeach) |           | Enumerates all of the documents in the `QuerySnapshot`. |

## QuerySnapshot.docs

An array of all the documents in the `QuerySnapshot`.

**Signature:**  

    get docs(): Array<QueryDocumentSnapshot<AppModelType, DbModelType>>;

## QuerySnapshot.empty

True if there are no documents in the `QuerySnapshot`.

**Signature:**  

    get empty(): boolean;

## QuerySnapshot.query

The query on which you called [getDocs()](https://firebase.google.com/docs/reference/js/firestore_.md#getdocs_4e56953) in order to get this `QuerySnapshot`.

**Signature:**  

    readonly query: Query<AppModelType, DbModelType>;

## QuerySnapshot.size

The number of documents in the `QuerySnapshot`.

**Signature:**  

    get size(): number;

## QuerySnapshot.forEach()

Enumerates all of the documents in the `QuerySnapshot`.

**Signature:**  

    forEach(callback: (result: QueryDocumentSnapshot<AppModelType, DbModelType>) => void, thisArg?: unknown): void;

#### Parameters

| Parameter |                                                                                            Type                                                                                            |                                        Description                                        |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| callback  | (result: [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_lite.querydocumentsnapshot.md#querydocumentsnapshot_class)\<AppModelType, DbModelType\>) =\> void | A callback to be called with a `QueryDocumentSnapshot` for each document in the snapshot. |
| thisArg   | unknown                                                                                                                                                                                    | The `this` binding for the callback.                                                      |

**Returns:**

void