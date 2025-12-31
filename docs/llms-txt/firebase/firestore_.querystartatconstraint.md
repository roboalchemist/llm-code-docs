# Source: https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md.txt

# QueryStartAtConstraint class

A `QueryStartAtConstraint` is used to exclude documents from the start of a result set returned by a Firestore query. `QueryStartAtConstraint`s are created by invoking [startAt()](https://firebase.google.com/docs/reference/js/firestore_.md#startat_9a4477f) or [startAfter()](https://firebase.google.com/docs/reference/js/firestore_.md#startafter_9a4477f) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains this `QueryStartAtConstraint`.

**Signature:**  

    export declare class QueryStartAtConstraint extends QueryConstraint 

**Extends:** [QueryConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryconstraint.md#queryconstraint_class)

## Properties

|                                                       Property                                                        | Modifiers |           Type            |            Description            |
|-----------------------------------------------------------------------------------------------------------------------|-----------|---------------------------|-----------------------------------|
| [type](https://firebase.google.com/docs/reference/js/firestore_.querystartatconstraint.md#querystartatconstrainttype) |           | 'startAt' \| 'startAfter' | The type of this query constraint |

## QueryStartAtConstraint.type

The type of this query constraint

**Signature:**  

    readonly type: 'startAt' | 'startAfter';