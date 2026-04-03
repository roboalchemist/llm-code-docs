# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/list-provider-configs-options.md.txt

# FirebaseAdmin.Auth.Providers.ListProviderConfigsOptions Class Reference

# FirebaseAdmin.Auth.Providers.ListProviderConfigsOptions

Options for listing auth provider configurations.

## Summary

|                                                                                                                                                          ### Properties                                                                                                                                                          ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [PageSize](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/list-provider-configs-options#class_firebase_admin_1_1_auth_1_1_providers_1_1_list_provider_configs_options_1aae3f54ca7616d4a024f2ec6bd130e95c)  | `int` Gets or sets the number of results to fetch in a single API call. |
| [PageToken](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/list-provider-configs-options#class_firebase_admin_1_1_auth_1_1_providers_1_1_list_provider_configs_options_1a8e3d18405fd14cf37a5fa77ffed6ed37) | `string` Gets or sets the page token.                                   |

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