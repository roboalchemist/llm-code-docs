# Source: https://firebase.google.com/docs/reference/js/auth.authcredential.md.txt

# AuthCredential class

Interface that represents the credentials returned by an [AuthProvider](https://firebase.google.com/docs/reference/js/auth.authprovider.md#authprovider_interface).

Implementations specify the details about each auth provider's credential requirements.

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `AuthCredential` class.

**Signature:**  

    export declare class AuthCredential 

## Properties

|                                                    Property                                                     | Modifiers |  Type  |                      Description                      |
|-----------------------------------------------------------------------------------------------------------------|-----------|--------|-------------------------------------------------------|
| [providerId](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredentialproviderid)     |           | string | The authentication provider ID for the credential.    |
| [signInMethod](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredentialsigninmethod) |           | string | The authentication sign in method for the credential. |

## Methods

|                                                Method                                                 | Modifiers |                        Description                         |
|-------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------|
| [toJSON()](https://firebase.google.com/docs/reference/js/auth.authcredential.md#authcredentialtojson) |           | Returns a JSON-serializable representation of this object. |

## AuthCredential.providerId

The authentication provider ID for the credential.

For example, 'facebook.com', or 'google.com'.

**Signature:**  

    readonly providerId: string;

## AuthCredential.signInMethod

The authentication sign in method for the credential.

For example, [SignInMethod](https://firebase.google.com/docs/reference/js/auth.md#signinmethod).EMAIL_PASSWORD, or [SignInMethod](https://firebase.google.com/docs/reference/js/auth.md#signinmethod).EMAIL_LINK. This corresponds to the sign-in method identifier as returned in [fetchSignInMethodsForEmail()](https://firebase.google.com/docs/reference/js/auth.md#fetchsigninmethodsforemail_efb3887).

**Signature:**  

    readonly signInMethod: string;

## AuthCredential.toJSON()

Returns a JSON-serializable representation of this object.

**Signature:**  

    toJSON(): object;

**Returns:**

object

a JSON-serializable representation of this object.