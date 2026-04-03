# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo.md.txt

# FirebaseRemoteConfigInfo

# FirebaseRemoteConfigInfo


```
interface FirebaseRemoteConfigInfo
```

<br />

*** ** * ** ***

Wraps the current state of the [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig) singleton object.

## Summary

|                                                              ### Public functions                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseRemoteConfigSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings) | [getConfigSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo#getConfigSettings())`()` Gets the current settings of the [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig) singleton object. |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)                                                                    | [getFetchTimeMillis](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo#getFetchTimeMillis())`()` Gets the timestamp (milliseconds since epoch) of the last successful fetch, regardless of whether the fetch was activated or not.                                                |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                      | [getLastFetchStatus](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo#getLastFetchStatus())`()` Gets the status of the most recent fetch attempt.                                                                                                                                |

## Public functions

### getConfigSettings

```
funÂ getConfigSettings():Â FirebaseRemoteConfigSettings
```

Gets the current settings of the [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig) singleton object.  

|                                                                     Returns                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseRemoteConfigSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings) | A [FirebaseRemoteConfigSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings) object indicating the current settings. |

### getFetchTimeMillis

```
funÂ getFetchTimeMillis():Â Long
```

Gets the timestamp (milliseconds since epoch) of the last successful fetch, regardless of whether the fetch was activated or not.  

|                                   Returns                                    |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | -1 if no fetch attempt has been made yet. Otherwise, returns the timestamp of the last successful fetch operation. |

### getLastFetchStatus

```
funÂ getLastFetchStatus():Â Int
```

Gets the status of the most recent fetch attempt.  

|                                  Returns                                   |
|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | Will return one of [LAST_FETCH_STATUS_SUCCESS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#LAST_FETCH_STATUS_SUCCESS()), [LAST_FETCH_STATUS_FAILURE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#LAST_FETCH_STATUS_FAILURE()), [LAST_FETCH_STATUS_THROTTLED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#LAST_FETCH_STATUS_THROTTLED()), or [LAST_FETCH_STATUS_NO_FETCH_YET](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig#LAST_FETCH_STATUS_NO_FETCH_YET()). |