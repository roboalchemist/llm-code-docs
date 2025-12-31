# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.credential.md.txt

# Credential interface

Interface that provides Google OAuth2 access tokens used to authenticate with Firebase services.

In most cases, you will not need to implement this yourself and can instead use the default implementations provided by the `firebase-admin/app` module.

**Signature:**  

    export interface Credential 

## Methods

|                                                               Method                                                                |                                       Description                                        |
|-------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [getAccessToken()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.credential.md#credentialgetaccesstoken) | Returns a Google OAuth2 access token object used to authenticate with Firebase services. |

## Credential.getAccessToken()

Returns a Google OAuth2 access token object used to authenticate with Firebase services.

**Signature:**  

    getAccessToken(): Promise<GoogleOAuthAccessToken>;

**Returns:**

Promise\<[GoogleOAuthAccessToken](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.googleoauthaccesstoken.md#googleoauthaccesstoken_interface)\>

A Google OAuth2 access token object.