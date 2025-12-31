# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/auth-provider-config-args-t-.md.txt

# FirebaseAdmin.Auth.Providers.AuthProviderConfigArgs Class Reference

# FirebaseAdmin.Auth.Providers.AuthProviderConfigArgs\< T \>


**This is an abstract class.**

The base auth provider configuration interface.

## Summary

[Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth) provider configuration support requires Google Cloud's Identity Platform (GCIP). To learn more about GCIP, including pricing and features, see the [GCIP documentation](https://cloud.google.com/identity-platform).

<br />

|                                                                                                                                                                                                                                                                                              Details                                                                                                                                                                                                                                                                                               ||
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Template Parameters | |-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `T` | Type of [AuthProviderConfig](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/auth-provider-config#class_firebase_admin_1_1_auth_1_1_providers_1_1_auth_provider_config) that can be created or updated using this argument type. | |

### Inheritance

Direct Known Subclasses:[FirebaseAdmin.Auth.Providers.OidcProviderConfigArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/oidc-provider-config-args), [FirebaseAdmin.Auth.Providers.SamlProviderConfigArgs](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/saml-provider-config-args)

|                                                                                                                                                                           ### Properties                                                                                                                                                                            ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [DisplayName](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/auth-provider-config-args-t-#class_firebase_admin_1_1_auth_1_1_providers_1_1_auth_provider_config_args_3_01_t_01_4_1acfc413bac632ef41974fae0b9c8d7997) | `string` Gets or sets the user-friendly display name of the configuration.                        |
| [Enabled](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/auth-provider-config-args-t-#class_firebase_admin_1_1_auth_1_1_providers_1_1_auth_provider_config_args_3_01_t_01_4_1a3170b7484ff9c3029168dbef51347c71)     | `bool` Gets or sets a value indicating whether the provider configuration is enabled or disabled. |
| [ProviderId](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/auth-provider-config-args-t-#class_firebase_admin_1_1_auth_1_1_providers_1_1_auth_provider_config_args_3_01_t_01_4_1ac778b4718716a1fb6cbc6f19c0334fe5)  | `string` Gets or sets the provider ID defined by the developer.                                   |

## Properties

### DisplayName

```text
string DisplayName
```  
Gets or sets the user-friendly display name of the configuration.

This name is also used as the provider label in the Cloud Console.  

### Enabled

```text
bool Enabled
```  
Gets or sets a value indicating whether the provider configuration is enabled or disabled.

A user cannot sign in using a disabled provider.  

### ProviderId

```text
string ProviderId
```  
Gets or sets the provider ID defined by the developer.

For an OIDC provider, this is always prefixed by `oidc.`. For a SAML provider, this is always prefixed by `saml.`.