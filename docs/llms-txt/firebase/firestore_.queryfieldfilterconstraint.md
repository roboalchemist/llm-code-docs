# Source: https://firebase.google.com/docs/reference/js/firestore_.queryfieldfilterconstraint.md.txt

# QueryFieldFilterConstraint class

A `QueryFieldFilterConstraint` is used to narrow the set of documents returned by a Firestore query by filtering on one or more document fields. `QueryFieldFilterConstraint`s are created by invoking [where()](https://firebase.google.com/docs/reference/js/firestore_.md#where_0fae4bf) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains this `QueryFieldFilterConstraint`.

**Signature:**  

    export declare class QueryFieldFilterConstraint extends QueryConstraint 

**Extends:** [QueryConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryconstraint.md#queryconstraint_class)

## Properties

|                                                           Property                                                            | Modifiers |      Type      |            Description            |
|-------------------------------------------------------------------------------------------------------------------------------|-----------|----------------|-----------------------------------|
| [type](https://firebase.google.com/docs/reference/js/firestore_.queryfieldfilterconstraint.md#queryfieldfilterconstrainttype) |           | (not declared) | The type of this query constraint |

## QueryFieldFilterConstraint.type

The type of this query constraint

**Signature:**  

    readonly type = "where";