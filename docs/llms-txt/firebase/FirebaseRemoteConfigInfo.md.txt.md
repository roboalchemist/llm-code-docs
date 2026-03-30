# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo.md.txt

# FirebaseRemoteConfigInfo

# FirebaseRemoteConfigInfo


```
public interface FirebaseRemoteConfigInfo
```

<br />

*** ** * ** ***

Wraps the current state of the `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig` singleton object.

## Summary

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo#getConfigSettings()()` Gets the current settings of the `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig` singleton object. |
| `abstract long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo#getFetchTimeMillis()()` Gets the timestamp (milliseconds since epoch) of the last successful fetch, regardless of whether the fetch was activated or not. |
| `abstract int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo#getLastFetchStatus()()` Gets the status of the most recent fetch attempt. |

## Public methods

### getConfigSettings

```
abstract @NonNull FirebaseRemoteConfigSettings getConfigSettings()
```

Gets the current settings of the `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig` singleton object.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings` object indicating the current settings. |

### getFetchTimeMillis

```
abstract long getFetchTimeMillis()
```

Gets the timestamp (milliseconds since epoch) of the last successful fetch, regardless of whether the fetch was activated or not.

| Returns |
|---|---|
| `long` | -1 if no fetch attempt has been made yet. Otherwise, returns the timestamp of the last successful fetch operation. |

### getLastFetchStatus

```
abstract int getLastFetchStatus()
```

Gets the status of the most recent fetch attempt.

| Returns |
|---|---|
| `int` | Will return one of `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#LAST_FETCH_STATUS_SUCCESS()`, `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#LAST_FETCH_STATUS_FAILURE()`, `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#LAST_FETCH_STATUS_THROTTLED()`, or `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#LAST_FETCH_STATUS_NO_FETCH_YET()`. |