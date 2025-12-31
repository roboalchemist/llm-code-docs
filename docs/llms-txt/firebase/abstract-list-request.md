# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/provider-config-client-t-/abstract-list-request.md.txt

# FirebaseAdmin.Auth.Providers.ProviderConfigClient.AbstractListRequest Class Reference

# FirebaseAdmin.Auth.Providers.ProviderConfigClient\< T \>.AbstractListRequest

A class for making batch GET requests to list a specific type of auth provider configuration.

## Summary

An instance of this class is used by the Google API client to provide pagination support.

### Inheritance

Inherits from: FirebaseAdmin.Auth.Providers.ProviderConfigClient\< T \>

|                                                                                                                                                    ### Properties                                                                                                                                                     ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [ApiClient](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/provider-config-client-t-/abstract-list-request#class_firebase_admin_1_1_auth_1_1_providers_1_1_provider_config_client_3_01_t_01_4_1_1_abstract_list_request_1aa88a1623ef240779230837f5fff60a06) | `ApiClient` |

|                                                                                                                                                                                                                                                                                     ### Protected functions                                                                                                                                                                                                                                                                                      ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| [AbstractListRequest](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/provider-config-client-t-/abstract-list-request#class_firebase_admin_1_1_auth_1_1_providers_1_1_provider_config_client_3_01_t_01_4_1_1_abstract_list_request_1aba165733f4697d8555e79d05da4ae6ca)`(ApiClient client, `[ListProviderConfigsOptions](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/list-provider-configs-options#class_firebase_admin_1_1_auth_1_1_providers_1_1_list_provider_configs_options)` options)` | ` ` ` ` |

|                                                                                                                                                                                    ### Public functions                                                                                                                                                                                     ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| [ExecuteAsStreamAsync](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/provider-config-client-t-/abstract-list-request#class_firebase_admin_1_1_auth_1_1_providers_1_1_provider_config_client_3_01_t_01_4_1_1_abstract_list_request_1a56466fbb5a009f89ad365982f69aaae4)`(CancellationToken cancellationToken)` | `override async Task< Stream >` |

## Properties

### ApiClient

```text
ApiClient ApiClient
```  

## Protected functions

### AbstractListRequest

```text
 AbstractListRequest(
  ApiClient client,
  ListProviderConfigsOptions options
)
```  

## Public functions

### ExecuteAsStreamAsync

```text
override async Task< Stream > ExecuteAsStreamAsync(
  CancellationToken cancellationToken
)
```