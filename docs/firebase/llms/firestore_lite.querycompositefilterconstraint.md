# Source: https://firebase.google.com/docs/reference/js/firestore_lite.querycompositefilterconstraint.md.txt

# QueryCompositeFilterConstraint class

A `QueryCompositeFilterConstraint` is used to narrow the set of documents returned by a Firestore query by performing the logical OR or AND of multiple [QueryFieldFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.queryfieldfilterconstraint.md#queryfieldfilterconstraint_class)s or [QueryCompositeFilterConstraint](https://firebase.google.com/docs/reference/js/firestore_.querycompositefilterconstraint.md#querycompositefilterconstraint_class)s. `QueryCompositeFilterConstraint`s are created by invoking [or()](https://firebase.google.com/docs/reference/js/firestore_.md#or_e72c712) or [and()](https://firebase.google.com/docs/reference/js/firestore_.md#and_e72c712) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4) to create a new query instance that also contains the `QueryCompositeFilterConstraint`.

**Signature:**  

    export declare class QueryCompositeFilterConstraint 

## Properties

|                                                                 Property                                                                  | Modifiers |     Type      |            Description            |
|-------------------------------------------------------------------------------------------------------------------------------------------|-----------|---------------|-----------------------------------|
| [type](https://firebase.google.com/docs/reference/js/firestore_lite.querycompositefilterconstraint.md#querycompositefilterconstrainttype) |           | 'or' \| 'and' | The type of this query constraint |

## QueryCompositeFilterConstraint.type

The type of this query constraint

**Signature:**  

    readonly type: 'or' | 'and';