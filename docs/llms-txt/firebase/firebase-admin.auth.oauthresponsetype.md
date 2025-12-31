# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.oauthresponsetype.md.txt

# OAuthResponseType interface

The interface representing OIDC provider's response object for OAuth authorization flow. One of the following settings is required:

- Set `code` to `true` for the code flow.
- Set `idToken` to `true` for the ID token flow.

<br />

**Signature:**  

    export interface OAuthResponseType 

## Properties

|                                                              Property                                                              |  Type   |                                Description                                |
|------------------------------------------------------------------------------------------------------------------------------------|---------|---------------------------------------------------------------------------|
| [code](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.oauthresponsetype.md#oauthresponsetypecode)       | boolean | Whether authorization code is returned from IdP's authorization endpoint. |
| [idToken](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.oauthresponsetype.md#oauthresponsetypeidtoken) | boolean | Whether ID token is returned from IdP's authorization endpoint.           |

## OAuthResponseType.code

Whether authorization code is returned from IdP's authorization endpoint.

**Signature:**  

    code?: boolean;

## OAuthResponseType.idToken

Whether ID token is returned from IdP's authorization endpoint.

**Signature:**  

    idToken?: boolean;