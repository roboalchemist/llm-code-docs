# Source: https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.booleanexpression.md.txt

# BooleanExpression class

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

An interface that represents a filter condition.

**Signature:**

    export declare abstract class BooleanExpression extends Expression 

**Extends:** [Expression](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.expression.md#expression_class)

## Methods

| Method | Modifiers | Description |
|---|---|---|
| [conditional(thenExpr, elseExpr)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.booleanexpression.md#booleanexpressionconditional) |   | ***(Public Preview)*** Creates a conditional expression that evaluates to the 'then' expression if `this` expression evaluates to `true`, or evaluates to the 'else' expression if `this` expressions evaluates `false`. |
| [countIf()](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.booleanexpression.md#booleanexpressioncountif) |   | ***(Public Preview)*** Creates an aggregation that finds the count of input documents satisfying this boolean expression. |
| [ifError(catchValue)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.booleanexpression.md#booleanexpressioniferror) |   | ***(Public Preview)*** Creates an expression that returns the `catch` argument if there is an error, else return the result of this expression. |
| [ifError(catchValue)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.booleanexpression.md#booleanexpressioniferror) |   | ***(Public Preview)*** Creates an expression that returns the `catch` argument if there is an error, else return the result of this expression. |
| [ifError(catchValue)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.booleanexpression.md#booleanexpressioniferror) |   | ***(Public Preview)*** Creates an expression that returns the `catch` argument if there is an error, else return the result of this expression. |
| [ifError(catchValue)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.booleanexpression.md#booleanexpressioniferror) |   | ***(Public Preview)*** Creates an expression that returns the `catch` argument if there is an error, else return the result of this expression. |
| [not()](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.booleanexpression.md#booleanexpressionnot) |   | ***(Public Preview)*** Creates an expression that negates this boolean expression. |

## BooleanExpression.conditional()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates a conditional expression that evaluates to the 'then' expression if `this` expression evaluates to `true`, or evaluates to the 'else' expression if `this` expressions evaluates `false`.

**Signature:**

    conditional(thenExpr: Expression, elseExpr: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| thenExpr | [Expression](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.expression.md#expression_class) | The expression to evaluate if the condition is true. |
| elseExpr | [Expression](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.expression.md#expression_class) | The expression to evaluate if the condition is false. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the conditional expression.

### Example

    // If 'age' is greater than 18, return "Adult"; otherwise, return "Minor".
    field("age").greaterThanOrEqual(18).conditional(constant("Adult"), constant("Minor"));

## BooleanExpression.countIf()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that finds the count of input documents satisfying this boolean expression.

**Signature:**

    countIf(): AggregateFunction;

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.aggregatefunction.md#aggregatefunction_class)

A new `AggregateFunction` representing the 'countIf' aggregation.

### Example

    // Find the count of documents with a score greater than 90
    field("score").greaterThan(90).countIf().as("highestScore");

## BooleanExpression.ifError()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the `catch` argument if there is an error, else return the result of this expression.

**Signature:**

    ifError(catchValue: BooleanExpression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| catchValue | [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.booleanexpression.md#booleanexpression_class) | The value that will be returned if this expression produces an error. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'ifError' operation.

### Example

    // Create an expression that protects against a divide by zero error
    // but always returns a boolean expression.
    constant(50).divide('length').gt(1).ifError(constant(false));

## BooleanExpression.ifError()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the `catch` argument if there is an error, else return the result of this expression.

**Signature:**

    ifError(catchValue: boolean): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| catchValue | boolean | The value that will be returned if this expression produces an error. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'ifError' operation.

### Example

    // Create an expression that protects against a divide by zero error
    // but always returns a boolean expression.
    constant(50).divide('length').gt(1).ifError(false);

## BooleanExpression.ifError()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the `catch` argument if there is an error, else return the result of this expression.

**Signature:**

    ifError(catchValue: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| catchValue | [Expression](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.expression.md#expression_class) | The value that will be returned if this expression produces an error. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'ifError' operation.

### Example

    // Create an expression that protects against a divide by zero error.
    constant(50).divide('length').gt(1).ifError(constant(0));

## BooleanExpression.ifError()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the `catch` argument if there is an error, else return the result of this expression.

**Signature:**

    ifError(catchValue: unknown): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| catchValue | unknown | The value that will be returned if this expression produces an error. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'ifError' operation.

### Example

    // Create an expression that protects against a divide by zero error.
    constant(50).divide('length').gt(1).ifError(0);

## BooleanExpression.not()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that negates this boolean expression.

**Signature:**

    not(): BooleanExpression;

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the negated filter condition.

### Example

    // Find documents where the 'tags' field does not contain 'completed'
    field("tags").arrayContains("completed").not();