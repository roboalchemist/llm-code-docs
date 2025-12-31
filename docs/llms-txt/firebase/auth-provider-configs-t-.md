# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/auth-provider-configs-t-.md.txt

# FirebaseAdmin.Auth.Providers.AuthProviderConfigs Class Reference

# FirebaseAdmin.Auth.Providers.AuthProviderConfigs\< T \>

A page of auth provider configurations.

## Summary

<br />

|                                                                                                                                                                                                                                                       Details                                                                                                                                                                                                                                                        ||
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Template Parameters | |-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `T` | Type of [AuthProviderConfig](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/auth-provider-config#class_firebase_admin_1_1_auth_1_1_providers_1_1_auth_provider_config) that is included. | |

|                                                                                                                                                                    ### Properties                                                                                                                                                                    ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [NextPageToken](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/auth-provider-configs-t-#class_firebase_admin_1_1_auth_1_1_providers_1_1_auth_provider_configs_3_01_t_01_4_1aa7da1afd541976250cb79acbec5d1fbb)   | `string` Gets the token representing the next page of auth provider configurations.    |
| [ProviderConfigs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/auth-provider-configs-t-#class_firebase_admin_1_1_auth_1_1_providers_1_1_auth_provider_configs_3_01_t_01_4_1a22a77c6cdca009102eaf3ef0770781d6) | `IEnumerable< T >` Gets the auth provider configurations included in the current page. |

## Properties

### NextPageToken

```text
string NextPageToken
```  
Gets the token representing the next page of auth provider configurations.

Null if there are no more pages.  

### ProviderConfigs

```text
IEnumerable< T > ProviderConfigs
```  
Gets the auth provider configurations included in the current page.