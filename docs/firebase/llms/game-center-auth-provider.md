# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/game-center-auth-provider.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/auth/game-center-auth-provider.md.txt

# Firebase.Auth.GameCenterAuthProvider Class Reference

# Firebase.Auth.GameCenterAuthProvider

GameCenter (Apple) auth provider.

## Summary

|                                                                                                     ### Properties                                                                                                     ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| [ProviderId](https://firebase.google.com/docs/reference/unity/class/firebase/auth/game-center-auth-provider#class_firebase_1_1_auth_1_1_game_center_auth_provider_1a9160bc8cea3e595b7206584fe66d195f) | `static string` |

|                                                                                                                                                                                  ### Public static functions                                                                                                                                                                                  ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GetCredentialAsync](https://firebase.google.com/docs/reference/unity/class/firebase/auth/game-center-auth-provider#class_firebase_1_1_auth_1_1_game_center_auth_provider_1a7511b533d7b602ac7a967810cc09b42f)`()`    | `System.Threading.Tasks.Task< `[Credential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/credential#class_firebase_1_1_auth_1_1_credential)` >` |
| [IsPlayerAuthenticated](https://firebase.google.com/docs/reference/unity/class/firebase/auth/game-center-auth-provider#class_firebase_1_1_auth_1_1_game_center_auth_provider_1a16a9d53d6acdaacef2e218964b62981a)`()` | `bool`                                                                                                                                                                  |

## Properties

### ProviderId

```c#
static string ProviderId
```  

## Public static functions

### GetCredentialAsync

```c#
System.Threading.Tasks.Task< Credential > GetCredentialAsync()
```  

### IsPlayerAuthenticated

```c#
bool IsPlayerAuthenticated()
```