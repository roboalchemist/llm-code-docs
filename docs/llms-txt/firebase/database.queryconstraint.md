# Source: https://firebase.google.com/docs/reference/js/database.queryconstraint.md.txt

# QueryConstraint class

A `QueryConstraint` is used to narrow the set of documents returned by a Database query. `QueryConstraint`s are created by invoking [endAt()](https://firebase.google.com/docs/reference/js/database.md#endat_51c2c8b), [endBefore()](https://firebase.google.com/docs/reference/js/database.md#endbefore_51c2c8b), [startAt()](https://firebase.google.com/docs/reference/js/database.md#startat_51c2c8b), [startAfter()](https://firebase.google.com/docs/reference/js/database.md#startafter_51c2c8b), [limitToFirst()](https://firebase.google.com/docs/reference/js/database.md#limittofirst_ec46c78), [limitToLast()](https://firebase.google.com/docs/reference/js/database.md#limittolast_ec46c78), [orderByChild()](https://firebase.google.com/docs/reference/js/database.md#orderbychild_fe1f8e4), [orderByChild()](https://firebase.google.com/docs/reference/js/database.md#orderbychild_fe1f8e4), [orderByKey()](https://firebase.google.com/docs/reference/js/database.md#orderbykey) , [orderByPriority()](https://firebase.google.com/docs/reference/js/database.md#orderbypriority) , [orderByValue()](https://firebase.google.com/docs/reference/js/database.md#orderbyvalue) or [equalTo()](https://firebase.google.com/docs/reference/js/database.md#equalto_51c2c8b) and can then be passed to [query()](https://firebase.google.com/docs/reference/js/database.md#query_870e07a) to create a new query instance that also contains this `QueryConstraint`.

**Signature:**  

    export declare abstract class QueryConstraint 

## Properties

|                                               Property                                                | Modifiers |                                                 Type                                                 |            Description             |
|-------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------------------------|------------------------------------|
| [type](https://firebase.google.com/docs/reference/js/database.queryconstraint.md#queryconstrainttype) |           | [QueryConstraintType](https://firebase.google.com/docs/reference/js/database.md#queryconstrainttype) | The type of this query constraints |

## QueryConstraint.type

The type of this query constraints

**Signature:**  

    abstract readonly type: QueryConstraintType;