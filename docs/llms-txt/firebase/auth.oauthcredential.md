# Source: https://firebase.google.com/docs/reference/js/auth.oauthcredential.md.txt

# OAuthCredential class

Represents the OAuth credentials returned by an [OAuthProvider](https://firebase.google.com/docs/reference/js/auth.oauthprovider.md#oauthprovider_class).

Implementations specify the details about each auth provider's credential requirements.

**Signature:**  

    export declare class OAuthCredential extends AuthCredential 

**Extends:** [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class)

## Properties

|                                                    Property                                                     | Modifiers |  Type  |                                                                                                           Description                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------|-----------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [accessToken](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredentialaccesstoken) |           | string | The OAuth access token associated with the credential if it belongs to an [OAuthProvider](https://firebase.google.com/docs/reference/js/auth.oauthprovider.md#oauthprovider_class), such as `facebook.com`, `twitter.com`, etc. |
| [idToken](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredentialidtoken)         |           | string | The OAuth ID token associated with the credential if it belongs to an OIDC provider, such as `google.com`.                                                                                                                      |
| [secret](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredentialsecret)           |           | string | The OAuth access token secret associated with the credential if it belongs to an OAuth 1.0 provider, such as `twitter.com`.                                                                                                     |

## Methods

|                                                     Method                                                      | Modifiers |                                                                                     Description                                                                                      |
|-----------------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [fromJSON(json)](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredentialfromjson) | `static`  | Static method to deserialize a JSON representation of an object into an [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class). |
| [toJSON()](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredentialtojson)         |           | Returns a JSON-serializable representation of this object.                                                                                                                           |

## OAuthCredential.accessToken

The OAuth access token associated with the credential if it belongs to an [OAuthProvider](https://firebase.google.com/docs/reference/js/auth.oauthprovider.md#oauthprovider_class), such as `facebook.com`, `twitter.com`, etc.

**Signature:**  

    accessToken?: string;

## OAuthCredential.idToken

The OAuth ID token associated with the credential if it belongs to an OIDC provider, such as `google.com`.

**Signature:**  

    idToken?: string;

## OAuthCredential.secret

The OAuth access token secret associated with the credential if it belongs to an OAuth 1.0 provider, such as `twitter.com`.

**Signature:**  

    secret?: string;

## OAuthCredential.fromJSON()

Static method to deserialize a JSON representation of an object into an [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class).

**Signature:**  

    static fromJSON(json: string | object): OAuthCredential | null;

#### Parameters

| Parameter |       Type       |                                                              Description                                                               |
|-----------|------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| json      | string \| object | Input can be either Object or the stringified representation of the object. When string is provided, JSON.parse would be called first. |

**Returns:**

[OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) \| null

If the JSON input does not represent an [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class), null is returned.

## OAuthCredential.toJSON()

Returns a JSON-serializable representation of this object.

**Signature:**  

    toJSON(): object;

**Returns:**

object

a JSON-serializable representation of this object.