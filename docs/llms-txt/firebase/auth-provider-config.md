# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/auth-provider-config.md.txt

# FirebaseAdmin.Auth.Providers.AuthProviderConfig Class Reference

# FirebaseAdmin.Auth.Providers.AuthProviderConfig

The base [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth) provider configuration interface.

## Summary

[Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth) provider configuration support requires Google Cloud's Identity Platform (GCIP). To learn more about GCIP, including pricing and features, see the [GCIP documentation](https://cloud.google.com/identity-platform).

### Inheritance

Direct Known Subclasses:[FirebaseAdmin.Auth.Providers.OidcProviderConfig](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/oidc-provider-config), [FirebaseAdmin.Auth.Providers.SamlProviderConfig](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/saml-provider-config)

|                                                                                                                                                           ### Properties                                                                                                                                                           ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [DisplayName](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/auth-provider-config#class_firebase_admin_1_1_auth_1_1_providers_1_1_auth_provider_config_1a0591048eb37b68faac9eb358fbc4eb0a) | `string` Gets the user-friendly display name of the configuration.                        |
| [Enabled](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/auth-provider-config#class_firebase_admin_1_1_auth_1_1_providers_1_1_auth_provider_config_1a8ad7d3672990c3688327dcbd000e815d)     | `bool` Gets a value indicating whether the provider configuration is enabled or disabled. |
| [ProviderId](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/auth-provider-config#class_firebase_admin_1_1_auth_1_1_providers_1_1_auth_provider_config_1a8b0b3d4c3d76a303e9492e09ff900e5b)  | `string` Gets the provider ID defined by the developer.                                   |

## Properties

### DisplayName

```text
string DisplayName
```  
Gets the user-friendly display name of the configuration.

This name is also used as the provider label in the Cloud Console.  

### Enabled

```text
bool Enabled
```  
Gets a value indicating whether the provider configuration is enabled or disabled.

A user cannot sign in using a disabled provider.  

### ProviderId

```text
string ProviderId
```  
Gets the provider ID defined by the developer.

For an OIDC provider, this is always prefixed by `oidc.`. For a SAML provider, this is always prefixed by `saml.`.