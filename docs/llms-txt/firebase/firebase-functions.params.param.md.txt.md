# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.param.md.txt

# params.Param class

Represents a parametrized value that will be read from .env files if present, or prompted for by the CLI if missing. Instantiate these with the defineX methods exported by the firebase-functions/params namespace.

**Signature:**

    export declare abstract class Param<T extends string | number | boolean | string[]> extends Expression<T> 

**Extends:** [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<T\>

## Constructors

| Constructor | Modifiers | Description |
|---|---|---|
| [(constructor)(name, options)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.param.md#paramsparamconstructor) |   | Constructs a new instance of the `Param` class |

## Properties

| Property | Modifiers | Type | Description |
|---|---|---|---|
| [name](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.param.md#paramsparamname) |   | string |   |
| [options](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.param.md#paramsparamoptions) |   | [ParamOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md#paramsparamoptions)\<T\> |   |
| [type](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.param.md#paramsparamtype) | `static` | ParamValueType |   |

## Methods

| Method | Modifiers | Description |
|---|---|---|
| [cmp(cmp, rhs)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.param.md#paramsparamcmp) |   | Returns a parametrized expression of Boolean type, based on comparing the value of this parameter to a literal or a different expression. |
| [equals(rhs)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.param.md#paramsparamequals) |   | Returns a parametrized expression of Boolean type, based on comparing the value of this parameter to a literal or a different expression. |
| [greaterThan(rhs)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.param.md#paramsparamgreaterthan) |   | Returns a parametrized expression of Boolean type, based on comparing the value of this parameter to a literal or a different expression. |
| [greaterThanOrEqualTo(rhs)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.param.md#paramsparamgreaterthanorequalto) |   | Returns a parametrized expression of Boolean type, based on comparing the value of this parameter to a literal or a different expression. |
| [lessThan(rhs)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.param.md#paramsparamlessthan) |   | Returns a parametrized expression of Boolean type, based on comparing the value of this parameter to a literal or a different expression. |
| [lessThanorEqualTo(rhs)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.param.md#paramsparamlessthanorequalto) |   | Returns a parametrized expression of Boolean type, based on comparing the value of this parameter to a literal or a different expression. |
| [lessThanOrEqualTo(rhs)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.param.md#paramsparamlessthanorequalto) |   | Returns a parametrized expression of Boolean type, based on comparing the value of this parameter to a literal or a different expression. |
| [notEquals(rhs)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.param.md#paramsparamnotequals) |   | Returns a parametrized expression of Boolean type, based on comparing the value of this parameter to a literal or a different expression. |
| [toString()](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.param.md#paramsparamtostring) |   |   |

## params.Param.(constructor)

Constructs a new instance of the `Param` class

**Signature:**

    constructor(name: string, options?: ParamOptions<T>);

### Parameters

| Parameter | Type | Description |
|---|---|---|
| name | string |   |
| options | [ParamOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.md#paramsparamoptions)\<T\> |   |

## params.Param.name

**Signature:**

    readonly name: string;

## params.Param.options

**Signature:**

    readonly options: ParamOptions<T>;

## params.Param.type

**Signature:**

    static type: ParamValueType;

## params.Param.cmp()

Returns a parametrized expression of Boolean type, based on comparing the value of this parameter to a literal or a different expression.

**Signature:**

    cmp(cmp: "==" | "!=" | ">" | ">=" | "<" | "<=", rhs: T | Expression<T>): CompareExpression<T>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| cmp | "==" \| "!=" \| "\>" \| "\>=" \| "\<" \| "\<=" |   |
| rhs | T \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<T\> |   |

**Returns:**

CompareExpression\<T\>

## params.Param.equals()

Returns a parametrized expression of Boolean type, based on comparing the value of this parameter to a literal or a different expression.

**Signature:**

    equals(rhs: T | Expression<T>): CompareExpression<T>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| rhs | T \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<T\> |   |

**Returns:**

CompareExpression\<T\>

## params.Param.greaterThan()

Returns a parametrized expression of Boolean type, based on comparing the value of this parameter to a literal or a different expression.

**Signature:**

    greaterThan(rhs: T | Expression<T>): CompareExpression<T>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| rhs | T \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<T\> |   |

**Returns:**

CompareExpression\<T\>

## params.Param.greaterThanOrEqualTo()

Returns a parametrized expression of Boolean type, based on comparing the value of this parameter to a literal or a different expression.

**Signature:**

    greaterThanOrEqualTo(rhs: T | Expression<T>): CompareExpression<T>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| rhs | T \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<T\> |   |

**Returns:**

CompareExpression\<T\>

## params.Param.lessThan()

Returns a parametrized expression of Boolean type, based on comparing the value of this parameter to a literal or a different expression.

**Signature:**

    lessThan(rhs: T | Expression<T>): CompareExpression<T>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| rhs | T \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<T\> |   |

**Returns:**

CompareExpression\<T\>

## params.Param.lessThanorEqualTo()

> > [!WARNING]
> > **Warning:** This API is now obsolete.
>
> A typo. Use lessThanOrEqualTo instead.

Returns a parametrized expression of Boolean type, based on comparing the value of this parameter to a literal or a different expression.

**Signature:**

    lessThanorEqualTo(rhs: T | Expression<T>): CompareExpression<T>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| rhs | T \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<T\> |   |

**Returns:**

CompareExpression\<T\>

## params.Param.lessThanOrEqualTo()

Returns a parametrized expression of Boolean type, based on comparing the value of this parameter to a literal or a different expression.

**Signature:**

    lessThanOrEqualTo(rhs: T | Expression<T>): CompareExpression<T>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| rhs | T \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<T\> |   |

**Returns:**

CompareExpression\<T\>

## params.Param.notEquals()

Returns a parametrized expression of Boolean type, based on comparing the value of this parameter to a literal or a different expression.

**Signature:**

    notEquals(rhs: T | Expression<T>): CompareExpression<T>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| rhs | T \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<T\> |   |

**Returns:**

CompareExpression\<T\>

## params.Param.toString()

**Signature:**

    toString(): string;

**Returns:**

string