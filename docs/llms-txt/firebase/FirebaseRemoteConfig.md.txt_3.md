# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig.md.txt

# FirebaseRemoteConfig

# FirebaseRemoteConfig


```
class FirebaseRemoteConfig
```

<br />

*** ** * ** ***

Entry point for the Firebase Remote Config API.

Callers should first get the singleton object using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getInstance()`, and then call operations on that singleton object. The singleton contains the complete set of Remote Config parameter values available to your app. The singleton also stores values fetched from the Remote Config server until they are made available for use with a call to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#activate()`.

## Summary

| ### Constants |
|---|---|
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#DEFAULT_VALUE_FOR_BOOLEAN() = false` The static default boolean value for any given key. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte/index.html>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#DEFAULT_VALUE_FOR_BYTE_ARRAY()` The static default byte array value for any given key. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#DEFAULT_VALUE_FOR_DOUBLE() = 0.0` The static default double value for any given key. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#DEFAULT_VALUE_FOR_LONG() = 0` The static default long value for any given key. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#DEFAULT_VALUE_FOR_STRING() = ""` The static default string value for any given key. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#LAST_FETCH_STATUS_FAILURE() = 1` Indicates that the most recent attempt to fetch parameter values from the Firebase Remote Config server has failed. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#LAST_FETCH_STATUS_NO_FETCH_YET() = 0` Indicates that the FirebaseRemoteConfig singleton object has not yet attempted to fetch parameter values from the Firebase Remote Config server. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#LAST_FETCH_STATUS_SUCCESS() = -1` Indicates that the most recent fetch of parameter values from the Firebase Remote Config server was completed successfully. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#LAST_FETCH_STATUS_THROTTLED() = 2` Indicates that the most recent attempt to fetch parameter values from the Firebase Remote Config server was throttled. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#VALUE_SOURCE_DEFAULT() = 1` Indicates that the value returned was retrieved from the defaults set by the client. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#VALUE_SOURCE_REMOTE() = 2` Indicates that the value returned was retrieved from the Firebase Remote Config server. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#VALUE_SOURCE_STATIC() = 0` Indicates that the value returned is the static default value. |

| ### Public functions |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#activate()()` Asynchronously activates the most recently fetched configs, so that the fetched key value pairs take effect. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListenerRegistration` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#addOnConfigUpdateListener(com.google.firebase.remoteconfig.ConfigUpdateListener)(configUpdateListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListener)` Starts listening for real-time config updates from the Remote Config backend and automatically fetches updates from the RC backend when they are available. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#ensureInitialized()()` Returns a `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` representing the initialization status of this Firebase Remote Config instance. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#fetch()()` Starts fetching configs, adhering to the default minimum fetch interval. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#fetch(long)(minimumFetchIntervalInSeconds: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Starts fetching configs, adhering to the specified minimum fetch interval. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#fetchAndActivate()()` Asynchronously fetches and then activates the fetched configs. |
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getAll()()` Returns a `https://developer.android.com/reference/kotlin/java/util/Map.html` of Firebase Remote Config key value pairs. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getBoolean(java.lang.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the parameter value for the given key as a `boolean`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getDouble(java.lang.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the parameter value for the given key as a `double`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getInfo()()` Returns the state of this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` instance as a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo`. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getInstance()()` Returns a singleton instance of Firebase Remote Config. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getInstance(com.google.firebase.FirebaseApp)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` Returns an instance of Firebase Remote Config for the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getKeysByPrefix(java.lang.String)(prefix: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns a `https://developer.android.com/reference/kotlin/java/util/Set.html` of all Firebase Remote Config parameter keys with the given prefix. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getLong(java.lang.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the parameter value for the given key as a `long`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getString(java.lang.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the parameter value for the given key as a `https://developer.android.com/reference/kotlin/java/lang/String.html`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#getValue(java.lang.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the parameter value for the given key as a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue`. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#reset()()` Deletes all activated, fetched and defaults configs and resets all Firebase Remote Config settings. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setConfigSettingsAsync(com.google.firebase.remoteconfig.FirebaseRemoteConfigSettings)(settings: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings)` Asynchronously changes the settings for this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` instance. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setCustomSignals(com.google.firebase.remoteconfig.CustomSignals)(customSignals: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals)` Asynchronously changes the custom signals for this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` instance. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setDefaultsAsync(java.util.Map<java.lang.String,java.lang.Object>)(defaults: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>)` Asynchronously sets default configs using the given `https://developer.android.com/reference/kotlin/java/util/Map.html`. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setDefaultsAsync(int)(resourceId: @https://developer.android.com/reference/kotlin/androidx/annotation/XmlRes.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Sets default configs using an XML resource. |

