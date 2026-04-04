# Source: https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md.txt

# FunctionExpression class

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

This class defines the base class for Firestore [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) functions, which can be evaluated within pipeline execution.

Typically, you would not use this class or its children directly. Use either the functions like [and()](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#and_e0c48bd), [equal()](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#equal_b3c3382), or the methods on [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) ([Expression.equal()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionequal), [Expression.lessThan()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionlessthan), etc.) to construct new Function instances.

**Signature:**

    export declare class FunctionExpression extends Expression 

**Extends:** [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)

## Constructors

| Constructor | Modifiers | Description |
|---|---|---|
| [(constructor)(name, params)](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpressionconstructor) |   | ***(Public Preview)*** Constructs a new instance of the `FunctionExpression` class |
| [(constructor)(name, params, _methodName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpressionconstructor) |   | ***(Public Preview)*** Constructs a new instance of the `FunctionExpression` class |

## Properties

| Property | Modifiers | Type | Description |
|---|---|---|---|
| [expressionType](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpressionexpressiontype) |   | [ExpressionType](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#expressiontype) | ***(Public Preview)*** |

## FunctionExpression.(constructor)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Constructs a new instance of the `FunctionExpression` class

**Signature:**

    constructor(name: string, params: Expression[]);

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| name | string |   |
| params | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)\[\] |   |

## FunctionExpression.(constructor)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Constructs a new instance of the `FunctionExpression` class

**Signature:**

    constructor(name: string, params: Expression[], _methodName: string | undefined);

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| name | string |   |
| params | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)\[\] |   |
| _methodName | string \| undefined |   |

## FunctionExpression.expressionType

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    readonly expressionType: ExpressionType;