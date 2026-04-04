# Source: https://firebase.google.com/docs/reference/unity/class/firebase/auth/play-games-auth-provider.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/play-games-auth-provider.md.txt

# firebase::auth::PlayGamesAuthProvider Class Reference

# firebase::auth::PlayGamesAuthProvider


`#include <credential.h>`

Use a server auth code provided by Google Play Games to authenticate.

## Summary

|                                                                                                                   ### Public static attributes                                                                                                                   ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| [kProviderId](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/play-games-auth-provider#classfirebase_1_1auth_1_1_play_games_auth_provider_1a4eae8bef113eb523a4d3689a6ebe5fe2) | `const char *const` The string used to identify this provider. |

|                                                                                                                                                                                                                                                      ### Public static functions                                                                                                                                                                                                                                                      ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GetCredential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/play-games-auth-provider#classfirebase_1_1auth_1_1_play_games_auth_provider_1a57ec99c1ef5ff2f077de4d54ae295f53)`(const char *server_auth_code)` | [Credential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential) Generate a credential from the given Server [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) Code. |

## Public static attributes

### kProviderId

```c++
const char *const kProviderId
```  
The string used to identify this provider.

## Public static functions

### GetCredential

```c++
Credential GetCredential(
  const char *server_auth_code
)
```  
Generate a credential from the given Server [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) Code.

<br />

|                                                                                                                                                                           Details                                                                                                                                                                            ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |--------------------|------------------------------------------------------------------------------------------------------------------------------------------------| | `server_auth_code` | Play Games Sign in Server [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) Code. | |
| **Returns** | New [Credential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential).                                                                                                                                                                                                           |