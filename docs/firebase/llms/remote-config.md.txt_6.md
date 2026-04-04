# Source: https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config.md.txt

# firebase::remote_config Namespace

# firebase::remote_config

Firebase Remote Config API.

## Summary

Firebase Remote Config is a cloud service that lets you change the appearance and behavior of your app without requiring users to download an app update.

| ### Enumerations ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#namespacefirebase_1_1remote__config_1abd312db12a2f0c9ad1f6907ec2c04434{ https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#namespacefirebase_1_1remote__config_1abd312db12a2f0c9ad1f6907ec2c04434abece739c9d1b23d8b0138f3cf2e69c92 }` | enumKeys of API settings. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#namespacefirebase_1_1remote__config_1a6fb05ff71e1e4820f002ccaf7d0b2968{ https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#namespacefirebase_1_1remote__config_1a6fb05ff71e1e4820f002ccaf7d0b2968a4d5611568fe6fbb8fe2b8939bad625c3, https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#namespacefirebase_1_1remote__config_1a6fb05ff71e1e4820f002ccaf7d0b2968af3d06dd83cdc950ffe07be7f4890e57c, https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#namespacefirebase_1_1remote__config_1a6fb05ff71e1e4820f002ccaf7d0b2968a254de71033d93c33d32d20d9de5cc666 }` | enumDescribes the most recent fetch failure. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#namespacefirebase_1_1remote__config_1ac0e46414bf605c3cfaac1c6f370d586a{ https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#namespacefirebase_1_1remote__config_1ac0e46414bf605c3cfaac1c6f370d586aa080d33dfe8997c552f749f87867a54b9, https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#namespacefirebase_1_1remote__config_1ac0e46414bf605c3cfaac1c6f370d586aa481fd8f4bb99abefc6d0bf4c00502bc6, https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#namespacefirebase_1_1remote__config_1ac0e46414bf605c3cfaac1c6f370d586aa242ce52eda369bb1b0f1411de469689b }` | enumDescribes the most recent fetch request status. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#namespacefirebase_1_1remote__config_1a4f37bb4a75b0df5dc85cd38222dbc3a2` | enumDescribes the error codes returned by Remote Config. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#namespacefirebase_1_1remote__config_1a825e9930f665960955ee8c7ae071192f{ https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#namespacefirebase_1_1remote__config_1a825e9930f665960955ee8c7ae071192fa2bd211253ca0dd3d85215892c9ff8242, https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#namespacefirebase_1_1remote__config_1a825e9930f665960955ee8c7ae071192fa13c00a32bc4cd3b5f6902dca6e0a2144, https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#namespacefirebase_1_1remote__config_1a825e9930f665960955ee8c7ae071192faa4ee15f9df9c19aa79ea2a0dfb1b480f }` | enumDescribes the source a config value was retrieved from. |

| ### Classes ||
|---|---|
| [firebase::remote_config::ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration) | Calling Remove stops the listener from receiving config updates and unregisters itself. |
| [firebase::remote_config::RemoteConfig](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config) | Entry point for the Firebase C++ SDK for Remote Config. |

| ### Structs ||
|---|---|
| [firebase::remote_config::ConfigInfo](https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-info) | Describes the state of the most recent Fetch() call. |
| [firebase::remote_config::ConfigKeyValue](https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-key-value) | Describes a mapping of a key to a string value. |
| [firebase::remote_config::ConfigKeyValueVariant](https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-key-value-variant) | Describes a mapping of a key to a value of any type. |
| [firebase::remote_config::ConfigSettings](https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-settings) | Configurations for Remote Config behavior. |
| [firebase::remote_config::ConfigUpdate](https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-update) | Information about the updated config. |
| [firebase::remote_config::ValueInfo](https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/value-info) | Describes a retrieved value. |

## Enumerations

### ConfigSetting

```c++
 ConfigSetting
```
Keys of API settings.

**See also:** SetConfigSetting **See also:**GetConfigSetting

| Properties ||
|---|---|
| `kConfigSettingDeveloperMode` | Set the value associated with this key to "1" to enable developer mode (i.e disable throttling) and "0" to disable. |

### FetchFailureReason

```c++
 FetchFailureReason
```
Describes the most recent fetch failure.

| Properties ||
|---|---|
| `kFetchFailureReasonError` | The most recent fetch failed for an unknown reason. |
| `kFetchFailureReasonInvalid` | The fetch has not yet failed. |
| `kFetchFailureReasonThrottled` | The most recent fetch failed because it was throttled by the server. (You are sending too many fetch requests in too short a time.) |

### LastFetchStatus

```c++
 LastFetchStatus
```
Describes the most recent fetch request status.

| Properties ||
|---|---|
| `kLastFetchStatusFailure` | The most recent fetch request failed. |
| `kLastFetchStatusPending` | The most recent fetch is still in progress. |
| `kLastFetchStatusSuccess` | The most recent fetch was a success, and its data is ready to be applied, if you have not already done so. |

### RemoteConfigError

```c++
 RemoteConfigError
```
Describes the error codes returned by Remote Config.

### ValueSource

```c++
 ValueSource
```
Describes the source a config value was retrieved from.

| Properties ||
|---|---|
| `kValueSourceDefaultValue` | The value was not specified, so the specified default value was returned instead. |
| `kValueSourceRemoteValue` | The value was found in the remote data store, and returned. |
| `kValueSourceStaticValue` | The value was not specified and no default was specified, so a static value (0 for numeric values, an empty string for strings) was returned. |