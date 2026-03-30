# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config.md.txt

# firebase::remote_config::RemoteConfig Class Reference

# firebase::remote_config::RemoteConfig


`#include <remote_config.h>`

Entry point for the Firebase C++ SDK for Remote Config.

## Summary

To use the SDK, call [firebase::remote_config::RemoteConfig::GetInstance()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1aefccefa735e8a592afeea18c4b4fe2ed) to obtain an instance of [RemoteConfig](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config), then call operations on that instance. The instance contains the complete set of FRC parameter values available to your app. The instance also stores values fetched from the FRC Server until they are made available for use with a call to [Activate()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a0be275ba1e04183d1ea475f021c968e9).

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a56cbbc42ea0052fc8a678c325fe5a1a9()` ||

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a0be275ba1e04183d1ea475f021c968e9()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< bool >` Asynchronously activates the most recently fetched configs, so that the fetched key value pairs take effect. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a896b4bae5190950f373f634f225e7e14()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< bool >` Get the (possibly still pending) results of the most recent [Activate()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a0be275ba1e04183d1ea475f021c968e9) call. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a3377907581f92851adfc5a2bd25d23b3(std::function< void(https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-update#structfirebase_1_1remote__config_1_1_config_update &&, https://firebase.google.com/docs/reference/cpp/namespace/firebase/remote-config#namespacefirebase_1_1remote__config_1a4f37bb4a75b0df5dc85cd38222dbc3a2)> config_update_listener)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/config-update-listener-registration#classfirebase_1_1remote__config_1_1_config_update_listener_registration` Starts listening for real-time config updates from the Remote Config backend and automatically fetches updates from the RC backend when they are available. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a5cfaf599440718c3a3587c6c21db88f1()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-info#structfirebase_1_1remote__config_1_1_config_info >` Returns a [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) that contains [ConfigInfo](https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-info#structfirebase_1_1remote__config_1_1_config_info) representing the initialization status of this Firebase Remote Config instance. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a17f57e3793adb73e38786e5f4caf5ddc()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-info#structfirebase_1_1remote__config_1_1_config_info >` Get the (possibly still pending) results of the most recent [EnsureInitialized()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a5cfaf599440718c3a3587c6c21db88f1) call. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a220a9869e6d1ce757159264ab8a8c184()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Fetches config data from the server. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a250db32ad3234ae10a32746ba197bbf9(uint64_t cache_expiration_in_seconds)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Fetches config data from the server. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1ae058180592e4218e063bc3f4871b1344()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< bool >` Asynchronously fetches and then activates the fetched configs. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a15b46cf6492a2a4899024c32de647e74()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< bool >` Get the (possibly still pending) results of the most recent [FetchAndActivate()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1ae058180592e4218e063bc3f4871b1344) call. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1ad70c0b48bb0c573b5766fe1e112c436a()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Get the (possibly still pending) results of the most recent [Fetch()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a220a9869e6d1ce757159264ab8a8c184) call. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a8127c1edbe74405007826d0f4c6c0ba6()` | `std::map< std::string, https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant >` Returns a Map of Firebase Remote Config key value pairs. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a740b3902a7296a2f430240f020b4c545(const char *key)` | `bool` Returns the value associated with a key, converted to a bool. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a5b0d6c6c2e045aa8cbed949748dcdc83(const char *key, https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/value-info#structfirebase_1_1remote__config_1_1_value_info *info)` | `bool` Returns the value associated with a key, converted to a bool. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1ac66398c152730b884483a68e8a1272aa()` | `https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-settings#structfirebase_1_1remote__config_1_1_config_settings` Gets the current settings of the [RemoteConfig](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config) object. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a3d3ca21d8594fbd931523e15b5e249a1(const char *key)` | `std::vector< unsigned char >` Returns the value associated with a key, as a vector of raw byte-data. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a9af8fb6694a679ef47601495f2850bcc(const char *key, https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/value-info#structfirebase_1_1remote__config_1_1_value_info *info)` | `std::vector< unsigned char >` Returns the value associated with a key, as a vector of raw byte-data. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1aeb6dc379aef6243e944e6592b4a34ffc(const char *key)` | `double` Returns the value associated with a key, converted to a double. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1ad384d427fae94006781a190820171a75(const char *key, https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/value-info#structfirebase_1_1remote__config_1_1_value_info *info)` | `double` Returns the value associated with a key, converted to a double. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a4be8dbac74bc25422c0619c0d219d398()` | `const https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-info#structfirebase_1_1remote__config_1_1_config_info` Returns information about the last fetch request, in the form of a [ConfigInfo](https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-info#structfirebase_1_1remote__config_1_1_config_info) struct. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1ab31a6760fd0b97801b1920462a9937b0()` | `std::vector< std::string >` Gets the set of all keys. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1aeebc5a5caa6a757723b9f32a94c87c33(const char *prefix)` | `std::vector< std::string >` Gets the set of keys that start with the given prefix. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a1b376e125df82c8bc61b6e4686896122(const char *key)` | `int64_t` Returns the value associated with a key, converted to a 64-bit integer. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1ab42f1de76b688ba0dd19a33c7fc41b92(const char *key, https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/value-info#structfirebase_1_1remote__config_1_1_value_info *info)` | `int64_t` Returns the value associated with a key, converted to a 64-bit integer. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a2a0912229bc6bede3dd11cfe381f7886(const char *key)` | `std::string` Returns the value associated with a key, converted to a string. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1ae485c87013d322c5d322288a9de7b843(const char *key, https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/value-info#structfirebase_1_1remote__config_1_1_value_info *info)` | `std::string` Returns the value associated with a key, converted to a string. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a539b7bea8717032e94486d558150ea5b(https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-settings#structfirebase_1_1remote__config_1_1_config_settings settings)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Asynchronously changes the settings for this Remote Config instance. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1aa706488b5a57cf158b480aa019d27f2d()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Get the (possibly still pending) results of the most recent [SetConfigSettings()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a539b7bea8717032e94486d558150ea5b) call. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1ad897741b34971d8d1c354d9fdc3812e8(const https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-key-value-variant#structfirebase_1_1remote__config_1_1_config_key_value_variant *defaults, size_t number_of_defaults)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Sets the default values based on a mapping of string to [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a7f575870b7c92739dbe4ba76e61947f6(const https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-key-value#structfirebase_1_1remote__config_1_1_config_key_value *defaults, size_t number_of_defaults)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Sets the default values based on a string map. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a37df46007ad1c605b5c5f7697c78b2be()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< void >` Get the (possibly still pending) results of the most recent [SetDefaults()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1ad897741b34971d8d1c354d9fdc3812e8) call. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a91446780cd7ba297d637a2568e01b562()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app *` Gets the [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) this remote config object is connected to. |

