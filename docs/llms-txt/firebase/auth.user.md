# Source: https://firebase.google.com/docs/reference/js/auth.user.md.txt

# User interface

A user account.

**Signature:**  

    export interface User extends UserInfo 

**Extends:** [UserInfo](https://firebase.google.com/docs/reference/js/auth.userinfo.md#userinfo_interface)

## Properties

|                                           Property                                            |                                                   Type                                                    |                                                                                                                           Description                                                                                                                           |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [emailVerified](https://firebase.google.com/docs/reference/js/auth.user.md#useremailverified) | boolean                                                                                                   | Whether the email has been verified with [sendEmailVerification()](https://firebase.google.com/docs/reference/js/auth.md#sendemailverification_6a885d6) and [applyActionCode()](https://firebase.google.com/docs/reference/js/auth.md#applyactioncode_d2ae15a). |
| [isAnonymous](https://firebase.google.com/docs/reference/js/auth.user.md#userisanonymous)     | boolean                                                                                                   | Whether the user is authenticated using the [ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).ANONYMOUS provider.                                                                                                                  |
| [metadata](https://firebase.google.com/docs/reference/js/auth.user.md#usermetadata)           | [UserMetadata](https://firebase.google.com/docs/reference/js/auth.usermetadata.md#usermetadata_interface) | Additional metadata around user creation and sign-in times.                                                                                                                                                                                                     |
| [providerData](https://firebase.google.com/docs/reference/js/auth.user.md#userproviderdata)   | [UserInfo](https://firebase.google.com/docs/reference/js/auth.userinfo.md#userinfo_interface)\[\]         | Additional per provider such as displayName and profile information.                                                                                                                                                                                            |
| [refreshToken](https://firebase.google.com/docs/reference/js/auth.user.md#userrefreshtoken)   | string                                                                                                    | Refresh token used to reauthenticate the user. Avoid using this directly and prefer [User.getIdToken()](https://firebase.google.com/docs/reference/js/auth.user.md#usergetidtoken) to refresh the ID token instead.                                             |
| [tenantId](https://firebase.google.com/docs/reference/js/auth.user.md#usertenantid)           | string \| null                                                                                            | The user's tenant ID.                                                                                                                                                                                                                                           |

## Methods

|                                                      Method                                                       |                                         Description                                          |
|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [delete()](https://firebase.google.com/docs/reference/js/auth.user.md#userdelete)                                 | Deletes and signs out the user.                                                              |
| [getIdToken(forceRefresh)](https://firebase.google.com/docs/reference/js/auth.user.md#usergetidtoken)             | Returns a JSON Web Token (JWT) used to identify the user to a Firebase service.              |
| [getIdTokenResult(forceRefresh)](https://firebase.google.com/docs/reference/js/auth.user.md#usergetidtokenresult) | Returns a deserialized JSON Web Token (JWT) used to identify the user to a Firebase service. |
| [reload()](https://firebase.google.com/docs/reference/js/auth.user.md#userreload)                                 | Refreshes the user, if signed in.                                                            |
| [toJSON()](https://firebase.google.com/docs/reference/js/auth.user.md#usertojson)                                 | Returns a JSON-serializable representation of this object.                                   |

## User.emailVerified

Whether the email has been verified with [sendEmailVerification()](https://firebase.google.com/docs/reference/js/auth.md#sendemailverification_6a885d6) and [applyActionCode()](https://firebase.google.com/docs/reference/js/auth.md#applyactioncode_d2ae15a).

**Signature:**  

    readonly emailVerified: boolean;

## User.isAnonymous

Whether the user is authenticated using the [ProviderId](https://firebase.google.com/docs/reference/js/auth.md#providerid).ANONYMOUS provider.

**Signature:**  

    readonly isAnonymous: boolean;

## User.metadata

Additional metadata around user creation and sign-in times.

**Signature:**  

    readonly metadata: UserMetadata;

## User.providerData

Additional per provider such as displayName and profile information.

**Signature:**  

    readonly providerData: UserInfo[];

## User.refreshToken

Refresh token used to reauthenticate the user. Avoid using this directly and prefer [User.getIdToken()](https://firebase.google.com/docs/reference/js/auth.user.md#usergetidtoken) to refresh the ID token instead.

**Signature:**  

    readonly refreshToken: string;

## User.tenantId

The user's tenant ID.

This is a read-only property, which indicates the tenant ID used to sign in the user. This is null if the user is signed in from the parent project.

**Signature:**  

    readonly tenantId: string | null;

### Example

    // Set the tenant ID on Auth instance.
    auth.tenantId = 'TENANT_PROJECT_ID';

    // All future sign-in request now include tenant ID.
    const result = await signInWithEmailAndPassword(auth, email, password);
    // result.user.tenantId should be 'TENANT_PROJECT_ID'.

## User.delete()

Deletes and signs out the user.
| **Important:** this is a security-sensitive operation that requires the user to have recently signed in. If this requirement isn't met, ask the user to authenticate again and then call one of the reauthentication methods like [reauthenticateWithCredential()](https://firebase.google.com/docs/reference/js/auth.md#reauthenticatewithcredential_60f8043).

This method is not supported on any [User](https://firebase.google.com/docs/reference/js/auth.user.md#user_interface) signed in by [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) instances created with a [FirebaseServerApp](https://firebase.google.com/docs/reference/js/app.firebaseserverapp.md#firebaseserverapp_interface).

**Signature:**  

    delete(): Promise<void>;

**Returns:**

Promise\<void\>

## User.getIdToken()

Returns a JSON Web Token (JWT) used to identify the user to a Firebase service.

Returns the current token if it has not expired or if it will not expire in the next five minutes. Otherwise, this will refresh the token and return a new one.

**Signature:**  

    getIdToken(forceRefresh?: boolean): Promise<string>;

#### Parameters

|  Parameter   |  Type   |                  Description                  |
|--------------|---------|-----------------------------------------------|
| forceRefresh | boolean | Force refresh regardless of token expiration. |

**Returns:**

Promise\<string\>

## User.getIdTokenResult()

Returns a deserialized JSON Web Token (JWT) used to identify the user to a Firebase service.

Returns the current token if it has not expired or if it will not expire in the next five minutes. Otherwise, this will refresh the token and return a new one.

**Signature:**  

    getIdTokenResult(forceRefresh?: boolean): Promise<IdTokenResult>;

#### Parameters

|  Parameter   |  Type   |                  Description                  |
|--------------|---------|-----------------------------------------------|
| forceRefresh | boolean | Force refresh regardless of token expiration. |

**Returns:**

Promise\<[IdTokenResult](https://firebase.google.com/docs/reference/js/auth.idtokenresult.md#idtokenresult_interface)\>

## User.reload()

Refreshes the user, if signed in.

**Signature:**  

    reload(): Promise<void>;

**Returns:**

Promise\<void\>

## User.toJSON()

Returns a JSON-serializable representation of this object.

**Signature:**  

    toJSON(): object;

**Returns:**

object

A JSON-serializable representation of this object.