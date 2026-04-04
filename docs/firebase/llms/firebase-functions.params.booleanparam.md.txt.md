# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.booleanparam.md.txt

# params.BooleanParam class

A parametrized value of Boolean type that will be read from .env files if present, or prompted for by the CLI if missing.

**Signature:**

    export declare class BooleanParam extends Param<boolean> 

**Extends:** [Param](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.param.md#paramsparam_class)\<boolean\>

## Properties

| Property | Modifiers | Type | Description |
|---|---|---|---|
| [type](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.booleanparam.md#paramsbooleanparamtype) | `static` | ParamValueType |   |

## Methods

| Method | Modifiers | Description |
|---|---|---|
| [then(ifTrue, ifFalse)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.booleanparam.md#paramsbooleanparamthen) |   |   |
| [thenElse(ifTrue, ifFalse)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.booleanparam.md#paramsbooleanparamthenelse) |   |   |

## params.BooleanParam.type

**Signature:**

    static type: ParamValueType;

## params.BooleanParam.then()

> > [!WARNING]
> > **Warning:** This API is now obsolete.
>
**Signature:**

    then<T extends string | number | boolean>(ifTrue: T | Expression<T>, ifFalse: T | Expression<T>): TernaryExpression<T>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| ifTrue | T \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<T\> |   |
| ifFalse | T \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<T\> |   |

**Returns:**

TernaryExpression\<T\>

## params.BooleanParam.thenElse()

**Signature:**

    thenElse<T extends string | number | boolean>(ifTrue: T | Expression<T>, ifFalse: T | Expression<T>): TernaryExpression<T>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| ifTrue | T \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<T\> |   |
| ifFalse | T \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<T\> |   |

**Returns:**

TernaryExpression\<T\>