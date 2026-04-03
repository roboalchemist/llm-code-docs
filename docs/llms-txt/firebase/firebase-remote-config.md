# Source: https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config.md.txt

# Firebase.RemoteConfig.FirebaseRemoteConfig Class Reference

# Firebase.RemoteConfig.FirebaseRemoteConfig

Entry point for the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) C# SDK for Remote Config.

## Summary

|                                                                                                                                                                                                                                                                                                                                                                                            ### Properties                                                                                                                                                                                                                                                                                                                                                                                             ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AllValues](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1a459c517c9cbb06df40d6a67f97300f60)                    | `IDictionary< string, `[ConfigValue](https://firebase.google.com/docs/reference/unity/struct/firebase/remote-config/config-value#struct_firebase_1_1_remote_config_1_1_config_value)` >` Returns a Dictionary of [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) Remote Config key value pairs.                                                                                                                                                                                                               |
| [App](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1a114806c9bbd3749bb2b26d22519c84cf)                          | [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) App object associated with this [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config).                                                                                                                                                                                                            |
| [ConfigSettings](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1a7b1a4f987f7f64d965e4c3b7a560d7ef)               | [ConfigSettings](https://firebase.google.com/docs/reference/unity/struct/firebase/remote-config/config-settings#struct_firebase_1_1_remote_config_1_1_config_settings) Gets the current settings of the [RemoteConfig](https://firebase.google.com/docs/reference/unity/namespace/firebase/remote-config#namespace_firebase_1_1_remote_config) object.                                                                                                                                                                                                           |
| [DefaultCacheExpiration](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1a7cd1c5067fe16f01f5cc3afe98a785bc)       | `static TimeSpan` The default cache expiration used by [FetchAsync()](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1a55b6f0ebc2b457e9c0e2ac7c52cc87fa), equal to 12 hours.                                                                                                                                                                                                                                                                   |
| [DefaultInstance](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1a3807422399a1e94cf3d81d771ff73495)              | `static `[FirebaseRemoteConfig](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config) Returns the [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config) initialized with the default [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app). |
| [DefaultTimeoutInMilliseconds](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1ae6061b14c79984b71b1c143333ea3445) | `static ulong` The default timeout used by [FetchAsync()](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1a55b6f0ebc2b457e9c0e2ac7c52cc87fa), equal to 30 seconds, in milliseconds.                                                                                                                                                                                                                                                            |
| [Info](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1a8ce23c52f5daff7292cd61cf25a053cf)                         | [ConfigInfo](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/config-info#class_firebase_1_1_remote_config_1_1_config_info) Returns information about the last fetch request, in the form of a [ConfigInfo](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/config-info#class_firebase_1_1_remote_config_1_1_config_info) object.                                                                                                                                                                     |
| [Keys](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1a2e2c6d3c9457912b47008ccca1bf9d8a)                         | `IEnumerable< string >` Gets the set of all Remote Config parameter keys.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [OnConfigUpdateListener](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1a0e48f203277a442100d3c1bd246f9499)       | `EventHandler< `[ConfigUpdateEventArgs](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/config-update-event-args#class_firebase_1_1_remote_config_1_1_config_update_event_args)` >`                                                                                                                                                                                                                                                                                                                                                |

|                                                                                                                                                                                                                                                                                                                                                                                                                               ### Public static functions                                                                                                                                                                                                                                                                                                                                                                                                                               ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GetInstance](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1a89acb21ce9577b6c16866c696930c7f6)`(`[FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app)` app)` | [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config) Returns a [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config), initialized with a custom [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) App. |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ### Public functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ActivateAsync](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1ac8959dadb409990ec73bca36daa5e920)`()`                                                                                                                                                                                           | `System.Threading.Tasks.Task< bool >` Asynchronously activates the most recently fetched configs, so that the fetched key value pairs take effect.                                                                                                                                                                                                                                                                                                                                                                                                                |
| [EnsureInitializedAsync](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1a74064e1519e5fc8c43ac913447e9267b)`()`                                                                                                                                                                                  | `async System.Threading.Tasks.Task< `[ConfigInfo](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/config-info#class_firebase_1_1_remote_config_1_1_config_info)` >` Returns a Task that contains [ConfigInfo](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/config-info#class_firebase_1_1_remote_config_1_1_config_info) representing the initialization status of this [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) Remote Config instance. |
| [FetchAndActivateAsync](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1ac09912b4b4a6b0f0b4e5744bf41dfc36)`()`                                                                                                                                                                                   | `Task< bool >` Asynchronously fetches and then activates the fetched configs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [FetchAsync](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1a55b6f0ebc2b457e9c0e2ac7c52cc87fa)`()`                                                                                                                                                                                              | `Task` Fetches config data from the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [FetchAsync](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1a392cb7d51e204473c2a43a742a934219)`(TimeSpan cacheExpiration)`                                                                                                                                                                      | `System.Threading.Tasks.Task` Fetches config data from the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [GetKeysByPrefix](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1acbee7940d840287397e78ad7939db503)`(string prefix)`                                                                                                                                                                            | `IEnumerable< string >` Gets the set of keys that start with the given prefix.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [GetValue](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1a851b25e295df00db60ad36fe05be2f2c)`(string key)`                                                                                                                                                                                      | [ConfigValue](https://firebase.google.com/docs/reference/unity/struct/firebase/remote-config/config-value#struct_firebase_1_1_remote_config_1_1_config_value) Gets the [ConfigValue](https://firebase.google.com/docs/reference/unity/struct/firebase/remote-config/config-value#struct_firebase_1_1_remote_config_1_1_config_value) corresponding to the key.                                                                                                                                                                                                    |
| [SetConfigSettingsAsync](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1a6022a0bcdfb8d5a8d734193bbe561076)`(`[ConfigSettings](https://firebase.google.com/docs/reference/unity/struct/firebase/remote-config/config-settings#struct_firebase_1_1_remote_config_1_1_config_settings)` settings)` | `Task` Asynchronously changes the settings for this Remote Config instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [SetDefaultsAsync](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1aee74c93e439d654f0be5ec84b9a6a878)`(IDictionary< string, object > defaults)`                                                                                                                                                  | `Task` Sets the default values based on a string to object dictionary.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

## Properties

### AllValues

```c#
IDictionary< string, ConfigValue > AllValues
```  
Returns a Dictionary of [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) Remote Config key value pairs.

Evaluates the values of the parameters in the following order: The activated value, if the last successful [ActivateAsync()](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1ac8959dadb409990ec73bca36daa5e920) contained the key. The default value, if the key was set with [SetDefaultsAsync()](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1aee74c93e439d654f0be5ec84b9a6a878).  

### App

```c#
FirebaseApp App
```  
App object associated with this [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config).  

### ConfigSettings

```c#
ConfigSettings ConfigSettings
```  
Gets the current settings of the [RemoteConfig](https://firebase.google.com/docs/reference/unity/namespace/firebase/remote-config#namespace_firebase_1_1_remote_config) object.  

### DefaultCacheExpiration

```c#
static TimeSpan DefaultCacheExpiration
```  
The default cache expiration used by [FetchAsync()](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1a55b6f0ebc2b457e9c0e2ac7c52cc87fa), equal to 12 hours.  

### DefaultInstance

```c#
static FirebaseRemoteConfig DefaultInstance
```  
Returns the [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config) initialized with the default [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app).  

### DefaultTimeoutInMilliseconds

```c#
static ulong DefaultTimeoutInMilliseconds
```  
The default timeout used by [FetchAsync()](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1a55b6f0ebc2b457e9c0e2ac7c52cc87fa), equal to 30 seconds, in milliseconds.  

### Info

```c#
ConfigInfo Info
```  
Returns information about the last fetch request, in the form of a [ConfigInfo](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/config-info#class_firebase_1_1_remote_config_1_1_config_info) object.  

### Keys

```c#
IEnumerable< string > Keys
```  
Gets the set of all Remote Config parameter keys.  

### OnConfigUpdateListener

```c#
EventHandler< ConfigUpdateEventArgs > OnConfigUpdateListener
```  

## Public static functions

### GetInstance

```c#
FirebaseRemoteConfig GetInstance(
  FirebaseApp app
)
```  
Returns a [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config), initialized with a custom [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) App.

app The customer [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) used for initialization.

<br />

|                                                                                                      Details                                                                                                      ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config) instance. |

## Public functions

### ActivateAsync

```c#
System.Threading.Tasks.Task< bool > ActivateAsync()
```  
Asynchronously activates the most recently fetched configs, so that the fetched key value pairs take effect.

<br />

|                                                                   Details                                                                    ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A Task that contains true if fetched configs were activated. The Task will contain false if the configs were already activated. |

### EnsureInitializedAsync

```c#
async System.Threading.Tasks.Task< ConfigInfo > EnsureInitializedAsync()
```  
Returns a Task that contains [ConfigInfo](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/config-info#class_firebase_1_1_remote_config_1_1_config_info) representing the initialization status of this [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) Remote Config instance.

Use this method to ensure Set/Get call not being blocked.

<br />

|                                                                                        Details                                                                                         ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A Task contains [ConfigInfo](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/config-info#class_firebase_1_1_remote_config_1_1_config_info). |

### FetchAndActivateAsync

```c#
Task< bool > FetchAndActivateAsync()
```  
Asynchronously fetches and then activates the fetched configs.

If the time elapsed since the last fetch from the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) Remote Config backend is more than the default minimum fetch interval, configs are fetched from the backend.

After the fetch is complete, the configs are activated so that the fetched key value pairs take effect.

<br />

|                                                                                  Details                                                                                  ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A Task that contains true if the call activated the fetched configs. The Task will contain false if the fetch failed, or the configs were already activated. |

### FetchAsync

```c#
Task FetchAsync()
```  
Fetches config data from the server.


| **Note:** This does not actually apply the data or make it accessible, it merely retrieves it and caches it. To accept and access the newly retrieved values, you must call [ActivateAsync()](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1ac8959dadb409990ec73bca36daa5e920). Note that this function is asynchronous, and will normally take an unspecified amount of time before completion.

<br />

|                                    Details                                     ||
|-------------|-------------------------------------------------------------------|
| **Returns** | A Task which can be used to determine with the fetch is complete. |

### FetchAsync

```c#
System.Threading.Tasks.Task FetchAsync(
  TimeSpan cacheExpiration
)
```  
Fetches config data from the server.


| **Note:** This does not actually apply the data or make it accessible, it merely retrieves it and caches it. To accept and access the newly retrieved values, you must call [ActivateAsync()](https://firebase.google.com/docs/reference/unity/class/firebase/remote-config/firebase-remote-config#class_firebase_1_1_remote_config_1_1_firebase_remote_config_1ac8959dadb409990ec73bca36daa5e920). Note that this function is asynchronous, and will normally take an unspecified amount of time before completion.

<br />

|                                                                                                                                                                                                                                                                               Details                                                                                                                                                                                                                                                                                ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `cacheExpiration` | The amount of time to keep previously fetch data available. If cached data is available that is newer than cacheExpiration, then the function returns immediately and does not fetch any data. A cacheExpiration of zero will always cause a fetch. | |
| **Returns** | A Task which can be used to determine with the fetch is complete.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

### GetKeysByPrefix

```c#
IEnumerable< string > GetKeysByPrefix(
  string prefix
)
```  
Gets the set of keys that start with the given prefix.

<br />

|                                                                                                  Details                                                                                                   ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |----------|---------------------------------------------------------------------------------| | `prefix` | The key prefix to look for. If empty or null, this method will return all keys. | |
| **Returns** | Set of Remote Config parameter keys that start with the specified prefix. Will return an empty set if there are no keys with the given prefix.                                                |

### GetValue

```c#
ConfigValue GetValue(
  string key
)
```  
Gets the [ConfigValue](https://firebase.google.com/docs/reference/unity/struct/firebase/remote-config/config-value#struct_firebase_1_1_remote_config_1_1_config_value) corresponding to the key.

<br />

|                                                                                                 Details                                                                                                 ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-------|-----------------------------------| | `key` | Key of the value to be retrieved. |                                                                                                |
| **Returns** | The [ConfigValue](https://firebase.google.com/docs/reference/unity/struct/firebase/remote-config/config-value#struct_firebase_1_1_remote_config_1_1_config_value) associated with the key. |

### SetConfigSettingsAsync

```c#
Task SetConfigSettingsAsync(
  ConfigSettings settings
)
```  
Asynchronously changes the settings for this Remote Config instance.

<br />

|                                                    Details                                                     ||
|-------------|---------------------------------------------------------------------------------------------------|
| Parameters  | |------------|---------------------------------| | `settings` | The new settings to be applied. | |
| **Returns** | a Task which can be used to determine when the operation is complete.                             |

### SetDefaultsAsync

```c#
Task SetDefaultsAsync(
  IDictionary< string, object > defaults
)
```  
Sets the default values based on a string to object dictionary.


| **Note:** This completely overrides all previous values.

<br />

|                                                                                                                                                                                                                   Details                                                                                                                                                                                                                    ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `defaults` | IDictionary of string keys to values, representing the new set of defaults to apply. If the same key is specified multiple times, the value associated with the last duplicate key is applied. | |
| **Returns** | A Task which can be used to determine when the operation is complete.                                                                                                                                                                                                                                                                                                                                                           |