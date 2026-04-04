# Source: https://firebase.google.com/docs/reference/unity/namespace/firebase/remote-config.md.txt

# Firebase.RemoteConfig Namespace

# Firebase.RemoteConfig

## Summary

| ### Enumerations ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/namespace/firebase/remote-config#namespace_firebase_1_1_remote_config_1a41e00bf8ed5b155fb433f5173212787b{ https://firebase.google.com/docs/reference/unity/namespace/firebase/remote-config#namespace_firebase_1_1_remote_config_1a41e00bf8ed5b155fb433f5173212787ba4bbb8f967da6d1a610596d7257179c2b, https://firebase.google.com/docs/reference/unity/namespace/firebase/remote-config#namespace_firebase_1_1_remote_config_1a41e00bf8ed5b155fb433f5173212787baca7bd438b66e51a7c4a108f471b9f18f, https://firebase.google.com/docs/reference/unity/namespace/firebase/remote-config#namespace_firebase_1_1_remote_config_1a41e00bf8ed5b155fb433f5173212787ba902b0d55fddef6f8d651fe1035b7d4bd }` | enumDescribes the most recent fetch failure. |
| `https://firebase.google.com/docs/reference/unity/namespace/firebase/remote-config#namespace_firebase_1_1_remote_config_1a36d228a1957619a925e1f9f5363e316e{ https://firebase.google.com/docs/reference/unity/namespace/firebase/remote-config#namespace_firebase_1_1_remote_config_1a36d228a1957619a925e1f9f5363e316ea505a83f220c02df2f85c3810cd9ceb38, https://firebase.google.com/docs/reference/unity/namespace/firebase/remote-config#namespace_firebase_1_1_remote_config_1a36d228a1957619a925e1f9f5363e316eae139a585510a502bbf1841cf589f5086, https://firebase.google.com/docs/reference/unity/namespace/firebase/remote-config#namespace_firebase_1_1_remote_config_1a36d228a1957619a925e1f9f5363e316ea2d13df6f8b5e4c5af9f87e0dc39df69d }` | enumDescribes the most recent fetch request status. |
| `https://firebase.google.com/docs/reference/unity/namespace/firebase/remote-config#namespace_firebase_1_1_remote_config_1aa509491114e6bcdfef90b19513a74693` | enumDescribes the error codes returned by Remote Config. |
| `https://firebase.google.com/docs/reference/unity/namespace/firebase/remote-config#namespace_firebase_1_1_remote_config_1a2f4f400ab2b2d9f09a147439cd0c5ca2{ https://firebase.google.com/docs/reference/unity/namespace/firebase/remote-config#namespace_firebase_1_1_remote_config_1a2f4f400ab2b2d9f09a147439cd0c5ca2a9ede99e889aee3d8a6641e111676259e, https://firebase.google.com/docs/reference/unity/namespace/firebase/remote-config#namespace_firebase_1_1_remote_config_1a2f4f400ab2b2d9f09a147439cd0c5ca2ac9d8182d28a17e32d17b2630638e2043, https://firebase.google.com/docs/reference/unity/namespace/firebase/remote-config#namespace_firebase_1_1_remote_config_1a2f4f400ab2b2d9f09a147439cd0c5ca2a47650c07c124a01fcd3206d452ce6a1c }` | enumDescribes the source a config value was retrieved from. |

| ### Classes ||
|---|---|
| [Firebase.RemoteConfig.ConfigInfo](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/config-info) | Describes the state of the most recent Fetch() call. |
| [Firebase.RemoteConfig.ConfigUpdateEventArgs](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/config-update-event-args) |   |
| [Firebase.RemoteConfig.FirebaseRemoteConfig](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config) | Entry point for the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) C# SDK for Remote Config. |

| ### Structs ||
|---|---|
| [Firebase.RemoteConfig.ConfigSettings](https://firebase.google.com/docs/reference/unity/struct/firebase/remote-config/config-settings) | Settings for [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config) operations. |
| [Firebase.RemoteConfig.ConfigValue](https://firebase.google.com/docs/reference/unity/struct/firebase/remote-config/config-value) | Wrapper for a Remote Config parameter value, with methods to get it as different types, such as bools and doubles, along with information about where the data came from. |

## Enumerations

### FetchFailureReason

```c#
 FetchFailureReason
```
Describes the most recent fetch failure.

| Properties ||
|---|---|
| `Error` | The most recent fetch failed for an unknown reason. |
| `Invalid` | The fetch has not yet failed. |
| `Throttled` | The most recent fetch failed because it was throttled by the server. (You are sending too many fetch requests in too short a time.) |

### LastFetchStatus

```c#
 LastFetchStatus
```
Describes the most recent fetch request status.

| Properties ||
|---|---|
| `Failure` | The most recent fetch request failed. |
| `Pending` | The most recent fetch is still in progress. |
| `Success` | The most recent fetch was a success, and its data is ready to be applied, if you have not already done so. |

### RemoteConfigError

```c#
 RemoteConfigError
```
Describes the error codes returned by Remote Config.

### ValueSource

```c#
 ValueSource
```
Describes the source a config value was retrieved from.

| Properties ||
|---|---|
| `DefaultValue` | The value was not specified, so the specified default value was returned instead. |
| `RemoteValue` | The value was found in the remote data store, and returned. |
| `StaticValue` | The value was not specified and no default was specified, so a static value (0 for numeric values, an empty string for strings) was returned. |