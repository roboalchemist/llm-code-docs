# Source: https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.ordering.md.txt

# Ordering class

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Represents an ordering criterion for sorting documents in a Firestore pipeline.

You create `Ordering` instances using the `ascending` and `descending` helper functions.

**Signature:**

    export declare class Ordering 

## Constructors

| Constructor | Modifiers | Description |
|---|---|---|
| [(constructor)(expr, direction, _methodName)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.ordering.md#orderingconstructor) |   | ***(Public Preview)*** Constructs a new instance of the `Ordering` class |

## Properties

| Property | Modifiers | Type | Description |
|---|---|---|---|
| [direction](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.ordering.md#orderingdirection) |   | 'ascending' \| 'descending' | ***(Public Preview)*** |
| [expr](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.ordering.md#orderingexpr) |   | [Expression](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.expression.md#expression_class) | ***(Public Preview)*** |

## Ordering.(constructor)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Constructs a new instance of the `Ordering` class

**Signature:**

    constructor(expr: Expression, direction: 'ascending' | 'descending', _methodName: string | undefined);

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expr | [Expression](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.expression.md#expression_class) |   |
| direction | 'ascending' \| 'descending' |   |
| _methodName | string \| undefined |   |

## Ordering.direction

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    readonly direction: 'ascending' | 'descending';

## Ordering.expr

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    readonly expr: Expression;