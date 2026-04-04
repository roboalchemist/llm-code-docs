# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-info.md.txt

# firebase::remote_config::ConfigInfo Struct Reference

# firebase::remote_config::ConfigInfo


`#include <remote_config.h>`

Describes the state of the most recent Fetch() call.

## Summary

Normally returned as a result of the GetInfo() function.

| ### Public attributes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-info#structfirebase_1_1remote__config_1_1_config_info_1a353be5e95447fb67de0cf34dc65a7013` | `uint64_t` The time (in milliseconds since the epoch) that the last fetch operation completed. |
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-info#structfirebase_1_1remote__config_1_1_config_info_1aa353fb3a873feeed0c8cee9d57217f7b` | `https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#namespacefirebase_1_1remote__config_1a6fb05ff71e1e4820f002ccaf7d0b2968` The reason the most recent fetch failed. |
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-info#structfirebase_1_1remote__config_1_1_config_info_1a023e7d12118c479ce06c8c07d3d5a1c7` | `https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#namespacefirebase_1_1remote__config_1ac0e46414bf605c3cfaac1c6f370d586a` The status of the last fetch request. |
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-info#structfirebase_1_1remote__config_1_1_config_info_1a9d6def15a09e0f0f2aa38c61c3e9e513` | `uint64_t` The time (in milliseconds since the epoch) when the refreshing of Remote Config data is throttled. |

## Public attributes

### fetch_time

```c++
uint64_t firebase::remote_config::ConfigInfo::fetch_time
```
The time (in milliseconds since the epoch) that the last fetch operation completed.

0 if no fetch attempt has been made yet.

### last_fetch_failure_reason

```c++
FetchFailureReason firebase::remote_config::ConfigInfo::last_fetch_failure_reason
```
The reason the most recent fetch failed.

### last_fetch_status

```c++
LastFetchStatus firebase::remote_config::ConfigInfo::last_fetch_status
```
The status of the last fetch request.

### throttled_end_time

```c++
uint64_t firebase::remote_config::ConfigInfo::throttled_end_time
```
The time (in milliseconds since the epoch) when the refreshing of Remote Config data is throttled.