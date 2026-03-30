# Source: https://firebase.google.com/docs/reference/unity/class/firebase/auth/federated-o-auth-provider.md.txt

# Firebase.Auth.FederatedOAuthProvider Class Reference

# Firebase.Auth.FederatedOAuthProvider

Authenticates with Federated OAuth Providers via the firebase::auth::Auth and firebase::auth::User classes.

## Summary

Once configured with a provider id, and with OAuth scope and OAuth custom parameters via an FedeartedOAuthProviderData structure, an object of this class may be used via Auth::SignInWithProvider to sign-in users, or via User::LinkWithProvider and User::ReauthenticateWithProvider for cross account linking and user reauthentication, respectively.

### Inheritance

Inherits from: [Firebase.Auth.FederatedAuthProvider](https://firebase.google.com/docs/reference/unity/class/firebase/auth/federated-auth-provider)

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/federated-o-auth-provider#class_firebase_1_1_auth_1_1_federated_o_auth_provider_1ac1e934b000ac5153a2e91cf36582e5cd()` ||
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/federated-o-auth-provider#class_firebase_1_1_auth_1_1_federated_o_auth_provider_1a2839ea9dcd93ea78d43ab8cc90b3601a(https://firebase.google.com/docs/reference/unity/class/firebase/auth/federated-o-auth-provider-data#class_firebase_1_1_auth_1_1_federated_o_auth_provider_data providerData)` ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/federated-o-auth-provider#class_firebase_1_1_auth_1_1_federated_o_auth_provider_1a8a9b58ad0337479e2135d4176fb0be35(bool disposing)` | `virtual override void` |
| `https://firebase.google.com/docs/reference/unity/class/firebase/auth/federated-o-auth-provider#class_firebase_1_1_auth_1_1_federated_o_auth_provider_1a1c033ff5563582f0bb4a1826b715bc5d(https://firebase.google.com/docs/reference/unity/class/firebase/auth/federated-o-auth-provider-data#class_firebase_1_1_auth_1_1_federated_o_auth_provider_data providerData)` | `void` |

## Public functions

### Dispose

```c#
virtual override void Dispose(
  bool disposing
)
```

### FederatedOAuthProvider

```c#
 FederatedOAuthProvider()
```

### FederatedOAuthProvider

```c#
 FederatedOAuthProvider(
  FederatedOAuthProviderData providerData
)
```

### SetProviderData

```c#
void SetProviderData(
  FederatedOAuthProviderData providerData
)
```