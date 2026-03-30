# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdateListener.md.txt

# ConfigUpdateListener

# ConfigUpdateListener


```
public interface ConfigUpdateListener
```

<br />

*** ** * ** ***

Event listener interface for real-time Remote Config updates. Implement `
ConfigUpdateListener` to call `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#addOnConfigUpdateListener(com.google.firebase.remoteconfig.ConfigUpdateListener)`.

## Summary

| ### Public methods |
|---|---|
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdateListener#onError(com.google.firebase.remoteconfig.FirebaseRemoteConfigException)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException error)` Callback for when an error occurs while listening for updates or fetching the latest version of the config. |
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdateListener#onUpdate(com.google.firebase.remoteconfig.ConfigUpdate)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdate configUpdate)` Callback for when a new config version has been automatically fetched from the backend and has changed from the activated config. |

## Public methods

### onError

```
abstract void onError(@NonNull FirebaseRemoteConfigException error)
```

Callback for when an error occurs while listening for updates or fetching the latest version of the config.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException error` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException` with information about the error. |

### onUpdate

```
abstract void onUpdate(@NonNull ConfigUpdate configUpdate)
```

Callback for when a new config version has been automatically fetched from the backend and has changed from the activated config.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdate configUpdate` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdate` with information about the updated config version, including the set of updated parameters. |