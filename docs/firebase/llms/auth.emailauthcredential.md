# Source: https://firebase.google.com/docs/reference/js/auth.emailauthcredential.md.txt

# EmailAuthCredential class

Interface that represents the credentials returned by [EmailAuthProvider](https://firebase.google.com/docs/reference/js/auth.emailauthprovider.md#emailauthprovider_class) for [ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).PASSWORD

Covers both [SignInMethod](https://firebase.google.com/docs/reference/js/auth.md#signinmethod).EMAIL_PASSWORD and [SignInMethod](https://firebase.google.com/docs/reference/js/auth.md#signinmethod).EMAIL_LINK.

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `EmailAuthCredential` class.

**Signature:**  

    export declare class EmailAuthCredential extends AuthCredential 

**Extends:** [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class)

## Methods

|                                                         Method                                                          | Modifiers |                                                                                     Description                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [fromJSON(json)](https://firebase.google.com/docs/reference/js/auth.emailauthcredential.md#emailauthcredentialfromjson) | `static`  | Static method to deserialize a JSON representation of an object into an [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class). |
| [toJSON()](https://firebase.google.com/docs/reference/js/auth.emailauthcredential.md#emailauthcredentialtojson)         |           | Returns a JSON-serializable representation of this object.                                                                                                                           |

## EmailAuthCredential.fromJSON()

Static method to deserialize a JSON representation of an object into an [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class).

**Signature:**  

    static fromJSON(json: object | string): EmailAuthCredential | null;

#### Parameters

| Parameter |       Type       |                                                          Description                                                          |
|-----------|------------------|-------------------------------------------------------------------------------------------------------------------------------|
| json      | object \| string | Either `object` or the stringified representation of the object. When string is provided, `JSON.parse` would be called first. |

**Returns:**

[EmailAuthCredential](https://firebase.google.com/docs/reference/js/auth.emailauthcredential.md#emailauthcredential_class) \| null

If the JSON input does not represent an [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class), null is returned.

## EmailAuthCredential.toJSON()

Returns a JSON-serializable representation of this object.

**Signature:**  

    toJSON(): object;

**Returns:**

object

a JSON-serializable representation of this object.