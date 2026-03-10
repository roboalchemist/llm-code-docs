# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/federated-provider-data.md.txt

# firebase::auth::FederatedProviderData Struct Reference

# firebase::auth::FederatedProviderData


`#include <types.h>`

Contains information required to authenticate with a third party provider.

## Summary

### Inheritance

Direct Known Subclasses:[firebase::auth::FederatedOAuthProviderData](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/federated-o-auth-provider-data)

| ### Public attributes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/federated-provider-data#structfirebase_1_1auth_1_1_federated_provider_data_1a3a4f052f8e1fd685ec2b2a253c190139` | `std::string` contains the id of the provider to be used during sign-in, link, or reauthentication requests. |

## Public attributes

### provider_id

```c++
std::string firebase::auth::FederatedProviderData::provider_id
```
contains the id of the provider to be used during sign-in, link, or reauthentication requests.