# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.jsonsecretparam.md.txt

# params.JsonSecretParam class

A parametrized object whose value is stored as a JSON string in Cloud Secret Manager. This is useful for managing groups of related configuration values, such as all settings for a third-party API, as a single unit. Supply instances of JsonSecretParam to the secrets array while defining a Function to make their values accessible during execution of that Function.

**Signature:**

    export declare class JsonSecretParam<T = any> 

## Constructors

| Constructor | Modifiers | Description |
|---|---|---|
| [(constructor)(name)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.jsonsecretparam.md#paramsjsonsecretparamconstructor) |   | Constructs a new instance of the `JsonSecretParam` class |

## Properties

| Property | Modifiers | Type | Description |
|---|---|---|---|
| [name](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.jsonsecretparam.md#paramsjsonsecretparamname) |   | string |   |
| [type](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.jsonsecretparam.md#paramsjsonsecretparamtype) | `static` | ParamValueType |   |

## Methods

| Method | Modifiers | Description |
|---|---|---|
| [value()](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.jsonsecretparam.md#paramsjsonsecretparamvalue) |   | Returns the secret's parsed JSON value at runtime. Throws an error if accessed during deployment, if the secret is not set, or if the value is not valid JSON. |

## params.JsonSecretParam.(constructor)

Constructs a new instance of the `JsonSecretParam` class

**Signature:**

    constructor(name: string);

### Parameters

| Parameter | Type | Description |
|---|---|---|
| name | string |   |

## params.JsonSecretParam.name

**Signature:**

    name: string;

## params.JsonSecretParam.type

**Signature:**

    static type: ParamValueType;

## params.JsonSecretParam.value()

Returns the secret's parsed JSON value at runtime. Throws an error if accessed during deployment, if the secret is not set, or if the value is not valid JSON.

**Signature:**

    value(): T;

**Returns:**

T