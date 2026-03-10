# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListener.md.txt

# ConfigUpdateListener

# ConfigUpdateListener


```
interface ConfigUpdateListener
```

<br />

*** ** * ** ***

Event listener interface for real-time Remote Config updates. Implement `
ConfigUpdateListener` to call `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#addOnConfigUpdateListener(com.google.firebase.remoteconfig.ConfigUpdateListener)`.

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListener#onError(com.google.firebase.remoteconfig.FirebaseRemoteConfigException)(error: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException)` Callback for when an error occurs while listening for updates or fetching the latest version of the config. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListener#onUpdate(com.google.firebase.remoteconfig.ConfigUpdate)(configUpdate: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdate)` Callback for when a new config version has been automatically fetched from the backend and has changed from the activated config. |

## Public functions

### onError

```
fun onError(error: FirebaseRemoteConfigException): Unit
```

Callback for when an error occurs while listening for updates or fetching the latest version of the config.

| Parameters |
|---|---|
| `error: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException` with information about the error. |

### onUpdate

```
fun onUpdate(configUpdate: ConfigUpdate): Unit
```

Callback for when a new config version has been automatically fetched from the backend and has changed from the activated config.

| Parameters |
|---|---|
| `configUpdate: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdate` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdate` with information about the updated config version, including the set of updated parameters. |