| ### Extension functions |
|---|---|
| `operator https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#(com.google.firebase.remoteconfig.FirebaseRemoteConfig).get(kotlin.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` See FirebaseRemoteConfig#getValue |

| ### Extension properties |
|---|---|
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdate>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#(com.google.firebase.remoteconfig.FirebaseRemoteConfig).configUpdates()` Starts listening for config updates from the Remote Config backend and emits `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdate`s via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. |

## Constants

### DEFAULT_VALUE_FOR_BOOLEAN

```
const val DEFAULT_VALUE_FOR_BOOLEAN = false: Boolean
```

The static default boolean value for any given key.

### DEFAULT_VALUE_FOR_BYTE_ARRAY

```
const val DEFAULT_VALUE_FOR_BYTE_ARRAY: ByteArray<Byte>!
```

The static default byte array value for any given key.

### DEFAULT_VALUE_FOR_DOUBLE

```
const val DEFAULT_VALUE_FOR_DOUBLE = 0.0: Double
```

The static default double value for any given key.

### DEFAULT_VALUE_FOR_LONG

```
const val DEFAULT_VALUE_FOR_LONG = 0: Long
```

The static default long value for any given key.

### DEFAULT_VALUE_FOR_STRING

```
const val DEFAULT_VALUE_FOR_STRING = "": String!
```

The static default string value for any given key.

### LAST_FETCH_STATUS_FAILURE

```
const val LAST_FETCH_STATUS_FAILURE = 1: Int
```

Indicates that the most recent attempt to fetch parameter values from the Firebase Remote Config server has failed.

### LAST_FETCH_STATUS_NO_FETCH_YET

```
const val LAST_FETCH_STATUS_NO_FETCH_YET = 0: Int
```

Indicates that the FirebaseRemoteConfig singleton object has not yet attempted to fetch parameter values from the Firebase Remote Config server.

### LAST_FETCH_STATUS_SUCCESS

```
const val LAST_FETCH_STATUS_SUCCESS = -1: Int
```

Indicates that the most recent fetch of parameter values from the Firebase Remote Config server was completed successfully.

### LAST_FETCH_STATUS_THROTTLED

```
const val LAST_FETCH_STATUS_THROTTLED = 2: Int
```

Indicates that the most recent attempt to fetch parameter values from the Firebase Remote Config server was throttled.

### VALUE_SOURCE_DEFAULT

```
const val VALUE_SOURCE_DEFAULT = 1: Int
```

Indicates that the value returned was retrieved from the defaults set by the client.

### VALUE_SOURCE_REMOTE

```
const val VALUE_SOURCE_REMOTE = 2: Int
```

Indicates that the value returned was retrieved from the Firebase Remote Config server.

### VALUE_SOURCE_STATIC

```
const val VALUE_SOURCE_STATIC = 0: Int
```

Indicates that the value returned is the static default value.

## Public functions

### activate

```
fun activate(): Task<Boolean!>
```

Asynchronously activates the most recently fetched configs, so that the fetched key value pairs take effect.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html!>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` with a `true` result if the current call activated the fetched configs; if the fetched configs were already activated by a previous call, it instead returns a `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` with a `false` result. |

### addOnConfigUpdateListener

```
fun addOnConfigUpdateListener(configUpdateListener: ConfigUpdateListener): ConfigUpdateListenerRegistration
```

Starts listening for real-time config updates from the Remote Config backend and automatically fetches updates from the RC backend when they are available.

If a connection to the Remote Config backend is not already open, calling this method will open it. Multiple listeners can be added by calling this method again, but subsequent calls re-use the same connection to the backend.

Note: Real-time Remote Config requires the Firebase Remote Config Realtime API. See the [Remote Config Get Started](https://firebase.google.com/docs/remote-config/get-started?platform=android#add-real-time-listener) guide to enable the API.

| Parameters |
|---|---|
| `configUpdateListener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListener` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListener` that can be used to respond to config updates when they're fetched. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListenerRegistration` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListenerRegistration` that allows you to remove the added ` configUpdateListener` and close the connection when there are no more listeners. |

### ensureInitialized

```
fun ensureInitialized(): Task<FirebaseRemoteConfigInfo!>
```

Returns a `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` representing the initialization status of this Firebase Remote Config instance.

### fetch

```
fun fetch(): Task<Void!>
```

Starts fetching configs, adhering to the default minimum fetch interval.

The fetched configs only take effect after the next `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#activate()` call.

Depending on the time elapsed since the last fetch from the Firebase Remote Config backend, configs are either served from local storage, or fetched from the backend. The default minimum fetch interval can be set with `
FirebaseRemoteConfigSettings.Builder#setMinimumFetchIntervalInSeconds(long)`; the static default is 12 hours.