| ### Public static functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1aefccefa735e8a592afeea18c4b4fe2ed(https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app *app)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config *` Returns the [RemoteConfig](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config) object for an [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app). |

## Public functions

### Activate

```c++
Future< bool > Activate()
```
Asynchronously activates the most recently fetched configs, so that the fetched key value pairs take effect.

<br />

| Details ||
|---|---|
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) that contains true if fetched configs were activated. The future will contain false if the configs were already activated. |

### ActivateLastResult

```c++
Future< bool > ActivateLastResult()
```
Get the (possibly still pending) results of the most recent [Activate()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a0be275ba1e04183d1ea475f021c968e9) call.

<br />

| Details ||
|---|---|
| **Returns** | The future result from the last call to [Activate()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a0be275ba1e04183d1ea475f021c968e9). |

### AddOnConfigUpdateListener

```c++
ConfigUpdateListenerRegistration AddOnConfigUpdateListener(
  std::function< void(ConfigUpdate &&, RemoteConfigError)> config_update_listener
)
```
Starts listening for real-time config updates from the Remote Config backend and automatically fetches updates from the RC backend when they are available.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `config_update_listener` | An event handler callback that can be used to respond to config updates when they're fetched | |
| **Returns** | A registration object that allows the listener to remove the associated listener. |

