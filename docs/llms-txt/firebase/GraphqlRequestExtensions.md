# Source: https://firebase.google.com/docs/reference/data-connect/rest/v1beta/GraphqlRequestExtensions.md.txt

# GraphqlRequestExtensions contains additional information of `GraphqlRequest`.

|                                                                JSON representation                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "impersonate": { object (https://firebase.google.com/docs/reference/data-connect/rest/v1beta/GraphqlRequestExtensions#Impersonation) } } ``` |

|                                                                                                                                                             Fields                                                                                                                                                              ||
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `impersonate` | `object (`[Impersonation](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/GraphqlRequestExtensions#Impersonation)`)` Optional. If set, impersonate a request with given Firebase Auth context and evaluate the auth policies on the operation. If omitted, bypass any defined auth policies. |

## Impersonation

Impersonation configures the Firebase Auth context to impersonate.

|                                                                                JSON representation                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { // Union field `kind` can be only one of the following: "unauthenticated": boolean, "authClaims": { object } // End of list of possible types for union field `kind`. } ``` |

|                                                                                                                                                                                 Fields                                                                                                                                                                                  ||
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Union field `kind`. `kind` can be only one of the following:                                                                                                                                                                                                                                                                                                            ||
| `unauthenticated` | `boolean` Evaluate the auth policy as an unauthenticated request. Can only be set to true.                                                                                                                                                                                                                                                           |
| `authClaims`      | `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Evaluate the auth policy with a customized JWT auth token. Should follow the Firebase Auth token format. <https://firebase.google.com/docs/rules/rules-and-auth> For example: a verified user may have authClaims of {"sub": , "email_verified": true} |