# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenantmanager.md.txt

# TenantManager class

Defines the tenant manager used to help manage tenant related operations. This includes:

- The ability to create, update, list, get and delete tenants for the underlying project.
- Getting a `TenantAwareAuth` instance for running Auth related operations (user management, provider configuration management, token verification, email link generation, etc) in the context of a specified tenant.

<br />

**Signature:**  

    export declare class TenantManager 

## Methods

|                                                                            Method                                                                             | Modifiers |                                                                                                  Description                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [authForTenant(tenantId)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenantmanager.md#tenantmanagerauthfortenant)              |           | Returns a `TenantAwareAuth` instance bound to the given tenant ID.                                                                                                                                            |
| [createTenant(tenantOptions)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenantmanager.md#tenantmanagercreatetenant)           |           | Creates a new tenant. When creating new tenants, tenants that use separate billing and quota will require their own project and must be defined as `full_service`.                                            |
| [deleteTenant(tenantId)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenantmanager.md#tenantmanagerdeletetenant)                |           | Deletes an existing tenant.                                                                                                                                                                                   |
| [getTenant(tenantId)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenantmanager.md#tenantmanagergettenant)                      |           | Gets the tenant configuration for the tenant corresponding to a given `tenantId`.                                                                                                                             |
| [listTenants(maxResults, pageToken)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenantmanager.md#tenantmanagerlisttenants)     |           | Retrieves a list of tenants (single batch only) with a size of `maxResults` starting from the offset as specified by `pageToken`. This is used to retrieve all the tenants of a specified project in batches. |
| [updateTenant(tenantId, tenantOptions)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenantmanager.md#tenantmanagerupdatetenant) |           | Updates an existing tenant configuration.                                                                                                                                                                     |

## TenantManager.authForTenant()

Returns a `TenantAwareAuth` instance bound to the given tenant ID.

**Signature:**  

    authForTenant(tenantId: string): TenantAwareAuth;

### Parameters

| Parameter |  Type  |                            Description                            |
|-----------|--------|-------------------------------------------------------------------|
| tenantId  | string | The tenant ID whose `TenantAwareAuth` instance is to be returned. |

**Returns:**

[TenantAwareAuth](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenantawareauth.md#tenantawareauth_class)

The `TenantAwareAuth` instance corresponding to this tenant identifier.

## TenantManager.createTenant()

Creates a new tenant. When creating new tenants, tenants that use separate billing and quota will require their own project and must be defined as `full_service`.

**Signature:**  

    createTenant(tenantOptions: CreateTenantRequest): Promise<Tenant>;

### Parameters

|   Parameter   |                                                          Type                                                           |                             Description                              |
|---------------|-------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| tenantOptions | [CreateTenantRequest](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#createtenantrequest) | The properties to set on the new tenant configuration to be created. |

**Returns:**

Promise\<[Tenant](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenant.md#tenant_class)\>

A promise fulfilled with the tenant configuration corresponding to the newly created tenant.

## TenantManager.deleteTenant()

Deletes an existing tenant.

**Signature:**  

    deleteTenant(tenantId: string): Promise<void>;

### Parameters

| Parameter |  Type  |                      Description                      |
|-----------|--------|-------------------------------------------------------|
| tenantId  | string | The `tenantId` corresponding to the tenant to delete. |

**Returns:**

Promise\<void\>

An empty promise fulfilled once the tenant has been deleted.

## TenantManager.getTenant()

Gets the tenant configuration for the tenant corresponding to a given `tenantId`.

**Signature:**  

    getTenant(tenantId: string): Promise<Tenant>;

### Parameters

| Parameter |  Type  |                              Description                               |
|-----------|--------|------------------------------------------------------------------------|
| tenantId  | string | The tenant identifier corresponding to the tenant whose data to fetch. |

**Returns:**

Promise\<[Tenant](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenant.md#tenant_class)\>

A promise fulfilled with the tenant configuration to the provided `tenantId`.

## TenantManager.listTenants()

Retrieves a list of tenants (single batch only) with a size of `maxResults` starting from the offset as specified by `pageToken`. This is used to retrieve all the tenants of a specified project in batches.

**Signature:**  

    listTenants(maxResults?: number, pageToken?: string): Promise<ListTenantsResult>;

### Parameters

| Parameter  |  Type  |                                     Description                                     |
|------------|--------|-------------------------------------------------------------------------------------|
| maxResults | number | The page size, 1000 if undefined. This is also the maximum allowed limit.           |
| pageToken  | string | The next page token. If not specified, returns tenants starting without any offset. |

**Returns:**

Promise\<[ListTenantsResult](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.listtenantsresult.md#listtenantsresult_interface)\>

A promise that resolves with a batch of downloaded tenants and the next page token.

## TenantManager.updateTenant()

Updates an existing tenant configuration.

**Signature:**  

    updateTenant(tenantId: string, tenantOptions: UpdateTenantRequest): Promise<Tenant>;

### Parameters

|   Parameter   |                                                                         Type                                                                          |                      Description                      |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| tenantId      | string                                                                                                                                                | The `tenantId` corresponding to the tenant to delete. |
| tenantOptions | [UpdateTenantRequest](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updatetenantrequest.md#updatetenantrequest_interface) | The properties to update on the provided tenant.      |

**Returns:**

Promise\<[Tenant](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenant.md#tenant_class)\>

A promise fulfilled with the update tenant data.