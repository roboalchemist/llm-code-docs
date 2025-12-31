# Source: https://firebase.google.com/docs/reference/js/remote-config.remoteconfigsettings.md.txt

# RemoteConfigSettings interface

Defines configuration options for the Remote Config SDK.

**Signature:**  

    export interface RemoteConfigSettings 

## Properties

|                                                                             Property                                                                             |  Type  |                                                                         Description                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [fetchTimeoutMillis](https://firebase.google.com/docs/reference/js/remote-config.remoteconfigsettings.md#remoteconfigsettingsfetchtimeoutmillis)                 | number | Defines the maximum amount of milliseconds to wait for a response when fetching configuration from the Remote Config server. Defaults to 60000 (One minute). |
| [minimumFetchIntervalMillis](https://firebase.google.com/docs/reference/js/remote-config.remoteconfigsettings.md#remoteconfigsettingsminimumfetchintervalmillis) | number | Defines the maximum age in milliseconds of an entry in the config cache before it is considered stale. Defaults to 43200000 (Twelve hours).                  |

## RemoteConfigSettings.fetchTimeoutMillis

Defines the maximum amount of milliseconds to wait for a response when fetching configuration from the Remote Config server. Defaults to 60000 (One minute).

**Signature:**  

    fetchTimeoutMillis: number;

## RemoteConfigSettings.minimumFetchIntervalMillis

Defines the maximum age in milliseconds of an entry in the config cache before it is considered stale. Defaults to 43200000 (Twelve hours).

**Signature:**  

    minimumFetchIntervalMillis: number;