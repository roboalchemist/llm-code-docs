# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/package-summary.md.txt

# com.google.firebase.remoteconfig

# com.google.firebase.remoteconfig

## Interfaces

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListener` | Event listener interface for real-time Remote Config updates. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListenerRegistration` | Listener registration returned by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#addOnConfigUpdateListener(com.google.firebase.remoteconfig.ConfigUpdateListener)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo` | Wraps the current state of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` singleton object. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue` | Wrapper for a Remote Config parameter value, with methods to get it as different types. |

## Classes

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdate` | Information about the updated config passed to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListener#onUpdate(com.google.firebase.remoteconfig.ConfigUpdate)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals` | A container type to represent key/value pairs of heterogeneous types to be set as custom signals in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setCustomSignals(com.google.firebase.remoteconfig.CustomSignals)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder` | Builder for constructing `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals` instances. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` | Entry point for the Firebase Remote Config API. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings` | Wraps the settings for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` operations. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder` | Builder for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings`. |

## Exceptions

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigClientException` | A Firebase Remote Config internal issue that isn't caused by an interaction with the Firebase Remote Config server. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException` | Base class for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` exceptions. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchThrottledException` | An exception thrown when a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#fetch()` call is throttled. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException` | A Firebase Remote Config internal issue caused by an interaction with the Firebase Remote Config server. |

## Enums

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code` |   |

## Top-level functions summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/package-summary#customSignals(kotlin.Function1)(builder: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/package-summary#remoteConfigSettings(kotlin.Function1)(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |

## Extension functions summary

|---|---|
| `operator https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/package-summary#(com.google.firebase.remoteconfig.FirebaseRemoteConfig).get(kotlin.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` See FirebaseRemoteConfig#getValue |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/package-summary#(com.google.firebase.Firebase).remoteConfig(com.google.firebase.FirebaseApp)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |

## Extension properties summary

|---|---|
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdate>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/package-summary#(com.google.firebase.remoteconfig.FirebaseRemoteConfig).configUpdates()` Starts listening for config updates from the Remote Config backend and emits `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdate`s via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/package-summary#(com.google.firebase.Firebase).remoteConfig()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |

## Top-level functions

### customSignals

```
fun customSignals(builder: CustomSignals.Builder.() -> Unit): CustomSignals
```

### remoteConfigSettings

```
fun remoteConfigSettings(init: FirebaseRemoteConfigSettings.Builder.() -> Unit): FirebaseRemoteConfigSettings
```

## Extension functions

### get

```
operator fun FirebaseRemoteConfig.get(key: String): FirebaseRemoteConfigValue
```

See FirebaseRemoteConfig#getValue

### remoteConfig

```
fun Firebase.remoteConfig(app: FirebaseApp): FirebaseRemoteConfig
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

## Extension properties

### configUpdates

```
val FirebaseRemoteConfig.configUpdates: Flow<ConfigUpdate>
```

Starts listening for config updates from the Remote Config backend and emits `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdate`s via a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html`. See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#addOnConfigUpdateListener(com.google.firebase.remoteconfig.ConfigUpdateListener)` for more information.

- When the returned flow starts being collected, an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListener` will be attached.

- When the flow completes, the listener will be removed. If there are no attached listeners, the connection to the Remote Config backend will be closed.

### remoteConfig

```
val Firebase.remoteConfig: FirebaseRemoteConfig
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.