# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/federated-auth-provider.md.txt

# firebase::auth::FederatedAuthProvider Class Reference

# firebase::auth::FederatedAuthProvider


`#include <auth.h>`

Used to authenticate with Federated [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) Providers.

## Summary

The federated auth provider implementation may facilitate multiple provider types in the future, with support for OAuth to start.

### Inheritance

Direct Known Subclasses:[firebase::auth::FederatedOAuthProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/federated-o-auth-provider)

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/federated-auth-provider#classfirebase_1_1auth_1_1_federated_auth_provider_1a0af09e2090395b21eaf1df32cbc56d6d()` ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/federated-auth-provider#classfirebase_1_1auth_1_1_federated_auth_provider_1ae1398400b6186c16a49393a359470a12()` ||

| ### Friend classes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/federated-auth-provider#classfirebase_1_1auth_1_1_federated_auth_provider_1aea624f81c47468d1d1adcec9ced75c01` | `friend class` |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/federated-auth-provider#classfirebase_1_1auth_1_1_federated_auth_provider_1a9b0f69109a181d67de4cbf01b854ae6e` | `friend class` |

## Friend classes

### ::firebase::auth::Auth

```c++
friend class ::firebase::auth::Auth
```

### ::firebase::auth::User

```c++
friend class ::firebase::auth::User
```

## Public functions

### FederatedAuthProvider

```c++
 FederatedAuthProvider()
```

### \~FederatedAuthProvider

```c++
virtual  ~FederatedAuthProvider()
```