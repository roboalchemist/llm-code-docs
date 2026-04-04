# Source: https://firebase.google.com/docs/reference/js/auth.phoneauthcredential.md.txt

# PhoneAuthCredential class

Represents the credentials returned by [PhoneAuthProvider](https://firebase.google.com/docs/reference/js/auth.phoneauthprovider.md#phoneauthprovider_class).

**Signature:**  

    export declare class PhoneAuthCredential extends AuthCredential 

**Extends:** [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class)

## Methods

|                                                         Method                                                          | Modifiers |                              Description                               |
|-------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------|
| [fromJSON(json)](https://firebase.google.com/docs/reference/js/auth.phoneauthcredential.md#phoneauthcredentialfromjson) | `static`  | Generates a phone credential based on a plain object or a JSON string. |
| [toJSON()](https://firebase.google.com/docs/reference/js/auth.phoneauthcredential.md#phoneauthcredentialtojson)         |           | Returns a JSON-serializable representation of this object.             |

## PhoneAuthCredential.fromJSON()

Generates a phone credential based on a plain object or a JSON string.

**Signature:**  

    static fromJSON(json: object | string): PhoneAuthCredential | null;

#### Parameters

| Parameter |       Type       | Description |
|-----------|------------------|-------------|
| json      | object \| string |             |

**Returns:**

[PhoneAuthCredential](https://firebase.google.com/docs/reference/js/auth.phoneauthcredential.md#phoneauthcredential_class) \| null

## PhoneAuthCredential.toJSON()

Returns a JSON-serializable representation of this object.

**Signature:**  

    toJSON(): object;

**Returns:**

object

a JSON-serializable representation of this object.