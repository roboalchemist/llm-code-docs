# Source: https://firebase.google.com/docs/reference/js/firestore_lite.queryendatconstraint.md.txt

# QueryEndAtConstraint class

A `QueryEndAtConstraint` is used to exclude documents from the end of a result set returned by a Firestore query. `QueryEndAtConstraint`s are created by invoking [endAt()](https://firebase.google.com/docs/reference/js/firestore_.md#endat_9a4477f) or [endBefore()](https://firebase.google.com/docs/reference/js/firestore_.md#endbefore_9a4477f) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains this `QueryEndAtConstraint`.

**Signature:**  

    export declare class QueryEndAtConstraint extends QueryConstraint 

**Extends:** [QueryConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.queryconstraint.md#queryconstraint_class)

## Properties

|                                                       Property                                                        | Modifiers |          Type          |            Description            |
|-----------------------------------------------------------------------------------------------------------------------|-----------|------------------------|-----------------------------------|
| [type](https://firebase.google.com/docs/reference/js/firestore_lite.queryendatconstraint.md#queryendatconstrainttype) |           | 'endBefore' \| 'endAt' | The type of this query constraint |

## QueryEndAtConstraint.type

The type of this query constraint

**Signature:**  

    readonly type: 'endBefore' | 'endAt';