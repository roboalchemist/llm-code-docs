# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdateListener.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListener.md.txt

# ConfigUpdateListener

# ConfigUpdateListener


```
interface ConfigUpdateListener
```

<br />

*** ** * ** ***

Event listener interface for real-time Remote Config updates. Implement `
ConfigUpdateListener` to call [addOnConfigUpdateListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#addOnConfigUpdateListener(com.google.firebase.remoteconfig.ConfigUpdateListener)).

## Summary

|                             ### Public functions                             |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [onError](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListener#onError(com.google.firebase.remoteconfig.FirebaseRemoteConfigException))`(error: `[FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException)`)` Callback for when an error occurs while listening for updates or fetching the latest version of the config. |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [onUpdate](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdateListener#onUpdate(com.google.firebase.remoteconfig.ConfigUpdate))`(configUpdate: `[ConfigUpdate](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdate)`)` Callback for when a new config version has been automatically fetched from the backend and has changed from the activated config.                     |

## Public functions

### onError

```
funÂ onError(error:Â FirebaseRemoteConfigException):Â Unit
```

Callback for when an error occurs while listening for updates or fetching the latest version of the config.  

|                                                                         Parameters                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `error: `[FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) | A [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) with information about the error. |

### onUpdate

```
funÂ onUpdate(configUpdate:Â ConfigUpdate):Â Unit
```

Callback for when a new config version has been automatically fetched from the backend and has changed from the activated config.  

|                                                           Parameters                                                            |
|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `configUpdate: `[ConfigUpdate](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdate) | A [ConfigUpdate](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/ConfigUpdate) with information about the updated config version, including the set of updated parameters. |