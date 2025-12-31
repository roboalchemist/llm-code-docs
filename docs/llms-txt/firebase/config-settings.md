# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-settings.md.txt

# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/remote-config/config-settings.md.txt

# Firebase.RemoteConfig.ConfigSettings Struct Reference

# Firebase.RemoteConfig.ConfigSettings

Settings for [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config) operations.

## Summary

|                                                                                                                                                                                                                 ### Properties                                                                                                                                                                                                                 ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FetchTimeoutInMilliseconds](https://firebase.google.com/docs/reference/unity/struct/firebase/remote-config/config-settings#struct_firebase_1_1_remote_config_1_1_config_settings_1a35df0caae275b6e9a435103683cad318)         | `ulong` The timeout specifies how long the client should wait for a connection to the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) Remote Config servers. |
| [MinimumFetchIntervalInMilliseconds](https://firebase.google.com/docs/reference/unity/struct/firebase/remote-config/config-settings#struct_firebase_1_1_remote_config_1_1_config_settings_1a36842ef254edd1cbc583f9aa8a78ed4c) | `ulong` The minimum interval between successive fetch calls.                                                                                                                                                    |

## Properties

### FetchTimeoutInMilliseconds

```c#
ulong Firebase::RemoteConfig::ConfigSettings::FetchTimeoutInMilliseconds
```  
The timeout specifies how long the client should wait for a connection to the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) Remote Config servers.


| **Note:** A fetch call will fail if it takes longer than the specified timeout to connect to the Remote Config servers. Default is 60 seconds.

<br />

### MinimumFetchIntervalInMilliseconds

```c#
ulong Firebase::RemoteConfig::ConfigSettings::MinimumFetchIntervalInMilliseconds
```  
The minimum interval between successive fetch calls.


| **Note:** Fetches less than duration seconds after the last fetch from the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) Remote Config server would use values returned during the last fetch. Default is 12 hours.

<br />