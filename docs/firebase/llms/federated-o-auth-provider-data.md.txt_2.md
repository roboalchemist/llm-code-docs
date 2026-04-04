# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/federated-o-auth-provider-data.md.txt

# firebase::auth::FederatedOAuthProviderData Struct Reference

# firebase::auth::FederatedOAuthProviderData


`#include <types.h>`

Contains information to identify an OAuth povider.

## Summary

### Inheritance

Inherits from: [firebase::auth::FederatedProviderData](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/federated-provider-data)

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/federated-o-auth-provider-data#structfirebase_1_1auth_1_1_federated_o_auth_provider_data_1a231678537898b48971bed4f195d5f8a4()` Initailizes an empty provider data structure. ||
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/federated-o-auth-provider-data#structfirebase_1_1auth_1_1_federated_o_auth_provider_data_1afda3bfa3534c1a1108cc668adb49d150(const std::string & provider)` Initializes the provider data structure with a provider id. ||
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/federated-o-auth-provider-data#structfirebase_1_1auth_1_1_federated_o_auth_provider_data_1a24a854283e00c0802de820771ab03634(const std::string & provider, std::vector< std::string > scopes, std::map< std::string, std::string > custom_parameters)` Initializes the provider data structure with the specified provider id, scopes and custom parameters. ||

| ### Public attributes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/federated-o-auth-provider-data#structfirebase_1_1auth_1_1_federated_o_auth_provider_data_1a27f1e28473cd0618716575cea63fdbfc` | `std::map< std::string, std::string >` OAuth parameters which are provided to the federated provider service. |
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/federated-o-auth-provider-data#structfirebase_1_1auth_1_1_federated_o_auth_provider_data_1afd20cd394e5f88f07c614a1d6103efb0` | `std::vector< std::string >` OAuth parmeters which specify which rights of access are being requested. |

## Public attributes

### custom_parameters

```c++
std::map< std::string, std::string > firebase::auth::FederatedOAuthProviderData::custom_parameters
```
OAuth parameters which are provided to the federated provider service.

### scopes

```c++
std::vector< std::string > firebase::auth::FederatedOAuthProviderData::scopes
```
OAuth parmeters which specify which rights of access are being requested.

## Public functions

### FederatedOAuthProviderData

```c++
 firebase::auth::FederatedOAuthProviderData::FederatedOAuthProviderData()
```
Initailizes an empty provider data structure.

### FederatedOAuthProviderData

```c++
 firebase::auth::FederatedOAuthProviderData::FederatedOAuthProviderData(
  const std::string & provider
)
```
Initializes the provider data structure with a provider id.

### FederatedOAuthProviderData

```c++
 firebase::auth::FederatedOAuthProviderData::FederatedOAuthProviderData(
  const std::string & provider,
  std::vector< std::string > scopes,
  std::map< std::string, std::string > custom_parameters
)
```
Initializes the provider data structure with the specified provider id, scopes and custom parameters.