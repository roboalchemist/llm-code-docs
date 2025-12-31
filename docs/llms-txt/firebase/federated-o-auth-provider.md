# Source: https://firebase.google.com/docs/reference/unity/class/firebase/auth/federated-o-auth-provider.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/federated-o-auth-provider.md.txt

# firebase::auth::FederatedOAuthProvider Class Reference

# firebase::auth::FederatedOAuthProvider


`#include <auth.h>`

Authenticates with Federated OAuth Providers via the [firebase::auth::Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) and [firebase::auth::User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user) classes.

## Summary

Once configured with a provider id, and with OAuth scope and OAuth custom parameters via an FedeartedOAuthProviderData structure, an object of this class may be used via [Auth::SignInWithProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth_1a91a15f187adad095df0eb5be3835583a) to sign-in users, or via [User::LinkWithProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a21ac8cf2e5b915dfd426c4fd707707c2) and [User::ReauthenticateWithProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1ad7501eae0b2c22c96edabacb13176bf6) for cross account linking and user reauthentication, respectively.

### Inheritance

Inherits from: [firebase::auth::FederatedAuthProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/federated-auth-provider)

| ### Constructors and Destructors ||
|---|---|
| [FederatedOAuthProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/federated-o-auth-provider#classfirebase_1_1auth_1_1_federated_o_auth_provider_1ab86ce7fa28d81a8a1959c6d4740e29fc)`()` Constructs an unconfigured provider. ||
| [FederatedOAuthProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/federated-o-auth-provider#classfirebase_1_1auth_1_1_federated_o_auth_provider_1a56d5a371ef702293edcf15bb5262479a)`(const `[FederatedOAuthProviderData](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/federated-o-auth-provider-data#structfirebase_1_1auth_1_1_federated_o_auth_provider_data)` & provider_data)` Constructs a [FederatedOAuthProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/federated-o-auth-provider#classfirebase_1_1auth_1_1_federated_o_auth_provider) preconfigured with provider data. ||
| [~FederatedOAuthProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/federated-o-auth-provider#classfirebase_1_1auth_1_1_federated_o_auth_provider_1a2a7eee290e923f6e8f5684102d651298)`()` ||

|                                                                                                      ### Friend classes                                                                                                       ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| [::firebase::auth::Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/federated-o-auth-provider#classfirebase_1_1auth_1_1_federated_o_auth_provider_1aea624f81c47468d1d1adcec9ced75c01) | `friend class` |

|                                                                                                                                                                                                                                     ### Public functions                                                                                                                                                                                                                                      ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| [SetProviderData](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/federated-o-auth-provider#classfirebase_1_1auth_1_1_federated_o_auth_provider_1a3be1e3b6e46af4facfb95b0b66d16ae0)`(const `[FederatedOAuthProviderData](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/federated-o-auth-provider-data#structfirebase_1_1auth_1_1_federated_o_auth_provider_data)` & provider_data)` | `void` Configures the provider with OAuth provider information. |

## Friend classes

### ::firebase::auth::Auth

```c++
friend class ::firebase::auth::Auth
```  

## Public functions

### FederatedOAuthProvider

```c++
 FederatedOAuthProvider()
```  
Constructs an unconfigured provider.  

### FederatedOAuthProvider

```c++
 FederatedOAuthProvider(
  const FederatedOAuthProviderData & provider_data
)
```  
Constructs a [FederatedOAuthProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/federated-o-auth-provider#classfirebase_1_1auth_1_1_federated_o_auth_provider) preconfigured with provider data.

<br />

|                                                                                                                                                            Details                                                                                                                                                            ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------|------------------------------------------------------------------------------------------------------------------------------------| | `provider_data` | Contains the federated provider id and OAuth scopes and OAuth custom parameters required for user authentication and user linking. | |

### SetProviderData

```c++
void SetProviderData(
  const FederatedOAuthProviderData & provider_data
)
```  
Configures the provider with OAuth provider information.

<br />

|                                                                                                                                                            Details                                                                                                                                                            ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------------|------------------------------------------------------------------------------------------------------------------------------------| | `provider_data` | Contains the federated provider id and OAuth scopes and OAuth custom parameters required for user authentication and user linking. | |

### \~FederatedOAuthProvider

```c++
 ~FederatedOAuthProvider() override
```