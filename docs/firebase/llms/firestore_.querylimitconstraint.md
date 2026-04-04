# Source: https://firebase.google.com/docs/reference/js/firestore_.querylimitconstraint.md.txt

# QueryLimitConstraint class

A `QueryLimitConstraint` is used to limit the number of documents returned by a Firestore query. `QueryLimitConstraint`s are created by invoking [limit()](https://firebase.google.com/docs/reference/js/firestore_.md#limit_ec46c78) or [limitToLast()](https://firebase.google.com/docs/reference/js/firestore_.md#limittolast_ec46c78) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains this `QueryLimitConstraint`.

**Signature:**  

    export declare class QueryLimitConstraint extends QueryConstraint 

**Extends:** [QueryConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryconstraint.md#queryconstraint_class)

## Properties

|                                                     Property                                                      | Modifiers |           Type           |            Description            |
|-------------------------------------------------------------------------------------------------------------------|-----------|--------------------------|-----------------------------------|
| [type](https://firebase.google.com/docs/reference/js/firestore_.querylimitconstraint.md#querylimitconstrainttype) |           | 'limit' \| 'limitToLast' | The type of this query constraint |

## QueryLimitConstraint.type

The type of this query constraint

**Signature:**  

    readonly type: 'limit' | 'limitToLast';