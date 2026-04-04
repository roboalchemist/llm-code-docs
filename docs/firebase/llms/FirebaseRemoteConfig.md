# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig.md.txt

# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig.md.txt

# FirebaseRemoteConfig

# FirebaseRemoteConfig


```
class FirebaseRemoteConfig
```

<br />

*** ** * ** ***

Entry point for the Firebase Remote Config API.

Callers should first get the singleton object using [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getInstance()), and then call operations on that singleton object. The singleton contains the complete set of Remote Config parameter values available to your app. The singleton also stores values fetched from the Remote Config server until they are made available for use with a call to [activate](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#activate()).

## Summary

|                                                                                   ### Constants                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `const `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                         | [DEFAULT_VALUE_FOR_BOOLEAN](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#DEFAULT_VALUE_FOR_BOOLEAN())` = false` The static default boolean value for any given key.                                                                                                    |
| `const `[ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)`<`[Byte](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte/index.html)`>!` | [DEFAULT_VALUE_FOR_BYTE_ARRAY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#DEFAULT_VALUE_FOR_BYTE_ARRAY()) The static default byte array value for any given key.                                                                                                     |
| `const `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)                                                                                           | [DEFAULT_VALUE_FOR_DOUBLE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#DEFAULT_VALUE_FOR_DOUBLE())` = 0.0` The static default double value for any given key.                                                                                                         |
| `const `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)                                                                                               | [DEFAULT_VALUE_FOR_LONG](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#DEFAULT_VALUE_FOR_LONG())` = 0` The static default long value for any given key.                                                                                                                 |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                                                                        | [DEFAULT_VALUE_FOR_STRING](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#DEFAULT_VALUE_FOR_STRING())` = ""` The static default string value for any given key.                                                                                                          |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                 | [LAST_FETCH_STATUS_FAILURE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#LAST_FETCH_STATUS_FAILURE())` = 1` Indicates that the most recent attempt to fetch parameter values from the Firebase Remote Config server has failed.                                        |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                 | [LAST_FETCH_STATUS_NO_FETCH_YET](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#LAST_FETCH_STATUS_NO_FETCH_YET())` = 0` Indicates that the FirebaseRemoteConfig singleton object has not yet attempted to fetch parameter values from the Firebase Remote Config server. |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                 | [LAST_FETCH_STATUS_SUCCESS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#LAST_FETCH_STATUS_SUCCESS())` = -1` Indicates that the most recent fetch of parameter values from the Firebase Remote Config server was completed successfully.                               |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                 | [LAST_FETCH_STATUS_THROTTLED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#LAST_FETCH_STATUS_THROTTLED())` = 2` Indicates that the most recent attempt to fetch parameter values from the Firebase Remote Config server was throttled.                                 |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                 | [VALUE_SOURCE_DEFAULT](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#VALUE_SOURCE_DEFAULT())` = 1` Indicates that the value returned was retrieved from the defaults set by the client.                                                                                 |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                 | [VALUE_SOURCE_REMOTE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#VALUE_SOURCE_REMOTE())` = 2` Indicates that the value returned was retrieved from the Firebase Remote Config server.                                                                                |
| `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                 | [VALUE_SOURCE_STATIC](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#VALUE_SOURCE_STATIC())` = 0` Indicates that the value returned is the static default value.                                                                                                         |

|                                                                                                                                                                                                        ### Public functions                                                                                                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`!>`                                                                                                                                                                                                                                             | [activate](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#activate())`()` Asynchronously activates the most recently fetched configs, so that the fetched key value pairs take effect.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListenerRegistration)                                                                                                                                                                                                                                                                             | [addOnConfigUpdateListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#addOnConfigUpdateListener(com.google.firebase.remoteconfig.ConfigUpdateListener))`(configUpdateListener: `[ConfigUpdateListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListener)`)` Starts listening for real-time config updates from the Remote Config backend and automatically fetches updates from the RC backend when they are available.                                                                                                                                                                 |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[FirebaseRemoteConfigInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo)`!>`                                                                                                                                                                                        | [ensureInitialized](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#ensureInitialized())`()` Returns a [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) representing the initialization status of this Firebase Remote Config instance.                                                                                                                                                                                                                                                                                                                                                                |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>`                                                                                                                                                                                                                                                     | [fetch](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#fetch())`()` Starts fetching configs, adhering to the default minimum fetch interval.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>`                                                                                                                                                                                                                                                     | [fetch](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#fetch(long))`(minimumFetchIntervalInSeconds: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)`)` Starts fetching configs, adhering to the specified minimum fetch interval.                                                                                                                                                                                                                                                                                                                                                                                     |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`!>`                                                                                                                                                                                                                                             | [fetchAndActivate](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#fetchAndActivate())`()` Asynchronously fetches and then activates the fetched configs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!, `[FirebaseRemoteConfigValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue)`!>` | [getAll](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getAll())`()` Returns a [Map](https://developer.android.com/reference/kotlin/java/util/Map.html) of Firebase Remote Config key value pairs.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                                                                                                                                                                                                                                                                                  | [getBoolean](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getBoolean(java.lang.String))`(key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns the parameter value for the given key as a `boolean`.                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)                                                                                                                                                                                                                                                                                                                                                    | [getDouble](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getDouble(java.lang.String))`(key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns the parameter value for the given key as a `double`.                                                                                                                                                                                                                                                                                                                                                                                                     |
| [FirebaseRemoteConfigInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo)                                                                                                                                                                                                                                                                                             | [getInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getInfo())`()` Returns the state of this [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig) instance as a [FirebaseRemoteConfigInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo).                                                                                                                                                                                                                                                            |
| `java-static `[FirebaseRemoteConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig)                                                                                                                                                                                                                                                                                       | [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getInstance())`()` Returns a singleton instance of Firebase Remote Config.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `java-static `[FirebaseRemoteConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig)                                                                                                                                                                                                                                                                                       | [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getInstance(com.google.firebase.FirebaseApp))`(app: `[FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)`)` Returns an instance of Firebase Remote Config for the given [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp).                                                                                                                                                                                                                                                                 |
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)`)`[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!>`                                                                                                                                               | [getKeysByPrefix](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getKeysByPrefix(java.lang.String))`(prefix: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns a [Set](https://developer.android.com/reference/kotlin/java/util/Set.html) of all Firebase Remote Config parameter keys with the given prefix.                                                                                                                                                                                                                                                                                            |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)                                                                                                                                                                                                                                                                                                                                                        | [getLong](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getLong(java.lang.String))`(key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns the parameter value for the given key as a `long`.                                                                                                                                                                                                                                                                                                                                                                                                           |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                                                                                                                                                                                                                                                                                    | [getString](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getString(java.lang.String))`(key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns the parameter value for the given key as a [String](https://developer.android.com/reference/kotlin/java/lang/String.html).                                                                                                                                                                                                                                                                                                                               |
| [FirebaseRemoteConfigValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue)                                                                                                                                                                                                                                                                                           | [getValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getValue(java.lang.String))`(key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns the parameter value for the given key as a [FirebaseRemoteConfigValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue).                                                                                                                                                                                                                                                                      |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>`                                                                                                                                                                                                                                                     | [reset](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#reset())`()` Deletes all activated, fetched and defaults configs and resets all Firebase Remote Config settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>`                                                                                                                                                                                                                                                     | [setConfigSettingsAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setConfigSettingsAsync(com.google.firebase.remoteconfig.FirebaseRemoteConfigSettings))`(settings: `[FirebaseRemoteConfigSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings)`)` Asynchronously changes the settings for this [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig) instance.                                                                                                                                |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>`                                                                                                                                                                                                                                                     | [setCustomSignals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setCustomSignals(com.google.firebase.remoteconfig.CustomSignals))`(customSignals: `[CustomSignals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals)`)` Asynchronously changes the custom signals for this [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig) instance.                                                                                                                                                                              |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>`                                                                                                                                                                                                                                                     | [setDefaultsAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setDefaultsAsync(java.util.Map<java.lang.String,java.lang.Object>))`(defaults: (`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!, `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>)` Asynchronously sets default configs using the given [Map](https://developer.android.com/reference/kotlin/java/util/Map.html). |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>`                                                                                                                                                                                                                                                     | [setDefaultsAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setDefaultsAsync(int))`(resourceId: @`[XmlRes](https://developer.android.com/reference/kotlin/androidx/annotation/XmlRes.html)` `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`)` Sets default configs using an XML resource.                                                                                                                                                                                                                                                                                                                        |

|                                                               ### Extension functions                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `operator `[FirebaseRemoteConfigValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue) | [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig)`.`[get](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#(com.google.firebase.remoteconfig.FirebaseRemoteConfig).get(kotlin.String))`(key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` See FirebaseRemoteConfig#getValue |

|                                                                                                          ### Extension properties                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)`<`[ConfigUpdate](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdate)`>` | [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig)`.`[configUpdates](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#(com.google.firebase.remoteconfig.FirebaseRemoteConfig).configUpdates()) Starts listening for config updates from the Remote Config backend and emits [ConfigUpdate](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdate)s via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html). |

## Constants

### DEFAULT_VALUE_FOR_BOOLEAN

```
constÂ valÂ DEFAULT_VALUE_FOR_BOOLEAN = false:Â Boolean
```

The static default boolean value for any given key.  

### DEFAULT_VALUE_FOR_BYTE_ARRAY

```
constÂ valÂ DEFAULT_VALUE_FOR_BYTE_ARRAY:Â ByteArray<Byte>!
```

The static default byte array value for any given key.  

### DEFAULT_VALUE_FOR_DOUBLE

```
constÂ valÂ DEFAULT_VALUE_FOR_DOUBLE = 0.0:Â Double
```

The static default double value for any given key.  

### DEFAULT_VALUE_FOR_LONG

```
constÂ valÂ DEFAULT_VALUE_FOR_LONG = 0:Â Long
```

The static default long value for any given key.  

### DEFAULT_VALUE_FOR_STRING

```
constÂ valÂ DEFAULT_VALUE_FOR_STRING = "":Â String!
```

The static default string value for any given key.  

### LAST_FETCH_STATUS_FAILURE

```
constÂ valÂ LAST_FETCH_STATUS_FAILURE = 1:Â Int
```

Indicates that the most recent attempt to fetch parameter values from the Firebase Remote Config server has failed.  

### LAST_FETCH_STATUS_NO_FETCH_YET

```
constÂ valÂ LAST_FETCH_STATUS_NO_FETCH_YET = 0:Â Int
```

Indicates that the FirebaseRemoteConfig singleton object has not yet attempted to fetch parameter values from the Firebase Remote Config server.  

### LAST_FETCH_STATUS_SUCCESS

```
constÂ valÂ LAST_FETCH_STATUS_SUCCESS = -1:Â Int
```

Indicates that the most recent fetch of parameter values from the Firebase Remote Config server was completed successfully.  

### LAST_FETCH_STATUS_THROTTLED

```
constÂ valÂ LAST_FETCH_STATUS_THROTTLED = 2:Â Int
```

Indicates that the most recent attempt to fetch parameter values from the Firebase Remote Config server was throttled.  

### VALUE_SOURCE_DEFAULT

```
constÂ valÂ VALUE_SOURCE_DEFAULT = 1:Â Int
```

Indicates that the value returned was retrieved from the defaults set by the client.  

### VALUE_SOURCE_REMOTE

```
constÂ valÂ VALUE_SOURCE_REMOTE = 2:Â Int
```

Indicates that the value returned was retrieved from the Firebase Remote Config server.  

### VALUE_SOURCE_STATIC

```
constÂ valÂ VALUE_SOURCE_STATIC = 0:Â Int
```

Indicates that the value returned is the static default value.  

## Public functions

### activate

```
funÂ activate():Â Task<Boolean!>
```

Asynchronously activates the most recently fetched configs, so that the fetched key value pairs take effect.  

|                                                                                         Returns                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`!>` | [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) with a `true` result if the current call activated the fetched configs; if the fetched configs were already activated by a previous call, it instead returns a [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) with a `false` result. |

### addOnConfigUpdateListener

```
funÂ addOnConfigUpdateListener(configUpdateListener:Â ConfigUpdateListener):Â ConfigUpdateListenerRegistration
```

Starts listening for real-time config updates from the Remote Config backend and automatically fetches updates from the RC backend when they are available.

If a connection to the Remote Config backend is not already open, calling this method will open it. Multiple listeners can be added by calling this method again, but subsequent calls re-use the same connection to the backend.

Note: Real-time Remote Config requires the Firebase Remote Config Realtime API. See the [Remote Config Get Started](https://firebase.google.com/docs/remote-config/get-started?platform=android#add-real-time-listener) guide to enable the API.  

|                                                                       Parameters                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `configUpdateListener: `[ConfigUpdateListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListener) | A [ConfigUpdateListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListener) that can be used to respond to config updates when they're fetched. |

|                                                                         Returns                                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListenerRegistration) | A [ConfigUpdateListenerRegistration](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListenerRegistration) that allows you to remove the added ` configUpdateListener` and close the connection when there are no more listeners. |

### ensureInitialized

```
funÂ ensureInitialized():Â Task<FirebaseRemoteConfigInfo!>
```

Returns a [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) representing the initialization status of this Firebase Remote Config instance.  

### fetch

```
funÂ fetch():Â Task<Void!>
```

Starts fetching configs, adhering to the default minimum fetch interval.

The fetched configs only take effect after the next [activate](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#activate()) call.

Depending on the time elapsed since the last fetch from the Firebase Remote Config backend, configs are either served from local storage, or fetched from the backend. The default minimum fetch interval can be set with `
FirebaseRemoteConfigSettings.Builder#setMinimumFetchIntervalInSeconds(long)`; the static default is 12 hours.

Note: Also initializes the Firebase installations SDK that creates installation IDs to identify Firebase installations and periodically sends data to Firebase servers. Remote Config requires installation IDs for Fetch requests. To stop the periodic sync, call [delete](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations#delete()). Sending a Fetch request after deletion will create a new installation ID for this Firebase installation and resume the periodic sync.  

|                                                                                     Returns                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) representing the `fetch` call. |

### fetch

```
funÂ fetch(minimumFetchIntervalInSeconds:Â Long):Â Task<Void!>
```

Starts fetching configs, adhering to the specified minimum fetch interval.

The fetched configs only take effect after the next [activate](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#activate()) call.

Depending on the time elapsed since the last fetch from the Firebase Remote Config backend, configs are either served from local storage, or fetched from the backend.

Note: Also initializes the Firebase installations SDK that creates installation IDs to identify Firebase installations and periodically sends data to Firebase servers. Remote Config requires installation IDs for Fetch requests. To stop the periodic sync, call [delete](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations#delete()). Sending a Fetch request after deletion will create a new installation ID for this Firebase installation and resume the periodic sync.  

|                                                  Parameters                                                   |
|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| `minimumFetchIntervalInSeconds: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | If configs in the local storage were fetched more than this many seconds ago, configs are served from the backend instead of local storage. |

|                                                                                     Returns                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) representing the `fetch` call. |

### fetchAndActivate

```
funÂ fetchAndActivate():Â Task<Boolean!>
```

Asynchronously fetches and then activates the fetched configs.

If the time elapsed since the last fetch from the Firebase Remote Config backend is more than the default minimum fetch interval, configs are fetched from the backend.

After the fetch is complete, the configs are activated so that the fetched key value pairs take effect.  

|                                                                                         Returns                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`!>` | [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) with a `true` result if the current call activated the fetched configs; if no configs were fetched from the backend and the local fetched configs have already been activated, returns a [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) with a `false` result. |

### getAll

```
funÂ getAll():Â (Mutable)Map<String!,Â FirebaseRemoteConfigValue!>
```

Returns a [Map](https://developer.android.com/reference/kotlin/java/util/Map.html) of Firebase Remote Config key value pairs.

Evaluates the values of the parameters in the following order:

1. The activated value, if the last successful [activate](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#activate()) contained the key.
2. The default value, if the key was set with [setDefaultsAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setDefaultsAsync(java.util.Map<java.lang.String,java.lang.Object>)).  

### getBoolean

```
funÂ getBoolean(key:Â String):Â Boolean
```

Returns the parameter value for the given key as a `boolean`.

Evaluates the value of the parameter in the following order:

1. The activated value, if the last successful [activate](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#activate()) contained the key, and the value can be converted into a `boolean`.
2. The default value, if the key was set with [setDefaultsAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setDefaultsAsync(java.util.Map<java.lang.String,java.lang.Object>)), and the value can be converted into a `boolean`.
3. [DEFAULT_VALUE_FOR_BOOLEAN](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#DEFAULT_VALUE_FOR_BOOLEAN()).

"1", "true", "t", "yes", "y", and "on" are strings that are interpreted (case insensitive) as `true`, and "0", "false", "f", "no", "n", "off", and empty string are interpreted (case insensitive) as `false`.  

|                                       Parameters                                        |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | A Firebase Remote Config parameter key with a `boolean` parameter value. |

|                                      Returns                                       |
|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | `boolean` representing the value of the Firebase Remote Config parameter with the given key. |

### getDouble

```
funÂ getDouble(key:Â String):Â Double
```

Returns the parameter value for the given key as a `double`.

Evaluates the value of the parameter in the following order:

1. The activated value, if the last successful [activate](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#activate()) contained the key, and the value can be converted into a `double`.
2. The default value, if the key was set with [setDefaultsAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setDefaultsAsync(java.util.Map<java.lang.String,java.lang.Object>)), and the value can be converted into a `double`.
3. [DEFAULT_VALUE_FOR_DOUBLE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#DEFAULT_VALUE_FOR_DOUBLE()).

|                                       Parameters                                        |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | A Firebase Remote Config parameter key with a `double` parameter value. |

|                                     Returns                                      |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html) | `double` representing the value of the Firebase Remote Config parameter with the given key. |

### getInfo

```
funÂ getInfo():Â FirebaseRemoteConfigInfo
```

Returns the state of this [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig) instance as a [FirebaseRemoteConfigInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo).  

### getInstance

```
java-staticÂ funÂ getInstance():Â FirebaseRemoteConfig
```

Returns a singleton instance of Firebase Remote Config.

[FirebaseRemoteConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig) uses the default [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp), throwing an [IllegalStateException](https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html) if one has not been initialized yet.

Note: Also initializes the Firebase installations SDK that creates installation IDs to identify Firebase installations and periodically sends data to Firebase servers. Remote Config requires installation IDs for Fetch requests. To stop the periodic sync, call [delete](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations#delete()). Sending a Fetch request after deletion will create a new installation ID for this Firebase installation and resume the periodic sync.  

|                                                             Returns                                                             |
|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig) | A singleton instance of [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig) for the default [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp). |

### getInstance

```
java-staticÂ funÂ getInstance(app:Â FirebaseApp):Â FirebaseRemoteConfig
```

Returns an instance of Firebase Remote Config for the given [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp).  

### getKeysByPrefix

```
funÂ getKeysByPrefix(prefix:Â String):Â (Mutable)Set<String!>
```

Returns a [Set](https://developer.android.com/reference/kotlin/java/util/Set.html) of all Firebase Remote Config parameter keys with the given prefix.  

|                                         Parameters                                         |
|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| `prefix: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The key prefix to look for. If the prefix is empty, all keys are returned. |

|                                                                                                                                        Returns                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)`)`[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!>` | [Set](https://developer.android.com/reference/kotlin/java/util/Set.html) of Remote Config parameter keys that start with the specified prefix. |

### getLong

```
funÂ getLong(key:Â String):Â Long
```

Returns the parameter value for the given key as a `long`.

Evaluates the value of the parameter in the following order:

1. The activated value, if the last successful [activate](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#activate()) contained the key, and the value can be converted into a `long`.
2. The default value, if the key was set with [setDefaultsAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setDefaultsAsync(java.util.Map<java.lang.String,java.lang.Object>)), and the value can be converted into a `long`.
3. [DEFAULT_VALUE_FOR_LONG](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#DEFAULT_VALUE_FOR_LONG()).

|                                       Parameters                                        |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| `key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | A Firebase Remote Config parameter key with a `long` parameter value. |

|                                   Returns                                    |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | `long` representing the value of the Firebase Remote Config parameter with the given key. |

### getString

```
funÂ getString(key:Â String):Â String
```

Returns the parameter value for the given key as a [String](https://developer.android.com/reference/kotlin/java/lang/String.html).

Evaluates the value of the parameter in the following order:

1. The activated value, if the last successful [activate](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#activate()) contained the key.
2. The default value, if the key was set with [setDefaultsAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setDefaultsAsync(java.util.Map<java.lang.String,java.lang.Object>)).
3. [DEFAULT_VALUE_FOR_STRING](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#DEFAULT_VALUE_FOR_STRING()).

|                                       Parameters                                        |
|-----------------------------------------------------------------------------------------|-----------------------------------------|
| `key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | A Firebase Remote Config parameter key. |

|                                     Returns                                      |
|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [String](https://developer.android.com/reference/kotlin/java/lang/String.html) representing the value of the Firebase Remote Config parameter with the given key. |

### getValue

```
funÂ getValue(key:Â String):Â FirebaseRemoteConfigValue
```

Returns the parameter value for the given key as a [FirebaseRemoteConfigValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue).

Evaluates the value of the parameter in the following order:

1. The activated value, if the last successful [activate](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#activate()) contained the key.
2. The default value, if the key was set with [setDefaultsAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setDefaultsAsync(java.util.Map<java.lang.String,java.lang.Object>)).
3. A [FirebaseRemoteConfigValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue) that returns the static value for each type.

|                                       Parameters                                        |
|-----------------------------------------------------------------------------------------|-----------------------------------------|
| `key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | A Firebase Remote Config parameter key. |

|                                                                  Returns                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseRemoteConfigValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue) | [FirebaseRemoteConfigValue](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue) representing the value of the Firebase Remote Config parameter with the given key. |

### reset

```
funÂ reset():Â Task<Void!>
```

Deletes all activated, fetched and defaults configs and resets all Firebase Remote Config settings.  

|                                                                                     Returns                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)`!>` | [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) representing the `clear` call. |

### setConfigSettingsAsync

```
funÂ setConfigSettingsAsync(settings:Â FirebaseRemoteConfigSettings):Â Task<Void!>
```

Asynchronously changes the settings for this [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig) instance.  

|                                                                         Parameters                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| `settings: `[FirebaseRemoteConfigSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings) | The new settings to be applied. |

### setCustomSignals

```
funÂ setCustomSignals(customSignals:Â CustomSignals):Â Task<Void!>
```

Asynchronously changes the custom signals for this [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig) instance.

Custom signals are subject to limits on the size of key/value pairs and the total number of signals. Any calls that exceed these limits will be discarded. See [Custom Signal Limits](https://firebase.google.com/docs/remote-config/parameters?template_type=client#custom-signal-limits).  

|                                                             Parameters                                                             |
|------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `customSignals: `[CustomSignals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals) | The custom signals to set for this instance. - New keys will add new key-value pairs in the custom signals. - Existing keys with new values will update the corresponding signals. - Setting a key's value to `null` will remove the associated signal. |

### setDefaultsAsync

```
funÂ setDefaultsAsync(defaults:Â (Mutable)Map<String!,Â Any!>):Â Task<Void!>
```

Asynchronously sets default configs using the given [Map](https://developer.android.com/reference/kotlin/java/util/Map.html).

The values in `defaults` must be one of the following types:

- `byte[]`
- `Boolean`
- `Double`
- `Long`
- `String`

|                                                                                                                                                                                   Parameters                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `defaults: (`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!, `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>` | [Map](https://developer.android.com/reference/kotlin/java/util/Map.html) of key value pairs representing Firebase Remote Config parameter keys and values. |

### setDefaultsAsync

```
funÂ setDefaultsAsync(resourceId:Â @XmlRes Int):Â Task<Void!>
```

Sets default configs using an XML resource.  

|                                                                                      Parameters                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| `resourceId: @`[XmlRes](https://developer.android.com/reference/kotlin/androidx/annotation/XmlRes.html)` `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | Id for the XML resource, which should be in your application's ` res/xml` folder. |

## Extension functions

### get

```
operatorÂ funÂ FirebaseRemoteConfig.get(key:Â String):Â FirebaseRemoteConfigValue
```

See FirebaseRemoteConfig#getValue  

## Extension properties

### configUpdates

```
valÂ FirebaseRemoteConfig.configUpdates:Â Flow<ConfigUpdate>
```

Starts listening for config updates from the Remote Config backend and emits [ConfigUpdate](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdate)s via a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html). See [FirebaseRemoteConfig.addOnConfigUpdateListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#addOnConfigUpdateListener(com.google.firebase.remoteconfig.ConfigUpdateListener)) for more information.

- When the returned flow starts being collected, an [ConfigUpdateListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListener) will be attached.

- When the flow completes, the listener will be removed. If there are no attached listeners, the connection to the Remote Config backend will be closed.