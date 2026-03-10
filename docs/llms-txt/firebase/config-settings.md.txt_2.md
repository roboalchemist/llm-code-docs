# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-settings.md.txt

# firebase::remote_config::ConfigSettings Struct Reference

# firebase::remote_config::ConfigSettings


`#include <remote_config.h>`

Configurations for Remote Config behavior.

## Summary

| ### Public attributes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-settings#structfirebase_1_1remote__config_1_1_config_settings_1a35d2883e062576bc80a2292400a79a22 = kDefaultTimeoutInMilliseconds` | `uint64_t` The timeout specifies how long the client should wait for a connection to the Firebase Remote Config servers. |
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-settings#structfirebase_1_1remote__config_1_1_config_settings_1ae5e78aa019e31ded1e35ae57137b94f8 = kDefaultCacheExpiration` | `uint64_t` The minimum interval between successive fetch calls. |

## Public attributes

### fetch_timeout_in_milliseconds

```c++
uint64_t firebase::remote_config::ConfigSettings::fetch_timeout_in_milliseconds = kDefaultTimeoutInMilliseconds
```
The timeout specifies how long the client should wait for a connection to the Firebase Remote Config servers.


> [!NOTE]
> **Note:** A fetch call will fail if it takes longer than the specified timeout to connect to the Remote Config servers. Default is 60 seconds.

<br />

### minimum_fetch_interval_in_milliseconds

```c++
uint64_t firebase::remote_config::ConfigSettings::minimum_fetch_interval_in_milliseconds = kDefaultCacheExpiration
```
The minimum interval between successive fetch calls.


> [!NOTE]
> **Note:** Fetches less than duration seconds after the last fetch from the Firebase Remote Config server would use values returned during the last fetch. Default is 12 hours.

<br />