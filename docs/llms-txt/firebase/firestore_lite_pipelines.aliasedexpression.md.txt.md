# Source: https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.aliasedexpression.md.txt

# AliasedExpression class

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    export declare class AliasedExpression implements Selectable 

**Implements:** [Selectable](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.selectable.md#selectable_interface)

## Constructors

| Constructor | Modifiers | Description |
|---|---|---|
| [(constructor)(expr, alias, _methodName)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.aliasedexpression.md#aliasedexpressionconstructor) |   | ***(Public Preview)*** Constructs a new instance of the `AliasedExpression` class |

## Properties

| Property | Modifiers | Type | Description |
|---|---|---|---|
| [alias](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.aliasedexpression.md#aliasedexpressionalias) |   | string | ***(Public Preview)*** |
| [expr](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.aliasedexpression.md#aliasedexpressionexpr) |   | [Expression](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.expression.md#expression_class) | ***(Public Preview)*** |
| [exprType](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.aliasedexpression.md#aliasedexpressionexprtype) |   | [ExpressionType](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.md#expressiontype) | ***(Public Preview)*** |
| [selectable](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.aliasedexpression.md#aliasedexpressionselectable) |   | true | ***(Public Preview)*** |

## AliasedExpression.(constructor)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Constructs a new instance of the `AliasedExpression` class

**Signature:**

    constructor(expr: Expression, alias: string, _methodName: string | undefined);

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expr | [Expression](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.expression.md#expression_class) |   |
| alias | string |   |
| _methodName | string \| undefined |   |

## AliasedExpression.alias

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    readonly alias: string;

## AliasedExpression.expr

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    readonly expr: Expression;

## AliasedExpression.exprType

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    exprType: ExpressionType;

## AliasedExpression.selectable

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    selectable: true;