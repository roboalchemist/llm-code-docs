# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant-manager.md.txt

# FirebaseAdmin.Auth.Multitenancy.TenantManager Class Reference

# FirebaseAdmin.Auth.Multitenancy.TenantManager

The tenant manager facilitates GCIP multitenancy related operations.

## Summary

This includes:

- Creating, updating, retrieving and deleting tenants in the underlying project.
- Obtaining [TenantAwareFirebaseAuth](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant-aware-firebase-auth#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant_aware_firebase_auth) instances for performing operations (user management, provider configuration management, token verification, email link generation, etc) in the context of a specified tenant.

<br />

### Inheritance

Inherits from: IDisposable

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AuthForTenant](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant-manager#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant_manager_1a216a1da2f70a89e70c1caee430990f0b)`(string tenantId)`                                                                                                                                                                                                                                          | [TenantAwareFirebaseAuth](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant-aware-firebase-auth#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant_aware_firebase_auth) Gets a [TenantAwareFirebaseAuth](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant-aware-firebase-auth#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant_aware_firebase_auth) instance scoped to the specified tenant. |
| [CreateTenantAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant-manager#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant_manager_1a2b30bc5d004876182d55694d0a42eb5d)`(`[TenantArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant-args#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant_args)` args)`                                                       | `async Task< `[Tenant](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant)` >` Creates a new tenant.                                                                                                                                                                                                                                                                                                     |
| [CreateTenantAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant-manager#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant_manager_1a5dcb2418f44d532e5682af93c0e263f6)`(`[TenantArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant-args#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant_args)` args, CancellationToken cancellationToken)`                  | `async Task< `[Tenant](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant)` >` Creates a new tenant.                                                                                                                                                                                                                                                                                                     |
| [DeleteTenantAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant-manager#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant_manager_1abb1437b978f10cdef356e3c0ebb87981)`(string tenantId)`                                                                                                                                                                                                                                      | `async Task` Deletes the tenant corresponding to the given *tenantId* .                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [DeleteTenantAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant-manager#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant_manager_1a4b3fefe99631ef4332127037c26b244a)`(string tenantId, CancellationToken cancellationToken)`                                                                                                                                                                                                 | `async Task` Deletes the tenant corresponding to the given *tenantId* .                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [GetTenantAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant-manager#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant_manager_1af33ee8a15c107a9e31fe752b8eb95fcb)`(string tenantId)`                                                                                                                                                                                                                                         | `async Task< `[Tenant](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant)` >` Gets the [Tenant](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant) corresponding to the given *tenantId* .                                                                                                |
| [GetTenantAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant-manager#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant_manager_1a25bbbcd7748864bc85d1d4a9ae5f8f85)`(string tenantId, CancellationToken cancellationToken)`                                                                                                                                                                                                    | `async Task< `[Tenant](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant)` >` Gets the [Tenant](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant) corresponding to the given *tenantId* .                                                                                                |
| [ListTenantsAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant-manager#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant_manager_1a6e7a80426d53d416ec66b9c0d9ec3cfc)`(`[ListTenantsOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/list-tenants-options#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_list_tenants_options)` options)`                           | `PagedAsyncEnumerable< `[TenantsPage](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenants-page#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenants_page)`, `[Tenant](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant)` >` Gets an async enumerable to iterate or page through tenants starting from the specified page token.               |
| [UpdateTenantAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant-manager#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant_manager_1ace5ef498218c01e030ed34bb9ed105c5)`(string tenantId, `[TenantArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant-args#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant_args)` args)`                                      | `async Task< `[Tenant](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant)` >` Updates an existing tenant.                                                                                                                                                                                                                                                                                               |
| [UpdateTenantAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant-manager#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant_manager_1a9f163bcbe940e2b64ba390a413879f27)`(string tenantId, `[TenantArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant-args#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant_args)` args, CancellationToken cancellationToken)` | `async Task< `[Tenant](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant)` >` Updates an existing tenant.                                                                                                                                                                                                                                                                                               |

## Public functions

### AuthForTenant

```text
TenantAwareFirebaseAuth AuthForTenant(
  string tenantId
)
```  
Gets a [TenantAwareFirebaseAuth](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant-aware-firebase-auth#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant_aware_firebase_auth) instance scoped to the specified tenant.

<br />

|                                                                         Details                                                                          ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|-----------------------------| | `tenantId` | A tenant identifier string. |                                                   |
| Exceptions  | |---------------------|---------------------------------------------| | `ArgumentException` | If the tenant ID argument is null or empty. | |
| **Returns** | An object that can be used to perform tenant-aware operations.                                                                              |

### CreateTenantAsync

```text
async Task< Tenant > CreateTenantAsync(
  TenantArgs args
)
```  
Creates a new tenant.

<br />

|                                                                                                                                      Details                                                                                                                                      ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------|-------------------------------------------------------| | `args` | Arguments that describe the new tenant configuration. |                                                                                                                                |
| Exceptions  | |-------------------------|----------------------------------------------------------| | `ArgumentNullException` | If *args* is null.                                       | | `FirebaseAuthException` | If an unexpected error occurs while creating the tenant. | |
| **Returns** | A task that completes with a [Tenant](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant).                                                              |

### CreateTenantAsync

```text
async Task< Tenant > CreateTenantAsync(
  TenantArgs args,
  CancellationToken cancellationToken
)
```  
Creates a new tenant.

<br />

|                                                                                                                                      Details                                                                                                                                      ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|-------------------------------------------------------------| | `args`              | Arguments that describe the new tenant configuration.       | | `cancellationToken` | A cancellation token to monitor the asynchronous operation. |    |
| Exceptions  | |-------------------------|----------------------------------------------------------| | `ArgumentNullException` | If *args* is null.                                       | | `FirebaseAuthException` | If an unexpected error occurs while creating the tenant. | |
| **Returns** | A task that completes with a [Tenant](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant).                                                              |

### DeleteTenantAsync

```text
async Task DeleteTenantAsync(
  string tenantId
)
```  
Deletes the tenant corresponding to the given *tenantId* .

<br />

|                                                                                                                             Details                                                                                                                             ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|-----------------------------| | `tenantId` | A tenant identifier string. |                                                                                                                                                          |
| Exceptions  | |-------------------------|----------------------------------------------------| | `ArgumentException`     | If the tenant ID argument is null or empty.        | | `FirebaseAuthException` | If a tenant cannot be found with the specified ID. | |
| **Returns** | A task that completes when the tenant is deleted.                                                                                                                                                                                                  |

### DeleteTenantAsync

```text
async Task DeleteTenantAsync(
  string tenantId,
  CancellationToken cancellationToken
)
```  
Deletes the tenant corresponding to the given *tenantId* .

<br />

|                                                                                                                                    Details                                                                                                                                     ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|-------------------------------------------------------------| | `tenantId`          | A tenant identifier string.                                 | | `cancellationToken` | A cancellation token to monitor the asynchronous operation. | |
| Exceptions  | |-------------------------|----------------------------------------------------| | `ArgumentException`     | If the tenant ID argument is null or empty.        | | `FirebaseAuthException` | If a tenant cannot be found with the specified ID. |                |
| **Returns** | A task that completes when the tenant is deleted.                                                                                                                                                                                                                 |

### GetTenantAsync

```text
async Task< Tenant > GetTenantAsync(
  string tenantId
)
```  
Gets the [Tenant](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant) corresponding to the given *tenantId* .

<br />

|                                                                                                                             Details                                                                                                                             ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|-----------------------------| | `tenantId` | A tenant identifier string. |                                                                                                                                                          |
| Exceptions  | |-------------------------|----------------------------------------------------| | `ArgumentException`     | If tenant ID argument is null or empty.            | | `FirebaseAuthException` | If a tenant cannot be found with the specified ID. | |
| **Returns** | A task that completes with a [Tenant](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant).                                            |

### GetTenantAsync

```text
async Task< Tenant > GetTenantAsync(
  string tenantId,
  CancellationToken cancellationToken
)
```  
Gets the [Tenant](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant) corresponding to the given *tenantId* .

<br />

|                                                                                                                                    Details                                                                                                                                     ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|-------------------------------------------------------------| | `tenantId`          | A tenant identifier string.                                 | | `cancellationToken` | A cancellation token to monitor the asynchronous operation. | |
| Exceptions  | |-------------------------|----------------------------------------------------| | `ArgumentException`     | If the tenant ID argument is null or empty.        | | `FirebaseAuthException` | If a tenant cannot be found with the specified ID. |                |
| **Returns** | A task that completes with a [Tenant](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant).                                                           |

### ListTenantsAsync

```text
PagedAsyncEnumerable< TenantsPage, Tenant > ListTenantsAsync(
  ListTenantsOptions options
)
```  
Gets an async enumerable to iterate or page through tenants starting from the specified page token.

If the page token is null or unspecified, iteration starts from the first page. See [Page Streaming](https://googleapis.github.io/google-cloud-dotnet/docs/guides/page-streaming.html) for more details on how to use this API.

<br />

|                                                                                                                                        Details                                                                                                                                         ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-----------|----------------------------------------------------------------------------------------------------------------------| | `options` | The options to control the starting point and page size. Pass null to list from the beginning with default settings. | |
| **Returns** | A PagedAsyncEnumerable{TenantsPage, Tenant} instance.                                                                                                                                                                                                                     |

### UpdateTenantAsync

```text
async Task< Tenant > UpdateTenantAsync(
  string tenantId,
  TenantArgs args
)
```  
Updates an existing tenant.

<br />

|                                                                                                                                                                                                                   Details                                                                                                                                                                                                                    ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|-----------------------------------------| | `tenantId` | ID of the tenant to be updated.         | | `args`     | Properties to be updated in the tenant. |                                                                                                                                                                                                                                                      |
| Exceptions  | |-------------------------|---------------------------------------------------------------------------| | `ArgumentException`     | If *tenantId* is null or empty, or if *args* does not contain any values. | | `ArgumentNullException` | If *args* is null.                                                        | | `FirebaseAuthException` | If an unexpected error occurs while updating the tenant.                  | |
| **Returns** | A task that completes with a [Tenant](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant).                                                                                                                                                                                                                         |

### UpdateTenantAsync

```text
async Task< Tenant > UpdateTenantAsync(
  string tenantId,
  TenantArgs args,
  CancellationToken cancellationToken
)
```  
Updates an existing tenant.

<br />

|                                                                                                                                                                                                                   Details                                                                                                                                                                                                                    ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |---------------------|-------------------------------------------------------------| | `tenantId`          | ID of the tenant to be updated.                             | | `args`              | Properties to be updated in the tenant.                     | | `cancellationToken` | A cancellation token to monitor the asynchronous operation. |                                                                         |
| Exceptions  | |-------------------------|---------------------------------------------------------------------------| | `ArgumentException`     | If *tenantId* is null or empty, or if *args* does not contain any values. | | `ArgumentNullException` | If *args* is null.                                                        | | `FirebaseAuthException` | If an unexpected error occurs while updating the tenant.                  | |
| **Returns** | A task that completes with a [Tenant](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant).                                                                                                                                                                                                                         |