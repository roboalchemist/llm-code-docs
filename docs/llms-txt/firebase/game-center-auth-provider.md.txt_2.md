# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/game-center-auth-provider.md.txt

# firebase::auth::GameCenterAuthProvider Class Reference

# firebase::auth::GameCenterAuthProvider


`#include <credential.h>`

GameCenter (Apple) auth provider.

## Summary

| ### Public static attributes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/game-center-auth-provider#classfirebase_1_1auth_1_1_game_center_auth_provider_1a9139fca14c3e2daa5777221c1d79a358` | `const char *const` The string used to identify this provider. |

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/game-center-auth-provider#classfirebase_1_1auth_1_1_game_center_auth_provider_1a6f8aaecaa1c4ff81e057de69a20cc2b3()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential >` Generate a credential from GameCenter for the current user. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/game-center-auth-provider#classfirebase_1_1auth_1_1_game_center_auth_provider_1a67f2b1e97aeeec6ebbcc082b64473c6a()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential >` Get the result of the most recent [GetCredential()](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/game-center-auth-provider#classfirebase_1_1auth_1_1_game_center_auth_provider_1a6f8aaecaa1c4ff81e057de69a20cc2b3) call. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/auth/game-center-auth-provider#classfirebase_1_1auth_1_1_game_center_auth_provider_1ab56ee9c4d887bc7207c03579dd6a5796()` | `bool` Tests to see if the current user is signed in to GameCenter. |

## Public static attributes

### kProviderId

```c++
const char *const kProviderId
```
The string used to identify this provider.

## Public static functions

### GetCredential

```c++
Future< Credential > GetCredential()
```
Generate a credential from GameCenter for the current user.

<br />

| Details ||
|---|---|
| **Returns** | a [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) that will be fulfilled with the resulting credential. |

### GetCredentialLastResult

```c++
Future< Credential > GetCredentialLastResult()
```
Get the result of the most recent [GetCredential()](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/game-center-auth-provider#classfirebase_1_1auth_1_1_game_center_auth_provider_1a6f8aaecaa1c4ff81e057de69a20cc2b3) call.

<br />

| Details ||
|---|---|
| **Returns** | an object which can be used to retrieve the [Credential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential). |

### IsPlayerAuthenticated

```c++
bool IsPlayerAuthenticated()
```
Tests to see if the current user is signed in to GameCenter.

<br />

| Details ||
|---|---|
| **Returns** | true if the user is signed in, false otherwise. |