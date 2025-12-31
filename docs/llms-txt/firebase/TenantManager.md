# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager.md.txt

# TenantManager

public final class **TenantManager** extends Object  
This class can be used to perform a variety of tenant-related operations, including creating,
updating, and listing tenants.  

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant)                                                | [createTenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#createTenant(com.google.firebase.auth.multitenancy.Tenant.CreateRequest))([Tenant.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.CreateRequest) request) Creates a new tenant with the attributes contained in the specified [Tenant.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.CreateRequest).                                                                     |
| ApiFuture\<[Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant)\>                                   | [createTenantAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#createTenantAsync(com.google.firebase.auth.multitenancy.Tenant.CreateRequest))([Tenant.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.CreateRequest) request) Similar to [createTenant(CreateRequest)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#createTenant(com.google.firebase.auth.multitenancy.Tenant.CreateRequest)) but performs the operation asynchronously. |
| void                                                                                                                                                                  | [deleteTenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#deleteTenant(java.lang.String))(String tenantId) Deletes the tenant identified by the specified tenant ID.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ApiFuture\<Void\>                                                                                                                                                     | [deleteTenantAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#deleteTenantAsync(java.lang.String))(String tenantId) Similar to [deleteTenant(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#deleteTenant(java.lang.String)) but performs the operation asynchronously.                                                                                                                                                                                                                                       |
| synchronized [TenantAwareFirebaseAuth](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantAwareFirebaseAuth) | [getAuthForTenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#getAuthForTenant(java.lang.String))(String tenantId)                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant)                                                | [getTenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#getTenant(java.lang.String))(String tenantId) Gets the tenant corresponding to the specified tenant ID.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ApiFuture\<[Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant)\>                                   | [getTenantAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#getTenantAsync(java.lang.String))(String tenantId) Similar to [getTenant(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#getTenant(java.lang.String)) but performs the operation asynchronously.                                                                                                                                                                                                                                                   |
| [ListTenantsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/ListTenantsPage)                              | [listTenants](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#listTenants(java.lang.String, int))(String pageToken, int maxResults) Gets a page of tenants starting from the specified `pageToken`.                                                                                                                                                                                                                                                                                                                                                                                              |
| [ListTenantsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/ListTenantsPage)                              | [listTenants](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#listTenants(java.lang.String))(String pageToken) Gets a page of tenants starting from the specified `pageToken`.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ApiFuture\<[ListTenantsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/ListTenantsPage)\>                 | [listTenantsAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#listTenantsAsync(java.lang.String, int))(String pageToken, int maxResults) Similar to [listTenants(String, int)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#listTenants(java.lang.String, int)) but performs the operation asynchronously.                                                                                                                                                                                                           |
| ApiFuture\<[ListTenantsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/ListTenantsPage)\>                 | [listTenantsAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#listTenantsAsync(java.lang.String))(String pageToken) Similar to [listTenants(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#listTenants(java.lang.String)) but performs the operation asynchronously.                                                                                                                                                                                                                                          |
| [Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant)                                                | [updateTenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#updateTenant(com.google.firebase.auth.multitenancy.Tenant.UpdateRequest))([Tenant.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest) request) Updates an existing user account with the attributes contained in the specified [Tenant.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest).                                                         |
| ApiFuture\<[Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant)\>                                   | [updateTenantAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#updateTenantAsync(com.google.firebase.auth.multitenancy.Tenant.UpdateRequest))([Tenant.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest) request) Similar to [updateTenant(UpdateRequest)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#updateTenant(com.google.firebase.auth.multitenancy.Tenant.UpdateRequest)) but performs the operation asynchronously. |

### Inherited Method Summary

From class java.lang.Object  

|------------------|---------------------------|
| Object           | clone()                   |
| boolean          | equals(Object arg0)       |
| void             | finalize()                |
| final Class\<?\> | getClass()                |
| int              | hashCode()                |
| final void       | notify()                  |
| final void       | notifyAll()               |
| String           | toString()                |
| final void       | wait(long arg0, int arg1) |
| final void       | wait(long arg0)           |
| final void       | wait()                    |

## Public Methods

#### public [Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant)
**createTenant**
([Tenant.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.CreateRequest) request)

Creates a new tenant with the attributes contained in the specified [Tenant.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.CreateRequest).  

##### Parameters

| request | A non-null [Tenant.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.CreateRequest) instance. |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A [Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant) instance corresponding to the newly created tenant.  

##### Throws

|                                                          NullPointerException                                                           |       if the provided request is null.        |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | if an error occurs while creating the tenant. |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|

#### public ApiFuture\<[Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant)\>
**createTenantAsync**
([Tenant.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.CreateRequest) request)

Similar to [createTenant(CreateRequest)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#createTenant(com.google.firebase.auth.multitenancy.Tenant.CreateRequest)) but performs the operation asynchronously.  

##### Parameters

| request | A non-null [Tenant.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.CreateRequest) instance. |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with a [Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant) instance corresponding to the newly created tenant. If an error occurs while creating the tenant, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| NullPointerException | if the provided request is null. |
|----------------------|----------------------------------|

#### public void
**deleteTenant**
(String tenantId)

Deletes the tenant identified by the specified tenant ID.  

##### Parameters

| tenantId | A tenant ID string. |
|----------|---------------------|

##### Throws

|                                                        IllegalArgumentException                                                         |   If the tenant ID string is null or empty.   |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | If an error occurs while deleting the tenant. |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|

#### public ApiFuture\<Void\>
**deleteTenantAsync**
(String tenantId)

Similar to [deleteTenant(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#deleteTenant(java.lang.String)) but performs the operation asynchronously.  

##### Parameters

| tenantId | A tenant ID string. |
|----------|---------------------|

##### Returns

- An `ApiFuture` which will complete successfully when the specified tenant account has been deleted. If an error occurs while deleting the tenant account, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| IllegalArgumentException | If the tenant ID string is null or empty. |
|--------------------------|-------------------------------------------|

#### public synchronized [TenantAwareFirebaseAuth](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantAwareFirebaseAuth)
**getAuthForTenant**
(String tenantId)

<br />

#### public [Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant)
**getTenant**
(String tenantId)

Gets the tenant corresponding to the specified tenant ID.  

##### Parameters

| tenantId | A tenant ID string. |
|----------|---------------------|

##### Returns

- A [Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant) instance.  

##### Throws

|                                                        IllegalArgumentException                                                         |   If the tenant ID string is null or empty.    |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | If an error occurs while retrieving user data. |
|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|

#### public ApiFuture\<[Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant)\>
**getTenantAsync**
(String tenantId)

Similar to [getTenant(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#getTenant(java.lang.String)) but performs the operation asynchronously.  

##### Parameters

| tenantId | A tenantId string. |
|----------|--------------------|

##### Returns

- An `ApiFuture` which will complete successfully with a [Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant) instance If an error occurs while retrieving tenant data or if the specified tenant ID does not exist, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).  

##### Throws

| IllegalArgumentException | If the tenant ID string is null or empty. |
|--------------------------|-------------------------------------------|

#### public [ListTenantsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/ListTenantsPage)
**listTenants**
(String pageToken, int maxResults)

Gets a page of tenants starting from the specified `pageToken`.  

##### Parameters

| pageToken  |    A non-empty page token string, or null to retrieve the first page of tenants.     |
| maxResults | Maximum number of tenants to include in the returned page. This may not exceed 1000. |
|------------|--------------------------------------------------------------------------------------|

##### Returns

- A [ListTenantsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/ListTenantsPage) instance.  

##### Throws

|                                                        IllegalArgumentException                                                         | If the specified page token is empty, or max results value is invalid. |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) |            If an error occurs while retrieving tenant data.            |
|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|

#### public [ListTenantsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/ListTenantsPage)
**listTenants**
(String pageToken)

Gets a page of tenants starting from the specified `pageToken`. Page size will be limited
to 1000 tenants.  

##### Parameters

| pageToken | A non-empty page token string, or null to retrieve the first page of tenants. |
|-----------|-------------------------------------------------------------------------------|

##### Returns

- A [ListTenantsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/ListTenantsPage) instance.  

##### Throws

|                                                        IllegalArgumentException                                                         |      If the specified page token is empty.       |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | If an error occurs while retrieving tenant data. |
|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|

#### public ApiFuture\<[ListTenantsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/ListTenantsPage)\>
**listTenantsAsync**
(String pageToken, int maxResults)

Similar to [listTenants(String, int)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#listTenants(java.lang.String, int)) but performs the operation asynchronously.  

##### Parameters

| pageToken  |    A non-empty page token string, or null to retrieve the first page of tenants.     |
| maxResults | Maximum number of tenants to include in the returned page. This may not exceed 1000. |
|------------|--------------------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with a [ListTenantsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/ListTenantsPage) instance. If an error occurs while retrieving tenant data, the future throws an exception.  

##### Throws

| IllegalArgumentException | If the specified page token is empty, or max results value is invalid. |
|--------------------------|------------------------------------------------------------------------|

#### public ApiFuture\<[ListTenantsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/ListTenantsPage)\>
**listTenantsAsync**
(String pageToken)

Similar to [listTenants(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#listTenants(java.lang.String)) but performs the operation asynchronously.  

##### Parameters

| pageToken | A non-empty page token string, or null to retrieve the first page of tenants. |
|-----------|-------------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with a [ListTenantsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/ListTenantsPage) instance. If an error occurs while retrieving tenant data, the future throws an exception.  

##### Throws

| IllegalArgumentException | If the specified page token is empty. |
|--------------------------|---------------------------------------|

#### public [Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant)
**updateTenant**
([Tenant.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest) request)

Updates an existing user account with the attributes contained in the specified [Tenant.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest).  

##### Parameters

| request | A non-null [Tenant.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest) instance. |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A [Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant) instance corresponding to the updated user account.  

##### Throws

|                                                          NullPointerException                                                           |       if the provided update request is null.       |
| [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException) | if an error occurs while updating the user account. |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|

#### public ApiFuture\<[Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant)\>
**updateTenantAsync**
([Tenant.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest) request)

Similar to [updateTenant(UpdateRequest)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#updateTenant(com.google.firebase.auth.multitenancy.Tenant.UpdateRequest)) but performs the operation asynchronously.  

##### Parameters

| request | A non-null [Tenant.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest) instance. |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully with a [Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant) instance corresponding to the updated user account. If an error occurs while updating the user account, the future throws a [FirebaseAuthException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/FirebaseAuthException).