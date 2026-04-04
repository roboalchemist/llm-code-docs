# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.graphqloptions.md.txt

Interface representing GraphQL options for executing arbitrary GraphQL operations.

**Signature:**  

    export interface GraphqlOptions<Variables> 

## Properties

|                                                                     Property                                                                     |                                                                                                                                                                               Type                                                                                                                                                                               |                                                                          Description                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [impersonate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.graphqloptions.md#graphqloptionsimpersonate)     | [ImpersonateAuthenticated](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.impersonateauthenticated.md#impersonateauthenticated_interface)\|[ImpersonateUnauthenticated](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.impersonateunauthenticated.md#impersonateunauthenticated_interface) | If set, impersonate a request with given Firebase Auth context and evaluate the auth policies on the operation. If omitted, bypass any defined auth policies. |
| [operationName](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.graphqloptions.md#graphqloptionsoperationname) | string                                                                                                                                                                                                                                                                                                                                                           | The name of the GraphQL operation. Required for operations that interact with services, such as executeGraphql, if`query`contains multiple operations.        |
| [variables](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.graphqloptions.md#graphqloptionsvariables)         | Variables                                                                                                                                                                                                                                                                                                                                                        | Values for GraphQL variables provided in this query or mutation.                                                                                              |

## GraphqlOptions.impersonate

If set, impersonate a request with given Firebase Auth context and evaluate the auth policies on the operation. If omitted, bypass any defined auth policies.

**Signature:**  

    impersonate?: ImpersonateAuthenticated | ImpersonateUnauthenticated;

## GraphqlOptions.operationName

The name of the GraphQL operation. Required for operations that interact with services, such as executeGraphql, if`query`contains multiple operations.

**Signature:**  

    operationName?: string;

## GraphqlOptions.variables

Values for GraphQL variables provided in this query or mutation.

**Signature:**  

    variables?: Variables;