# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.md.txt

# FirebaseRemoteConfigSettings

# FirebaseRemoteConfigSettings


```
class FirebaseRemoteConfigSettings
```

<br />

*** ** * ** ***

Wraps the settings for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfig` operations.

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder` Builder for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings`. |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings#getMinimumFetchIntervalInSeconds()()` Returns the minimum interval between successive fetches calls in seconds. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings#toBuilder()()` Constructs a builder initialized with the current `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings`. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings#fetchTimeoutInSeconds()` |

## Public functions

### getMinimumFetchIntervalInSeconds

```
fun getMinimumFetchIntervalInSeconds(): Long
```

Returns the minimum interval between successive fetches calls in seconds.

### toBuilder

```
fun toBuilder(): FirebaseRemoteConfigSettings.Builder
```

Constructs a builder initialized with the current `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings`.

## Public properties

### fetchTimeoutInSeconds

```
val fetchTimeoutInSeconds: Long
```