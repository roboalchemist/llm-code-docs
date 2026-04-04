# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/package-summary.md.txt

# com.google.firebase.remoteconfig

# com.google.firebase.remoteconfig

## Interfaces

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdateListener` | Event listener interface for real-time Remote Config updates. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdateListenerRegistration` | Listener registration returned by `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#addOnConfigUpdateListener(com.google.firebase.remoteconfig.ConfigUpdateListener)`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo` | Wraps the current state of the `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig` singleton object. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigValue` | Wrapper for a Remote Config parameter value, with methods to get it as different types. |

## Classes

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdate` | Information about the updated config passed to `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/ConfigUpdateListener#onUpdate(com.google.firebase.remoteconfig.ConfigUpdate)`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals` | A container type to represent key/value pairs of heterogeneous types to be set as custom signals in `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setCustomSignals(com.google.firebase.remoteconfig.CustomSignals)`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals.Builder` | Builder for constructing `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals` instances. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig` | Entry point for the Firebase Remote Config API. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings` | Wraps the settings for `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig` operations. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder` | Builder for a `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/RemoteConfigKt` |   |

## Enums

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException.Code` |   |

## Exceptions

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigClientException` | A Firebase Remote Config internal issue that isn't caused by an interaction with the Firebase Remote Config server. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigException` | Base class for `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig` exceptions. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchThrottledException` | An exception thrown when a `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#fetch()` call is throttled. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigServerException` | A Firebase Remote Config internal issue caused by an interaction with the Firebase Remote Config server. |