Note: Also initializes the Firebase installations SDK that creates installation IDs to identify Firebase installations and periodically sends data to Firebase servers. Remote Config requires installation IDs for Fetch requests. To stop the periodic sync, call `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations#delete()`. Sending a Fetch request after deletion will create a new installation ID for this Firebase installation and resume the periodic sync.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` representing the `fetch` call. |

### fetch

```
fun fetch(minimumFetchIntervalInSeconds: Long): Task<Void!>
```

Starts fetching configs, adhering to the specified minimum fetch interval.

The fetched configs only take effect after the next `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#activate()` call.

Depending on the time elapsed since the last fetch from the Firebase Remote Config backend, configs are either served from local storage, or fetched from the backend.

Note: Also initializes the Firebase installations SDK that creates installation IDs to identify Firebase installations and periodically sends data to Firebase servers. Remote Config requires installation IDs for Fetch requests. To stop the periodic sync, call `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations#delete()`. Sending a Fetch request after deletion will create a new installation ID for this Firebase installation and resume the periodic sync.

| Parameters |
|---|---|
| `minimumFetchIntervalInSeconds: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | If configs in the local storage were fetched more than this many seconds ago, configs are served from the backend instead of local storage. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` representing the `fetch` call. |

### fetchAndActivate

```
fun fetchAndActivate(): Task<Boolean!>
```

Asynchronously fetches and then activates the fetched configs.

If the time elapsed since the last fetch from the Firebase Remote Config backend is more than the default minimum fetch interval, configs are fetched from the backend.

After the fetch is complete, the configs are activated so that the fetched key value pairs take effect.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html!>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` with a `true` result if the current call activated the fetched configs; if no configs were fetched from the backend and the local fetched configs have already been activated, returns a `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` with a `false` result. |

### getAll

```
fun getAll(): (Mutable)Map<String!, FirebaseRemoteConfigValue!>
```

Returns a `https://developer.android.com/reference/kotlin/java/util/Map.html` of Firebase Remote Config key value pairs.

Evaluates the values of the parameters in the following order:

1. The activated value, if the last successful `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#activate()` contained the key.
2. The default value, if the key was set with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setDefaultsAsync(java.util.Map<java.lang.String,java.lang.Object>)`.

### getBoolean

```
fun getBoolean(key: String): Boolean
```

Returns the parameter value for the given key as a `boolean`.

Evaluates the value of the parameter in the following order:

1. The activated value, if the last successful `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#activate()` contained the key, and the value can be converted into a `boolean`.
2. The default value, if the key was set with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setDefaultsAsync(java.util.Map<java.lang.String,java.lang.Object>)`, and the value can be converted into a `boolean`.
3. `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#DEFAULT_VALUE_FOR_BOOLEAN()`.

"1", "true", "t", "yes", "y", and "on" are strings that are interpreted (case insensitive) as `true`, and "0", "false", "f", "no", "n", "off", and empty string are interpreted (case insensitive) as `false`.

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A Firebase Remote Config parameter key with a `boolean` parameter value. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `boolean` representing the value of the Firebase Remote Config parameter with the given key. |

### getDouble

```
fun getDouble(key: String): Double
```

Returns the parameter value for the given key as a `double`.

Evaluates the value of the parameter in the following order:

1. The activated value, if the last successful `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#activate()` contained the key, and the value can be converted into a `double`.
2. The default value, if the key was set with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setDefaultsAsync(java.util.Map<java.lang.String,java.lang.Object>)`, and the value can be converted into a `double`.
3. `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#DEFAULT_VALUE_FOR_DOUBLE()`.

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A Firebase Remote Config parameter key with a `double` parameter value. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` | `double` representing the value of the Firebase Remote Config parameter with the given key. |

### getInfo

```
fun getInfo(): FirebaseRemoteConfigInfo
```

Returns the state of this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` instance as a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo`.

### getInstance

```
java-static fun getInstance(): FirebaseRemoteConfig
```

Returns a singleton instance of Firebase Remote Config.

`https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` uses the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`, throwing an `https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html` if one has not been initialized yet.

Note: Also initializes the Firebase installations SDK that creates installation IDs to identify Firebase installations and periodically sends data to Firebase servers. Remote Config requires installation IDs for Fetch requests. To stop the periodic sync, call `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/FirebaseInstallations#delete()`. Sending a Fetch request after deletion will create a new installation ID for this Firebase installation and resume the periodic sync.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` | A singleton instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` for the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |

### getInstance

```
java-static fun getInstance(app: FirebaseApp): FirebaseRemoteConfig
```

Returns an instance of Firebase Remote Config for the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

### getKeysByPrefix

```
fun getKeysByPrefix(prefix: String): (Mutable)Set<String!>
```

Returns a `https://developer.android.com/reference/kotlin/java/util/Set.html` of all Firebase Remote Config parameter keys with the given prefix.

