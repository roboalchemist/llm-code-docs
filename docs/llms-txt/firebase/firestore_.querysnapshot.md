# Source: https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md.txt

# QuerySnapshot class

A `QuerySnapshot` contains zero or more `DocumentSnapshot` objects representing the results of a query. The documents can be accessed as an array via the `docs` property or enumerated using the `forEach` method. The number of documents can be determined via the `empty` and `size` properties.

**Signature:**  

    export declare class QuerySnapshot<AppModelType = DocumentData, DbModelType extends DocumentData = DocumentData> 

## Properties

|                                                  Property                                                   | Modifiers |                                                                                     Type                                                                                     |                                        Description                                        |
|-------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [docs](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshotdocs)         |           | Array\<[QueryDocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.querydocumentsnapshot.md#querydocumentsnapshot_class)\<AppModelType, DbModelType\>\> | An array of all the documents in the `QuerySnapshot`.                                     |
| [empty](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshotempty)       |           | boolean                                                                                                                                                                      | True if there are no documents in the `QuerySnapshot`.                                    |
| [metadata](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshotmetadata) |           | [SnapshotMetadata](https://firebase.google.com/docs/reference/js/firestore_.snapshotmetadata.md#snapshotmetadata_class)                                                      | Metadata about this snapshot, concerning its source and if it has local modifications.    |
| [query](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshotquery)       |           | [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class)\<AppModelType, DbModelType\>                                                          | The query on which you called `get` or `onSnapshot` in order to get this `QuerySnapshot`. |
| [size](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshotsize)         |           | number                                                                                                                                                                       | The number of documents in the `QuerySnapshot`.                                           |

## Methods

|                                                            Method                                                            | Modifiers |                                                                       Description                                                                       |
|------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [docChanges(options)](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshotdocchanges)     |           | Returns an array of the documents changes since the last snapshot. If this is the first snapshot, all documents will be in the list as 'added' changes. |
| [forEach(callback, thisArg)](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshotforeach) |           | Enumerates all of the documents in the `QuerySnapshot`.                                                                                                 |
| [toJSON()](https://firebase.google.com/docs/reference/js/firestore_.querysnapshot.md#querysnapshottojson)                    |           | Returns a JSON-serializable representation of this `QuerySnapshot` instance.                                                                            |

## QuerySnapshot.docs

An array of all the documents in the `QuerySnapshot`.

**Signature:**  

    get docs(): Array<QueryDocumentSnapshot<AppModelType, DbModelType>>;

## QuerySnapshot.empty

True if there are no documents in the `QuerySnapshot`.

**Signature:**  

    get empty(): boolean;

## QuerySnapshot.metadata

Metadata about this snapshot, concerning its source and if it has local modifications.

**Signature:**  

    readonly metadata: SnapshotMetadata;

## QuerySnapshot.query

The query on which you called `get` or `onSnapshot` in order to get this `QuerySnapshot`.

**Signature:**  

    readonly query: Query<AppModelType, DbModelType>;

## QuerySnapshot.size

The number of documents in the `QuerySnapshot`.

**Signature:**  

    get size(): number;

## QuerySnapshot.docChanges()

Returns an array of the documents changes since the last snapshot. If this is the first snapshot, all documents will be in the list as 'added' changes.

**Signature:**  

    docChanges(options?: SnapshotListenOptions): Array<DocumentChange<AppModelType, DbModelType>>;

#### Parameters

| Parameter |                                                                    Type                                                                    |                                                                    Description                                                                     |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| options   | [SnapshotListenOptions](https://firebase.google.com/docs/reference/js/firestore_.snapshotlistenoptions.md#snapshotlistenoptions_interface) | `SnapshotListenOptions` that control whether metadata-only changes (i.e. only `DocumentSnapshot.metadata` changed) should trigger snapshot events. |

**Returns:**

Array\<[DocumentChange](https://firebase.google.com/docs/reference/js/firestore_.documentchange.md#documentchange_interface)\<AppModelType, DbModelType\>\>

## QuerySnapshot.forEach()

Enumerates all of the documents in the `QuerySnapshot`.

**Signature:**  

    forEach(callback: (result: QueryDocumentSnapshot<AppModelType, DbModelType>) => void, thisArg?: unknown): void;

#### Parameters

| Parameter |                                                                                          Type                                                                                          |                                        Description                                        |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| callback  | (result: [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.querydocumentsnapshot.md#querydocumentsnapshot_class)\<AppModelType, DbModelType\>) =\> void | A callback to be called with a `QueryDocumentSnapshot` for each document in the snapshot. |
| thisArg   | unknown                                                                                                                                                                                | The `this` binding for the callback.                                                      |

**Returns:**

void

## QuerySnapshot.toJSON()

Returns a JSON-serializable representation of this `QuerySnapshot` instance.

**Signature:**  

    toJSON(): object;

**Returns:**

object

a JSON representation of this object. Throws a [FirestoreError](https://firebase.google.com/docs/reference/js/firestore_.firestoreerror.md#firestoreerror_class) if this `QuerySnapshot` has pending writes.