### EnsureInitialized

```c++
Future< ConfigInfo > EnsureInitialized()
```
Returns a [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) that contains [ConfigInfo](https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-info#structfirebase_1_1remote__config_1_1_config_info) representing the initialization status of this Firebase Remote Config instance.

Use this method to ensure Set/Get call not being blocked.

### EnsureInitializedLastResult

```c++
Future< ConfigInfo > EnsureInitializedLastResult()
```
Get the (possibly still pending) results of the most recent [EnsureInitialized()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a5cfaf599440718c3a3587c6c21db88f1) call.

<br />

| Details ||
|---|---|
| **Returns** | The future result from the last call to [EnsureInitialized()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a5cfaf599440718c3a3587c6c21db88f1). |

### Fetch

```c++
Future< void > Fetch()
```
Fetches config data from the server.

<br />

> [!NOTE]
> **Note:** This does not actually apply the data or make it accessible, it merely retrieves it and caches it. To accept and access the newly retrieved values, you must call [Activate()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a0be275ba1e04183d1ea475f021c968e9).

Note that this function is asynchronous, and will normally take an unspecified amount of time before completion.

<br />

<br />

| Details ||
|---|---|
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) which can be used to determine when the fetch is complete. |

### Fetch

```c++
Future< void > Fetch(
  uint64_t cache_expiration_in_seconds
)
```
Fetches config data from the server.


> [!NOTE]
> **Note:** This does not actually apply the data or make it accessible, it merely retrieves it and caches it. To accept and access the newly retrieved values, you must call [Activate()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a0be275ba1e04183d1ea475f021c968e9). Note that this function is asynchronous, and will normally take an unspecified amount of time before completion.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `cache_expiration_in_seconds` | The number of seconds to keep previously fetch data available. If cached data is available that is newer than cache_expiration_in_seconds, then the function returns immediately and does not fetch any data. A cache_expiration_in_seconds of zero will always cause a fetch. | |
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) which can be used to determine when the fetch is complete. |

### FetchAndActivate

```c++
Future< bool > FetchAndActivate()
```
Asynchronously fetches and then activates the fetched configs.

If the time elapsed since the last fetch from the Firebase Remote Config backend is more than the default minimum fetch interval, configs are fetched from the backend.

After the fetch is complete, the configs are activated so that the fetched key value pairs take effect.

<br />

| Details ||
|---|---|
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) that contains true if the current call activated the fetched configs; if no configs were fetched from the backend and the local fetched configs have already been activated, the future will contain false. |

### FetchAndActivateLastResult

```c++
Future< bool > FetchAndActivateLastResult()
```
Get the (possibly still pending) results of the most recent [FetchAndActivate()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1ae058180592e4218e063bc3f4871b1344) call.

<br />

| Details ||
|---|---|
| **Returns** | The future result from the last call to [FetchAndActivate()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1ae058180592e4218e063bc3f4871b1344). |

### FetchLastResult

```c++
Future< void > FetchLastResult()
```
Get the (possibly still pending) results of the most recent [Fetch()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a220a9869e6d1ce757159264ab8a8c184) call.

<br />

| Details ||
|---|---|
| **Returns** | The future result from the last call to [Fetch()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a220a9869e6d1ce757159264ab8a8c184). |

### GetAll

```c++
std::map< std::string, Variant > GetAll()
```
Returns a Map of Firebase Remote Config key value pairs.

Evaluates the values of the parameters in the following order: The activated value, if the last successful [Activate()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a0be275ba1e04183d1ea475f021c968e9) contained the key. The default value, if the key was set with [SetDefaults()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1ad897741b34971d8d1c354d9fdc3812e8).

### GetBoolean

```c++
bool GetBoolean(
  const char *key
)
```
Returns the value associated with a key, converted to a bool.

Values of "1", "true", "t", "yes", "y" and "on" are interpreted (case insensitive) as `true` and "0", "false", "f", "no", "n", "off", and empty strings are interpreted (case insensitive) as `false`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `key` | Key of the value to be retrieved. | |
| **Returns** | Value associated with the specified key converted to a boolean value. |

