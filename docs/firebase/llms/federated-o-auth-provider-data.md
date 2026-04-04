# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/federated-o-auth-provider-data.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/auth/federated-o-auth-provider-data.md.txt

# Firebase.Auth.FederatedOAuthProviderData Class Reference

# Firebase.Auth.FederatedOAuthProviderData

Contains information to identify an OAuth povider.

## Summary

### Inheritance

Inherits from: [Firebase.Auth.FederatedProviderData](https://firebase.google.com/docs/reference/unity/class/firebase/auth/federated-provider-data)

| ### Constructors and Destructors ||
|---|---|
| [FederatedOAuthProviderData](https://firebase.google.com/docs/reference/unity/class/firebase/auth/federated-o-auth-provider-data#class_firebase_1_1_auth_1_1_federated_o_auth_provider_data_1a82f735ec245e71b334158de71e179ba7)`()` ||
| [FederatedOAuthProviderData](https://firebase.google.com/docs/reference/unity/class/firebase/auth/federated-o-auth-provider-data#class_firebase_1_1_auth_1_1_federated_o_auth_provider_data_1a818be334d2de493138d8cff2bf9365f3)`(string provider)` ||

|                                                                                                                                      ### Properties                                                                                                                                       ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| [CustomParameters](https://firebase.google.com/docs/reference/unity/class/firebase/auth/federated-o-auth-provider-data#class_firebase_1_1_auth_1_1_federated_o_auth_provider_data_1aa8687875d1ff9e8b4a8d3f61ef3886b1) | `global::System.Collections.Generic.IDictionary< string, string >` |
| [Scopes](https://firebase.google.com/docs/reference/unity/class/firebase/auth/federated-o-auth-provider-data#class_firebase_1_1_auth_1_1_federated_o_auth_provider_data_1aae8b4c84d9930ae04ab8986820ae34ff)           | `global::System.Collections.Generic.IEnumerable< string >`         |

|                                                                                                                  ### Public functions                                                                                                                   ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| [Dispose](https://firebase.google.com/docs/reference/unity/class/firebase/auth/federated-o-auth-provider-data#class_firebase_1_1_auth_1_1_federated_o_auth_provider_data_1aff2ed0649805489e0352e193758b1655)`(bool disposing)` | `virtual override void` |

## Properties

### CustomParameters

```c#
global::System.Collections.Generic.IDictionary< string, string > CustomParameters
```  

### Scopes

```c#
global::System.Collections.Generic.IEnumerable< string > Scopes
```  

## Public functions

### Dispose

```c#
virtual override void Dispose(
  bool disposing
)
```  

### FederatedOAuthProviderData

```c#
 FederatedOAuthProviderData()
```  

### FederatedOAuthProviderData

```c#
 FederatedOAuthProviderData(
  string provider
)
```