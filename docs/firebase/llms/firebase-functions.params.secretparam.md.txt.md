# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.secretparam.md.txt

# params.SecretParam class

A parametrized string whose value is stored in Cloud Secret Manager instead of the local filesystem. Supply instances of SecretParams to the secrets array while defining a Function to make their values accessible during execution of that Function.

**Signature:**

    export declare class SecretParam 

## Constructors

| Constructor | Modifiers | Description |
|---|---|---|
| [(constructor)(name)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.secretparam.md#paramssecretparamconstructor) |   | Constructs a new instance of the `SecretParam` class |

## Properties

| Property | Modifiers | Type | Description |
|---|---|---|---|
| [name](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.secretparam.md#paramssecretparamname) |   | string |   |
| [type](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.secretparam.md#paramssecretparamtype) | `static` | ParamValueType |   |

## Methods

| Method | Modifiers | Description |
|---|---|---|
| [value()](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.secretparam.md#paramssecretparamvalue) |   | Returns the secret's value at runtime. Throws an error if accessed during deployment. |

## params.SecretParam.(constructor)

Constructs a new instance of the `SecretParam` class

**Signature:**

    constructor(name: string);

### Parameters

| Parameter | Type | Description |
|---|---|---|
| name | string |   |

## params.SecretParam.name

**Signature:**

    name: string;

## params.SecretParam.type

**Signature:**

    static type: ParamValueType;

## params.SecretParam.value()

Returns the secret's value at runtime. Throws an error if accessed during deployment.

**Signature:**

    value(): string;

**Returns:**

string