# Source: https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.aggregatefunction.md.txt

# AggregateFunction class

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

A class that represents an aggregate function.

**Signature:**

    export declare class AggregateFunction 

## Constructors

| Constructor | Modifiers | Description |
|---|---|---|
| [(constructor)(name, params)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.aggregatefunction.md#aggregatefunctionconstructor) |   | ***(Public Preview)*** Constructs a new instance of the `AggregateFunction` class |

## Properties

| Property | Modifiers | Type | Description |
|---|---|---|---|
| [exprType](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.aggregatefunction.md#aggregatefunctionexprtype) |   | [ExpressionType](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.md#expressiontype) | ***(Public Preview)*** |

## Methods

| Method | Modifiers | Description |
|---|---|---|
| [as(name)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.aggregatefunction.md#aggregatefunctionas) |   | ***(Public Preview)*** Assigns an alias to this AggregateFunction. The alias specifies the name that the aggregated value will have in the output document. |

## AggregateFunction.(constructor)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Constructs a new instance of the `AggregateFunction` class

**Signature:**

    constructor(name: string, params: Expression[]);

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| name | string |   |
| params | [Expression](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.expression.md#expression_class)\[\] |   |

## AggregateFunction.exprType

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    exprType: ExpressionType;

## AggregateFunction.as()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Assigns an alias to this AggregateFunction. The alias specifies the name that the aggregated value will have in the output document.

**Signature:**

    as(name: string): AliasedAggregate;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| name | string | The alias to assign to this AggregateFunction. |

**Returns:**

[AliasedAggregate](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.aliasedaggregate.md#aliasedaggregate_class)

A new [AliasedAggregate](https://firebase.google.com/docs/reference/js/firestore_pipelines.aliasedaggregate.md#aliasedaggregate_class) that wraps this AggregateFunction and associates it with the provided alias.

### Example

    // Calculate the average price of all items and assign it the alias "averagePrice".
    firestore.pipeline().collection("items")
      .aggregate(field("price").average().as("averagePrice"));