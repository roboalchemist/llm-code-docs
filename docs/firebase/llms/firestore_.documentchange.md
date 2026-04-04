# Source: https://firebase.google.com/docs/reference/js/firestore_.documentchange.md.txt

# DocumentChange interface

A `DocumentChange` represents a change to the documents matching a query. It contains the document affected and the type of change that occurred.

**Signature:**  

    export declare interface DocumentChange<AppModelType = DocumentData, DbModelType extends DocumentData = DocumentData> 

## Properties

|                                                   Property                                                    |                                                                                Type                                                                                 |                                                                                                                 Description                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [doc](https://firebase.google.com/docs/reference/js/firestore_.documentchange.md#documentchangedoc)           | [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_.querydocumentsnapshot.md#querydocumentsnapshot_class)\<AppModelType, DbModelType\> | The document affected by this change.                                                                                                                                                                                                       |
| [newIndex](https://firebase.google.com/docs/reference/js/firestore_.documentchange.md#documentchangenewindex) | number                                                                                                                                                              | The index of the changed document in the result set immediately after this `DocumentChange` (i.e. supposing that all prior `DocumentChange` objects and the current `DocumentChange` object have been applied). Is -1 for 'removed' events. |
| [oldIndex](https://firebase.google.com/docs/reference/js/firestore_.documentchange.md#documentchangeoldindex) | number                                                                                                                                                              | The index of the changed document in the result set immediately prior to this `DocumentChange` (i.e. supposing that all prior `DocumentChange` objects have been applied). Is `-1` for 'added' events.                                      |
| [type](https://firebase.google.com/docs/reference/js/firestore_.documentchange.md#documentchangetype)         | [DocumentChangeType](https://firebase.google.com/docs/reference/js/firestore_.md#documentchangetype)                                                                | The type of change ('added', 'modified', or 'removed').                                                                                                                                                                                     |

## DocumentChange.doc

The document affected by this change.

**Signature:**  

    readonly doc: QueryDocumentSnapshot<AppModelType, DbModelType>;

## DocumentChange.newIndex

The index of the changed document in the result set immediately after this `DocumentChange` (i.e. supposing that all prior `DocumentChange` objects and the current `DocumentChange` object have been applied). Is -1 for 'removed' events.

**Signature:**  

    readonly newIndex: number;

## DocumentChange.oldIndex

The index of the changed document in the result set immediately prior to this `DocumentChange` (i.e. supposing that all prior `DocumentChange` objects have been applied). Is `-1` for 'added' events.

**Signature:**  

    readonly oldIndex: number;

## DocumentChange.type

The type of change ('added', 'modified', or 'removed').

**Signature:**  

    readonly type: DocumentChangeType;