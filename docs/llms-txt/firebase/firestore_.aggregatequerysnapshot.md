# Source: https://firebase.google.com/docs/reference/js/firestore_.aggregatequerysnapshot.md.txt

# AggregateQuerySnapshot class

The results of executing an aggregation query.

**Signature:**  

    export declare class AggregateQuerySnapshot<AggregateSpecType extends AggregateSpec, AppModelType = DocumentData, DbModelType extends DocumentData = DocumentData> 

## Properties

|                                                        Property                                                         | Modifiers |                                                        Type                                                         |                                                Description                                                 |
|-------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [query](https://firebase.google.com/docs/reference/js/firestore_.aggregatequerysnapshot.md#aggregatequerysnapshotquery) |           | [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class)\<AppModelType, DbModelType\> | The underlying query over which the aggregations recorded in this `AggregateQuerySnapshot` were performed. |
| [type](https://firebase.google.com/docs/reference/js/firestore_.aggregatequerysnapshot.md#aggregatequerysnapshottype)   |           | (not declared)                                                                                                      | A type string to uniquely identify instances of this class.                                                |

## Methods

|                                                         Method                                                          | Modifiers |                                                                                                                              Description                                                                                                                              |
|-------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [data()](https://firebase.google.com/docs/reference/js/firestore_.aggregatequerysnapshot.md#aggregatequerysnapshotdata) |           | Returns the results of the aggregations performed over the underlying query.The keys of the returned object will be the same as those of the `AggregateSpec` object specified to the aggregation method, and the values will be the corresponding aggregation result. |

## AggregateQuerySnapshot.query

The underlying query over which the aggregations recorded in this `AggregateQuerySnapshot` were performed.

**Signature:**  

    readonly query: Query<AppModelType, DbModelType>;

## AggregateQuerySnapshot.type

A type string to uniquely identify instances of this class.

**Signature:**  

    readonly type = "AggregateQuerySnapshot";

## AggregateQuerySnapshot.data()

Returns the results of the aggregations performed over the underlying query.

The keys of the returned object will be the same as those of the `AggregateSpec` object specified to the aggregation method, and the values will be the corresponding aggregation result.

**Signature:**  

    data(): AggregateSpecData<AggregateSpecType>;

**Returns:**

[AggregateSpecData](https://firebase.google.com/docs/reference/js/firestore_.md#aggregatespecdata)\<AggregateSpecType\>

The results of the aggregations performed over the underlying query.