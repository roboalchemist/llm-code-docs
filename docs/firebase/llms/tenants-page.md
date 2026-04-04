# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenants-page.md.txt

# FirebaseAdmin.Auth.Multitenancy.TenantsPage Class Reference

# FirebaseAdmin.Auth.Multitenancy.TenantsPage

Contains a collection of tenants.

## Summary

|                                                                                                                                                                                                                                ### Properties                                                                                                                                                                                                                                ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [NextPageToken](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenants-page#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenants_page_1ac1f82dfada622d659805123a6fb73dd4) | `string` Gets the token representing the next page of tenants.                                                                                                                                                                              |
| [Tenants](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenants-page#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenants_page_1af7ae38ab3b50ddd5cc2675d324d36bd4)       | `IEnumerable< `[Tenant](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant)` >` Gets the tenants included in the current page. |

## Properties

### NextPageToken

```text
string NextPageToken
```  
Gets the token representing the next page of tenants.

Null if there are no more pages.  

### Tenants

```text
IEnumerable< Tenant > Tenants
```  
Gets the tenants included in the current page.