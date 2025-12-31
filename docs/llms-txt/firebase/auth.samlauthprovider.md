# Source: https://firebase.google.com/docs/reference/js/auth.samlauthprovider.md.txt

# SAMLAuthProvider class

An [AuthProvider](https://firebase.google.com/docs/reference/js/auth.authprovider.md#authprovider_interface) for SAML.

**Signature:**  

    export declare class SAMLAuthProvider extends FederatedAuthProvider 

**Extends:** FederatedAuthProvider

## Constructors

|                                                           Constructor                                                           | Modifiers |                     Description                     |
|---------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------|
| [(constructor)(providerId)](https://firebase.google.com/docs/reference/js/auth.samlauthprovider.md#samlauthproviderconstructor) |           | Constructor. The providerId must start with "saml." |

## Methods

|                                                                       Method                                                                        | Modifiers |                                                                                                                                                         Description                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [credentialFromError(error)](https://firebase.google.com/docs/reference/js/auth.samlauthprovider.md#samlauthprovidercredentialfromerror)            | `static`  | Used to extract the underlying [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) from a [AuthError](https://firebase.google.com/docs/reference/js/auth.autherror.md#autherror_interface) which was thrown during a sign-in, link, or reauthenticate operation. |
| [credentialFromJSON(json)](https://firebase.google.com/docs/reference/js/auth.samlauthprovider.md#samlauthprovidercredentialfromjson)               | `static`  | Creates an [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class) from a JSON string or a plain object.                                                                                                                                                                |
| [credentialFromResult(userCredential)](https://firebase.google.com/docs/reference/js/auth.samlauthprovider.md#samlauthprovidercredentialfromresult) | `static`  | Generates an [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class) from a [UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface) after a successful SAML flow completes.                                     |

## SAMLAuthProvider.(constructor)

Constructor. The providerId must start with "saml."

**Signature:**  

    constructor(providerId: string);

#### Parameters

| Parameter  |  Type  |    Description    |
|------------|--------|-------------------|
| providerId | string | SAML provider ID. |

## SAMLAuthProvider.credentialFromError()

Used to extract the underlying [OAuthCredential](https://firebase.google.com/docs/reference/js/auth.oauthcredential.md#oauthcredential_class) from a [AuthError](https://firebase.google.com/docs/reference/js/auth.autherror.md#autherror_interface) which was thrown during a sign-in, link, or reauthenticate operation.

**Signature:**  

    static credentialFromError(error: FirebaseError): AuthCredential | null;

#### Parameters

| Parameter |                                                   Type                                                   | Description |
|-----------|----------------------------------------------------------------------------------------------------------|-------------|
| error     | [FirebaseError](https://firebase.google.com/docs/reference/js/util.firebaseerror.md#firebaseerror_class) |             |

**Returns:**

[AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class) \| null

## SAMLAuthProvider.credentialFromJSON()

Creates an [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class) from a JSON string or a plain object.

**Signature:**  

    static credentialFromJSON(json: string | object): AuthCredential;

#### Parameters

| Parameter |       Type       |           Description           |
|-----------|------------------|---------------------------------|
| json      | string \| object | A plain object or a JSON string |

**Returns:**

[AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class)

## SAMLAuthProvider.credentialFromResult()

Generates an [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class) from a [UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface) after a successful SAML flow completes.

For example, to get an [AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class), you could write the following code:  

    const userCredential = await signInWithPopup(auth, samlProvider);
    const credential = SAMLAuthProvider.credentialFromResult(userCredential);

**Signature:**  

    static credentialFromResult(userCredential: UserCredential): AuthCredential | null;

#### Parameters

|   Parameter    |                                                      Type                                                       |     Description      |
|----------------|-----------------------------------------------------------------------------------------------------------------|----------------------|
| userCredential | [UserCredential](https://firebase.google.com/docs/reference/js/auth.usercredential.md#usercredential_interface) | The user credential. |

**Returns:**

[AuthCredential](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredential_class) \| null