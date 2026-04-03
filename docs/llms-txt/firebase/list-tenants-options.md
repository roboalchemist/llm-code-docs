# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/list-tenants-options.md.txt

# FirebaseAdmin.Auth.Multitenancy.ListTenantsOptions Class Reference

# FirebaseAdmin.Auth.Multitenancy.ListTenantsOptions

Options for listing tenants.

## Summary

|                                                                                                                                                    ### Properties                                                                                                                                                    ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [PageSize](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/list-tenants-options#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_list_tenants_options_1a0a31a3f77f53cd926f06e01edbf976a7)  | `int` Gets or sets the number of results to fetch in a single API call. |
| [PageToken](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/list-tenants-options#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_list_tenants_options_1aa08ceeacee064052b39d976c1af76d75) | `string` Gets or sets the page token.                                   |

## Properties

### PageSize

```text
int PageSize
```  
Gets or sets the number of results to fetch in a single API call.

This does not affect the total number of results returned. Must not exceed 100.  

### PageToken

```text
string PageToken
```  
Gets or sets the page token.

If set, this token is used to indicate a continued list operation.