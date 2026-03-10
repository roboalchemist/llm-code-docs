# Source: https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.aliasedaggregate.md.txt

# AliasedAggregate class

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

An AggregateFunction with alias.

**Signature:**

    export declare class AliasedAggregate 

## Constructors

| Constructor | Modifiers | Description |
|---|---|---|
| [(constructor)(aggregate, alias, _methodName)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.aliasedaggregate.md#aliasedaggregateconstructor) |   | ***(Public Preview)*** Constructs a new instance of the `AliasedAggregate` class |

## Properties

| Property | Modifiers | Type | Description |
|---|---|---|---|
| [aggregate](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.aliasedaggregate.md#aliasedaggregateaggregate) |   | [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.aggregatefunction.md#aggregatefunction_class) | ***(Public Preview)*** |
| [alias](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.aliasedaggregate.md#aliasedaggregatealias) |   | string | ***(Public Preview)*** |

## AliasedAggregate.(constructor)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Constructs a new instance of the `AliasedAggregate` class

**Signature:**

    constructor(aggregate: AggregateFunction, alias: string, _methodName: string | undefined);

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| aggregate | [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.aggregatefunction.md#aggregatefunction_class) |   |
| alias | string |   |
| _methodName | string \| undefined |   |

## AliasedAggregate.aggregate

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    readonly aggregate: AggregateFunction;

## AliasedAggregate.alias

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    readonly alias: string;