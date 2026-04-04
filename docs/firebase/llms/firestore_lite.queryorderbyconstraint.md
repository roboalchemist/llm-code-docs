# Source: https://firebase.google.com/docs/reference/js/firestore_lite.queryorderbyconstraint.md.txt

# QueryOrderByConstraint class

A `QueryOrderByConstraint` is used to sort the set of documents returned by a Firestore query. `QueryOrderByConstraint`s are created by invoking [orderBy()](https://firebase.google.com/docs/reference/js/firestore_.md#orderby_006d61f) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains this `QueryOrderByConstraint`.
| **Note:** Documents that do not contain the orderBy field will not be present in the query result.

**Signature:**  

    export declare class QueryOrderByConstraint extends QueryConstraint 

**Extends:** [QueryConstraint](https://firebase.google.com/docs/reference/js/firestore_lite.queryconstraint.md#queryconstraint_class)

## Properties

|                                                         Property                                                          | Modifiers |      Type      |            Description            |
|---------------------------------------------------------------------------------------------------------------------------|-----------|----------------|-----------------------------------|
| [type](https://firebase.google.com/docs/reference/js/firestore_lite.queryorderbyconstraint.md#queryorderbyconstrainttype) |           | (not declared) | The type of this query constraint |

## QueryOrderByConstraint.type

The type of this query constraint

**Signature:**  

    readonly type = "orderBy";