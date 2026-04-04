# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.impersonateauthenticated.md.txt

# ImpersonateAuthenticated interface

Interface representing the impersonation of an authenticated user.

**Signature:**  

    export interface ImpersonateAuthenticated 

## Properties

|                                                                                 Property                                                                                 |                                                     Type                                                      |                                                                                       Description                                                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [authClaims](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.impersonateauthenticated.md#impersonateauthenticatedauthclaims)           | [AuthClaims](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.md#authclaims) | Evaluate the auth policy with a customized JWT auth token. Should follow the Firebase Auth token format. https://firebase.google.com/docs/data-connect/cel-reference#auth-token-contents |
| [unauthenticated](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.impersonateauthenticated.md#impersonateauthenticatedunauthenticated) | never                                                                                                         | Both `authClaims` and `unauthenticated` are mutually exclusive fields and should not be both set.                                                                                        |

## ImpersonateAuthenticated.authClaims

Evaluate the auth policy with a customized JWT auth token. Should follow the Firebase Auth token format. https://firebase.google.com/docs/data-connect/cel-reference#auth-token-contents

**Signature:**  

    authClaims: AuthClaims;

### Example

A verified user may have the following `authClaims`:  

    { "sub": "uid", "email_verified": true }

## ImpersonateAuthenticated.unauthenticated

Both `authClaims` and `unauthenticated` are mutually exclusive fields and should not be both set.

**Signature:**  

    unauthenticated?: never;