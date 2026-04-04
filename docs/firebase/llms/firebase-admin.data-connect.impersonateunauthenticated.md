# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.impersonateunauthenticated.md.txt

# ImpersonateUnauthenticated interface

Interface representing the impersonation of an unauthenticated user.

**Signature:**  

    export interface ImpersonateUnauthenticated 

## Properties

|                                                                                   Property                                                                                   | Type  |                                            Description                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|---------------------------------------------------------------------------------------------------|
| [authClaims](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.impersonateunauthenticated.md#impersonateunauthenticatedauthclaims)           | never | Both `authClaims` and `unauthenticated` are mutually exclusive fields and should not be both set. |
| [unauthenticated](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.impersonateunauthenticated.md#impersonateunauthenticatedunauthenticated) | true  | Evaluates the auth policy as an unauthenticated request. Can only be set to true.                 |

## ImpersonateUnauthenticated.authClaims

Both `authClaims` and `unauthenticated` are mutually exclusive fields and should not be both set.

**Signature:**  

    authClaims?: never;

## ImpersonateUnauthenticated.unauthenticated

Evaluates the auth policy as an unauthenticated request. Can only be set to true.

**Signature:**  

    unauthenticated: true;