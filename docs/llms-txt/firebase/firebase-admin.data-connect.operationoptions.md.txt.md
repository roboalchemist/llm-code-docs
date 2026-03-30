# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.operationoptions.md.txt

# OperationOptions interface

Interface representing options for executing defined operations.

**Signature:**

    export interface OperationOptions 

## Properties

| Property | Type | Description |
|---|---|---|
| [impersonate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.operationoptions.md#operationoptionsimpersonate) | [ImpersonateAuthenticated](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.impersonateauthenticated.md#impersonateauthenticated_interface) \| [ImpersonateUnauthenticated](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.impersonateunauthenticated.md#impersonateunauthenticated_interface) | If set, impersonate a request with given Firebase Auth context and evaluate the auth policies on the operation. If omitted, bypass any defined auth policies. |

## OperationOptions.impersonate

If set, impersonate a request with given Firebase Auth context and evaluate the auth policies on the operation. If omitted, bypass any defined auth policies.

**Signature:**

    impersonate?: ImpersonateAuthenticated | ImpersonateUnauthenticated;