# Source: https://firebase.google.com/docs/reference/js/firestore_lite.aggregatefield.md.txt

# AggregateField class

Represents an aggregation that can be performed by Firestore.

**Signature:**  

    export declare class AggregateField<T> 

## Properties

|                                                          Property                                                           | Modifiers |                                              Type                                              |                         Description                         |
|-----------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| [aggregateType](https://firebase.google.com/docs/reference/js/firestore_lite.aggregatefield.md#aggregatefieldaggregatetype) |           | [AggregateType](https://firebase.google.com/docs/reference/js/firestore_lite.md#aggregatetype) | Indicates the aggregation operation of this AggregateField. |
| [type](https://firebase.google.com/docs/reference/js/firestore_lite.aggregatefield.md#aggregatefieldtype)                   |           | (not declared)                                                                                 | A type string to uniquely identify instances of this class. |

## AggregateField.aggregateType

Indicates the aggregation operation of this AggregateField.

**Signature:**  

    readonly aggregateType: AggregateType;

## AggregateField.type

A type string to uniquely identify instances of this class.

**Signature:**  

    readonly type = "AggregateField";