### GetBoolean

```c++
bool GetBoolean(
  const char *key,
  ValueInfo *info
)
```
Returns the value associated with a key, converted to a bool.

Values of "1", "true", "t", "yes", "y" and "on" are interpreted (case insensitive) as `true` and "0", "false", "f", "no", "n", "off", and empty strings are interpreted (case insensitive) as `false`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `key` | Key of the value to be retrieved. | | `info` | A return value, specifying the source of the returned value. | |
| **Returns** | Value associated with the specified key converted to a boolean value. |

### GetConfigSettings

```c++
ConfigSettings GetConfigSettings()
```
Gets the current settings of the [RemoteConfig](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config) object.

<br />

| Details ||
|---|---|
| **Returns** | A [ConfigSettings](https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-settings#structfirebase_1_1remote__config_1_1_config_settings) struct. |

### GetData

```c++
std::vector< unsigned char > GetData(
  const char *key
)
```
Returns the value associated with a key, as a vector of raw byte-data.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `key` | Key of the value to be retrieved. | |
| **Returns** | Vector of bytes. |

### GetData

```c++
std::vector< unsigned char > GetData(
  const char *key,
  ValueInfo *info
)
```
Returns the value associated with a key, as a vector of raw byte-data.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `key` | Key of the value to be retrieved. | | `info` | A return value, specifying the source of the returned value. | |
| **Returns** | Vector of bytes. |

### GetDouble

```c++
double GetDouble(
  const char *key
)
```
Returns the value associated with a key, converted to a double.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `key` | Key of the value to be retrieved. | |
| **Returns** | Value associated with the specified key converted to a double. |

### GetDouble

```c++
double GetDouble(
  const char *key,
  ValueInfo *info
)
```
Returns the value associated with a key, converted to a double.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `key` | Key of the value to be retrieved. | | `info` | A return value, specifying the source of the returned value. | |
| **Returns** | Value associated with the specified key converted to a double. |

### GetInfo

```c++
const ConfigInfo GetInfo()
```
Returns information about the last fetch request, in the form of a [ConfigInfo](https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-info#structfirebase_1_1remote__config_1_1_config_info) struct.

<br />

| Details ||
|---|---|
| **Returns** | A [ConfigInfo](https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-info#structfirebase_1_1remote__config_1_1_config_info) struct, containing fields reflecting the state of the most recent fetch request. |

### GetKeys

```c++
std::vector< std::string > GetKeys()
```
Gets the set of all keys.

<br />

| Details ||
|---|---|
| **Returns** | Set of all Remote Config parameter keys. |

### GetKeysByPrefix

```c++
std::vector< std::string > GetKeysByPrefix(
  const char *prefix
)
```
Gets the set of keys that start with the given prefix.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `prefix` | The key prefix to look for. If empty or null, this method will return all keys. | |
| **Returns** | Set of Remote Config parameter keys that start with the specified prefix. Will return an empty set if there are no keys with the given prefix. |

### GetLong

```c++
int64_t GetLong(
  const char *key
)
```
Returns the value associated with a key, converted to a 64-bit integer.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `key` | Key of the value to be retrieved. | |
| **Returns** | Value associated with the specified key converted to a 64-bit integer. |

### GetLong

```c++
int64_t GetLong(
  const char *key,
  ValueInfo *info
)
```
Returns the value associated with a key, converted to a 64-bit integer.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `key` | Key of the value to be retrieved. | | `info` | A return value, specifying the source of the returned value. | |
| **Returns** | Value associated with the specified key converted to a 64-bit integer. |

### GetString

```c++
std::string GetString(
  const char *key
)
```
Returns the value associated with a key, converted to a string.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `key` | Key of the value to be retrieved. | |
| **Returns** | Value as a string associated with the specified key. |

### GetString

```c++
std::string GetString(
  const char *key,
  ValueInfo *info
)
```
Returns the value associated with a key, converted to a string.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `key` | Key of the value to be retrieved. | | `info` | A return value, specifying the source of the returned value. | |
| **Returns** | Value as a string associated with the specified key. |

### SetConfigSettings

```c++
Future< void > SetConfigSettings(
  ConfigSettings settings
)
```
Asynchronously changes the settings for this Remote Config instance.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `settings` | The new settings to be applied. | |
| **Returns** | a [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) which can be used to determine when the operation is complete. |

### SetConfigSettingsLastResult

```c++
Future< void > SetConfigSettingsLastResult()
```
Get the (possibly still pending) results of the most recent [SetConfigSettings()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a539b7bea8717032e94486d558150ea5b) call.

<br />

| Details ||
|---|---|
| **Returns** | The future result from the last call to [SetConfigSettings()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a539b7bea8717032e94486d558150ea5b). |

### SetDefaults

```c++
Future< void > SetDefaults(
  const ConfigKeyValueVariant *defaults,
  size_t number_of_defaults
)
```
Sets the default values based on a mapping of string to [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant).

This allows you to specify defaults of type other than string.

The type of each [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) in the map determines the type of data for which you are providing a default. For example, boolean values can be retrieved with GetBool(), integer values can be retrieved with [GetLong()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a1b376e125df82c8bc61b6e4686896122), double values can be retrieved with [GetDouble()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1aeb6dc379aef6243e944e6592b4a34ffc), string values can be retrieved with [GetString()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a2a0912229bc6bede3dd11cfe381f7886), and binary data can be retrieved with [GetData()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1a3d3ca21d8594fbd931523e15b5e249a1). Aggregate [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) types are not allowed.

**See also:** [firebase::Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) for more information on how to create a [Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) of each type.

> [!NOTE]
> **Note:** This completely overrides all previous values.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `defaults` | Array of [ConfigKeyValueVariant](https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-key-value-variant#structfirebase_1_1remote__config_1_1_config_key_value_variant), representing the new set of defaults to apply. If the same key is specified multiple times, the value associated with the last duplicate key is applied. | | `number_of_defaults` | Number of elements in the defaults array. | |
| **Returns** | a [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) which can be used to determine when the operation is complete. |

### SetDefaults

```c++
Future< void > SetDefaults(
  const ConfigKeyValue *defaults,
  size_t number_of_defaults
)
```
Sets the default values based on a string map.


> [!NOTE]
> **Note:** This completely overrides all previous values.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `defaults` | Array of [ConfigKeyValue](https://firebase.google.com/docs/reference/cpp/struct/firebase/remote-config/config-key-value#structfirebase_1_1remote__config_1_1_config_key_value), representing the new set of defaults to apply. If the same key is specified multiple times, the value associated with the last duplicate key is applied. | | `number_of_defaults` | Number of elements in the defaults array. | |
| **Returns** | a [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) which can be used to determine when the operation is complete. |

### SetDefaultsLastResult

```c++
Future< void > SetDefaultsLastResult()
```
Get the (possibly still pending) results of the most recent [SetDefaults()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1ad897741b34971d8d1c354d9fdc3812e8) call.

<br />

| Details ||
|---|---|
| **Returns** | The future result from the last call to [SetDefaults()](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config_1ad897741b34971d8d1c354d9fdc3812e8). |

### app

```c++
App * app()
```
Gets the [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) this remote config object is connected to.

### \~RemoteConfig

```c++
 ~RemoteConfig()
```

## Public static functions

### GetInstance

```c++
RemoteConfig * GetInstance(
  App *app
)
```
Returns the [RemoteConfig](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config) object for an [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app).

Creates the [RemoteConfig](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config) if required.

To get the [RemoteConfig](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config) object for the default app, use, GetInstance(GetDefaultFirebaseApp());

If the library [RemoteConfig](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config) fails to initialize, init_result_out will be written with the result status (if a pointer is given).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `app` | The [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) to use for the [RemoteConfig](https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config#classfirebase_1_1remote__config_1_1_remote_config) object. | |