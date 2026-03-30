# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo.md.txt

# FirebaseRemoteConfigInfo

# FirebaseRemoteConfigInfo


```
interface FirebaseRemoteConfigInfo
```

<br />

*** ** * ** ***

Wraps the current state of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` singleton object.

## Summary

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo#getConfigSettings()()` Gets the current settings of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` singleton object. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo#getFetchTimeMillis()()` Gets the timestamp (milliseconds since epoch) of the last successful fetch, regardless of whether the fetch was activated or not. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo#getLastFetchStatus()()` Gets the status of the most recent fetch attempt. |

## Public functions

### getConfigSettings

```
fun getConfigSettings(): FirebaseRemoteConfigSettings
```

Gets the current settings of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` singleton object.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings` object indicating the current settings. |

### getFetchTimeMillis

```
fun getFetchTimeMillis(): Long
```

Gets the timestamp (milliseconds since epoch) of the last successful fetch, regardless of whether the fetch was activated or not.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | -1 if no fetch attempt has been made yet. Otherwise, returns the timestamp of the last successful fetch operation. |

### getLastFetchStatus

```
fun getLastFetchStatus(): Int
```

Gets the status of the most recent fetch attempt.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | Will return one of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#LAST_FETCH_STATUS_SUCCESS()`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#LAST_FETCH_STATUS_FAILURE()`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#LAST_FETCH_STATUS_THROTTLED()`, or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#LAST_FETCH_STATUS_NO_FETCH_YET()`. |