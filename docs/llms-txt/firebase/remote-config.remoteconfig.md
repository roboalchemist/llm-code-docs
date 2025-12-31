# Source: https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md.txt

# RemoteConfig interface

The Firebase Remote Config service interface.

**Signature:**  

    export interface RemoteConfig 

## Properties

|                                                          Property                                                          |                                                                    Type                                                                    |                                                                                                                                 Description                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [app](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfigapp)                         | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface)                                      | The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) this `RemoteConfig` instance is associated with.                                                                                                                   |
| [defaultConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfigdefaultconfig)     | { \[key: string\]: string \| number \| boolean; }                                                                                          | Object containing default values for configs.                                                                                                                                                                                                                                |
| [fetchTimeMillis](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfigfetchtimemillis) | number                                                                                                                                     | The Unix timestamp in milliseconds of the last *successful* fetch, or negative one if the [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) instance either hasn't fetched or initialization is incomplete. |
| [lastFetchStatus](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfiglastfetchstatus) | [FetchStatus](https://firebase.google.com/docs/reference/js/remote-config.md#fetchstatus)                                                  | The status of the last fetch *attempt*.                                                                                                                                                                                                                                      |
| [settings](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfigsettings)               | [RemoteConfigSettings](https://firebase.google.com/docs/reference/js/remote-config.remoteconfigsettings.md#remoteconfigsettings_interface) | Defines configuration for the Remote Config SDK.                                                                                                                                                                                                                             |

## RemoteConfig.app

The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) this `RemoteConfig` instance is associated with.

**Signature:**  

    app: FirebaseApp;

## RemoteConfig.defaultConfig

Object containing default values for configs.

**Signature:**  

    defaultConfig: {
            [key: string]: string | number | boolean;
        };

## RemoteConfig.fetchTimeMillis

The Unix timestamp in milliseconds of the last *successful* fetch, or negative one if the [RemoteConfig](https://firebase.google.com/docs/reference/js/remote-config.remoteconfig.md#remoteconfig_interface) instance either hasn't fetched or initialization is incomplete.

**Signature:**  

    fetchTimeMillis: number;

## RemoteConfig.lastFetchStatus

The status of the last fetch *attempt*.

**Signature:**  

    lastFetchStatus: FetchStatus;

## RemoteConfig.settings

Defines configuration for the Remote Config SDK.

**Signature:**  

    settings: RemoteConfigSettings;