| Parameters |
|---|---|
| `prefix: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The key prefix to look for. If the prefix is empty, all keys are returned. |

| Returns |
|---|---|
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>` | `https://developer.android.com/reference/kotlin/java/util/Set.html` of Remote Config parameter keys that start with the specified prefix. |

### getLong

```
fun getLong(key: String): Long
```

Returns the parameter value for the given key as a `long`.

Evaluates the value of the parameter in the following order:

1. The activated value, if the last successful `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#activate()` contained the key, and the value can be converted into a `long`.
2. The default value, if the key was set with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setDefaultsAsync(java.util.Map<java.lang.String,java.lang.Object>)`, and the value can be converted into a `long`.
3. `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#DEFAULT_VALUE_FOR_LONG()`.

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A Firebase Remote Config parameter key with a `long` parameter value. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `long` representing the value of the Firebase Remote Config parameter with the given key. |

### getString

```
fun getString(key: String): String
```

Returns the parameter value for the given key as a `https://developer.android.com/reference/kotlin/java/lang/String.html`.

Evaluates the value of the parameter in the following order:

1. The activated value, if the last successful `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#activate()` contained the key.
2. The default value, if the key was set with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setDefaultsAsync(java.util.Map<java.lang.String,java.lang.Object>)`.
3. `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#DEFAULT_VALUE_FOR_STRING()`.

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A Firebase Remote Config parameter key. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://developer.android.com/reference/kotlin/java/lang/String.html` representing the value of the Firebase Remote Config parameter with the given key. |

### getValue

```
fun getValue(key: String): FirebaseRemoteConfigValue
```

Returns the parameter value for the given key as a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue`.

Evaluates the value of the parameter in the following order:

1. The activated value, if the last successful `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#activate()` contained the key.
2. The default value, if the key was set with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setDefaultsAsync(java.util.Map<java.lang.String,java.lang.Object>)`.
3. A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue` that returns the static value for each type.

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A Firebase Remote Config parameter key. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue` representing the value of the Firebase Remote Config parameter with the given key. |

### reset

```
fun reset(): Task<Void!>
```

Deletes all activated, fetched and defaults configs and resets all Firebase Remote Config settings.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/kotlin/java/lang/Void.html!>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` representing the `clear` call. |

### setConfigSettingsAsync

```
fun setConfigSettingsAsync(settings: FirebaseRemoteConfigSettings): Task<Void!>
```

Asynchronously changes the settings for this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` instance.

| Parameters |
|---|---|
| `settings: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings` | The new settings to be applied. |

### setCustomSignals

```
fun setCustomSignals(customSignals: CustomSignals): Task<Void!>
```

Asynchronously changes the custom signals for this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` instance.

Custom signals are subject to limits on the size of key/value pairs and the total number of signals. Any calls that exceed these limits will be discarded. See [Custom Signal Limits](https://firebase.google.com/docs/remote-config/parameters?template_type=client#custom-signal-limits).

| Parameters |
|---|---|
| `customSignals: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals` | The custom signals to set for this instance. - New keys will add new key-value pairs in the custom signals. - Existing keys with new values will update the corresponding signals. - Setting a key's value to `null` will remove the associated signal. |

### setDefaultsAsync

```
fun setDefaultsAsync(defaults: (Mutable)Map<String!, Any!>): Task<Void!>
```

Asynchronously sets default configs using the given `https://developer.android.com/reference/kotlin/java/util/Map.html`.

The values in `defaults` must be one of the following types:

- `byte[]`
- `Boolean`
- `Double`
- `Long`
- `String`

| Parameters |
|---|---|
| `defaults: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>` | `https://developer.android.com/reference/kotlin/java/util/Map.html` of key value pairs representing Firebase Remote Config parameter keys and values. |

### setDefaultsAsync

```
fun setDefaultsAsync(resourceId: @XmlRes Int): Task<Void!>
```

Sets default configs using an XML resource.

| Parameters |
|---|---|
| `resourceId: @https://developer.android.com/reference/kotlin/androidx/annotation/XmlRes.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | Id for the XML resource, which should be in your application's ` res/xml` folder. |

## Extension functions

### get

```
operator fun FirebaseRemoteConfig.get(key: String): FirebaseRemoteConfigValue
```

See FirebaseRemoteConfig#getValue

## Extension properties

### configUpdates

```
val FirebaseRemoteConfig.configUpdates: Flow<ConfigUpdate>
```

Starts listening for config updates from the Remote Config backend and emits `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdate`s via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#addOnConfigUpdateListener(com.google.firebase.remoteconfig.ConfigUpdateListener)` for more information.

- When the returned flow starts being collected, an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListener` will be attached.

- When the flow completes, the listener will be removed. If there are no attached listeners, the connection to the Remote Config backend will be closed.