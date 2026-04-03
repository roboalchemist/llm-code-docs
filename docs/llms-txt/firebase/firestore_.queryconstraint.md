# Source: https://firebase.google.com/docs/reference/js/firestore_.queryconstraint.md.txt

# QueryConstraint class

A `QueryConstraint` is used to narrow the set of documents returned by a Firestore query. `QueryConstraint`s are created by invoking [where()](https://firebase.google.com/docs/reference/js/firestore_.md#where_0fae4bf), [orderBy()](https://firebase.google.com/docs/reference/js/firestore_.md#orderby_006d61f), [startAt()](https://firebase.google.com/docs/reference/js/firestore_.md#startat_9a4477f), [startAfter()](https://firebase.google.com/docs/reference/js/firestore_.md#startafter_9a4477f), [endBefore()](https://firebase.google.com/docs/reference/js/firestore_.md#endbefore_9a4477f), [endAt()](https://firebase.google.com/docs/reference/js/firestore_.md#endat_9a4477f), [limit()](https://firebase.google.com/docs/reference/js/firestore_.md#limit_ec46c78), [limitToLast()](https://firebase.google.com/docs/reference/js/firestore_.md#limittolast_ec46c78) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains this `QueryConstraint`.

**Signature:**  

    export declare abstract class QueryConstraint 

## Properties

|                                                Property                                                 | Modifiers |                                                  Type                                                  |            Description            |
|---------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------------------------|-----------------------------------|
| [type](https://firebase.google.com/docs/reference/js/firestore_.queryconstraint.md#queryconstrainttype) |           | [QueryConstraintType](https://firebase.google.com/docs/reference/js/firestore_.md#queryconstrainttype) | The type of this query constraint |

## QueryConstraint.type

The type of this query constraint

**Signature:**  

    abstract readonly type: QueryConstraintType;