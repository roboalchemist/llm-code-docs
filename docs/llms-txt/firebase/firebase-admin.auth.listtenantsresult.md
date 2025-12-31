# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.listtenantsresult.md.txt

# ListTenantsResult interface

Interface representing the object returned from a [TenantManager.listTenants()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenantmanager.md#tenantmanagerlisttenants) operation. Contains the list of tenants for the current batch and the next page token if available.

**Signature:**  

    export interface ListTenantsResult 

## Properties

|                                                                Property                                                                |                                                      Type                                                      |                                                                       Description                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [pageToken](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.listtenantsresult.md#listtenantsresultpagetoken) | string                                                                                                         | The next page token if available. This is needed for the next batch download.                                                                            |
| [tenants](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.listtenantsresult.md#listtenantsresulttenants)     | [Tenant](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenant.md#tenant_class)\[\] | The list of [Tenant](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenant.md#tenant_class) objects for the downloaded batch. |

## ListTenantsResult.pageToken

The next page token if available. This is needed for the next batch download.

**Signature:**  

    pageToken?: string;

## ListTenantsResult.tenants

The list of [Tenant](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenant.md#tenant_class) objects for the downloaded batch.

**Signature:**  

    tenants: Tenant[];