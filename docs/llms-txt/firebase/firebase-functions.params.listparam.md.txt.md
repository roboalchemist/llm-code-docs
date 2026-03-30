# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.listparam.md.txt

# params.ListParam class

A parametrized value of String\[\] type that will be read from .env files if present, or prompted for by the CLI if missing.

**Signature:**

    export declare class ListParam extends Param<string[]> 

**Extends:** [Param](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.param.md#paramsparam_class)\<string\[\]\>

## Properties

| Property | Modifiers | Type | Description |
|---|---|---|---|
| [type](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.listparam.md#paramslistparamtype) | `static` | ParamValueType |   |

## Methods

| Method | Modifiers | Description |
|---|---|---|
| [greaterThan(rhs)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.listparam.md#paramslistparamgreaterthan) |   |   |
| [greaterThanOrEqualTo(rhs)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.listparam.md#paramslistparamgreaterthanorequalto) |   |   |
| [lessThan(rhs)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.listparam.md#paramslistparamlessthan) |   |   |
| [lessThanorEqualTo(rhs)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.listparam.md#paramslistparamlessthanorequalto) |   |   |

## params.ListParam.type

**Signature:**

    static type: ParamValueType;

## params.ListParam.greaterThan()

**Signature:**

    greaterThan(rhs: string[] | Expression<string[]>): CompareExpression<string[]>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| rhs | string\[\] \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\[\]\> |   |

**Returns:**

CompareExpression\<string\[\]\>

## params.ListParam.greaterThanOrEqualTo()

**Signature:**

    greaterThanOrEqualTo(rhs: string[] | Expression<string[]>): CompareExpression<string[]>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| rhs | string\[\] \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\[\]\> |   |

**Returns:**

CompareExpression\<string\[\]\>

## params.ListParam.lessThan()

**Signature:**

    lessThan(rhs: string[] | Expression<string[]>): CompareExpression<string[]>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| rhs | string\[\] \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\[\]\> |   |

**Returns:**

CompareExpression\<string\[\]\>

## params.ListParam.lessThanorEqualTo()

**Signature:**

    lessThanorEqualTo(rhs: string[] | Expression<string[]>): CompareExpression<string[]>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| rhs | string\[\] \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\[\]\> |   |

**Returns:**

CompareExpression\<string\[\]\>